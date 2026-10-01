# Hindi alignment report — Tārā’s Profound Essence

Source: `0-INBOX/raw-data/དགོངས་གཏེར་སྒྲོལ་མའི་ཟབ་ཏིག་ལས། མཎྜལ་ཆོ་ག་ཚོགས་གཉིས་སྙིང་པོ་ཞེས་བྱ་བ་བཞུགས་སོ།།.md` (Tibetan–Hindi booklet, PDF text).  
Output: `1-SOURCES/Translations/Hi-Tārā’s_Profound_Essence.md`, block-aligned to `1-SOURCES/Text/bo-ཟབ་ཏིག་སྒྲོལ་ཆོག.md`.  
Generated 2026-09-30. Raw line numbers below refer to the inbox file.

## Method

1. Every line of the booklet was classed as Tibetan, Devanagari, page number or other. PDF line-wraps inside a Hindi passage were joined; line breaks between passages were kept.
2. The booklet's Tibetan was split into syllables and aligned against the root's syllables in one monotonic pass. Each Hindi passage went to the root block that held most of the Tibetan just above it.
3. Passages with no Tibetan above them (section II, the Sanskrit Twenty-one Praises, Hindi sub-headings, instruction lines) were placed by hand by content and position. The Sanskrit praises were mapped by position within each of the three recitation sets.
4. The booklet's Tibetan was removed. Each block got a transclusion of its root block and the root's block id, and `yigchung-transfer` carried over the root's `<small>` marks.

**Result:** 332 content blocks and 12 headings, the same ids in the same order as the root. 15 blocks have no Hindi. `translation-alignment-check` passes every structural check except two: line counts differ (the Hindi is prose, one passage per verse) and the placeholders are still there.

## Decisions to review

### Heading generated from the Tibetan (no Hindi heading in the booklet)

- `^I-0` → **भगवान शाक्यराज की पन्द्रह श्लोकों वाली प्रार्थना**. Translated from བཅོམ་ལྡན་འདས་ཤཱཀྱའི་རྒྱལ་པོ་ལ་གསོལ་བ་འདེབས་པའི་ཚིགས་སུ་བཅད་པ་བཅོ་ལྔ་པ།, in the translator's own wording from the `^I-17` colophon.

All other headings are the booklet's own. For `^a-0` the booklet's heading and its bracketed rendering of the Tibetan title were kept together. `^g-0` drops a trailing `(1)` footnote mark.

### Root blocks with no Hindi (`*[not yet translated]*`)

- `^II-6` — མངྒ་ལའི་གསུང་།
- `^1-7` — ཚར་གསུམ།
- `^1-8` — ཚོགས་བསགས་པ་ནི།
- `^1-19` — ཞེས་བསང་སྦྱང་༌།
- `^1-23` — དེ་ནས་ཐོག་མར་དཀོན་མཆོག་སྤྱི་ལ་ཕྱག་མཆོད་འབུལ་བ་ནི།
- `^1-85` — རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། ། / ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག །
- `^1-119` — རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་འདི་དང་། ། / ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག །
- `^1-120` — ཚར་གསུམ་བརྗོད།
- `^1-154` — ཚར་བདུན།
- `^1-163` — གཏོར་མ་ཨ་མྲྀ་ཏས་བསང་༌།
- `^1-165` — སྭ་བྷཱ་བས་སྦྱང་༌།
- `^1-181` — ཐལ་མོ་སྦྱར་ལ།
- `^b-1` — ཨོཾ་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་སྭཱ་ཧཱ།
- `^c-1` — ན་མོ་ཨཱརྻཱ་ཏཱ་ར་ཡེ།
- `^d-1` — ན་མསྟཱ་ར་ཡེ།

Most are one-word rubrics such as ཚར་གསུམ། "three times" that the booklet leaves out or folds into a neighbouring instruction. For `^1-8` and `^1-23` the booklet's Hindi sub-heading is unreadable in the PDF text (a legacy-font rendering such as `AR-ing`), so nothing could be kept.

### Booklet passages with no counterpart in the root (kept on the nearest block)

