# 【M1-8】条件：成就の時はいつ効力が生じ、既成条件はどうなるのか　図解インフォグラフィック プロンプト（1枚）

民法編の総合記事（`note-articles/column/sokatsu-01-minpou.md`）の【M1-8】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、はい＝青、いいえ＝赤、中立＝濃紺です。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。キャラクターは描かないので、参照画像は不要です。契約の時に条件の成否がすでに確定していた場合は、成就が確定していたとき（131条1項）と不成就が確定していたとき（131条2項）を分けて描いています。

- 図解1：条件：成就の時はいつ効力が生じ、既成条件はどうなるのか
  - 型：フローチャート型（契約の時に確定していたか→成就か不成就か→停止条件か、の判定）
  - サイズ：1080×2300
  - 保存名：`図解_M1-8_条件の効力の判定フロー.png`
  - 記事の挿入位置：総合記事 sokatsu-01-minpou.md の【M1-8】の「判断のしかた」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：条件：成就の時はいつ効力が生じ、既成条件はどうなるのか

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定フロー).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「条件の効力はいつ生じる？」
「契約の時の条件の状態で分ける」
Subtitle (smaller, centered, 1 line):
「民法 第127条・第131条」
--- FLOWCHART ---
Layout (4 rows): ROW 1 = the START node, centered. ROW 2 = DIAMOND 1, centered. ROW 3 = DIAMOND 2 in the left half and DIAMOND 3 in the right half, at least 100 px apart. ROW 4 = DIAMOND 4 (far left) and DIAMOND 5 (center-left) below DIAMOND 2, and RESULT A and RESULT B (right side, side by side) below DIAMOND 3. ROW 5 (bottom row) = four result boxes RESULT 1, RESULT 2, RESULT 3, RESULT 4 from left to right, each about 230 px wide with a gap of at least 20 px; RESULT 1 and RESULT 2 sit under DIAMOND 4, and RESULT 3 and RESULT 4 sit under DIAMOND 5. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「条件付きの法律行為」
NODE DIAMOND 1: 「契約の時に、条件の成否はすでに確定していたか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down-left to DIAMOND 2 with the BLUE label 「はい」.
  - Arrow down-right to DIAMOND 3 with the RED label 「いいえ」.
NODE DIAMOND 2: 「確定していたのは、成就か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down-left to DIAMOND 4 with the BLUE label 「はい（成就）」.
  - Arrow down-right to DIAMOND 5 with the RED label 「いいえ（不成就）」.
NODE DIAMOND 3: 「その条件は、停止条件か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down-left to RESULT A with the BLUE label 「はい」.
  - Arrow down-right to RESULT B with the RED label 「いいえ」.
NODE DIAMOND 4: 「その条件は、停止条件か？」 The text is placed inside the diamond on 2 lines. The text of DIAMOND 3, DIAMOND 4 and DIAMOND 5 is the same on purpose; draw the same string in all three.
  - Arrow down-left to RESULT 1 with the BLUE label 「はい」.
  - Arrow down-right to RESULT 2 with the RED label 「いいえ」.
NODE DIAMOND 5: 「その条件は、停止条件か？」 The text is placed inside the diamond on 2 lines.
  - Arrow down-left to RESULT 3 with the BLUE label 「はい」.
  - Arrow down-right to RESULT 4 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「無条件」 on the first line and 「（有効）」 on the second line, with a small light-gray tag 「131条1項」 under the text.
NODE RESULT 2 (red box): 「無効」 on the first line, with a small light-gray tag 「131条1項」 under the text.
NODE RESULT 3 (red box): 「無効」 on the first line, with a small light-gray tag 「131条2項」 under the text.
NODE RESULT 4 (blue box): 「無条件」 on the first line and 「（有効）」 on the second line, with a small light-gray tag 「131条2項」 under the text.
NODE RESULT A (blue box): 「成就した時から」 on the first line, 「効力を生ずる」 on the second line and 「（知った時ではない）」 on the third line, with a small light-gray tag 「127条1項」 under the text.
NODE RESULT B (red box): 「成就した時から」 on the first line, 「効力を失う」 on the second line and 「（知った時ではない）」 on the third line, with a small light-gray tag 「127条2項」 under the text.
Counts: 1 start node, 5 diamonds, 6 result boxes (RESULT 1 to RESULT 4 and RESULT A, RESULT B), 6 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. RESULT 1 and RESULT 4 have the same text and RESULT 2 and RESULT 3 have the same text on purpose, but they differ in the tag (131条1項 or 131条2項); RESULT A and RESULT B differ in the words 「効力を生ずる」 and 「効力を失う」; do not copy one into the other. Do not draw any loop arrow and do not add any other node.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 無; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 5 diamonds and 6 result boxes, that every diamond shows a blue 「はい」 and a red 「いいえ」 (DIAMOND 2 shows 「はい（成就）」 and 「いいえ（不成就）」), that RESULT 1, RESULT 4 and RESULT A are blue and RESULT 2, RESULT 3 and RESULT B are red, that RESULT 1 to RESULT 4 are in this order from left to right, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`図解_M1-8_条件の効力の判定フロー.png`

検品チェック：
- ひし形が5つ、結果の箱が6つ、開始が1つで、下段の4つの箱が左から順に「無条件（有効）」「無効」「無効」「無条件（有効）」（131条1項・1項・2項・2項）、右側の2つの箱が「効力を生ずる」「効力を失う」（127条1項・2項）になっている
- すべてのひし形の出口が「はい」（青）と「いいえ」（赤）で、矢印が交差していない
- 文字が簡体字・繁体字になっていない（特に 条・停・止・効・無・成・就）
- 背景が透過していない
- 結果の箱の下に、まとめの枠・トロフィー・○×の再掲が描かれていない
- 画像の中に図の番号・問題番号・年度がない
