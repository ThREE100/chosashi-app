# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（【PA-3】表題部所有者の更正に、承諾情報と所有権証明情報のどちらが要るか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解4 | 更正の添付情報は何が要る？（加わる者がいるか） | フローチャート型 | 1080×2400 | 不登法編1_図解4_更正の添付情報.png | 【PA-3】「中身の整理」の直後 |
| 図解5 | 持分の更正、誰の承諾が要る？ | 早見表型（4列） | 1080×1700 | 不登法編1_図解5_持分の更正の承諾.png | 【PA-3】「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解4：更正の添付情報は何が要る？（加わる者がいるか）

- 型：フローチャート型　／　サイズ：1080×2400　／　保存名：`不登法編1_図解4_更正の添付情報.png`
- 記事の挿入位置：【PA-3】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「更正の添付情報は何が要る？」
「加わる者がいるかで分かれる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第33条・令別表」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, RESULT 1. RESULT 2 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The side note card sits at the bottom. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「表題部所有者についての更正の登記」
NODE DIAMOND 1: 「新たに表題部所有者として加わる者がいるか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to RESULT 1 with the BLUE label 「はい」.
  - Arrow right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): the first line 「加わる者の証明が要る」 and three body lines 「加わる者の所有権を証する情報」, 「加わる者の住所を証する情報」, 「外れる者がいれば、その承諾を証する情報」.
NODE RESULT 2 (red box): the first line 「持分だけを直す更正」 and two body lines 「持分が変わる他の共有者の承諾だけ」, 「所有権を証する情報は要らない」.
--- SIDE NOTE CARD (a wide card with a dashed dark navy outline at the bottom, neutral dark navy text) ---
Heading 「承諾が要る相手は、記録から外れる者・持分が変わる共有者だけ」, body 「承諾を証する情報の代わりに、その者に対抗できる裁判があったことを証する情報でもよい」.
Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts; do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 対, 所, 承, 抗, 権, 登, 記, 証, 諾, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解5：持分の更正、誰の承諾が要る？

- 型：早見表型（4列）　／　サイズ：1080×1700　／　保存名：`不登法編1_図解5_持分の更正の承諾.png`
- 記事の挿入位置：【PA-3】「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with four columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「持分の更正、誰の承諾が要る？」
「持分が変わる共有者だけ」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第33条第3項・第4項」
A small gray caption above the table: 「丙が申請して、乙の持分を10分の2、丙の持分を10分の3に直す」.
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns and exactly 3 data rows, no merged cells.
Header row (dark navy cells with white text): 「共有者」, 「更正前」, 「更正後」, 「承諾」.
Data rows, one per line, in this order (column 1 | column 2 | column 3 | column 4):
Row 1: 「甲」 | 「10分の5」 | 「10分の5」 | 「変わらない：承諾は要らない」
Row 2: 「乙」 | 「10分の3」 | 「10分の2」 | 「減る：承諾が要る」
Row 3: 「丙」 | 「10分の2」 | 「10分の3」 | 「増える（申請する共有者）：承諾は要らない」
Highlighting: the string 「承諾が要る」 in row 2 has a pale yellow highlighter marker; the other two rows are plain. Copy each cell exactly as given; the strings 「10分の2」 and 「10分の3」 differ by one digit, so copy each exactly and do not change one into the other.
Under the table, one wide dark navy band with large white text 「承諾が要るのは、持分を更正することとなる他の共有者だけ」.
Under the band, one small gray note line 「承諾があれば、共有者の一人が単独で申請できる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 承, 登, 記, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 3 data rows, that every cell reads exactly as given, that only row 2 reads 承諾が要る, that the fractions 10分の2 and 10分の3 are copied exactly in rows 2 and 3, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
