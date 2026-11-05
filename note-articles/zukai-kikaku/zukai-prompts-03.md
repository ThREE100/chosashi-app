# 表示に関する登記の添付情報 早見図 図解画像のプロンプト（ChatGPT用・note用とInstagram用）

作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。記事 `03-tenpu-jouhou-hayami.md` に差し込む図2枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1350・4:5）の2種類**を用意した。

## 使い方

1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。文字は同じで、大きさと余白だけ違う。
2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。
3. 色の約束：**表示に関する登記＝青、権利に関する登記＝薄い橙**。ほかの色は意味を持たせない（手順は薄い黄と水色）。同じ企画の図を並べたとき、色がそろっているか確かめる。
4. ファイル名は、note用が `kz03_zu01.png` から、Instagram用が `kz03_ig01.png` から。
5. 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

## 確かめること

- 大きさが指定どおりか（note用は図ごとに違う、Instagram用は1080×1350）。
- 文字が、各プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。
- 条文番号・項番号が正しく出ているか。
- 図番（図1など）が画像に入っていないか。
- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下68px）の内側にあるか。アカウント名・URLが入っていないか。
- 背景が不透明か。

文字が何度やっても崩れるときは、「Words allowed」の行を残したまま「No text」の版（文字なしの枠と絵だけ）を作らせて、文字はCanvaで入れる。

## 図の一覧

| 管理番号 | 内容 | note用のサイズ | Instagram用のサイズ |
|---|---|---|---|
| zu01 | 土地の登記と添付情報 | 1080x1700 | 1080x1350 |
| zu02 | 建物の登記と添付情報 | 1080x1800 | 1080x1350 |

## 図1：土地の登記と添付情報（zu01）

### note用（1080x1700）

```
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a clipboard and paper clips, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地の登記に付ける情報」 / subtitle band: 「令別表で決まる」

--- BODY (a table with a blue header row and a first column of registration names; four attachment columns; each cell holds one mark) ---
 - Column headers: 「土地所在図」 「地積測量図」 「所有権証明情報」 「住所証明情報」
 - Row 「土地の表題登記」 with small tag 「令別表四の項」: 「○」 「○」 「○」 「○」
 - Row 「地目の変更・更正」 with small tag 「五の項」: 「－」 「－」 「－」 「－」
 - Row 「地積の変更・更正」 with small tag 「六の項」: 「－」 「○」 「－」 「－」
 - Row 「分筆」 with small tag 「八の項」: 「－」 「○」 「－」 「－」
 - Row 「合筆」 with small tag 「九の項」: 「－」 「－」 「－」 「－」
 - Legend under the table: 「○　別表に定めがある」 「－　通常は別表に定めがない」

--- FOOTER --- conclusion band: 「代理人が申請するなら代理権限証明情報も」

Words allowed on this poster (exactly these strings, nothing else): 「土地の登記に付ける情報」 / 「令別表で決まる」 / 「土地所在図」 / 「地積測量図」 / 「所有権証明情報」 / 「住所証明情報」 / 「土地の表題登記」 / 「令別表四の項」 / 「○」 / 「地目の変更・更正」 / 「五の項」 / 「－」 / 「地積の変更・更正」 / 「六の項」 / 「分筆」 / 「八の項」 / 「合筆」 / 「九の項」 / 「○　別表に定めがある」 / 「－　通常は別表に定めがない」 / 「代理人が申請するなら代理権限証明情報も」

Final check before rendering: confirm the canvas is exactly 1080x1700 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 土、地、登、記、付、情、報、令、別、表、決、所、在、図、積、測、量、有、権、証、明、住、題、四、項、目、変、更、正、五、六、分、筆、八、合、九、定、通、常、代、理、人、申、請、限.
```

### Instagram用（1080x1350・4:5）

