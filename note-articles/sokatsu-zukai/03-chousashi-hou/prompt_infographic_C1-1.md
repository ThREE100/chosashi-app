# 総合記事③ 土地家屋調査士法編　図解インフォグラフィック プロンプト（【C1-1】正当な事由がなくても依頼を拒めるのは、どの業務か（調査士法人でも同じか）・2枚）

総合記事③「直前期の苦手論点つぶし 土地家屋調査士法編」（`note-articles/column/sokatsu-03-chousashi-hou.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この科目の図解は『拒めるか・要るか』のような分類が中心で、はい／いいえの分岐ではないため、共通部品の配色の規則（青＝はい、赤＝いいえ）は入れず、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解2 | 正当な事由なく拒めるのは？（法3条1項の号で仕分ける） | 対比表型（3列） | 1080×1900 | 調査士法編_図解2_正当な事由なく拒めるのは.png | 【C1-1】「中身の整理」の直後 |
| 図解3 | 22条と22条の2は、別の話（同意で行えるのはどれ） | 対比表型＋カード | 1080×2300 | 調査士法編_図解3_22条と22条の2は別の話.png | 【C1-1】「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解2：正当な事由なく拒めるのは？（法3条1項の号で仕分ける）

- 型：対比表型（3列）　／　サイズ：1080×1900　／　保存名：`調査士法編_図解2_正当な事由なく拒めるのは.png`
- 記事の挿入位置：【C1-1】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「正当な事由なく拒めるのは？」
「法3条1項の号で仕分ける」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法 第22条・第3条第1項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 8 data rows, no merged cells.
Header row (dark navy cells with white text): 「号」, 「業務（法3条1項）」, 「正当な事由がなくても拒めるか」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「1号」 | 「表示登記のための調査・測量」 | 「拒めない」
Row 2: 「2号」 | 「表示登記の申請手続・審査請求の代理」 | 「拒めない」
Row 3: 「3号」 | 「表示登記の申請書類の作成」 | 「拒めない」
Row 4: 「4号」 | 「筆界特定の手続の代理」 | 「拒める」
Row 5: 「5号」 | 「筆界特定の書類の作成」 | 「拒めない」
Row 6: 「6号」 | 「前各号の事務についての相談」 | 「4号に関する部分だけ拒める」
Row 7: 「7号」 | 「民間紛争解決手続の代理」 | 「拒める」
Row 8: 「8号」 | 「その相談」 | 「拒める」
Highlighting: in column 3, the strings 「拒める」 of rows 4, 7 and 8 and the string 「4号に関する部分だけ拒める」 of row 6 have a pale yellow highlighter marker; every 「拒めない」 cell is plain. The cells 「拒める」 and 「拒めない」 differ by one character; copy each exactly as given and do not change one into the other.
Under the table, one wide dark navy band with large white text 「調査士法人も同じ（法41条1項が法22条を準用）」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 対, 当, 登, 解, 記, 請, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 8 data rows, that every cell reads exactly as given, that exactly the rows 4, 7 and 8 read 「拒める」 in column 3 and the other rows other than row 6 read 「拒めない」, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：22条と22条の2は、別の話（同意で行えるのはどれ）

- 型：対比表型＋カード　／　サイズ：1080×2300　／　保存名：`調査士法編_図解3_22条と22条の2は別の話.png`
- 記事の挿入位置：【C1-1】「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster: two cards at the top and a table below.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「22条と22条の2は、別の話」
「同意で行えるのはどれ？」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法 第22条・第22条の2」
--- TWO CARDS (side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card, small tag 「法22条」, heading 「依頼を拒めるか」, body 「正当な事由がなければ、拒めない」.
Right card, small tag 「法22条の2」, heading 「その事件の業務を行ってよいか」, body 「行ってはならない事件がある」.
The two cards have clearly different texts; the texts are NOT identical.
--- TABLE ---
A small dark navy tag above the table: 「法22条の2第2項（筆界特定手続代理関係業務）」.
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Header row (dark navy cells with white text): 「号」, 「行ってはならない事件」, 「依頼者の同意」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「1号」 | 「相手方の協議を受けて賛助し、又はその依頼を承諾した事件」 | 「同意があっても行えない」
Row 2: 「2号」 | 「相手方の協議を受けた事件で、信頼関係に基づくもの」 | 「同意があっても行えない」
Row 3: 「3号」 | 「受任している事件の相手方からの依頼による他の事件」 | 「同意があれば行える」
Row 4: 「4号〜6号」 | 「調査士法人の社員・使用人としての事件」 | 「同意があっても行えない」
Row 5: 「7号」 | 「調査士法人の使用人としての、3号と同様の事件」 | 「同意があれば行える」
Highlighting: the string 「同意があれば行える」 of rows 3 and 5 has a pale yellow highlighter marker; the three cells 「同意があっても行えない」 are plain. The two kinds of cells differ in their wording; copy each exactly as given and do not change one into the other.
Under the table, one wide dark navy band with large white text 「同意で外れるのは、3号と7号だけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 当, 承, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards at the top and a table with exactly 3 columns and exactly 5 data rows, that rows 3 and 5 read 「同意があれば行える」 and rows 1, 2 and 4 read 「同意があっても行えない」, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
