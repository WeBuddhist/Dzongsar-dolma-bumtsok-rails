#!/usr/bin/env python3
"""Remove `<small>`/`</small>` markers from a published edition's content, in
place, without moving a single segment boundary.

The markers came in with the source as received and were published with it.
Stripping them from the vault file is not enough: the backend holds its own
copy of the content, and every segment is a character span into that copy. So
the same deletion has to be replayed against the backend, and the spans have to
survive it.

    PATCH /v2/editions/{id}/content   {"type": "delete", "start": N, "end": M}

One operation per call, **highest position first**. Each op's offsets are
stated against the content as it is on the backend now; applying them from the
bottom up keeps every earlier offset valid, so nothing has to be recomputed
between calls and an interrupted run can simply be re-run.

Why not one whole-content replace: the backend's span arithmetic collapses
every span a replace fully encompasses onto the replacement, so replacing
[0, len) would flatten all 424 segments into one. Targeted deletes are the only
shape that leaves the segmentation intact.

Safety: this never calls a mutating endpoint without `--execute`, and before it
offers to, it proves the result. It replays the backend's own span arithmetic
over the live spans, then compares the predicted spans — char for char, by the
text they select — against a fresh parse of the cleaned vault file. If the two
disagree anywhere, nothing is sent.

Usage (from the vault root):

    set -a; source 4-SYSTEM/scripts/.env; set +a
    python3 4-SYSTEM/scripts/strip_small_print.py <cleaned note>            # dry run
    python3 4-SYSTEM/scripts/strip_small_print.py <cleaned note> --execute
    python3 4-SYSTEM/scripts/strip_small_print.py <cleaned note> --verify

The note must already have its markers removed and must carry `edition_id` in
its frontmatter. Env: WEBUDDHIST_API_KEY, WEBUDDHIST_APP (default
"webuddhist"), WEBUDDHIST_API_BASE.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

VAULT = pathlib.Path(__file__).resolve().parents[2]
BASE = os.environ.get("WEBUDDHIST_API_BASE", "https://library.webuddhist.com").rstrip("/")
MARKERS = ("<small>", "</small>")


# ---------------------------------------------------------------------------
# The backend's own span arithmetic for a delete, vendored so the simulation is
# the server's and not a re-reading of it. See UPSTREAM.md beside this file.
# ---------------------------------------------------------------------------

def adjust_span_for_delete(start, end, del_start, del_end):
    del_len = del_end - del_start
    if del_end <= start:
        return (start - del_len, end - del_len)
    if del_start >= end:
        return (start, end)
    if del_start <= start and del_end >= end:
        return None
    if del_start <= start < del_end < end:
        return (del_start, end - del_len)
    if start < del_start < end <= del_end:
        return (start, del_start)
    if start < del_start and del_end < end:
        return (start, end - del_len)
    return (start, end)


# ---------------------------------------------------------------------------
# api
# ---------------------------------------------------------------------------

def headers():
    h = {"X-Application": os.environ.get("WEBUDDHIST_APP") or "webuddhist"}
    key = os.environ.get("WEBUDDHIST_API_KEY")
    if key:
        h["X-API-Key"] = key
    return h


def call(method, path, body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers())
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:500]


def live_content(edition_id):
    st, d = call("GET", f"/v2/editions/{edition_id}/content")
    if st != 200:
        sys.exit(f"GET content -> {st} {d}")
    return d if isinstance(d, str) else (d.get("content") or "")


def live_spans(edition_id):
    """Every line span in the backend's own order, with a label for reporting."""
    st, d = call("GET", f"/v2/editions/{edition_id}/segmentation/segments")
    if st != 200:
        sys.exit(f"GET segments -> {st} {d}")
    segs = d["items"] if isinstance(d, dict) and "items" in d else d
    spans, labels = [], []
    for s in segs:
        lines = s.get("lines") or ([s["span"]] if s.get("span") else [])
        for i, ln in enumerate(lines):
            spans.append((ln["start"], ln["end"]))
            labels.append(f'^{s.get("reference")}[{i}]')
    return spans, labels


# ---------------------------------------------------------------------------
# the vault side
# ---------------------------------------------------------------------------

def frontmatter(note: pathlib.Path):
    t = note.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m:
        sys.exit(f"{note.name}: no frontmatter")
    out = {}
    for line in m.group(1).split("\n"):
        k = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if k:
            out[k.group(1)] = k.group(2).strip()
    return out


def find_tools():
    for linter in sorted(VAULT.glob("4-SYSTEM/Skills/*/scripts/linter-root-text/lint_text_input.py")):
        parser = linter.parent.parent / "parser-root-text" / "parser.py"
        if parser.exists():
            return linter, parser
    sys.exit("could not find the bundled linter-root-text / parser-root-text")


