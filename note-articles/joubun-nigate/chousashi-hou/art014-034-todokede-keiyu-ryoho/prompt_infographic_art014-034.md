# 届出先・申請先の決め方（調査士法の届出先／不動産登記法の申請先）　図解インフォグラフィック プロンプト（7枚）

条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、届出先・申請先の決め方（第1部：土地家屋調査士法の届出先、調査士会を経由する場合と両方に届け出る場合。第2部：不動産登記法の申請先、登記と筆界特定）の記事に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 届出先は、経由か、両方か（4つのパターン） | カードポスター型 | 1080×2000 | 図解1_届出先は経由か両方か.png | 「ひとことで」の直後 |
| 図解2 | まず主語を見る（個人か、法人か）の判定の流れ | フローチャート型 | 1080×1800 | 図解2_主語で分ける判定の流れ.png | 「部品1：まず、主語で分ける」の節の終わり |
| 図解3 | 調査士（個人）の手続の一覧表 | 早見表型（3列） | 1080×1900 | 図解3_個人の手続の一覧表.png | 「部品2：調査士（個人）」の節の終わり |
| 図解4 | 調査士法人の届出の一覧表 | 早見表型（4列） | 1080×2300 | 図解4_法人の届出の一覧表.png | 「部品3：調査士法人」の節の、届出の一覧のあと |
| 図解5 | 調査士法人が解散したとき、どの条文で届け出るか | フローチャート型 | 1080×1900 | 図解5_解散と合併の仕分け.png | 「解散と合併は、条文が分かれる」の節の終わり |
| 図解6 | 登記の申請と筆界特定の申請の対比表 | 対比表型（3列） | 1080×1900 | 図解6_登記と筆界特定の申請先の対比表.png | 「部品5：登記は登記所、筆界特定は法務局又は地方法務局」の節の終わり |
| 図解7 | 管轄区域にまたがるとき、どこに申請するか | フローチャート型 | 1080×2000 | 図解7_管轄にまたがるときの申請先.png | 「部品7：指定がされる前でも、そのうちの一つに申請できる」の節の終わり |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。表の行数（図解3は5行、図解4は7行、図解6は5行）と、流れ図の分岐の数も確かめてください。

## 図解1：届出先は、経由か、両方か（4つのパターン）

- 型：カードポスター型　／　サイズ：1080×2000　／　保存名：`図解1_届出先は経由か両方か.png`
- 記事の挿入位置：「ひとことで」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「届出先はどこ？」
「経由か、両方か」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法 第14条・第34条ほか」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「調査士（個人）」
Illustration: A person pictogram with the name tag 「調査士」 handing a document sheet to a small building icon labeled 「調査士会」, and from that building a solid navy arrow leading to a larger building icon labeled 「調査士会連合会」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「調査士会を経由して連合会へ」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「調査士法人」
Illustration: A building icon labeled 「調査士法人」 with two separate solid navy arrows, one to a small building icon labeled 「調査士会」 and one to a larger building icon labeled 「調査士会連合会」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「調査士会と連合会の両方へ」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「変更の登録を申請するとき」
Illustration: A person pictogram with the name tag 「調査士」 holding a small notice sheet, with one solid navy arrow to a small building icon labeled 「現に所属する調査士会」 only (no second building).
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「現に所属する調査士会だけ」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「協会の成立の届出」
Illustration: A building icon labeled 「公共嘱託登記土地家屋調査士協会」 with two separate solid navy arrows, one to a building icon labeled 「法務局又は地方法務局の長」 and one to a building icon labeled 「調査士会」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「法務局の長と調査士会へ」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 届, 所, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解2：まず主語を見る（個人か、法人か）の判定の流れ

- 型：フローチャート型　／　サイズ：1080×1800　／　保存名：`図解2_主語で分ける判定の流れ.png`
- 記事の挿入位置：「部品1：まず、主語で分ける」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「まず、主語を見る」
「届け出るのは、だれ？」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 1. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「連合会への届出の肢を読む」
NODE DIAMOND 1: 「手続をするのは、調査士か、調査士法人か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「調査士（個人）」 and 「調査士法人」; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.
  - Arrow down-left with the label 「調査士（個人）」 to RESULT 1.
  - Arrow down-right with the label 「調査士法人」 to RESULT 2.
