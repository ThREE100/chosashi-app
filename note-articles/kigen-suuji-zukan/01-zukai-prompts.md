# 「数字の図鑑」 図解画像のプロンプト（ChatGPT用・note用とInstagram用）

2026-11-04 作成（`src/gen_prompts.py` で作る。手で直さない）。記事 `01-fudousan-touki-hou-kigen-suuji-zukan.md` に差し込む図7枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1440・3:4）の2種類**を用意した。画像の生成と目視確認はChatGPTで行う（未実施）。

## 使い方

1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。内容（文字）は同じで、大きさと余白だけ違う。
2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
3. 色の約束：**青＝表示の登記、薄い橙＝権利の登記、赤橙＝過料・罰則、灰緑＝保存期間、紫灰＝その他**。7枚を並べたとき色がそろっているか確かめる。
4. 仕上がりを確かめる（下の「確かめること」）。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。
5. ファイル名は、note用が `kigen_zu01.png` 〜 `kigen_zu07.png`、Instagram用が `kigen_ig01.png` 〜 `kigen_ig07.png`。

## 確かめること

- 大きさが指定どおりか（note用は図ごとに違う、Instagram用は1080×1440）。
- 文字が、各プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。
- 条文番号が正しく出ているか（「第70条の2」の「の2」、「第164条第2項」など）。
- 図番（図1など）が画像に入っていないか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下72px）の内側にあるか。アカウント名・URLが入っていないか。
- 背景が不透明か。

文字が何度やっても崩れるときは、「Words allowed」の行を残したまま「No text」の版（文字なしの引き出しや階段の絵だけ）を作らせて、文字はCanvaで入れる。

## 図の一覧

| 管理番号 | 内容 | note用のサイズ | Instagram用のサイズ |
|---|---|---|---|
| zu01 | 数字の7つの引き出し | 1080x1800 | 1080x1440 |
| zu02 | 一月以内の登記と起算点 | 1080x1800 | 1080x1440 |
| zu03 | 相続の三年と氏名・住所の二年 | 1080x1600 | 1080x1440 |
| zu04 | 過料と罰則の金額 | 1080x1700 | 1080x1440 |
| zu05 | 十年・二十年・三十年 | 1080x1700 | 1080x1440 |
| zu06 | 保存期間の階段 | 1080x1900 | 1080x1440 |
| zu07 | その他の数字 | 1080x1500 | 1080x1440 |

## 図1：数字の7つの引き出し（zu01）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「不動産登記法の数字の図鑑」 / subtitle band: 「数字は7つの引き出しに分ける」

--- BODY (a cabinet of seven labeled drawers, stacked top to bottom; each drawer = one rounded card with an icon, the drawer name and its representative numbers) ---
 - Blue drawer: 「表示の登記の期限」 with 「一月以内」
 - Pale orange drawer: 「権利の登記の期限」 with 「三年以内」 and 「二年以内」
 - Red-orange drawer: 「過料」 with 「十万円以下」 and 「五万円以下」
 - Red-orange drawer: 「罰則」 with 「二年以下の拘禁刑」 and 「百万円以下の罰金」
 - Pale orange drawer: 「時の経過で単独申請」 with 「十年」 「二十年」 「三十年」
 - Gray-green drawer: 「保存期間」 with 「永久」 and 「一年」
 - Purple-gray drawer: 「その他の数字」 with 「四親等内」

--- FOOTER --- conclusion band: 「何の登記か、いつから数えるか」

