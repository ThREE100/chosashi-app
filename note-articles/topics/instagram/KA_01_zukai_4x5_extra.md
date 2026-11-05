# KA_01 Instagram用 図解の追加プロンプト（4:5・1080×1350）

- 対象の記事：`note-articles/topics/KA_01_hyoudaibu-shoyuusha-vs-toukimeigijin.md`
- 総論の4:5は `KA_01_zukai_4x5.md`。このファイルは、記事の画像3（段階フロー型）と画像4（対比表型）の4:5版。文字・結論は記事と同じ（大きさと余白だけ変えた）。
- 記事の画像2（令和6年度の場面のフローチャート）は、問題番号を画像に入れない決まりのため4:5には含めない。
- 画像の生成と目視確認はChatGPTで行う（未実施）。

## 画像A（段階フロー型）

```
Create a Japanese-language infographic, portrait layout, 4:5 aspect ratio, 1080x1350 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded sections, consistent with a modern
explainer-graphic aesthetic (icons: an isometric registry book, stick-figure
people, stamps/hanko seals, small land-plot tiles, check marks).

GLANCEABLE-POSTER REQUIREMENT (critical): quick-reference poster, NOT a
text-heavy document. NO intro illustration and NO paragraph of prose. Every
element is a short label (a few words) plus an icon. Do NOT render any
full-sentence explanation or legal citation inside the picture area.

CRITICAL TEXT REQUIREMENT: All text must be standard Japanese only -
hiragana, katakana and Jōyō kanji. Do NOT use Simplified or Traditional
Chinese characters, Korean Hangul, Latin letters, digits or stray decorative
glyphs anywhere. Reproduce the exact strings below verbatim - do not
paraphrase or substitute. Pay special attention to the kanji 表・題・部・権・
登・記・義・申・請・管・轄・抹・消・保・存・移・転 - render them in standard
Japanese forms.

ILLUSTRATION TEXT RULE (critical): the only text allowed inside the
illustrations is the words written in 「」 on each element's Illustration line.
Do not invent any other text, number or pseudo-writing inside props. If a
prop needs no word, leave it blank or use an icon or a mark.

NO NUMBERING (critical): do not draw any number or numbered circle.

COLOR RULE (critical): affirmative (はい, あり, 満たす) = blue; negative
(いいえ, なし) = red. Use these two colors for that meaning only.

BACKGROUND REQUIREMENT (critical): the entire canvas is fully opaque from
edge to edge; no transparency, no checkerboard, no unpainted edge.

INSTAGRAM FEED FORMAT (critical - overrides every other statement about size or layout): the canvas is EXACTLY 1080x1350 pixels, portrait 4:5. Keep every element inside a margin of 54 px left/right and 68 px top/bottom, filled with the opaque background only. Text size for a phone: title 72 px or larger, subtitle 36 px or larger, headings and table text 34 px or larger, tags 32 px or larger; if text does not fit, shrink the illustrations, never the text. BOTTOM ALIGNMENT: the bottom edges of the boxes, cards or table rows line up, with the last row or box ending on one horizontal line at the bottom margin, equal gaps between boxes, and spare height absorbed inside the boxes (vertical centring, padding), never as a ragged gap. Draw NO footer, account name, URL, hashtag, logo or call-to-action text.

--- HEADER ---
Title (large, bold, up to 2 lines):
表題部所有者から登記名義人へ、登記簿の成長
Subtitle (smaller, 1 line):
表題部だけの状態から、権利部ができるまで

--- STAGE FLOW (top to bottom, four stage boxes joined by plain downward arrows, no loops) ---
STAGE A (soft green box)
  Heading: 表題登記だけの状態
  Illustration: an isometric registry book with only the left page filled, labeled 「表題部」, and a person icon on it; the right page is blank gray with a dashed outline.
  Words allowed inside this illustration (verbatim, nothing else): 「表題部」
  Tag: 表題部所有者

STAGE B (soft green box)
  Heading: 所有権保存登記を申請する
  Illustration: three small person icons in a row, each with a short torn-paper label.
  Words allowed inside this illustration (verbatim, nothing else): 「表題部所有者・一般承継人」「確定判決で確認された者」「収用で取得した者」
  Tag: 申請できる人は三類型だけ

STAGE C (soft blue box)
  Heading: 権利部（甲区）ができる
  Illustration: the same registry book now with both pages filled, the left page labeled 「表題部」 with a small hanko seal crossing out the person icon, the right page labeled 「権利部」 with a tag 「甲区」.
  Words allowed inside this illustration (verbatim, nothing else): 「表題部」「権利部」「甲区」
  Tag: 所有権の登記名義人／表題部所有者の記録は抹消

STAGE D (soft blue box)
  Heading: 持ち主が代わるときの順序
  Illustration: two small boxes joined by an arrow, left box 「保存登記」, right box 「移転登記」.
  Words allowed inside this illustration (verbatim, nothing else): 「保存登記」「移転登記」
  Tag: 先に保存、そのあとで移転

No footer text: the legal basis is given in the article, not in the picture.

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified or Traditional Chinese; remove
any non-Japanese character, Latin letter or digit; confirm there is no intro
block and no extra panel after the last element; confirm no illustration
contains text other than its allowed words; confirm the canvas is fully opaque.
```

