# 総合記事②不動産登記法編 第4章　図解インフォグラフィック プロンプト（【PD-1】分筆を申請できるのは誰か。管理人・共有者・買主・国はどうか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『申請できるか』『合筆できるか』のような分類が中心で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。例外は、はい／いいえの判定の流れ図（分筆を錯誤で戻せるか）で、はい＝青、いいえ＝赤で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解2 | 分筆・合筆を申請できる人は？ | 早見表型（3列） | 1080×2000 | 不動産登記法編4章_図解2_分筆合筆を申請できる人.png | 【PD-1】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解2：分筆・合筆を申請できる人は？

- 型：早見表型（3列）　／　サイズ：1080×2000　／　保存名：`不動産登記法編4章_図解2_分筆合筆を申請できる人.png`
- 記事の挿入位置：【PD-1】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆・合筆を申請できる人は？」
「名義人と、代位できる人」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第39条第1項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Header row (dark navy cells with white text): 「申請する人」, 「申請できるか」, 「決め手」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「表題部所有者・所有権の登記名義人」 | 「申請できる」 | 「法39条1項」
Row 2: 「表題部所有者の土地を買っただけの者」 | 「自分では申請できない」 | 「売主の承諾書があっても同じ」
Row 3: 「土地の一部を買った者」 | 「売主に代位して申請できる」 | 「民法423条・令3条4号」
Row 4: 「共有地の持分の一部を買った者（国を含む）」 | 「当然には代位できない」 | 「土地を分ける前提がない」
Row 5: 「共有者の1人」 | 「単独では申請できない（原則）」 | 「承諾書を添えても同じ」
Row 6: 「相続財産の管理人・不在者の財産管理人」 | 「申請できる」 | 「家庭裁判所の許可は要らない」
Highlighting: the string 「当然には代位できない」 of row 4 and the string 「家庭裁判所の許可は要らない」 of row 6 have a pale yellow highlighter marker; every other cell is plain. Copy each cell exactly as given; cells that look alike differ in their wording, so do not change one into another.
Under the table, one wide dark navy band with large white text 「名義人以外は、代位の根拠があるときだけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 売, 当, 所, 承, 権, 登, 記, 請, 諾, 買; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that only the two marked strings are highlighted, and that no check mark, no cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
