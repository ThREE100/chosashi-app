# 【M3-6】図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M3-6】（不動産質は、全部弁済まで全体に及び、転質も使用収益も承諾が要らない）に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は記事（`h20-mondai/q01-fudousan-shichi.md`）と法令DB（`note-articles/laws/`）の範囲です。

- 図解：不動産質の質権者にできること（全部に及ぶ・転質・使用収益・負担）
- 型：カードポスター型（5枚）　／　サイズ：1080×2300　／　保存名：`不動産質の質権者にできること_M3-6.png`
- 記事の挿入位置：総合記事【M3-6】の「結論」の直後（または「中身の整理」の終わり）

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせてください。

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Draw no check mark and no cross mark anywhere, and use no blue or red anywhere on this poster.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「不動産質の質権者にできること」
「全部に及び、承諾は要らない」
Subtitle (smaller, centered, 1 line):
「民法 第348条・第350条・第356条・第357条・第358条・第359条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「一部を返しても、全部に及ぶ」
Illustration: An isometric vacation cottage wrapped by a dark navy ribbon labeled 「質権」. Beside it, a horizontal bar split into two segments: a short segment labeled 「返した100万円」 and a longer segment labeled 「残り200万円」, under a small label 「借入れは300万円」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「全部の弁済まで全部に」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「転質に、設定者の承諾はいらない」
Illustration: A person pictogram with the name tag 「質権者」 standing beside a stack of two cards: the lower card labeled 「質権」 and the upper card labeled 「転質」. Next to the stack, a document sheet with a dotted outline labeled 「設定者の承諾」 with a small gray tag 「いらない」. Under the stack, a small note 「損失は不可抗力でも責任」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「自己の責任で転質」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「使用・収益にも、承諾はいらない」
Illustration: An isometric vacation cottage with a person pictogram tagged 「質権者」 at its door and a small pile of coins labeled 「収益」 beside it. Next to the cottage, a document sheet with a dotted outline labeled 「設定者の承諾」 with a small gray tag 「いらない」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「用法に従って使う」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「使える代わりに、負担がある」
Illustration: Two items side by side: on the left an invoice sheet labeled 「管理の費用」 with a small tag 「質権者が負担」; on the right a coin drawn with a dotted outline labeled 「利息」 with a small tag 「請求できない」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「費用は負担、利息は不可」
--- CARD 5 ---
Badge: a filled dark navy circle containing the number 5 (numbers run 1 to 5 in order).
Heading (bold, ONE line):
「使用・負担・利息は、定めで変えられる」
Illustration: A contract sheet labeled 「設定行為」 with a rubber stamp, and three small tags lined up beside it: 「使用・収益」, 「管理の費用」, 「利息」. A small label on the sheet: 「別段の定め」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「設定行為の別段の定め」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 承, 抗, 権, 請, 諾; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose, a check mark, or a cross mark. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

検品チェック：
- 文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない
- カードがちょうど5枚で、番号が1〜5の順。カードの中に文章（説明文）がない
- カード1の「返した100万円」と「残り200万円」の数字が入れ替わっていない（借入れは300万円）
- カード2・3の点線の書類（設定者の承諾）に「いらない」の札がある
- ✓・✕・青・赤がどこにもない／背景が透過でなく、最後のカードの下に追加のまとめがない
