# 論点別 復習用 図解インフォグラフィック プロンプト（T01 敷地権・敷地利用権・分離処分可能規約・4枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T01-1 | 敷地権になる条件（4つがそろったものだけ） | ステップ型 | 1080×2200 | 敷地権_図解1_敷地権の条件.png |
| 図解T01-2 | どの権利が敷地権になるか（場面別に仕分ける） | 早見表型 | 1080×2400 | 敷地権_図解2_権利別の早見表.png |
| 図解T01-3 | 敷地権の割合の決まり方（専有部分を何個持つかで分かれる） | 対比カード型（2列） | 1080×1900 | 敷地権_図解3_敷地権の割合.png |
| 図解T01-4 | 敷地権が変わったとき（どの登記を、いつまでに） | 早見表型 | 1080×2200 | 敷地権_図解4_敷地権が変わるとき.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T01-1：敷地権になる条件（4つがそろったものだけ）

- 型：ステップ型　／　サイズ：1080×2200　／　保存名：`敷地権_図解1_敷地権の条件.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical step poster with four step cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権になる条件」
「4つがそろったものだけ」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第44条1項9号／区分所有法 第22条」
--- STEPS ---
Layout: four step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1, 2, 3, 4 in order), one bold heading line, and one body line.
STEP 1: heading 「区分建物の敷地である」, body 「建物が所在する土地。床面積に入らないベランダの直下の土地も敷地」.
STEP 2: heading 「土地を使う権利である（敷地利用権）」, body 「所有権・賃借権など。使用貸借の権利は登記できないので、敷地権にならない」.
STEP 3 (the card has a pale yellow highlighter marker on its heading): heading 「専有部分と分離して処分できない」, body 「数人で有する権利は分離処分が禁止される（区分所有法22条1項）。専有部分の全部を持つ人の単独所有も同じ（同条3項）」.
STEP 4: heading 「登記された権利である」, body 「本登記であることが必要。仮登記は、敷地権として登記されない」.
Under the steps, one wide dark navy band with large white text 「規約で別段の定めをすると、分離して処分できて敷地権にならない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 所, 権, 物, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly four step cards numbered 1 to 4 in order, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T01-2：どの権利が敷地権になるか（場面別に仕分ける）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`敷地権_図解2_権利別の早見表.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「どの権利が敷地権になるか」
「場面別に仕分ける」
Subtitle (smaller, centered, 1 line):
「区分所有法 第22条／不動産登記法 第44条1項9号」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「分離処分」, 「敷地権」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「数人で有する所有権（共有）」 | 「できない（区分所有法22条1項）」 | 「登記されれば、なる」
Row 2: 「数人で有する賃借権（準共有）」 | 「できない（同条1項）」 | 「登記されれば、なる」
Row 3: 「専有部分の全部を持つ人の単独所有」 | 「できない（同条3項）」 | 「登記されれば、なる」
Row 4: 「各自が別の筆を単独で所有（分有）」 | 「規約がなくてもできる」 | 「ならない」
Row 5: 「使用貸借で借りているだけの人」 | 「該当しない（登記できない権利）」 | 「ならない」
Row 6: 「仮登記がされた権利」 | 「本登記ではない」 | 「ならない」
Highlighting: the string 「規約がなくてもできる」 inside the column-3 cell of row 5 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「分有は、規約がなくても分離して処分できる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 当, 所, 権, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T01-3：敷地権の割合の決まり方（専有部分を何個持つかで分かれる）

- 型：対比カード型（2列）　／　サイズ：1080×1900　／　保存名：`敷地権_図解3_敷地権の割合.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権の割合の決まり方」
「専有部分を何個持つかで分かれる」
Subtitle (smaller, centered, 1 line):
「区分所有法 第14条・第22条2項」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「専有部分を数個持つ人」, heading 「専有部分の床面積の割合」 (the string 「専有部分の床面積の割合」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「原則は、専有部分の床面積の割合（区分所有法22条2項本文・14条1項）」, 「床面積は、壁などの内側で測る（同法14条3項）」, 「規約で別の割合を定めてもよい（22条2項ただし書）」, 「規約の割合にしたときは、規約を設定したことを証する情報を提供（令別表16項ハ（2））」.
Right card: small tag 「甲と乙が1個ずつ持つ」, heading 「土地の持分の割合」 (the string 「土地の持分の割合」 has a pale yellow highlighter marker), and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「それぞれが有する土地の持分の割合になる」, 「建物の床面積の割合では決まらない」.
The two cards have clearly different texts; the texts are NOT identical.
Under the cards, one wide dark navy band with large white text 「まず、専有部分を何個持つ人かを見る」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 所, 権, 物, 規, 証; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly four item lines and the right card has exactly two item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T01-4：敷地権が変わったとき（どの登記を、いつまでに）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`敷地権_図解4_敷地権が変わるとき.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権が変わったとき」
「どの登記を、いつまでに」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条／不動産登記規則 第124条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「できごと」, 「申請する登記」, 「ポイント」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「敷地権が消滅した」 | 「建物の表題部の変更の登記」 | 「消滅した日から1月以内（法51条1項）」
Row 2: 「賃借権の敷地権について、賃借権の抹消の登記がされた」 | 「建物の表題部の変更の登記」 | 「抹消の登記がされた日から1月以内」
Row 3: 「敷地が分筆で2筆になった」 | 「建物の表題部の変更の登記」 | 「規約敷地とみなされても必要（区分所有法5条2項）」
Row 4: 「敷地権でなくなった」 | 「建物の表題部の変更の登記」 | 「土地の権利部の敷地権である旨の登記が抹消される（規則124条1項）」
Row 5: 「土地の地目の変更」 | 「土地の地目の変更の登記だけ」 | 「敷地権の抹消は要らない（分離処分ではない）」
Highlighting: the string 「土地の権利部」 inside the column-3 cell of row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「敷地権である旨の登記は、土地の権利部にある」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 所, 権, 物, 登, 規, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
