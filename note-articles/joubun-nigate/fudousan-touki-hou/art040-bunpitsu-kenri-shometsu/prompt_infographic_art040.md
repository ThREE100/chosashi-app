# 第40条　図解インフォグラフィック プロンプト（6枚）

条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第40条（分筆に伴う権利の消滅の登記）の記事に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 第40条を5つの部品で読む | カードポスター型（俯瞰） | 1080×2300 | 図解1_第40条を5つの部品で読む.png | 条文の原文とひとことでの直後 |
| 図解2 | だれの承諾の情報が要る？ | カードポスター型 | 1080×2300 | 図解2_だれの承諾の情報が要る.png | 「部品3：だれが承諾するか」の節の終わり |
| 図解3 | 分筆で抵当権はどうなる（承諾の有無と、消える土地） | 対比表型（3列） | 1080×1900 | 図解3_分筆で抵当権はどうなる.png | 「部品4：何が登記されるか」の節の終わり |
| 図解4 | 地役権が付いた土地の分筆（要役地と承役地） | 対比表型（2列） | 1080×1800 | 図解4_地役権が付いた土地の分筆.png | 「部品5：地役権の特則」の節の終わり |
| 図解5 | 分筆の登記を錯誤で戻せるか | 対比表型（2列） | 1080×1800 | 図解5_分筆の登記を錯誤で戻せるか.png | 「承諾で権利を消したあとは、錯誤で戻せるか」の節の終わり |
| 図解6 | 承諾の情報は要る？の判定フロー | フローチャート型 | 1080×2600 | 図解6_承諾の情報は要るかの判定フロー.png | 「肢を読むときの確認の順番」の節の終わり |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：第40条を5つの部品で読む

- 型：カードポスター型（俯瞰）　／　サイズ：1080×2300　／　保存名：`図解1_第40条を5つの部品で読む.png`
- 記事の挿入位置：条文の原文とひとことでの直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆に伴う権利の消滅の登記」
「条文を5つの部品で読む」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「どんなとき？」
Illustration: A land plot icon split by a boundary line into two plots, with a registry ledger card beside it labeled 「所有権以外の権利の登記」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「権利の登記がある土地の分筆」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「何を添える？」
Illustration: Two document sheets clipped together: the front sheet labeled 「分筆の申請情報」 and the back sheet labeled 「承諾した情報」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「申請と併せて提供」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「だれが承諾する？」
Illustration: A person pictogram with the name tag 「権利の登記名義人」, and behind it a smaller person pictogram with the name tag 「第三者」 and the small note 「その権利を目的とする権利があるとき」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「権利者と第三者」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「何が登記される？」
Illustration: A registry ledger page with one stamped line labeled 「消滅した旨」 and a small land plot tag 「承諾に係る土地」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「消滅した旨を登記」
--- CARD 5 ---
Badge: a filled dark navy circle containing the number 5 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「地役権は？」
Illustration: Two land plot icons side by side with dark navy tags 「要役地」 and 「承役地」, and a small document sheet between them labeled 「扱いが違う」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「規則に別の定め」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 所, 承, 権, 登, 規, 記, 請, 諾, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解2：だれの承諾の情報が要る？

- 型：カードポスター型　／　サイズ：1080×2300　／　保存名：`図解2_だれの承諾の情報が要る.png`
- 記事の挿入位置：「部品3：だれが承諾するか」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「だれの承諾の情報が要る？」
「第40条の承諾する人」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条・不動産登記規則 第104条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「土地の所有者」
Illustration: A person pictogram with the name tag 「土地の所有者」, drawn with a thin dotted outline to show that this person is not the one who consents.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「承諾する人ではない」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「権利の登記名義人」
Illustration: A person pictogram with the name tag 「抵当権者・地上権者など」 holding a signed paper sheet.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「この人が承諾」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「抵当証券があるとき」
Illustration: A certificate icon with two small name tags next to it: 「所持人」 and 「裏書人」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「所持人・裏書人も」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「第三者の権利があるとき」
Illustration: A small stack of two cards: the lower card labeled 「抵当権」 and the upper card labeled 「転抵当権」, with a person pictogram tagged 「転抵当権者」 beside the stack.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「第三者の承諾も」
--- CARD 5 ---
Badge: a filled dark navy circle containing the number 5 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「承諾の情報の形」
Illustration: Two sheets side by side: the left sheet labeled 「登記名義人が作成した情報」 and the right sheet, with a small gavel icon, labeled 「裁判があったことを証する情報」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「作成した情報か裁判」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 当, 所, 承, 抵, 権, 登, 規, 記, 証, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：分筆で抵当権はどうなる（承諾の有無と、消える土地）

- 型：対比表型（3列）　／　サイズ：1080×1900　／　保存名：`図解3_分筆で抵当権はどうなる.png`
- 記事の挿入位置：「部品4：何が登記されるか」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three columns (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆で抵当権はどうなる？」
「承諾の有無と、消える土地」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条・不動産登記規則 第102条・第104条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three data columns) and exactly 2 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right, with a small light-gray tag under each of the three data headers: the first cell is empty; the second header 「承諾の情報がない」 with the tag 「規則102条1項」; the third header 「乙土地について消す承諾」 with the tag 「規則104条2項」; the fourth header 「分筆後の甲土地について消す承諾」 with the tag 「規則104条3項」.
In the third header the word 「乙土地」 has a pale yellow highlighter marker, and in the fourth header the words 「甲土地」 has a pale yellow highlighter marker. These two headers are NOT identical; do not copy one into the other.
Data row 1 (row label cell, dark navy, white text: 「甲土地の記録」): second column 「抵当権が残る」; third column 「抵当権に、乙土地について消滅の付記」; fourth column 「抵当権に、消滅の付記と抹消の記号」.
Data row 2 (row label cell, dark navy, white text: 「乙土地の記録」): second column 「抵当権が転写される」; third column 「抵当権は転写しない」; fourth column 「抵当権が転写される」.
The second-column cell and the fourth-column cell of data row 2 have the same text on purpose; draw the same string in both. Every other cell has its own text exactly as given.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 対, 当, 承, 抵, 権, 無, 登, 規, 記, 諾, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 2 data rows, that every cell reads exactly as given, that the third and fourth headers differ in the highlighted words 乙土地 and 甲土地, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：地役権が付いた土地の分筆（要役地と承役地）

