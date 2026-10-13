# 総合記事②不動産登記法編 第6章　図解インフォグラフィック プロンプト（【PF1-1】合併の登記ができないのはどんな場合か（法第56条）・2枚）

総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『できない建物の一覧』『要る・要らない』のような分類が中心なので、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。フローチャート（図解4）だけは、分岐の矢印とラベルを濃紺にし、結果の箱を『5号の制限に当たらない＝青』『5号の制限に当たる＝赤』で塗り分けます（『はい』『いいえ』の文字は使いません）。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解2 | 合併できない建物は？（法56条の5つ） | 早見表型（3列） | 1080×1900 | 不登法編6章_図解2_法56条の5つ.png | 【PF1-1】「中身の整理」の直後 |
| 図解3 | 住所が食い違うとき、合併の前に何をする？ | ステップ型 | 1080×2400 | 不登法編6章_図解3_住所の食い違い.png | 【PF1-1】「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解2：合併できない建物は？（法56条の5つ）

- 型：早見表型（3列）　／　サイズ：1080×1900　／　保存名：`不登法編6章_図解2_法56条の5つ.png`
- 記事の挿入位置：【PF1-1】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「合併できない建物は？」
「法56条の5つを覚える」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第56条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Header row (dark navy cells with white text): 「号」, 「合併の登記ができない建物」, 「見分け方」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「1号」 | 「共用部分である旨の登記又は団地共用部分である旨の登記がある建物」 | 「両方にあっても不可」
Row 2: 「2号」 | 「表題部所有者・所有権の登記名義人が相互に異なる建物」 | 「名義人が違う」
Row 3: 「3号」 | 「表題部所有者・所有権の登記名義人が相互に持分を異にする建物」 | 「持分が違う」
Row 4: 「4号」 | 「所有権の登記がない建物と、所有権の登記がある建物」 | 「登記の有無が違う」
Row 5: 「5号」 | 「所有権等の登記以外の権利に関する登記がある建物」 | 「例外は担保権と信託（規則131条）」
Highlighting: the string 「両方にあっても不可」 of row 1 and the string 「例外は担保権と信託（規則131条）」 of row 5 have a pale yellow highlighter marker; the other cells are plain. Copy each cell exactly as given.
Row order rule: the first column reads 「1号」, 「2号」, 「3号」, 「4号」, 「5号」 from top to bottom, each exactly once; no row is duplicated, merged, or missing.
Under the table, one wide dark navy band with large white text 「地番区域が異なっても、建物は合併できる」 and, directly below it, one smaller line of white text 「土地の合筆は、地番区域が異なると不可（法41条2号）」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 号, 地, 建, 所, 権, 無, 物, 番, 登, 規, 記, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows in the order 1号 to 5号, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：住所が食い違うとき、合併の前に何をする？

- 型：ステップ型　／　サイズ：1080×2400　／　保存名：`不登法編6章_図解3_住所の食い違い.png`
- 記事の挿入位置：【PF1-1】「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical step poster with four step cards and one side note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「住所が食い違うとき」
「合併の前に何をする？」
Subtitle (smaller, centered, 1 line):
「建物の合併の登記（実務の取扱い）」
--- STEPS ---
Layout: four step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to 4 in order), one bold heading line, and one or two short body lines.
STEP 1: heading 「甲建物の登記は、旧住所のまま」, body 「引っ越したあとに、乙建物を取得して登記した」.
STEP 2: heading 「登記記録上の住所が、食い違う」, body 「同じ人でも、同一人とは扱われない」.
STEP 3 (the card has a pale yellow highlighter marker on its heading): heading 「住所の変更を証する情報を付けても足りない」, body 「住民票を付けても、合併はできない」.
STEP 4: heading 「先に、甲建物の住所の変更の登記をする」, body 「そのあとで、合併の登記を申請する」.
--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---
Heading 「住居表示の実施で住所が変わったときも同じ」, body 「住居表示の実施を証する情報を付けても足りない」 and a small gray tag 「条文に明記はなく、実務の取扱い」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 物, 登, 記, 証, 請, 違, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly four step cards numbered 1 to 4 in order, followed by exactly one side note card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
