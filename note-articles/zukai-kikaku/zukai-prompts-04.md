# 条文の読み方 図解 図解画像のプロンプト（ChatGPT用・note用とInstagram用）

作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。記事 `04-joubun-no-yomikata.md` に差し込む図3枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1440・3:4）の2種類**を用意した。

## 使い方

1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。文字は同じで、大きさと余白だけ違う。
2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
3. 色の約束：**表示に関する登記＝青、権利に関する登記＝薄い橙**。ほかの色は意味を持たせない（手順は薄い黄と水色）。同じ企画の図を並べたとき、色がそろっているか確かめる。
4. ファイル名は、note用が `kz04_zu01.png` から、Instagram用が `kz04_ig01.png` から。
5. 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

## 確かめること

- 大きさが指定どおりか（note用は図ごとに違う、Instagram用は1080×1440）。
- 文字が、各プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。
- 条文番号・項番号が正しく出ているか。
- 図番（図1など）が画像に入っていないか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下72px）の内側にあるか。アカウント名・URLが入っていないか。
- 背景が不透明か。

文字が何度やっても崩れるときは、「Words allowed」の行を残したまま「No text」の版（文字なしの枠と絵だけ）を作らせて、文字はCanvaで入れる。

## 図の一覧

| 管理番号 | 内容 | note用のサイズ | Instagram用のサイズ |
|---|---|---|---|
| zu01 | 本文とただし書 | 1080x1700 | 1080x1440 |
| zu02 | 除きと次に掲げる | 1080x1700 | 1080x1440 |
| zu03 | 前項・準用・みなす | 1080x1800 | 1080x1440 |

## 図1：本文とただし書（zu01）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: an open statute book with a magnifying glass, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「ただし書は、例外の合図」 / subtitle band: 「第25条を例に」

--- BODY (a statute-reading diagram; a large pale card in the middle split into two parts, upper part = main text, lower part = proviso, joined by a small down arrow) ---
 - Small tag above the card: 「第25条　申請の却下」
 - Upper part, tab 「本文」 (blue): 「登記官は、次の場合には却下しなければならない」
 - Lower part, tab 「ただし書」 (pale orange): 「補正できる不備を、期間内に補正したときは、この限りでない」
 - Left margin label on the upper part: 「原則」 ; left margin label on the lower part: 「例外」
 - Under the card, three small reading steps in a row: 「まず本文」 「次にただし書」 「例外に当たるか確かめる」

--- FOOTER --- conclusion band: 「この限りでない＝そこは適用しない」

Words allowed on this poster (exactly these strings, nothing else): 「ただし書は、例外の合図」 / 「第25条を例に」 / 「第25条　申請の却下」 / 「本文」 / 「登記官は、次の場合には却下しなければならない」 / 「ただし書」 / 「補正できる不備を、期間内に補正したときは、この限りでない」 / 「原則」 / 「例外」 / 「まず本文」 / 「次にただし書」 / 「例外に当たるか確かめる」 / 「この限りでない＝そこは適用しない」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 書、例、外、合、図、第、条、申、請、却、下、本、文、登、記、官、次、場、補、正、不、備、期、間、内、限、原、則、当、確、適、用.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: an open statute book with a magnifying glass, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「ただし書は、例外の合図」 / subtitle band: 「第25条を例に」

--- BODY (a statute-reading diagram; a large pale card in the middle split into two parts, upper part = main text, lower part = proviso, joined by a small down arrow) ---
 - Small tag above the card: 「第25条　申請の却下」
 - Upper part, tab 「本文」 (blue): 「登記官は、次の場合には却下しなければならない」
 - Lower part, tab 「ただし書」 (pale orange): 「補正できる不備を、期間内に補正したときは、この限りでない」
 - Left margin label on the upper part: 「原則」 ; left margin label on the lower part: 「例外」
 - Under the card, three small reading steps in a row: 「まず本文」 「次にただし書」 「例外に当たるか確かめる」

