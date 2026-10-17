# 論点別 復習用 図解インフォグラフィック プロンプト（T03 区分建物の成立・合併・合体・分割・建物の表示・6枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T03-1 | 1個の建物か、別の建物か（独立性と主従で決まる） | 対比カード型（2列） | 1080×1900 | 建物の登記_図解1_建物かどうかの見分け.png |
| 図解T03-2 | 非区分建物が区分建物になったとき（登記の流れ） | ステップ型 | 1080×2200 | 建物の登記_図解2_区分建物になったとき.png |
| 図解T03-3 | 区分合併と附属合併（できない場合を押さえる） | 対比カード型（2列） | 1080×2200 | 建物の登記_図解3_合併の種類.png |
| 図解T03-4 | 一の申請情報にできる組合せ（建物の登記） | 早見表型 | 1080×2000 | 建物の登記_図解4_一の申請情報の組合せ.png |
| 図解T03-5 | 合体と分割の書類・識別情報（場面別の扱い） | 早見表型 | 1080×2400 | 建物の登記_図解5_合体と分割の書類.png |
| 図解T03-6 | 建物の表示の書き方（冠記と建物の種類） | 早見表型 | 1080×2000 | 建物の登記_図解6_表示の書き方.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T03-1：1個の建物か、別の建物か（独立性と主従で決まる）

- 型：対比カード型（2列）　／　サイズ：1080×1900　／　保存名：`建物の登記_図解1_建物かどうかの見分け.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「1個の建物か、別の建物か」
「独立性と主従で決まる」
Subtitle (smaller, centered, 1 line):
「区分所有法 第1条／不動産登記法 第2条23号」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「区分所有の対象になるか」, heading 「ガラスドアで仕切られた2棟」 (the string 「ガラスドアで仕切られた2棟」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「地下通路で2棟をつなぎ、行き来できる」, 「全体が1棟の建物になる」, 「強化ガラスのドアも、壁と同じ障壁とみなす」, 「甲建物と乙建物は、区分所有権の目的になる」.
Right card: small tag 「別々の所有者の物置」, heading 「物置だけでは1個の建物にならない」 (the string 「物置だけでは1個の建物にならない」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「基礎工事があれば、土地への定着性は認められる」, 「物置は、主である建物の効用を助けるもの」, 「居宅と一体の附属建物としてだけ扱われる」, 「居宅と所有者が違えば、物置だけで登記できない」.
The two cards have clearly different texts; the texts are NOT identical.
Under the cards, one wide dark navy band with large white text 「独立した建物か、主である建物に付くものかを見分ける」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 号, 地, 対, 建, 所, 権, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly four item lines and the right card has exactly four item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T03-2：非区分建物が区分建物になったとき（登記の流れ）

- 型：ステップ型　／　サイズ：1080×2200　／　保存名：`建物の登記_図解2_区分建物になったとき.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical step poster with three step cards and one side note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「非区分建物が区分建物になったとき」
「登記の流れ」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第48条・第52条／不動産登記規則 第140条」
--- STEPS ---
Layout: three step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1, 2, 3 in order), one bold heading line, and one body line.
STEP 1: heading 「非区分建物に接続して、区分建物を新築」, body 「既存の建物と新築の建物が一棟の建物になり、既存の建物は区分建物になる」.
STEP 2 (the card has a pale yellow highlighter marker on its heading): heading 「2つの登記を併せて申請する」, body 「新築した区分建物の表題登記と、既存の建物の表題部の変更の登記（法48条3項・52条1項）」.
STEP 3: heading 「登記記録は新しく作る」, body 「その建物に新たに登記記録を作成し、従前の登記記録は閉鎖する（規則140条1項・3項）」.
--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---
Heading (bold): 「代位でできる」
Body lines, each with a small dark navy dot at its left end (NO number on the dots):
「新築した区分建物の所有者は、既存の建物の所有者に代わって申請できる（法48条4項）」
「既存の建物の所有者は、新築した区分建物の所有者に代わって申請できる（法52条2項）」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 建, 所, 物, 登, 規, 記, 請, 録, 閉; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly three step cards numbered 1 to 3 in order, followed by exactly one side note card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T03-3：区分合併と附属合併（できない場合を押さえる）

