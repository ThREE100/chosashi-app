# 【M3-4】遺贈・遺産分割・遺言による承継は、登記が要るか　追加の図解インフォグラフィック プロンプト（1枚）

総合記事『直前期の苦手論点つぶし総合記事①民法編』の第3章（`note-articles/column/sokatsu-01-minpou-ch3.md`）の【M3-4】の「判断のしかた」の直後（登記が要るかの判定の流れ図）に差し込む、追加の図解のプロンプトです。作成済みの図解（`infographic/prompt_infographic_M3-?.md`）は変えず、記事の要点のうち図がなかった部分を補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。当事者はラテン文字ではなく役割名で書いています。キャラクターは描かないので、参照画像は不要です。

既存の図解（承継と対抗の対比表）との違い：既存の図解は、取得の原因ごとに結論を横に並べる表です。この図解は、記事の『判断のしかた』（原因を確かめる→法定相続分を超えるかを見る）を、上から順にたどる判定の流れ図にしたものです。

- 図解1：登記が要るのは、どんなとき？（原因と取得した範囲の判定の流れ）（型：フローチャート型／サイズ：1080×2400）
  - 保存名：`民法編3_4_追加_登記が要るかの判定の流れ.png`
  - 記事の挿入位置：【M3-4】の「判断のしかた」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：登記が要るのは、どんなとき？（原因と取得した範囲の判定の流れ）

- 型：フローチャート型　／　サイズ：1080×2400　／　保存名：`民法編3_4_追加_登記が要るかの判定の流れ.png`
- 記事の挿入位置：【M3-4】の「判断のしかた」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「登記が要るのは、どんなとき？」
「原因と、取得した範囲で決まる」
Subtitle (smaller, centered, 1 line):
「民法　第177条・第899条の2」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, each with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The side note card sits at the bottom, below RESULT 3. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「相続・遺産分割・遺言などで取得した不動産を」 on the first line and 「第三者に主張する」 on the second line.
NODE DIAMOND 1: 「特定遺贈ではなく、相続による承継か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box): 「登記が要る」 on the first line, 「特定遺贈は個別の権利移転」 on the second line and 「（民法177条）」 on the third line.
NODE DIAMOND 2: 「取得した部分は、法定相続分の範囲内か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to RESULT 3 with the BLUE label 「はい」.
  - Arrow right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 2 (red box): 「登記が要る」 on the first line, 「遺産分割でも遺言でも」 on the second line and 「（民法899条の2第1項）」 on the third line.
NODE RESULT 3 (blue box): 「登記なしで主張できる」 on the first line and 「法定相続分の範囲内」 on the second line.
--- SIDE NOTE CARD (a wide card with a dashed dark navy outline at the bottom, neutral dark navy text, no arrow attached) ---
Heading 「相続させる旨の遺言は、死亡と同時に承継される」, body 「承継の時期と、登記が要るかは、別の問い」.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. RESULT 1 and RESULT 2 start with the same first line on purpose, and their second and third lines are different; the strings 「特定遺贈は個別の権利移転」 and 「遺産分割でも遺言でも」 are NOT identical, so do not copy one into the other.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 張, 承, 権, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are red, that RESULT 3 is blue and sits directly below DIAMOND 2, that the side note card has no arrow attached and is the last element, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 検品チェック（生成後）

- [ ] 開始ノード1・ひし形2・結果の箱3の数と並びが合っている（ひし形1の右に結果1、ひし形2の右に結果2、ひし形2の下に結果3）
- [ ] 両方のひし形で、下向きが青の『はい』、右向きが赤の『いいえ』。結果1・2は赤、結果3は青
- [ ] 結果1と結果2の2〜3行目が別の文言（コピーされていない）。下の破線の札に矢印が付いていない
- [ ] 簡体字・繁体字・英字・余計な文字がない。背景が不透明。文字が箱からはみ出していない

### 記事・条文との照合

- 特定遺贈は民法177条の問題（記事【M3-4】の中身の整理・肢の判定D0115）。法定相続分を超える部分は、遺産分割でも遺言でも対抗要件が必要（民法899条の2第1項、`note-articles/laws/minpou-3-shinzoku-souzoku.md` で原文確認済み）
- 『法定相続分の範囲内は、登記なしで主張できる』：民法899条の2第1項が対抗要件を求めるのは『相続分を超える部分』なので、その反対の整理（条文に明記はなく、記事の判断のしかた2『法定相続分を超えるなら登記が必要』の裏返し）。図では、条文の根拠を結果の箱3に載せていない
- 相続させる旨の遺言：記事の中身の整理（遺贈と解すべき特段の事情がなければ、遺産分割方法の指定と解され、死亡と同時に承継される）。承継の時期と対抗の要否を別の問いとして側注にした。法定相続分を超える部分は、この遺言でも結果2の経路（民法899条の2第1項）になる
- 共有物分割と遺産分割の関係（民法258条の2）は、既存の図解（別の問いのカード）にあるため、この流れ図には入れていない
