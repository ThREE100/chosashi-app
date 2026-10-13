# 【M1-8】条件：成就の時はいつ効力が生じ、既成条件はどうなるのか　図解インフォグラフィック プロンプト（1枚）

民法編の総合記事（`note-articles/column/sokatsu-01-minpou.md`）の【M1-8】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、はい＝青、いいえ＝赤、中立＝濃紺です。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。キャラクターは描かないので、参照画像は不要です。なお、条件が成就しないことが契約の時にすでに確定していた場合（民法131条2項。停止条件は無効、解除条件は無条件）は、結論を決める肢がなく図が複雑になるため、この図には入れていません。

- 図解1：条件：成就の時はいつ効力が生じ、既成条件はどうなるのか
  - 型：フローチャート型（契約の時にすでに成就→停止条件か、の2段の判定）
  - サイズ：1080×2000
  - 保存名：`図解_M1-8_条件の効力の判定フロー.png`
  - 記事の挿入位置：総合記事 sokatsu-01-minpou.md の【M1-8】の「判断のしかた」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：条件：成就の時はいつ効力が生じ、既成条件はどうなるのか

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「条件の効力はいつ生じる？」
「契約の時にすでに成就していたか」
Subtitle (smaller, centered, 1 line):
「民法 第127条・第131条」
--- FLOWCHART ---
Layout: the START node and DIAMOND 1 sit on one vertical center line at the top. Below DIAMOND 1 the flow splits into a LEFT branch and a RIGHT branch: DIAMOND 2 is placed in the left half, DIAMOND 3 in the right half, on the same row, at least 100 px apart. Below them, on one bottom row, the four result boxes sit side by side from left to right in this order: RESULT 1, RESULT 2, RESULT 3, RESULT 4, each about 230 px wide with a gap of at least 20 px. RESULT 1 and RESULT 2 are the two exits of DIAMOND 2, and RESULT 3 and RESULT 4 are the two exits of DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「条件付きの法律行為」
NODE DIAMOND 1: 「条件は、契約の時にすでに成就していたか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down-left to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow down-right to DIAMOND 3 with the RED label 「いいえ」.
NODE DIAMOND 2: 「その条件は、停止条件か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down-left to RESULT 1 with the BLUE label 「はい」.
  - Arrow down-right to RESULT 2 with the RED label 「いいえ」.
NODE DIAMOND 3: 「その条件は、停止条件か？」 The text is placed inside the diamond on 2 lines. The text of DIAMOND 2 and the text of DIAMOND 3 are the same on purpose; draw the same string in both.
  - Arrow down-left to RESULT 3 with the BLUE label 「はい」.
  - Arrow down-right to RESULT 4 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「無条件」 on the first line and 「（有効）」 on the second line, with a small light-gray tag 「131条1項」 under the text.
NODE RESULT 2 (red box): 「無効」 on the first line, with a small light-gray tag 「131条1項」 under the text.
NODE RESULT 3 (blue box): 「成就した時から」 on the first line, 「効力を生ずる」 on the second line and 「（知った時ではない）」 on the third line, with a small light-gray tag 「127条1項」 under the text.
NODE RESULT 4 (red box): 「成就した時から」 on the first line, 「効力を失う」 on the second line and 「（知った時ではない）」 on the third line, with a small light-gray tag 「127条2項」 under the text.
Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. RESULT 1 and RESULT 2 have different texts, and RESULT 3 and RESULT 4 differ in the words 「効力を生ずる」 and 「効力を失う」; do not copy one into the other. Do not draw any loop arrow and do not add any other node.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 無; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that every diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 3 are blue and RESULT 2 and RESULT 4 are red, that the four result boxes are in the order RESULT 1, RESULT 2, RESULT 3, RESULT 4 from left to right, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`図解_M1-8_条件の効力の判定フロー.png`

検品チェック：
- ひし形が3つ、結果の箱が4つ、開始が1つで、結果の箱が左から順に「無条件（有効）」「無効」「効力を生ずる」「効力を失う」になっている
- すべてのひし形の出口が「はい」（青）と「いいえ」（赤）で、矢印が交差していない
- 文字が簡体字・繁体字になっていない（特に 条・停・止・効・無・成・就）
- 背景が透過していない
- 結果の箱の下に、まとめの枠・トロフィー・○×の再掲が描かれていない
- 画像の中に図の番号・問題番号・年度がない