Words allowed on this poster (exactly these strings, nothing else): 「不動産登記法の数字の図鑑」 / 「数字は7つの引き出しに分ける」 / 「表示の登記の期限」 / 「一月以内」 / 「権利の登記の期限」 / 「三年以内」 / 「二年以内」 / 「過料」 / 「十万円以下」 / 「五万円以下」 / 「罰則」 / 「二年以下の拘禁刑」 / 「百万円以下の罰金」 / 「時の経過で単独申請」 / 「十年」 / 「二十年」 / 「三十年」 / 「保存期間」 / 「永久」 / 「一年」 / 「その他の数字」 / 「四親等内」 / 「何の登記か、いつから数えるか」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 不、動、産、登、記、法、数、字、図、鑑、引、出、分、表、示、期、限、一、月、以、内、権、利、三、年、二、過、料、十、万、円、下、五、罰、則、拘、禁、刑、百、金、時、経、単、独、申、請、保、存、間、永、久、他、四、親、等、何.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「不動産登記法の数字の図鑑」 / subtitle band: 「数字は7つの引き出しに分ける」

--- BODY (a cabinet of seven labeled drawers, stacked top to bottom; each drawer = one rounded card with an icon, the drawer name and its representative numbers) ---
 - Blue drawer: 「表示の登記の期限」 with 「一月以内」
 - Pale orange drawer: 「権利の登記の期限」 with 「三年以内」 and 「二年以内」
 - Red-orange drawer: 「過料」 with 「十万円以下」 and 「五万円以下」
 - Red-orange drawer: 「罰則」 with 「二年以下の拘禁刑」 and 「百万円以下の罰金」
 - Pale orange drawer: 「時の経過で単独申請」 with 「十年」 「二十年」 「三十年」
 - Gray-green drawer: 「保存期間」 with 「永久」 and 「一年」
 - Purple-gray drawer: 「その他の数字」 with 「四親等内」

--- FOOTER --- conclusion band: 「何の登記か、いつから数えるか」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「不動産登記法の数字の図鑑」 / 「数字は7つの引き出しに分ける」 / 「表示の登記の期限」 / 「一月以内」 / 「権利の登記の期限」 / 「三年以内」 / 「二年以内」 / 「過料」 / 「十万円以下」 / 「五万円以下」 / 「罰則」 / 「二年以下の拘禁刑」 / 「百万円以下の罰金」 / 「時の経過で単独申請」 / 「十年」 / 「二十年」 / 「三十年」 / 「保存期間」 / 「永久」 / 「一年」 / 「その他の数字」 / 「四親等内」 / 「何の登記か、いつから数えるか」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 不、動、産、登、記、法、数、字、図、鑑、引、出、分、表、示、期、限、一、月、以、内、権、利、三、年、二、過、料、十、万、円、下、五、罰、則、拘、禁、刑、百、金、時、経、単、独、申、請、保、存、間、永、久、他、四、親、等、何.
```

## 図2：一月以内の登記と起算点（zu02）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「表示の登記は一月以内」 / subtitle band: 「起算点が登記ごとに違う」

--- BODY (a table in blue tones; two column headers 「土地」 and 「建物」 with a land plot icon and a house icon; rows with a row label on the left and the cell text) ---
 - Row 「表題登記」: 「第36条　所有権の取得の日」 | 「第47条　所有権の取得の日」
 - Row 「変更」: 「第37条　変更があった日」 | 「第51条　変更があった日」
 - Row 「滅失」: 「第42条　滅失の日」 | 「第57条　滅失の日」
 - Row 「合体」: gray dash icon | 「第49条　合体の日」
 - Row 「規約の廃止」: gray dash icon | 「第58条　規約の廃止の日」
Below the table, one red-orange band: 「怠ると十万円以下の過料」

--- FOOTER --- 「一月は同じ、数え始めが違う」

Words allowed on this poster (exactly these strings, nothing else): 「表示の登記は一月以内」 / 「起算点が登記ごとに違う」 / 「土地」 / 「建物」 / 「表題登記」 / 「第36条　所有権の取得の日」 / 「第47条　所有権の取得の日」 / 「変更」 / 「第37条　変更があった日」 / 「第51条　変更があった日」 / 「滅失」 / 「第42条　滅失の日」 / 「第57条　滅失の日」 / 「合体」 / 「第49条　合体の日」 / 「規約の廃止」 / 「第58条　規約の廃止の日」 / 「怠ると十万円以下の過料」 / 「一月は同じ、数え始めが違う」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 表、示、登、記、一、月、以、内、起、算、点、違、土、地、建、物、題、第、条、所、有、権、取、得、日、変、更、滅、失、合、体、規、約、廃、止、怠、十、万、円、下、過、料、同、数、始.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「表示の登記は一月以内」 / subtitle band: 「起算点が登記ごとに違う」

--- BODY (a table in blue tones; two column headers 「土地」 and 「建物」 with a land plot icon and a house icon; rows with a row label on the left and the cell text) ---
 - Row 「表題登記」: 「第36条　所有権の取得の日」 | 「第47条　所有権の取得の日」
 - Row 「変更」: 「第37条　変更があった日」 | 「第51条　変更があった日」
 - Row 「滅失」: 「第42条　滅失の日」 | 「第57条　滅失の日」
 - Row 「合体」: gray dash icon | 「第49条　合体の日」
 - Row 「規約の廃止」: gray dash icon | 「第58条　規約の廃止の日」
Below the table, one red-orange band: 「怠ると十万円以下の過料」

--- FOOTER --- 「一月は同じ、数え始めが違う」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「表示の登記は一月以内」 / 「起算点が登記ごとに違う」 / 「土地」 / 「建物」 / 「表題登記」 / 「第36条　所有権の取得の日」 / 「第47条　所有権の取得の日」 / 「変更」 / 「第37条　変更があった日」 / 「第51条　変更があった日」 / 「滅失」 / 「第42条　滅失の日」 / 「第57条　滅失の日」 / 「合体」 / 「第49条　合体の日」 / 「規約の廃止」 / 「第58条　規約の廃止の日」 / 「怠ると十万円以下の過料」 / 「一月は同じ、数え始めが違う」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 表、示、登、記、一、月、以、内、起、算、点、違、土、地、建、物、題、第、条、所、有、権、取、得、日、変、更、滅、失、合、体、規、約、廃、止、怠、十、万、円、下、過、料、同、数、始.
```

