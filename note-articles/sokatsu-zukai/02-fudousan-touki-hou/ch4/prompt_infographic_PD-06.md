# 総合記事②不動産登記法編 第4章　図解インフォグラフィック プロンプト（【PD-6】権利を消した分筆は、錯誤で抹消できるか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『申請できるか』『合筆できるか』のような分類が中心で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。例外は、はい／いいえの判定の流れ図（分筆を錯誤で戻せるか）で、はい＝青、いいえ＝赤で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解7 | 分筆を錯誤で戻せる？（判定の流れ図） | フローチャート型 | 1080×2300 | 不動産登記法編4章_図解7_分筆を錯誤で戻せるか.png | 【PD-6】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解7：分筆を錯誤で戻せる？（判定の流れ図）

- 型：フローチャート型　／　サイズ：1080×2300　／　保存名：`不動産登記法編4章_図解7_分筆を錯誤で戻せるか.png`
- 記事の挿入位置：【PD-6】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ図).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「分筆を錯誤で戻せる？」
「分かれ目は、権利を消したか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第40条・第72条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit below the diamond, one to the left and one to the right of the center line, at the same height and the same size. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「分筆の登記を、錯誤で抹消したい」
NODE DIAMOND 1: 「分筆のとき、権利を消す承諾の情報を出していないか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down-left with the BLUE label 「はい」 to RESULT 1.
  - Arrow down-right with the RED label 「いいえ」 to RESULT 2.
NODE RESULT 1 (blue box): 「錯誤を原因に、分筆の登記を抹消できる」 on the first line and 「前から付いていた抵当権は、転写されただけ」 on the second line.
NODE RESULT 2 (red box): 「分筆錯誤だけでは、抹消できない」 on the first line, 「先に、消えた権利の登記の回復が要る（法72条）」 on the second line and 「回復には、利害関係人の承諾が要る」 on the third line.
Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts.
--- SIDE NOTE (below the result boxes, a wide card with a dashed dark navy outline and a small gray tag 「右の扱いは、実務の取扱いによる整理」) ---
Heading 「分かれ目は、承諾の情報を出したか」, body 「抵当権があるだけでは、分筆錯誤を妨げない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 当, 承, 抵, 権, 登, 記, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that no text overflows its box, that no arrow label is hidden, and that the side note appears once below the result boxes. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