NODE RESULT 1 (blue box): 「調査士会を経由して」 on the first line and 「連合会に届け出る」 on the second line.
NODE RESULT 2 (blue box): 「調査士会と連合会の」 on the first line and 「両方に届け出る」 on the second line.
At the very bottom, one small light-gray tag centered across both result boxes: 「どちらにも、法務局への届出は出てこない」
Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings 「調査士会を経由して」 and 「調査士会と連合会の」 are NOT identical); do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 届, 肢; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows only the two navy labels 調査士（個人） and 調査士法人 and no はい or いいえ, that both result boxes are blue and have different texts, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：調査士（個人）の手続の一覧表

- 型：早見表型（3列）　／　サイズ：1080×1900　／　保存名：`図解3_個人の手続の一覧表.png`
- 記事の挿入位置：「部品2：調査士（個人）」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference table poster with three columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「調査士（個人）の手続」
「調査士会を経由して連合会へ」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: 「手続」, 「条文」, 「経由する調査士会」.
Data row 1: first column 「登録の申請」; second column 「9条1項」; third column 「事務所を設けようとする地の調査士会」.
Data row 2: first column 「所属する調査士会の変更の登録の申請」; second column 「13条1項」; third column 「移転先の管轄区域の調査士会」.
Data row 3: first column 「登録事項に変更が生じたときの届出」; second column 「14条」; third column 「所属する調査士会」.
Data row 4: first column 「登録の取消し事由に当たるときの届出」; second column 「15条2項」; third column 「所属し、又は所属していた調査士会」.
Data row 5: first column 「心身の故障のおそれがあるときの届出」; second column 「16条2項」; third column 「所属する調査士会」.
Under the table, one wide pale-yellow banner with dark navy text: 「どれも、経由先の調査士会を通して連合会に出す」.
In data row 2, the words 「移転先」 have a pale yellow highlighter marker. Every row has its own text exactly as given; the rows are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 届, 当, 所, 登, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the words 移転先 in row 2 carry the yellow marker, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：調査士法人の届出の一覧表

- 型：早見表型（4列）　／　サイズ：1080×2300　／　保存名：`図解4_法人の届出の一覧表.png`
- 記事の挿入位置：「部品3：調査士法人」の節の、届出の一覧のあと

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference table poster with four columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「調査士法人の届出」
「調査士会と連合会の両方へ」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns and exactly 7 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: 「手続」, 「条文」, 「期限」, 「あわせて届け出る調査士会」.
Data row 1: first column 「成立の届出」; second column 「33条」; third column 「成立の日から2週間以内」; fourth column 「主たる事務所の所在地の調査士会」.
Data row 2: first column 「定款の変更の届出」; second column 「34条2項」; third column 「変更の日から2週間以内」; fourth column 「主たる事務所の所在地の調査士会」.
Data row 3: first column 「解散の届出（合併を除く）」; second column 「39条2項」; third column 「解散の日から2週間以内」; fourth column 「主たる事務所の所在地の調査士会」.
Data row 4: first column 「合併の届出」; second column 「40条3項」; third column 「合併の日から2週間以内」; fourth column 「主たる事務所の所在地の調査士会」.
Data row 5: first column 「清算結了の届出」; second column 「53条3項」; third column 「清算結了の登記後速やかに」; fourth column 「主たる事務所の所在地の調査士会」.
Data row 6: first column 「新たに会員になったときの届出」; second column 「53条6項」; third column 「会員となった日から2週間以内」; fourth column 「その会員になった調査士会」.
Data row 7: first column 「調査士会を退会したときの届出」; second column 「53条7項」; third column 「退会の日から2週間以内」; fourth column 「その退会した調査士会」.
Under the table, one wide pale-yellow banner with dark navy text: 「どの行も、調査士会連合会にもあわせて届け出る」.
In data row 3 the words 「合併を除く」 have a pale yellow highlighter marker, and in data row 5 the words 「登記後速やかに」 have a pale yellow highlighter marker. Every row has its own text exactly as given, except that the fourth column of rows 1 to 5 reads the same on purpose; draw the same string in those five cells.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 届, 所, 款, 登, 解, 記, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 7 data rows, that every cell reads exactly as given, that only the two marked phrases carry the yellow marker, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解5：調査士法人が解散したとき、どの条文で届け出るか

- 型：フローチャート型　／　サイズ：1080×1900　／　保存名：`図解5_解散と合併の仕分け.png`
- 記事の挿入位置：「解散と合併は、条文が分かれる」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「調査士法人が解散したとき」
「どの条文で届け出る？」
Subtitle (smaller, centered, 1 line):
「土地家屋調査士法 第39条・第40条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 1. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「調査士法人が解散した」
NODE DIAMOND 1: 「解散の理由は、他の調査士法人との合併か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「合併」 and 「合併以外」; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.
  - Arrow down-left with the label 「合併」 to RESULT 1.
  - Arrow down-right with the label 「合併以外」 to RESULT 2.
