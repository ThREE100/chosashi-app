# 【M3-5】図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M3-5】（地上権は、承諾なしで譲渡でき、地代は約束があって初めて生じる）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は記事（`h21-mondai/q02-chijouken.md`）と法令DB（`note-articles/laws/`）の範囲です。

- 図解：地上権と賃借権の違い（承諾・地代・時効取得）
- 型：対比表型（2列＋カード1枚）　／　サイズ：1080×1900　／　保存名：`地上権と賃借権の違い_M3-5.png`
- 記事の挿入位置：総合記事【M3-5】の「結論」の直後（または「中身の整理」の終わり）

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせてください。

```text
Create a Japanese-language infographic, portrait layout, 1080x1900 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster (対比表) with a short card below the table.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「地上権と賃借権の違い」
「承諾・地代・時効取得で整理する」
Subtitle (smaller, centered, 1 line):
「民法 第265条・第266条・第369条・第601条・第612条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header 「地上権」 with a small light-gray tag 「物権」 under it; the third header 「賃借権」 with a small light-gray tag 「債権」 under it.
Data row 1 (row label cell, dark navy, white text: 「どんな権利？」): second column 「工作物や竹木を所有するため、他人の土地を使う権利」; third column 「賃料を払って、土地を使わせてもらう権利」.
Data row 2 (row label cell, dark navy, white text: 「譲渡するとき」): second column 「所有者の承諾なしに譲渡できる」 with the words 「承諾なしに」 in a pale yellow highlighter marker, and a second smaller line 「抵当権も設定できる」; third column 「賃貸人の承諾を得なければ譲渡できない」 with the words 「承諾を得なければ」 in a pale yellow highlighter marker.
Data row 3 (row label cell, dark navy, white text: 「地代・賃料」): second column 「設定契約で定めて初めて生じる」 with the words 「定めて初めて」 in a pale yellow highlighter marker, and a second smaller line 「無償もあり、裁判所が額を定める制度はない」; third column 「賃料の支払が契約の前提」.
The second-column and third-column cells of each data row have clearly different texts; the texts are NOT identical, so copy each cell exactly as given.
--- CARD BELOW THE TABLE ---
One wide rounded card below the table, pale gray fill with a dark navy outline, with a dark navy heading 「地上権の時効取得」 and two short body lines: 「土地を使い続けている外形的な事実」 and 「地上権を行使する意思が、外から分かること」. Beside the heading, a small icon of a house on a plot of land. This card has no check mark and no cross, and it is NOT part of the table.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 債, 初, 効, 地, 対, 当, 所, 承, 抵, 権, 渡, 無, 物, 諾, 譲, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, that the second and third columns differ in every row, that the card below the table appears once, and that no check mark or cross mark appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

検品チェック：
- 文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない
- 表は3列（行見出し・地上権・賃借権）×3行で、左右の文言が全行で違う（取り違えていない）
- 「物権」は地上権の列、「債権」は賃借権の列の見出しの下にある（入れ替わっていない）
- 表の下のカード（地上権の時効取得）が1枚だけあり、表の一部になっていない
- ✓・✕・青・赤が表のどこにもない／背景が透過でなく、最後のカードの下に追加のまとめがない
