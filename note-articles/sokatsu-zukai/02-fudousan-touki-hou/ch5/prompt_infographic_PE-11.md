# 総合記事② 不動産登記法編 第5章　図解インフォグラフィック プロンプト（【PE-11】建物の滅失の登記（申請人・添付情報・滅失の意味・保存期間）・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。判定の流れ図（フローチャート）では、はい＝青・いいえ＝赤で描きます。分類・早見表・比較カードの図は、はい／いいえの分岐ではないため、青・赤を使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解16 | 建物の滅失の登記は、誰が・いつ？ | 早見表型（3列） | 1080×2600 | 不動産登記法編⑤_図解16_滅失の登記の申請人.png | 【PE-11】「中身の整理」の直後 |
| 図解17 | 滅失の登記が使えるのは、いつ？（効用を失ったかで判断） | 判定の流れ型＋補足カード | 1080×2600 | 不動産登記法編⑤_図解17_滅失かどうか.png | 【PE-11】図解16の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解16：建物の滅失の登記は、誰が・いつ？

- 型：早見表型（3列）　／　サイズ：1080×2600　／　保存名：`不動産登記法編⑤_図解16_滅失の登記の申請人.png`
- 記事の挿入位置：【PE-11】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with 3 columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「建物の滅失の登記は、誰が・いつ？」
「申請人・添付情報・保存期間」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第57条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells. Cell and card text may wrap onto two or three lines: make every row and card tall enough that all of its text fits fully inside it, at least 24 px high, and nothing is cut off or overflows.
Header row (dark navy cells with white text): 「場面」, 「申請人・添付情報など」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「通常の建物」 | 「表題部所有者又は所有権の登記名義人が、滅失の日から1か月以内に申請」 | 「法57条」
Row 2: 「共用部分である旨の登記がある建物」 | 「所有者が申請し、所有者を証する情報を添える。所有者の一人から申請できる」 | 「法57条・令別表17項」
Row 3: 「所有者が異なる区分建物が属する一棟の建物の全部滅失」 | 「区分建物の所有者の一人から、一棟の建物の滅失の登記を申請できる」 | 「先例による取扱い」
Row 4: 「特定登記がある区分建物の滅失」 | 「土地の抵当権も消滅させる承諾の情報を提供すると、その土地の抵当権が消滅した旨が記録される」 | 「法55条4項」
Row 5: 「申請情報・添付情報の保存期間」 | 「受付の日から30年間」 | 「規則28条9号」
Highlighting: the string 「1か月以内」 of row 1, the string 「所有者の一人から申請できる」 of row 2 and the string 「30年間」 of row 5 have a pale yellow highlighter marker. Copy each cell exactly as given.
At the bottom of the poster, below everything else, one wide dark navy band with large white text 「共用部分の登記がある建物は、申請人が所有者」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 号, 地, 建, 当, 所, 承, 抵, 権, 物, 登, 規, 記, 証, 請, 諾, 録, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.  Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解17：滅失の登記が使えるのは、いつ？（効用を失ったかで判断）

- 型：判定の流れ型＋補足カード　／　サイズ：1080×2600　／　保存名：`不動産登記法編⑤_図解17_滅失かどうか.png`
- 記事の挿入位置：【PE-11】図解16の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ) with one side note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「滅失の登記が使えるのは、いつ？」
「効用を失ったかで判断する」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第57条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every RED 「いいえ」 branch leads down or right as described, and the blue result boxes sit to the RIGHT of their diamonds on the same row with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The red result box at the bottom sits below DIAMOND 2 on the center line. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「建物の滅失の登記を考える」
NODE DIAMOND 1: 「社会通念上、建物が効用を失った状態か？」 The text is placed inside the diamond on 3 lines.
  - Arrow right to RESULT 1 with the BLUE label 「はい」.
  - Arrow down to DIAMOND 2 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「建物の滅失」 on the first line and 「滅失の日から1か月以内に、滅失の登記を申請する」 on the next two lines.
NODE DIAMOND 2: 「区分建物として登記されているが、初めから区分していなかったことが明らかか？」 The text is placed inside the diamond on 4 lines.
  - Arrow right to RESULT 2 with the BLUE label 「はい」.
  - Arrow down to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 2 (blue box): 「錯誤を原因として、滅失の登記を申請する」 on two lines and the small tag 「先例による取扱い」.
NODE RESULT 3 (red box): 「滅失の登記は申請できない」 on the first line and 「例：火災で一部が焼けても、主要構造部が残り使える」 on the next two lines.
--- SIDE NOTE CARD (below the flowchart, a wide card with a dashed dark navy outline) ---
Heading 「滅失とは」, body 「社会通念上、建物が効用を失った状態」 and 「定義した条文はなく、判例・先例の整理」.
Counts: 1 start node, 2 diamonds, 3 result boxes, 1 side note card. Every diamond has exactly two exits, and no arrow leaves a result box.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 初, 効, 建, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there is exactly 1 start node, 2 diamonds, 3 result boxes and 1 side note card, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
