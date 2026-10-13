# 総合記事② 不動産登記法編 第9章　図解インフォグラフィック プロンプト（【PG2-3】区分建物の登記の申請は「併せて」か「一括して」か、いつまでか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第9章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch9.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この章の図解は『誰が・いつまでに・何を添えるか』の分類や手続の流れが中心で、はい／いいえの分岐ではないため、共通部品の配色の規則（青＝はい、赤＝いいえ）は入れず、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解6 | 併せて申請？一括して申請？（区分建物の申請方法） | 早見表型（3列） | 1080×2100 | 不登法編ch9_図解6_併せてか一括してか.png | 【PG2-3】「中身の整理」の直後 |
| 図解7 | 合体による登記等、誰が・いつまでに申請するか | カード＋表型 | 1080×2100 | 不登法編ch9_図解7_合体による登記等.png | 【PG2-3】図解6の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解6：併せて申請？一括して申請？（区分建物の申請方法）

- 型：早見表型（3列）　／　サイズ：1080×2100　／　保存名：`不登法編ch9_図解6_併せてか一括してか.png`
- 記事の挿入位置：【PG2-3】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (場面と申請方法).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「併せて申請？一括して申請？」
「区分建物の申請方法を整理する」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第48条・第52条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.
Header row (dark navy cells with white text): 「場面」, 「申請の方法」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「区分建物が属する一棟の建物を、新築した」 | 「その一棟の他の区分建物の表題登記と、併せて」 | 「法48条1項」
Row 2: 「表題登記のある非区分建物に接続して、区分建物を新築した」 | 「新築区分建物の表題登記と、既存建物の表題部の変更の登記を、併せて」 | 「法48条3項・法52条1項」
Row 3: 「表題登記のある二以上の非区分建物が、増築で相互に接続して区分建物になった」 | 「表題部の変更の登記を、一括して」 | 「法52条3項」
Row 4: 「別の一棟の区分建物を、附属建物にする」 | 「その一棟の他の区分建物の表題登記も、併せて」 | 「法48条1項の趣旨（整理）」
Highlighting: the string 「一括して」 in the column-2 cell of row 3 has a pale yellow highlighter marker; every 「併せて」 is plain. The cell of column 3 in row 4 has a slightly darker pale gray fill to show that it is an organizing note, not a written provision. The words 「併せて」 and 「一括して」 differ; copy each exactly as given and do not change one into the other.
Under the table, one wide dark navy band with large white text 「既存の非区分建物どうしの接続は、法52条3項で一括申請」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that only row 3 reads 一括して in column 2, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解7：合体による登記等、誰が・いつまでに申請するか

- 型：カード＋表型　／　サイズ：1080×2100　／　保存名：`不登法編ch9_図解7_合体による登記等.png`
- 記事の挿入位置：【PG2-3】図解6の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a poster with two top cards and a three-column table below.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「合体による登記等」
「誰が・いつまでに申請するか」
Subtitle (smaller, centered, 1 line):
「不動産登記法 第49条第1項」
--- TWO CARDS (side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: heading 「申請するもの」, two body lines each with a small dark navy dot at its left end (NO number on the dots): 「合体後の建物の表題登記」, 「合体前の建物の表題部の登記の抹消」.
Right card: heading 「期限」, body 「合体の日から1月以内」 (the string 「1月以内」 has a pale yellow highlighter marker).
The two cards have clearly different texts; the texts are NOT identical.
--- TABLE ---
A small dark navy tag above the table: 「申請人は、合体前の建物の登記の状態で決まる」.
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells.
Header row (dark navy cells with white text): 「号」, 「合体前の建物」, 「申請人」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「3号」 | 「いずれも表題登記がある建物」 | 「表題部所有者」
Row 2: 「5号」 | 「いずれも所有権の登記がある建物」 | 「所有権の登記名義人」
Row 3: 「1号・2号・4号・6号」 | 「上の2つ以外の組み合わせ」 | 「号ごとに法49条1項が定める者」
Highlighting: the strings 「表題部所有者」 in row 1 and 「所有権の登記名義人」 in row 2 have a pale yellow highlighter marker; the row 3 cells are plain. Copy each cell exactly as given.
Under the table, one wide dark navy band with large white text 「表題登記だけなら表題部所有者、所有権の登記ありなら登記名義人」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 建, 所, 権, 物, 登, 記, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards at the top and a table with exactly 3 columns and exactly 3 data rows, that rows 1 and 2 read 表題部所有者 and 所有権の登記名義人 in column 3 and are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
