# 論点別 復習用 図解インフォグラフィック プロンプト（T08 筆界特定・法定相続情報・保存期間・証明書・4枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T08-1 | 帳簿と書類の保存期間（早見表） | 早見表型 | 1080×2400 | 手続と書類_図解1_保存期間.png |
| 図解T08-2 | 登記事項証明書と登記事項要約書（請求と作り方の違い） | 早見表型 | 1080×2400 | 手続と書類_図解2_証明書と要約書.png |
| 図解T08-3 | 筆界特定の申請（管轄・申請書・却下） | 早見表型 | 1080×2700 | 手続と書類_図解3_筆界特定の申請.png |
| 図解T08-4 | 法定相続情報の申出と利用（申出先・住所・番号） | 早見表型 | 1080×2200 | 手続と書類_図解4_法定相続情報.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T08-1：帳簿と書類の保存期間（早見表）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`手続と書類_図解1_保存期間.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「帳簿と書類の保存期間」
「早見表」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第28条・第28条の2」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「書類」, 「保存期間」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「不正登記防止申出書類つづり込み帳」 | 「作成の年の翌年から3年」 | 「規則28条の2第4号」
Row 2: 「法定相続情報一覧図つづり込み帳」 | 「作成の年の翌年から5年」 | 「規則28条の2第6号」
Row 3: 「職権表示登記等書類つづり込み帳の書類」 | 「立件の日から30年」 | 「規則28条12号」
Row 4: 「事件簿（職権表示登記等）」 | 「5年」 | 「規則28条11号」
Row 5: 「表示に関する登記の申請情報と添付情報」 | 「受付の日から30年」 | 「規則28条9号」
Row 6: 「書面の地積測量図を、電磁的記録に記録して保存したとき」 | 「電磁的記録に記録して保存した日から30年」 | 「規則28条9号かっこ書」
Highlighting: the string 「30年」 inside the column-2 cell of row 3; the string 「5年」 inside the column-2 cell of row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「事件簿は5年、つづり込み帳の書類は30年」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 号, 地, 権, 登, 規, 記, 請, 録, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T08-2：登記事項証明書と登記事項要約書（請求と作り方の違い）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`手続と書類_図解2_証明書と要約書.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with two columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「登記事項証明書と登記事項要約書」
「請求と作り方の違い」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第194条・第197条・第198条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 2 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「項目」, 「扱い」.
Data rows, one per line, in this order (column 1 | column 2):
Row 1: 「請求の方法（原則）」 | 「請求情報を記載した書面を、登記所に提出（規則194条1項）」
Row 2: 「入出力装置・電子情報処理組織による請求」 | 「できるのは、登記事項証明書だけ。登記事項要約書はできない」
Row 3: 「入出力装置で請求した登記事項証明書」 | 「送付による交付は除かれる（規則194条2項）」
Row 4: 「登記事項証明書の認証文と職印」 | 「認証文を付し、職氏名を記載して職印を押す（規則197条1項）」
Row 5: 「登記事項要約書の認証文と職印」 | 「求められていない（規則198条1項）」
Row 6: 「登記事項要約書の用紙」 | 「別段の申出がなければ、一の用紙に二以上の不動産を記載できる（規則198条3項）」
Highlighting: the string 「登記事項要約書はできない」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「要約書は、書面で請求し、認証文も職印もない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 所, 押, 登, 規, 記, 証, 認, 請, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 2 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T08-3：筆界特定の申請（管轄・申請書・却下）

- 型：早見表型　／　サイズ：1080×2700　／　保存名：`手続と書類_図解3_筆界特定の申請.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「筆界特定の申請」
「管轄・申請書・却下」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第124条・第132条／不動産登記規則 第207条・第211条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 7 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「事務を行う法務局」 | 「対象土地の所在地を管轄する法務局または地方法務局」 | 「法124条1項」
Row 2: 「管轄がまたがる」 | 「事務を行う法務局が指定されるまでは、いずれか一つに申請できる」 | 「法124条2項・6条3項」
Row 3: 「申請書の署名・記名押印」 | 「要らない。代理人による申請は、委任状に申請人が記名する」 | 「規則211条3項」
Row 4: 「対象土地の状況（工作物・囲障・境界標など）」 | 「必要的な事項。書かなければ却下される。補正できれば却下されない」 | 「規則207条2項7号・法132条1項3号」
Row 5: 「手数料が足りない」 | 「すぐには却下しない。納付すべき額を通知して、補正の機会を与える」 | 「法132条1項8号」
Row 6: 「確定判決があるかどうか不明」 | 「判決がないものとして手続を進める。却下されるのは、判決が現に存在するとき」 | 「法132条1項6号」
Row 7: 「表題登記のない土地」 | 「地番は示せない。何番地先などの表示で、特定できる」 | 「規則207条2項6号」
Highlighting: the string 「要らない」 inside the column-2 cell of row 3 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「筆界特定の申請書には、署名も記名押印も要らない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 対, 所, 押, 物, 番, 登, 規; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 7 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T08-4：法定相続情報の申出と利用（申出先・住所・番号）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`手続と書類_図解4_法定相続情報.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「法定相続情報の申出と利用」
「申出先・住所・番号」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第37条の3・第181条・第247条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「申出ができる登記所」 | 「被相続人の本籍地または最後の住所地、申出人の住所地、被相続人名義の不動産の所在地を管轄する登記所」 | 「規則247条1項」
Row 2: 「申出人の本籍地を管轄する登記所」 | 「含まれない。含まれるのは被相続人の本籍地」 | 「規則247条1項」
Row 3: 「一覧図に相続人の住所を記載」 | 「記載は任意。記載したら、住所を証する書面を添付する」 | 「規則247条4項」
Row 4: 「法定相続情報番号の提供」 | 「相続があったことを証する情報の提供に代えられる。登記官が確認できるときに限る」 | 「規則37条の3第1項」
Row 5: 「書面申請の登記完了証」 | 「申請情報として記録されるのは、登記の目的だけ」 | 「規則181条2項7号」
Highlighting: the string 「含まれない」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「申出人の本籍地は含まれない。被相続人の本籍地は含まれる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 所, 番, 登, 規, 記, 証, 認; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
