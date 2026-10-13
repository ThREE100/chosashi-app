# 総合記事②不動産登記法編 第2章　図解インフォグラフィック プロンプト（【PB-1】添付情報は番号や電子証明書で省略できるのか。省略できるのは何か・1枚）

総合記事②不動産登記法編の第2章「添付情報・電子申請・登記識別情報・保存期間・登録免許税」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・対比・早見表が中心の図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解12）だけは、はい＝青・いいえ＝赤で描きます（緑には触れません）。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解2 | 省略できるのは、添付情報だけ | 対比カード型（2列） | 1080×2100 | 不動産登記法編2章_図解2_省略できるのは添付情報だけ.png | 【PB-1】「中身の整理」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解2：省略できるのは、添付情報だけ

- 型：対比カード型（2列）　／　サイズ：1080×2100　／　保存名：`不動産登記法編2章_図解2_省略できるのは添付情報だけ.png`
- 記事の挿入位置：【PB-1】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards and one wide note card.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「省略できるのは、添付情報だけ」
「申請情報の記載事項は省略できない」
Subtitle (smaller, centered, 1 line):
「不動産登記令 第3条・第7条／規則 第36条・第37条・第44条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「申請情報（令3条）」, heading 「番号を出しても、書く」 (the heading string has a pale yellow highlighter marker), and exactly 2 short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「法人の代表者の氏名（令3条2号）」, 「会社法人等番号を提供しても省略できない」.
Right card: small tag 「添付情報（令7条）」, heading 「番号や電子証明書で省略できる」, and exactly 3 short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「代表者の資格を証する情報（会社法人等番号の提供で足りる）」, 「支配人の権限を証する情報（番号を有する法人の支配人等）」, 「住所を証する情報（署名用電子証明書の提供で足りる）」.
The two cards have clearly different texts; the texts are NOT identical.
--- NOTE CARD (below the two cards, a wide card with a dashed dark navy outline) ---
Heading 「同時の申請は、援用できる」, 2 body lines 「同一の登記所に同時に二以上の申請をするとき、共通の添付情報は一方に付ければ足りる（規則37条）」 and 「もう一方の申請情報に、付けた旨を書く」.
Under the last card, one wide dark navy band with large white text 「省略できるのは添付情報。申請情報の記載事項は書く」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 号, 所, 援, 権, 番, 登, 規, 記, 証, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly 2 item lines and the right card has exactly 3 item lines, that the two headings are not swapped, that there is exactly one note card below the two cards, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
