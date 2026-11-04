# 「建て付け」マップ 図解画像のプロンプト（ChatGPT用）

2026-11-04 作成。記事 `01-fudousan-touki-hou-tatekata-map.md` に差し込む図7枚＋Instagram用（図1の3:4版）＋見出し画像（別ファイル）。画像の生成はChatGPTで行う。

## 使い方

1. 図ごとに、コードブロックをそのままChatGPTに貼る。画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
2. 色の約束：**表示＝青、権利＝薄い橙**を全図で統一する。7枚を並べたとき色がそろっているか確かめる。
3. 仕上がりを確かめる（下の「確かめること」）。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。
4. ファイル名は `tatekata_zu01.png` 〜 `tatekata_zu07.png`、Instagram用は `tatekata_ig01.png`。

## 確かめること

- 大きさが指定どおりか（図ごとに違う）。
- 文字が、プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。
- 条文番号が、「第39条」のように正しく出ているか（とくに「第73条の2〜第77条」「第97条〜第104条の2」の「の2」）。
- 図番（図1など）が画像に入っていないか。
- 表示は青、権利は薄い橙でそろっているか。
- 背景が不透明か。

文字が何度やっても崩れるときは、各プロンプトの「Words allowed」の行を残したまま「No text」の版（文字なしの棚と絵だけ）を作らせて、文字はCanvaで入れる。

## 図の一覧

| 管理番号 | 内容 | サイズ | 記事の位置 |
|---|---|---|---|
| zu01 | 8つの棚の全体マップ | 1080x1800 | 記事の「画像挿入」マーカー |
| zu02 | 登記簿・登記記録・表題部と権利部 | 1080x1500 | 記事の「画像挿入」マーカー |
| zu03 | 登記ができあがるまでの流れ | 1080x1800 | 記事の「画像挿入」マーカー |
| zu04 | 表示の棚の中身 | 1080x1800 | 記事の「画像挿入」マーカー |
| zu05 | 権利の棚の8つの款 | 1080x1800 | 記事の「画像挿入」マーカー |
| zu06 | 表示と権利の対比 | 1080x1500 | 記事の「画像挿入」マーカー |
| zu07 | 確かめる棚と周辺の棚 | 1080x1500 | 記事の「画像挿入」マーカー |

## 図1：8つの棚の全体マップ（zu01・1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold, two lines): 「不動産登記法の建て付けマップ」 / subtitle in a pale-yellow band: 「第1条〜第164条を8つの棚に分ける」

--- BODY (a cutaway of a library with eight labeled areas; top to bottom) ---
Top row, three small shelf cards side by side (gray-green):
 - 「土台」 with small text 「第1条〜第5条」 and 「目的・定義・権利・順位」
 - 「担い手」 with 「第6条〜第10条」 and 「登記所と登記官」
 - 「記録」 with 「第11条〜第15条」 and 「登記簿と登記記録」
Below it, one wide purple-gray bar: 「共通手続」 with 「第16条〜第26条」 and 「申請・受付・却下」
Middle, two LARGE cards side by side (the heart of the map, each taller than the others):
 - Left, blue: 「表示」 with 「第27条〜第58条」 and 「土地と建物の状況」 (icons: a land plot and a house)
 - Right, pale orange: 「権利」 with 「第59条〜第118条」 and 「所有権・抵当権など」 (icons: a key and a stamp)
Bottom row, two cards side by side (beige-gray):
 - 「確かめる」 with 「第119条〜第150条」 and 「証明書・筆界特定」
 - 「周辺」 with 「第151条〜第164条」 and 「雑則・罰則」

--- FOOTER --- a conclusion band: 「全体像は、8つの棚で見る」

Words allowed on this poster (exactly these strings, nothing else): 「不動産登記法の建て付けマップ」 / 「第1条〜第164条を8つの棚に分ける」 / 「土台」 / 「第1条〜第5条」 / 「目的・定義・権利・順位」 / 「担い手」 / 「第6条〜第10条」 / 「登記所と登記官」 / 「記録」 / 「第11条〜第15条」 / 「登記簿と登記記録」 / 「共通手続」 / 「第16条〜第26条」 / 「申請・受付・却下」 / 「表示」 / 「第27条〜第58条」 / 「土地と建物の状況」 / 「権利」 / 「第59条〜第118条」 / 「所有権・抵当権など」 / 「確かめる」 / 「第119条〜第150条」 / 「証明書・筆界特定」 / 「周辺」 / 「第151条〜第164条」 / 「雑則・罰則」 / 「全体像は、8つの棚で見る」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 不、動、産、登、記、法、建、付、第、条、棚、分、土、台、目、的、定、義、権、利、順、位、担、手、所、官、録、簿、共、通、続、申、請、受、却、下、表、示、地、物、状、況、有、抵、当、確、証、明、書、筆、界、特、周、辺、雑、則、罰、全、体、像、見.
```

## 図2：登記簿・登記記録・表題部と権利部（zu02・1080x1500）

```
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold): 「登記は2種類、帳簿は1冊」 / subtitle band: 「表示は表題部、権利は権利部」

