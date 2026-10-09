# 第51条第1項　図解インフォグラフィック プロンプト（6枚）

条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第51条第1項の記事に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 第51条第1項を5つの部品で読む | カードポスター型（俯瞰） | 1080×2300 | 図解1_第51条1項を5つの部品で読む.png | 条文の原文とひとことでの直後（「条文を5つの部品に分けて読む」の節の冒頭） |
| 図解2 | 44条1項の9つの登記事項と、51条1項の対象 | 早見表型 | 1080×2200 | 図解2_44条1項の9つの登記事項.png | 「どの欄が変わったら対象か」の節の冒頭 |
| 図解3 | 変更の登記は要る？の判定フロー | フローチャート型 | 1080×2600 | 図解3_変更の登記は要るかの判定フロー.png | 「どの欄が変わったら対象か」の節の終わり（「確認する順番」の直前） |
| 図解4 | 通常の建物と共用部分の建物で、申請する人が違う | 対比表型 | 1080×1700 | 図解4_通常の建物と共用部分の建物.png | 「誰が申請するか」の節（部品2）の終わり |
| 図解5 | 第51条の1項〜4項の申請する人と起算点 | 早見表型 | 1080×1600 | 図解5_1項から4項の起算点.png | 「他の項との違い」の節 |
| 図解6 | 似ているけれど違う登記（更正・住所の変更・分割・滅失） | 早見表型 | 1080×1700 | 図解6_似ているけれど違う登記.png | 「隣の条文との違い」の節 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：第51条第1項を5つの部品で読む

- 型：カードポスター型（俯瞰）　／　サイズ：1080×2300　／　保存名：`図解1_第51条1項を5つの部品で読む.png`
- 記事の挿入位置：条文の原文とひとことでの直後（「条文を5つの部品に分けて読む」の節の冒頭）

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「建物の表題部の変更の登記」
「条文を5つの部品で読む」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条第1項」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「何が変わったら？」
Illustration: An isometric small house icon beside a registry ledger card labeled 「登記事項」; three small name tags around the house: 「所在」, 「床面積」, 「敷地権」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「登記事項の変更」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「誰が申請する？」
Illustration: Two person pictograms side by side with name tags 「表題部所有者」 and 「所有権の登記名義人」. Beside them, a third person pictogram inside a dotted frame with the tag 「所有者」 and a small note 「共用部分の登記がある建物」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「名義人（共用部分は所有者）」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「いつまでに？」
Illustration: A calendar page with one circled date tagged 「変更があった日」 and a wide bracket spanning one month from that date, tagged 「1か月以内」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「変更から1か月以内」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「何を申請する？」
Illustration: A document sheet with a rubber stamp, labeled 「変更の登記」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「変更の登記を申請」
--- CARD 5 ---
Badge: a filled dark navy circle containing the number 5 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「怠るとどうなる？」
Illustration: A caution triangle sign and a coin icon, with the small note 「正当な理由がない場合」 and the label 「10万円以下の過料」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「10万円以下の過料」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 当, 所, 権, 物, 登, 記, 請, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解2：44条1項の9つの登記事項と、51条1項の対象

