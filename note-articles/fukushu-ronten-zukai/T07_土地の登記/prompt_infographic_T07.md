# 論点別 復習用 図解インフォグラフィック プロンプト（T07 土地の登記（分筆・地番・区画整理・登録免許税）・5枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T07-1 | 分筆の登記は、だれがするか（申請と職権） | 早見表型 | 1080×2200 | 土地の登記_図解1_分筆の申請と職権.png |
| 図解T07-2 | 分筆に伴う権利の消滅（記録の方法と地番） | 早見表型 | 1080×2200 | 土地の登記_図解2_権利の消滅の記録.png |
| 図解T07-3 | 地番の定め方（場面別の扱い） | 早見表型 | 1080×2400 | 土地の登記_図解3_地番の定め方.png |
| 図解T07-4 | 土地区画整理事業の登記（分筆・嘱託・代位） | 早見表型 | 1080×2000 | 土地の登記_図解4_区画整理の登記.png |
| 図解T07-5 | 分筆の登録免許税（だれに、いくら課されるか） | 早見表型 | 1080×2400 | 土地の登記_図解5_登録免許税.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T07-1：分筆の登記は、だれがするか（申請と職権）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`土地の登記_図解1_分筆の申請と職権.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆の登記は、だれがするか」
「申請と職権」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第39条・第43条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「条文」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「分筆の申請ができる人」 | 「所有権の登記名義人（または表題部所有者）」 | 「法39条1項」
Row 2: 「一部が別の地目になった。または、地番区域（字）を異にするに至った」 | 「申請がなくても、登記官は職権で分筆しなければならない」 | 「法39条2項」
Row 3: 「地図を作成するため必要がある」 | 「所有者の異議がないときに限り、職権でできる」 | 「法39条3項」
Row 4: 「河川区域内の土地」 | 「河川管理者が嘱託できるのは、区域内となった旨の登記、その抹消、一部の場合の分筆、全部滅失、一部滅失の地積の変更など」 | 「法43条」
Row 5: 「河川区域内の土地の地積の更正」 | 「河川管理者に嘱託する権限はない。所有者が申請する」 | 「法43条」
Highlighting: the string 「所有者の異議がないときに限り」 inside the column-2 cell of row 3 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「地図作成のための職権分筆は、異議がないときに限る」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 所, 権, 番, 登, 記, 請, 嘱; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T07-2：分筆に伴う権利の消滅（記録の方法と地番）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`土地の登記_図解2_権利の消滅の記録.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆に伴う権利の消滅」
「記録の方法と地番」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条／不動産登記規則 第104条／不動産登記事務取扱手続準則 第67条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「分筆後の甲土地について、権利を消滅させる」 | 「承諾を証する情報を提供。甲の登記記録の登記に、付記登記で消滅を記録し、抹消の記号を記録」 | 「法40条・規則104条3項」
Row 2: 「分筆後の乙土地について、権利を消滅させる」 | 「乙土地には転写しない。甲の登記記録に、乙土地について消滅した旨を付記」 | 「規則104条2項」
Row 3: 「差押え・仮差押え・仮処分の登記」 | 「消滅の承諾の対象にならない。承諾しても抹消されない」 | 「実務の取扱い」
Row 4: 「支号のない土地の分筆」 | 「原則、分筆前の地番に支号を付けて定める」 | 「準則67条1項4号」
Row 5: 「要役地の地役権を、分筆後の土地で消滅させる」 | 「例外として、支号を用いない地番を存することができる。承役地ではない」 | 「準則67条1項5号・規則104条6項」
Highlighting: the string 「乙土地には転写しない」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「乙土地には転写せず、甲の記録に付記する」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 対, 承, 押, 権, 番, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T07-3：地番の定め方（場面別の扱い）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`土地の登記_図解3_地番の定め方.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「地番の定め方」
「場面別の扱い」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第67条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「条文」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「土地の表題登記」 | 「地番区域内の最終の地番に続けて定める。最終が300番3なら、301番」 | 「準則67条1項3号」
Row 2: 「閉鎖された土地の地番」 | 「特別の事情がなければ、再使用しない」 | 「準則67条1項2号」
Row 3: 「同一の地番が重複」 | 「登記記録を閉鎖せず、登記官が地番を変更する」 | 「準則67条3項」
Row 4: 「合筆」 | 「原則、合筆前の首位の地番。特別の事情があれば、適宜の地番も定められる」 | 「準則67条1項6号・7号」
Row 5: 「地番が著しく錯雑」 | 「必要があると認めるとき、登記官は地番を変更できる」 | 「準則67条4項」
Row 6: 「土地区画整理事業を施行した地域」 | 「ブロック（街区）地番を付して差し支えない。義務ではない」 | 「準則67条1項8号」
Highlighting: the string 「登記記録を閉鎖せず」 inside the column-2 cell of row 3 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「地番の重複は、閉鎖ではなく変更で解消する」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 番, 登, 解, 記, 認, 録, 閉, 鎖; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T07-4：土地区画整理事業の登記（分筆・嘱託・代位）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`土地の登記_図解4_区画整理の登記.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「土地区画整理事業の登記」
「分筆・嘱託・代位」
Subtitle (smaller, centered, 1 line):
「土地区画整理法 第82条／土地区画整理登記規則」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「仮換地の指定を受けた従前地の分筆」 | 「工事前の実測図に基づく地積測量図が添付されれば、申請を受理できる」 | 「先例」
Row 2: 「1筆の従前地に、数個の換地が定められた」 | 「従前地の分筆の嘱託は要らない。換地処分の登記で、換地ごとの登記記録が整う」 | 「土地区画整理登記規則8条1項・3項」
Row 3: 「施行者の代位」 | 「事業のために必要があるとき、所有者に代わって分筆・合筆の登記を申請できる」 | 「土地区画整理法82条1項」
Row 4: 「施行者の代位による表題部の変更の登記」 | 「登記の目的や原因が同一でなくても、一の申請情報でできる」 | 「土地区画整理登記規則1条」
Highlighting: the string 「分筆の嘱託は要らない」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「区画整理の区域には、通常と違う特例がある」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 地, 所, 登, 規, 記, 請, 違, 録, 嘱; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T07-5：分筆の登録免許税（だれに、いくら課されるか）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`土地の登記_図解5_登録免許税.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with two columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆の登録免許税」
「だれに、いくら課されるか」
Subtitle (smaller, centered, 1 line):
「登録免許税法 別表第一の一（十三）イ／国税通則法 第119条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 2 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「税」.
Data rows, one per line, in this order (column 1 | column 2):
Row 1: 「所有権の登記がある土地の分筆」 | 「分筆後の土地1個につき1000円」
Row 2: 「だれに課されるか」 | 「登記を受ける申請人である土地の所有者。賃借権が敷地権になっている借地人には課されない」
Row 3: 「表題部所有者が申請する分筆（所有権の登記がない）」 | 「課されない」
Row 4: 「一部地目変更の登記」 | 「課税の対象ではない」
Row 5: 「税額に100円未満の端数」 | 「切り捨てる（国税通則法119条1項）」
Row 6: 「課税標準の端数」 | 「1000円未満を切り捨てる。税額の端数とは別のルール」
Highlighting: the string 「100円未満」 inside the column-2 cell of row 5 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「税額の端数は100円未満、課税標準の端数は1000円未満」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 対, 所, 権, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 2 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