--- BODY ---
Top: a big ledger book labeled 「登記簿」. A friendly clerk icon beside it labeled 「登記官」 writing into the book (no other text on the clerk).
Middle: from the ledger, two sheets come out, one for a land plot icon labeled 「一筆の土地」, one for a house icon labeled 「一個の建物」, with a small caption between them: 「登記記録は1つずつ」.
Bottom: one sheet enlarged and divided into two halves, top and bottom:
 - Upper half, blue: heading 「表題部」, and below it a ribbon 「表示に関する登記」 (icon: a land plot and a house).
 - Lower half, pale orange: heading 「権利部」, and below it a ribbon 「権利に関する登記」 (icon: a key and a stamp).

--- FOOTER --- 「表示は表題部、権利は権利部」

Words allowed on this poster (exactly these strings, nothing else): 「登記は2種類、帳簿は1冊」 / 「表示は表題部、権利は権利部」 / 「登記簿」 / 「登記官」 / 「一筆の土地」 / 「一個の建物」 / 「登記記録は1つずつ」 / 「表題部」 / 「表示に関する登記」 / 「権利部」 / 「権利に関する登記」

Final check before rendering: confirm the canvas is exactly 1080x1500 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 登、記、種、類、帳、簿、冊、表、示、題、部、権、利、官、一、筆、土、地、個、建、物、録、関.
```

## 図3：登記ができあがるまでの流れ（zu03・1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold): 「登記ができあがるまで」 / subtitle band: 「共通手続の棚（第16条〜第26条）」

--- BODY (a vertical flow with arrows pointing downward; five steps as rounded cards) ---
Step 1, two small cards side by side feeding into the same arrow: 「当事者の申請」 (person icon) and 「官庁・公署の嘱託」 (building icon).
Step 2 card: 「受付」 (inbox icon).
Step 3 card, split: left half 「審査」 (magnifier icon); a small branch to the side with a red cross icon and the label 「却下」; and below the card a small blue tag 「表示は登記官の調査」.
Step 4 card: 「登記」 (stamp icon), with a small pale orange tag 「権利は受付番号の順」.
Step 5 card: 「登記識別情報の通知」 (envelope icon).

--- FOOTER --- 「表示でも権利でも、この流れを通る」

Words allowed on this poster (exactly these strings, nothing else): 「登記ができあがるまで」 / 「共通手続の棚（第16条〜第26条）」 / 「当事者の申請」 / 「官庁・公署の嘱託」 / 「受付」 / 「審査」 / 「却下」 / 「表示は登記官の調査」 / 「登記」 / 「権利は受付番号の順」 / 「登記識別情報の通知」 / 「表示でも権利でも、この流れを通る」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 登、記、共、通、手、続、棚、第、条、当、事、者、申、請、官、庁、公、署、嘱、託、受、付、審、査、却、下、表、示、調、権、利、番、号、順、識、別、情、報、知、流.
```

## 図4：表示の棚の中身（zu04・1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold): 「表示の棚の中身」 / subtitle band: 「第27条〜第58条」

--- BODY ---
Top: three small blue tabs in a row: 「通則」 with 「第27条〜第33条」, 「土地」 with 「第34条〜第43条」, 「建物」 with 「第44条〜第58条」.
Middle: a comparison table with two columns 「土地」 and 「建物」 and six rows; each row has a row label on the left and the article strings in the cells (icons: a land plot on the 土地 column header, a house on the 建物 column header):
 - 「表題登記」: 「第36条」 | 「第47条」
 - 「変更」: 「第37条」 | 「第51条」
 - 「更正」: 「第38条」 | 「第53条」
 - 「分筆・合筆／分割・区分・合併」: 「第39条」 | 「第54条」
 - 「合筆・合併の制限」: 「第41条」 | 「第56条」
 - 「滅失」: 「第42条」 | 「第57条」
Bottom: three emphasized bands stacked: red-orange band 「多くは一月以内に申請」, then 「怠ると十万円以下の過料」, then green band 「登記官の職権でもできる」.

