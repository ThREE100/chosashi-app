# 【M2-4】占有の訴えの相手方と、本権との関係はどうなっているのか　追加の図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-4】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-4.md`＝4つの場面の早見表）は変更せず、表では文章の行になっている「占有回収の訴えの相手方は、奪った者本人か、特定承継人か。承継人なら侵奪の事実を知っていたか」という分かれ道を、記事の「判断のしかた」3（侵奪者が占有を失ったか、保ち続けているか）に沿って判定の流れで補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・個人の演習結果を入れません。キャラクターは描きません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 占有回収の訴えの相手方（奪った者か、その承継人か） | フローチャート型 | 1080×2300 | 民法編2_M2-4_追加_占有回収の訴えの相手方の分かれ道.png | 【M2-4】の「判断のしかた」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：占有回収の訴えの相手方（奪った者か、その承継人か）

- 型：フローチャート型　／　サイズ：1080×2300　／　保存名：`民法編2_M2-4_追加_占有回収の訴えの相手方の分かれ道.png`
- 記事の挿入位置：【M2-4】の「判断のしかた」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ) read from top to bottom.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「占有回収の訴えの相手方」
「奪った者か、その承継人か」
Subtitle (smaller, centered, 1 line):
「民法 第181条・第200条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 2. Every side result box (RESULT 1 and RESULT 3) sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 sits on the center line directly below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy, white text): 「占有を奪われた。誰を相手にするか」
NODE DIAMOND 1: 「相手は、奪った者本人か、特定承継人か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond is NOT a yes/no question, so its two exits use NEUTRAL DARK NAVY arrows and dark navy labels (no blue and no red on this diamond).
  - Arrow down to DIAMOND 2 with the dark navy label 「特定承継人」.
  - Arrow right to RESULT 1 with the dark navy label 「本人」.
NODE RESULT 1 (neutral box with a dark navy outline and a pale gray fill, NOT blue and NOT red, at the right of DIAMOND 1): 「奪った者本人には、回収の訴えを提起できる」 on the first lines, and 「目的物を貸しただけでも、貸主として間接占有を続けている」 on the next lines.
Under RESULT 1, a small light-gray tag attached to the box: 「民法181条」.
NODE DIAMOND 2: 「承継人は、侵奪の事実を知っていたか？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow down to RESULT 2 with the BLUE label 「はい」.
  - Arrow right to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 2 (blue box, on the center line below DIAMOND 2): 「承継人にも提起できる」 on the first line and 「ただし書：侵奪の事実を知っていたとき」 on the next lines.
NODE RESULT 3 (red box, at the right of DIAMOND 2): 「承継人には提起できない」 on the first line and 「原則：特定承継人に対しては不可」 on the next lines.
Under RESULT 3, a small light-gray tag attached to the box: 「民法200条2項」.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another. RESULT 2 is the last element of the poster.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 占, 対, 承, 物, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that DIAMOND 1 has dark navy labels 「特定承継人」 and 「本人」 and no blue or red, that DIAMOND 2 shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is a neutral dark navy outlined box, RESULT 2 is blue and RESULT 3 is red, that the two small light-gray tags are attached to RESULT 1 and RESULT 3, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- ひし形が2つ。1つ目（「相手は、奪った者本人か、特定承継人か？」）は、はい／いいえではないので濃紺の「特定承継人」「本人」の矢印で、青・赤を使っていないか。2つ目（「承継人は、侵奪の事実を知っていたか？」）には青の「はい」と赤の「いいえ」が付いているか。
- 結果の箱が3つ（濃紺の枠の中立の箱1つ＝奪った者本人、青1つ＝承継人にも提起できる、赤1つ＝承継人には提起できない）で、箱の文字が指定どおりか。小さな灰色のタグが中立の箱（民法181条）と赤い箱（民法200条2項）に付いているか。
- 最後の要素（青い箱）のあとに、まとめ・トロフィー・追加の文字ブロックが描かれていないか。
- 見出し・箱の文字を、上のコードブロックの文言と一字ずつ突き合わせた（「承継」「侵奪」「占有」「奪」「間接」「貸主」が簡体字・別字になっていない）。簡体字・余計な文字・透過・図番がない。

## 記事・条文との照合（作成者用）

- 民法200条2項（占有回収の訴えは、占有を侵奪した者の特定承継人に対して提起することができない。ただし、その承継人が侵奪の事実を知っていたときは、この限りでない）、181条（占有権は代理人によって取得できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。
- 「侵奪者が目的物を第三者に貸しただけなら、侵奪者は貸主として代理占有（間接占有）を続けており、なお相手方になる」は、記事の中身の整理・肢の判定による判例の整理で、条文に直接の記述はない（181条は代理占有の取得を定めるのみ）。図ではタグに民法181条とだけ添え、結論の断定は記事の範囲にとどめた。
- 1つ目のひし形は「本人か、承継人か」という二択で、はい／いいえの分岐ではないため、濃紺の中立の矢印と箱にした（本人への提起は『できる』なので、赤い箱にすると『できない』と読み違えるおそれがある）。2つ目のひし形は「知っていたか」のはい／いいえなので、青・赤にした。
- 占有を手放した場合（元の侵奪者が占有を失ったとき）の扱いは、記事の判断のしかたにある対比（手放した／貸しただけ）を、承継人の分岐として描いた。
