# 論点別 復習用 図解インフォグラフィック プロンプト（T05 代位申請・申請人・通知・代理権・5枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T05-1 | 申請の代理権が消えるとき（死亡では消えず、破産では消える） | 早見表型 | 1080×2200 | 代位と通知_図解1_代理権の消滅.png |
| 図解T05-2 | 区分建物の登記の代位（だれが、だれに代わるか） | 早見表型 | 1080×2200 | 代位と通知_図解2_区分建物の代位.png |
| 図解T05-3 | 民法の代位ができるとき（できないとき） | 対比カード型（2列） | 1080×1900 | 代位と通知_図解3_民法による代位.png |
| 図解T05-4 | 更正の登記の要件と通知（持分の更正・表題部所有者の更正） | 早見表型 | 1080×2000 | 代位と通知_図解4_更正の登記.png |
| 図解T05-5 | 登記識別情報と事前通知（だれに、どう通知するか） | 早見表型 | 1080×2200 | 代位と通知_図解5_通知.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T05-1：申請の代理権が消えるとき（死亡では消えず、破産では消える）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`代位と通知_図解1_代理権の消滅.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「申請の代理権が消えるとき」
「死亡では消えず、破産では消える」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第17条／民法 第111条・第653条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「できごと」, 「資格者代理人の代理権」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「本人が死亡」 | 「消えない」 | 「法17条1号」
Row 2: 「法定代理人が死亡」 | 「消えない」 | 「法17条4号」
Row 3: 「法定代理人が後見開始の審判を受け、代理権が消滅」 | 「消えない」 | 「法17条4号」
Row 4: 「法定代理人が破産手続開始の決定を受けた」 | 「消えない」 | 「法17条4号」
Row 5: 「本人が破産手続開始の決定を受けた」 | 「消える」 | 「民法653条2号・111条2項（法17条に定めがない）」
Highlighting: the string 「消える」 inside the column-2 cell of row 5 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「死亡では消えず、本人の破産では消える」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 権, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T05-2：区分建物の登記の代位（だれが、だれに代わるか）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`代位と通知_図解2_区分建物の代位.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「区分建物の登記の代位」
「だれが、だれに代わるか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第47条・第48条・第52条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「申請する人」, 「代位・承継」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「一棟の区分建物の表題登記（一括申請）」 | 「区分建物の所有者」 | 「他の区分建物の所有者に代わって（法48条2項）」
Row 2: 「未登記のまま区分建物を譲り受けた」 | 「譲り受けた人」 | 「新築した人に代わって。その人の代位権も代位行使できる」
Row 3: 「区分建物を新築した人が、登記せずに死亡した」 | 「相続人（一般承継人）」 | 「代位ではない。被承継人を表題部所有者として申請（法47条2項）」
Row 4: 「非区分建物に接続して区分建物を新築」 | 「新築した区分建物の所有者」 | 「既存の建物の所有者に代わって、表題部の変更の登記（法48条4項）。代位原因は不動産登記法第48条第4項」
Row 5: 「同上」 | 「既存の建物の所有者」 | 「新築した区分建物の所有者に代わって、表題登記（法52条2項）」
Highlighting: the string 「代位ではない」 inside the column-3 cell of row 3 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「一般承継人は、代位ではなく、承継人として申請する」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 建, 所, 承, 権, 物, 登, 記, 請, 譲; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T05-3：民法の代位ができるとき（できないとき）

- 型：対比カード型（2列）　／　サイズ：1080×1900　／　保存名：`代位と通知_図解3_民法による代位.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「民法の代位ができるとき」
「できないとき」
Subtitle (smaller, centered, 1 line):
「民法 第423条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「代位申請できる」, heading 「自分の権利を守るのに必要」 (the string 「自分の権利を守るのに必要」 has a pale yellow highlighter marker), and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「非区分建物の一部に抵当権の設定を受けたい」, 「先に、その部分を区分建物として登記する必要がある」, 「抵当権の設定を受ける人は、所有者に代わって、建物の区分の登記を申請できる」.
Right card: small tag 「代位申請できない」, heading 「合併しなくても権利を守れる」 (the string 「合併しなくても権利を守れる」 has a pale yellow highlighter marker), and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「居宅と車庫を、別々の建物のまま売る約束」, 「それぞれの所有権移転登記を請求する権利は、合併しなくても守れる」, 「買主は、所有者に代わって、合併の登記を申請できない」.
The two cards have clearly different texts; the texts are NOT identical.
Under the cards, one wide dark navy band with large white text 「代位は、自分の登記を請求する権利を守るために必要なときだけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 売, 建, 当, 所, 抵, 権, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly three item lines and the right card has exactly three item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T05-4：更正の登記の要件と通知（持分の更正・表題部所有者の更正）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`代位と通知_図解4_更正の登記.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「更正の登記の要件と通知」
「持分の更正・表題部所有者の更正」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第33条／不動産登記令 別表2項／不動産登記規則 第183条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「要件・通知」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「表題部所有者の持分の更正」 | 「申請できるのは、その共有者。持分が変わる他の共有者全員の承諾が必要。増える人の承諾も必要」 | 「法33条3項・4項」
Row 2: 「表題部所有者の更正」 | 「新しい表題部所有者の所有を証する情報と、住所を証する情報を添付」 | 「令別表2項」
Row 3: 「完了の通知（持分の更正）」 | 「更正前の表題部所有者のうち、申請人以外の者に通知。2人以上なら1人でよい」 | 「規則183条1項1号・2項」
Row 4: 「完了の通知（表題部所有者の更正）」 | 「申請人と、更正前の表題部所有者に通知。更正前が2人以上なら1人でよい」 | 「規則183条1項1号・2項」
Highlighting: the string 「増える人の承諾も必要」 inside the column-2 cell of row 1 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「持分が増える人の承諾も、要る」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 所, 承, 登, 規, 記, 証, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T05-5：登記識別情報と事前通知（だれに、どう通知するか）

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`代位と通知_図解5_通知.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「登記識別情報と事前通知」
「だれに、どう通知するか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第21条／不動産登記規則 第62条・第70条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「登記識別情報の通知」 | 「その登記で、申請人自らが登記名義人となる場合に、その申請人へ」 | 「法21条」
Row 2: 「法定代理人が申請」 | 「通知の相手は法定代理人。本人に意思能力があるかは関係ない」 | 「規則62条1項1号」
Row 3: 「申請人でない名義人」 | 「通知されない。申請人にだけ通知される」 | 「法21条」
Row 4: 「事前通知」 | 「電子申請でも、書面を送付して行う」 | 「規則70条1項」
Row 5: 「事前通知への申出」 | 「申請書や委任状に押したものと、同一の印を押す」 | 「規則70条5項2号」
Highlighting: the string 「電子申請でも、書面を送付」 inside the column-2 cell of row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「通知されるのは、申請人だけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 押, 登, 規, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