```
Create a Japanese-language infographic, portrait layout, 1080x1350 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a clipboard and paper clips, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「土地の登記に付ける情報」 / subtitle band: 「令別表で決まる」

--- BODY (a table with a blue header row and a first column of registration names; four attachment columns; each cell holds one mark) ---
 - Column headers: 「土地所在図」 「地積測量図」 「所有権証明情報」 「住所証明情報」
 - Row 「土地の表題登記」 with small tag 「令別表四の項」: 「○」 「○」 「○」 「○」
 - Row 「地目の変更・更正」 with small tag 「五の項」: 「－」 「－」 「－」 「－」
 - Row 「地積の変更・更正」 with small tag 「六の項」: 「－」 「○」 「－」 「－」
 - Row 「分筆」 with small tag 「八の項」: 「－」 「○」 「－」 「－」
 - Row 「合筆」 with small tag 「九の項」: 「－」 「－」 「－」 「－」
 - Legend under the table: 「○　別表に定めがある」 「－　通常は別表に定めがない」

--- FOOTER --- conclusion band: 「代理人が申請するなら代理権限証明情報も」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1350 pixels (4:5). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 68px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1350px of height. BOTTOM ALIGNMENT (critical): the bottom edges of the cards or boxes must line up: the last card of every column (or the last row) ends on one and the same horizontal line at the bottom margin, cards in the same row have the same height, and the gaps between cards are equal; absorb any spare height inside the cards (larger illustration area, vertical centring, padding), never as a ragged gap under one column. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「土地の登記に付ける情報」 / 「令別表で決まる」 / 「土地所在図」 / 「地積測量図」 / 「所有権証明情報」 / 「住所証明情報」 / 「土地の表題登記」 / 「令別表四の項」 / 「○」 / 「地目の変更・更正」 / 「五の項」 / 「－」 / 「地積の変更・更正」 / 「六の項」 / 「分筆」 / 「八の項」 / 「合筆」 / 「九の項」 / 「○　別表に定めがある」 / 「－　通常は別表に定めがない」 / 「代理人が申請するなら代理権限証明情報も」

Final check before rendering: confirm the canvas is exactly 1080x1350 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 土、地、登、記、付、情、報、令、別、表、決、所、在、図、積、測、量、有、権、証、明、住、題、四、項、目、変、更、正、五、六、分、筆、八、合、九、定、通、常、代、理、人、申、請、限.
```

## 図2：建物の登記と添付情報（zu02）

### note用（1080x1800）

```
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a clipboard and paper clips, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「建物の登記に付ける情報」 / subtitle band: 「令別表で決まる」

--- BODY (a table with a blue header row and a first column of registration names; four attachment columns; each cell holds one mark) ---
 - Column headers: 「建物図面」 「各階平面図」 「所有権証明情報」 「住所証明情報」
 - Row 「建物の表題登記」 with small tag 「令別表十二の項」: 「○」 「○」 「○」 「○」
 - Row 「合体による登記等」 with small tag 「十三の項」: 「○」 「○」 「○」 「○」
 - Row 「表題部の変更・更正」 with small tag 「十四の項」: 「△」 「△」 「△」 「－」
 - Row 「分割・区分・合併」 with small tag 「十六の項」: 「○」 「○」 「－」 「－」
 - Row 「滅失」 with small tag 「別表に項なし」: 「－」 「－」 「－」 「－」
 - Legend under the table: 「○　別表に定めがある」 「△　変更の内容による」 「－　通常は別表に定めがない」

--- FOOTER --- conclusion band: 「代理人が申請するなら代理権限証明情報も」

Words allowed on this poster (exactly these strings, nothing else): 「建物の登記に付ける情報」 / 「令別表で決まる」 / 「建物図面」 / 「各階平面図」 / 「所有権証明情報」 / 「住所証明情報」 / 「建物の表題登記」 / 「令別表十二の項」 / 「○」 / 「合体による登記等」 / 「十三の項」 / 「表題部の変更・更正」 / 「十四の項」 / 「△」 / 「－」 / 「分割・区分・合併」 / 「十六の項」 / 「滅失」 / 「別表に項なし」 / 「○　別表に定めがある」 / 「△　変更の内容による」 / 「－　通常は別表に定めがない」 / 「代理人が申請するなら代理権限証明情報も」

Final check before rendering: confirm the canvas is exactly 1080x1800 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 建、物、登、記、付、情、報、令、別、表、決、図、面、各、階、平、所、有、権、証、明、住、題、十、二、項、合、体、等、三、部、変、更、正、四、分、割、区、併、六、滅、失、定、内、容、通、常、代、理、人、申、請、限.
```

