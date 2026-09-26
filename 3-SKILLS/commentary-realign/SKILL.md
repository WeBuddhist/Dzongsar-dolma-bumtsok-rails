---
name: commentary-realign
description: >
  Make a copy of a commentary that is aligned to one root text, re-aligned to a
  second root text that contains the same root passages (possibly several
  times), by carrying the existing alignment across: every transcluded root
  block is matched to all of its occurrences in the new root, the copy's
  transclusions are re-pointed there, its frontmatter is re-pointed and cleared
  of the old live ids and given a new unique title, the result is verified
  against the old alignment, and the old file is deleted. Dry-run by default.

  Trigger this skill when the user says: "align this commentary to the other
  root", "migrate the alignment to the Zabtig text", "re-align the commentary to
  a new root text", "the root passage appears three times — point the
  commentary at all of them", "re-upload the commentary as a commentary of
  another root".
profile: rails-vault
---

# commentary-realign

The library lets a commentary be aligned to **one** root text only. When the same root passage also lives inside a second root text — the Praise to the Twenty-One Tārās (`bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།`) is recited three times inside the Zabtig Drolchok ritual (`bo-ཟབ་ཏིག་སྒྲོལ་ཆོག`) — the commentary has to be uploaded again as a new commentary of the second root. This skill builds that copy from the alignment the commentary already has, instead of re-aligning it by hand.

Correct output is a copy that differs from the original **only** in its transclusion lines and its frontmatter; whose alignment (as `parser-commentary` reads it) is exactly the old alignment carried through the block map; in which every commentary block that pointed at a repeated root passage now points at every occurrence of it; and that carries no live id of the original, so `commentary-upload` creates a new text instead of touching the old one.

---

## Inputs

| Input | Description | Required |
|---|---|---|
| **Commentary** | A `1-SOURCES/Commentaries/` file with `file_type: commentary`, `root_text:` set, and its root passages transcluded (`![[<root>#^ref]]`) | yes |
| **New root** | The root text to align to, in `1-SOURCES/Text/`, with block IDs; it should carry `text_id` (uploaded) so `commentary_of` can be set | yes |
| **New title** | A title for the copy that is not already a title or alt title of any text in the same language on the library (titles are unique per language; the original keeps its titles) | yes, for `--write` |
| **Overrides** | Optional JSON `{"<old ref>": ["<new ref>", …]}` replacing the automatic matches for those refs (`[]` = leave unaligned) | no |

If the new title is not given, stop and ask for it. Do not invent one without the human's approval.

## Output

| Path | What |
|---|---|
| `1-SOURCES/Commentaries/<old stem>-<new root name>.md` (or `--out`) | The re-aligned copy |
| `0-INBOX/temp/commentary-realign/<old stem>.mapping.json` | The block map with scores, for review and for building overrides |
| the old commentary file | Deleted after verification passes (`--delete-old`) |

---

## Output file format

Body: identical to the original except each transclusion of the old root:

```markdown
![[1-SOURCES/Text/<old-root>.md#^1-1]]
```

becomes one line per occurrence in the new root, written as one group so the parser aligns the commentary blocks beneath it to all of them:

```markdown
![[1-SOURCES/Text/<new-root>.md#^1-64]]

![[1-SOURCES/Text/<new-root>.md#^1-98]]

![[1-SOURCES/Text/<new-root>.md#^1-132]]
```

A root block with **no** counterpart in the new root keeps its transclusion of the old root. `parser-commentary` reads a transclusion of any file other than `root_text` as a scope break with no target, so the commentary on it is left unaligned rather than paired with a same-numbered block of the new root.

Frontmatter, changes only:

```yaml
title: <new unique title>
root_text: 1-SOURCES/Text/<new-root>.md
commentary_of: <new root text_id>
covers_verses: <first target>–<last target>
source_description: "<original> Re-aligned copy for <new root>: … The original remains live as a commentary of <old root> (text <old text_id>)."
realigned_from: 1-SOURCES/Commentaries/<old file>.md
realigned_from_text_id: <old text_id>
realigned_from_edition_id: <old edition_id>
realigned_from_root_text: 1-SOURCES/Text/<old-root>.md
# removed: text_id, edition_id, toc_id, aligned_to_edition_id, alt_titles
```

`alt_titles` are dropped because the original already claims them on the library (titles and alt titles are unique per language, and a claimed alt title cannot be removed); pass `--keep-alt-titles` only for alt titles that are new.

---

## Rules

1. **Dry run first, always.** Read the block map before writing. Every ref must have the expected number of targets (for the Zabtig ritual: 3 for the homage, the 21 verses and the closing line; 1 for each benefit verse). A `⚠ close call` (accepted score within 0.15 of the best rejected block) or an unexpected count must be settled with an `--map` override, never by lowering the threshold blindly.
2. **Only transclusion lines and frontmatter change.** The script verifies this and refuses to delete the old file if anything else differs. Never hand-edit the commentary text in this skill.
3. **The copy's alignment must equal the old alignment mapped through the block map.** Verified with `parser-commentary` on both files; a mismatch stops the run.
4. **Never carry live ids over.** `text_id`, `edition_id`, `toc_id`, `aligned_to_edition_id` belong to the original's live text; the copy gets its own from `commentary-upload`.
5. **Never reuse a title.** The new title must differ from the original's title and alt titles.
6. **The original on the library is untouched.** This skill deletes the old *file* only; the live text stays a commentary of the old root. Deleting anything on the library is not part of this skill.
7. **Uploading is a separate step.** Run `commentary-upload` on the copy (dry run, then `--execute` only after explicit human confirmation).
8. **Translations of the commentary are not re-pointed here.** After `--delete-old` the script lists every file that still names the old file; handle those as a follow-up with the human.

---

## Procedure

1. **Dry run** from the vault root:
   ```bash
   python3 3-SKILLS/commentary-realign/scripts/realign_commentary.py "<commentary.md>" --new-root "<new-root.md>" --title "<new title>"
   ```
   Read the table: old ref, number of targets, targets with scores, best rejected block. Check the counts against the structure of the new root.
2. **Settle any doubt** by writing overrides to a JSON file (start from `0-INBOX/temp/commentary-realign/<stem>.mapping.json`) and re-running with `--map <file>`.
3. **Confirm the new title** with the human if they have not given it.
4. **Write and verify**:
   ```bash
   python3 3-SKILLS/commentary-realign/scripts/realign_commentary.py "<commentary.md>" --new-root "<new-root.md>" --title "<new title>" --write --delete-old
   ```
   The script writes the copy, checks that only transclusion lines changed and that the alignment is the mapped old alignment, and only then deletes the old file. It prints the files that still name the old file.
5. **Dry-run the upload** of the copy with `commentary-upload` and read it back: lint clean, `commentary_of` = the new root's `text_id`, the expected pair count, no title clash.
6. **Report** to the human: the block map summary, pair counts old → new, commentary blocks left unaligned, the files that still name the old file, and the upload dry run. Upload only on an explicit yes.

---

## Completion check

- [ ] Dry run read: every old ref has the expected number of targets; no unexplained close call or unmapped ref
- [ ] New title confirmed and distinct from the original's title and alt titles
- [ ] Copy written; verification `OK` (only transclusion lines changed; alignment = mapped old alignment)
- [ ] Copy frontmatter: new `root_text`, `commentary_of`, `covers_verses`; no `text_id`/`edition_id`/`toc_id`/`aligned_to_edition_id`; `realigned_from*` recorded
- [ ] Old file deleted only after verification passed
- [ ] Files still naming the old file reported to the human
- [ ] `commentary-upload` dry run of the copy passes