NODE RESULT 1 (blue box): 「40条3項の届出」 on the first line, 「合併の日から2週間以内」 on the second line and 「登記事項証明書を添える」 on the third line.
NODE RESULT 2 (blue box): 「39条2項の届出」 on the first line, 「解散の日から2週間以内」 on the second line and 「破産手続開始の決定もここ」 on the third line.
At the very bottom, one small light-gray tag centered across both result boxes: 「届出先は、どちらも調査士会と連合会」
Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings 「40条3項の届出」 and 「39条2項の届出」 are NOT identical); do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 届, 登, 解, 記, 証, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows only the two navy labels 合併 and 合併以外 and no はい or いいえ, that both result boxes are blue and have different texts, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解6：登記の申請と筆界特定の申請の対比表

- 型：対比表型（3列）　／　サイズ：1080×1900　／　保存名：`図解6_登記と筆界特定の申請先の対比表.png`
- 記事の挿入位置：「部品5：登記は登記所、筆界特定は法務局又は地方法務局」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three columns (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「登記と筆界特定の申請先」
「どこが違う？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第6条・第124条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header 「登記の申請」; the third header 「筆界特定の申請」. The two headers are NOT identical.
Data row 1 (row label cell, dark navy, white text: 「事務をつかさどる所」): second column 「登記所（法務局・地方法務局・支局・出張所）」; third column 「法務局又は地方法務局」.
Data row 2 (row label cell, dark navy, white text: 「管轄の基準」): second column 「不動産の所在地」; third column 「対象土地の所在地」.
Data row 3 (row label cell, dark navy, white text: 「二以上にまたがるとき」): second column 「事務を行う所が指定される」; third column 「事務を行う所が指定される」.
Data row 4 (row label cell, dark navy, white text: 「指定がされる前」): second column 「一の登記所に申請できる」; third column 「一の法務局又は地方法務局に申請できる」.
Data row 5 (row label cell, dark navy, white text: 「根拠」): second column 「不動産登記法6条」; third column 「不動産登記法124条」.
In data row 1 the words 「登記所」 in the second column and the words 「法務局又は地方法務局」 in the third column have a pale yellow highlighter marker, and in data row 4 the words 「申請できる」 in both columns have a pale yellow highlighter marker. The second and third columns of data row 3 have the same text on purpose; draw the same string in both cells. Every other cell has its own text exactly as given.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 対, 張, 所, 登, 記, 請, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the marked phrases carry the yellow marker, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解7：管轄区域にまたがるとき、どこに申請するか

- 型：フローチャート型　／　サイズ：1080×2000　／　保存名：`図解7_管轄にまたがるときの申請先.png`
- 記事の挿入位置：「部品7：指定がされる前でも、そのうちの一つに申請できる」の節の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「管轄区域にまたがるとき」
「どこに申請する？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第6条・第124条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas for START, DIAMOND 1 and DIAMOND 2, in this order from top to bottom. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between them. RESULT 2 and RESULT 3 sit below DIAMOND 2, one at the lower left and one at the lower right. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「申請先を決める」
NODE DIAMOND 1: 「対象の不動産は、二以上の管轄区域にまたがるか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「またがらない」 and 「またがる」; do not draw the strings 「はい」 or 「いいえ」 on these arrows.
  - Arrow right with the label 「またがらない」 to RESULT 1.
  - Arrow down with the label 「またがる」 to DIAMOND 2.
NODE RESULT 1 (blue box): 「所在地を管轄する所に」 on the first line and 「申請する」 on the second line.
NODE DIAMOND 2: 「事務を行う所の指定は、されたか？」 The text is placed inside the diamond on 3 lines. This diamond has TWO neutral navy branches with the labels 「された」 and 「まだ」.
  - Arrow down-left with the label 「された」 to RESULT 2.
  - Arrow down-right with the label 「まだ」 to RESULT 3.
NODE RESULT 2 (blue box): 「指定された所に」 on the first line and 「申請する」 on the second line.
NODE RESULT 3 (blue box): 「そのうち一つに」 on the first line and 「申請できる」 on the second line.
At the very bottom, one small light-gray tag centered across the canvas: 「筆界特定でも、登記でも同じ」
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three blue boxes have different texts (the strings 「所在地を管轄する所に」, 「指定された所に」 and 「そのうち一つに」 are NOT identical); do not copy one into another.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 対, 所, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show only their two navy labels and no はい or いいえ, that all three result boxes are blue and have different texts, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
