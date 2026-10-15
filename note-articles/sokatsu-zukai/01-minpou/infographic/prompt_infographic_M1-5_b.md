# 【M1-5】代理権の濫用と無権代理の相続：追加の図解「地位はだれに集まるか」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-5】に追加で差し込む図解のプロンプトです。既存の図解2（`prompt_infographic_M1-5.md`）は判定の流れ図なので、「本人の地位」と「無権代理人の地位」がだれに移るかを、4つの場面の関係図で補います（無権代理人の地位を共同相続した後に本人の地位を単独承継する場面は、既存の図では小さな注記だけでした）。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は関係図で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの番号1〜4は図の部品です）。キャラクターは描きません。

- 図解1：無権代理と相続：地位はだれに集まるか（4つの場面の関係図）
  - 型：関係図型（シナリオカード4枚）　／　サイズ：1080×2600　／　保存名：`民法編1_M1-5_追加_地位はだれに集まるか.png`
  - 記事の挿入位置：【M1-5】の「たとえば」の直後（図解2の判定フローの次）

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：無権代理と相続：地位はだれに集まるか（4つの場面の関係図）

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a relationship-diagram poster with four scenario cards stacked in one column, each drawing who inherits which position; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the person pictograms, arrows and short labels plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「無権代理と相続」
「地位はだれに集まるか」
Subtitle (smaller, centered, 1 line):
「民法 第113条1項（判例の考え方）」
--- SCENARIO CARD 1 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 1, numbers run 1 to 4 in order) ---
Heading (bold, ONE line):
「無権代理人が、本人を単独で相続した」
Diagram: Two faceless person pictograms in one row. Left: a pictogram drawn with a thin dotted outline (faded) with the dark navy name tag 「本人」 and a small gray tag 「死亡」. Right: a pictogram with the dark navy name tag 「無権代理人」. A solid dark navy arrow runs from the left to the right with the label 「相続」. Above the right pictogram, two small round badges are stacked together on the same person: 「本人の地位」 and 「無権代理人の地位」.
Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence):
「二つの地位が融合する」
--- SCENARIO CARD 2 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 2, numbers run 1 to 4 in order) ---
Heading (bold, ONE line):
「無権代理人が、他の相続人とともに本人を相続した」
Diagram: Three faceless person pictograms. Left: a faded pictogram (thin dotted outline) with the dark navy name tag 「本人」 and a small gray tag 「死亡」. Right, one above the other: a pictogram with the dark navy name tag 「無権代理人」 and a pictogram with the dark navy name tag 「他の相続人」. Two solid dark navy arrows run from the left pictogram to each of the two right pictograms with the label 「共同相続」. A thin bracket encloses the two right pictograms with the label 「追認は全員でする」.
Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence):
「全員で追認を拒絶できる」
--- SCENARIO CARD 3 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 3, numbers run 1 to 4 in order) ---
Heading (bold, ONE line):
「本人が追認を拒絶したあとに、無権代理人が相続した」
Diagram: Two faceless person pictograms in one row. Left: a faded pictogram (thin dotted outline) with the dark navy name tag 「本人」 and a small gray tag 「死亡」; in front of it a paper sheet labeled 「追認拒絶」 with a closed padlock icon, placed before the arrow. Right: a pictogram with the dark navy name tag 「無権代理人」. A solid dark navy arrow runs from the left to the right with the label 「相続」.
Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence):
「拒絶は確定している」
--- SCENARIO CARD 4 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 4, numbers run 1 to 4 in order) ---
Heading (bold, ONE line):
「無権代理人の地位を共同相続したあと、本人の地位も単独で承継した」
Diagram: Four faceless person pictograms. At the top left, a faded pictogram (thin dotted outline) with the dark navy name tag 「無権代理人」 and a small gray tag 「死亡」; at the bottom left, a faded pictogram with the dark navy name tag 「本人」 and a small gray tag 「死亡」. At the right, one above the other: a pictogram with the dark navy name tag 「承継した者」 and a pictogram with the dark navy name tag 「他の共同相続人」. From the top-left faded pictogram, two solid arrows labeled 「共同相続」 go to both right pictograms. From the bottom-left faded pictogram, one solid arrow labeled 「単独で承継」 goes only to the 「承継した者」 pictogram. Above the 「承継した者」 pictogram, two small round badges are stacked together: 「無権代理人の地位」 and 「本人の地位」.
Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence):
「両方の地位が一人に集まる」
The four conclusion tags are four different texts; copy each exactly as given and do not copy one into another.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 地, 承, 権, 無, 認; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of scenario cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, that there is no intro illustration or paragraph block between the header and the cards, that no card contains a full sentence of explanatory prose, that the deceased persons are drawn faded with a thin dotted outline, and that no check mark, cross mark, blue or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-5_追加_地位はだれに集まるか.png`

## 検品チェック

- カードがちょうど4枚で、番号が1〜4の順か。死亡した人物が薄い点線の輪郭で描かれ、「死亡」の札が付いているか。
- カード1は「本人の地位」「無権代理人の地位」の2つの丸札が同じ人物に重なっているか。カード2は相続人が2人で、括弧の文言が「追認は全員でする」か。
- カード3は「追認拒絶」の札と南京錠が、相続の矢印の手前にあるか。カード4は「共同相続」の矢印が2本、「単独で承継」の矢印が1本（承継した者へだけ）か。
- 導入のイラスト・文章の段落・まとめの帯が、カードの前後に描かれていないか。青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。