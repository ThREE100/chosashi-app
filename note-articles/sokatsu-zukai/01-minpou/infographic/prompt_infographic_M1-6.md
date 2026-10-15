# 【M1-6】図解インフォグラフィック プロンプト（2枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M1-6】（取得時効：登記はだれに対して要り、占有の推定はどこまで及ぶのか）に差し込む図解のプロンプトです。論点が「登記は誰に対して要るか」と「占有の推定はどこまで及ぶか」の2つの別の問いなので、1枚ずつ（2枚）に分けました。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は総合記事の【M1-6】の節と、民法第162条・第186条1項（`note-articles/laws/minpou-1-soukyoku-bukken.md`で原文を確認）の範囲です。

## 図解：時効取得に登記は要るかの判定フロー（相手と時点）

- 型：フローチャート型
- サイズ：1080×2300
- 保存名：`M1-6_時効取得に登記は要るか.png`
- 記事の挿入位置：「たとえば」の直後（判断のしかたの前）

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせてください。

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「時効取得に登記は要る？」
「相手と時点で決まる」
Subtitle (smaller, centered, 1 line):
「民法 第162条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, with at least 60 px of empty space between each diamond and its box so that the arrow label stays visible. All arrows are straight or have at most one right-angle bend and never cross each other. Do not draw any arrow that returns to an earlier node.
NODE START (rounded pill, dark navy): 「占有者が、時効取得を主張する」
NODE DIAMOND 1: 「主張する相手は、元の所有者か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow right to RESULT 1 with the BLUE label 「はい」.
  - Arrow down to DIAMOND 2 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「元の所有者は、時効の当事者」 on the first line, 「対抗関係に立たない」 on the second line and 「登記なしで主張できる」 on the third line.
NODE DIAMOND 2: 「第三者が所有権を得たのは、時効完成の前か？」 The text is placed inside the diamond on 3 lines.
  - Arrow right to RESULT 2 with the BLUE label 「はい」.
  - Arrow down to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 2 (blue box): 「元の所有者と同じ立場（当事者類似）」 on the first line and 「登記なしで主張できる」 on the next line.
NODE RESULT 3 (red box): 「完成の後の第三者とは対抗関係」 on the first line and 「登記の先後で決まる」 on the next line.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts, except that the string 「登記なしで主張できる」 appears in both RESULT 1 and RESULT 2 on purpose; the other lines of every box are NOT identical.
--- SMALL TAG (light gray, directly under RESULT 2 and RESULT 3, centered) ---
「判例の考え方」
--- NOTE CARD AT THE BOTTOM (one separate gray card below RESULT 3, with no arrow) ---
Heading 「占有の推定とは別の問い」 and one body line 「無過失が推定されるかは、この流れでは決まらない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 占, 対, 張, 当, 所, 抗, 権, 無, 登, 記, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 on the arrow to the right and a red 「いいえ」 on the arrow going down, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, that no arrow label is hidden, and that the gray card at the bottom is one separate card with no arrow. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

検品チェック：
- 文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない
- 開始1・ひし形2・結果の箱3で、ひし形は右に青い「はい」、下に赤い「いいえ」が付いている
- 結果1・2が青い箱、結果3が赤い箱で、文言が入れ替わっていない（完成の後の第三者だけが「登記の先後で決まる」）
- 「判例の考え方」の小さなタグと、一番下の灰色のカード（占有の推定とは別の問い）が、矢印のない別の部品になっている
- 背景が透過でなく、最後のカードの下に追加のまとめがない

## 図解：取得時効の要件と占有の推定（推定が及ぶ範囲）

- 型：早見表型（4列）＋カード1枚
- サイズ：1080×1900
- 保存名：`M1-6_取得時効の要件と占有の推定.png`
- 記事の挿入位置：「中身の整理」の占有の推定の箇条書きの直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせてください。

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference table poster (早見表) with a short card below the table.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「取得時効の要件と占有の推定」
「推定が及ぶのはどこまで」
Subtitle (smaller, centered, 1 line):
「民法 第162条・第186条1項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three data columns) and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: the first cell is 「要素」; the second header 「20年の取得時効」 with a small light-gray tag 「162条1項」 under it; the third header 「10年の取得時効」 with a small light-gray tag 「162条2項」 under it; the fourth header 「占有の推定」 with a small light-gray tag 「186条1項」 under it. The three data headers are NOT identical.
Data row 1 (row label cell, dark navy, white text: 「所有の意思」): second column 「必要」; third column 「必要」; fourth column 「推定される」.
Data row 2 (row label cell, dark navy, white text: 「善意」): second column 「不要」; third column 「必要（占有の開始の時）」; fourth column 「推定される」.
Data row 3 (row label cell, dark navy, white text: 「平穏」): second column 「必要」; third column 「必要」; fourth column 「推定される」.
Data row 4 (row label cell, dark navy, white text: 「公然」): second column 「必要」; third column 「必要」; fourth column 「推定される」.
Data row 5 (row label cell, dark navy, white text: 「無過失」): second column 「不要」; third column 「必要（占有の開始の時）」; fourth column 「推定されない」. Draw this whole row 5 with a pale yellow highlighter marker behind the row label and the fourth-column cell.
The cells 「必要」, 「不要」 and 「推定される」 repeat across rows on purpose; draw each of them exactly as given in the row where it is listed, and do not merge any cells.
--- CARD BELOW THE TABLE ---
One wide rounded card with a dark navy outline and a pale gray fill, with a dark navy heading 「推定されない無過失」 and one body line 「10年で時効取得を主張する側が、自分で立証する」. Draw this card as ONE separate card below the table, not as a row of the table. Draw no arrow.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 占, 張, 所, 無, 証, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 5 data rows in the order 所有の意思, 善意, 平穏, 公然, 無過失, that only row 5 is highlighted and its fourth-column cell reads 推定されない while rows 1 to 4 read 推定される, that the card below the table is one separate card, and that no check mark, cross mark, blue or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

検品チェック：
- 文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない
- 表は4列（要素・20年・10年・占有の推定）×5行で、行の並びが所有の意思・善意・平穏・公然・無過失の順
- 第4列は「無過失」の行だけが「推定されない」で、ほかの4行は「推定される」。無過失の行だけに黄色のマーカーがある
- 表の下のカード（推定されない無過失）が1枚だけあり、表の一部になっていない
- ✓・✕・青・赤が表のどこにもない／背景が透過でなく、カードの下に追加のまとめがない