--- FOOTER --- none (the bands above are the conclusion).

Words allowed on this poster (exactly these strings, nothing else): 「表示の棚の中身」 / 「第27条〜第58条」 / 「通則」 / 「第27条〜第33条」 / 「土地」 / 「第34条〜第43条」 / 「建物」 / 「第44条〜第58条」 / 「表題登記」 / 「第36条」 / 「第47条」 / 「変更」 / 「第37条」 / 「第51条」 / 「更正」 / 「第38条」 / 「第53条」 / 「分筆・合筆／分割・区分・合併」 / 「第39条」 / 「第54条」 / 「合筆・合併の制限」 / 「第41条」 / 「第56条」 / 「滅失」 / 「第42条」 / 「第57条」 / 「多くは一月以内に申請」 / 「怠ると十万円以下の過料」 / 「登記官の職権でもできる」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 表、示、棚、中、身、第、条、通、則、土、地、建、物、題、登、記、変、更、正、分、筆、合、割、区、併、制、限、滅、失、多、一、月、以、内、申、請、怠、十、万、円、下、過、料、官、職、権.
```

## 図5：権利の棚の8つの款（zu05・1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold): 「権利の棚の8つの款」 / subtitle band: 「第59条〜第118条」

--- BODY (eight small pale-orange cards in a 2-column by 4-row grid; each has an icon, the card name, and the article range) ---
 - 「通則」 「第59条〜第73条」 and small text 「共同申請」 (icon: two hands)
 - 「所有権」 「第73条の2〜第77条」 and small text 「保存の登記」 (icon: a key)
 - 「用益権」 「第78条〜第82条」 and small text 「地上権・賃借権など」 (icon: a house with a person)
 - 「担保権等」 「第83条〜第96条」 and small text 「抵当権・質権など」 (icon: a bank building)
 - 「信託」 「第97条〜第104条の2」 (icon: a handshake)
 - 「仮登記」 「第105条〜第110条」 (icon: a pencil sketch stamp)
 - 「仮処分」 「第111条〜第114条」 (icon: a padlock)
 - 「官庁又は公署が関与する登記等」 「第115条〜第118条」 (icon: a government building)

--- FOOTER --- 「通則の次に、権利の種類ごとに並ぶ」

Words allowed on this poster (exactly these strings, nothing else): 「権利の棚の8つの款」 / 「第59条〜第118条」 / 「通則」 / 「第59条〜第73条」 / 「共同申請」 / 「所有権」 / 「第73条の2〜第77条」 / 「保存の登記」 / 「用益権」 / 「第78条〜第82条」 / 「地上権・賃借権など」 / 「担保権等」 / 「第83条〜第96条」 / 「抵当権・質権など」 / 「信託」 / 「第97条〜第104条の2」 / 「仮登記」 / 「第105条〜第110条」 / 「仮処分」 / 「第111条〜第114条」 / 「官庁又は公署が関与する登記等」 / 「第115条〜第118条」 / 「通則の次に、権利の種類ごとに並ぶ」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 権、利、棚、款、第、条、通、則、共、同、申、請、所、有、保、存、登、記、用、益、地、上、賃、借、担、等、抵、当、質、信、託、仮、処、分、官、庁、又、公、署、関、与、次、種、類、並.
```

## 図6：表示と権利の対比（zu06・1080x1500）

```
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold): 「表示と権利の違い」

--- BODY (a two-column comparison; left column blue 「表示に関する登記」, right column pale orange 「権利に関する登記」; five rows with a row label in the center strip) ---
 - Row 「記録される場所」: left 「表題部」 | right 「権利部」
 - Row 「登記するもの」: left 「土地と建物の状況」 | right 「所有権・抵当権など」
 - Row 「申請」: left 「表題部所有者など」 | right 「原則、共同申請」
 - Row 「職権」: left 「登記官ができる」 | right 「申請か嘱託が必要」
 - Row 「期限」: left 「多くは一月以内」 | right 「原則なし」, with a small note under the right cell: 「相続は三年以内」「氏名・住所の変更は二年以内」
 - Row 「順位」: left blank cell with a gray dash icon | right 「登記の前後」

--- FOOTER --- 「期限のある権利の登記は、例外として覚える」

Words allowed on this poster (exactly these strings, nothing else): 「表示と権利の違い」 / 「表示に関する登記」 / 「権利に関する登記」 / 「記録される場所」 / 「表題部」 / 「権利部」 / 「登記するもの」 / 「土地と建物の状況」 / 「所有権・抵当権など」 / 「申請」 / 「表題部所有者など」 / 「原則、共同申請」 / 「職権」 / 「登記官ができる」 / 「申請か嘱託が必要」 / 「期限」 / 「多くは一月以内」 / 「原則なし」 / 「相続は三年以内」 / 「氏名・住所の変更は二年以内」 / 「順位」 / 「登記の前後」 / 「期限のある権利の登記は、例外として覚える」

Final check before rendering: confirm the canvas is exactly 1080x1500 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 表、示、権、利、違、関、登、記、録、場、所、題、部、土、地、建、物、状、況、有、抵、当、申、請、者、原、則、共、同、職、官、嘱、託、必、要、期、限、多、一、月、以、内、相、続、三、年、氏、名、住、変、更、二、順、位、前、後、例、外、覚.
```

