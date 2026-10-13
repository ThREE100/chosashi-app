# 総合記事②不動産登記法編 第3章　図解インフォグラフィック プロンプト（【PC-8】地積測量図の訂正・閉鎖・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表が中心の図は、青・赤・チェック・バツを使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。はい／いいえの判定の流れ図だけ、共通部品の配色の規則（青＝はい、赤＝いいえ）で描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解11 | 地積測量図の誤りの直し方（判定の流れ） | 判定の流れ図型 | 1080×2500 | 不登法第3章_図解11_地積測量図の誤りの直し方.png | 【PC-8】『中身の整理』の直後 |
| 図解12 | 図面が閉鎖されるとき | 対比カード型（2列） | 1080×2100 | 不登法第3章_図解12_図面が閉鎖されるとき.png | 【PC-8】『たとえば』の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解11：地積測量図の誤りの直し方（判定の流れ）

- 型：判定の流れ図型　／　サイズ：1080×2500　／　保存名：`不登法第3章_図解11_地積測量図の誤りの直し方.png`
- 記事の挿入位置：【PC-8】『中身の整理』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「地積測量図の誤りの直し方」
「上から順に確かめる」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第88条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit side by side below DIAMOND 1, one to the left and one to the right of the center line, with at least 60 px of empty space between them so that the arrow labels stay visible. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「地積測量図に誤りがある」
NODE DIAMOND 1: 「表題部の更正の登記ができる誤りか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down-left to RESULT 1 with the BLUE label 「はい」.
  - Arrow down-right to RESULT 2 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「更正の登記で直す」 on the first line and 「訂正の申出はできない」 on the second line, with the small gray tag 「規則88条1項ただし書」.
NODE RESULT 2 (red box): 「訂正の申出で直す」 on the first line and 「訂正後の図面を提供する」 on the second line, with the small gray tag 「規則88条2項」.
Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts; do not copy one into the other.
--- COMPARISON CARD (below the flowchart, a wide card with a dashed dark navy outline and a small dark navy tag 「地積に錯誤があるとき」) ---
Heading 「更正の登記と併せて申し出るか」, then two body lines: 「地図の訂正の申出：併せて申し出る（規則16条2項）」 and 「地積測量図の訂正の申出：併せる義務はない（規則88条3項で準用されない）」. Neutral dark navy outlines only; no blue and no red in this card.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that the comparison card below is neutral dark navy, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解12：図面が閉鎖されるとき

- 型：対比カード型（2列）　／　サイズ：1080×2100　／　保存名：`不登法第3章_図解12_図面が閉鎖されるとき.png`
- 記事の挿入位置：【PC-8】『たとえば』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards and one wide band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「図面が閉鎖されるとき」
「限られた場合だけ」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第85条・第87条」
--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「規則85条2項」, heading 「土地所在図・地積測量図・建物図面・各階平面図」, and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「変更後・更正後の図面がある変更の登記・更正の登記をしたとき」, 「滅失の登記・表題部の抹消をしたとき」, 「換地処分の登記をしたとき」.
Right card: small tag 「規則87条1項」, heading 「地役権図面」, and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「地役権の登記の抹消をしたとき」, 「地役権図面を添付情報とする分筆・合筆・変更・更正の登記をしたとき」.
The two cards have clearly different texts; the texts are NOT identical.
Under the two cards, one wide dark navy band with large white text 「合筆の登記だけでは、地積測量図は閉鎖されない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 所, 権, 物, 登, 規, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards with exactly three item lines in the left card and exactly two item lines in the right card, followed by one band, that the two card headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
