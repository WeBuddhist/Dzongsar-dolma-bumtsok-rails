---
name: tara-plan-creator
description: Generate one or more days of the 21-Taras day-plan — today's Tara image, name and introduction; the day's praise stanza from the Twenty-One Praises to Tara; and a never-repeating story — in Tibetan, English and Chinese. Trigger whenever the human contributor asks to run Tara-Plan-Creator, build/generate the Tara day-plan(s), or create Day-N Tara Plan for one day, a range of days, or a list of days.
profile: vault-local
creator: Tigerboy
supersedes: none — this is the first formal registration of the ad hoc process that produced the pre-existing bo-21-Day-Plans/Day-1 and Day-2 files
---

# Tara-Plan-Creator

This skill produces the daily plan for the 21-Taras devotional project: one Tara per day, for up to 21 days, each day delivered as three parallel files — Tibetan, English, Chinese — built entirely from existing vault material. Nothing is composed, translated, or paraphrased; every piece of content is either transcluded verbatim from its source file or copied character-for-character. The skill exists so that all three language versions of a given day always agree on which Tara and which story that day carries, and so the same five-heading shape is produced every time, day after day, without drift.

---

## Inputs

Before starting, gather:

| Field | Description |
|---|---|
| `days` | Which day(s) to generate this run — a single day (`Day 4`), a range (`Day 3 to Day 6`), or a list (`Day 1, Day 9, Day 14`). Never generate more than what was asked. Never generate all 21 speculatively. |
| `languages` | Normally all three (Tibetan, English, Chinese). If the human contributor asks for only one or two languages for this run, produce only those — but still resolve `tara_number` and `story_number` the same way (see Rule 4), so a later run for the missing language(s) stays consistent. |

Source material this skill reads (never writes to, except the one-time structural preparation in Rule 6):

| # | Content | Tibetan source | English source | Chinese source |
|---|---|---|---|---|
| 1a | Tara image | `0-INBOX/21-Tara's-Images/21-Surya-Gupta-Taras-Images/` | *(same folder — the image is language-neutral)* | *(same folder)* |
| 1b | Tara name | `0-INBOX/21-Drolma-Introductions/<NN> <Title> (Tibetan).md` | `0-INBOX/21-Drolma-Introductions/<NN> <Title> (English).md` | `0-INBOX/21-Drolma-Introductions/<NN> <Title> (Chinese).md` |
| 1c | Introduction | *(same file as 1b, Tibetan)* | *(same file as 1b, English)* | *(same file as 1b, Chinese)* |
| 2 | Praise stanza | `1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md` | `1-SOURCES/Translations/en-The Twenty-One Praises to Tara.md` | `1-SOURCES/Translations/Zh-The-Twenty-One-Praises-To-Tara.md` |
| 3 | Story | `0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md` | `0-INBOX/Story/en-Khenpo-Tsulnam_Stories.md` | `0-INBOX/Story/zh-Khenpo-Tsulnam_Stories.md` |

If any of these paths does not exist when the skill runs, stop and report exactly which one is missing — do not substitute or invent a location.

---

## Output

Three files per requested day, one per language:

```
3-TRANSFORMATIONS/Plans/bo-21-Day-Plans/Day-<N> Tara Plan.md
3-TRANSFORMATIONS/Plans/en-21-Day-Plans/Day-<N> Tara Plan.md
3-TRANSFORMATIONS/Plans/zh-21-Day-Plans/Day-<N> Tara Plan.md
```

`<N>` is the plain day number (`Day-1 Tara Plan.md`, `Day-2 Tara Plan.md`, … `Day-21 Tara Plan.md`), matching the file names already in use in `bo-21-Day-Plans`.

