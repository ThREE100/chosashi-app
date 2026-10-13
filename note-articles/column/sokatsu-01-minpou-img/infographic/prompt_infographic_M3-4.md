# 【M3-4】順次譲渡（A→B→C）で、相続人・債権者・他人物売買をどう扱うか　図解インフォグラフィック プロンプト（1枚）

民法編の総合記事（`note-articles/column/sokatsu-01-minpou.md`）の【M3-4】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一していますが、この図解は対比表なので、○×・青・赤は使いません。画像の中には、図の番号を入れません。4コマ（`4koma/prompt_4koma_M3-4_D0115-D0116-D1629.md`）が3つの肢を並べ直す形なのに対し、この図解は、取得の原因ごとに『承継（いつ移るか）』と『対抗（第三者に主張できるか）』を1枚で見比べる早見表です。

- 図解1：承継と対抗は別の話（遺産分割・『相続させる』遺言・特定遺贈）
  - 型：対比表型（2列・3行）＋別の問いのカード
  - サイズ：1080×1900
  - 保存名：図解1_承継と対抗は別の話.png
  - 記事の挿入位置：【M3-4】の『中身の整理』の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：承継と対抗は別の話（遺産分割・『相続させる』遺言・特定遺贈）

- 型：対比表型（2列・3行）＋別の問いのカード　／　サイズ：1080×1900　／　保存名：`図解1_承継と対抗は別の話.png`
- 記事の挿入位置：【M3-4】の『中身の整理』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a two-column comparison table poster (対比表型) with a separate small card below it.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「承継と対抗は別の話」
「登記が要る場面を分ける」
Subtitle (smaller, centered, 1 line):
「民法 第177条・第899条の2・第909条・第258条の2」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header 「承継：いつ自分のものになる？」 with a small light-gray tag 「権利が移る話」; the third header 「対抗：第三者に主張できる？」 with a small light-gray tag 「登記の話」. The two headers are NOT identical; copy each one exactly as given.
Data row 1 (row label cell, dark navy, white text: 「遺産分割で取得」): second column 「相続開始の時にさかのぼって効力が生じる。ただし、第三者の権利は害せない（民法909条）」; third column 「法定相続分を超える部分は、登記などの対抗要件が必要（民法899条の2）」.
Data row 2 (row label cell, dark navy, white text: 「『相続させる』遺言で取得」): second column 「遺産分割方法の指定と解され、協議や審判を経ず、死亡と同時に承継される」; third column 「法定相続分を超える部分は、遺言でも、登記などの対抗要件が必要（民法899条の2）」.
Data row 3 (row label cell, dark navy, white text: 「特定遺贈で取得」): second column 「遺言という意思表示による個別の権利移転」; third column 「登記がなければ、相続人の債権者に対抗できない（民法177条）」.
In every cell of the third column the words 「登記」 have a pale yellow highlighter marker. Every cell has its own text exactly as given; no two cells share the same text.
--- SEPARATE CARD (a single rounded card placed under the table with a clear gap, NOT part of the table; this is the last element of the poster) ---
Card heading (dark navy, one line): 「別の問い：遺産共有の分け方」
Card body, two short lines: 「共有物分割ではなく、遺産分割で分ける（民法258条の2第1項）」 and 「相続開始から10年を経過すると、共有物分割ができる例外がある（同条2項）」.
At the very bottom of the card, one small light-gray tag: 「承継と対抗は、別々に問われる」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 債, 効, 対, 張, 承, 抗, 権, 物, 登, 解, 記, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows with the two headers 承継：いつ自分のものになる？ and 対抗：第三者に主張できる？ in this order, that the separate card below it is the last element, that every cell reads exactly as given, and that no check mark, cross mark, blue or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- [ ] 表が3列（行の見出し＋2つの列）・3行で、列の見出しが左から『承継：いつ自分のものになる？』『対抗：第三者に主張できる？』の順になっている
- [ ] 各セルの文字がプロンプトと一字一句同じ（『民法909条』『民法899条の2』『民法177条』『死亡と同時に承継される』など）。2列目と3列目の文が入れ替わっていない
- [ ] 右の列のセルの『登記』の文字だけに黄色のマーカーがある。○×・青・赤が一つもない
- [ ] 表の下に、表とは分かれた小さなカード（『別の問い：遺産共有の分け方』）が1枚だけあり、その下には何もない
- [ ] 簡体字・繁体字・英字・ハングルの混入がない。背景が不透明（透過・チェッカーボードなし）

## 記事・条文との照合（設計メモ）

- 法定相続分を超える承継は、遺産分割によるかどうかにかかわらず、登記などの対抗要件がなければ第三者に対抗できない（民法899条の2第1項。記事【M3-4】中身の整理、H18-Q03オ）。総合記事の結論は『遺産分割でも遺言でも』
- 遺産分割は相続開始にさかのぼるが、第三者の権利は害せない（民法909条。法令DB `note-articles/laws/minpou-3-shinzoku-souzoku.md` で確認。記事【M3-4】中身の整理）
- 特定遺贈は遺言という意思表示による個別の権利移転で、通常の物権変動と同様に対抗要件主義（民法177条）に服する（H18-Q03エ）
- 『相続させる』遺言は、遺贈と解すべき特段の事情がなければ遺産分割方法の指定と解され、協議や審判を待たず死亡と同時に承継される（R03-Q03オ）。承継の話であり、対抗の話とは別（記事の言い方）
- 遺産共有の分け方：共有物分割ではなく遺産分割（民法258条の2第1項）。相続開始から10年を経過すると共有物分割ができるが、遺産分割の請求があり異議の申出があれば別（同条2項。法令DB `note-articles/laws/minpou-1-soukyoku-bukken.md` で確認）。図は例外の存在だけを小さく添えた