--- FOOTER --- conclusion band: 「この限りでない＝そこは適用しない」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「ただし書は、例外の合図」 / 「第25条を例に」 / 「第25条　申請の却下」 / 「本文」 / 「登記官は、次の場合には却下しなければならない」 / 「ただし書」 / 「補正できる不備を、期間内に補正したときは、この限りでない」 / 「原則」 / 「例外」 / 「まず本文」 / 「次にただし書」 / 「例外に当たるか確かめる」 / 「この限りでない＝そこは適用しない」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 書、例、外、合、図、第、条、申、請、却、下、本、文、登、記、官、次、場、補、正、不、備、期、間、内、限、原、則、当、確、適、用.
```

## 図2：除きと次に掲げる（zu02）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: an open statute book with a magnifying glass, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「除きと次に掲げる」 / subtitle band: 「第16条と第41条を例に」

--- BODY (two statute cards stacked) ---
 - Card 1 (blue), tag 「第16条第1項」: sentence 「法令に別段の定めがある場合を除き、申請または嘱託がなければ、登記はできない」; below it two small boxes: 「原則　申請または嘱託が必要」 and 「除く　別段の定めがあるとき」
 - Card 2 (blue), tag 「第41条」: sentence 「次に掲げる合筆の登記は、することができない」; below it a short list of labeled boxes: 「一号　相互に接続していない土地」 「二号　地目または地番区域が異なる土地」 「三号　所有者が異なる土地」 and a small box 「ほか三つの号」
 - A small reading hint under card 2: 「号のどれかに当たれば、できない」

--- FOOTER --- conclusion band: 「除きは例外を外す、次に掲げるは号を読む」

Words allowed on this poster (exactly these strings, nothing else): 「除きと次に掲げる」 / 「第16条と第41条を例に」 / 「第16条第1項」 / 「法令に別段の定めがある場合を除き、申請または嘱託がなければ、登記はできない」 / 「原則　申請または嘱託が必要」 / 「除く　別段の定めがあるとき」 / 「第41条」 / 「次に掲げる合筆の登記は、することができない」 / 「一号　相互に接続していない土地」 / 「二号　地目または地番区域が異なる土地」 / 「三号　所有者が異なる土地」 / 「ほか三つの号」 / 「号のどれかに当たれば、できない」 / 「除きは例外を外す、次に掲げるは号を読む」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 除、次、掲、第、条、例、項、法、令、別、段、定、場、合、申、請、嘱、託、登、記、原、則、必、要、筆、一、号、相、互、接、続、土、地、二、目、番、区、域、異、三、所、有、者、当、外、読.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: an open statute book with a magnifying glass, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「除きと次に掲げる」 / subtitle band: 「第16条と第41条を例に」

--- BODY (two statute cards stacked) ---
 - Card 1 (blue), tag 「第16条第1項」: sentence 「法令に別段の定めがある場合を除き、申請または嘱託がなければ、登記はできない」; below it two small boxes: 「原則　申請または嘱託が必要」 and 「除く　別段の定めがあるとき」
 - Card 2 (blue), tag 「第41条」: sentence 「次に掲げる合筆の登記は、することができない」; below it a short list of labeled boxes: 「一号　相互に接続していない土地」 「二号　地目または地番区域が異なる土地」 「三号　所有者が異なる土地」 and a small box 「ほか三つの号」
 - A small reading hint under card 2: 「号のどれかに当たれば、できない」

--- FOOTER --- conclusion band: 「除きは例外を外す、次に掲げるは号を読む」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「除きと次に掲げる」 / 「第16条と第41条を例に」 / 「第16条第1項」 / 「法令に別段の定めがある場合を除き、申請または嘱託がなければ、登記はできない」 / 「原則　申請または嘱託が必要」 / 「除く　別段の定めがあるとき」 / 「第41条」 / 「次に掲げる合筆の登記は、することができない」 / 「一号　相互に接続していない土地」 / 「二号　地目または地番区域が異なる土地」 / 「三号　所有者が異なる土地」 / 「ほか三つの号」 / 「号のどれかに当たれば、できない」 / 「除きは例外を外す、次に掲げるは号を読む」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 除、次、掲、第、条、例、項、法、令、別、段、定、場、合、申、請、嘱、託、登、記、原、則、必、要、筆、一、号、相、互、接、続、土、地、二、目、番、区、域、異、三、所、有、者、当、外、読.
```

