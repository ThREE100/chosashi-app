# 総合記事②不動産登記法編 第6章　図解インフォグラフィック プロンプト（【PF1-5】分割の登記で、登記記録にはどう記録され、抵当権はどうなるか・2枚）

総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『できない建物の一覧』『要る・要らない』のような分類が中心なので、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。フローチャート（図解4）だけは、分岐の矢印とラベルを濃紺にし、結果の箱を『5号の制限に当たらない＝青』『5号の制限に当たる＝赤』で塗り分けます（『はい』『いいえ』の文字は使いません）。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解8 | 分割した乙建物には何が記録される？（転写と旨の記録） | 対比カード型＋3段階 | 1080×2500 | 不登法編6章_図解8_分割後の乙建物の記録.png | 【PF1-5】「中身の整理」の直後 |
| 図解9 | 分割の登記の承諾の要否と所在の記録 | 対比カード型（2列） | 1080×2000 | 不登法編6章_図解9_分割の承諾と所在の記録.png | 【PF1-5】図解8の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解8：分割した乙建物には何が記録される？（転写と旨の記録）

- 型：対比カード型＋3段階　／　サイズ：1080×2500　／　保存名：`不登法編6章_図解8_分割後の乙建物の記録.png`
- 記事の挿入位置：【PF1-5】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster: two cards at the top, a three-stage row in the middle, and one wide card at the bottom.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分割した乙建物には」
「何が記録される？」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第128条」
--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card, small tag 「規則128条1項」, heading 「原則は、転写」, three body lines 「分割前の甲建物の」, 「権利に関する登記を」, 「乙建物に転写する」.
Right card, small tag 「規則128条2項」, heading 「例外は、旨を記録」, three body lines 「所有権の登記のあとに、」, 「附属建物の新築による」, 「表題部の変更の登記があるとき」, and under them a pale-yellow highlighted line 「転写に代えて、旨を記録する」.
The two cards have clearly different texts; the texts are NOT identical.
--- THREE-STAGE ROW (below the two cards, with a small dark navy tag 「例外に当たる場面の順番」 above it; three cards in ONE row from left to right, all the same size; no arrows, no connectors) ---
Stage card 1: badge 「まず」, text 「甲建物に所有権の登記」.
Stage card 2: badge 「次に」, text 「附属建物を新築して変更の登記」.
Stage card 3: badge 「最後に」, text 「その附属建物を分割して乙建物に」.
--- WIDE CARD (at the bottom, a wide card with a dashed dark navy outline) ---
Heading 「旨を記録するとき、乙建物の甲区に記録されるもの」, three short rows each with a small dark navy dot at its left end (NO number on the dots): 「分割による所有権の登記をする旨」, 「所有権の登記名義人の氏名又は名称及び住所」, 「登記の年月日」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 建, 当, 所, 権, 物, 番, 登, 規, 記, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards at the top (left 原則は、転写 and right 例外は、旨を記録, never swapped), exactly three stage cards in one row in the order まず, 次に, 最後に, and exactly one wide card at the bottom with exactly three rows, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解9：分割の登記の承諾の要否と所在の記録

- 型：対比カード型（2列）　／　サイズ：1080×2000　／　保存名：`不登法編6章_図解9_分割の承諾と所在の記録.png`
- 記事の挿入位置：【PF1-5】図解8の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards and one band.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「分割の登記の手続と記録」
「承諾の要否と所在の記録」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第54条第3項・第40条／不動産登記規則 第127条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「法54条3項・40条」, heading 「分割後の建物から抵当権を消すには」, and exactly three short rows, each with a small dark navy dot at its left end (NO number on the dots): 「要る：権利者の承諾を証する情報」, 「要らない：登記識別情報」, 「第三者の権利の登記があれば、その者の承諾も要る」. The row 「要らない：登記識別情報」 has a pale yellow highlighter marker.
Right card: small tag 「規則127条3項」, heading 「分割で所在が変わるとき」, and exactly four short rows, each with a small dark navy dot at its left end (NO number on the dots): 「変更後の所在」, 「分割により変更した旨」, 「変更前の所在を消す記号」, 「別に変更の登記を申請する必要はない」. The row 「別に変更の登記を申請する必要はない」 has a pale yellow highlighter marker.
The two cards have clearly different texts; the texts are NOT identical.
Under the two cards, one wide dark navy band with large white text 「消すのに要るのは、承諾を証する情報だけ」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 当, 所, 承, 抵, 権, 物, 登, 規, 記, 証, 請, 諾, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly three rows and the right card has exactly four rows, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