**Day 1 and Day 2, Tibetan, already exist and predate this skill.** They were built by an earlier, richer format (a full sadhana embed, the complete 21-praises recitation, a video-link section) that this skill does not reproduce — the human contributor's current specification for this skill is the leaner five-heading shape below. Do not silently overwrite those two files with the new shape. If a run is requested for Day 1 or Day 2, stop and ask the human contributor whether to (a) leave the existing Tibetan file untouched and only add the English/Chinese counterparts in the new shape, (b) regenerate the Tibetan file too in the new shape, or (c) skip those two days entirely. For every other day, if a target file already exists, update it in place only if asked — otherwise stop and report the collision rather than overwrite.

---

## Output file format

One file per language, all five sections at heading level `##` (never deeper), in this order: image, name, introduction, praise stanza, story. The bracketed labels below are fixed per language; do not translate them differently between runs.

**Tibetan — `bo-21-Day-Plans/Day-<N> Tara Plan.md`:**

```markdown
---
plan: Tara-Plan-Creator
day: <N>
language: bo
tara_number: <N>
tara_name: "<Tibetan name, exact copy of the intro file's title line>"
story_number: <M>
generation_date: <YYYY-MM-DD>
status: draft
---

# ཉིན་<N>་པའི་སྒྲོལ་མའི་གྲོས་འཆར།

## སྐུ་བརྙན

![[0-INBOX/21-Tara's-Images/21-Surya-Gupta-Taras-Images/<NN>_<exact filename>.png]]

## མཚན

<Tibetan name, exact copy of the intro file's title line>

## ངོ་སྤྲོད

![[0-INBOX/21-Drolma-Introductions/<NN> <Title> (Tibetan).md]]

## བསྟོད་པའི་ཚིགས་བཅད

![[1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md#^1-<N>]]

## སྒྲོལ་མའི་ལོ་རྒྱུས

![[0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md#^1-<M>-0]]

![[0-INBOX/Story/bo-མཁན་པོ་ཚུལ་རྣམ།_སྒྲུང།.md#^1-<M>]]
```

**English — `en-21-Day-Plans/Day-<N> Tara Plan.md`:**

```markdown
---
plan: Tara-Plan-Creator
day: <N>
language: en
tara_number: <N>
tara_name: "<English name, exact copy of the intro file's title line>"
story_number: <M>
generation_date: <YYYY-MM-DD>
status: draft
---

# Day <N> Tara Plan

## Tara's Image

![[0-INBOX/21-Tara's-Images/21-Surya-Gupta-Taras-Images/<NN>_<exact filename>.png]]

## Tara's Name

<English name, exact copy of the intro file's title line>

## Introduction

![[0-INBOX/21-Drolma-Introductions/<NN> <Title> (English).md]]

## Praise Stanza

![[1-SOURCES/Translations/en-The Twenty-One Praises to Tara.md#^1-<N>]]

## Story

![[0-INBOX/Story/en-Khenpo-Tsulnam_Stories.md#^1-<M>-0]]

![[0-INBOX/Story/en-Khenpo-Tsulnam_Stories.md#^1-<M>]]
```

**Chinese — `zh-21-Day-Plans/Day-<N> Tara Plan.md`:**

```markdown
---
plan: Tara-Plan-Creator
day: <N>
language: zh
tara_number: <N>
tara_name: "<Chinese name, exact copy of the intro file's title line>"
story_number: <M>
generation_date: <YYYY-MM-DD>
status: draft
---

# 第<N>天度母计划

## 度母法相

![[0-INBOX/21-Tara's-Images/21-Surya-Gupta-Taras-Images/<NN>_<exact filename>.png]]

## 度母名号

<Chinese name, exact copy of the intro file's title line>

## 度母介绍

![[0-INBOX/21-Drolma-Introductions/<NN> <Title> (Chinese).md]]

## 赞偈

![[1-SOURCES/Translations/Zh-The-Twenty-One-Praises-To-Tara.md#^1-<N>]]

## 度母故事

![[0-INBOX/Story/zh-Khenpo-Tsulnam_Stories.md#^1-<M>-0]]

![[0-INBOX/Story/zh-Khenpo-Tsulnam_Stories.md#^1-<M>]]
```

