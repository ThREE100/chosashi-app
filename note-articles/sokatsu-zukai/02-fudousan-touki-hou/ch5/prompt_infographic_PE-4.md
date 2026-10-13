# 総合記事② 不動産登記法編 第5章　図解インフォグラフィック プロンプト（【PE-4】床面積の測り方と算入・不算入、記録の順序・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。判定の流れ図（フローチャート）では、はい＝青・いいえ＝赤で描きます。分類・早見表・比較カードの図は、はい／いいえの分岐ではないため、青・赤を使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解6 | 床面積は、どの線で測る？（専有部分だけが内法） | 早見表型＋カード | 1080×2400 | 不動産登記法編⑤_図解6_床面積の基準線.png | 【PE-4】「中身の整理」の直後 |
| 図解7 | 床面積に算入する？ しない？（低い天井・塔屋・観覧席） | 判定の流れ型＋補足カード | 1080×2500 | 不動産登記法編⑤_図解7_床面積に算入するか.png | 【PE-4】図解6の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解6：床面積は、どの線で測る？（専有部分だけが内法）

- 型：早見表型＋カード　／　サイズ：1080×2400　／　保存名：`不動産登記法編⑤_図解6_床面積の基準線.png`
- 記事の挿入位置：【PE-4】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with 3 columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「床面積は、どの線で測る？」
「専有部分だけが内法」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第115条・準則 第91条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells. Cell and card text may wrap onto two or three lines: make every row and card tall enough that all of its text fits fully inside it, at least 24 px high, and nothing is cut off or overflows.
Header row (dark navy cells with white text): 「建物の区分」, 「床面積を測る線」, 「根拠・注意」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「区分建物でない建物」 | 「壁その他の区画の中心線（壁芯）」 | 「規則115条」
Row 2: 「区分建物の専有部分」 | 「壁その他の区画の内側線（内法）」 | 「規則115条（区分建物にあっては）」
Row 3: 「区分建物が属する一棟の建物」 | 「壁その他の区画の中心線（壁芯）」 | 「内側線とするのは専有部分だけ」
Highlighting: the string 「壁その他の区画の内側線（内法）」 of row 2 has a pale yellow highlighter marker; the other two cells of column 2 are plain. Copy each cell exactly as given.
--- RECORD CARD (below the table, a wide card with a dashed dark navy outline and a small dark navy tag 「記録のしかた」) ---
Heading 「床面積の記録」, and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「1平方メートルの100分の1未満は、切り捨てる（規則115条）」, 「平家建以外は、各階ごとに記録する（合計は不要）」, 「地階は、地上階の次に記録する」, 「平方メートル未満がなくても、00と記録する」.
At the bottom of the poster, below everything else, one wide dark navy band with large white text 「専有部分は内法、一棟は壁芯」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 物, 登, 規, 記, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm that the record card has exactly four item lines. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解7：床面積に算入する？ しない？（低い天井・塔屋・観覧席）

- 型：判定の流れ型＋補足カード　／　サイズ：1080×2500　／　保存名：`不動産登記法編⑤_図解7_床面積に算入するか.png`
- 記事の挿入位置：【PE-4】図解6の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a poster with one small flowchart (判定の流れ) and two side note cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「床面積に算入する？ しない？」
「低い天井・塔屋・観覧席」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第82条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. START at the top, then DIAMOND 1. The BLUE 「はい」 arrow goes down to a blue result box; the RED 「いいえ」 arrow goes right to a red result box on the same row, with at least 60 px of empty space between the diamond and the red box so that the arrow label stays visible.
NODE START (rounded pill, dark navy): 「天井の高さ1.5メートル未満の部分がある」
NODE DIAMOND 1: 「地階・屋階の階全体が低いか？」 The text is placed inside the diamond on 2 lines.
  - Arrow down with the BLUE label 「はい」 to RESULT 1.
  - Arrow right with the RED label 「いいえ」 to RESULT 2.
NODE RESULT 1 (blue box): 「その階（特殊階）全体を、床面積に算入しない」 on three lines and the small tag 「準則82条1号」.
NODE RESULT 2 (red box): 「一室の一部が低いだけなら、その部分も一室の面積に算入する」 on three lines and the small tag 「同号ただし書」.
--- SIDE NOTE CARDS (two wide cards stacked below the flowchart, each with a dashed dark navy outline and a small dark navy tag at its top left) ---
Card A, tag 「塔屋（屋上の階段室・機械室など）」, heading 「一部でも事務所・倉庫に使うと」, two body lines 「使っていない部分も含め、塔屋全体を」 and 「床面積に算入する」, and a small gray tag 「条文にない取扱い」.
Card B, tag 「観覧席」, heading 「野球場・競馬場などの観覧席」, body line 「屋根の設備のある部分の面積を、床面積とする」, and a small gray tag 「準則82条3号」.
Counts: 1 start node, 1 diamond, 2 result boxes, 2 side note cards. The diamond has exactly two exits, and no arrow leaves a result box.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 所, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there is exactly 1 start node, 1 diamond, 2 result boxes and 2 side note cards, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
