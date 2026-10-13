# 総合記事②不動産登記法編 第2章　図解インフォグラフィック プロンプト（【PB-14】表示に関する登記の登録免許税は、どの登記に・いくらかかるのか・2枚）

総合記事②不動産登記法編の第2章「添付情報・電子申請・登記識別情報・保存期間・登録免許税」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・対比・早見表が中心の図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解12）だけは、はい＝青・いいえ＝赤で描きます（緑には触れません）。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解20 | 表示の登記の登録免許税 | 早見表型（3列） | 1080×2300 | 不動産登記法編2章_図解20_登録免許税の仕分け.png | 【PB-14】「中身の整理」の直後 |
| 図解21 | 個数は、後の数で数える | カードポスター型 | 1080×2300 | 不動産登記法編2章_図解21_個数の数え方.png | 【PB-14】図解20の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解20：表示の登記の登録免許税

- 型：早見表型（3列）　／　サイズ：1080×2300　／　保存名：`不動産登記法編2章_図解20_登録免許税の仕分け.png`
- 記事の挿入位置：【PB-14】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「表示の登記の登録免許税」
「課税は分筆・区分と合筆・合併だけ」
Subtitle (smaller, centered, 1 line):
「登録免許税法 別表第一（十三）・第5条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Header row (dark navy cells with white text): 「登記」, 「課税の扱い」, 「金額」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「土地の分筆・建物の分割・区分」 | 「課税される」 | 「後の個数×1,000円」
Row 2: 「土地の合筆・建物の合併」 | 「課税される」 | 「後の個数×1,000円」
Row 3: 「一部地目変更」 | 「課税範囲外」 | 「かからない」
Row 4: 「表題部の登記の抹消（合筆の登記の錯誤による抹消など）」 | 「課税範囲外」 | 「かからない」
Row 5: 「墓地部分に関する登記（墳墓地に関する登記）」 | 「非課税」 | 「かからない」
Row 6: 「国などが私人に代位してする分筆の嘱託」 | 「非課税」 | 「かからない」
Highlighting: the string 「後の個数×1,000円」 in rows 1 and 2 has a pale yellow highlighter marker; the cells 「課税される」, 「課税範囲外」 and 「非課税」 differ in their wording, so copy each exactly as given. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「分筆・区分と合筆・合併だけが、後の個数×1,000円」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 地, 建, 物, 登, 記, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解21：個数は、後の数で数える

- 型：カードポスター型　／　サイズ：1080×2300　／　保存名：`不動産登記法編2章_図解21_個数の数え方.png`
- 記事の挿入位置：【PB-14】図解20の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with 3 numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「個数は、後の数で数える」
「再区分も、国との共有地も」
Subtitle (smaller, centered, 1 line):
「登録免許税法 別表第一（十三）イ」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「再区分（1個の区分建物を2個にする）」
Illustration: Two small apartment-building blocks separating from one block, no text.
Item lines (2 short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「区分後の2個で数える」
「1個×1,000円ではなく、2個で2,000円」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「区分後の個数」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「国と私人が共有する土地を、2筆に分筆する」
Illustration: A plot of land divided into two plots with a small flag icon at its edge, no text.
Item lines (2 short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「分筆後の2筆で数える」
「国の持分があっても、通常どおり課税」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「国が入っても課税」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「敷地権の目的である土地の筆数」
Illustration: Two small plots under one building block, no text.
Item lines (2 short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「数えない」
「数えるのは、区分建物の個数」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「筆数は数えない」
Under the last card, one wide dark navy band with large white text 「分筆・区分・合筆・合併は、後の個数×1,000円」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 権, 物, 登, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose, and confirm that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