- 型：対比カード型（2列）　／　サイズ：1080×2200　／　保存名：`建物の登記_図解3_合併の種類.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「区分合併と附属合併」
「できない場合を押さえる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条1項3号／不動産登記事務取扱手続準則 第86条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「区分合併」, heading 「できない場合」 (the string 「できない場合」 has a pale yellow highlighter marker), and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「区分された建物が、互いに接続していないとき（準則86条）」, 「接続していることが、区分合併の条件」.
Right card: small tag 「附属合併」, heading 「できない場合」 (the string 「できない場合」 has a pale yellow highlighter marker), and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「合併しようとする建物が、主たる建物と附属建物の関係にないとき（準則86条）」, 「主従の関係があることが、附属合併の条件」.
The two cards have clearly different texts; the texts are NOT identical.
--- NOTE CARD (below, a wide card with a dashed dark navy outline and a small dark navy tag 「補足」) ---
Heading (bold): 「接続していても、区分合併に限られない」
Body lines, each with a small dark navy dot at its left end (NO number on the dots):
「主従の関係があれば、附属合併もできる」
「敷地権の登記がある建物も、敷地権の登記がない建物の附属建物とする合併ができる（法56条5号に当たらない）」
Under the note card, one wide dark navy band with large white text 「接続していても、区分合併とは限らない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 当, 押, 権, 物, 登, 記, 附; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly two item lines and the right card has exactly two item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T03-4：一の申請情報にできる組合せ（建物の登記）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`建物の登記_図解4_一の申請情報の組合せ.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「一の申請情報にできる組合せ」
「建物の登記」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第35条／不動産登記法 第49条／不動産登記令 第5条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「組合せ」, 「一の申請情報」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「建物の区分と、接続する区分建物への合併」 | 「できる」 | 「規則35条5号」
Row 2: 「建物の分割と、建物の合併」 | 「できる」 | 「規則35条2号・3号」
Row 3: 「建物の分割と、合体による登記等」 | 「まとめる規定がない。別々に申請」 | 「規則35条に列挙がない」
Row 4: 「表題登記のない建物と、所有権の登記がある建物の合体」 | 「所有権の登記と、一の申請情報でしなければならない」 | 「法49条1項後段・令5条1項後段」
Highlighting: the string 「まとめる規定がない」 inside the column-2 cell of row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「一の申請情報にできる組合せは、規則35条に列挙されている」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 所, 権, 物, 登, 規, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T03-5：合体と分割の書類・識別情報（場面別の扱い）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`建物の登記_図解5_合体と分割の書類.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with two columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「合体と分割の書類・識別情報」
「場面別の扱い」
Subtitle (smaller, centered, 1 line):
「不動産登記令 第8条／不動産登記法 第21条・第23条・第54条／不動産登記規則 第128条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 2 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「扱い」.
Data rows, one per line, in this order (column 1 | column 2):
Row 1: 「合体前の建物の所有権の登記名義人が同一」 | 「いずれか1個の建物の登記識別情報を提供すれば足りる（令8条2項2号）」
Row 2: 「分割で、職権により所有権の登記がされた乙建物」 | 「登記識別情報はない（法21条）。分割前の甲建物のものは提供できない」
Row 3: 「提供できる登記識別情報がない」 | 「事前通知の制度を利用する（法23条1項）」
Row 4: 「所有権の登記がある建物と、表題登記のみの建物が増築で合体」 | 「所有権を証する情報は、増築部分のものだけで足りる」
Row 5: 「担保権のある建物を分割する」 | 「共同担保目録を作る（規則128条1項・102条1項）」
Row 6: 「建物の分割の登記」 | 「義務ではない。申請できるのは、表題部所有者か所有権の登記名義人だけ（法54条1項）」
Highlighting: the string 「登記識別情報はない」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「分割の登記は、所有者が希望したときに申請する」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 号, 建, 所, 権, 物, 登, 規, 記, 証; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 2 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T03-6：建物の表示の書き方（冠記と建物の種類）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`建物の登記_図解6_表示の書き方.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with two columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「建物の表示の書き方」
「冠記と建物の種類」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第113条・第162条／不動産登記事務取扱手続準則 第88条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 2 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「書き方」.
Data rows, one per line, in this order (column 1 | column 2):
Row 1: 「先取特権の保存の登記のあとで、新築の表題登記。床面積が設計書と違う」 | 「欄の番号の冠記は付けない。新築による表題登記だから（規則162条1項）」
Row 2: 「建物が他の都道府県にまたがる」 | 「他の都道府県名だけを冠記する。管轄の県名は付けない（準則88条1項）」
Row 3: 「幼稚園の建物」 | 「種類は校舎（学校教育法の学校の建物）」
Row 4: 「料亭・割烹の建物」 | 「種類は料理店。店舗ではない（規則113条1項）」
Highlighting: the string 「冠記は付けない」 inside the column-2 cell of row 1 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「幼稚園は校舎、料亭は料理店」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 号, 建, 権, 物, 番, 登, 規, 記, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 2 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