def fresh_build(note: pathlib.Path):
    """Run the uploader's own lint+parse path over the cleaned note."""
    linter, parser = find_tools()
    r = subprocess.run([sys.executable, str(linter), str(note)], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"{linter.name} failed:\n{r.stdout}\n{r.stderr}")
    lint_json = linter.parent / "output" / (note.stem + ".lint.json")
    if not lint_json.exists():
        sys.exit(f"linter did not write {lint_json}")
    r = subprocess.run([sys.executable, str(parser), str(note), str(lint_json)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"parser failed:\n{r.stdout}\n{r.stderr}")
    edition = json.loads((parser.parent / "output" / (note.stem + ".edition.json")).read_text(encoding="utf-8"))
    spans, labels = [], []
    for s in edition["segmentation"]["segments"]:
        for i, ln in enumerate(s["lines"]):
            spans.append((ln["start"], ln["end"]))
            labels.append(f'^{s["reference"]}[{i}]')
    return edition["content"], spans, labels


# ---------------------------------------------------------------------------
# ops
# ---------------------------------------------------------------------------

def delete_ops(old, new):
    """The minimal operations taking the live content to the cleaned one,
    positions stated against `old`, highest position first.

    Deriving these from a diff rather than from the marker positions matters:
    removing `<small>` also changes how the parser normalises the whitespace
    around it, so a marker-only deletion leaves stray spaces behind and the
    result no longer equals a fresh parse of the note. Anything other than a
    delete means this is not a pure markup removal, and the caller stops.
    """
    ops = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        if tag != "delete":
            sys.exit(f"ABORT: the change is not deletion-only — {tag} at {i1}:{i2} "
                     f"({old[i1:i2]!r} -> {new[j1:j2]!r})")
        ops.append({"type": "delete", "start": i1, "end": i2})
    ops.sort(key=lambda o: o["start"], reverse=True)
    return ops


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("note", help="the vault note, markers already removed")
    ap.add_argument("--execute", action="store_true", help="send the PATCH calls")
    ap.add_argument("--verify", action="store_true", help="GET the live state and exit")
    a = ap.parse_args()

    note = pathlib.Path(a.note).resolve()
    fm = frontmatter(note)
    eid = fm.get("edition_id")
    if not eid:
        sys.exit(f"{note.name}: no edition_id in frontmatter — nothing published to patch")

    live = live_content(eid)
    spans, labels = live_spans(eid)

    if a.verify:
        print(f"edition {eid}: {len(live)} chars, {len(spans)} line spans, "
              f"markers remaining: {sum(live.count(m) for m in MARKERS)}")
        new_text, new_spans, _ = fresh_build(note)
        print(f"vault note: {len(new_text)} chars, {len(new_spans)} line spans")
        print("content matches the note:", live == new_text)
        print("spans match the note:", spans == new_spans)
        return

    print(f"== edition {eid} ==")
    print(f"  live content   : {len(live)} chars, {len(spans)} line spans")
    found = {m: live.count(m) for m in MARKERS}
    print(f"  markers live   : " + ", ".join(f"{m} x{n}" for m, n in found.items()))
    if not sum(found.values()):
        print("  nothing to strip — already clean.")
        return

    new_text, new_spans, new_labels = fresh_build(note)
    ops = delete_ops(live, new_text)
    predicted = list(spans)
    simulated = live
    for op in ops:
        predicted = [None if s is None else adjust_span_for_delete(s[0], s[1], op["start"], op["end"])
                     for s in predicted]
        simulated = simulated[:op["start"]] + simulated[op["end"]:]

    print(f"  operations     : {len(ops)} deletes, descending "
          f"({ops[0]['start']} down to {ops[-1]['start']}), "
          f"{sum(o['end'] - o['start'] for o in ops)} chars removed")

    dropped = [labels[i] for i, s in enumerate(predicted) if s is None]
    if dropped:
        sys.exit(f"ABORT: the backend would drop {len(dropped)} spans, e.g. {dropped[:5]}")

    if simulated != new_text:
        sys.exit("ABORT: the simulated content does not equal a fresh parse of the note")
    if new_labels != labels:
        sys.exit("ABORT: segment references changed between the live edition and the note")

    bad = [(labels[i], predicted[i], new_spans[i])
           for i in range(len(new_spans)) if predicted[i] != new_spans[i]]
    if bad:
        for lbl, p, n in bad[:10]:
            print(f"    {lbl}: replayed {p} != fresh {n}")
        sys.exit(f"ABORT: {len(bad)} spans disagree")

    print(f"  checks         : content matches a fresh parse ✓  "
          f"all {len(new_spans)} spans replay identically ✓  no span dropped ✓")

    if not a.execute:
        print("\ndry run: nothing sent. Re-run with --execute after confirmation.")
        return

    print("\n== EXECUTE ==")
    for n, op in enumerate(ops, 1):
        st, d = call("PATCH", f"/v2/editions/{eid}/content", op)
        if st not in (200, 204):
            sys.exit(f"\nop {n}/{len(ops)} at {op['start']} -> {st} {d}\n"
                     f"Stopped. The ops already applied are the ones above this position; "
                     f"re-running recomputes from the live content and resumes safely.")
        if n % 20 == 0 or n == len(ops):
            print(f"  {n}/{len(ops)} applied")

    after = live_content(eid)
    after_spans, _ = live_spans(eid)
    print(f"\n  after: {len(after)} chars, {len(after_spans)} line spans, "
          f"markers remaining: {sum(after.count(m) for m in MARKERS)}")
    print(f"  equals the vault note: {after == new_text}")
    print(f"  spans equal the note : {after_spans == new_spans}")


if __name__ == "__main__":
    main()