- 型：早見表型　／　サイズ：1080×2200　／　保存名：`図解2_44条1項の9つの登記事項.png`
- 記事の挿入位置：「どの欄が変わったら対象か」の節の冒頭

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「44条1項の9つの登記事項」
「変更の登記が要るのはどれ？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第44条第1項・第51条第1項」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns and exactly 9 data rows, no merged cells.
Header row (dark navy cells with white text), in this order: 「号」, 「登記事項」, 「第51条1項の対象」, 「変わる場面の例」.
Data row 1: 「1号」, 「所在」, 「対象」, 「分筆で地番が変わった」.
Data row 2: 「2号」, 「家屋番号」, 「対象外」, 「登記所が付す番号」.
Data row 3: 「3号」, 「種類・構造・床面積」, 「対象」, 「増築、用途の変更、屋根の種類の変更」.
Data row 4: 「4号」, 「名称」, 「対象」, 「建物の名称を変えた」.
Data row 5: 「5号」, 「附属建物」, 「対象」, 「附属建物の新築、取壊し」.
Data row 6: 「6号」, 「共用部分である旨」, 「対象外」, 「共用部分の登記で扱う」.
Data row 7: 「7号」, 「一棟の建物の構造・床面積」, 「対象」, 「一棟の床面積の変更」.
Data row 8: 「8号」, 「一棟の建物の名称」, 「対象」, 「一棟の建物の名称を変えた」.
Data row 9: 「9号」, 「敷地権」, 「対象」, 「敷地権が生じた、割合が変わった」.
In the third column, the string 「対象」 is written in BLUE and the string 「対象外」 is written in RED. The two rows whose third column is 「対象外」 (data rows 2 and 6) have a pale gray row background so they stand out; the other seven rows keep the alternating colors. Use words only in that column; draw no check mark and no cross mark.
Along the right edge of data rows 7, 8, and 9, draw one dark navy bracket with the small tag 「区分建物のみ」.
Row order rule: the first column reads 「1号」, 「2号」, 「3号」, 「4号」, 「5号」, 「6号」, 「7号」, 「8号」, 「9号」 from top to bottom, each exactly once; no row is duplicated, merged, or missing.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 対, 建, 所, 権, 物, 番, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 9 data rows in the order 1号 to 9号, that every cell reads exactly as given, that exactly two rows (2号 and 6号) show the red string 対象外, and that the other seven rows show the blue string 対象. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：変更の登記は要る？の判定フロー

- 型：フローチャート型　／　サイズ：1080×2600　／　保存名：`図解3_変更の登記は要るかの判定フロー.png`
- 記事の挿入位置：「どの欄が変わったら対象か」の節の終わり（「確認する順番」の直前）

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「変更の登記は要る？」
「上から順に確かめる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条第1項」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「変更の登記が要るか考える」
NODE DIAMOND 1: 「登記事項（家屋番号と共用部分である旨を除く）に食い違いが出たか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「第51条1項の対象外」 on the first line and 「外壁・屋根の材料の張り替えだけ、表題部所有者の住所の変更など」 on the next two lines.
NODE DIAMOND 2: 「登記をしたあとで、現実が変わったからか？」
  - Arrow down to DIAMOND 3 with the BLUE label 「はい」.
  - Arrow right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 2 (red box): 「更正の登記（法53条）」 on the first line and 「申請の義務はない」 on the second line.
NODE DIAMOND 3: 「共用部分である旨の登記がある建物か？」 This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「ある」 and 「ない」; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.
  - Arrow down-left with the label 「ある」 to RESULT 3.
  - Arrow down-right with the label 「ない」 to RESULT 4.
NODE RESULT 3 (blue box): 「所有者が申請する」 on the first line and 「変更があった日から1か月以内」 on the second line.
NODE RESULT 4 (blue box): 「表題部所有者・所有権の登記名義人が申請する」 on the first two lines and 「変更があった日から1か月以内」 on the third line.
Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings 「所有者が申請する」 and 「表題部所有者・所有権の登記名義人が申請する」 are NOT identical); do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 対, 建, 張, 所, 権, 物, 番, 登, 記, 請, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that DIAMOND 1 and DIAMOND 2 each show a blue 「はい」 and a red 「いいえ」, that DIAMOND 3 shows only the two navy labels 「ある」 and 「ない」, that RESULT 1 and RESULT 2 are red and RESULT 3 and RESULT 4 are blue, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：通常の建物と共用部分の建物で、申請する人が違う

- 型：対比表型　／　サイズ：1080×1700　／　保存名：`図解4_通常の建物と共用部分の建物.png`
- 記事の挿入位置：「誰が申請するか」の節（部品2）の終わり

