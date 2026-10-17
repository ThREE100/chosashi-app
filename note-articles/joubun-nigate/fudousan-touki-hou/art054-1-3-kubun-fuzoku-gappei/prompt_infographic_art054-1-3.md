# 区分合併と附属合併の使い分け　図解インフォグラフィック プロンプト（5枚）

条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第54条1項3号（建物の合併の登記）の記事に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 建物の合併は2種類（附属合併と区分合併） | カードポスター型 | 1080×2000 | 図解1_建物の合併は2種類.png | 「ひとことで」の直後 |
| 図解2 | 附属合併と区分合併の要件の対比表 | 対比表型（3列） | 1080×1900 | 図解2_附属合併と区分合併の対比表.png | 「部品1：合併の登記は2種類」の節の終わり |
| 図解3 | どちらの合併になるかの判定の流れ | フローチャート型 | 1080×2900 | 図解3_どちらの合併になるかの判定の流れ.png | 「部品4：両方の要件がそろうとき」の直前（判断の流れの節） |
| 図解4 | 場面ごとの早見表（どの合併ができるか） | 早見表型（3列） | 1080×2300 | 図解4_場面ごとの早見表.png | 判定の流れの直後 |
| 図解5 | 両方できるとき、合併後の姿で選ぶ | 二択カード型 | 1080×1800 | 図解5_合併後の姿で選ぶ.png | 「部品4：両方の要件がそろうとき」の節の終わり |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。表の行数（図解2は5行、図解4は6行）と、図解3の分岐（ひし形4つ・結果5つ）も確かめてください。

## 図解1：建物の合併は2種類（附属合併と区分合併）

- 型：カードポスター型　／　サイズ：1080×2000　／　保存名：`図解1_建物の合併は2種類.png`
- 記事の挿入位置：「ひとことで」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「建物の合併は2種類」
「附属合併と区分合併」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条1項3号」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「附属合併」
Illustration: Two separate isometric house icons labeled 「甲建物」 and 「乙建物」, with a solid navy arrow from the first house into a small annex box attached to the second house, and a small pale tag 「主たる建物と附属建物」 between them.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「主従の関係が要る」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「区分合併」
Illustration: Two attached rooms of one apartment building labeled 「甲建物」 and 「乙建物」, side by side and touching, with a solid navy arrow merging them into one single room.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「接続していることが要る」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「共通の制限」
Illustration: A registry ledger card with a small stop-sign icon beside it and the small tag 「法56条」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「どちらの合併にも同じ」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「両方の要件がそろうとき」
Illustration: Two touching apartment rooms with a small double-headed branch icon pointing to a left small label 「附属合併」 and to a right small label 「区分合併」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「どちらも申請できる」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解2：附属合併と区分合併の要件の対比表