`<N>` = day number = Tara number. `<M>` = the story number assigned to that day (Rule 4). `<NN>` = the two-digit, zero-padded Tara number as it appears in the image filename prefix (`01`… `21`).

---

## Rules

1. **Never rewrite, paraphrase, translate, or summarize.** Every piece of content in a plan is either an Obsidian transclusion (`![[...]]`) of the source, or — for the Name line and any block a transclusion cannot isolate — a character-for-character copy of the source text. If a source line contains bold, italic, small-caps, `<small>` or any other markdown/HTML styling, copy it with that styling intact; do not strip or "clean up" formatting.

2. **Tara number is sequential and fixed, never random.** Day 1 = Tara 1, Day 2 = Tara 2, … Day 21 = Tara 21, matching the numeric prefix shared by the image files, the introduction files, and the `^1-N` praise-stanza block in every language. Do not shuffle or reassign this mapping.

3. **Story number is drawn at random, without replacement, from 1–28.** Before assigning a story to a new day, scan every existing `Day-*.md` file across all three `*-21-Day-Plans` folders and collect every `story_number` already present in their frontmatter. Draw the new day's story only from the remaining, unused numbers. With 21 days and 28 stories, every day gets a distinct story and up to 7 stories are never used — that is expected, not an error.

4. **Story number is decided once per day, not once per language.** If a plan for this day already exists in *any* one of the three language folders, read its frontmatter `story_number` and reuse that exact value for the other language(s) being generated this run — never draw a new number for a day that already has one. Only draw a fresh random number when none of the three language folders yet has a file for that day.

5. **Within one run that covers several days, draw without replacement across the whole batch**, not just against pre-existing files — two days generated in the same run must not receive the same story.

6. **Praise-stanza and story sources must carry matching block-ID anchors in all three languages before this skill can transclude from them.** The Tibetan source already has them (`^1-1`…`^1-21` for the praise; `^1-1-0`/`^1-1` … `^1-28-0`/`^1-28` for the stories). The English praise source already has them (`^1-1`…`^1-21`). The following do **not** yet have them and need the one-time structural preparation in Rule 7 before first use: the Chinese praise source (`Zh-The-Twenty-One-Praises-To-Tara.md`, currently just 21 unmarked stanzas plus an opening invocation line and a closing colophon couplet), and the English and Chinese story sources (`en-Khenpo-Tsulnam_Stories.md` and `zh-Khenpo-Tsulnam_Stories.md`, currently numbered `### N. <Title>` headings with no block IDs).

7. **Adding a missing block-ID anchor is a permitted structural edit, not a content change**, per `4-SYSTEM/Guidelines/skill-locations.md`'s permission rule ("block boundaries, block IDs, navigation links… factual notes" only). Before generating a Chinese praise stanza or an English/Chinese story for the first time, check whether the needed anchor already exists in the source; if not, add it by inserting `^1-<N>` (praise) or `^1-<N>-0` / `^1-<N>` (story heading / story body) at the end of the corresponding line or paragraph, exactly mirroring the numbering already used in the Tibetan sibling file — counting stanzas/stories in the same top-to-bottom order. Do not touch a single character of the existing wording, and do not add, remove, or reorder any stanza or story while doing this. Prefer running the vault's own `add-block-ids` skill for this if it can be pointed at "no internal numbering" prose; otherwise add the anchors by hand following the pattern above.

8. **The five headings are always level 2 (`##`), never nested deeper**, and always appear in the fixed order: image, name, introduction, praise stanza, story. Do not add extra headings, sections, or content beyond what the Output file format specifies (no sadhana embed, no full-recitation section, no external links) unless the human contributor explicitly asks for an addition.

