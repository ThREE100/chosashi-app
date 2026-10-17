# 論点別 復習用 図解インフォグラフィック プロンプト（T02 共用部分・団地共用部分の登記・3枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T02-1 | 共用部分である旨の登記（申請人・添付・効果） | 早見表型 | 1080×2400 | 共用部分_図解1_共用部分の登記のしくみ.png |
| 図解T02-2 | 共用部分に関する登記の期限（数え始める日が違う） | 早見表型 | 1080×2000 | 共用部分_図解2_期限の起算日.png |
| 図解T02-3 | 団地共用部分（共有の範囲と申請情報） | 対比カード型（2列） | 1080×2200 | 共用部分_図解3_団地共用部分.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T02-1：共用部分である旨の登記（申請人・添付・効果）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`共用部分_図解1_共用部分の登記のしくみ.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with two columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「共用部分である旨の登記」
「申請人・添付・効果」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第58条／不動産登記令 別表18項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 2 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「項目」, 「内容」.
Data rows, one per line, in this order (column 1 | column 2):
Row 1: 「申請できる人」 | 「建物の表題部所有者か、所有権の登記名義人だけ（法58条2項）」
Row 2: 「申請の義務」 | 「ない。第三者に対抗するための登記（区分所有法4条2項）」
Row 3: 「添付情報」 | 「規約を設定したことを証する情報など。建物の所有者を証する情報は要らない（令別表18項）」
Row 4: 「新築の区分建物の表題登記の一括申請」 | 「同時には共用部分にできない。表題登記のあとで申請する」
Row 5: 「登記をしたあと」 | 「表題部所有者や権利に関する登記が、職権で抹消される（法58条4項）」
Row 6: 「所有権以外の権利の登記があるとき」 | 「その登記名義人の承諾が必要（法58条3項）」
Highlighting: the string 「建物の所有者を証する情報は要らない」 inside the column-2 cell of row 6 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「申請人は、登記記録に現れている所有者だけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 対, 建, 所, 承, 抗, 権, 物, 登, 規; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 2 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T02-2：共用部分に関する登記の期限（数え始める日が違う）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`共用部分_図解2_期限の起算日.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「共用部分に関する登記の期限」
「数え始める日が違う」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条・第58条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「起算日」, 「条文」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「規約を廃止した（廃止の時の所有者）」 | 「廃止の日から1月以内に、表題登記」 | 「法58条6項」
Row 2: 「規約の廃止のあとに所有権を取得した」 | 「所有権の取得の日から1月以内」 | 「法58条7項」
Row 3: 「共用部分である旨の登記がある建物で、変更のあとに所有権を取得した」 | 「所有権の取得の日から1月以内」 | 「法51条4項」
Row 4: 「変更があったあとに、共用部分である旨の登記がされた」 | 「共用部分である旨の登記がされた日から1月以内」 | 「法51条3項」
Highlighting: the string 「所有権の取得の日」 inside the column-2 cell of row 2; the string 「所有権の取得の日」 inside the column-2 cell of row 3 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「どれも1月以内。数え始める日が、場面ごとに違う」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 権, 物, 登, 規, 記, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T02-3：団地共用部分（共有の範囲と申請情報）

- 型：対比カード型（2列）　／　サイズ：1080×2200　／　保存名：`共用部分_図解3_団地共用部分.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「団地共用部分」
「共有の範囲と申請情報」
Subtitle (smaller, centered, 1 line):
「区分所有法 第67条／不動産登記令 別表19項／不動産登記法 第54条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「だれの共有か」, heading 「団地建物所有者全員」 (the string 「団地建物所有者全員」 has a pale yellow highlighter marker), and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「一部共用という扱いは、ない（区分所有法67条3項）」, 「特定の棟の所有者だけの共有にはできない」.
Right card: small tag 「登記の申請」, heading 「区分建物のときの申請情報」 (the string 「区分建物のときの申請情報」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「家屋番号ではない」, 「一棟の建物の所在と地番を提供（令別表19項ロ）」, 「一棟の建物の構造と床面積、または名称を提供」, 「承諾が得られないときは、承諾に代わる裁判があったことを証する情報を提供」.
The two cards have clearly different texts; the texts are NOT identical.
--- NOTE CARD (below, a wide card with a dashed dark navy outline and a small dark navy tag 「補足」) ---
Heading (bold): 「建物の区分の登記」
Body lines, each with a small dark navy dot at its left end (NO number on the dots):
「団地共用部分である旨の登記がある建物でも、建物の区分の登記は申請できる。申請できるのは所有者に限られる（法54条2項）」
Under the note card, one wide dark navy band with large white text 「団地共用部分にも、建物の区分の登記はできる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 建, 所, 承, 物, 番, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly two item lines and the right card has exactly four item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
