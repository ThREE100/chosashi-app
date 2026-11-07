# 似た用語の対比図鑑 図解画像のプロンプト（ChatGPT用・note用とInstagram用）

作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。記事 `02-taihi-zukan.md` に差し込む図3枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1440・3:4）の2種類**を用意した。

## 使い方

1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。文字は同じで、大きさと余白だけ違う。
2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
3. 色の約束：**表示に関する登記＝青、権利に関する登記＝薄い橙**。ほかの色は意味を持たせない（手順は薄い黄と水色）。同じ企画の図を並べたとき、色がそろっているか確かめる。
4. ファイル名は、note用が `kz02_zu01.png` から、Instagram用が `kz02_ig01.png` から。
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
| zu01 | 分筆・合筆と分割・合併 | 1080x1700 | 1080x1440 |
| zu02 | 区分と分割、合体と合併 | 1080x1700 | 1080x1440 |
| zu03 | 変更と更正、表題登記と所有権の保存 | 1080x1700 | 1080x1440 |

## 図1：分筆・合筆と分割・合併（zu01）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a pair of picture-book pages facing each other, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地は筆、建物は個で数える」 / subtitle band: 「分筆・合筆と分割・合併」

--- BODY (a two-column comparison; left column header 「土地」 with a land plot icon, right column header 「建物」 with a house icon; two rows, each row has a row label on the left edge) ---
 - Row label 「分ける」:
   left cell: 「分筆」, line 「一筆の土地を二筆以上に分ける」, tag 「第39条」
   right cell: 「分割」, line 「附属建物を別の一個の建物にする」, tag 「第54条」
 - Row label 「つなぐ」:
   left cell: 「合筆」, line 「二筆以上の土地を一筆にする」, tag 「第39条・第41条」
   right cell: 「合併」, line 「他の建物の附属建物にする、または一個にする」, tag 「第54条・第56条」

--- FOOTER --- conclusion band: 「土地は一筆、建物は一個で登記記録をつくる」