- 型：対比表型（2列）　／　サイズ：1080×1800　／　保存名：`図解4_地役権が付いた土地の分筆.png`
- 記事の挿入位置：「部品5：地役権の特則」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a two-column comparison poster (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「地役権が付いた土地の分筆」
「要役地と承役地で違う」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第103条・第104条」
--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---
「要役地の地役権」
--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---
「承役地の地役権」
The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere, and use no blue or red.
--- ROW 1 (row label 「どんな土地？」) ---
Left card: a land plot icon with a small arrow-free tag 「便益を受ける土地」.
Right card: a land plot icon with a small arrow-free tag 「便益を供する土地」.
--- ROW 2 (row label 「分筆のとき」) ---
Left card: a document sheet labeled 「地役権者が作成した情報を、分筆の申請と併せて提供」 and, under it, a second document sheet labeled 「土地の抵当権者など第三者の承諾の情報も併せて」.
Right card: a document sheet labeled 「地役権設定の範囲が一部のとき、範囲を申請情報に書き、範囲を証する情報を添える」.
--- ROW 3 (row label 「登記官がすること」) ---
Left card: a registry ledger icon with the string 「地役権が消滅した旨を登記（規則104条6項）」.
Right card: a registry ledger icon with the string 「地役権設定の範囲と地役権図面番号を記録（規則103条1項）」.
The left and right cards of each row have clearly different texts; the texts are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 対, 当, 承, 抵, 権, 番, 登, 規, 記, 証, 請, 諾, 違, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 2 columns and exactly 3 rows of cards, that the left and right texts of each row are different, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解5：分筆の登記を錯誤で戻せるか

- 型：対比表型（2列）　／　サイズ：1080×1800　／　保存名：`図解5_分筆の登記を錯誤で戻せるか.png`
- 記事の挿入位置：「承諾で権利を消したあとは、錯誤で戻せるか」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a two-column comparison poster (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆の登記を錯誤で戻せる？」
「分かれ目は、権利を消したか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条」
--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---
「権利が転写されただけ」
--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---
「承諾で権利を消した」
The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere, and use no blue or red.
--- ROW 1 (row label 「分筆のとき」) ---
Left card: a land plot icon split in two, with a ledger line copied into both parts, and the string 「分筆前からの抵当権が、各土地に引き継がれた」.
Right card: a land plot icon split in two, with a ledger line crossed out in one part, and the string 「承諾の情報で、抵当権を消した」.
--- ROW 2 (row label 「あとで錯誤と分かったら」) ---
Left card: a document sheet labeled 「錯誤を原因に、分筆の登記を抹消できる」.
Right card: a document sheet labeled 「分筆錯誤では、分筆の登記を抹消できない」.
--- ROW 3 (row label 「やり直すには」) ---
Left card: a small stamp icon with the string 「そのまま抹消の申請ができる」.
Right card: a small stamp icon with the string 「権利の登記を抹消し、合筆して、改めて設定する」.
At the bottom, one small light-gray tag centered across both columns: 「右の列は、先例の扱いによる整理」
The left and right cards of each row have clearly different texts; the texts are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 対, 当, 承, 抵, 権, 登, 記, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 2 columns and exactly 3 rows of cards plus the small gray tag at the bottom, that the left and right texts of each row are different, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解6：承諾の情報は要る？の判定フロー

- 型：フローチャート型　／　サイズ：1080×2600　／　保存名：`図解6_承諾の情報は要るかの判定フロー.png`
- 記事の挿入位置：「肢を読むときの確認の順番」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「承諾の情報は要る？」
「上から順に確かめる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「分筆の登記を申請する」
NODE DIAMOND 1: 「分筆後の土地について、権利を消したいか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「承諾の情報は要らない」 on the first line and 「権利は分筆後の各土地に転写される」 on the next two lines.
NODE DIAMOND 2: 「消したいのは、所有権以外の権利の登記か？」 The text is placed inside the diamond on 3 lines.
  - Arrow down to DIAMOND 3 with the BLUE label 「はい」.
  - Arrow right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 2 (red box): 「法40条の対象外」 on the first line and 「仮差押え・差押えなど」 on the second line.
NODE DIAMOND 3: 「その権利を目的とする第三者の権利の登記があるか？」 This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「ある」 and 「ない」; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.
  - Arrow down-left with the label 「ある」 to RESULT 3.
  - Arrow down-right with the label 「ない」 to RESULT 4.
NODE RESULT 3 (blue box): 「権利者と第三者の承諾の情報を」 on the first line and 「分筆の申請と併せて提供」 on the second line.
NODE RESULT 4 (blue box): 「権利者の承諾の情報を」 on the first line and 「分筆の申請と併せて提供」 on the second line.
Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings 「権利者と第三者の承諾の情報を」 and 「権利者の承諾の情報を」 are NOT identical); do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 対, 所, 承, 押, 権, 登, 記, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that DIAMOND 1 and DIAMOND 2 each show a blue 「はい」 and a red 「いいえ」, that DIAMOND 3 shows only the two navy labels 「ある」 and 「ない」, that RESULT 1 and RESULT 2 are red and RESULT 3 and RESULT 4 are blue, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
