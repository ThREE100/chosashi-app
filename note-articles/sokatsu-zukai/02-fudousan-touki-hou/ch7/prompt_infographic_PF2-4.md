# 総合記事② 不動産登記法編 第7章　図解インフォグラフィック プロンプト（【PF2-4】合体前の建物の権利は、合体後の建物にどう引き継がれ、どう消えるのか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第7章「建物の合体による登記等」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch7.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は、分類・早見表が中心のものは、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解4）だけは、はい＝青・いいえ＝赤です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解7 | 合体前の権利は、どうなる？（存続させる権利の仕分け） | 早見表型（3列） | 1080×2100 | 登記法編7章_図解7_存続させる権利の仕分け.png | 【PF2-4】「中身の整理」の直後 |
| 図解8 | 合体の添付情報（記号で呼び分けて覚える） | 早見表型（2列） | 1080×2400 | 登記法編7章_図解8_添付情報の記号.png | 【PF2-4】図解7の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解7：合体前の権利は、どうなる？（存続させる権利の仕分け）

- 型：早見表型（3列）　／　サイズ：1080×2100　／　保存名：`登記法編7章_図解7_存続させる権利の仕分け.png`
- 記事の挿入位置：【PF2-4】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (早見表), followed by one dashed side note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「合体前の権利は、どうなる？」
「存続させる権利を仕分ける」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第50条・不動産登記令 別表13の項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Header row (dark navy cells with white text): 「合体前の権利」, 「合体後の建物の持分に」, 「添えるもの」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「所有権の登記以外の所有権に関する登記」 | 「存続させられる」 | 「権利者の承諾情報等（ト）」
Row 2: 「先取特権・質権の登記」 | 「存続させられる」 | 「権利者の承諾情報等（ト）」
Row 3: 「抵当権の登記」 | 「存続させられる」 | 「権利者の承諾情報等（ト）」
Row 4: 「抵当証券が発行されている抵当権」 | 「存続させられる」 | 「承諾情報等（チ）と抵当証券」
Row 5: 「賃借権の登記」 | 「存続させられない（実務の整理）」 | 「申請情報にも書かない」
Highlighting: the string 「と抵当証券」 in the column-3 cell of row 4 has a pale yellow highlighter marker; row 5 has a slightly darker pale gray fill across all three cells to show that it is the one that cannot be kept. Copy each cell exactly as given; the cells 「存続させられる」 and 「存続させられない（実務の整理）」 differ in wording, so do not change one into the other.
--- SIDE NOTE CARD (below the table, a wide card with a dashed dark navy outline) ---
Heading 「存続させずに消すとき」, body 「権利者が消滅を承諾した情報を提供して、消滅の登記をする（法50条）」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 当, 所, 承, 抵, 権, 物, 登, 記, 証, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that rows 1 to 4 read 「存続させられる」 and only row 5 reads 「存続させられない（実務の整理）」, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解8：合体の添付情報（記号で呼び分けて覚える）

- 型：早見表型（2列）　／　サイズ：1080×2400　／　保存名：`登記法編7章_図解8_添付情報の記号.png`
- 記事の挿入位置：【PF2-4】図解7の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with two columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「合体の添付情報」
「記号で呼び分けて覚える」
Subtitle (smaller, centered, 1 line):
「不動産登記令 別表13の項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 2 columns and exactly 9 data rows, no merged cells. Column 1 is narrow and holds one katakana letter; column 2 is wide.
Header row (dark navy cells with white text): 「記号」, 「添える情報」.
Data rows, one per line, in this order (column 1 | column 2):
Row 1: 「イ」 | 「建物図面」
Row 2: 「ロ」 | 「各階平面図」
Row 3: 「ハ」 | 「表題部所有者となる者が所有権を有することを証する情報」
Row 4: 「ニ」 | 「表題部所有者となる者の住所を証する情報」
Row 5: 「ホ」 | 「敷地権とならない事由を証する情報（合体前後とも敷地権の登記がない区分建物のときは不要）」
Row 6: 「ヘ」 | 「合体後の建物に敷地権が存するときの、規約を設定したことを証する情報など」
Row 7: 「ト」 | 「存続登記と同一の登記をするときの、権利者の承諾情報等」
Row 8: 「チ」 | 「抵当証券が発行されているときの、承諾情報等と抵当証券」
Row 9: 「リ」 | 「所有権の登記を併せて申請するときの、登記名義人となる者の住所を証する情報」
Highlighting: the katakana letters of rows 3, 5, 7 and 8 (ハ, ホ, ト, チ) in column 1 have a pale yellow highlighter marker; all other cells are plain. The nine katakana letters in column 1 are different from each other and appear in the order イ, ロ, ハ, ニ, ホ, ヘ, ト, チ, リ; copy each exactly as given.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 当, 所, 承, 抵, 権, 物, 登, 規, 記, 証, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 2 columns and exactly 9 data rows, that column 1 reads イ, ロ, ハ, ニ, ホ, ヘ, ト, チ, リ in this order with no letter duplicated or missing, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
