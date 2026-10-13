# 総合記事② 不動産登記法編 第9章　図解インフォグラフィック プロンプト（【PG2-1】区分建物の表示・合併・区分に、非区分建物のルールをどこまで持ち込めるか・3枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第9章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch9.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『誰が・いつまでに・何を添えるか』の分類や手続の流れが中心で、はい／いいえの分岐ではないため、共通部品の配色の規則（青＝はい、赤＝いいえ）は入れず、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解2 | 区分建物の表示の3つの決まり（非区分建物とどこが違うか） | 対比表型（3列） | 1080×1900 | 不登法編ch9_図解2_区分建物の表示の3つの決まり.png | 【PG2-1】「中身の整理」の直後 |
| 図解3 | 主従が要る合併、要らない合併（附属合併と区分合併） | 対比カード型（2列） | 1080×1900 | 不登法編ch9_図解3_附属合併と区分合併.png | 【PG2-1】図解2の直後 |
| 図解4 | 建物を区分したとき、抵当権が残るのはどちらか | ステップ型＋結果カード | 1080×2300 | 不登法編ch9_図解4_区分の登記と抵当権.png | 【PG2-1】「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解2：区分建物の表示の3つの決まり（非区分建物とどこが違うか）

- 型：対比表型（3列）　／　サイズ：1080×1900　／　保存名：`不登法編ch9_図解2_区分建物の表示の3つの決まり.png`
- 記事の挿入位置：【PG2-1】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「区分建物の表示の3つの決まり」
「非区分建物とどこが違うか」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第115条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells.
Header row (dark navy cells with white text): 「区分建物の場面」, 「扱い」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「床面積の測り方」 | 「壁その他の区画の内側線で囲まれた部分（非区分建物は中心線）」 | 「規則115条」
Row 2: 「柱が突き出ているとき」 | 「凹凸をならして、壁面のみで囲まれた部分を求積する」 | 「実務の取扱い（条文に明記なし）」
Row 3: 「地下と地上にまたがるとき」 | 「階層を地下一階付き平家建とは表示しない」 | 「実務の取扱い（直接の条文は確認できていない）」
Highlighting: the string 「内側線」 in row 1 has a pale yellow highlighter marker. The cells of column 3 in rows 2 and 3 have a slightly darker pale gray fill to show that they are practice, not a written provision. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「区分建物は、非区分建物のルールをそのまま使えない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 対, 建, 物, 登, 規, 記, 認, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：主従が要る合併、要らない合併（附属合併と区分合併）

- 型：対比カード型（2列）　／　サイズ：1080×1900　／　保存名：`不登法編ch9_図解3_附属合併と区分合併.png`
- 記事の挿入位置：【PG2-1】図解2の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards, one example strip, and one band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「主従が要る合併、要らない合併」
「附属合併と区分合併を並べる」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第86条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「主たる建物と附属建物」, heading 「附属合併」, and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「主従の関係にないと、できない」, 「主従の関係が要る」 (the string 「主従の関係が要る」 has a pale yellow highlighter marker).
Right card: small tag 「区分建物どうし」, heading 「区分合併」, and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「互いに接続していないと、できない」, 「主従の関係は要らない」 (the string 「主従の関係は要らない」 has a pale yellow highlighter marker).
The two cards have clearly different texts; the texts are NOT identical.
--- EXAMPLE STRIP (below the two cards, a wide card with a dashed dark navy outline and a small dark navy tag 「たとえば」) ---
Body 「名義人が同じ、隣り合う101号室と102号室」 and 「主従の関係がなくても、接続していれば区分合併ができる」.
Under the example strip, one wide dark navy band with large white text 「主従が要るのは、附属合併だけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards with exactly two item lines each, that the headings 附属合併 and 区分合併 are not swapped, that the example strip is below the two cards, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：建物を区分したとき、抵当権が残るのはどちらか

- 型：ステップ型＋結果カード　／　サイズ：1080×2300　／　保存名：`不登法編ch9_図解4_区分の登記と抵当権.png`
- 記事の挿入位置：【PG2-1】「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical step poster with three step cards followed by two result cards side by side.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「建物を区分したとき」
「抵当権が残るのはどちらか」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第130条第1項」
--- STEPS ---
Layout: three step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1, 2, 3 in order), one bold heading line, and one body line.
STEP 1: heading 「抵当権つきの建物を、2個に区分する」, body 「建物の区分の登記を申請する」.
STEP 2: heading 「原則は、区分後の各建物に引き継がれる」, body 「権利に関する登記を移記する（規則130条1項）」.
STEP 3 (the card has a pale yellow highlighter marker on its heading): heading 「抵当権者が、一方の建物の消滅を承諾」, body 「消滅の承諾を証する情報を提供する」.
--- RESULT CARDS (below the steps, two cards side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card, with no arrow into them and no check mark and no cross) ---
Left result card: small tag 「抵当権の消滅を承諾」, heading 「承諾のあった建物」, body 「抵当権の登記は、載らない」.
Right result card: small tag 「消滅の承諾がない」, heading 「承諾のない建物」, body 「抵当権の登記が、転写される」 (the string 「転写される」 has a pale yellow highlighter marker).
The two result cards have clearly different texts; the texts are NOT identical.
Under the two result cards, one wide dark navy band with large white text 「抵当権が残るのは、承諾のない建物だけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 当, 承, 抵, 権, 物, 登, 規, 記, 証, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly three step cards numbered 1 to 3 in order, followed by exactly two result cards side by side, that the arrows carry no labels, that the headings 承諾のあった建物 and 承諾のない建物 are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
