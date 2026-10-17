# 論点別 復習用 図解インフォグラフィック プロンプト（T09 民法（登記と第三者・共有・相続・意思表示・相隣関係）・5枚）

この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 |
|---|---|---|---|---|
| 図解T09-1 | 善意・無過失・登記（第三者の要件を仕分ける） | 早見表型 | 1080×2000 | 民法_図解1_登記と第三者.png |
| 図解T09-2 | 共有物の分割と相続（場面別の結論） | 早見表型 | 1080×2700 | 民法_図解2_共有と相続.png |
| 図解T09-3 | 意思表示のルール（公示・未成年者・錯誤） | 早見表型 | 1080×1700 | 民法_図解3_意思表示.png |
| 図解T09-4 | 配偶者居住権（成立・期間・譲渡） | 早見表型 | 1080×2400 | 民法_図解4_配偶者居住権.png |
| 図解T09-5 | 相隣関係の承諾（ライフラインと共有の障壁） | 対比カード型（2列） | 1080×1900 | 民法_図解5_相隣関係.png |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解T09-1：善意・無過失・登記（第三者の要件を仕分ける）

- 型：早見表型　／　サイズ：1080×2000　／　保存名：`民法_図解1_登記と第三者.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「善意・無過失・登記」
「第三者の要件を仕分ける」
Subtitle (smaller, centered, 1 line):
「民法 第94条・第177条・第186条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「結論」, 「条文」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「通謀虚偽表示の第三者」 | 「善意であればよい。無過失も登記も要らない」 | 「民法94条2項」
Row 2: 「占有者の善意・無過失（時効取得）」 | 「善意は推定される。無過失は推定されず、主張する側が立証する」 | 「民法186条1項」
Row 3: 「契約解除のあとに現れた第三者」 | 「元の売主と第三者は、先に登記を備えた方が優先する」 | 「民法177条」
Row 4: 「未登記のまま建物を譲渡した人」 | 「収去・明渡しの請求の相手にならない。所有権を失っているから」 | 「相手は現に建物を所有する人」
Highlighting: the string 「無過失も登記も要らない」 inside the column-2 cell of row 1 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「虚偽表示の第三者は、善意だけでよい」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 占, 売, 建, 張, 所, 権, 渡, 無, 物; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T09-2：共有物の分割と相続（場面別の結論）

- 型：早見表型　／　サイズ：1080×2700　／　保存名：`民法_図解2_共有と相続.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「共有物の分割と相続」
「場面別の結論」
Subtitle (smaller, centered, 1 line):
「民法 第256条・第258条の2」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 7 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「結論」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「共有物の分割の請求」 | 「いつでもできる。ただし、5年以内の分割しない契約ができる」 | 「民法256条1項」
Row 2: 「分割しない契約の更新」 | 「できる。更新の時から5年以内」 | 「民法256条2項」
Row 3: 「相続財産の共有」 | 「遺産分割をすべき場面では、共有物分割を請求できない」 | 「民法258条の2第1項」
Row 4: 「相続開始から10年を経過」 | 「共有物分割ができるようになる」 | 「民法258条の2第2項」
Row 5: 「相続人が持分を第三者に譲渡した」 | 「第三者との共有は、遺産分割ではなく共有物分割で解消する」 | 「判例」
Row 6: 「預貯金債権」 | 「当然には分割されず、遺産分割の対象になる」 | 「判例」
Row 7: 「慰謝料請求権」 | 「生前に請求の意思を示さなくても、相続される」 | 「判例」
Highlighting: the string 「できる」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「分割しない契約は、更新できる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 債, 対, 当, 権, 渡, 物, 解, 請, 譲, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 7 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T09-3：意思表示のルール（公示・未成年者・錯誤）

- 型：早見表型　／　サイズ：1080×1700　／　保存名：`民法_図解3_意思表示.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「意思表示のルール」
「公示・未成年者・錯誤」
Subtitle (smaller, centered, 1 line):
「民法 第95条・第98条・第98条の2」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「場面」, 「結論」, 「条文」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「公示による意思表示」 | 「最後に官報に掲載した日などから2週間で到達したものとみなす。ただし、相手の所在を知らないことに表意者の過失があれば、効力は生じない」 | 「民法98条」
Row 2: 「未成年者に対する意思表示」 | 「原則は主張できない。法定代理人が知った後は、主張できる」 | 「民法98条の2」
Row 3: 「事情についての錯誤」 | 「その事情が法律行為の基礎とされていることが表示されていたときに限り、取り消せる」 | 「民法95条1項2号・2項」
Highlighting: the string 「法定代理人が知った後は、主張できる」 inside the column-2 cell of row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「未成年者への意思表示は、親権者が知れば主張できる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 効, 号, 対, 張, 所, 権, 過, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T09-4：配偶者居住権（成立・期間・譲渡）

- 型：早見表型　／　サイズ：1080×2400　／　保存名：`民法_図解4_配偶者居住権.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「配偶者居住権」
「成立・期間・譲渡」
Subtitle (smaller, centered, 1 line):
「民法 第1028条から第1032条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.
Header row (dark navy cells with white text): 「項目」, 「内容」, 「条文」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「成立しないとき」 | 「亡くなった人が、建物を配偶者以外の者と共有していたとき」 | 「民法1028条1項ただし書」
Row 2: 「配偶者との共有」 | 「成立する。配偶者に遺贈できる」 | 「民法1028条1項」
Row 3: 「存続期間」 | 「原則は配偶者の終身。別の定めがあれば、その期間。更新はできない」 | 「民法1030条」
Row 4: 「所有者の義務」 | 「配偶者居住権の設定の登記を備えさせる義務を負う」 | 「民法1031条1項」
Row 5: 「譲渡」 | 「所有者の承諾があっても、譲渡できない」 | 「民法1032条2項」
Row 6: 「所有者の承諾があればできること」 | 「改築・増築、第三者に使用・収益させること」 | 「民法1032条3項」
Highlighting: the string 「譲渡できない」 inside the column-2 cell of row 5 has a pale yellow highlighter marker. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「承諾があっても、配偶者居住権は譲渡できない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 承, 権, 渡, 物, 登, 記, 諾, 譲; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解T09-5：相隣関係の承諾（ライフラインと共有の障壁）

- 型：対比カード型（2列）　／　サイズ：1080×1900　／　保存名：`民法_図解5_相隣関係.png`

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「相隣関係の承諾」
「ライフラインと共有の障壁」
Subtitle (smaller, centered, 1 line):
「民法 第213条の2・第231条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「ライフライン」, heading 「承諾は要らない」 (the string 「承諾は要らない」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「電気・ガス・水道水の供給を受けるため、他の土地に設備を設置できる」, 「目的・場所・方法を通知すれば足りる」, 「場所と方法は、他の土地の損害が最も少ないものを選ぶ」, 「損害には償金を支払う（民法213条の2）」.
Right card: small tag 「共有の障壁」, heading 「高さを増すのに承諾は要らない」 (the string 「高さを増すのに承諾は要らない」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「相隣者の一人は、共有の障壁の高さを増せる（民法231条1項）」, 「他の相隣者の承諾は、条文上の要件ではない」, 「塀が耐えられないときは、増す人が補強か造り直しをする」, 「増した部分は、工事をした人だけの物になる」.
The two cards have clearly different texts; the texts are NOT identical.
Under the cards, one wide dark navy band with large white text 「どちらも、承諾は要らない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 所, 承, 物, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly four item lines and the right card has exactly four item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
