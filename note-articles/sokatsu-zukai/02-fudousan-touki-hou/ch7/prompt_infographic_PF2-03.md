# 総合記事② 不動産登記法編 第7章　図解インフォグラフィック プロンプト（【PF2-3】合体による登記等は誰が、いつから1か月以内に申請するのか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第7章「建物の合体による登記等」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch7.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は、分類・早見表が中心のものは、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解4）だけは、はい＝青・いいえ＝赤です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解5 | 合体の申請は、誰が？（法49条1項の号） | 早見表型（3列） | 1080×2200 | 登記法編7章_図解5_誰が申請するか.png | 【PF2-3】「中身の整理」の直後 |
| 図解6 | 1か月の数え始めは、人によって違う | ステージカード型 | 1080×2000 | 登記法編7章_図解6_1か月の数え始め.png | 【PF2-3】図解5の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解5：合体の申請は、誰が？（法49条1項の号）

- 型：早見表型（3列）　／　サイズ：1080×2200　／　保存名：`登記法編7章_図解5_誰が申請するか.png`
- 記事の挿入位置：【PF2-3】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (早見表), followed by one dashed side note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「合体の申請は、誰が？」
「一人から単独で申請できる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第49条第1項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Header row (dark navy cells with white text): 「号」, 「合体前の建物」, 「申請人」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「1号」 | 「表題登記がない建物と、表題登記のみの建物」 | 「未登記建物の所有者または表題部所有者」
Row 2: 「2号」 | 「表題登記がない建物と、所有権の登記がある建物」 | 「未登記建物の所有者または所有権の登記名義人」
Row 3: 「3号」 | 「いずれも表題登記のみの建物」 | 「表題部所有者」
Row 4: 「4号」 | 「表題登記のみの建物と、所有権の登記がある建物」 | 「表題部所有者または所有権の登記名義人」
Row 5: 「5号」 | 「いずれも所有権の登記がある建物」 | 「所有権の登記名義人」
Row 6: 「6号」 | 「三以上の建物で、未登記・表題登記のみ・所有権の登記ありが混じる」 | 「未登記建物の所有者、表題部所有者または所有権の登記名義人」
Highlighting: the string 「または」 inside the column-3 cells of rows 1, 2, 4 and 6 has a pale yellow highlighter marker; rows 3 and 5 have a slightly darker pale gray cell fill in column 3 because they name only one kind of person. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「申請人が二つ並ぶ号は、そのうちの一人から単独で申請できる」.
--- SIDE NOTE CARD (below the band, a wide card with a dashed dark navy outline) ---
Heading 「共同申請の定めはない」, body 「権利に関する登記の共同申請（法60条）は、表示に関する登記にはない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 所, 権, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that rows 3 and 5 are the only rows with a single kind of person in column 3 and that rows 1, 2, 4 and 6 contain 「または」, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解6：1か月の数え始めは、人によって違う

- 型：ステージカード型　／　サイズ：1080×2000　／　保存名：`登記法編7章_図解6_1か月の数え始め.png`
- 記事の挿入位置：【PF2-3】図解5の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical poster with three stage cards and one closing band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「1か月の数え始めは」
「人によって違う」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第49条第1項・第3項・第4項」
--- STAGE CARDS ---
Layout: three stage cards stacked top to bottom on the center line, all the same size, separated only by a small empty gap (no arrows, nothing drawn between them). Each stage card has a dark navy badge with its stage name at the top left, one bold heading line, one body text, and one small gray tag at the bottom right.
STAGE CARD 1: badge 「原則」, heading 「合体の日から1か月以内」, body 「各号に定める申請人は、合体の日から数える」, small gray tag 「法49条1項」.
STAGE CARD 2: badge 「合体の後に持分を取得した人」, heading 「持分の取得の日から1か月以内」, body 「合体前の未登記の建物の所有者から、持分を取得した人」, small gray tag 「法49条3項」.
STAGE CARD 3: badge 「合体の後に名義人になった人」, heading 「登記があった日から1か月以内」, body 「表題部所有者または所有権の登記名義人になった人は、その者に係る更正の登記または所有権の登記があった日から数える」, small gray tag 「法49条4項」.
The three headings are different texts; do not copy one into another.
--- CLOSING BAND (a wide pale yellow band with a thin dark navy outline and dark navy text) ---
「1か月は同じ。数え始める日が違う」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 所, 権, 物, 登, 記, 請, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly three stage cards in the order 原則, 合体の後に持分を取得した人, 合体の後に名義人になった人, followed by exactly one closing band, that no arrow is drawn between the cards, that the badge of the first card reads 原則 exactly (never 思則), and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