### Instagram用（1080x1350・4:5）

```
Create a Japanese-language infographic, portrait layout, 1080x1350 pixels,
clean flat-design illustration style with soft pastel colors (blue, green, beige, gray, pale orange), rounded card sections, a friendly explainer-graphic feel. Use the motif given at the end of this sentence: a clipboard and paper clips, drawn simply.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings (for example 第36条). No Latin letters anywhere.

ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere on the poster is the strings written in 「」 below (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface or shows its meaning with an icon.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. No figure number, no panel number, no page number.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel background, no checkerboard, no unpainted edge. Fill every corner and margin with a pale warm-beige background.

Keep generous margins (at least 48px), large readable type, and a clear uncluttered layout. Dark navy text on light cards. Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.

--- HEADER ---
Title (large, bold): 「建物の登記に付ける情報」 / subtitle band: 「令別表で決まる」

--- BODY (a table with a blue header row and a first column of registration names; four attachment columns; each cell holds one mark) ---
 - Column headers: 「建物図面」 「各階平面図」 「所有権証明情報」 「住所証明情報」
 - Row 「建物の表題登記」 with small tag 「令別表十二の項」: 「○」 「○」 「○」 「○」
 - Row 「合体による登記等」 with small tag 「十三の項」: 「○」 「○」 「○」 「○」
 - Row 「表題部の変更・更正」 with small tag 「十四の項」: 「△」 「△」 「△」 「－」
 - Row 「分割・区分・合併」 with small tag 「十六の項」: 「○」 「○」 「－」 「－」
 - Row 「滅失」 with small tag 「別表に項なし」: 「－」 「－」 「－」 「－」
 - Legend under the table: 「○　別表に定めがある」 「△　変更の内容による」 「－　通常は別表に定めがない」

--- FOOTER --- conclusion band: 「代理人が申請するなら代理権限証明情報も」

INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1350 pixels (4:5). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 68px at the top and bottom, because the profile grid crops the image. Make the type slightly larger than the note version and compress the spacing so that everything fits in 1350px of height. BOTTOM ALIGNMENT (critical): the bottom edges of the cards or boxes must line up: the last card of every column (or the last row) ends on one and the same horizontal line at the bottom margin, cards in the same row have the same height, and the gaps between cards are equal; absorb any spare height inside the cards (larger illustration area, vertical centring, padding), never as a ragged gap under one column. Do not draw any account name, handle, URL or call-to-action text.

Words allowed on this poster (exactly these strings, nothing else): 「建物の登記に付ける情報」 / 「令別表で決まる」 / 「建物図面」 / 「各階平面図」 / 「所有権証明情報」 / 「住所証明情報」 / 「建物の表題登記」 / 「令別表十二の項」 / 「○」 / 「合体による登記等」 / 「十三の項」 / 「表題部の変更・更正」 / 「十四の項」 / 「△」 / 「－」 / 「分割・区分・合併」 / 「十六の項」 / 「滅失」 / 「別表に項なし」 / 「○　別表に定めがある」 / 「△　変更の内容による」 / 「－　通常は別表に定めがない」 / 「代理人が申請するなら代理権限証明情報も」

Final check before rendering: confirm the canvas is exactly 1080x1350 pixels; confirm the only text is the strings given above, reproduced exactly (scan every kanji for Simplified or Traditional Chinese forms and redraw any that appear); confirm no figure number or extra number appears; confirm the whole canvas is opaque. Pay special attention to the kanji: 建、物、登、記、付、情、報、令、別、表、決、図、面、各、階、平、所、有、権、証、明、住、題、十、二、項、合、体、等、三、部、変、更、正、四、分、割、区、併、六、滅、失、定、内、容、通、常、代、理、人、申、請、限.
```

## 見出し画像

見出し画像（note用 1280x670・Instagram用 1080x1350）は `header-image-prompts.md`、キャプションは `instagram-captions.md`。