## 図3：相続の三年と氏名・住所の二年（zu03）

### note用（1080x1600）

```
Create a Japanese-language infographic, portrait layout, 1080x1600 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「権利の登記の期限は2つだけ」 / subtitle band: 「相続は三年、氏名・住所は二年」

--- BODY (two large pale-orange cards side by side or stacked; each with an icon, a heading, a big number and the starting point) ---
 - Card A, icon: a family and a house. Heading 「相続による所有権の移転」, big 「三年以内」, caption 「第76条の2」. Two small lines under it: 「相続の開始と取得を知った日から」 and 「遺産の分割の日から」
 - Card B, icon: a name tag and an address sign. Heading 「氏名・住所の変更」, big 「二年以内」, caption 「第76条の5」. One small line: 「変更があった日から」

--- FOOTER --- 「権利の登記に期限はない、この2つを除いて」

Words allowed on this poster (exactly these strings, nothing else): 「権利の登記の期限は2つだけ」 / 「相続は三年、氏名・住所は二年」 / 「相続による所有権の移転」 / 「三年以内」 / 「第76条の2」 / 「相続の開始と取得を知った日から」 / 「遺産の分割の日から」 / 「氏名・住所の変更」 / 「二年以内」 / 「第76条の5」 / 「変更があった日から」 / 「権利の登記に期限はない、この2つを除いて」

Final check before rendering: confirm the canvas is exactly 1080x1600 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 権、利、登、記、期、限、相、続、三、年、氏、名、住、所、二、有、移、転、以、内、第、条、開、始、取、得、知、日、遺、産、分、割、変、更、除.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「権利の登記の期限は2つだけ」 / subtitle band: 「相続は三年、氏名・住所は二年」

--- BODY (two large pale-orange cards side by side or stacked; each with an icon, a heading, a big number and the starting point) ---
 - Card A, icon: a family and a house. Heading 「相続による所有権の移転」, big 「三年以内」, caption 「第76条の2」. Two small lines under it: 「相続の開始と取得を知った日から」 and 「遺産の分割の日から」
 - Card B, icon: a name tag and an address sign. Heading 「氏名・住所の変更」, big 「二年以内」, caption 「第76条の5」. One small line: 「変更があった日から」

--- FOOTER --- 「権利の登記に期限はない、この2つを除いて」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「権利の登記の期限は2つだけ」 / 「相続は三年、氏名・住所は二年」 / 「相続による所有権の移転」 / 「三年以内」 / 「第76条の2」 / 「相続の開始と取得を知った日から」 / 「遺産の分割の日から」 / 「氏名・住所の変更」 / 「二年以内」 / 「第76条の5」 / 「変更があった日から」 / 「権利の登記に期限はない、この2つを除いて」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 権、利、登、記、期、限、相、続、三、年、氏、名、住、所、二、有、移、転、以、内、第、条、開、始、取、得、知、日、遺、産、分、割、変、更、除.
```

