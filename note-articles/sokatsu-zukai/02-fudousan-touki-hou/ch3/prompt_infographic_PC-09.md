# 総合記事②不動産登記法編 第3章　図解インフォグラフィック プロンプト（【PC-9】地図・地積測量図には何を記録し、どう作るのか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表が中心の図は、青・赤・チェック・バツを使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。はい／いいえの判定の流れ図だけ、共通部品の配色の規則（青＝はい、赤＝いいえ）で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解13 | 地積測量図の記録事項（分筆で省略できるのは4つ） | 早見表型（3列） | 1080×2500 | 不登法第3章_図解13_地積測量図の記録事項.png | 【PC-9】『中身の整理』の直後 |
| 図解14 | 地積測量図と地図の約束ごと（精度・署名・座標値） | カードポスター型 | 1080×2300 | 不登法第3章_図解14_精度署名座標値.png | 【PC-9】『たとえば』の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解13：地積測量図の記録事項（分筆で省略できるのは4つ）

- 型：早見表型（3列）　／　サイズ：1080×2500　／　保存名：`不登法第3章_図解13_地積測量図の記録事項.png`
- 記事の挿入位置：【PC-9】『中身の整理』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「地積測量図の記録事項」
「分筆で省略できるのは4つ」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第77条・準則 第72条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 10 data rows, no merged cells.
Header row (dark navy cells with white text): 「号」, 「記録事項」, 「分筆の便宜省略」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「1号」 | 「地番区域の名称」 | 「省略の対象外」
Row 2: 「2号」 | 「方位」 | 「省略の対象外」
Row 3: 「3号」 | 「縮尺」 | 「省略の対象外」
Row 4: 「4号」 | 「地番（隣接地の地番を含む）」 | 「省略の対象外」
Row 5: 「5号」 | 「地積及びその求積方法」 | 「求積方法だけ省略できる」
Row 6: 「6号」 | 「筆界点間の距離」 | 「省略できる」
Row 7: 「7号」 | 「平面直角座標系の番号又は記号」 | 「省略できる」
Row 8: 「8号」 | 「基本三角点等に基づく測量の成果による筆界点の座標値」 | 「省略できる」
Row 9: 「9号」 | 「境界標があるときは、その表示」 | 「省略の対象外」
Row 10: 「10号」 | 「測量の年月日」 | 「省略の対象外」
Highlighting: the cell 「方位」 of row 2 and the cell 「地積及びその求積方法」 of row 5 have a pale yellow highlighter marker. The cells 「省略できる」 and 「省略の対象外」 differ in wording; copy each exactly as given and do not change one into the other.
Under the table, one wide dark navy band with large white text 「省略できるのは、特別の事情があるとき、分筆後の1筆だけ」.
Under the band, one small light-gray tag centered: 「座標値を記録しても、方位は省略できない」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 対, 番, 登, 規, 記, 録, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 10 data rows labeled 1号 to 10号 in order, that rows 5, 6, 7 and 8 are the only rows whose third cell contains 省略できる, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解14：地積測量図と地図の約束ごと（精度・署名・座標値）

- 型：カードポスター型　／　サイズ：1080×2300　／　保存名：`不登法第3章_図解14_精度署名座標値.png`
- 記事の挿入位置：【PC-9】『たとえば』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with three numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「地積測量図と地図の約束ごと」
「精度・署名・座標値」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第10条・第13条・第74条・第77条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「精度区分は、土地の地域で決まる」
Illustration: A map sheet with three small zone icons in a row (houses, farmland, mountains), no text on the icons.
Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「市街地地域：甲二まで」
「村落・農耕地域：乙一まで」
「山林・原野地域：乙三まで」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「地域で決まる。区分は上限」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「地積測量図の作成者」
Illustration: A drawing sheet with a pen signing in the corner and a small rubber stamp beside it, no text on the sheet.
Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「署名するか、記名して押印する」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「署名すれば押印は不要」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「電磁的記録に記録する地図」
Illustration: A computer screen icon showing a map with small dots on the corners of the plots, no text on the screen.
Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「各筆界点の座標値を記録する」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「座標値の記録」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 押, 登, 規, 記, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
