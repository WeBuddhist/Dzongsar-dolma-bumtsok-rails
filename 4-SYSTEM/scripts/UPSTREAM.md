# Vendored code in this folder

## `strip_small_print.py` — `adjust_span_for_delete()`

That one function is the backend's own span arithmetic, not a re-reading of it,
so that the simulation this script runs before it offers to write is the
server's behaviour rather than our model of it.

| | |
|---|---|
| Source repository | `webuddhist-library/openpecha-backend` |
| Path | `database/span_database.py`, lines 11–101 |
| Pinned at | commit `cd1c205` (2026-09-04) |
| Reached here via | `Liturgy-rails/4-SYSTEM/scripts/content_patch_payloads.py`, which vendored it first |
| Vendored | 2026-09-24 |

Only the delete case is carried over. `strip_small_print.py` refuses to run on
anything that is not deletion-only, so the insert and replace arithmetic in the
upstream file is deliberately not copied — code that cannot be exercised here
would rot unnoticed.

A Segment line span is a "continuous" span in the upstream vocabulary; a TOC
section span is an "annotation" span. This script only ever touches the former.

**If the backend changes its span arithmetic, this copy is wrong and the
script's safety check silently becomes a check of the old behaviour.** Re-pin
it against the upstream file before trusting a run after any backend upgrade.

The rest of `content_patch_payloads.py` was not copied: it solves a harder
problem (arbitrary expert edits diffed between `1-SOURCES/` and `0-INBOX/`,
with insert/replace support and its own report format). Our case is one
deletion-only pass over two editions, so a smaller script that fails loudly on
anything else is easier to be sure of. If this vault later needs the general
case, take that script rather than growing this one.