## 図4：過料と罰則の金額（zu04）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「怠ったとき・違反したときの金額」 / subtitle band: 「過料と罰則は別の条文」

--- BODY (a staircase from small to large amounts, red-orange tones; each step is a card with an amount, the article and a short label) ---
 - Step 1 (smallest): 「五万円以下の過料」 / 「第164条第2項」 / 「第76条の5の申請を怠る」
 - Step 2: 「十万円以下の過料」 / 「第164条第1項」 / 「申請義務のある登記を怠る」
 - Step 3: 「三十万円以下の罰金」 / 「第162条」 / 「検査を拒み、妨げる」
 - Step 4: 「五十万円以下の罰金」 / 「第160条・第161条」 / 「二年以下の拘禁刑または」
 - Step 5 (largest): 「百万円以下の罰金」 / 「第159条」 / 「二年以下の拘禁刑または」
A small label near the steps 1 and 2: 「過料」, and near the steps 3 to 5: 「罰則」.

--- FOOTER --- 「氏名・住所の変更だけ半額」

Words allowed on this poster (exactly these strings, nothing else): 「怠ったとき・違反したときの金額」 / 「過料と罰則は別の条文」 / 「五万円以下の過料」 / 「第164条第2項」 / 「第76条の5の申請を怠る」 / 「十万円以下の過料」 / 「第164条第1項」 / 「申請義務のある登記を怠る」 / 「三十万円以下の罰金」 / 「第162条」 / 「検査を拒み、妨げる」 / 「五十万円以下の罰金」 / 「第160条・第161条」 / 「二年以下の拘禁刑または」 / 「百万円以下の罰金」 / 「第159条」 / 「過料」 / 「罰則」 / 「氏名・住所の変更だけ半額」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 怠、違、反、金、額、過、料、罰、則、別、条、文、五、万、円、以、下、第、項、申、請、十、義、務、登、記、三、検、査、拒、妨、二、年、拘、禁、刑、百、氏、名、住、所、変、更、半.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「怠ったとき・違反したときの金額」 / subtitle band: 「過料と罰則は別の条文」

--- BODY (a staircase from small to large amounts, red-orange tones; each step is a card with an amount, the article and a short label) ---
 - Step 1 (smallest): 「五万円以下の過料」 / 「第164条第2項」 / 「第76条の5の申請を怠る」
 - Step 2: 「十万円以下の過料」 / 「第164条第1項」 / 「申請義務のある登記を怠る」
 - Step 3: 「三十万円以下の罰金」 / 「第162条」 / 「検査を拒み、妨げる」
 - Step 4: 「五十万円以下の罰金」 / 「第160条・第161条」 / 「二年以下の拘禁刑または」
 - Step 5 (largest): 「百万円以下の罰金」 / 「第159条」 / 「二年以下の拘禁刑または」
A small label near the steps 1 and 2: 「過料」, and near the steps 3 to 5: 「罰則」.

