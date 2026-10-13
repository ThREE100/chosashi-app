# 総合記事②不動産登記法編 第6章　図解インフォグラフィック プロンプト（【PF1-2】抵当権・賃借権などの登記があるとき合併できるか（法第56条第5号・規則第131条）・1枚）

総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『できない建物の一覧』『要る・要らない』のような分類が中心なので、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。フローチャート（図解4）だけは、分岐の矢印とラベルを濃紺にし、結果の箱を『5号の制限に当たらない＝青』『5号の制限に当たる＝赤』で塗り分けます（『はい』『いいえ』の文字は使いません）。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解4 | 権利の登記がある建物は合併できる？（判定の流れ） | フローチャート／判定フロー型 | 1080×2900 | 不登法編6章_図解4_権利の登記と合併の判定.png | 【PF1-2】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解4：権利の登記がある建物は合併できる？（判定の流れ）

- 型：フローチャート／判定フロー型　／　サイズ：1080×2900　／　保存名：`不登法編6章_図解4_権利の登記と合併の判定.png`
- 記事の挿入位置：【PF1-2】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE (this flowchart): every arrow and every arrow label is dark navy; the strings 「はい」 and 「いいえ」 do not appear anywhere. The result boxes are colored by their outcome: a result box that says 「5号の制限に当たらない」 is BLUE, and a result box that says 「5号の制限に当たる」 is RED. Use dark navy for the start pill, the diamonds' outlines, the headings, and the badges, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「権利の登記がある建物は」
「合併できる？」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第56条5号／不動産登記規則 第131条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. The result boxes of DIAMOND 1 and DIAMOND 2 sit to the RIGHT of their diamonds on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「合併しようとする2つの建物」
NODE DIAMOND 1: 「所有権等以外の権利の登記が、ある？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. Under the diamond, a small gray caption 「所有権等：所有権・地上権・永小作権・地役権・採石権」.
  - Arrow right to RESULT 1 with the dark navy label 「ない」.
  - Arrow down to DIAMOND 2 with the dark navy label 「ある」.
NODE RESULT 1 (blue box): 「5号の制限に当たらない」 on the first line and 「ほかの号は別に確かめる」 on the second line.
NODE DIAMOND 2: 「その登記は、担保権の登記か信託の登記か？」
  - Arrow down to DIAMOND 3 with the dark navy label 「そうである」.
  - Arrow right to RESULT 2 with the dark navy label 「それ以外」.
NODE RESULT 2 (red box): 「5号の制限に当たる」 on the first line and 「賃借権などは、同一でも不可」 on the second line.
NODE DIAMOND 3: 「両建物で、決まった項目が同一か？」 The text is placed inside the diamond on 3 lines.
  - Arrow down-left with the dark navy label 「同一」 to RESULT 3.
  - Arrow down-right with the dark navy label 「同一でない」 to RESULT 4.
NODE RESULT 3 (blue box): 「5号の制限に当たらない」 on the first line and 「規則131条の例外に当たる」 on the second line.
NODE RESULT 4 (red box): 「5号の制限に当たる」 on the first line and 「決まった項目が同一でない」 on the second line.
Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different second lines, and the two red result boxes have different second lines. The first-line strings 「5号の制限に当たらない」 (blue) and 「5号の制限に当たる」 (red) differ by two characters and are NOT identical; copy each exactly as given and never turn one into the other.
--- TWO SIDE NOTE CARDS (below the flowchart, side by side, exactly the same size, each with a dashed dark navy outline and its heading placed fully INSIDE the card) ---
Left card, heading 「同一でなければならない項目」, two body lines 「担保権の登記：登記の目的、受付の年月日及び受付番号、登記原因及びその日付」 and 「信託の登記：法97条1項各号の登記事項」.
Right card, heading 「工場財団の登記がある建物」, body 「同一の財団を組成していても、合併できない」 and a small gray tag 「条文に直接の定めはない」.
The two cards have clearly different texts; the texts are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 号, 地, 建, 当, 所, 権, 物, 番, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that every arrow label is dark navy and the strings 「はい」 and 「いいえ」 appear nowhere, that RESULT 1 and RESULT 3 are blue and read 5号の制限に当たらない and RESULT 2 and RESULT 4 are red and read 5号の制限に当たる, that exactly two side note cards sit below the flowchart, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
