# 論点別 復習用 図解インフォグラフィック プロンプト（T06 申請情報・添付情報・図面・登記原因・原本還付・5枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T06-1 | 図面が要るとき、要らないとき（地図の訂正と建物の変更） | 早見表型 | 1080×2000 | 申請と添付_図解1_図面が要るとき.png |
| 図解T06-2 | 地役権図面が要るとき（範囲が一部になるかで決まる） | 早見表型 | 1080×2400 | 申請と添付_図解2_地役権図面.png |
| 図解T06-3 | 登記原因及びその日付（土地の登記での書き方） | 早見表型 | 1080×2000 | 申請と添付_図解3_登記原因の書き方.png |
| 図解T06-4 | 縮尺と図面の兼用（土地所在図・地積測量図） | 早見表型 | 1080×2700 | 申請と添付_図解4_縮尺と兼用.png |
| 図解T06-5 | 原本の還付を請求できるか（できないものを覚える） | 早見表型 | 1080×2400 | 申請と添付_図解5_原本還付.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T06-1：図面が要るとき、要らないとき（地図の訂正と建物の変更）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`申請と添付_図解1_図面が要るとき.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「図面が要るとき、要らないとき」
「地図の訂正と建物の変更」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第16条／不動産登記令 別表14項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「図面」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「地図の訂正の申出：地番の誤りだけ」 | 「土地所在図・地積測量図は要らない」 | 「規則16条5項1号」
Row 2: 「地図の訂正の申出：区画・位置・形状の誤り」 | 「土地所在図か地積測量図を提供する」 | 「規則16条5項2号」
Row 3: 「建物の表題部の変更：建物の所在する土地の地番の変更」 | 「変更後の建物図面だけ。各階平面図は要らない」 | 「令別表14項イ」
Row 4: 「建物の表題部の変更：床面積の変更」 | 「各階平面図が要る。各階の形や面積が変わるから」 | 「令別表14項ロ（1）」
Highlighting: the string 「要らない」 inside the column-2 cell of row 1 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「地番の誤りだけなら、図面は要らない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 所, 物, 番, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T06-2：地役権図面が要るとき（範囲が一部になるかで決まる）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`申請と添付_図解2_地役権図面.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「地役権図面が要るとき」
「範囲が一部になるかで決まる」
Subtitle (smaller, centered, 1 line):
「不動産登記令 別表8項・9項／不動産登記規則 第79条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「地役権図面」, 「理由」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「承役地の分筆で、範囲が分筆後の土地の一部」 | 「提供する」 | 「令別表8項」
Row 2: 「承役地の分筆で、範囲が分筆後の土地の全部」 | 「要らない」 | 「図面がなくても範囲が明らか」
Row 3: 「承役地の合筆で、範囲が合筆後の土地の一部」 | 「提供する」 | 「令別表9項」
Row 4: 「地役権のない土地と合筆」 | 「必ず一部になるので、提供する」 | 「元の土地の部分にだけ地役権がある」
Row 5: 「要役地の分筆」 | 「提供しない」 | 「地役権図面は承役地のもの。範囲は変わらない」
Row 6: 「地役権図面の縮尺」 | 「適宜の縮尺でよい」 | 「規則79条2項。地積測量図に合わせる決まりはない」
Highlighting: the string 「必ず一部になるので、提供する」 inside the column-2 cell of row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「地役権図面は、承役地の図面」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 承, 権, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T06-3：登記原因及びその日付（土地の登記での書き方）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`申請と添付_図解3_登記原因の書き方.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「登記原因及びその日付」
「土地の登記での書き方」
Subtitle (smaller, centered, 1 line):
「不動産登記令 第3条／不動産登記事務取扱手続準則 第73条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「書き方」, 「理由」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「公有水面を埋め立てた土地の表題登記」 | 「年月日公有水面埋立。日付は、竣功認可の告示の日」 | 「その日に所有権を取得する（公有水面埋立法24条1項）」
Row 2: 「未登記の国有地の払い下げを受けた土地の表題登記」 | 「登記原因及びその日付欄は、不詳」 | 「払い下げの日は、土地が生じた日ではない」
Row 3: 「地目の変更の時期が分からない（年だけ分かる）」 | 「平成20年月日不詳地目変更のように、分かる範囲まで書く」 | 「先頭に欄の番号を付ける（準則73条）」
Row 4: 「地目変更と地積更正を、一の申請情報で申請」 | 「欄ごとに書き分ける。地目変更は日付つき、地積更正は錯誤」 | 「日付を付けるのは、地目変更だけ（準則73条）」
Highlighting: the string 「竣功認可の告示の日」 inside the column-2 cell of row 1 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「埋立地の日付は、工事完了日ではなく告示の日」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 所, 権, 番, 登, 記, 認, 請, 竣; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T06-4：縮尺と図面の兼用（土地所在図・地積測量図）

- 型：早見表型　／　サイズ：1080×2700　／　保存名：`申請と添付_図解4_縮尺と兼用.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「縮尺と図面の兼用」
「土地所在図・地積測量図」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第10条・第73条・第76条・第77条／不動産登記事務取扱手続準則 第51条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 7 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「項目」, 「決まり」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「土地所在図の縮尺」 | 「近傍類似の土地の地図と同一の縮尺」 | 「規則76条2項」
Row 2: 「地図の縮尺（市街地地域）」 | 「250分の1または500分の1」 | 「規則10条2項」
Row 3: 「地図の縮尺（村落・農耕地域）」 | 「500分の1または1000分の1」 | 「規則10条2項」
Row 4: 「地図の縮尺（山林・原野地域）」 | 「1000分の1または2500分の1」 | 「規則10条2項」
Row 5: 「電子申請の地積測量図」 | 「縮尺を問わず、土地所在図を兼ねられる」 | 「準則51条2項・規則73条1項」
Row 6: 「書面の地積測量図」 | 「縮尺が土地所在図と同じなら、兼ねられる」 | 「準則51条4項」
Row 7: 「基本三角点等に基づく測量ができない特別な事情」 | 「近傍の恒久的な地物に基づく座標値。平面直角座標系の記録は不要」 | 「規則77条2項」
Highlighting: the string 「近傍類似の土地の地図と同一」 inside the column-2 cell of row 1 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「土地所在図の縮尺は、近傍類似の地図と同じ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 所, 物, 登, 規, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 7 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T06-5：原本の還付を請求できるか（できないものを覚える）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`申請と添付_図解5_原本還付.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「原本の還付を請求できるか」
「できないものを覚える」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第55条／不動産登記令 第16条・第18条・第19条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「還付」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「還付の請求のしかた」 | 「原本と相違ない旨を記載した謄本を提出する」 | 「規則55条2項」
Row 2: 「申請書に押印した人の印鑑証明書」 | 「請求できない」 | 「令16条2項」
Row 3: 「委任状に押印した人の印鑑証明書」 | 「請求できない」 | 「令18条2項」
Row 4: 「承諾書に押印した人の印鑑証明書」 | 「請求できない」 | 「令19条2項」
Row 5: 「遺産分割協議書に添付した相続人の印鑑証明書」 | 「請求できる」 | 「上の3つのどれにも当たらない」
Row 6: 「2以上の登記所に申請するために作った委任状」 | 「請求できる」 | 「その申請のためにのみ作成されたものではない」
Highlighting: the string 「請求できる」 inside the column-2 cell of row 5; the string 「請求できる」 inside the column-2 cell of row 6 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「申請書・委任状・承諾書の印鑑証明書は、返してもらえない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 当, 所, 承, 押, 登, 規, 記, 証, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