## 図7：確かめる棚と周辺の棚（zu07・1080x1500）

```
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold): 「確かめる棚と周辺の棚」

--- BODY (two shelf blocks stacked; each block has two cards) ---
Upper block, beige-gray, heading band 「確かめる」 with 「第119条〜第150条」:
 - Card 「証明・図面の交付」 with 「第119条〜第122条」 and small text 「何人も請求できる」 (icon: a certificate and a map)
 - Card 「筆界特定」 with 「第123条〜第150条」 and small text 「筆界の位置を特定」 (icon: two land plots with a boundary line and a marker)
Lower block, gray, heading band 「周辺」 with 「第151条〜第164条」:
 - Card 「雑則」 with 「第151条〜第158条」
 - Card 「罰則」 with 「第159条〜第164条」 and small text 「第164条は過料」 (icon: a yen coin)

--- FOOTER --- 「登記を調べる・境を決める・守らせる」

Words allowed on this poster (exactly these strings, nothing else): 「確かめる棚と周辺の棚」 / 「確かめる」 / 「第119条〜第150条」 / 「証明・図面の交付」 / 「第119条〜第122条」 / 「何人も請求できる」 / 「筆界特定」 / 「第123条〜第150条」 / 「筆界の位置を特定」 / 「周辺」 / 「第151条〜第164条」 / 「雑則」 / 「第151条〜第158条」 / 「罰則」 / 「第159条〜第164条」 / 「第164条は過料」 / 「登記を調べる・境を決める・守らせる」

Final check before rendering: confirm the canvas is exactly 1080x1500 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 確、棚、周、辺、第、条、証、明、図、面、交、付、何、人、請、求、筆、界、特、定、位、置、雑、則、罰、過、料、登、記、調、境、決、守.
```

## Instagram用：図1の3:4版（tatekata_ig01・1080x1440）

カードの並びは図1と同じ。縦が短いので余白を詰める。

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold, two lines): 「不動産登記法の建て付けマップ」 / subtitle in a pale-yellow band: 「第1条〜第164条を8つの棚に分ける」

--- BODY (a cutaway of a library with eight labeled areas; top to bottom) ---
Top row, three small shelf cards side by side (gray-green):
 - 「土台」 with small text 「第1条〜第5条」 and 「目的・定義・権利・順位」
 - 「担い手」 with 「第6条〜第10条」 and 「登記所と登記官」
 - 「記録」 with 「第11条〜第15条」 and 「登記簿と登記記録」
Below it, one wide purple-gray bar: 「共通手続」 with 「第16条〜第26条」 and 「申請・受付・却下」
Middle, two LARGE cards side by side (the heart of the map, each taller than the others):
 - Left, blue: 「表示」 with 「第27条〜第58条」 and 「土地と建物の状況」 (icons: a land plot and a house)
 - Right, pale orange: 「権利」 with 「第59条〜第118条」 and 「所有権・抵当権など」 (icons: a key and a stamp)
Bottom row, two cards side by side (beige-gray):
 - 「確かめる」 with 「第119条〜第150条」 and 「証明書・筆界特定」
 - 「周辺」 with 「第151条〜第164条」 and 「雑則・罰則」

--- FOOTER --- a conclusion band: 「全体像は、8つの棚で見る」

