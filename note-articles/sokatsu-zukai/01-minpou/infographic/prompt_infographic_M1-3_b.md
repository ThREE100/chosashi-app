# 【M1-3】心裡留保・虚偽表示：追加の図解「仮装売買の登場人物」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-3】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-3.md`）は判定の流れ図なので、転得者と相続人が「元の所有者」「仮装の買主」とどういう関係にあるかを、当事者関係図で補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は関係図で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの番号1・2は図の部品です）。キャラクターは描きません。

- 図解1：仮装売買の登場人物（だれが第三者になるか）
  - 型：関係図型（シナリオカード2枚＋帯）　／　サイズ：1080×2100　／　保存名：`民法編1_M1-3_追加_仮装売買の登場人物.png`
  - 記事の挿入位置：【M1-3】の「たとえば」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：仮装売買の登場人物（だれが第三者になるか）

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a relationship-diagram poster with two scenario cards stacked in one column and one closing band; every card draws three faceless person pictograms in a row.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「仮装売買の登場人物」
「だれが「第三者」になるか」
Subtitle (smaller, centered, 1 line):
「民法 第94条2項」
--- SCENARIO CARD 1 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 1) ---
Heading (bold, ONE line): 「仮装の買主が、他の人に転売した」.
Diagram (three faceless person pictograms in one row, left to right):
  - Left pictogram with the dark navy name tag 「元の所有者」.
  - Middle pictogram with the dark navy name tag 「仮装の買主」. Between the left and middle pictograms, a dotted double-headed arrow with the label 「通じて仮装売買」 and a small gray tag 「無効」 under it.
  - Right pictogram with the dark navy name tag 「転得者（善意）」, holding a small shield. A solid dark navy arrow runs from the middle pictogram to the right pictogram with the label 「転売」. Under the right pictogram, a small registry ledger icon with the label 「登記がなくても守られる（判例）」.
Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence): 「第三者として守られる」, with the small gray tag 「94条2項」 beside it.
--- SCENARIO CARD 2 (a wide rounded card below scenario card 1, same style; badge: a filled dark navy circle containing the number 2) ---
Heading (bold, ONE line): 「仮装の買主が死亡し、子が単独で相続した」.
Diagram (three faceless person pictograms in one row, left to right):
  - Left pictogram with the dark navy name tag 「元の所有者」.
  - Middle pictogram drawn with a thin dotted outline (faded) with the dark navy name tag 「仮装の買主」 and a small gray tag 「死亡」. Between the left and middle pictograms, a dotted double-headed arrow with the label 「通じて仮装売買」.
  - Right pictogram with the dark navy name tag 「子（相続人）」. A solid dark navy arrow runs from the middle pictogram to the right pictogram with the label 「相続」. One thin dark navy bracket encloses the middle and right pictograms together, with the label 「買主の地位を、まるごと引き継ぐ」.
Under the diagram, one small dotted-outline tag (no check mark, no cross): 「善意でも、第三者ではない」.
Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence): 「第三者に当たらない」, with the small gray tag 「896条」 beside it.
The two scenario cards use the same three-pictogram layout and the same name tag 「元の所有者」 on purpose, but their headings, the right-hand name tags and the conclusion tags are different texts; copy each exactly as given.
--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below scenario card 2) ---
「新たに独立の利害関係をもった者だけが、」 on the first line and 「善意の第三者として守られる」 on the second line.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 地, 売, 当, 所, 無, 物, 登, 記, 買; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 2 scenario cards followed by exactly 1 closing band, that each card has exactly 3 person pictograms in one row, that card 1 shows the right-hand name tag 転得者（善意） and card 2 shows the right-hand name tag 子（相続人）, that the middle pictogram of card 2 is faded with the tag 死亡, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-3_追加_仮装売買の登場人物.png`

## 検品チェック

- シナリオのカードがちょうど2枚で、それぞれに人物のピクトグラムが3つ横に並んでいるか。カード1の右が「転得者（善意）」、カード2の右が「子（相続人）」か。
- カード2の中央（仮装の買主）が薄い点線の輪郭で「死亡」の札が付いているか。「相続」の矢印と、中央と右をまとめる括弧の文言（買主の地位を、まるごと引き継ぐ）があるか。
- 条番号（94条2項・896条）と、「登記がなくても守られる（判例）」が指定どおりか。濃紺の帯が最後に1つだけで、そのあとに何も描かれていないか。
- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。