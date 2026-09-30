Read `3-SKILLS/edition-spacing-fix/SKILL.md` in full, then execute it on the file(s) or input the user specifies.

Skill purpose: Scan a published edition for spacing errors (run-together words, no space after punctuation, stray or odd spaces), map every hit, and after human review fix the approved ones in place, bottom-up, through `PATCH /v2/editions/{id}/content` without moving a segment boundary.