- raw L123 → `^II-3`: (यह प्रार्थना ख्येनत्से वांगपो द्वारा रचित है।)
- raw L776 → `^1-198`: (यदि कोई भौतिक आधार/प्रतिमा न हो, तो इस प्रकार कहें:)
- raw L779 → `^1-198`: ॐ! समस्त संसारी जीवों का पूर्ण कल्याण करने वाली, तथा उनकी साधना के अनुरूप फल व सिद्धियाँ प्रदान करने वाली हे भ…
- raw L783 → `^1-198`: वज्र मुः !
- raw L785 → `^1-198`: (ऐसा कहकर आमंत्रित अतिथि-देवताओं को विसर्जन व प्रस्थान कराएँ।)
- raw L854 → `^1-213`: नित्य साधना-विधि
- raw L858 → `^1-213`: दूसरा क्रम नित्य (प्रतिदिन की संक्षिप्त) साधना का है: यदि पूज्य आर्य तारा की प्रतिमा/चित्र उपलब्ध हो तो उत्तम …
- raw L865 → `^1-213`: 'एक क्षण के स्मरण मात्र से, मैं स्वयं पूज्य आर्य तारा के स्वरूप में...' यहाँ से आरम्भ करके पूजा, मण्डल-अर्पण औ…
- raw L872 → `^1-213`: 'हे पूज्य आर्य तारा! अपने पावन मण्डल सहित...' इत्यादि द्वारा अपने अभीष्ट की प्रार्थना करें।
- raw L873 → `^1-213`: यदि संक्षेप में करना हो, तो इसे छोड़ा भी जा सकता है। इसके बाद 'सम्मुख कल्पित स्वरूप प्रकाश में विलीन होकर...' …
- raw L1338 → `^f-6`: सर्वज्ञ दोलपोपा के पावन वचन

*(Superseded: these passages were moved out on 2026-09-30, see "Meaning review" below.)*

### Reordered to follow the root

- Section g (tea offering, raw L1303–1317) comes before section f (raw L1320–1344) in the booklet. The root has f first.
- The `^III-2` attribution (raw L139) comes before its verse in the booklet.

### Passages split at a sentence or clause boundary to fit two root blocks