--- FOOTER --- 「氏名・住所の変更だけ半額」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「怠ったとき・違反したときの金額」 / 「過料と罰則は別の条文」 / 「五万円以下の過料」 / 「第164条第2項」 / 「第76条の5の申請を怠る」 / 「十万円以下の過料」 / 「第164条第1項」 / 「申請義務のある登記を怠る」 / 「三十万円以下の罰金」 / 「第162条」 / 「検査を拒み、妨げる」 / 「五十万円以下の罰金」 / 「第160条・第161条」 / 「二年以下の拘禁刑または」 / 「百万円以下の罰金」 / 「第159条」 / 「過料」 / 「罰則」 / 「氏名・住所の変更だけ半額」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 怠、違、反、金、額、過、料、罰、則、別、条、文、五、万、円、以、下、第、項、申、請、十、義、務、登、記、三、検、査、拒、妨、二、年、拘、禁、刑、百、氏、名、住、所、変、更、半.
```

## 図5：十年・二十年・三十年（zu05）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「年月が経つと単独で申請できる」 / subtitle band: 「登記の抹消の特則」

--- BODY (a vertical timeline in pale orange with three milestones; each milestone is a card) ---
 - Milestone 「十年」 with 「第69条の2」, 「買戻しの特約に関する登記」, 「契約の日から」
 - Milestone 「二十年」 with 「第70条第4項」, 「先取特権・質権・抵当権」, 「弁済期から、そのあと全額を供託」
 - Milestone 「三十年」 with 「第70条の2」, 「解散した法人の担保権」, 「弁済期から、解散の日からも」
At the right of the timeline, a small icon of one person with a stamp and the label 「登記権利者が単独で申請」.

--- FOOTER --- 「条件はそれぞれ違う」

Words allowed on this poster (exactly these strings, nothing else): 「年月が経つと単独で申請できる」 / 「登記の抹消の特則」 / 「十年」 / 「第69条の2」 / 「買戻しの特約に関する登記」 / 「契約の日から」 / 「二十年」 / 「第70条第4項」 / 「先取特権・質権・抵当権」 / 「弁済期から、そのあと全額を供託」 / 「三十年」 / 「第70条の2」 / 「解散した法人の担保権」 / 「弁済期から、解散の日からも」 / 「登記権利者が単独で申請」 / 「条件はそれぞれ違う」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 年、月、経、単、独、申、請、登、記、抹、消、特、則、十、第、条、買、戻、約、関、契、日、二、項、先、取、権、質、抵、当、弁、済、期、全、額、供、託、三、解、散、法、人、担、保、利、者、件、違.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「年月が経つと単独で申請できる」 / subtitle band: 「登記の抹消の特則」

--- BODY (a vertical timeline in pale orange with three milestones; each milestone is a card) ---
 - Milestone 「十年」 with 「第69条の2」, 「買戻しの特約に関する登記」, 「契約の日から」
 - Milestone 「二十年」 with 「第70条第4項」, 「先取特権・質権・抵当権」, 「弁済期から、そのあと全額を供託」
 - Milestone 「三十年」 with 「第70条の2」, 「解散した法人の担保権」, 「弁済期から、解散の日からも」
At the right of the timeline, a small icon of one person with a stamp and the label 「登記権利者が単独で申請」.

--- FOOTER --- 「条件はそれぞれ違う」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「年月が経つと単独で申請できる」 / 「登記の抹消の特則」 / 「十年」 / 「第69条の2」 / 「買戻しの特約に関する登記」 / 「契約の日から」 / 「二十年」 / 「第70条第4項」 / 「先取特権・質権・抵当権」 / 「弁済期から、そのあと全額を供託」 / 「三十年」 / 「第70条の2」 / 「解散した法人の担保権」 / 「弁済期から、解散の日からも」 / 「登記権利者が単独で申請」 / 「条件はそれぞれ違う」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 年、月、経、単、独、申、請、登、記、抹、消、特、則、十、第、条、買、戻、約、関、契、日、二、項、先、取、権、質、抵、当、弁、済、期、全、額、供、託、三、解、散、法、人、担、保、利、者、件、違.
```

