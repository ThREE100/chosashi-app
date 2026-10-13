# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（【PA-5】建物の表題登記は誰が、どの登記と併せて、誰に代わって申請するのか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解7 | 区分建物が新築されたとき、何と併せて申請する？ | フローチャート型（中立の分岐） | 1080×2300 | 不登法編1_図解7_区分建物の新築.png | 【PA-5】「中身の整理」の直後 |
| 図解8 | 建物の表題登記、誰が誰に代わる？ | カードポスター型（4枚） | 1080×2500 | 不登法編1_図解8_誰が誰に代わるか.png | 【PA-5】図解7の直後（「たとえば」の前） |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解7：区分建物が新築されたとき、何と併せて申請する？

- 型：フローチャート型（中立の分岐）　／　サイズ：1080×2300　／　保存名：`不登法編1_図解7_区分建物の新築.png`
- 記事の挿入位置：【PA-5】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「区分建物が新築されたとき」
「何と併せて申請する？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第48条・第52条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. START at the top, then the DIAMOND, then the two result boxes at the bottom, one down-left and one down-right of the diamond, side by side with the same size. All arrows are straight or have at most one right-angle bend and never cross each other. All arrows and labels are dark navy.
NODE START (rounded pill, dark navy): 「区分建物が新築されて、一棟の建物になった」
NODE DIAMOND: 「接続する建物（区分建物を除く）に、表題登記があるか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy and carry the labels 「ない」 and 「ある」; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.
  - Arrow down-left with the label 「ない」 to RESULT 1.
  - Arrow down-right with the label 「ある」 to RESULT 2.
NODE RESULT 1 (pale gray box with a dark navy outline): the first line 「他の区分建物の表題登記と併せる」, then body lines 「所有者が、他の区分建物の所有者に代わって申請できる」 and a small tag 「法48条1項・2項」.
NODE RESULT 2 (pale gray box with a dark navy outline): the first line 「既存建物の表題部の変更と併せる」 (the string 「表題部の変更」 has a pale yellow highlighter marker), then body lines 「既存建物の登記記録は残る。抹消ではない」 and a small tag 「法48条3項・52条1項」.
Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts; do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 建, 所, 物, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows only the two navy labels 「ない」 and 「ある」 and never 「はい」 or 「いいえ」, that RESULT 1 is on the left and RESULT 2 is on the right, that no text overflows its box, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解8：建物の表題登記、誰が誰に代わる？

- 型：カードポスター型（4枚）　／　サイズ：1080×2500　／　保存名：`不登法編1_図解8_誰が誰に代わるか.png`
- 記事の挿入位置：【PA-5】図解7の直後（「たとえば」の前）

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two or three short item lines, and one short conclusion tag. Do NOT render any paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「建物の表題登記、誰が誰に代わる？」
「代位は両方向、相続人は被承継人」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第47条・第48条・第52条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「未登記の建物に接続して新築」
Illustration: Two small isometric buildings joined together, one with a dashed outline, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「新築した区分建物の所有者が」
「他の区分建物の所有者に代わって」
「他の区分建物の表題登記を申請できる（法48条2項）」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「新築側が代わって申請」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「登記のある建物に接続して新築」
Illustration: Two small isometric buildings joined together, one with a ledger card beside it, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「新築区分建物の所有者は、既存建物の変更の登記を代わって申請できる（法48条4項）」
「既存建物の名義人は、新築区分建物の表題登記を代わって申請できる（法52条2項）」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「代位は両方向にある」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「全部の原始取得者が、一部を売却」
Illustration: A small apartment block icon with one door tagged with a key, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「原始取得者は、自分で申請できる（法47条1項）」
「代位に限られない」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「代位の形をとるのは転得者」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「区分建物を新築した人が亡くなった」
Illustration: A small document sheet with a pen, and a faded person pictogram behind it, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「相続人は、被承継人を表題部所有者として申請できる（法47条2項）」
「相続人自身を表題部所有者とする申請はできない」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「記録されるのは被承継人」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 売, 建, 所, 承, 物, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a paragraph of body text. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
