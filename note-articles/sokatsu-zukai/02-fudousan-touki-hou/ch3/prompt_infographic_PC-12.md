# 総合記事②不動産登記法編 第3章　図解インフォグラフィック プロンプト（【PC-12】筆界特定の却下・立入調査・結果の公開・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表が中心の図は、青・赤・チェック・バツを使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。はい／いいえの判定の流れ図だけ、共通部品の配色の規則（青＝はい、赤＝いいえ）で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解17 | 筆界特定の申請は却下される？（判定の流れ） | 判定の流れ図型 | 1080×2700 | 不登法第3章_図解17_筆界特定の却下.png | 【PC-12】『中身の整理』の直後 |
| 図解18 | 筆界特定の手続の相手と主体 | カードポスター型 | 1080×2300 | 不登法第3章_図解18_筆界特定の相手と主体.png | 【PC-12】『たとえば』の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解17：筆界特定の申請は却下される？（判定の流れ）

- 型：判定の流れ図型　／　サイズ：1080×2700　／　保存名：`不登法第3章_図解17_筆界特定の却下.png`
- 記事の挿入位置：【PC-12】『中身の整理』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「筆界特定の申請は却下される？」
「特定済みの筆界を、再び申請」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第132条・第156条・第158条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The YES result box of DIAMOND 2 sits at the bottom, to the left of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「筆界特定を申請する」
NODE DIAMOND 1: 「その筆界は、既に筆界特定がされているか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「この理由では、却下されない」 on the first line and 「ほかの却下事由は別に確かめる」 on the second line.
NODE DIAMOND 2: 「更に筆界特定をする、特段の必要があるか？」 The text is placed inside the diamond on 3 lines.
  - Arrow down-left to RESULT 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 2 (blue box): 「却下されない」 on the first line and 「法132条1項7号ただし書」 on the second line.
NODE RESULT 3 (red box): 「却下される」 on the first line and 「法132条1項7号」 on the second line.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The result boxes have different texts; do not copy one into another.
--- SIDE NOTE CARD (below the flowchart, a wide card with a dashed dark navy outline and a small dark navy tag 「却下されたあと」) ---
Three body lines, neutral dark navy outlines only (no blue and no red in this card): 「却下は、登記官の処分とみなされる（法132条2項）」, 「法務局又は地方法務局の長に審査請求ができる（法156条1項）」, 「審査請求の期間の制限はない（法158条）」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 登, 記, 請, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 2 is blue and RESULT 1 and RESULT 3 are red, that the side note card below is neutral dark navy, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解18：筆界特定の手続の相手と主体

- 型：カードポスター型　／　サイズ：1080×2300　／　保存名：`不登法第3章_図解18_筆界特定の相手と主体.png`
- 記事の挿入位置：【PC-12】『たとえば』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with three numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「筆界特定の手続の相手と主体」
「誰に通知し、誰が請求するか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第137条・第149条・第156条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「立入調査の通知先」
Illustration: A person pictogram standing at a garden gate with the name tag 「占有者」 and a small notice sheet in front of the gate.
Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「あらかじめ、日時と場所を通知」
「通知の相手は、土地の占有者」
「名義人に通知する規定はない」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「占有者」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「筆界特定書の写し」
Illustration: A document sheet with a row of three plain person pictograms in front of it, each holding a small coin icon, no text on the document.
Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「手数料を納付して請求する」
「請求できるのは、何人も」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「何人も」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「却下への不服」
Illustration: A decision sheet with a rubber stamp, and an arrow-free small building icon beside it with the tag 「法務局」.
Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「却下された申請人が審査請求できる」
「宛先は、法務局又は地方法務局の長」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「審査請求」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 占, 地, 所, 登, 規, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