## 図6：保存期間の階段（zu06）

### note用（1080x1900）

```
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「登記所の保存期間」 / subtitle band: 「永久から一年までの階段」

--- BODY (a descending staircase in gray-green tones; each step is a card with the period on the left and two or three items on the right) ---
 - 「永久」: 「登記記録」 「地図」 「建物所在図」
 - 「五十年」: 「土地の閉鎖登記記録」
 - 「三十年」: 「建物の閉鎖登記記録」 「申請情報・添付情報」 「閉鎖した図面」
 - 「二十年」: 「信託目録」
 - 「十年」: 「共同担保目録」 「受付帳」
 - 「五年」: 「職権表示登記等事件簿」 「法定相続情報一覧図つづり込み帳」
 - 「三年」: 「不正登記防止申出書類つづり込み帳」
 - 「一年」: 「登記事務日記帳」
A callout pointing at the 「永久」 step and the 「三十年」 step: 「図面は閉鎖すると三十年」

--- FOOTER --- 「建物所在図だけは閉鎖しても永久」

Words allowed on this poster (exactly these strings, nothing else): 「登記所の保存期間」 / 「永久から一年までの階段」 / 「永久」 / 「登記記録」 / 「地図」 / 「建物所在図」 / 「五十年」 / 「土地の閉鎖登記記録」 / 「三十年」 / 「建物の閉鎖登記記録」 / 「申請情報・添付情報」 / 「閉鎖した図面」 / 「二十年」 / 「信託目録」 / 「十年」 / 「共同担保目録」 / 「受付帳」 / 「五年」 / 「職権表示登記等事件簿」 / 「法定相続情報一覧図つづり込み帳」 / 「三年」 / 「不正登記防止申出書類つづり込み帳」 / 「一年」 / 「登記事務日記帳」 / 「図面は閉鎖すると三十年」 / 「建物所在図だけは閉鎖しても永久」

Final check before rendering: confirm the canvas is exactly 1080x1900 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 登、記、所、保、存、期、間、永、久、一、年、階、段、録、地、図、建、物、在、五、十、土、閉、鎖、三、申、請、情、報、添、付、面、二、信、託、目、共、同、担、受、帳、職、権、表、示、等、事、件、簿、法、定、相、続、覧、込、不、正、防、止、出、書、類、務、日.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「登記所の保存期間」 / subtitle band: 「永久から一年までの階段」

--- BODY (a descending staircase in gray-green tones; each step is a card with the period on the left and two or three items on the right) ---
 - 「永久」: 「登記記録」 「地図」 「建物所在図」
 - 「五十年」: 「土地の閉鎖登記記録」
 - 「三十年」: 「建物の閉鎖登記記録」 「申請情報・添付情報」 「閉鎖した図面」
 - 「二十年」: 「信託目録」
 - 「十年」: 「共同担保目録」 「受付帳」
 - 「五年」: 「職権表示登記等事件簿」 「法定相続情報一覧図つづり込み帳」
 - 「三年」: 「不正登記防止申出書類つづり込み帳」
 - 「一年」: 「登記事務日記帳」
A callout pointing at the 「永久」 step and the 「三十年」 step: 「図面は閉鎖すると三十年」

--- FOOTER --- 「建物所在図だけは閉鎖しても永久」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「登記所の保存期間」 / 「永久から一年までの階段」 / 「永久」 / 「登記記録」 / 「地図」 / 「建物所在図」 / 「五十年」 / 「土地の閉鎖登記記録」 / 「三十年」 / 「建物の閉鎖登記記録」 / 「申請情報・添付情報」 / 「閉鎖した図面」 / 「二十年」 / 「信託目録」 / 「十年」 / 「共同担保目録」 / 「受付帳」 / 「五年」 / 「職権表示登記等事件簿」 / 「法定相続情報一覧図つづり込み帳」 / 「三年」 / 「不正登記防止申出書類つづり込み帳」 / 「一年」 / 「登記事務日記帳」 / 「図面は閉鎖すると三十年」 / 「建物所在図だけは閉鎖しても永久」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 登、記、所、保、存、期、間、永、久、一、年、階、段、録、地、図、建、物、在、五、十、土、閉、鎖、三、申、請、情、報、添、付、面、二、信、託、目、共、同、担、受、帳、職、権、表、示、等、事、件、簿、法、定、相、続、覧、込、不、正、防、止、出、書、類、務、日.
```