9. **Match the image file by its two-digit numeric prefix only** (`01_`…`21_`) — the remainder of each filename is inconsistent (some end ` - Edited`, one ends ` - Edited - Edited`, spacing and the embedded Tibetan caption vary file to file) and must not be guessed or normalized; copy the exact filename as it exists on disk into the transclusion link.

10. **The Name section is a plain-text copy of the introduction file's own title line** — its first line for the English and Chinese files, its only title line for the Tibetan file (which has no separate English title line). Do not compose a name from the image filename; the image filename uses a different (Surya Gupta iconographic) naming convention that may not match the introduction's name and is not the source of truth for this field.

11. **Do not modify any file under `1-SOURCES/`** beyond the block-ID additions explicitly permitted by Rule 7, and do not modify the introduction, image, or story files at all beyond those same permitted anchor additions in `0-INBOX/`.

---

## Procedure

1. Parse the requested day(s) and language(s) from the human contributor's instruction. If nothing was specified beyond "run Tara-Plan-Creator," stop and ask which day(s).
2. For each requested day `N`:
   a. Confirm `1 ≤ N ≤ 21`. If not, stop and report.
   b. If `N` is 1 or 2, apply the Day 1/2 exception in the Output section and get a decision before writing the Tibetan file.
   c. Locate the image file in `21-Surya-Gupta-Taras-Images/` whose filename starts with the zero-padded prefix `NN_`.
   d. For each language being produced, locate the matching introduction file `0-INBOX/21-Drolma-Introductions/<NN> <Title> (<Language>).md` (the `<NN> <Title>` portion is shared across all three language files for that Tara; only the trailing `(Tibetan|English|Chinese)` and file contents differ) and read its first line as the Name.
   e. Confirm block `^1-N` exists in that language's praise-stanza source (Rule 6/7); add it first if it is the Chinese source and the anchor is missing.
   f. Determine the story number `M` per Rules 3–5: check existing plan files for this day first; if none exist, collect all `story_number`s already used across all existing days (and any already assigned earlier in this same run) and draw a random unused number from 1–28.
   g. Confirm blocks `^1-M-0` and `^1-M` exist in that language's story source (Rule 6/7); add them first if missing (English/Chinese).
   h. Build the file from the Output file format template, substituting `N`, `M`, `NN`, the exact image filename, the exact introduction file path, and the exact Name text.
   i. Write the file to the correct language folder. If it already exists and overwriting was not requested, stop and report the collision instead.
3. After all requested days/languages are written, run every item in the Completion check below against the actual files just written before telling the human contributor the run is done.

---

## Completion check

Fact-check every one of these against the files actually on disk — do not tick a box from memory of what should be true.

- [ ] For every file written, `tara_number` (frontmatter) equals the day number `N`, and the image filename prefix, the introduction filename prefix, and the praise-stanza block ID (`^1-N`) all agree with that same `N`.
- [ ] For every file written, `story_number` (frontmatter) is identical across all language versions of the same day.
- [ ] No `story_number` value appears more than once across all files in `bo-21-Day-Plans`, `en-21-Day-Plans`, and `zh-21-Day-Plans` combined (check the full set, not just today's batch).
- [ ] Every heading in every file written is exactly level `##`, in the fixed order (image, name, introduction, praise stanza, story), with no extra sections added.
- [ ] The Name text under `## Tara's Name` / `## མཚན` / `## 度母名号` matches, character for character, the first line of the introduction file transcluded immediately below it.
- [ ] Every transclusion link (`![[...]]`) resolves to a file and, where a block ID is used, an anchor that actually exists in the vault — no broken link, no guessed anchor.
- [ ] Any block-ID anchor added under Rule 7 was inserted at the end of the existing line/paragraph only, with no wording changed, added, or removed in the source file.
- [ ] Every file was saved to the correct language folder under the correct exact filename (`Day-<N> Tara Plan.md`), and no existing file was overwritten without the human contributor's go-ahead.
- [ ] The Day 1/2 legacy-format question was asked and resolved before writing anything for those two days, if they were part of this run.