## 図3：前項・準用・みなす（zu03）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: an open statute book with a magnifying glass, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「前項・準用・みなす」 / subtitle band: 「指す先を確かめる」

--- BODY (three statute cards stacked, each with an arrow icon pointing to the thing it refers to) ---
 - Card 1 (blue), tag 「第51条第2項」: phrase 「前項の登記事項について変更があった後に…」; small arrow label 「前項＝すぐ前の第1項」
 - Card 2 (blue), tag 「第54条第3項」: phrase 「第40条の規定は、権利の登記がある建物の分割・区分の登記をするときに準用する」; small arrow label 「準用＝同じ規定を当てはめる」; small caption 「第40条は分筆に伴う権利の消滅の登記」
 - Card 3 (pale orange), tag 「第19条第2項」: phrase 「その前後が明らかでないときは、同時にされたものとみなす」; small arrow label 「みなす＝事実と違っても、そう扱う」

--- FOOTER --- conclusion band: 「指す先の条文を、必ず開いて読む」

Words allowed on this poster (exactly these strings, nothing else): 「前項・準用・みなす」 / 「指す先を確かめる」 / 「第51条第2項」 / 「前項の登記事項について変更があった後に…」 / 「前項＝すぐ前の第1項」 / 「第54条第3項」 / 「第40条の規定は、権利の登記がある建物の分割・区分の登記をするときに準用する」 / 「準用＝同じ規定を当てはめる」 / 「第40条は分筆に伴う権利の消滅の登記」 / 「第19条第2項」 / 「その前後が明らかでないときは、同時にされたものとみなす」 / 「みなす＝事実と違っても、そう扱う」 / 「指す先の条文を、必ず開いて読む」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 前、項、準、用、指、先、確、第、条、登、記、事、変、更、後、規、定、権、利、建、物、分、割、区、同、当、筆、伴、消、滅、明、時、実、違、扱、文、必、開、読.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: an open statute book with a magnifying glass, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「前項・準用・みなす」 / subtitle band: 「指す先を確かめる」

--- BODY (three statute cards stacked, each with an arrow icon pointing to the thing it refers to) ---
 - Card 1 (blue), tag 「第51条第2項」: phrase 「前項の登記事項について変更があった後に…」; small arrow label 「前項＝すぐ前の第1項」
 - Card 2 (blue), tag 「第54条第3項」: phrase 「第40条の規定は、権利の登記がある建物の分割・区分の登記をするときに準用する」; small arrow label 「準用＝同じ規定を当てはめる」; small caption 「第40条は分筆に伴う権利の消滅の登記」
 - Card 3 (pale orange), tag 「第19条第2項」: phrase 「その前後が明らかでないときは、同時にされたものとみなす」; small arrow label 「みなす＝事実と違っても、そう扱う」

--- FOOTER --- conclusion band: 「指す先の条文を、必ず開いて読む」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「前項・準用・みなす」 / 「指す先を確かめる」 / 「第51条第2項」 / 「前項の登記事項について変更があった後に…」 / 「前項＝すぐ前の第1項」 / 「第54条第3項」 / 「第40条の規定は、権利の登記がある建物の分割・区分の登記をするときに準用する」 / 「準用＝同じ規定を当てはめる」 / 「第40条は分筆に伴う権利の消滅の登記」 / 「第19条第2項」 / 「その前後が明らかでないときは、同時にされたものとみなす」 / 「みなす＝事実と違っても、そう扱う」 / 「指す先の条文を、必ず開いて読む」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 前、項、準、用、指、先、確、第、条、登、記、事、変、更、後、規、定、権、利、建、物、分、割、区、同、当、筆、伴、消、滅、明、時、実、違、扱、文、必、開、読.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1440）は `header-image-prompts.md`、キャプションは `instagram-captions.md`。
