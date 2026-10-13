# 総合記事② 不動産登記法編 第7章　図解インフォグラフィック プロンプト（【PF2-2】合体前の建物にどんな登記があるかで、申請の形はどう変わるか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第7章「建物の合体による登記等」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch7.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は、分類・早見表が中心のものは、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解4）だけは、はい＝青・いいえ＝赤です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解4 | 合体前の建物の登記は、どうなっているか（判定の流れ） | 判定の流れ型 | 1080×2300 | 登記法編7章_図解4_合体前の登記の状態.png | 【PF2-2】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解4：合体前の建物の登記は、どうなっているか（判定の流れ）

- 型：判定の流れ型　／　サイズ：1080×2300　／　保存名：`登記法編7章_図解4_合体前の登記の状態.png`
- 記事の挿入位置：【PF2-2】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「合体前の建物の登記は」
「どうなっているか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第49条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 and RESULT 3 sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「二以上の建物が合体して、一個の建物になった」
NODE DIAMOND 1: 「合体前の建物は、いずれも表題登記がない建物か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow right to RESULT 1 with the BLUE label 「はい」.
  - Arrow down to DIAMOND 2 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「新築の建物の表題登記を申請する」 on the first two lines, 「登記原因は、新築、新築、合体の形」 on the next two lines, and the small gray tag 「実務の取扱い」 on the last line.
NODE DIAMOND 2: 「所有権の登記がある建物と、ない建物が混じっているか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down-left with the BLUE label 「はい」 to RESULT 2.
  - Arrow down-right with the RED label 「いいえ」 to RESULT 3.
NODE RESULT 2 (blue box): 「合体による登記等と、所有権の登記を併せて申請する」 on the first three lines, 「未登記の建物の所有者や表題部所有者を、登記名義人とする」 on the next three lines, and the small gray tag 「法49条1項後段」 on the last line.
NODE RESULT 3 (red box): 「合体による登記等だけを申請する」 on the first two lines.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 権, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
