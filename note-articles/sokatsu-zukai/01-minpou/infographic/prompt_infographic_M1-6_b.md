# 【M1-6】取得時効：追加の図解「時効取得と登記の時間軸」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-6】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-6.md`）は判定の流れ図と早見表なので、時効の完成を境にした時間軸の上で、元の所有者・完成の前の第三者・完成の後の第三者がどこにいるかを示します。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図ははい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの番号1〜3は図の部品です）。キャラクターは描きません。

- 図解1：時効取得と登記：完成の前か後かの時間軸
  - 型：時間軸型（時間軸パネル＋カード3枚＋帯）　／　サイズ：1080×2300　／　保存名：`民法編1_M1-6_追加_時効取得と登記の時間軸.png`
  - 記事の挿入位置：【M1-6】の「中身の整理」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：時効取得と登記：完成の前か後かの時間軸

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a timeline poster: one wide timeline panel at the top followed by three numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the timeline panel. Every card has one heading, one mini timeline, one item line and one conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「時効取得と登記」
「時効の完成の前か後かで決まる」
Subtitle (smaller, centered, 1 line):
「民法 第162条（判例の考え方）」
--- TIMELINE PANEL (a wide rounded white panel directly below the header, dark navy outline) ---
A single horizontal dark navy arrow runs left to right across the panel with exactly three milestone flags on it, each with a one-line label under the flag, in this order: 「占有の開始」, 「時効の完成」, 「時効取得を主張する」.
The segment between the first and second flags has the bracket label 「完成の前」; the segment between the second and third flags has the bracket label 「完成の後」.
At the far left above the arrow: a faceless person pictogram with the dark navy name tag 「占有者」. Above the first segment: a small pin and a faceless person pictogram with the name tag 「第三者」 and the label 「所有権を得た」. Above the second segment: another pin and a faceless person pictogram with the name tag 「第三者」 and the label 「所有権を得た」. The two 「第三者」 pictograms are the same text on purpose; draw the same string in both.
Below the arrow, spanning its whole length (under all three flag labels, with at least 20 px of space), one thin dotted bracket with a faceless person pictogram at its left end with the dark navy name tag 「元の所有者」.
--- CARD 1 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 1, numbers run 1 to 3 in order) ---
Heading (bold, ONE line):
「元の所有者に対して」
Mini timeline at the left of the card: a short horizontal dark navy line with one small flag labeled 「完成」 at its middle; no pin on it, and one faceless person pictogram with the dark navy name tag 「元の所有者」 beside the mini timeline.
Item line (one short line of dark navy text with a small dark navy dot at its left end, NO number on the dot):
「時効の当事者で、対抗関係に立たない」
Conclusion tag (a short pale-yellow banner directly below the item line, a keyword phrase, not a sentence):
「登記なしで主張できる」
--- CARD 2 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 2, numbers run 1 to 3 in order) ---
Heading (bold, ONE line):
「完成の前の第三者に対して」
Mini timeline at the left of the card: a short horizontal dark navy line with one small flag labeled 「完成」 at its middle; a small pin is placed on the left of the 完成 flag.
Item line (one short line of dark navy text with a small dark navy dot at its left end, NO number on the dot):
「元の所有者と同じ立場（当事者類似）」
Conclusion tag (a short pale-yellow banner directly below the item line, a keyword phrase, not a sentence):
「登記なしで主張できる」
Small gray tag under the conclusion tag: 「判例の考え方」.
--- CARD 3 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 3, numbers run 1 to 3 in order) ---
Heading (bold, ONE line):
「完成の後の第三者に対して」
Mini timeline at the left of the card: a short horizontal dark navy line with one small flag labeled 「完成」 at its middle; a small pin is placed on the right of the 完成 flag.
Item line (one short line of dark navy text with a small dark navy dot at its left end, NO number on the dot):
「第三者との間で対抗関係に立つ」
Conclusion tag (a short pale-yellow banner directly below the item line, a keyword phrase, not a sentence):
「登記の先後で決まる」
Small gray tag under the conclusion tag: 「判例の考え方」.
The conclusion tag 「登記なしで主張できる」 appears in both CARD 1 and CARD 2 on purpose; the headings, item lines and mini timelines of the three cards are different, so copy each exactly as given.
--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below card 3) ---
「相手と、第三者が所有権を得た時点で」 on the first line and 「登記が要るかが決まる」 on the second line.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 占, 対, 張, 当, 所, 抗, 権, 登, 記, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the timeline panel has exactly 3 flags in the order 占有の開始, 時効の完成, 時効取得を主張する, with the labels 完成の前 and 完成の後 on the two segments, that there are exactly 3 numbered cards followed by exactly 1 closing band, that the mini timeline pin is absent in card 1, on the left of the flag in card 2 and on the right of the flag in card 3, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-6_追加_時効取得と登記の時間軸.png`

## 検品チェック

- 時間軸パネルの旗が3つ（占有の開始・時効の完成・時効取得を主張する）で、2つの区間に「完成の前」「完成の後」の括弧があるか。第三者の人物が2人（区間ごとに1人）描かれているか。
- カードがちょうど3枚で、ミニ時間軸の目印（ピン）が、カード1はなし、カード2は完成の旗の左、カード3は右か。
- 「登記なしで主張できる」がカード1とカード2にあり、カード3は「登記の先後で決まる」か。カード2・3に「判例の考え方」の札があるか。
- 濃紺の帯が最後に1つだけで、そのあとに何も描かれていないか。青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。