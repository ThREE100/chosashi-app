# 総合記事② 不動産登記法編 第5章　図解インフォグラフィック プロンプト（【PE-6】附属建物の表示で何を書き、何が省略できるか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。判定の流れ図（フローチャート）では、はい＝青・いいえ＝赤で描きます。分類・早見表・比較カードの図は、はい／いいえの分岐ではないため、青・赤を使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解9 | 附属建物の表示は、何を書く？（区分建物かどうかで分かれる） | 判定の流れ型 | 1080×2600 | 不動産登記法編⑤_図解9_附属建物の表示.png | 【PE-6】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解9：附属建物の表示は、何を書く？（区分建物かどうかで分かれる）

- 型：判定の流れ型　／　サイズ：1080×2600　／　保存名：`不動産登記法編⑤_図解9_附属建物の表示.png`
- 記事の挿入位置：【PE-6】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「附属建物の表示は、何を書く？」
「区分建物かどうかで分かれる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第44条第1項第5号」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every RED 「いいえ」 result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two blue result boxes at the bottom sit one to the left and one to the right of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「主である建物に附属建物がある」
NODE DIAMOND 1: 「附属建物は、区分建物か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「所在・種類・構造・床面積を書く」 on two lines.
NODE DIAMOND 2: 「主である建物と同じ一棟に属するか？」 The text is placed inside the diamond on 3 lines. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels 「同じ一棟」 and 「別の一棟」; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.
  - Arrow down-left with the label 「同じ一棟」 to RESULT 2.
  - Arrow down-right with the label 「別の一棟」 to RESULT 3.
NODE RESULT 2 (blue box): 「附属建物自体の種類・構造・床面積を書く」 on three lines, and the small line 「一棟の所在・構造・床面積は、記録を要しない（準則89条）」.
NODE RESULT 3 (blue box): 「附属建物自体の表示に加え、その一棟の所在地番も申請情報に書く」 on four lines.
--- SIDE NOTE CARD (below the flowchart, a wide card with a dashed dark navy outline) ---
Heading 「家屋番号は、一個の建物に一つ」, body 「附属建物には、別の家屋番号は付かない（管轄登記所が違っても同じ）」 and a small gray tag 「法45条」.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts; do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 所, 物, 番, 登, 記, 請, 違, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there is exactly 1 start node, 2 diamonds, 3 result boxes and 1 side note card, that DIAMOND 1 shows a blue 「はい」 and a red 「いいえ」, that DIAMOND 2 shows only the two navy labels 「同じ一棟」 and 「別の一棟」, that RESULT 1 is red and RESULT 2 and RESULT 3 are blue, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