## 図7：その他の数字（zu07）

### note用（1080x1500）

```
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「条文に散らばる数字」 / subtitle band: 「ほかの数字もここで確認」

--- BODY (five purple-gray cards in a column; each card has an icon, the number in large type, the article and a short label) ---
 - 「十個」 / 「第3条」 / 「登記できる権利」
 - 「四親等内」 / 「第10条」 / 「登記官の親族の申請は不可」
 - 「一月以内の期間」 / 「第71条第1項」 / 「異議を述べる期間」
 - 「三日以内」 / 「第157条第2項」 / 「審査請求の事件の送付」
 - 「二年」 / 「第127条第3項」 / 「筆界調査委員の任期」

--- FOOTER --- 「一つずつ別の条文にある」

Words allowed on this poster (exactly these strings, nothing else): 「条文に散らばる数字」 / 「ほかの数字もここで確認」 / 「十個」 / 「第3条」 / 「登記できる権利」 / 「四親等内」 / 「第10条」 / 「登記官の親族の申請は不可」 / 「一月以内の期間」 / 「第71条第1項」 / 「異議を述べる期間」 / 「三日以内」 / 「第157条第2項」 / 「審査請求の事件の送付」 / 「二年」 / 「第127条第3項」 / 「筆界調査委員の任期」 / 「一つずつ別の条文にある」

Final check before rendering: confirm the canvas is exactly 1080x1500 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 条、文、散、数、字、確、認、十、個、第、登、記、権、利、四、親、等、内、官、族、申、請、不、可、一、月、以、期、間、項、異、議、述、三、日、審、査、求、事、件、送、付、二、年、筆、界、調、委、員、任、別.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use a "picture book / specimen drawer" motif (a cabinet of small labeled drawers, index tabs), drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示の登記 (土地・建物の状況), pale orange = 権利の登記, red-orange = 過料・罰則, gray-green = 保存期間, purple-gray = その他.

--- HEADER ---
Title (large, bold): 「条文に散らばる数字」 / subtitle band: 「ほかの数字もここで確認」

--- BODY (five purple-gray cards in a column; each card has an icon, the number in large type, the article and a short label) ---
 - 「十個」 / 「第3条」 / 「登記できる権利」
 - 「四親等内」 / 「第10条」 / 「登記官の親族の申請は不可」
 - 「一月以内の期間」 / 「第71条第1項」 / 「異議を述べる期間」
 - 「三日以内」 / 「第157条第2項」 / 「審査請求の事件の送付」
 - 「二年」 / 「第127条第3項」 / 「筆界調査委員の任期」

--- FOOTER --- 「一つずつ別の条文にある」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「条文に散らばる数字」 / 「ほかの数字もここで確認」 / 「十個」 / 「第3条」 / 「登記できる権利」 / 「四親等内」 / 「第10条」 / 「登記官の親族の申請は不可」 / 「一月以内の期間」 / 「第71条第1項」 / 「異議を述べる期間」 / 「三日以内」 / 「第157条第2項」 / 「審査請求の事件の送付」 / 「二年」 / 「第127条第3項」 / 「筆界調査委員の任期」 / 「一つずつ別の条文にある」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 条、文、散、数、字、確、認、十、個、第、登、記、権、利、四、親、等、内、官、族、申、請、不、可、一、月、以、期、間、項、異、議、述、三、日、審、査、求、事、件、送、付、二、年、筆、界、調、委、員、任、別.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1440）のプロンプトは `02-header-image-prompts.md` にある。