```text
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a two-column comparison poster (対比表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「変更の登記は、だれが申請する？」
「通常の建物と共用部分の建物」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条第1項」
--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---
「通常の建物」
--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---
「共用部分である旨の登記がある建物」
The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere.
--- ROW 1 (row label 「登記記録」) ---
Left card: a simple ledger icon with the string 「表題部所有者または所有権の登記名義人が記録されている」.
Right card: a simple ledger icon with an empty name field and the string 「名義人の登記は抹消されている（法58条4項）」.
--- ROW 2 (row label 「申請する人」) ---
Left card: a person pictogram with the name tag 「表題部所有者または所有権の登記名義人」.
Right card: a person pictogram with the name tag 「所有者（法51条1項かっこ書）」.
--- BOTTOM BAND (one wide dark navy band across both columns, white text) ---
「どちらも、変更があった日から1か月以内に変更の登記を申請」
The left and right cards of each row have clearly different texts; the texts are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 対, 建, 所, 権, 物, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 2 columns and exactly 2 rows of cards plus one bottom band, that the left and right texts of each row are different, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解5：第51条の1項〜4項の申請する人と起算点

- 型：早見表型　／　サイズ：1080×1600　／　保存名：`図解5_1項から4項の起算点.png`
- 記事の挿入位置：「他の項との違い」の節

```text
Create a Japanese-language infographic, portrait layout, 1080x1600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「1か月は、だれが、いつから数える？」
「第51条の1項〜4項」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第51条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Header row (dark navy cells with white text), in this order: 「項」, 「申請する人」, 「1か月の起算点」.
Data row 1: 「1項」, 「変更があった当時の名義人（共用部分の建物は所有者）」, 「変更があった日」.
Data row 2: 「2項」, 「変更のあとに名義人になった者」, 「その者の登記があった日」.
Data row 3: 「3項」, 「変更のあとに共用部分の登記がされたときの所有者（1項・2項の人を除く）」, 「共用部分の登記がされた日」.
Data row 4: 「4項」, 「共用部分の登記がある建物で、変更のあとに所有権を取得した者（3項の人を除く）」, 「所有権の取得の日」.
In data row 2, under the third-column string, add one line of small gray text: 「表題部所有者は更正の登記、名義人は所有権の登記」.
Data row 1 is highlighted with a pale yellow row background and a small dark navy tag 「この記事の対象」 at its left edge. The other three rows keep the alternating colors.
The four first-column strings 「1項」, 「2項」, 「3項」, 「4項」 are all different; each appears exactly once.
Draw no check mark and no cross mark; use no blue or red anywhere except for the dark navy header cells.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 対, 建, 当, 所, 権, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows in the order 1項, 2項, 3項, 4項, that every cell reads exactly as given, and that only data row 1 is highlighted. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解6：似ているけれど違う登記（更正・住所の変更・分割・滅失）

- 型：早見表型　／　サイズ：1080×1700　／　保存名：`図解6_似ているけれど違う登記.png`
- 記事の挿入位置：「隣の条文との違い」の節

```text
Create a Japanese-language infographic, portrait layout, 1080x1700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「似ているけれど違う登記」
「申請の義務があるのはどれ？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第31条・第51条・第53条・第54条・第57条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.
Header row (dark navy cells with white text), in this order: 「登記」, 「どんなとき」, 「申請の義務」.
Data row 1: 「変更の登記（法51条1項）」, 「登記のあとで、事実が変わった」, 「あり：変更の日から1か月以内」.
Data row 2: 「更正の登記（法53条）」, 「登記したときから、誤っていた」, 「なし」.
Data row 3: 「表題部所有者の氏名・住所の変更（法31条）」, 「表題部所有者の住所などが変わった」, 「なし」.
Data row 4: 「建物の分割（法54条）」, 「附属建物を別の一個の建物にする」, 「なし」.
Data row 5: 「建物の滅失（法57条）」, 「建物がなくなった」, 「あり：滅失の日から1か月以内」.
In the third column, strings that begin with 「あり」 are written in BLUE and the string 「なし」 is written in RED. Use words only; draw no check mark and no cross mark.
Data row 1 is highlighted with a pale yellow row background and a small dark navy tag 「この記事の対象」 at its left edge.
The three rows whose third column is 「なし」 (data rows 2, 3, and 4) have the identical third-column string; that is intended, so draw the same string in all three.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 対, 建, 所, 物, 登, 記, 請, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 5 data rows in the order given, that every cell reads exactly as given, that exactly two rows show a blue string beginning with あり and exactly three rows show the red string なし. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