- raw L475: `^1-86` / `^1-87`, split before “फिर पुनः…”
- raw L683: `^1-168` / `^1-169`, split before “तीन बार…”
- raw L759: `^1-193` / `^1-194`, split before “(तीन बार…”
- raw L1272: `^e-10` / `^e-11`, split before “आप तो दस…”
- raw L1280: `^e-12` / `^e-13`, split before “जो सद्धर्म…”
- raw L1287: `^e-13` / `^e-14`, split before “विहारों और…”
- raw L1335: `^f-4` / `^f-5`, split before “(यह श्लोक…”

### Hindi sub-headings placed as the first line of a block

The booklet has sub-headings inside chapter 1 that the root has no heading for. Where the sub-heading renders a root rubric it became that rubric's text: `^1-16` पूजा-सामग्रियों का अधिष्ठान, `^1-27` भद्रचर्या-प्रणिधान पर आधारित सप्तांग पूजा, `^1-162` बलि (नैवेद्य-पिण्ड) विधानः. Where it doesn't, it is the first line of the block it introduces, or of the empty rubric slot just before it: `^1-40` मण्डल-अर्पण, `^1-45` प्रार्थना एवं अभीष्ट-याचना, `^1-59` विशेष मण्डल-अर्पण, `^1-94` द्वितीय भावना एवं पाठ (अभय-मुद्रा), `^1-121` तृतीय पूजा-क्रम एवं अमृत-वर्षा भावना, `^1-155` तारा-स्तोत्र की फलश्रुति / गुणानुशंसा -, `^1-213` नित्य साधना-विधि, `^f-6` सर्वज्ञ दोलपोपा के पावन वचन.

### Removed

- Page numbers, the stray `B` and `1` lines, the booklet's English title (raw L7–10), and the booklet's own copy of every Tibetan line.
- raw L14: “प्रथम भाग (आरम्भिक स्तुति एवं बोधिचित्त)”. Page-header label (the booklet's pages 1 and 2 only).
- raw L38: “द्वितीय भाग”. Page-header label (the booklet's pages 1 and 2 only).
- Unreadable Tibetan sub-headings in legacy-font renderings (raw L167, 176, 225, 371, 412, e.g. `QRUMHA Çd aMAMa (སྐྱབས་སེམས་ནི།)`).
- OCR garbage in front of or inside Hindi lines, most likely mis-encoded Tibetan rubrics:
  - raw L210: `(कॅडोबा)`
  - raw L224: `ईश्वराण`
  - raw L239: `(गायक)`
  - raw L327: `(कुत्नुথ'বা)`
  - raw L347: `('')`
  - raw L411: `(डे'सानु''नु'वा)`
  - raw L484: `बैं हूँ`
  - raw L630: `(खा)`
  - raw L670: `बाबा`
  - raw L673: `मार्केका`
  - raw L683: `অঁঃ ঃ 'मासुमा`
  - raw L694: `बारा`
  - raw L711: `डेन बुरा`
  - raw L773: `आँसुका`
  - raw L776: `देवमेनका`
  - raw L798: `डेरा`
  - raw L816: `'गा |`
  - raw L854: `(कुरुरु)`
  - raw L1303: `(1)`

### Kept as delivered but possibly garbled

- `ॐ ॐ ॐ आः हूँ।` (raw L328, L563; root ཨོཾ་ཨཱཿཧཱུྃ). `बैं हूँ` in front of the same mantra at raw L484 was removed as garbage.

## Low-confidence Tibetan matches

Booklet Tibetan chunks that matched less than 80% of their syllables, or that spanned more than one root block. The Hindi went to the block marked ▶.

| raw line | coverage | root blocks (syllables matched) | booklet Tibetan |
|---|---|---|---|
| 176 | 100% | 1-8 (4), ▶1-9 (27) | AR-ing (ཚོགས་བསགས་པ་ནི།) རྗེ་བཙུན་འཕགས་མ་སྒྲོལ་མ་དང༌། ། ཕྱོག |
| 214 | 64% | ▶1-18 (7) | ཨོཾ་སྭ་བྷཱ་བ་ཤུདྡྷེ་སརྦ་དྷརྨ་སྭ་བྷཱ་བ་ཤུདྡྷེ྅ཧཾ། |
| 222 | 29% | ▶1-21 (2) | ཨོྃ་བཛྲ་ཨཧཱུྃ་… ནས་ ...ཤཔྟ་ཨཱཿ ཧཱུྃ། |
| 353 | 95% | 1-45 (7), ▶1-46 (13) | ཡེ་ཤེས་གཅིག་གི་ངོ་བོ་ལས༔ རང་བཞིན་མ་འགགས་ཅིར་ཡང་སྟོན༔ ཐུགས་རྗ |
| 356 | 100% | ▶1-46 (14), 1-47 (14) | འགྲོ་ཀུན་སྐྱབས་དང་མགོན་གྱུར་པ༔ མཁྱེན་བརྩེའི་བདག་ཉིད་ཁྱེད་རྣམ |
| 405 | 76% | ▶1-57 (13) | ཨོཾ་ཨཱརྻ་ཏཱ་རེ་ས་པ་རི་བཱ་ར་བཛྲ་ཨརྦྷ་… ནས་ ...ཤབྡ་པྲ་ཏཱིཙྪ་སྭ |
| 474 | 92% | ▶1-85 (7), 1-86 (3), 1-87 (2) | ྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག ། ཚར་གཉིས་བརྗོད། སླར་ཡང་། |
| 480 | 76% | ▶1-89 (13) | ཨོཾ་ཨཱརྻ་ཏཱ་རེ་ས་པ་རི་བཱ་ར་བཛྲ་ཨཧཱུྃ་... ནས་ ...ཤཔྟ་པྲ་ཏཱིཙྪ |
| 499 | 90% | ▶1-95 (3), 1-96 (2), 1-119 (1), 1-120 (3) | ཅེས་མོས་ལ་ཕྱག་འཚལ་ཉེར་གཅིག་ཚར་གསུམ་བརྗོད། |
| 559 | 76% | ▶1-123 (13) | ཨོཾ་ཨཱརྻ་ཏཱ་རེ་ས་པ་རི་བཱ་ར་བཛྲ་ཨཧཱུཾ་... ནས་ ...ཤཔྤ་པྲ་ཏཱིཙྪ |
| 576 | 90% | ▶1-129 (7), 1-154 (2) | ཅེས་མོས་ལ་ཕྱག་འཚལ་ཉེར་གཅིག་ཚར་བདུན་དང༌། |
| 632 | 97% | 1-155 (14), ▶1-156 (16) | ལྷ་མོ་ལ་གུསཡང་དག་ལྡན་པའི། ། བློ་ལྡན་གང་གིས་རབ་དང་བརྗོད་དེ། ། |
| 641 | 91% | 1-156 (14), ▶1-157 (25) | སྡིག་པ་ཐམས་ཅད་རབཏུ་ཞི་བྱེད། ། ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། |
| 676 | 54% | ▶1-166 (7) | ཨོཾ་སྭ་བྷཱ་བ་ཤུདྡྷ་སརྦ་དྷརྨ་སྭ་བྷཱ་བ་ཤུདྡྷེ྅ཧཾ། གིས་སྦྱང༌། |
| 684 | 88% | 1-168 (1), ▶1-170 (17), 1-171 (5) | ཨོཾ་ཨཱརྻ་ཏཱ་རེ་ས་པ་རི་བཱ་ར་ཨི་དཾ་བ་ལི་ཏ་ཁ་ཁ་ཁཱ་ཧི་ཁཱ་ཧི། ལན་ |
| 687 | 76% | ▶1-172 (14), 1-173 (8) | ཨོཾ་ཨ་ཀཱ་རོ་མུ་ཁཾ་སརྦ་དྷརྨཱ་ཎཱཾ་ཨཱ་དྱ་ནུཏྤནྣ་ཏྭཱ་ཏ་ཨོཾ་ཨཱཿ ཧ |
| 695 | 81% | ▶1-176 (9), 1-177 (4) | ཨོཾ་ཨཱརྻ་ཏཱ་རེ་ས་པ་རི་བཱ་ར་བཛྲ་ཨཧཱུྃ་སོགས་སྔགས་ཙམ་གྱིས་མཆོད། |
| 757 | 33% | ▶1-192 (2) | ཅི་འགྲུབ་མཐར། ཡིག་བརྒྱ་དང་། |
| 814 | 100% | 1-206 (18), ▶1-207 (31) | ཐམས་ཅད་མཁྱེན་པ་སྒྲུབ་པར་བྱེད་པ་ལ། ། བར་གཅོད་གདོན་བགེགས་རིམས་ |
| 1082 | 98% | b-0 (27), b-1 (1), ▶b-2 (30) | ༄༅། །འཕགས་མ་སྒྲོལ་མ་ལ་རྩ་སྔགས་དང་སྦྱར་བའི་སྒོ་ནས་གསོལ་བ་འདེབ |
| 1126 | 100% | c-0 (23), ▶c-2 (36) | ༄༅། །འཕགས་མ་སྒྲོལ་མ་ཡིད་བཞིན་འཁོར་ལོ་ལ་ཕྱག་འཚལ་བའི་ཚིགས་སུ་བ |
| 1174 | 95% | d-0 (12), ▶d-2 (27) | རྗེ་བཙུན་འཕགས་མ་ལ་བསྔགས་པ་འདོད་དོན་འགྲུབ་པའི་ཤིས་བརྗོད། ཁྱེད |
| 1216 | 100% | ▶e-0 (16), e-1 (15) | ༄༅། །ཀུན་མཁྱེན་ཐུབ་པའི་བསྟན་པ་རྒྱས་པའི་སྨོན་ལམ་དྲང་སྲོང་ལྷ་ཡ |
| 1269 | 98% | e-10 (27), ▶e-11 (35) | ཀྱེ་མ་ཀྱི་ཧུད་མགོན་པོ་ཐུགས་རྗེ་ཅན། ། ཁྱོད་རྣམས་ཐུགས་དམ་མཐུ་ར |
| 1278 | 100% | ▶e-12 (27), e-13 (18) | འཕགས་བོད་གཉིས་སུ་རྫོགས་ལྡན་ཕྱི་མ་ཡི། ། དགའ་སྟོན་རིན་ཆེན་སྒྲོ |
| 1284 | 100% | e-13 (18), ▶e-14 (36) | བསྟན་འཛིན་དགེ་འདུན་སྡེ་ཡིས་འཛམ་གླིང་ཁྱབ། ། བཤད་དང་སྒྲུབ་པ་དར |

The hand-placed passages override ▶ where the table disagrees with the output. For example `^1-95`, `^1-129` and `^1-86`/`^1-87` were placed by position.

## Block map

| block | raw lines | method |
|---|---|---|
| # ^0 | 11–12 | manual |
| ## ^I-0 | — | heading generated |
| ^I-1 | 16 | tibetan |
| ^I-2 | 22–26 | tibetan |
| ^I-3 | 29–30 | tibetan |
| ^I-4 | 33–35 | tibetan |
| ^I-5 | 40–41, 43–44 | tibetan |
| ^I-6 | 46–47, 49–50 | tibetan |
| ^I-7 | 52, 54–55 | tibetan |
| ^I-8 | 58–60 | tibetan |
| ^I-9 | 62–63, 67–68 | tibetan |
| ^I-10 | 70–71, 73–74 | tibetan |
| ^I-11 | 76, 78–79 | tibetan |
| ^I-12 | 81, 83–84 | tibetan |
| ^I-13 | 89–91 | tibetan |
| ^I-14 | 94–96 | tibetan |
| ^I-15 | 99–101 | tibetan |
| ^I-16 | 104–105 | tibetan |
| ^I-17 | 108–109 | tibetan |
| ## ^II-0 | 112 | manual |
| ^II-1 | 113–115 | manual |
| ^II-2 | 116–118 | manual |
| ^II-3 | 119–122, 123 | extra, manual |
| ^II-4 | 124 | manual |
| ^II-5 | 125–127 | manual |
| ^II-6 | — | no Hindi |
| ^II-7 | 128–130 | manual |
| ^II-8 | 131–133 | manual |
| ^II-9 | 134–135 | manual |
| ## ^III-0 | 138 | manual |
| ^III-1 | 140, 141–142 | manual |
| ^III-2 | 139 | manual |
| ## ^1-0 | 143 | manual |
| ^1-1 | 144, 145 | manual |
| ^1-2 | 146–148 | manual |
| ^1-3 | 149–151 | manual |
| ^1-4 | 152–154, 155, 156, 157, 158, 159, 160, 161–164 | manual |
| ^1-5 | 168–169 | manual |
| ^1-6 | 171–172, 174, 175 | tibetan |
| ^1-7 | — | no Hindi |
| ^1-8 | — | no Hindi |
| ^1-9 | 179–180 | tibetan |
| ^1-10 | 183–184 | tibetan |
| ^1-11 | 187–189 | tibetan |
| ^1-12 | 194–195 | tibetan |
| ^1-13 | 198–199 | tibetan |
| ^1-14 | 202–203 | tibetan |
| ^1-15 | 206–207 | tibetan |
| ^1-16 | 210 | manual |
| ^1-17 | 212, 213 | manual, tibetan |
| ^1-18 | 215, 216 | manual, tibetan |
| ^1-19 | — | no Hindi |
| ^1-20 | 219–221 | tibetan |
| ^1-21 | 223 | tibetan |
| ^1-22 | 224 | manual |
| ^1-23 | — | no Hindi |
| ^1-24 | 226–227, 228 | manual |
| ^1-25 | 231–233 | tibetan |
| ^1-26 | 235, 236 | tibetan |
| ^1-27 | 239 | manual |
| ^1-28 | 242, 243, 244–245 | tibetan |
| ^1-29 | 248, 249, 250–252 | tibetan |
| ^1-30 | 255, 256, 257–258 | tibetan |
| ^1-31 | 261, 262, 263–265 | tibetan |
| ^1-32 | 270, 271, 272–273 | tibetan |
| ^1-33 | 276, 277, 278–280 | tibetan |
| ^1-34 | 283, 284, 285–287 | tibetan |
| ^1-35 | 290, 291, 292–294 | tibetan |
| ^1-36 | 299, 300, 301–303 | tibetan |
| ^1-37 | 306, 307, 308–310 | tibetan |
| ^1-38 | 313, 314, 315–317 | tibetan |
| ^1-39 | 320, 321, 322–324 | tibetan |
| ^1-40 | 327 | manual |
| ^1-41 | 328, 331–333 | manual, tibetan |
| ^1-42 | 336–338, 340–341 | tibetan |
| ^1-43 | 343 | tibetan |
| ^1-44 | 344 | manual |
| ^1-45 | 347, 349, 351–352 | manual, tibetan |
| ^1-46 | 354–355, 358–360 | tibetan |
| ^1-47 | 362 | tibetan |
| ^1-48 | 365–367 | tibetan |
| ^1-49 | 368 | manual |
| ^1-50 | 372–373 | manual |
| ^1-51 | 375–376, 378–379 | tibetan |
| ^1-52 | 381–382 | tibetan |
| ^1-53 | 383, 386–388, 389 | manual, tibetan |
| ^1-54 | 394–396 | tibetan |
| ^1-55 | 398, 399 | tibetan |
| ^1-56 | 402–404 | tibetan |
| ^1-57 | 406–407 | tibetan |
| ^1-58 | 408 | manual |
| ^1-59 | 411, 413, 416–418 | manual, tibetan |
| ^1-60 | 420 | tibetan |
| ^1-61 | 421–422 | manual |
| ^1-62 | 425 | manual |
| ^1-63 | 426, 427 | manual |
| ^1-64 | 428, 429 | manual |
| ^1-65 | 430, 431 | manual |
| ^1-66 | 432, 433 | manual |
| ^1-67 | 434, 435 | manual |
| ^1-68 | 436, 437 | manual |
| ^1-69 | 438, 439 | manual |
| ^1-70 | 440, 441 | manual |
| ^1-71 | 442, 443 | manual |
| ^1-72 | 444, 445 | manual |
| ^1-73 | 446, 447 | manual |
| ^1-74 | 450, 451 | manual |
| ^1-75 | 452, 453 | manual |
| ^1-76 | 454, 455 | manual |
| ^1-77 | 456, 457 | manual |
| ^1-78 | 458, 459 | manual |
| ^1-79 | 460, 461 | manual |
| ^1-80 | 462, 463 | manual |
| ^1-81 | 464, 465 | manual |
| ^1-82 | 466, 467 | manual |
| ^1-83 | 468, 469 | manual |
| ^1-84 | 470, 471 | manual |
| ^1-85 | — | no Hindi |
| ^1-86 | 475 | split |
| ^1-87 | 475 | split |
| ^1-88 | 478–479 | tibetan |
| ^1-89 | 481–482 | tibetan |
| ^1-90 | 483 | manual |
| ^1-91 | 484, 487–489 | manual, tibetan |
| ^1-92 | 491 | tibetan |
| ^1-93 | 492 | manual |
| ^1-94 | 493, 496–498 | manual, tibetan |
| ^1-95 | 500 | tibetan |
| ^1-96 | 503 | manual |
| ^1-97 | 504, 505 | manual |
| ^1-98 | 506, 507 | manual |
| ^1-99 | 508, 509 | manual |
| ^1-100 | 510, 511 | manual |
| ^1-101 | 512, 513 | manual |
| ^1-102 | 514, 515 | manual |
| ^1-103 | 516, 517 | manual |
| ^1-104 | 518, 519 | manual |
| ^1-105 | 520, 521 | manual |
| ^1-106 | 522, 523 | manual |
| ^1-107 | 524, 525 | manual |
| ^1-108 | 528, 529 | manual |
| ^1-109 | 530, 531 | manual |
| ^1-110 | 532, 533 | manual |
| ^1-111 | 534, 535 | manual |
| ^1-112 | 536, 537 | manual |
| ^1-113 | 538, 539 | manual |
| ^1-114 | 540, 541 | manual |
| ^1-115 | 542, 543 | manual |
| ^1-116 | 544, 545 | manual |
| ^1-117 | 546, 547 | manual |
| ^1-118 | 548, 549 | manual |
| ^1-119 | — | no Hindi |
| ^1-120 | — | no Hindi |
| ^1-121 | 552, 554 | manual, tibetan |
| ^1-122 | 557–558 | tibetan |
| ^1-123 | 560–561 | tibetan |
| ^1-124 | 562 | manual |
| ^1-125 | 563, 566–567 | manual, tibetan |
| ^1-126 | 569 | tibetan |
| ^1-127 | 570 | manual |
| ^1-128 | 573–575 | tibetan |
| ^1-129 | 577 | tibetan |
| ^1-130 | 580 | manual |
| ^1-131 | 581, 582 | manual |
| ^1-132 | 583, 584 | manual |
| ^1-133 | 585, 586 | manual |
| ^1-134 | 587, 588 | manual |
| ^1-135 | 589, 590 | manual |
| ^1-136 | 591, 592 | manual |
| ^1-137 | 593, 594 | manual |
| ^1-138 | 595, 596 | manual |
| ^1-139 | 597, 598 | manual |
| ^1-140 | 599, 600 | manual |
| ^1-141 | 601, 602 | manual |
| ^1-142 | 605, 606 | manual |
| ^1-143 | 607, 608 | manual |
| ^1-144 | 609, 610 | manual |
| ^1-145 | 611, 612 | manual |
| ^1-146 | 613, 614 | manual |
| ^1-147 | 615, 616 | manual |
| ^1-148 | 617, 618 | manual |
| ^1-149 | 619, 620 | manual |
| ^1-150 | 621, 622 | manual |
| ^1-151 | 623, 624 | manual |
| ^1-152 | 625, 626 | manual |
| ^1-153 | 627 | manual |
| ^1-154 | — | no Hindi |
| ^1-155 | 630, 631, 634 | manual |
| ^1-156 | 635, 636, 637–640 | manual, tibetan |
| ^1-157 | 643, 644, 645, 646–647 | tibetan |
| ^1-158 | 650, 651, 652–654 | tibetan |
| ^1-159 | 656, 657, 658–659 | tibetan |
| ^1-160 | 664, 665, 666–669 | tibetan |
| ^1-161 | 670 | manual |
| ^1-162 | 673 | manual |
| ^1-163 | — | no Hindi |
| ^1-164 | 675 | tibetan |
| ^1-165 | — | no Hindi |
| ^1-166 | 677 | tibetan |
| ^1-167 | 680–682 | tibetan |
| ^1-168 | 683 | split |
| ^1-169 | 683 | split |
| ^1-170 | 685 | tibetan |
| ^1-171 | 686 | manual |
| ^1-172 | 688 | tibetan |
| ^1-173 | 689 | manual |
| ^1-174 | 692–693 | tibetan |
| ^1-175 | 694 | manual |
| ^1-176 | 696–697 | tibetan |
| ^1-177 | 698 | manual |
| ^1-178 | 703–705 | tibetan |
| ^1-179 | 708–710 | tibetan |
| ^1-180 | 711 | manual |
| ^1-181 | — | no Hindi |
| ^1-182 | 714–716 | tibetan |
| ^1-183 | 719–721 | tibetan |
| ^1-184 | 724–726 | tibetan |
| ^1-185 | 729–731 | tibetan |
| ^1-186 | 734–738 | tibetan |
| ^1-187 | 741–743 | tibetan |
| ^1-188 | 745–746 | tibetan |
| ^1-189 | 749–751 | tibetan |
| ^1-190 | 753–754 | tibetan |
| ^1-191 | 756 | tibetan |
| ^1-192 | 758 | tibetan |
| ^1-193 | 759–761 | split |
| ^1-194 | 759–761 | split |
| ^1-195 | 766–767 | tibetan |
| ^1-196 | 770–772 | tibetan |
| ^1-197 | 773 | manual |
| ^1-198 | 775, 776, 779–781, 783, 785 | extra, tibetan |
| ^1-199 | 787–788 | tibetan |
| ^1-200 | 792 | tibetan |
| ^1-201 | 795–797 | tibetan |
| ^1-202 | 798 | manual |
| ^1-203 | 801–803 | tibetan |
| ^1-204 | 805 | tibetan |
| ^1-205 | 808–810 | tibetan |
| ^1-206 | 812–813 | tibetan |
| ^1-207 | 816–818 | tibetan |
| ^1-208 | 823–824 | tibetan |
| ^1-209 | 827–829 | tibetan |
| ^1-210 | 832–834 | tibetan |
| ^1-211 | 837–840 | tibetan |
| ^1-212 | 843–845 | tibetan |
| ^1-213 | 849–851, 854, 858–862, 865–868, 872, 873–877 | extra, tibetan |
| ## ^a-0 | 880, 882–883 | manual |
| ^a-1 | 886–888 | tibetan |
| ^a-2 | 891–893 | tibetan |
| ^a-3 | 896–898 | tibetan |
| ^a-4 | 901–903 | tibetan |
| ^a-5 | 908–910 | tibetan |
| ^a-6 | 913–916 | tibetan |
| ^a-7 | 919–921 | tibetan |
| ^a-8 | 924–926 | tibetan |
| ^a-9 | 929–931 | tibetan |
| ^a-10 | 936–938 | tibetan |
| ^a-11 | 941–943 | tibetan |
| ^a-12 | 946–948 | tibetan |
| ^a-13 | 951–953 | tibetan |
| ^a-14 | 956–958 | tibetan |
| ^a-15 | 963–965 | tibetan |
| ^a-16 | 968–970 | tibetan |
| ^a-17 | 973–975 | tibetan |
| ^a-18 | 978–980 | tibetan |
| ^a-19 | 983–985 | tibetan |
| ^a-20 | 990–992 | tibetan |
| ^a-21 | 995–997 | tibetan |
| ^a-22 | 1000–1002 | tibetan |
| ^a-23 | 1005–1007 | tibetan |
| ^a-24 | 1010–1012 | tibetan |
| ^a-25 | 1017–1020 | tibetan |
| ^a-26 | 1023–1025 | tibetan |
| ^a-27 | 1028–1030 | tibetan |
| ^a-28 | 1033–1035 | tibetan |
| ^a-29 | 1038–1040 | tibetan |
| ^a-30 | 1045–1047 | tibetan |
| ^a-31 | 1050–1052 | tibetan |
| ^a-32 | 1055–1058 | tibetan |
| ^a-33 | 1061–1063 | tibetan |
| ^a-34 | 1066–1068 | tibetan |
| ^a-35 | 1073–1075 | tibetan |
| ^a-36 | 1076–1078 | manual |
| ## ^b-0 | 1081 | manual |
| ^b-1 | — | no Hindi |
| ^b-2 | 1086–1088 | tibetan |
| ^b-3 | 1091–1093 | tibetan |
| ^b-4 | 1096–1098 | tibetan |
| ^b-5 | 1101–1103 | tibetan |
| ^b-6 | 1106–1108 | tibetan |
| ^b-7 | 1113–1115 | tibetan |
| ^b-8 | 1118–1120 | tibetan |
| ^b-9 | 1121–1122 | manual |
| ## ^c-0 | 1125 | manual |
| ^c-1 | — | no Hindi |
| ^c-2 | 1129–1131 | tibetan |
| ^c-3 | 1134–1136 | tibetan |
| ^c-4 | 1139–1141 | tibetan |
| ^c-5 | 1144–1146 | tibetan |
| ^c-6 | 1151–1153 | tibetan |
| ^c-7 | 1156–1158 | tibetan |
| ^c-8 | 1161–1163 | tibetan |
| ^c-9 | 1166–1168 | tibetan |
| ^c-10 | 1169–1170 | manual |
| ## ^d-0 | 1173 | manual |
| ^d-1 | — | no Hindi |
| ^d-2 | 1177–1178 | tibetan |
| ^d-3 | 1181–1183 | tibetan |
| ^d-4 | 1186–1187 | tibetan |
| ^d-5 | 1190–1191 | tibetan |
| ^d-6 | 1194, 1195 | tibetan |
| ^d-7 | 1200–1202 | tibetan |
| ^d-8 | 1205–1206 | tibetan |
| ^d-9 | 1209–1210 | tibetan |
| ^d-10 | 1211–1212 | manual |
| ## ^e-0 | 1215 | manual |
| ^e-1 | 1218 | manual |
| ^e-2 | 1221–1223 | tibetan |
| ^e-3 | 1226–1228 | tibetan |
| ^e-4 | 1231–1233 | tibetan |
| ^e-5 | 1236–1239 | tibetan |
| ^e-6 | 1245–1248 | tibetan |
| ^e-7 | 1252–1256 | tibetan |
| ^e-8 | 1259–1261 | tibetan |
| ^e-9 | 1264–1266 | tibetan |
| ^e-10 | 1272–1276 | split |
| ^e-11 | 1272–1276 | split |
| ^e-12 | 1280–1283 | split |
| ^e-13 | 1280–1283, 1287–1290 | split |
| ^e-14 | 1287–1290 | split |
| ^e-15 | 1293–1296 | tibetan |
| ^e-16 | 1297–1299 | manual |
| ## ^f-0 | 1320 | manual |
| ^f-1 | 1323–1325 | manual |
| ^f-2 | 1328–1330 | manual |
| ^f-3 | 1331–1332 | manual |
| ^f-4 | 1335–1337 | split |
| ^f-5 | 1335–1337 | split |
| ^f-6 | 1338, 1341–1343 | extra, manual |
| ^f-7 | 1344 | manual |
| ## ^g-0 | 1303 | manual |
| ^g-1 | 1305–1306 | tibetan |
| ^g-2 | 1309–1312 | tibetan |
| ^g-3 | 1315–1317 | tibetan |

## Line layout (added 2026-09-30, second pass)

Each Hindi block is now laid out in the same number of lines as its root block, so `translation-alignment-check` passes the line-count check. The wording is unchanged. Every block's text is identical to the first pass once whitespace is removed, and the script checked this for each block.

- **Splits (242 blocks):** break points were picked to keep lines even in length (measured in syllables). Existing line breaks come first, then clause punctuation (`।` `!` `?` `;` `॥`, then `,` `:` `–`, then `)`), and a plain space only as a last resort. Hindi prose is never broken inside a word or inside brackets.
- **Sanskrit Twenty-one Praises:** each half-verse is one long compound, so it is broken at the pāda boundary. That usually falls inside the compound, e.g. `नमः शक्रानलब्रह्म / मरुद्विश्वेश्वरार्चिते ।`. This happens in 30 blocks (^1-64–1-79, ^1-98–1-113 and ^1-132–1-147, not every verse). The uploader joins a block's lines with no separator, so the words are whole on the published page.
- **Offering mantras (^1-57, ^1-89, ^1-123, ^1-176):** one offering per line at the commas, matching the Tibetan's eight mantra lines.
- **Joins (11 blocks):** where the booklet had more lines than the root, lines were joined with a space: ^1-1, ^1-4 (the list of offering materials), ^1-17, ^1-18, ^1-24, ^1-26, ^1-55, ^1-121, ^1-155, ^1-198, ^1-213.
- **Placeholders:** repeated once per root line. `translation-alignment-check` now fails only on "untranslated placeholder in content".

## Meaning review (added 2026-09-30, third pass)

Every block's Hindi was read against its Tibetan block, with the English translation as a cross-check. The Sanskrit Twenty-one Praises were checked mechanically: every block carries the right verse number, १–२१, in all three sets. After the fixes below, `translation-alignment-check` reports `RESULT: OK`, and the English and Chinese files still pass.

**Clauses moved to the block they translate.** Wording is unchanged, checked by script:
- `^1-45–47`: "from one wisdom essence" moved to ^1-45, and "I prostrate and take refuge; I offer body and wealth" moved to ^1-47. It had sat one block late in each case.
- `^1-95` / `^1-120` and `^1-129` / `^1-154`: "while imagining this" stays; "recite the 21 praises three/seven times" moves to the "three times"/"seven times" rubric after the praises.
- `^1-155` / `^1-156`: "whoever wise, with true devotion to Tārā" moved to ^1-155.
- `^1-159` / `^1-160`: the Sanskrit half-line द्वित्रिसप्ताभिवर्तितम् ("recited two, three, seven times") moved to ^1-160.
- `^1-180` / `^1-181`: "thus having praised" / "join both palms and say".
- `^1-206` / `^1-207`: "all obstacles to accomplishing omniscience, harmful spirits, epidemics, illness" moved to ^1-206.

**Filled from the booklet's own rendering of identical Tibetan:** `^1-7` from ^1-194 (ཚར་གསུམ།), `^1-85` and `^1-119` from ^1-153 (मन्त्रमूलमिदं स्तोत्रं…), `^b-1` from ^1-191 (the ten-syllable mantra).

**Drafted by Claude, approved by the vault owner:** `^II-6`, `^1-8`, `^1-19`, `^1-23`, `^1-163`, `^1-165`, `^c-1`, `^d-1`, and the restored mantra in `^1-22`. These are listed in the file's `editorial_notes`; a translator should review them.

**Moved out to `0-INBOX/temp/hi-unaligned-passages.md`:** the `^II-3` attribution, the farewell verse (after ^1-198), the daily-practice section (after ^1-213) and the heading before `^f-6`. The booklet's short section sub-headings were kept.

**OCR repair:** ॐ ॐ ॐ आः हूँ। → ॐ आः हूँ। in `^1-41` and `^1-125`.

**Still different from the Tibetan, kept as delivered:**
- `^II-9`: the booklet's colophon names a different author ("written by Mañjughoṣa… arranged by Jamgön Guṇa") from the root ("written by Pema Dongak Lingpa at Karma Khyentse Rabgye's request"). The booklet was probably translated from a different edition.
- `^f-0`: "गुरु-परम्परा स्तुति एवं मङ्गलाचरण" describes the section; it doesn't translate གྲོལ་འདོན།.
- `^1-40`: the root's "And thus:" slot holds the booklet's sub-heading मण्डल-अर्पण.
- `^1-192`: "after reciting as much as you can" sits with the hundred-syllable rubric, following the booklet's own Tibetan. The root has it at the end of ^1-190.
