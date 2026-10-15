# 【M1-8】条件：追加の図解「既成条件の早見表」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-8】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-8.md`）の判定フローは「契約の時にすでに成就していた場合」だけを扱うので、記事の「中身の整理」にある「成就しないことがすでに確定していた場合」（131条2項）を、2×2の早見表で補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は早見表で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：既成条件の早見表（成就済みか、不成就の確定か）
  - 型：対比表型（2×2）＋カード1枚＋帯　／　サイズ：1080×1800　／　保存名：`民法編1_M1-8_追加_既成条件の早見表.png`
  - 記事の挿入位置：【M1-8】の「中身の整理」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：既成条件の早見表（成就済みか、不成就の確定か）

```text
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three columns (早見表), followed by one note card and one closing band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this poster; use dark navy outlines and the pale yellow highlighter only for the strings marked as highlighted.
--- HEADER ---
Title (large, bold, 2 lines):
「既成条件は、どうなる？」
「成就済みか、不成就の確定か」
Subtitle (smaller, centered, 1 line):
「民法 第131条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 2 data rows, no merged cells.
Header row (dark navy cells with white text), from left to right: the first cell is 「契約の時に、すでに」; the second header 「停止条件」; the third header 「解除条件」.
Data row 1 (row label cell, dark navy, white text: 「成就していた」 with the small light-gray tag 「131条1項」 under it): second column 「無条件（有効）」; third column 「無効」. In this row the string 「無条件（有効）」 has a pale yellow highlighter marker.
Data row 2 (row label cell, dark navy, white text: 「成就しないと確定していた」 with the small light-gray tag 「131条2項」 under it): second column 「無効」; third column 「無条件（有効）」. In this row the string 「無条件（有効）」 has a pale yellow highlighter marker.
The strings 「無条件（有効）」 and 「無効」 each appear twice in the table on purpose, in diagonal positions (row 1 second column and row 2 third column hold 「無条件（有効）」; row 1 third column and row 2 second column hold 「無効」); draw each cell exactly as given and do not merge or swap any cells.
--- NOTE CARD (a wide rounded card directly below the table, pale gray fill, dark navy outline, with NO arrow) ---
Heading (bold, ONE line): 「成就した時から、とは別の問い」.
Body (ONE line): 「ここで決まるのは、契約の時にすでに決まっていた場合の扱い」.
--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below the note card) ---
「不成就が確定していたら、」 on the first line and 「成就済みの場合と結論が逆になる」 on the second line.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 無, 解; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 2 data rows, that row 1 reads 無条件（有効） then 無効 and row 2 reads 無効 then 無条件（有効）, that exactly two cells are highlighted in pale yellow (the two 無条件（有効） cells), that there is exactly 1 note card followed by exactly 1 closing band, that no check mark or cross mark appears anywhere, and that no blue or red is used anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-8_追加_既成条件の早見表.png`

## 検品チェック

- 表は3列（行見出し・停止条件・解除条件）×データ2行で、1行目が「無条件（有効）」「無効」、2行目が「無効」「無条件（有効）」と斜めに入れ替わっているか。
- 黄色のマーカーが、2つの「無条件（有効）」のセルだけか。条番号（131条1項・131条2項）が行見出しの下に付いているか。
- 表の下にカードが1枚、その下に濃紺の帯が1つだけで、帯のあとに何も描かれていないか。
- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。