LAYOUT LOCK (critical): the header and the bottom edge are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group (content starts at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the content fills the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if the poster has exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

Words allowed on this poster (exactly these strings, nothing else): 「土地は筆、建物は個で数える」 / 「分筆・合筆と分割・合併」 / 「土地」 / 「建物」 / 「分ける」 / 「分筆」 / 「一筆の土地を二筆以上に分ける」 / 「第39条」 / 「分割」 / 「附属建物を別の一個の建物にする」 / 「第54条」 / 「つなぐ」 / 「合筆」 / 「二筆以上の土地を一筆にする」 / 「第39条・第41条」 / 「合併」 / 「他の建物の附属建物にする、または一個にする」 / 「第54条・第56条」 / 「土地は一筆、建物は一個で登記記録をつくる」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Confirm the header and bottom edges follow LAYOUT LOCK (no empty band, edges aligned, no empty grid slot). Pay special attention to the kanji: 土、地、筆、建、物、個、数、分、合、割、併、一、二、以、上、第、条、附、属、別、他、登、記、録.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a pair of picture-book pages facing each other, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地は筆、建物は個で数える」 / subtitle band: 「分筆・合筆と分割・合併」

--- BODY (a two-column comparison; left column header 「土地」 with a land plot icon, right column header 「建物」 with a house icon; two rows, each row has a row label on the left edge) ---
 - Row label 「分ける」:
   left cell: 「分筆」, line 「一筆の土地を二筆以上に分ける」, tag 「第39条」
   right cell: 「分割」, line 「附属建物を別の一個の建物にする」, tag 「第54条」
 - Row label 「つなぐ」:
   left cell: 「合筆」, line 「二筆以上の土地を一筆にする」, tag 「第39条・第41条」
   right cell: 「合併」, line 「他の建物の附属建物にする、または一個にする」, tag 「第54条・第56条」

--- FOOTER --- conclusion band: 「土地は一筆、建物は一個で登記記録をつくる」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

LAYOUT LOCK (critical): the header and the bottom edge are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group (content starts at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the content fills the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if the poster has exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

Words allowed on this poster (exactly these strings, nothing else): 「土地は筆、建物は個で数える」 / 「分筆・合筆と分割・合併」 / 「土地」 / 「建物」 / 「分ける」 / 「分筆」 / 「一筆の土地を二筆以上に分ける」 / 「第39条」 / 「分割」 / 「附属建物を別の一個の建物にする」 / 「第54条」 / 「つなぐ」 / 「合筆」 / 「二筆以上の土地を一筆にする」 / 「第39条・第41条」 / 「合併」 / 「他の建物の附属建物にする、または一個にする」 / 「第54条・第56条」 / 「土地は一筆、建物は一個で登記記録をつくる」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Confirm the header and bottom edges follow LAYOUT LOCK (no empty band, edges aligned, no empty grid slot). Pay special attention to the kanji: 土、地、筆、建、物、個、数、分、合、割、併、一、二、以、上、第、条、附、属、別、他、登、記、録.
```

## 図2：区分と分割、合体と合併（zu02）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a pair of picture-book pages facing each other, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「区分と分割、合体と合併」 / subtitle band: 「似ているが別の手続」

--- BODY (two comparison blocks stacked; each block has two cards side by side separated by a thin vertical divider line; all cards blue) ---
 - Block 1, cards:
   left card: heading 「建物の分割」, line 「附属建物を、別の一個の建物にする」
   right card: heading 「建物の区分」, line 「建物の部分を、区分建物にする」
   below the block, a small tag: 「どちらも第54条」
 - Block 2, cards:
   left card: heading 「合体」, line 「二以上の建物が一個の建物になった事実」, tag 「第49条　合体の日から一月以内」
   right card: heading 「合併」, line 「登記の手続で、附属建物にする、または一個にする」, tag 「第54条　申請の期限の定めなし」

--- FOOTER --- conclusion band: 「合体は事実、合併は手続」

LAYOUT LOCK (critical): the header and the bottom edge are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group (content starts at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the content fills the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if the poster has exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

Words allowed on this poster (exactly these strings, nothing else): 「区分と分割、合体と合併」 / 「似ているが別の手続」 / 「建物の分割」 / 「附属建物を、別の一個の建物にする」 / 「建物の区分」 / 「建物の部分を、区分建物にする」 / 「どちらも第54条」 / 「合体」 / 「二以上の建物が一個の建物になった事実」 / 「第49条　合体の日から一月以内」 / 「合併」 / 「登記の手続で、附属建物にする、または一個にする」 / 「第54条　申請の期限の定めなし」 / 「合体は事実、合併は手続」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Confirm the header and bottom edges follow LAYOUT LOCK (no empty band, edges aligned, no empty grid slot). Pay special attention to the kanji: 区、分、割、合、体、併、似、別、手、続、建、物、附、属、一、個、部、第、条、二、以、上、事、実、日、月、内、登、記、申、請、期、限、定.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a pair of picture-book pages facing each other, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「区分と分割、合体と合併」 / subtitle band: 「似ているが別の手続」

--- BODY (two comparison blocks stacked; each block has two cards side by side separated by a thin vertical divider line; all cards blue) ---
 - Block 1, cards:
   left card: heading 「建物の分割」, line 「附属建物を、別の一個の建物にする」
   right card: heading 「建物の区分」, line 「建物の部分を、区分建物にする」
   below the block, a small tag: 「どちらも第54条」
 - Block 2, cards:
   left card: heading 「合体」, line 「二以上の建物が一個の建物になった事実」, tag 「第49条　合体の日から一月以内」
   right card: heading 「合併」, line 「登記の手続で、附属建物にする、または一個にする」, tag 「第54条　申請の期限の定めなし」

--- FOOTER --- conclusion band: 「合体は事実、合併は手続」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

LAYOUT LOCK (critical): the header and the bottom edge are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group (content starts at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the content fills the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if the poster has exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

Words allowed on this poster (exactly these strings, nothing else): 「区分と分割、合体と合併」 / 「似ているが別の手続」 / 「建物の分割」 / 「附属建物を、別の一個の建物にする」 / 「建物の区分」 / 「建物の部分を、区分建物にする」 / 「どちらも第54条」 / 「合体」 / 「二以上の建物が一個の建物になった事実」 / 「第49条　合体の日から一月以内」 / 「合併」 / 「登記の手続で、附属建物にする、または一個にする」 / 「第54条　申請の期限の定めなし」 / 「合体は事実、合併は手続」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Confirm the header and bottom edges follow LAYOUT LOCK (no empty band, edges aligned, no empty grid slot). Pay special attention to the kanji: 区、分、割、合、体、併、似、別、手、続、建、物、附、属、一、個、部、第、条、二、以、上、事、実、日、月、内、登、記、申、請、期、限、定.
```

## 図3：変更と更正、表題登記と所有権の保存（zu03）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a pair of picture-book pages facing each other, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「変更と更正、表題と保存」 / subtitle band: 「いつの誤りか、どの部分の最初か」

--- BODY (two comparison blocks stacked) ---
 - Block 1 (blue cards):
   left card: heading 「変更」, line 「登記したあとに、現実が変わった」, tag 「第37条・第51条　一月以内」
   right card: heading 「更正」, line 「登記したときから、内容が誤っていた」, tag 「第38条・第53条　期限の定めなし」
 - Block 2:
   left card (blue): heading 「表題登記」, line 「表題部に最初にされる登記」, tag 「第2条第20号」
   right card (pale orange): heading 「所有権の保存」, line 「権利部に最初にされる所有権の登記」, tag 「第74条」

--- FOOTER --- conclusion band: 「表題部は表示、権利部は権利」

LAYOUT LOCK (critical): the header and the bottom edge are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group (content starts at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the content fills the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if the poster has exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

Words allowed on this poster (exactly these strings, nothing else): 「変更と更正、表題と保存」 / 「いつの誤りか、どの部分の最初か」 / 「変更」 / 「登記したあとに、現実が変わった」 / 「第37条・第51条　一月以内」 / 「更正」 / 「登記したときから、内容が誤っていた」 / 「第38条・第53条　期限の定めなし」 / 「表題登記」 / 「表題部に最初にされる登記」 / 「第2条第20号」 / 「所有権の保存」 / 「権利部に最初にされる所有権の登記」 / 「第74条」 / 「表題部は表示、権利部は権利」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Confirm the header and bottom edges follow LAYOUT LOCK (no empty band, edges aligned, no empty grid slot). Pay special attention to the kanji: 変、更、正、表、題、保、存、誤、部、分、最、初、登、記、現、実、第、条、一、月、以、内、容、期、限、定、号、所、有、権、利、示.
```

### Instagram用（1080x1440・3:4）

```
Create a Japanese-language infographic, portrait layout, 1080x1440 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a pair of picture-book pages facing each other, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「変更と更正、表題と保存」 / subtitle band: 「いつの誤りか、どの部分の最初か」

--- BODY (two comparison blocks stacked) ---
 - Block 1 (blue cards):
   left card: heading 「変更」, line 「登記したあとに、現実が変わった」, tag 「第37条・第51条　一月以内」
   right card: heading 「更正」, line 「登記したときから、内容が誤っていた」, tag 「第38条・第53条　期限の定めなし」
 - Block 2:
   left card (blue): heading 「表題登記」, line 「表題部に最初にされる登記」, tag 「第2条第20号」
   right card (pale orange): heading 「所有権の保存」, line 「権利部に最初にされる所有権の登記」, tag 「第74条」

--- FOOTER --- conclusion band: 「表題部は表示、権利部は権利」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1440px of height. Do not draw any account name, handle, URL or call-to-action text.

LAYOUT LOCK (critical): the header and the bottom edge are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group (content starts at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the content fills the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if the poster has exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

Words allowed on this poster (exactly these strings, nothing else): 「変更と更正、表題と保存」 / 「いつの誤りか、どの部分の最初か」 / 「変更」 / 「登記したあとに、現実が変わった」 / 「第37条・第51条　一月以内」 / 「更正」 / 「登記したときから、内容が誤っていた」 / 「第38条・第53条　期限の定めなし」 / 「表題登記」 / 「表題部に最初にされる登記」 / 「第2条第20号」 / 「所有権の保存」 / 「権利部に最初にされる所有権の登記」 / 「第74条」 / 「表題部は表示、権利部は権利」

Final check before rendering: confirm the canvas is exactly 1080x1440 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Confirm the header and bottom edges follow LAYOUT LOCK (no empty band, edges aligned, no empty grid slot). Pay special attention to the kanji: 変、更、正、表、題、保、存、誤、部、分、最、初、登、記、現、実、第、条、一、月、以、内、容、期、限、定、号、所、有、権、利、示.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1440）は `header-image-prompts.md`、キャプションは `instagram-captions.md`。
