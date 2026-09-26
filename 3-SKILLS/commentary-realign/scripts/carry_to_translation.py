#!/usr/bin/env python3
"""Carry a re-aligned commentary's root transclusions into one of its translations.

A translation of a commentary (same block IDs, each block transcluding its
source block: ``![[<source commentary>#^X]]``) is uploaded as its own
commentary of the root, like every commentary in this vault. Once the source
commentary has been re-aligned with realign_commentary.py, this script makes a
copy of the translation that follows it:

  1. read the re-aligned source's alignment with parser-commentary
     (source block -> root blocks, all occurrences)
  2. before every ``![[<old source>#^X]]`` insert the root transclusions of
     block X, in the same transclusion group, and re-point the source
     transclusion to the re-aligned source file (it stays for reading; the
     parser gives targets only for root_text transclusions)
  3. turn the frontmatter into that of a commentary of the new root: new
     title, file_type commentary, root_text, commentary_of, covers_verses,
     a link to the source edition; the old live ids and translation_of* go
  4. verify: the copy's alignment equals the source's alignment restricted to
     the translation's blocks, and nothing but transclusion lines changed

Dry run by default.

Usage (from the vault root):
  python3 3-SKILLS/commentary-realign/scripts/carry_to_translation.py "<translation.md>" \\
      --source "<re-aligned commentary.md>" --title "<new unique title>"   # dry run
  ... --write [--delete-old]
"""
from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from realign_commentary import (  # noqa: E402
    LIVE_ID_KEYS, TRANS_LINE_RE, alignment_pairs, content_blocks, delete_and_report,
    edit_frontmatter, load_parser, non_transclusion_lines, note_name, read_note, resolve,
    vault_rel,
)

TRANSLATION_KEYS = ("translation_of", "translation_of_text_id", "translation_of_edition_id")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("translation", type=pathlib.Path)
    ap.add_argument("--source", required=True, type=pathlib.Path,
                    help="the re-aligned source commentary (written by realign_commentary.py)")
    ap.add_argument("--title", help="new title, unique in its language on the library")
    ap.add_argument("--out", type=pathlib.Path)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--delete-old", action="store_true")
    args = ap.parse_args(argv)

    old_path = args.translation.resolve()
    src_path = args.source.resolve()
    fm, text, fm_match = read_note(old_path)
    src_fm, src_text, src_m = read_note(src_path)
    if not src_fm.get("realigned_from"):
        sys.exit(f"{src_path.name} has no realigned_from: run realign_commentary.py on it first")
    root = resolve(src_fm.get("root_text", ""), src_path)
    if not root:
        sys.exit(f"source root_text {src_fm.get('root_text')!r} does not resolve")
    root_fm, root_text, rm = read_note(root)
    root_order = list(content_blocks(root_text[rm.end():]))
    root_link = vault_rel(root)

    # old and new names the translation may use for its source commentary
    old_src_name = note_name(src_fm["realigned_from"])
    src_names = {old_src_name, note_name(src_path.name)}

    parser = load_parser()
    src_pairs = alignment_pairs(parser, src_path)
    src_map = {}
    for s, t in src_pairs:
        src_map.setdefault(s, []).append(t)
    for s in src_map:
        src_map[s].sort(key=root_order.index)

    body = text[fm_match.end():]
    out_lines, carried, bare, seen = [], 0, [], []
    for line in body.split("\n"):
        m = TRANS_LINE_RE.match(line)
        if not (m and note_name(m["file"]) in src_names):
            out_lines.append(line)
            continue
        ref, ind = m["ref"], m["indent"]
        seen.append(ref)
        # keep the link style the file already uses (short name or full path)
        src_link = src_path.stem if "/" not in m["file"] else vault_rel(src_path)
        group = [f"{ind}![[{root_link}#^{t}]]" for t in src_map.get(ref, [])]
        group.append(f"{ind}![[{src_link}#^{ref}]]")
        out_lines.append("\n\n".join(group))
        if src_map.get(ref):
            carried += 1
        else:
            bare.append(ref)
    new_body = "\n".join(out_lines)

    tr_blocks = set(content_blocks(body))
    src_blocks = set(content_blocks(src_text[src_m.end():]))
    missing_in_src = sorted(set(seen) - src_blocks)
    untranscluded = sorted(tr_blocks - set(seen))

    sets = {
        "title": args.title or fm.get("title"),
        "file_type": "commentary",
        "root_text": root_link,
        "covers_verses": src_fm.get("covers_verses", ""),
        ("tibetan_edition" if src_fm.get("lang_tag") == "bo" else "source_edition"): vault_rel(src_path),
        "realigned_from": vault_rel(old_path),
        "realigned_from_text_id": fm.get("text_id", ""),
        "realigned_from_edition_id": fm.get("edition_id", ""),
    }
    if "title_original" in fm:
        sets["title_original"] = src_fm.get("title")
    if root_fm.get("text_id"):
        sets["commentary_of"] = root_fm["text_id"]
    drops = set(LIVE_ID_KEYS) | set(TRANSLATION_KEYS) | {"alt_titles"}
    new_fm = edit_frontmatter(fm_match.group(1), sets, drops)
    out_text = f"---\n{new_fm}\n---\n{new_body}"

    stem_tail = old_path.stem[len(old_src_name[:-3]):] if old_path.stem.startswith(old_src_name[:-3]) else f"-{old_path.stem}"
    out_path = (args.out or old_path.with_name(f"{src_path.stem}{stem_tail}.md")).resolve()

    print(f"translation: {vault_rel(old_path)}")
    print(f"source     : {vault_rel(src_path)}  ({len(src_pairs)} pairs -> {root.name})")
    print(f"copy       : {vault_rel(out_path)}")
    print(f"  source transclusions: {len(seen)}; given root targets: {carried}; "
          f"none (unaligned in the source too): {bare or 'none'}")
    print(f"  blocks not in the source: {missing_in_src or 'none'}; "
          f"blocks with no source transclusion: {untranscluded or 'none'}")
    print(f"  title      : {sets['title']}" + ("" if args.title else "   ⚠ unchanged — pass --title"))
    print(f"  dropped    : {sorted(k for k in drops if k in fm)}")
    if not args.write:
        print("\nDRY RUN — nothing written. Re-run with --write.")
        return 0
    if not args.title:
        sys.exit("refusing to write without --title: the old title is already taken on the library")
    if out_path == old_path or out_path.exists():
        sys.exit(f"{out_path.name}: must be a new file")
    out_path.write_text(out_text, encoding="utf-8")
    print(f"  WROTE {vault_rel(out_path)}")

    problems = []
    if non_transclusion_lines(body) != non_transclusion_lines(new_body):
        problems.append("text other than transclusion lines changed")
    expected = {(s, t) for s, t in src_pairs if s in tr_blocks}
    actual = alignment_pairs(parser, out_path)
    if actual != expected:
        problems.append(f"alignment differs from the source's: missing {sorted(expected - actual)[:6]}, "
                        f"extra {sorted(actual - expected)[:6]}")
    print(f"\nverify: source {len(src_pairs)} pairs; copy {len(actual)} pairs "
          f"({len({s for s, _ in actual})} blocks -> {len({t for _, t in actual})} root blocks)")
    if problems:
        for p in problems:
            print(f"  FAIL {p}")
        print("  the old file was NOT deleted")
        return 1
    print("  OK  alignment = the source's alignment on the same blocks; only transclusion lines changed")
    if args.delete_old:
        delete_and_report(old_path, out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