## 画像B（対比表型）

```
Create a Japanese-language infographic, portrait layout, 4:5 aspect ratio, 1080x1350 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded sections, consistent with a modern
explainer-graphic aesthetic (icons: an isometric registry book, stick-figure
people, stamps/hanko seals, small land-plot tiles, check marks).

GLANCEABLE-POSTER REQUIREMENT (critical): quick-reference poster, NOT a
text-heavy document. NO intro illustration and NO paragraph of prose. Every
element is a short label (a few words) plus an icon. Do NOT render any
full-sentence explanation or legal citation inside the picture area.

CRITICAL TEXT REQUIREMENT: All text must be standard Japanese only -
hiragana, katakana and Jōyō kanji. Do NOT use Simplified or Traditional
Chinese characters, Korean Hangul, Latin letters, digits or stray decorative
glyphs anywhere. Reproduce the exact strings below verbatim - do not
paraphrase or substitute. Pay special attention to the kanji 表・題・部・権・
登・記・義・申・請・管・轄・抹・消・保・存・移・転 - render them in standard
Japanese forms.

ILLUSTRATION TEXT RULE (critical): the only text allowed inside the
illustrations is the words written in 「」 on each element's Illustration line.
Do not invent any other text, number or pseudo-writing inside props. If a
prop needs no word, leave it blank or use an icon or a mark.

NO NUMBERING (critical): do not draw any number or numbered circle.

COLOR RULE (critical): affirmative (はい, あり, 満たす) = blue; negative
(いいえ, なし) = red. Use these two colors for that meaning only.

BACKGROUND REQUIREMENT (critical): the entire canvas is fully opaque from
edge to edge; no transparency, no checkerboard, no unpainted edge.

INSTAGRAM FEED FORMAT (critical - overrides every other statement about size or layout): the canvas is EXACTLY 1080x1350 pixels, portrait 4:5. Keep every element inside a margin of 54 px left/right and 68 px top/bottom, filled with the opaque background only. Text size for a phone: title 72 px or larger, subtitle 36 px or larger, headings and table text 34 px or larger, tags 32 px or larger; if text does not fit, shrink the illustrations, never the text. BOTTOM ALIGNMENT: the bottom edges of the boxes, cards or table rows line up, with the last row or box ending on one horizontal line at the bottom margin, equal gaps between boxes, and spare height absorbed inside the boxes (vertical centring, padding), never as a ragged gap. Draw NO footer, account name, URL, hashtag, logo or call-to-action text.

--- HEADER ---
Title (large, bold, 1 line):
表題部所有者と所有権の登記名義人
Subtitle (smaller, 1 line):
5つの観点で見比べる

--- TABLE (render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font) ---
Header row: 観点 | 表題部所有者 | 所有権の登記名義人
Row 1: 記録される場所 | 表題部 | 権利部（甲区）
Row 2: 対象となる不動産 | 所有権の登記がない | 所有権の登記がある
Row 3: 登記のしかた | 表題登記 | 所有権保存登記（または移転登記）
Row 4: 対抗力 | なし | あり
Row 5: 持ち主が代わるとき | 先に保存登記、そのあと移転登記 | 移転登記
Column header colors: 表題部所有者 = soft green, 所有権の登記名義人 = soft blue. In Row 4 mark 「なし」 with a red cross and 「あり」 with a blue check mark.

--- CALLOUT (one line, below the table) ---
1つの不動産で両方になることはない

--- FOOTER ---
No footer text: the legal basis is given in the article, not in the picture.

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified or Traditional Chinese; remove
any non-Japanese character, Latin letter or digit; confirm there is no intro
block and no extra panel after the last element; confirm no illustration
contains text other than its allowed words; confirm the canvas is fully opaque.
```
