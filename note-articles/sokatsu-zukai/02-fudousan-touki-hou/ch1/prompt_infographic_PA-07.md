# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（【PA-7】分筆の登記を、誰が申請でき、誰が代位して申請できるのか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解10 | 分筆を申請できるのは誰？ | 早見表型（3列） | 1080×2400 | 不登法編1_図解10_分筆の申請人.png | 【PA-7】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解10：分筆を申請できるのは誰？

- 型：早見表型（3列）　／　サイズ：1080×2400　／　保存名：`不登法編1_図解10_分筆の申請人.png`
- 記事の挿入位置：【PA-7】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆を申請できるのは誰？」
「原則は名義人、代位は保全の必要性」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第39条・第30条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Header row (dark navy cells with white text): 「申請する人」, 「結論」, 「決め手」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「表題部所有者・所有権の登記名義人（その相続人）」 | 「申請できる」 | 「原則（法39条1項・30条）」
Row 2: 「土地の一部の買主が設定した、抵当権者」 | 「代位して申請できる」 | 「担保の目的物（その部分）を特定する必要」
Row 3: 「共有物分割の確定判決を得た共有者」 | 「協力しない共有者に代位して申請できる」 | 「判決正本が代位原因を証する情報」
Row 4: 「土地の一部に地役権を得た、地役権者」 | 「代位して申請できない」 | 「保全の必要性がない」
Row 5: 「遺産分割で、土地を取得する相続人」 | 「申請できる」 | 「遺産分割協議書と分筆後の地積測量図等」
Row 6: 「遺産分割で、どちらも取得しない相続人」 | 「申請できない」 | 「取得する相続人が申請人になる」
Highlighting: the cells of column 2 in rows 4 and 6 have a pale yellow highlighter marker over the whole cell text; the cells of column 2 in rows 1, 2, 3 and 5 are plain. The strings 「代位して申請できる」 and 「代位して申請できない」 differ by one character; copy each exactly as given and do not change one into the other.
Under the table, one wide dark navy band with large white text 「代位できるかは、保全の必要性があるかで決まる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 保, 地, 当, 所, 抵, 権, 物, 登, 記, 証, 請, 買; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that row 2 reads 代位して申請できる and row 4 reads 代位して申請できない (never swapped), and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
