# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（【PA-11】添付情報：何を添え、何は要らず、どの方式なら置き換えられるか・2枚）

総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解14 | 建物の添付情報は？（何を添え、何は要らないか） | カードポスター型（3枚） | 1080×2300 | 不登法編1_図解14_建物の添付情報.png | 【PA-11】「中身の整理」の直後 |
| 図解15 | 電子申請の添付情報、置き換えは？ | 対比カード型（2列） | 1080×2100 | 不登法編1_図解15_添付情報の置き換え.png | 【PA-11】図解14の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解14：建物の添付情報は？（何を添え、何は要らないか）

- 型：カードポスター型（3枚）　／　サイズ：1080×2300　／　保存名：`不登法編1_図解14_建物の添付情報.png`
- 記事の挿入位置：【PA-11】「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with three numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two or three short item lines, and one short conclusion tag. Do NOT render any paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「建物の添付情報は？」
「何を添え、何は要らないか」
Subtitle (smaller, centered, 1 line):
「不動産登記令 別表」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「建物の表題登記」
Illustration: A folder with a floor plan sheet, a certificate sheet and an address card, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「建物図面・各階平面図」
「所有権を証する情報」
「住所を証する情報」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「令別表の建物の表題登記」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「他人の土地に建てた建物の表題登記」
Illustration: A small house on a plot, with a dashed outline around a lease contract sheet, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「借地権を証する情報は、必須ではない」
「敷地所有者の証明書も、所有権を証する情報に使える」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「借地権の証明は要らない」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「建物の床面積の変更」
Illustration: A floor plan sheet with an added room drawn with a dashed outline, no text.
Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):
「変更後の建物図面・各階平面図」
「増えた部分の所有権を証する情報」
「一部取壊しの後に増築して一の申請なら、全体で減っても必要（実務上の取扱い）」
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「増えた部分の証明が要る」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 所, 権, 物, 登, 記, 証, 請; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a paragraph of body text. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解15：電子申請の添付情報、置き換えは？

- 型：対比カード型（2列）　／　サイズ：1080×2100　／　保存名：`不登法編1_図解15_添付情報の置き換え.png`
- 記事の挿入位置：【PA-11】図解14の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison poster with two side-by-side cards.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「電子申請の添付情報、置き換えは？」
「対象になるもの・ならないもの」
Subtitle (smaller, centered, 1 line):
「不動産登記令 第13条」
--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---
Left card: small tag 「令13条1項」, heading 「置き換えられる」, and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「書面の添付情報を、電磁的記録にする」, 「作成者の電子署名を付ける」, 「登記官が定めた期間内に、書面を提示する」.
Right card: small tag 「対象外」, heading 「置き換えられない」 (the string 「置き換えられない」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): 「申請人・代表者・代理人が作成した情報」, 「調査士が作る調査報告情報（代理人の作成）」, 「図面（地積測量図・建物図面など）」, 「地役権設定の範囲を証する、地役権者作成の情報」.
The two cards have clearly different texts; the texts are NOT identical.
Under the cards, one wide dark navy band with large white text 「調査士報告方式でも、地役権者作成の書面は書面の提示が必要」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 地, 対, 建, 権, 物, 登, 記, 証, 請, 録, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly two cards, that the left card has exactly three item lines and the right card has exactly four item lines, that the two headings 置き換えられる and 置き換えられない are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
