# 【M1-3】心裡留保・虚偽表示：善意の第三者は何を満たせば守られるのか　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M1-3】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、はい＝青、いいえ＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：善意の第三者は守られるかの判定フロー
  - 型：フローチャート型　／　サイズ：1080×2500　／　保存名：`図解1_善意の第三者は守られるかの判定フロー.png`
  - 記事の挿入位置：【M1-3】の「判断のしかた」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：善意の第三者は守られるかの判定フロー

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー) followed by one note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「善意の第三者は守られる？」
「上から順に確かめる」
Subtitle (smaller, centered, 1 line):
「民法 総則（意思表示）」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. Every red result box (RESULT 1 and RESULT 2) sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final blue result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「無効や取消しを、第三者に対抗できるか」
NODE DIAMOND 1: 「その人は、新たに取引に入った第三者か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「第三者に当たらない」 on the first line and 「当事者・包括承継人（相続人）は守られない」 on the next two lines.
NODE DIAMOND 2: 「その第三者は、善意か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down to DIAMOND 3 with the BLUE label 「はい」.
  - Arrow right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 2 (red box): 「善意でないと守られない」 on the first line and 「無効や取消しを対抗できる」 on the second line.
NODE DIAMOND 3: 「原因は、心裡留保・虚偽表示か、詐欺・錯誤か？」 This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red); do not draw the strings 「はい」 or 「いいえ」 on these two arrows. The text is placed inside the diamond on 3 lines.
  - Arrow down-left with the label 「心裡留保・虚偽表示」 to RESULT 3.
  - Arrow down-right with the label 「詐欺・錯誤」 to RESULT 4.
NODE RESULT 3 (blue box): 「善意だけで守られる」 on the first line and 「過失があってもよい」 on the second line, with the small gray tag 「93条2項・94条2項」.
NODE RESULT 4 (blue box): 「善意でかつ過失がないとき守られる」 on the first two lines, with the small gray tag 「96条3項・95条4項」.
Counts: 1 start node, 3 diamonds, 4 result boxes (RESULT 1 and RESULT 2 red, RESULT 3 and RESULT 4 blue), 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings 「善意だけで守られる」 and 「善意でかつ過失がないとき守られる」 are NOT identical); do not copy one into the other.
--- NOTE CARD (a wide rounded card directly below the flowchart, pale gray fill, dark navy outline, with NO arrow connecting it to any node, and no blue or red) ---
Heading (bold, ONE line): 「虚偽表示の第三者は」
Body (ONE line): 「登記がなくても守られる（判例）」.
Under the body, a small dark navy tag: 「相続人は、善意でも第三者でない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 効, 対, 当, 承, 抗, 欺, 無, 登, 記, 詐, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that DIAMOND 1 and DIAMOND 2 each show a blue 「はい」 and a red 「いいえ」, that DIAMOND 3 shows only the two navy labels 「心裡留保・虚偽表示」 and 「詐欺・錯誤」, that RESULT 1 and RESULT 2 are red and RESULT 3 and RESULT 4 are blue, that there is exactly one note card below the flowchart and it is not connected by any arrow, that no text overflows its box, and that no arrow label is hidden. Confirm that the second character of 心裡留保 is drawn exactly as 裡 (clothing radical on the left, 里 on the right) everywhere it appears. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`図解1_善意の第三者は守られるかの判定フロー.png`

## 検品チェック

- 開始の楕円が1つ、ひし形が3つ、結果の箱が4つ（赤2・青2）か。ひし形1・2にだけ、青の「はい」と赤の「いいえ」が付いているか。
- ひし形3の出口が、濃紺の「心裡留保・虚偽表示」と「詐欺・錯誤」の2つだけで、青・赤の矢印やラベルになっていないか。
- 結果の箱のあとに矢印が出ていないか。注記のカードが1枚だけで、矢印でつながれていないか。
- 条番号（93条2項・94条2項・96条3項・95条4項）と、「虚偽表示の第三者は登記がなくても守られる（判例）」が指定どおりか。
- 簡体字・余計な文字・透過・図番がないか。