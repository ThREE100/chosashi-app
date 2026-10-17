# 論点別 復習用 図解インフォグラフィック プロンプト（T04 移記・転写（登記記録の記録の仕方）・1枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T04-1 | 移記と転写の見分け方（元の登記記録が閉鎖されるか） | 早見表型 | 1080×2500 | 移記と転写_図解1_移記と転写.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T04-1：移記と転写の見分け方（元の登記記録が閉鎖されるか）

- 型：早見表型　／　サイズ：1080×2500　／　保存名：`移記と転写_図解1_移記と転写.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「移記と転写の見分け方」
「元の登記記録が閉鎖されるか」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第107条・第120条・第124条・第129条・第130条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「元の登記記録」, 「記録の方法」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「合筆（承役地の地役権の登記）」 | 「甲土地は閉鎖される」 | 「移記。地役権設定の範囲と地役権図面番号も記録」
Row 2: 「合体による登記等（存続登記）」 | 「合体前の建物は閉鎖される」 | 「移記。末尾に移記した旨と年月日を記録」
Row 3: 「非区分建物の区分」 | 「区分前の甲建物は閉鎖される」 | 「移記。受付年月日と受付番号も記録」
Row 4: 「区分建物の区分」 | 「甲建物は閉鎖されない」 | 「転写。受付年月日と受付番号も記録」
Row 5: 「敷地権でなくなった（建物から土地へ）」 | 「建物の登記記録は閉鎖されない」 | 「転写。特定登記だけ。末尾に転写した旨を記録」
Highlighting: the string 「転写」 inside the column-3 cell of row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
--- NOTE CARD (below, a wide card with a dashed dark navy outline and a small dark navy tag 「補足」) ---
Heading (bold): 「土地には転写されないもの」
Body lines, each with a small dark navy dot at its left end (NO number on the dots):
「建物のみに関する旨の付記登記がある抵当権は、特定登記ではないので、土地には転写されない（規則124条3項）」
Under the note card, one wide dark navy band with large white text 「閉鎖されるなら移記、残るなら転写」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 当, 承, 抵, 権, 物, 番, 登; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
