# 総合記事② 不動産登記法編 第5章　図解インフォグラフィック プロンプト（【PE-2】建物の個数はどう決まるか（効用上一体・区分・附属建物の主従）・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。判定の流れ図（フローチャート）では、はい＝青・いいえ＝赤で描きます。分類・早見表・比較カードの図は、はい／いいえの分岐ではないため、青・赤を使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解3 | 一個の建物にできる？（数棟か、一棟の中かで見分ける） | 判定の流れ型（フローチャート） | 1080×2500 | 不動産登記法編⑤_図解3_一個の建物にできるか.png | 【PE-2】「中身の整理」の直後 |
| 図解4 | 抵当権があると、できない？（新築の附属建物と合併は別） | 対比カード型（2列） | 1080×1800 | 不動産登記法編⑤_図解4_新築の附属建物と合併.png | 【PE-2】「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解3：一個の建物にできる？（数棟か、一棟の中かで見分ける）

- 型：判定の流れ型（フローチャート）　／　サイズ：1080×2500　／　保存名：`不動産登記法編⑤_図解3_一個の建物にできるか.png`
- 記事の挿入位置：【PE-2】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ) made of two sections.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「一個の建物にできる？」
「数棟か、一棟の中かで見分ける」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第78条」
--- FLOWCHART ---
Layout: two section panels stacked top to bottom, both the same size, each with a dashed dark navy outline and a small dark navy tag at its top left. In each panel there is ONE diamond placed at the left-center; the BLUE 「はい」 arrow goes straight down from the diamond to a blue result box directly below it; the RED 「いいえ」 arrow goes right from the diamond to a red result box on the same row, with at least 60 px of empty space between the diamond and the red box so that the arrow label stays visible. Arrows never cross.
A banner at the very top, below the header, in dark navy with white text: 「まず、数棟か、一棟の中の区分かを見分ける」.
SECTION 1 (tag 「数棟の建物」):
NODE DIAMOND 1: 「効用上一体として利用される状態か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down with the BLUE label 「はい」 to RESULT 1.
  - Arrow right with the RED label 「いいえ」 to RESULT 2.
NODE RESULT 1 (blue box): 「所有者の意思に反しない限り、一個の建物」 on the first two lines and the small tag 「準則78条1項」.
NODE RESULT 2 (red box): 「別々の建物」 on the first line and 「例：借主が別々の居宅の三棟」 on the second line.
SECTION 2 (tag 「一棟の建物の中の区分」):
NODE DIAMOND 2: 「所有者が同一か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down with the BLUE label 「はい」 to RESULT 3.
  - Arrow right with the RED label 「いいえ」 to RESULT 4.
NODE RESULT 3 (blue box): 「一棟の全部（離れていてもよい）又は隣接する数個の部分を、一個にできる」 on three lines, the small line 「所有者の意思に反しない限り」, and the small tag 「準則78条2項ただし書」.
NODE RESULT 4 (red box): 「各部分が、別々の一個の建物」 on two lines and the small tag 「同項本文」.
--- SIDE NOTE CARD (below the two sections, a wide card with a dashed dark navy outline) ---
Heading 「数棟を附属建物として一個にするには」, body 「主従の関係が前提（法2条23号）」.
Counts: 2 diamonds, 4 result boxes, 4 distinct paths. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue boxes and the two red boxes have different texts; do not copy one into another.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 号, 建, 所, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 2 diamonds and 4 result boxes, that each diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 3 are blue and RESULT 2 and RESULT 4 are red, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：抵当権があると、できない？（新築の附属建物と合併は別）

- 型：対比カード型（2列）　／　サイズ：1080×1800　／　保存名：`不動産登記法編⑤_図解4_新築の附属建物と合併.png`
- 記事の挿入位置：【PE-2】「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x1800 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「抵当権があると、できない？」
「新築の附属建物と、合併は別」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第56条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「法56条5号は働かない」, heading 「新築した建物を、附属建物にする」, and exactly 2 short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「主である建物の表題部の変更の登記で足りる」, 「主である建物に抵当権の登記があっても、妨げられない」.
Right card: small tag 「合併の制限がある」, heading 「既登記の建物どうしを、一つにする」, and exactly 2 short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「表題登記がある建物どうしを、一つにする」, 「権利に関する登記がある建物の合併を制限（法56条5号）」.
Highlighting: the string 「表題部の変更の登記で足りる」 in the left card and the string 「合併を制限」 in the right card have a pale yellow highlighter marker.
Cell and card text may wrap onto two or three lines: make every row and card tall enough that all of its text fits fully inside it, at least 24 px high, and nothing is cut off or overflows.
The two cards have clearly different texts; the texts are NOT identical.
Under the two cards, one wide dark navy band with large white text 「抵当権の制限が関係するのは、右の合併のほう」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 当, 抵, 権, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly 2 item lines and the right card has exactly 2 item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.  Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
