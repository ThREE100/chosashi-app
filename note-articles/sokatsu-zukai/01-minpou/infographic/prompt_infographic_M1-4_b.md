# 【M1-4】錯誤・詐欺による取消し：追加の図解「取り消せるか、対抗できるか」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-4】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-4.md`）はカード4枚の個別の整理なので、第三者が取消しの前に現れるという時の流れと、「取消しの可否」「第三者への対抗の可否」の2つの問いを、1枚の関係図で補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図ははい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：取り消せるか、対抗できるか（詐欺の取消しと第三者の関係図）
  - 型：関係図型（時の流れ＋結果カード2枚）　／　サイズ：1080×2200　／　保存名：`民法編1_M1-4_追加_取り消せるか対抗できるか.png`
  - 記事の挿入位置：【M1-4】の「たとえば」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：取り消せるか、対抗できるか（詐欺の取消しと第三者の関係図）

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a timeline-and-relationship poster: a horizontal timeline with three milestones, two result cards side by side, one note card and one closing band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「取り消せるか、対抗できるか」
「詐欺では二つの問いを分ける」
Subtitle (smaller, centered, 1 line):
「民法 第96条」
--- TIMELINE (a wide rounded white panel directly below the header, dark navy outline) ---
A single horizontal dark navy arrow runs left to right across the panel, with exactly three round milestone dots on it, each with a one-line label under the dot, in this order from left to right: 「詐欺による売買」, 「転売」, 「取消し」.
Above the first milestone: two faceless person pictograms side by side with the dark navy name tags 「だまされた売主」 and 「だました買主」.
Above the second milestone: one faceless person pictogram holding a small shield, with the dark navy name tag 「善意でかつ過失のない第三者」 and a small gray tag 「転得者・抵当権者など」 under the name tag.
Above the third milestone: a rubber stamp icon labeled 「取消し」.
--- TWO RESULT CARDS (directly below the timeline, side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: a small dark navy tag 「売主と買主の間では」, the heading (bold) 「取り消せる」, and a small gray tag 「96条1項」.
Right card: a small dark navy tag 「第三者に対しては」, the heading (bold) 「対抗できない」, a small gray tag 「96条3項」, and one body line 「第三者は、登記がなくても守られる（判例）」.
The two cards have clearly different texts; the texts are NOT identical, so copy each exactly as given.
--- NOTE CARD (a wide rounded card below the two result cards, pale gray fill, dark navy outline, with NO arrow) ---
Heading (bold, ONE line): 「錯誤による取消しも、第三者の保護は同じ」.
Body (ONE line): 「善意でかつ過失がない第三者に対抗できない」 with the small gray tag 「95条4項」.
--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below the note card) ---
「取消しができることと、」 on the first line and 「第三者に対抗できないことは別の問い」 on the second line.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 売, 対, 当, 抗, 抵, 権, 欺, 登, 記, 詐, 買, 過, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the timeline has exactly 3 milestones in the order 詐欺による売買, 転売, 取消し, that the third-party pictogram is above the second milestone (before the cancellation), that there are exactly 2 result cards side by side, exactly 1 note card and exactly 1 closing band in this order, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-4_追加_取り消せるか対抗できるか.png`

## 検品チェック

- 時の流れの上の里程標が3つ（詐欺による売買・転売・取消し）で、第三者の人物が「転売」の上（取消しより前）に描かれているか。
- 結果のカードが左右2枚（取り消せる／対抗できない）で、右のカードに「第三者は、登記がなくても守られる（判例）」があるか。条番号（96条1項・96条3項・95条4項）が指定どおりか。
- 注記のカード1枚、濃紺の帯1つの順で終わり、そのあとに何も描かれていないか。
- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。