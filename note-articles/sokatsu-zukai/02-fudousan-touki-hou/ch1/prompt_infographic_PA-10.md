# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（【PA-10】どの登記と、どの登記を、一の申請情報でまとめて申請できるのか・1枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解13 | 一の申請情報で、まとめられる？（規則35条の組合せ） | 早見表型（3列） | 1080×2500 | 不登法編1_図解13_一の申請情報.png | 【PA-10】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解13：一の申請情報で、まとめられる？（規則35条の組合せ）

- 型：早見表型（3列）　／　サイズ：1080×2500　／　保存名：`不登法編1_図解13_一の申請情報.png`
- 記事の挿入位置：【PA-10】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「一の申請情報で、まとめられる？」
「規則35条の組合せだけ」
Subtitle (smaller, centered, 1 line):
「不動産登記規則 第35条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.
Header row (dark navy cells with white text): 「登記の組合せ」, 「まとめて申請」, 「根拠」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「同じ土地の地積の更正と、更正後の分筆」 | 「できる」 | 「規則35条7号」
Row 2: 「表題部所有者の住所・氏名の変更と、合筆」 | 「できる」 | 「規則35条7号」
Row 3: 「土地の一部の分筆と、他の土地への合筆」 | 「できる」 | 「規則35条1号」
Row 4: 「甲建物の附属建物の分割と、乙建物の附属建物とする合併」 | 「できる」 | 「規則35条2号」
Row 5: 「区分建物の附属建物の分割と、接続する区分建物への合併」 | 「接続していればできる」 | 「規則35条3号」
Row 6: 「甲建物の滅失と、乙建物の表題登記」 | 「できない」 | 「別の不動産で、目的も違う」
Highlighting: the string 「できない」 in row 6 and the string 「接続していれば」 in row 5 have a pale yellow highlighter marker; the other cells in column 2 are plain. The strings 「できる」 and 「できない」 differ by one character; copy each exactly as given and do not change one into the other.
Under the table, two wide bands stacked: the first band, dark navy with large white text, 「原則は、目的と登記原因・日付が同一（令4条ただし書）」; the second band, pale gray with dark navy text, 「例外は、規則35条の限定列挙」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 号, 地, 建, 所, 物, 登, 規, 記, 請, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that only row 6 reads できない and row 5 reads 接続していればできる, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
