# 総合記事②不動産登記法編 第3章　図解インフォグラフィック プロンプト（【PC-1】地目は「土地全体の主な用途」で一つに決まるのか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表が中心の図は、青・赤・チェック・バツを使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。はい／いいえの判定の流れ図だけ、共通部品の配色の規則（青＝はい、赤＝いいえ）で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解2 | 水に関わる土地の地目（ため池・池沼・用悪水路・雑種地） | 早見表型（3列） | 1080×1700 | 不登法第3章_図解2_水に関わる土地の地目.png | 【PC-1】『中身の整理』の直後 |
| 図解3 | 地目を決める順番 | ステップ型 | 1080×2000 | 不登法第3章_図解3_地目を決める順番.png | 【PC-1】『判断のしかた』の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解2：水に関わる土地の地目（ため池・池沼・用悪水路・雑種地）

- 型：早見表型（3列）　／　サイズ：1080×1700　／　保存名：`不登法第3章_図解2_水に関わる土地の地目.png`
- 記事の挿入位置：【PC-1】『中身の整理』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「水に関わる土地の地目」
「ため池・池沼・用悪水路・雑種地」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第68条・第69条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Header row (dark navy cells with white text): 「土地の状況」, 「地目」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「耕地かんがい用の用水貯留池」 | 「ため池」 | 「準則68条17号」
Row 2: 「かんがい用水でない水の貯留池」 | 「池沼」 | 「準則68条8号」
Row 3: 「かんがい用又は悪水排せつ用の水路」 | 「用悪水路」 | 「準則68条16号」
Row 4: 「水力発電のための水路又は排水路」 | 「雑種地」 | 「準則69条5号」
Highlighting: the strings 「ため池」 of row 1, 「池沼」 of row 2 and 「雑種地」 of row 4 have a pale yellow highlighter marker. Rows 1 and 2 have similar wording in column 1 but different meanings; copy each cell exactly as given and do not change one into the other.
Under the table, one wide dark navy band with large white text 「同じ水の土地でも、かんがい用かどうかと用途で地目が分かれる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 対, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that row 1 reads ため池 and row 2 reads 池沼 in column 2, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：地目を決める順番

- 型：ステップ型　／　サイズ：1080×2000　／　保存名：`不登法第3章_図解3_地目を決める順番.png`
- 記事の挿入位置：【PC-1】『判断のしかた』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical step poster with 3 step cards and one closing band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「地目を決める順番」
「土地全体の用途から考える」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第99条・準則 第68条・第69条」
--- STEPS ---
Layout: 3 step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to 3 in order), one bold heading line, and one body line.
STEP 1 (the card has a pale yellow highlighter marker on its heading): heading 「土地全体の主な用途を見る」, body 「わずかな差異があっても、全体で一つに決める」.
STEP 2: heading 「水に関わるなら、かんがい用か見る」, body 「貯留池は、かんがい用ならため池、でなければ池沼。発電用の水路は雑種地」.
STEP 3: heading 「建物が附随的か見る」, body 「遊園地・ゴルフ場などで附随的なら、全体を一団の雑種地」.
Under the steps, one wide dark navy band with large white text 「畑・雑種地のような複合地目は付けられない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 物, 番, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 3 step cards numbered 1 to 3 in order, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
