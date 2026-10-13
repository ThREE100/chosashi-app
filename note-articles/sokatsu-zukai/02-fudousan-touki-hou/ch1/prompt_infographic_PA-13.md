# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（【PA-13】登記官の本人確認調査は、いつ義務になり、不正登記防止申出はどうするのか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解17 | 本人確認調査は、必ずする？ | フローチャート型 | 1080×2600 | 不登法編1_図解17_本人確認調査.png | 【PA-13】「中身の整理」の直後 |
| 図解18 | 相当な理由と、不正登記防止申出 | 対比カード型（2列） | 1080×2400 | 不登法編1_図解18_相当な理由と申出.png | 【PA-13】図解17の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解17：本人確認調査は、必ずする？

- 型：フローチャート型　／　サイズ：1080×2600　／　保存名：`不登法編1_図解17_本人確認調査.png`
- 記事の挿入位置：【PA-13】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「本人確認調査は、必ずする？」
「相当な理由があるときだけ」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第24条第1項」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, each with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. All arrows are straight or have at most one right-angle bend and never cross each other.
NODE START (rounded pill, dark navy): 「登記の申請があった」
NODE DIAMOND 1: 「申請を却下すべき場合か？」 The text is placed inside the diamond on 2 lines.
  - Arrow right to RESULT 1 with the BLUE label 「はい」.
  - Arrow down to DIAMOND 2 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「調査せず、却下する」 on the first line and 「調査の対象にならない」 on the second line.
NODE DIAMOND 2: 「申請人となるべき者以外が申請していると疑うに足りる相当な理由があるか？」 The text is placed inside the diamond on 4 lines; enlarge the diamond so that all text stays inside it.
  - Arrow right to RESULT 2 with the BLUE label 「はい」.
  - Arrow down to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 2 (blue box): 「本人確認調査をしなければならない」 on the first two lines and 「申請権限の有無を調査する（法24条1項）」 on the next two lines.
NODE RESULT 3 (red box): 「調査の義務は生じない」 on the first line and 「申請の度に調べるのではない」 on the second line.
Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 対, 当, 権, 無, 登, 記, 認, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, and that no arrow label is hidden. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解18：相当な理由と、不正登記防止申出

- 型：対比カード型（2列）　／　サイズ：1080×2400　／　保存名：`不登法編1_図解18_相当な理由と申出.png`
- 記事の挿入位置：【PA-13】図解17の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「相当な理由と、不正登記防止申出」
「列挙を確かめ、申出は出頭で」
Subtitle (smaller, centered, 1 line):
「不動産登記事務取扱手続準則 第33条・第35条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「準則33条1項」, heading 「相当な理由の例」, and exactly five short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「捜査機関等から、不正事件のおそれの通報」, 「不正登記防止申出から3月以内の申請」, 「同一の申請人に係る、他の不正事件の発覚」, 「前の住所地への通知後の、異議の申出」, 「登記識別情報の誤りによる補正等が複数回」.
Right card: small tag 「準則35条1項」, heading 「不正登記防止申出」, and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「登記所に出頭してする」, 「申出書の送付だけではできない」, 「出頭できないやむを得ない事情があれば、委任による代理人でもよい」.
At the bottom of the left card, one pale-yellow banner 「申請前3月以内の住所変更の登記は、この列挙にない」.
The two cards have clearly different texts; the texts are NOT identical.
Under the cards, one wide dark navy band with large white text 「住所変更が3月以内でも、それだけでは調査義務は生じない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 地, 当, 所, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly five item lines and the right card has exactly three item lines, that the pale-yellow banner is at the bottom of the left card, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
