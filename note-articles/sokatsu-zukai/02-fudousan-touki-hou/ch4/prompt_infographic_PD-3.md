# 総合記事②不動産登記法編 第4章　図解インフォグラフィック プロンプト（【PD-3】分筆の地積はどう書くか。地目変更との一括申請では何を書くか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『申請できるか』『合筆できるか』のような分類が中心で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。例外は、はい／いいえの判定の流れ図（分筆を錯誤で戻せるか）で、はい＝青、いいえ＝赤で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解4 | 地積の桁は、どう決まる？ | 早見表型（3列）＋補足 | 1080×2400 | 不動産登記法編4章_図解4_地積の桁.png | 【PD-3】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解4：地積の桁は、どう決まる？

- 型：早見表型（3列）＋補足　／　サイズ：1080×2400　／　保存名：`不動産登記法編4章_図解4_地積の桁.png`
- 記事の挿入位置：【PD-3】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns, followed by two example chips and two note cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「地積の桁は、どう決まる？」
「10平方メートルが分かれ目」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第100条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells.
Header row (dark navy cells with white text): 「土地の大きさ」, 「地目」, 「地積の書き方」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「10平方メートル以下」 | 「地目を問わない」 | 「小数点以下第2位まで」
Row 2: 「10平方メートルを超える」 | 「宅地・鉱泉地」 | 「小数点以下第2位まで」
Row 3: 「10平方メートルを超える」 | 「それ以外の地目」 | 「整数（1平方メートル未満は切り捨て）」
Highlighting: the string 「地目を問わない」 of row 1 and the string 「整数（1平方メートル未満は切り捨て）」 of row 3 have a pale yellow highlighter marker; every other cell is plain. Rows 1 and 2 have the same text in column 3 on purpose; draw the same string in both. Copy each cell exactly as given; cells that look alike differ in their wording, so do not change one into another.
--- TWO EXAMPLE CHIPS (side by side, same size, below the table) ---
Left chip: 「例：公衆用道路 9.0025 → 9.00」. Right chip: 「例：畑 215.4766 → 215」.
--- TWO NOTE CARDS (stacked, below the chips, each a wide card with a dashed dark navy outline) ---
Note card 1: heading 「宅地造成工事中の畑」, body 「完成するまでは、従前の地目（畑）のまま」 and a small gray tag 「現況主義からの整理」.
Note card 2: heading 「地目変更と分筆を一の申請情報にするとき」, body 「地目変更の登記原因とその日付も書く」 and a small gray tag 「規則35条7号」.
At the very bottom of the poster, below everything else, one wide dark navy band with large white text 「宅地・鉱泉地以外は、10平方メートル超で整数」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 登, 規, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that rows 1 and 2 show the same string in column 3, that there are exactly two example chips and two note cards below the table, and that no check mark, no cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