Words allowed on this poster (exactly these strings, nothing else): 「不動産登記法の建て付けマップ」 / 「第1条〜第164条を8つの棚に分ける」 / 「土台」 / 「第1条〜第5条」 / 「目的・定義・権利・順位」 / 「担い手」 / 「第6条〜第10条」 / 「登記所と登記官」 / 「記録」 / 「第11条〜第15条」 / 「登記簿と登記記録」 / 「共通手続」 / 「第16条〜第26条」 / 「申請・受付・却下」 / 「表示」 / 「第27条〜第58条」 / 「土地と建物の状況」 / 「権利」 / 「第59条〜第118条」 / 「所有権・抵当権など」 / 「確かめる」 / 「第119条〜第150条」 / 「証明書・筆界特定」 / 「周辺」 / 「第151条〜第164条」 / 「雑則・罰則」 / 「全体像は、8つの棚で見る」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 不、動、産、登、記、法、建、付、第、条、棚、分、土、台、目、的、定、義、権、利、順、位、担、手、所、官、録、簿、共、通、続、申、請、受、却、下、表、示、地、物、状、況、有、抵、当、確、証、明、書、筆、界、特、周、辺、雑、則、罰、全、体、像、見.

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version. Do not draw any account name, handle, URL or call-to-action text.
```

## Instagram用：図1の4:5版（tatekata_ig01_45・1080x1350）

2026-11-04 追加（ユーザー指示。8つの棚のマップだけ、4:5でも作る）。カードの並びは図1と同じ。3:4版より縦が90px短いので、カードの間隔をさらに詰める。フィードの投稿は4:5（1080×1350）も使えるが、プロフィールのグリッドでは上下がわずかに切れる（`note-unei/instagram/image-spec.md`）。大事な要素は上下の余白（60px）の内側に置く。

```
Create a Japanese-language infographic, portrait layout, 1080x1350 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a library / bookshelf motif as the visual theme (shelves, books, drawers), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・の are allowed ONLY inside the given strings (for example 第1条〜第5条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. The two main colors for the law structure: blue for 表示 (physical state of land and buildings) and pale orange for 権利 (rights); use the same two colors in every poster of this set.

--- HEADER ---
Title (large, bold, two lines): 「不動産登記法の建て付けマップ」 / subtitle in a pale-yellow band: 「第1条〜第164条を8つの棚に分ける」

--- BODY (a cutaway of a library with eight labeled areas; top to bottom) ---
Top row, three small shelf cards side by side (gray-green):
 - 「土台」 with small text 「第1条〜第5条」 and 「目的・定義・権利・順位」
 - 「担い手」 with 「第6条〜第10条」 and 「登記所と登記官」
 - 「記録」 with 「第11条〜第15条」 and 「登記簿と登記記録」
Below it, one wide purple-gray bar: 「共通手続」 with 「第16条〜第26条」 and 「申請・受付・却下」
Middle, two LARGE cards side by side (the heart of the map, each taller than the others):
 - Left, blue: 「表示」 with 「第27条〜第58条」 and 「土地と建物の状況」 (icons: a land plot and a house)
 - Right, pale orange: 「権利」 with 「第59条〜第118条」 and 「所有権・抵当権など」 (icons: a key and a stamp)
Bottom row, two cards side by side (beige-gray):
 - 「確かめる」 with 「第119条〜第150条」 and 「証明書・筆界特定」
 - 「周辺」 with 「第151条〜第164条」 and 「雑則・罰則」

--- FOOTER --- a conclusion band: 「全体像は、8つの棚で見る」

Words allowed on this poster (exactly these strings, nothing else): 「不動産登記法の建て付けマップ」 / 「第1条〜第164条を8つの棚に分ける」 / 「土台」 / 「第1条〜第5条」 / 「目的・定義・権利・順位」 / 「担い手」 / 「第6条〜第10条」 / 「登記所と登記官」 / 「記録」 / 「第11条〜第15条」 / 「登記簿と登記記録」 / 「共通手続」 / 「第16条〜第26条」 / 「申請・受付・却下」 / 「表示」 / 「第27条〜第58条」 / 「土地と建物の状況」 / 「権利」 / 「第59条〜第118条」 / 「所有権・抵当権など」 / 「確かめる」 / 「第119条〜第150条」 / 「証明書・筆界特定」 / 「周辺」 / 「第151条〜第164条」 / 「雑則・罰則」 / 「全体像は、8つの棚で見る」

Final check before rendering: confirm the canvas is exactly 1080x1350 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 不、動、産、登、記、法、建、付、第、条、棚、分、土、台、目、的、定、義、権、利、順、位、担、手、所、官、録、簿、共、通、続、申、請、受、却、下、表、示、地、物、状、況、有、抵、当、確、証、明、書、筆、界、特、周、辺、雑、則、罰、全、体、像、見.

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1350 pixels (4:5). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 60px at the top and bottom, because the feed and the profile grid crop the image. Make the type slightly larger than the note version. Do not draw any account name, handle, URL or call-to-action text.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1440）のプロンプトは `02-header-image-prompts.md` にある。
