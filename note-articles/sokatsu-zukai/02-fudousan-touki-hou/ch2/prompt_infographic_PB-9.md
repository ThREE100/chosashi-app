# 総合記事②不動産登記法編 第2章　図解インフォグラフィック プロンプト（【PB-9】登記識別情報は、誰に・どんな登記で・どう通知されるのか・2枚）

総合記事②不動産登記法編の第2章「添付情報・電子申請・登記識別情報・保存期間・登録免許税」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・対比・早見表が中心の図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解12）だけは、はい＝青・いいえ＝赤で描きます（緑には触れません）。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解12 | 登記識別情報は、通知されるか（判定の流れ） | 判定の流れ型 | 1080×2300 | 不動産登記法編2章_図解12_通知されるか.png | 【PB-9】「中身の整理」の直後 |
| 図解13 | 通知を受けるのは、誰か | 早見表型＋カード | 1080×2300 | 不動産登記法編2章_図解13_通知を受ける者.png | 【PB-9】「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解12：登記識別情報は、通知されるか（判定の流れ）

- 型：判定の流れ型　／　サイズ：1080×2300　／　保存名：`不動産登記法編2章_図解12_通知されるか.png`
- 記事の挿入位置：【PB-9】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a vertical decision-flow poster with two diamond questions, three result boxes, and one side note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「登記識別情報は、通知されるか」
「申請人自らが登記名義人になるか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第21条／規則 第64条」
--- FLOWCHART ---
Layout: one vertical flow on the center line. Node 1 at the top is a rounded navy start box with white text 「登記が完了した」.
Node 2 (a diamond question): 「その登記で、申請人自らが登記名義人となるか」. Two arrows leave it: the YES arrow (BLUE, with the small label 「はい」 in blue) goes down to node 3, and the NO arrow (RED, with the small label 「いいえ」 in red) goes to the right to the result box A.
Result box A (RED outline, on the right of node 2): 「通知されない」, with one small gray line under it: 「例：合筆の土地の抵当権者」.
Node 3 (a diamond question): 「あらかじめ、通知を希望しない旨の申出があるか」. Two arrows leave it: the YES arrow (BLUE, label 「はい」 in blue) goes to the left to the result box B, and the NO arrow (RED, label 「いいえ」 in red) goes down to the result box C.
Result box B (BLUE outline, on the left of node 3): 「通知されない」.
Result box C (RED outline, at the bottom): 「通知される」, with one small gray line under it: 「共有名義なら、名義人ごとに通知」.
--- SIDE NOTE CARD (below the flow, a wide card with a dashed dark navy outline) ---
Heading 「表示に関する登記でも通知される」, body 「所有権の登記がある土地の合筆・建物の合体による登記等・建物の合併」.
The arrows carry only the labels given above. The flow has exactly 3 result boxes and no other box. The letters A, B and C used in these instructions only identify the boxes and are never drawn in the image.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 当, 所, 抵, 権, 物, 登, 規, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two diamond questions and exactly three result boxes (A, B, C), that every YES arrow and its label are blue and every NO arrow and its label are red, that the three result boxes read exactly as given, and that no check mark or cross mark is drawn. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解13：通知を受けるのは、誰か

- 型：早見表型＋カード　／　サイズ：1080×2300　／　保存名：`不動産登記法編2章_図解13_通知を受ける者.png`
- 記事の挿入位置：【PB-9】「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns, and two deadline cards below the table.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「通知を受けるのは、誰か」
「名義人ごと、期限つき」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第62条・第64条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Header row (dark navy cells with white text): 「場面」, 「通知を受ける者」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「法定代理人が申請した」 | 「法定代理人」 | 「規則62条1項1号」
Row 2: 「申請人が法人である」 | 「その法人の代表者」 | 「規則62条1項2号」
Row 3: 「特別の委任を受けた代理人がいる」 | 「その代理人」 | 「規則62条2項」
Row 4: 「共有名義の土地2筆を合筆した」 | 「名義人ごとに、固有の内容」 | 「法21条」
Highlighting: the string 「名義人ごとに、固有の内容」 in row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.
--- TWO DEADLINE CARDS (below the table, side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「電子申請（規則64条1項2号）」, heading 「30日以内」 (the heading has a pale yellow highlighter marker), body 「送信が可能になった時から、自分のファイルに記録しないと通知されない」.
Right card: small tag 「書面申請（規則64条1項3号）」, heading 「3月以内」 (the heading has a pale yellow highlighter marker), body 「登記完了の時から、書面を受領しないと通知されない」.
The two cards have clearly different texts; the texts are NOT identical.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 地, 登, 規, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that there are exactly two deadline cards (電子申請 30日以内 on the left and 書面申請 3月以内 on the right, not swapped), and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