- 型：対比表型（3列）　／　サイズ：1080×1900　／　保存名：`図解2_附属合併と区分合併の対比表.png`
- 記事の挿入位置：「部品1：合併の登記は2種類」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three columns (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「附属合併と区分合併」
「要件はどこが違う？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条1項3号」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header 「附属合併」; the third header 「区分合併」. The two headers are NOT identical.
Data row 1 (row label cell, dark navy, white text: 「どんな合併？」): second column 「甲建物を、乙建物の附属建物とする」; third column 「接続する区分建物を、一個の建物にする」.
Data row 2 (row label cell, dark navy, white text: 「甲建物は？」): second column 「区分建物でも、そうでなくてもよい」; third column 「区分建物であること」.
Data row 3 (row label cell, dark navy, white text: 「接続は？」): second column 「要らない」; third column 「必要」.
Data row 4 (row label cell, dark navy, white text: 「主従の関係は？」): second column 「必要」; third column 「要らない」.
Data row 5 (row label cell, dark navy, white text: 「根拠」): second column 「規則132条・準則86条1号」; third column 「規則133条・準則86条2号」.
In data row 3 the words 「要らない」 in the second column have a pale yellow highlighter marker, and in data row 4 the words 「要らない」 in the third column have a pale yellow highlighter marker. Every other cell has its own text exactly as given.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 対, 建, 物, 登, 規, 記, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the two marked phrases carry the yellow marker, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：どちらの合併になるかの判定の流れ

- 型：フローチャート型　／　サイズ：1080×2900　／　保存名：`図解3_どちらの合併になるかの判定の流れ.png`
- 記事の挿入位置：「部品4：両方の要件がそろうとき」の直前（判断の流れの節）

```text
Create a Japanese-language infographic, portrait layout, 1080x2900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「どちらの合併になる？」
「上から順に確かめる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条1項3号・第56条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas for START, DIAMOND 1 and DIAMOND 2, in this order from top to bottom. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between them. Below DIAMOND 2 the chart splits: DIAMOND 3 sits at the lower left and DIAMOND 4 sits at the lower right, on the same row. RESULT 2 and RESULT 3 sit below DIAMOND 3, one at the lower left and one at the lower center-left. RESULT 4 and RESULT 5 sit below DIAMOND 4, one at the lower center-right and one at the lower right. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「甲建物と乙建物の合併を考える」
NODE DIAMOND 1: 「第56条の制限に当たるか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「当たる」 and 「当たらない」; do not draw the strings 「はい」 or 「いいえ」 on these arrows.
  - Arrow right with the label 「当たる」 to RESULT 1.
  - Arrow down with the label 「当たらない」 to DIAMOND 2.
NODE RESULT 1 (red box): 「どちらの合併も」 on the first line and 「できない」 on the second line.
NODE DIAMOND 2: 「どちらも区分建物で、互いに接続しているか？」 The text is placed inside the diamond on 3 lines. This diamond has TWO neutral navy branches with the labels 「接続する区分建物」 and 「それ以外」.
  - Arrow down-left with the label 「接続する区分建物」 to DIAMOND 3.
  - Arrow down-right with the label 「それ以外」 to DIAMOND 4.
NODE DIAMOND 3: 「主従の関係もあるか？」 This diamond has TWO neutral navy branches with the labels 「ある」 and 「ない」.
  - Arrow down-left with the label 「ある」 to RESULT 2.
  - Arrow down-right with the label 「ない」 to RESULT 3.
NODE RESULT 2 (blue box): 「附属合併も」 on the first line and 「区分合併も選べる」 on the second line.
NODE RESULT 3 (blue box): 「区分合併が」 on the first line and 「できる」 on the second line.
NODE DIAMOND 4: 「主従の関係があるか？」 This diamond has TWO neutral navy branches with the labels 「ある」 and 「ない」.
  - Arrow down-left with the label 「ある」 to RESULT 4.
  - Arrow down-right with the label 「ない」 to RESULT 5.
NODE RESULT 4 (blue box): 「附属合併が」 on the first line and 「できる」 on the second line.
NODE RESULT 5 (red box): 「どちらの合併も」 on the first line and 「できない」 on the second line.
Counts: 1 start node, 4 diamonds, 5 result boxes (3 blue boxes and 2 red boxes), 5 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three blue boxes have different texts (the strings 「附属合併も」, 「区分合併が」 and 「附属合併が」 are NOT identical); do not copy one into another. The two red boxes have the same text on purpose.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 当, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 4 diamonds and 5 result boxes, that every diamond shows only its two navy labels and no はい or いいえ, that RESULT 1 and RESULT 5 are red and RESULT 2, RESULT 3 and RESULT 4 are blue, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：場面ごとの早見表（どの合併ができるか）

- 型：早見表型（3列）　／　サイズ：1080×2300　／　保存名：`図解4_場面ごとの早見表.png`
- 記事の挿入位置：判定の流れの直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference table poster with three columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「場面ごとの早見表」
「どの合併ができる？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条1項3号」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: 「場面」, 「附属合併」, 「区分合併」.
Data row 1: first column 「第56条の制限に当たる」; second column 「できない」; third column 「できない」.
Data row 2: first column 「接続する区分建物どうしで、主従の関係もある」; second column 「できる」; third column 「できる」.
Data row 3: first column 「接続する区分建物どうしで、主従の関係はない」; second column 「できない」; third column 「できる」.
Data row 4: first column 「区分建物どうしだが接続しておらず、主従の関係はある」; second column 「できる」; third column 「できない」.
Data row 5: first column 「区分建物でない建物がからみ、主従の関係はある」; second column 「できる」; third column 「できない」.
Data row 6: first column 「主従の関係もなく、接続する区分建物どうしでもない」; second column 「できない」; third column 「できない」.
In data row 2 the words 「主従の関係もある」 in the first column have a pale yellow highlighter marker. Every row has its own first-column text exactly as given; the second and third columns use only the two strings 「できる」 and 「できない」 exactly as listed row by row.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 当, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that only the marked phrase in data row 2 carries the yellow marker, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解5：両方できるとき、合併後の姿で選ぶ

- 型：二択カード型　／　サイズ：1080×1800　／　保存名：`図解5_合併後の姿で選ぶ.png`
- 記事の挿入位置：「部品4：両方の要件がそろうとき」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a two-card choice poster.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「両方の要件がそろったら」
「合併後の姿で選ぶ」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条1項3号・不動産登記規則 第132条・第133条」
--- TWO CARDS ---
Two large cards stacked top and bottom, both exactly the same size, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, with no arrow and no connector between them, and with no check mark and no cross mark. The cards are separated only by a small empty gap.
Top card, heading 「附属合併を選ぶ」, an illustration of two touching apartment rooms where the second room has a small annex box labeled 「附属建物」, and two body lines: 「甲建物が、乙建物の附属建物になる」, 「乙建物の登記記録に入り、甲建物の登記記録は閉鎖」.
Bottom card, heading 「区分合併を選ぶ」, an illustration of two touching apartment rooms merged into one room, and two body lines: 「甲建物と乙建物が、一個の建物になる」, 「一棟の全部を合併すると、区分建物でなくなることがある」.
Under the two cards, one wide dark navy band with large white text 「条文は選び方を定めていない」, and under it one wide pale-yellow banner with dark navy text 「問題文の指示と、合併後の姿で決める」.
The top and bottom cards have clearly different texts; the texts are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 物, 登, 規, 記, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards plus the dark navy band and the pale-yellow banner, that the two cards have different texts, that no text overflows its box, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
