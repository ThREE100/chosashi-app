# 総合記事② 不動産登記法編 第5章　図解インフォグラフィック プロンプト（【PE-8】表題部の変更・更正の登記が必要なとき、必要な添付情報と記録のしかた・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。判定の流れ図（フローチャート）では、はい＝青・いいえ＝赤で描きます。分類・早見表・比較カードの図は、はい／いいえの分岐ではないため、青・赤を使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解12 | 変更の登記は、要る？ 要らない？ | 判定の流れ型＋補足カード | 1080×2700 | 不動産登記法編⑤_図解12_変更の登記は要るか.png | 【PE-8】「中身の整理」の直後 |
| 図解13 | 附属建物の変更は、全部を書き直す（申請人と添付情報） | 対比カード＋早見表型 | 1080×2400 | 不動産登記法編⑤_図解13_附属建物の変更と申請人.png | 【PE-8】図解12の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解12：変更の登記は、要る？ 要らない？

- 型：判定の流れ型＋補足カード　／　サイズ：1080×2700　／　保存名：`不動産登記法編⑤_図解12_変更の登記は要るか.png`
- 記事の挿入位置：【PE-8】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ) with two side note cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「変更の登記は、要る？ 要らない？」
「登記事項が変わったかで見る」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条第1項」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every RED 「いいえ」 result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The final blue result box at the bottom sits below DIAMOND 2 on the center line. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「建物に変化があった」
NODE DIAMOND 1: 「表題部の登記事項が変わったか？」 The text is placed inside the diamond on 2 lines, with a smaller line under it 「（家屋番号と共用部分である旨を除く）」.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「変更の登記は要らない」 on the first line and 「外壁材の張替え・屋根材の変更（屋根の種類が同じ）」 on the next two lines.
NODE DIAMOND 2: 「既存の建物を全部取り壊して、建て直したか？」 The text is placed inside the diamond on 3 lines.
  - Arrow down to RESULT 3 with the BLUE label 「はい」.
  - Arrow right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 2 (red box): 「変更の日から1か月以内に、変更の登記を申請する」 on three lines and the small tag 「法51条1項」.
NODE RESULT 3 (blue box): 「滅失と新築として扱う」 on the first line and 「表示を新しい建物に変える変更の登記はできない（準則83条）」 on the next two lines.
--- SIDE NOTE CARDS (two wide cards stacked below the flowchart, each with a dashed dark navy outline and a small dark navy tag at its top left) ---
Card A, tag 「非区分建物に接続して区分建物を新築」, body 「区分建物の表題登記と、非区分建物の表題部の変更の登記を併せて申請（法48条3項）」.
Card B, tag 「独立性のない増築部分」, body 「既存の建物に付合し、既存の建物の所有者のものになる（民法242条）」.
Counts: 1 start node, 2 diamonds, 3 result boxes, 2 side note cards. Every diamond has exactly two exits, and no arrow leaves a result box.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 張, 所, 物, 番, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there is exactly 1 start node, 2 diamonds, 3 result boxes and 2 side note cards, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are red and RESULT 3 is blue, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解13：附属建物の変更は、全部を書き直す（申請人と添付情報）

- 型：対比カード＋早見表型　／　サイズ：1080×2400　／　保存名：`不動産登記法編⑤_図解13_附属建物の変更と申請人.png`
- 記事の挿入位置：【PE-8】図解12の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with 3 columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「附属建物の変更は、全部を書き直す」
「申請人と添付情報もそろえる」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第94条」
--- BEFORE / AFTER CARDS (two cards side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card; a small dark navy tag 「附属建物の種類・構造・床面積の変更・更正」 above them; a short plain dark navy right-pointing arrow sits between the two cards, with no text on it) ---
Left card, heading 「従前の附属建物の表示」, three item lines: 「符号」, 「従前の種類・構造・床面積」 (drawn struck through with a thin line), and the small line 「符号を除く全部を抹消する」; only the first item line 「符号」 has a pale yellow highlighter marker.
Right card, heading 「変更後・更正後の表示」, three item lines: 「符号（従前のまま）」, 「変更後の種類・構造・床面積の全部を記録」, and the small tag 「準則94条1項」.
The cards and cells have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells. Cell and card text may wrap onto two or three lines: make every row and card tall enough that all of its text fits fully inside it, at least 24 px high, and nothing is cut off or overflows.
Header row (dark navy cells with white text): 「場面」, 「申請人・添付など」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「附属建物を新築したとき」 | 「変更後の建物図面及び各階平面図と、所有権を有することを証する情報」 | 「令別表14項ハ」
Row 2: 「共有建物の表題部の変更」 | 「共有者の1人から、単独で申請できる（代位ではない）」 | 「民法252条5項（保存行為）」
Row 3: 「独立性のない増築部分」 | 「既存の建物の所有者のものになる。費用を出しただけでは共有者にならない」 | 「民法242条（付合）」
Highlighting: the string 「単独で申請できる」 of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
At the bottom of the poster, below everything else, one wide dark navy band with large white text 「更正後の全部を記録し、従前は符号を除いて抹消」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 保, 号, 建, 所, 権, 物, 登, 記, 証, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm that there are exactly two before/after cards above the table. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
