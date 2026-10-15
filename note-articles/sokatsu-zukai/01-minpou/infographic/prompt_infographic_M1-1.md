# 【M1-1】無効と取消しは何が違うのか　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M1-1】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：無効と取消しの違い（三つの場面で比べる）
  - 型：対比表型（2列）　／　サイズ：1080×2000　／　保存名：`図解1_無効と取消しの違い.png`
  - 記事の挿入位置：【M1-1】の「中身の整理」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：無効と取消しの違い（三つの場面で比べる）

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three columns (対比表), followed by two note cards and one closing band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「無効と取消しの違い」
「三つの場面で比べる」
Subtitle (smaller, centered, 1 line):
「民法 総則（無効と取消し）」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this poster; use dark navy outlines and the pale yellow highlighter only for the strings marked as highlighted.
Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header 「無効」; the third header 「取消し」.
Data row 1 (row label cell, dark navy, white text: 「追認したら」): second column 「追認しても、効力を生じない」 with the small gray tag 「119条」; third column 「追認すれば、以後は取り消せない」 with the small gray tag 「122条」.
Data row 2 (row label cell, dark navy, white text: 「時間がたつと」): second column 「何年たっても、有効にならない」; third column 「5年（行為の時から20年）で取消権が消える」 on the first two lines and 「確定的に有効になる」 on the next line, with the small gray tag 「126条」. In this third-column cell the string 「確定的に有効になる」 has a pale yellow highlighter marker.
Data row 3 (row label cell, dark navy, white text: 「主張できる人」): second column 「だれでも主張できる」; third column 「取消権者だけ」 on the first line and 「本人・代理人・承継人など」 on the second line, with the small gray tag 「120条」. In this third-column cell the string 「取消権者だけ」 has a pale yellow highlighter marker.
Every cell has its own text exactly as given; no two cells carry the same string.
--- NOTE CARD 1 (a wide rounded card directly below the table, pale gray fill, dark navy outline) ---
Heading (bold, ONE line): 「取り消すと」
Body (ONE line): 「初めから無効だったものとみなされる」 with the small gray tag 「121条」.
Under the body, a small dark navy tag: 「将来に向かってだけ、ではない」.
--- NOTE CARD 2 (a wide rounded card below note card 1, same style) ---
Heading (bold, ONE line): 「無効と知って追認したとき」
Body (ONE line): 「新たな行為をしたものとみなされる」 with the small gray tag 「119条ただし書」.
--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below note card 2) ---
「取消しのみ、と言い切る文は」 on the first line and 「無効にも当てはまる性質かを確かめる」 on the second line.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 初, 効, 対, 張, 当, 承, 権, 無, 認, 違, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that the second and third columns of every row have different texts, that exactly two strings are highlighted in pale yellow (確定的に有効になる and 取消権者だけ), that there are exactly 2 note cards followed by exactly 1 closing band, that no check mark or cross mark appears anywhere, and that no blue or red is used anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`図解1_無効と取消しの違い.png`

## 検品チェック

- 表は3列（行見出し・無効・取消し）×データ3行で、各セルの文字が指定どおりか（119条・122条・126条・120条・121条・119条ただし書の条番号を含む）。
- 黄色のマーカーが、「確定的に有効になる」と「取消権者だけ」の2か所だけか。青・赤・チェック・×が一つもないか。
- 表の下にカードが2枚、その下に濃紺の帯が1つだけで、帯のあとに何も描かれていないか。
- 簡体字・余計な文字・透過・図番がないか。