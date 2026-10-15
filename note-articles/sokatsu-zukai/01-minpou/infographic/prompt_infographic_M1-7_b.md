# 【M1-7】時効の援用・更新・完成猶予：追加の図解「更新と完成猶予の違い」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-7】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-7.md`）は6枚のカードの並びなので、論点の題である「承認と猶予は何を変えるのか」＝更新（やり直し）と完成猶予（先延ばし）の効果の違いを、時間軸の絵で対比します。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図ははい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：更新と完成猶予の違い（承認と猶予は何を変えるのか）
  - 型：対比型（カード2枚＋カード1枚＋帯）　／　サイズ：1080×2200　／　保存名：`民法編1_M1-7_追加_更新と完成猶予の違い.png`
  - 記事の挿入位置：【M1-7】の「中身の整理」の直後（図解の次）

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：更新と完成猶予の違い（承認と猶予は何を変えるのか）

```text
Create a Japanese-language infographic, portrait layout, 1080x2200 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster: two cards side by side, each with a small timeline picture, followed by one wide card and one closing band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「更新と完成猶予の違い」
「承認と猶予は何を変えるのか」
Subtitle (smaller, centered, 1 line):
「民法 第147条・第152条・第158条」
--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
LEFT CARD: a small dark navy tag 「更新」 and the heading (bold) 「時効が、新たに進行する」.
  - Timeline picture: a horizontal bar that is filled with dark navy up to a vertical dashed line, then restarts as an empty bar from that line; a small rubber stamp icon sits on the dashed line, and the small label 「やり直し」 is written under the empty part.
  - Item lines (each with a small dark navy dot at its left end, NO number on the dots): 「承認」 with the small gray tag 「152条1項」; 「一部弁済（残りの債務の承認）」; 「確定判決で権利が確定した裁判上の請求」 with the small gray tag 「147条2項」.
RIGHT CARD: a small dark navy tag 「完成猶予」 and the heading (bold) 「その間は、時効が完成しない」.
  - Timeline picture: a horizontal bar that is filled with dark navy and ends at a small flag; a second light-gray bar extends beyond the flag to the right with a bracket labeled 「6か月」, showing that the end is pushed back.
  - Item lines (each with a small dark navy dot at its left end, NO number on the dots): 「訴えの取下げ → 終了の時から6か月」 with the small gray tag 「147条1項」; 「法定代理人のいない成年被後見人 → 就職の時などから6か月」 with the small gray tag 「158条1項」.
The two cards have clearly different texts; the texts are NOT identical, so copy each exactly as given.
--- WIDE CARD (a wide rounded card below the two cards, pale gray fill, dark navy outline, with NO arrow) ---
Heading (bold, ONE line): 「時効の完成のあとに承認したら」.
Body (ONE line): 「更新も猶予もなく、援用できない」 with the small gray tag 「判例」.
Under the body, a small dotted-outline tag (no check mark, no cross): 「完成を知らなくても同じ」.
--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below the wide card) ---
「更新はやり直し、」 on the first line and 「完成猶予は先延ばし」 on the second line.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 債, 効, 承, 援, 権, 認, 請, 違, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 2 cards side by side, exactly 1 wide card and exactly 1 closing band in this order, that the left card has exactly 3 item lines and the right card has exactly 2 item lines, that the left timeline picture shows an empty bar restarting after the dashed line and the right timeline picture shows the end pushed back by a 6か月 bracket, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-7_追加_更新と完成猶予の違い.png`

## 検品チェック

- 上段が左右2枚のカード（更新／完成猶予）で、左は項目が3行（承認・一部弁済・確定判決で権利が確定した裁判上の請求）、右は2行（訴えの取下げ・成年被後見人）か。
- 左の絵は空の棒が破線から再スタート（やり直し）、右の絵は終点が「6か月」の括弧で後ろへ延びている（先延ばし）か。
- 条番号（152条1項・147条2項・147条1項・158条1項）と「判例」の札が指定どおりか。濃紺の帯が最後に1つだけで、そのあとに何も描かれていないか。
- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。