# 総合記事②不動産登記法編 第8章　図解インフォグラフィック プロンプト（【PG1-2】何が敷地権になるのか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第8章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch8.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・列挙が中心の図解（カードポスター・表・ステップ）は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）だけは、はい＝青・いいえ＝赤の配色です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解3 | 敷地権になれるか（判定の流れ） | フローチャート型 | 1080×2000 | 不登法8章_図解3_敷地権になれるか.png | 【PG1-2】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解3：敷地権になれるか（判定の流れ）

- 型：フローチャート型　／　サイズ：1080×2000　／　保存名：`不登法8章_図解3_敷地権になれるか.png`
- 記事の挿入位置：【PG1-2】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ図).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権になれるか」
「上から順に確かめる」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第44条第1項第9号」
--- FLOWCHART ---
Layout: a vertical main line down the center: START at the top, then DIAMOND 1, then DIAMOND 2, then RESULT 1 at the bottom. RESULT 2 sits to the right of DIAMOND 1 and RESULT 3 sits to the right of DIAMOND 2, each reached by one straight horizontal arrow. Keep at least 60 px of empty space around every arrow label so that the labels stay visible. All arrows are straight, and no arrows cross each other.
NODE START (rounded pill, dark navy): 「専有部分のための敷地の権利」
NODE DIAMOND 1: 「登記された権利か？」 The text is placed inside the diamond on 2 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down with the label 「はい」 to DIAMOND 2.
  - Arrow right with the label 「いいえ」 to RESULT 2.
NODE DIAMOND 2: 「専有部分と分離して処分できないか？」 The text is placed inside the diamond on 3 lines.
  - Arrow down with the label 「はい」 to RESULT 1.
  - Arrow right with the label 「いいえ」 to RESULT 3.
NODE RESULT 1 (white box, blue outline): 「敷地権になる」
NODE RESULT 2 (white box, red outline): 「敷地権にならない」 on the first line and 「使用借権は登記できない」 on the second line.
NODE RESULT 3 (white box, red outline): 「敷地権にならない」 on the first line and 「規約に別段の定めがある」 on the second line.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The first line of RESULT 2 and RESULT 3 is the same string on purpose; their second lines differ.
Under the flowchart, two small light-gray tags side by side: 「共有の持分でも、敷地権になる」 and 「所有権・地上権・賃借権は登記できる」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 所, 権, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that the arrows pointing to the right result boxes are red with the label いいえ and the arrows pointing down are blue with the label はい, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
