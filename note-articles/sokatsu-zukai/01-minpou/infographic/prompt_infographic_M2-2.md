# 【M2-2】占有の善意・悪意と占有の移転は、誰を基準に、いつから考えるのか　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M2-2】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：占有の善意と悪意（いつから・誰を・誰が）
  - 型：対比表型（3列）＋イメージ行　／　サイズ：1080×2100　／　保存名：`図解1_占有の善意と悪意.png`
  - 記事の挿入位置：【M2-2】の「中身の整理」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：占有の善意と悪意（いつから・誰を・誰が）

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three data columns (対比表) and an illustration row at the top of the table.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「占有の善意と悪意」
「いつから・誰を・誰が」
Subtitle (smaller, centered, 1 line):
「民法 第189条・第184条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three data columns) and exactly 4 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header 「いつから悪意とみなす？」; the third header 「善意・悪意は誰を基準に？」; the fourth header 「承諾するのは誰？」.
Data row 1 (row label cell, dark navy, white text: 「イメージ」): this row is taller than the others and holds one small flat illustration per column, drawn only with the labels given here.
  - Second column illustration: a horizontal timeline with three markers from left to right labeled 「占有の開始」, 「訴えの提起」 and 「敗訴」; the middle marker 「訴えの提起」 has a pale yellow highlighter marker and a small tag 「ここから悪意」 above it.
  - Third column illustration: two faceless pictograms side by side in the same light gray-blue color with dark navy tags 「本人」 and 「占有代理人」; under the first a small label 「善意」 and under the second a small label 「悪意」; a small caption under both: 「悪意の占有として扱う」.
  - Fourth column illustration: three faceless pictograms in a row in the same light gray-blue color with dark navy tags 「本人」, 「占有代理人」 and 「第三者」; one dark navy arrow from the first to the second carrying the small label 「命じる」, and a small speech tag 「承諾」 beside the third; under the third a small label 「占有権を取得」.
Data row 2 (row label cell, dark navy, white text: 「答え」): second column 「訴えの提起の時から、悪意とみなす」 with the part 「訴えの提起の時」 in a pale yellow highlighter marker; third column 「占有代理人について決める」 with the part 「占有代理人」 in a pale yellow highlighter marker; fourth column 「第三者が承諾すると、第三者が占有権を取得する」 with the part 「第三者が承諾」 in a pale yellow highlighter marker.
Data row 3 (row label cell, dark navy, white text: 「取り違えやすい点」): second column 「占有の開始の時と取り違える」; third column 「本人を基準にしてしまう」; fourth column 「占有代理人の承諾と取り違える」.
Data row 4 (row label cell, dark navy, white text: 「根拠」): second column 「民法189条2項」; third column 「判例・通説の理解」; fourth column 「民法184条」. These three cells use a smaller font in a light-gray tag style.
Every cell has its own text exactly as given; no two cells carry the same string. Exactly three strings are highlighted in pale yellow in data row 2, and one more in the timeline illustration.
The table is the last element of the poster.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 占, 対, 承, 権, 解, 説, 諾, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 4 data rows, that every cell reads exactly as given, that the illustration row uses only the labels listed, that no check mark, cross mark, blue, or red appears anywhere, and that the table is the last element of the poster. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`図解1_占有の善意と悪意.png`

## 検品チェック

- 表は4列（行見出し・3つの問い）×データ4行で、各セルの文字が指定どおりか（民法189条2項・判例・通説の理解・民法184条）。
- 「イメージ」の行の3つの絵が、指定のラベルだけで描かれているか（時間軸の3つの印、本人と占有代理人の2人、本人・占有代理人・第三者の3人と「命じる」の矢印1本）。
- 黄色のマーカーが、「答え」の行の3か所と、時間軸の「訴えの提起」だけか。青・赤・チェック・×が一つもないか。
- 表のあとに、まとめ・帯・追加の文字ブロックが描かれていないか。簡体字・余計な文字・透過・図番がないか。