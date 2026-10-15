# 【M2-1】共有者の一人は、単独で何ができ、何ができないのか　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M2-1】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：共有者の一人にできること（相手と請求の中身で決まる）
  - 型：フローチャート型　／　サイズ：1080×2100　／　保存名：`図解1_共有者の一人にできること.png`
  - 記事の挿入位置：【M2-1】の「判断のしかた」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：共有者の一人にできること（相手と請求の中身で決まる）

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー) read from top to bottom.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「共有者の一人にできること」
「相手と請求の中身で決まる」
Subtitle (smaller, centered, 1 line):
「民法 第252条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 2. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 sits on the center line directly below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy, white text): 「共有物をめぐる請求を考える」
NODE DIAMOND 1: 「請求する相手は、第三者か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 1 with the RED label 「いいえ」.
NODE RESULT 1 (red box, at the right of DIAMOND 1): 「相手は、ほかの共有者」 on the first line, 「相手にも持分に基づく使用の権原がある」 on the second and third lines, and 「持分の過半数でも、直ちには明渡しを請求できない」 on the next lines.
Under RESULT 1, a small light-gray tag attached to the box: 「特別の影響を及ぼす決定には承諾が必要（252条3項）」.
NODE DIAMOND 2: 「請求の中身は、守る請求（明渡し）か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to RESULT 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 2 (blue box, on the center line below DIAMOND 2): 「保存行為（民法252条5項）」 on the first line and 「各共有者が単独で、共有物の全部を請求できる」 on the next two lines.
NODE RESULT 3 (red box, at the right of DIAMOND 2): 「お金の請求（損害賠償）」 on the first line, 「請求権は持分に応じて分かれる」 on the second line, and 「請求できるのは自分の持分割合まで」 on the next lines.
Under RESULT 3, a small light-gray tag attached to the box: 「例：持分3分の1で損害90万円なら、30万円まで」.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another. RESULT 2 is the last element of the poster.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 保, 承, 権, 渡, 物, 請, 諾, 過; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 2 is blue and RESULT 1 and RESULT 3 are red, that the two small light-gray tags are attached to RESULT 1 and RESULT 3, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`図解1_共有者の一人にできること.png`

## 検品チェック

- ひし形が2つ（「請求する相手は、第三者か？」「請求の中身は、守る請求（明渡し）か？」）で、各ひし形に青の「はい」と赤の「いいえ」が付いているか。
- 結果の箱が3つ（青1つ＝保存行為、赤2つ＝相手が共有者、お金の請求）で、箱の文字が指定どおりか。小さな灰色のタグが赤い箱の2つに付いているか。
- 最後の要素（保存行為の青い箱）のあとに、まとめ・トロフィー・追加の文字ブロックが描かれていないか。
- 条番号は「252条3項」「民法252条5項」の2つだけか。簡体字・余計な文字・透過・図番がないか。