---
audit_date: 2026-09-23
total_issues: 10
---

# Vault audit — 2026-09-23

**10 issue(s) found.**

Run immediately after syncing the system layer to `rails-template@3d17090`. The
vault has no rails and no transformations yet, so checks 2–4 and 7b have nothing
to examine — that is a clean result, not an empty one.

---

## 1. Skills sync

56 skills are installed. All 56 carry `name:`/`description:` frontmatter and a
`.claude/commands/` stub, and every one of the catalog's 53 entries points to a
skill folder that exists. Three installed skills have no catalog entry:

- [ ] `gemini-article-polish`: missing from SKILLS-CATALOG.md
- [ ] `wiki-article-from-claims`: missing from SKILLS-CATALOG.md
- [ ] `wiki-article-inventory`: missing from SKILLS-CATALOG.md

These three arrive unregistered from `rails-template@3d17090` itself — this vault
did not drop them. Per `How-to guides/Sync with rails-template.md`
§"Syncing skills from the shared library", the fix belongs in the shared library
or the template, not in a vault copy: patching the catalog here puts the entry
somewhere neither the template nor any other vault will see.

## 2. Frontmatter completeness

✓ No issues found.

`2-RAILS/` holds no verse packages and no consolidated glossaries;
`3-TRANSFORMATIONS/` holds no generated outputs. The only non-`About` file is
`2-RAILS/Verses/_TEMPLATE.md`, which is the skeleton shipped by the template,
not a rail — see Notes.

## 3. Citation chain integrity

✓ No issues found.

No file in `3-TRANSFORMATIONS/` links or transcludes into `1-SOURCES/`.

## 4. Status consistency

✓ No issues found.

No transformation carries `status: complete`. The four occurrences of that string
in `3-TRANSFORMATIONS/` are all inside `About *.md` documentation.

## 5. Stale inbox files

✓ No files older than 7 days in 0-INBOX/.

`0-INBOX/` contains only `.gitkeep` structural placeholders.

## 6. Dead wiki links

✓ No issues found.

Eleven wiki links exist in `2-RAILS/`, all of them documentation examples
carrying `<placeholder>` syntax (`[[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]`,
`![[1-SOURCES/Text/<lang>-root-text.md#^<ref>]]`, and similar) in
`About Rails.md` and `_TEMPLATE.md`. These are patterns to be filled in, not
links to resolve, so they are not counted as dead.

## 7. File placement

- [ ] `2-RAILS/Verses/_TEMPLATE.md`: misplaced file — does not follow verse-ID naming convention (`<chapter>-<verse>.md`). **False positive** — this is the verse-package skeleton that `rails-template@3d17090` ships at exactly this path, and `verse-context` copies it. Do not move or rename it; the check itself needs an exemption. Recorded here because the check as written flags it.

7b: no `3-TRANSFORMATIONS/*/Verses/` directories exist, so no verse rail is
missing for an existing transformation.

## 8. Unfilled template placeholders

The vault still identifies itself as the unnamed template. Every item below is a
real gap — this vault is for the Zabtig Drolchok (ཟབ་ཏིག་སྒྲོལ་ཆོག), and nothing
in its own documentation says so.

- [ ] `README.md:1`: still contains template placeholder `[text-slug]` — fill in or delete before the vault is used.
- [ ] `README.md:5`: still contains the `> **Using this template:**` instruction block — delete once the placeholders are filled.
- [ ] `README.md:60`: still contains template placeholder `[name of text]` — fill in or delete before the vault is used.
- [ ] `4-SYSTEM/CLAUDE.md:49`: still contains template placeholder `[name of text]` — fill in or delete before the vault is used.
- [ ] `4-SYSTEM/Guidelines/vault-annex.md:1`: still contains template placeholder `[text-slug]` — fill in or delete before the vault is used.
- [ ] `4-SYSTEM/Guidelines/vault-annex.md:3,15`: still contains template placeholder `[name of text]` — fill in or delete before the vault is used.
- [ ] `4-SYSTEM/Guidelines/vault-annex.md:9`: still contains the `> **Template instructions:**` block, and all 8 sections are unfilled. Until §2 is written, the addressing scheme this vault's block IDs actually use is recorded nowhere.

`4-SYSTEM/CLAUDE.md:396` also matches, but that line is the lint rule that
describes these placeholders. It is not itself a placeholder.

---

## Notes — outside the eight checks

Two things this audit cannot flag mechanically, recorded so they are not lost.

**Duplicate citation addresses in `1-SOURCES/`.** The same three texts are
present twice, under two names each:

| Copy A (schema-conformant) | Copy B (as received) |
| --- | --- |
| `1-SOURCES/Text/bo-zabtig-drolchok.md` | `1-SOURCES/Text/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md` |
| `1-SOURCES/Text/bo-phon-zabtig-drolchok.md` | `1-SOURCES/Text/En-Tārā’s_Profound_Essence_Transliteration.md` |
| `1-SOURCES/Translations/en-zabtig-drolchok.md` | `1-SOURCES/Text/En-Tārā’s_Profound_Essence_Translation.md` |

Both sets carry the same 437 block IDs, so `^I-2` resolves to two different
files. A block ID is a citation address: once rails start citing verses, two
addresses for one verse split the backlinks and let the copies drift apart
unnoticed. The vault annex §1 should name which file rails cite. Copy B is kept
by decision — this is a bookkeeping gap, not a mistake.

**Check 2's field list is out of step with the current verse schema.** This
skill requires `verse_id`, `root_text`, `root_block`, `language`,
`commentaries`, `status`. The `_TEMPLATE.md` shipped with the same template
declares `ref`, `unit_type`, `unit_verses`, `commentary_coverage`,
`tradition_coverage`, `concepts_in_verse`, `status` and others. The first verse
package written here will be flagged by a check that is reading an older schema.
Like the catalog gaps above, the fix belongs upstream.

**`-bo-phon` is not a registered language tag.** `bo-phon-zabtig-drolchok.md`
uses it for phonetic transliteration; `About Sources.md` §12 lists only `-bo`,
`-bo-wy`, `-bo-thl` and `-bo-acip`. Register it in §12 or in the annex.
