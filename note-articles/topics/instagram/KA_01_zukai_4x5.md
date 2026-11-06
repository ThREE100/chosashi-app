# KA_01 Instagram用 総論の図解インフォグラフィック（4:5・1080×1350）のプロンプト

- 対象の記事：`note-articles/topics/KA_01_hyoudaibu-shoyuusha-vs-toukimeigijin.md`
- 元にした図解：記事の「画像1（俯瞰カードポスター型：表題部所有者と所有権の登記名義人の違い）」。この記事の総論にあたる。カードは4枚のまま、中身と結論は記事と同じ。
- note用は記事末尾の「インフォグラフィック プロンプト」の画像1。このファイルはInstagram用（1080×1350・縦4:5）。
- 記事の画像2（令和6年度の場面のフローチャート）は、問題番号を画像に入れない決まりと、1枚で読める量に収める都合で、この4:5の総論には含めていない。
- 画像の生成と目視確認はChatGPTで行う（未実施）。キャラクターは描かない（図解は人型アイコンのみ）。
- 4:5はプロフィールのグリッドでは上下がわずかに切れる（`note-unei/instagram/image-spec.md`）。大事な要素は余白（左右54px・上下72px）の内側に置く。

## 画像の文字（1字ずつ確かめる）

| 場所 | 文字 |
|---|---|
| タイトル | 表題部所有者と登記名義人、何が違う？ |
| サブタイトル | 登記記録は「表題部」と「権利部」の二段階でできている |
| 左の見出し（青） | 二つの呼び名の違い |
| 右の見出し（緑） | 実務でのポイント |
| カード1 | 表題部所有者／表題登記のみ・対抗力なし |
| カード2 | 所有権の登記名義人／保存登記まで完了・対抗力あり |
| カード3 | 同じ人でも土地ごとに立場が違う／実務でよくある混在 |
| カード4 | 混在していてもまとめて申請できる／管轄・目的・原因・日付が同じ |

数字・英字は画像に入れない（記事の条文番号も入れない。条文は記事とキャプションで案内する）。

## 4:5画像プロンプト（ChatGPTに貼る）

```
Create a Japanese-language infographic, portrait layout, 4:5 aspect ratio, 1080x1350 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: an isometric registry book,
stick-figure people, torn-paper labels, stamps/hanko seals, small land-plot
tiles, a shield icon, check marks - adapt icon set to the topic).

INSTAGRAM FEED FORMAT (critical - this overrides every other statement about size or layout in this prompt):
the canvas is EXACTLY 1080x1350 pixels, portrait 4:5 (NOT 9:16, NOT 3:4). It is for an Instagram feed post, so
nothing important may touch the edges, and the top and bottom may be slightly cropped in the profile grid.
- Safe area: keep the title, subtitle, every column header, every card heading, every illustration and every
  conclusion tag inside a margin of 54 px on the left and right and 72 px at the top and bottom. Fill the
  margin with the opaque background only.
- Layout: a header band at the top (title and subtitle, see LAYOUT LOCK; at most 16% of the height),
  then the cards. Arrange the cards in TWO columns, reading the left column first (top to bottom), then the
  right column. Each column has one pill-shaped header badge above its two cards. The cards are compact:
  the illustration takes about 55% of the card height, the heading is ONE line and the conclusion tag is
  ONE line. The layout must not need more than 1350 px of height: shrink the illustrations, never the text.
- Text size for a phone screen (1080 px wide): title 72 px or larger, subtitle 36 px or larger, column
  header 36 px or larger, card heading 36 px or larger, conclusion tag 32 px or larger, any word inside an
  illustration 32 px or larger. If the text does not fit, shorten nothing: make the illustrations smaller.
- Do NOT draw any footer, account name, URL, hashtag, logo, watermark or call-to-action text anywhere in
  the image. The only text on the canvas is the title, the subtitle, the column headers, the card headings,
  the conclusion tags and the words allowed inside the illustrations.

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster - go straight from the header
to the cards. Every card must communicate its point almost entirely
through the illustration (icons, check marks, small embedded labels) plus
one short heading and one short conclusion tag. Do NOT render any
full-sentence explanation, legal citation, or paragraph of body text
anywhere on the poster. If a piece of information cannot be expressed as a
short label (a few words) or drawn as an icon, leave it out rather than
writing it as prose.

LAYOUT LOCK (critical): the header, the bottom edge and a five-card set are fixed as follows.
- HEADER: the header (title + subtitle) is a fixed block at the top, inside the safe margin. The title is bold and 72 px tall (never larger), on ONE line if it fits within the safe width, otherwise on TWO lines of the same size. The subtitle is 36 px, placed directly under the title with a gap of at most 16 px. The header block is at most 16% of the canvas height. There is NO empty band above the title, NO empty gap between the title and the subtitle, and NO empty band between the header and the first card or group header (the cards start at most 24 px below the subtitle). Do not enlarge the title to fill space.
- BOTTOM ALIGNMENT: the cards fill the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line on that bottom margin line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, the card's own padding), never as an empty strip or a ragged bottom edge.
- FIVE CARDS: if there are exactly five cards, do NOT leave an empty slot in the grid. With no column group headers, place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and conclusion tag on the right). With two column group headers, keep every card under its own header and make the cards of the column with fewer cards taller so that both columns end on the same bottom line.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only - hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form - every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image -
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, no Latin letters, no digits, and no stray or decorative glyphs of
any kind, even as small background or texture elements. Every kanji must
match standard Japanese orthography exactly as written below,
stroke-for-stroke. Reproduce the exact text strings given below verbatim -
do not paraphrase, translate, summarize, or substitute any characters. Pay
special attention to the kanji 表・題・部・権・登・記・義・申・請・混・管・轄 - these must be
rendered in their standard Japanese forms, never as Simplified Chinese
variants.

ILLUSTRATION TEXT RULE (critical): the only text allowed inside the
illustrations is the specified words (絵の中に入れる文字は、指定した語だけ).
This is an instruction, never text to draw. Inside every illustration (on
objects, signs, papers, documents, stamps, books, land tiles and any other
prop), render ONLY the words written in 「」 in that card's Illustration line
(and repeated on the "Words allowed" line under it), each one large, clear
and exactly as written. Do not invent or add any other text inside an
illustration: no extra signs, labels, captions, numbers or pseudo-writing.
If a prop needs no specified word, leave its surface blank or show its
meaning with an icon or a mark (check mark) instead. The title, subtitle,
column headers, card headings and conclusion tags are the only other text
on the poster.

NO NUMBERING (critical): do not draw any number, numbered circle, badge or
sequence mark on or near any card. The cards are not numbered.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas - including every corner and
margin outside the cards/columns - with a solid or illustrated opaque
background (the pale beige/gray tone used elsewhere in this style is a
good default). There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, up to 2 lines):
表題部所有者と登記名義人、何が違う？

Subtitle (smaller, centered, 1 line):
登記記録は「表題部」と「権利部」の二段階でできている

（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文のブロックは置かない。）

--- COLUMN A HEADER (pill-shaped badge, color: blue) ---
二つの呼び名の違い

--- COLUMN A, CARD 1 ---
Heading (bold, ONE line, ~20 characters or fewer):
表題部所有者
Illustration: Isometric scene: an open registry book whose left page is labeled 「表題部」 with a person icon on it and a torn-paper tag reading 「所有者らしい」; the right page of the book is blank gray and empty (nothing recorded there yet), with a small dashed outline to show it does not exist yet.
Words allowed inside this illustration (verbatim, nothing else): 「表題部」「所有者らしい」
Conclusion tag (blue banner below the illustration, 5-15 characters):
表題登記のみ・対抗力なし

--- COLUMN A, CARD 2 ---
Heading (bold, ONE line, ~20 characters or fewer):
所有権の登記名義人
Illustration: Isometric scene: the same registry book, now with both pages filled: the left page labeled 「表題部」 and the right page labeled 「権利部」 with a hanko seal stamped on it and a torn-paper tag reading 「甲区」, a small shield icon with a check mark beside the book.
Words allowed inside this illustration (verbatim, nothing else): 「表題部」「権利部」「甲区」
Conclusion tag (blue banner below the illustration, 5-15 characters):
保存登記まで完了・対抗力あり

--- COLUMN B HEADER (pill-shaped badge, color: green) ---
実務でのポイント

--- COLUMN B, CARD 3 ---
Heading (bold, ONE line, ~20 characters or fewer):
同じ人でも土地ごとに立場が違う
Illustration: Isometric scene: one stick-figure owner standing between two small land-plot tiles; the left tile carries a torn-paper tag reading 「表題部所有者」 and is labeled 「甲土地」, the right tile carries a tag reading 「所有権の登記名義人」 and is labeled 「乙土地」.
Words allowed inside this illustration (verbatim, nothing else): 「甲土地」「乙土地」「表題部所有者」「所有権の登記名義人」
Conclusion tag (green banner below the illustration, 5-15 characters):
実務でよくある混在

--- COLUMN B, CARD 4 ---
Heading (bold, ONE line, ~20 characters or fewer):
混在していてもまとめて申請できる
Illustration: Isometric scene: the two land-plot tiles 「甲土地」 and 「乙土地」 side by side, both feeding into ONE single application form document reading 「一の申請情報」, with a large green check mark stamped on the form.
Words allowed inside this illustration (verbatim, nothing else): 「甲土地」「乙土地」「一の申請情報」
Conclusion tag (green banner below the illustration, 5-15 characters):
管轄・目的・原因・日付が同じ

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji - including any Chinese-only character, Korean Hangul, other non-Japanese script, any Latin letter, any digit, or stray decorative glyph - and remove or redraw it so that only standard Japanese text appears anywhere in the image. If any character
renders as a Simplified or Traditional Chinese variant, redraw that character in the
correct Japanese form. Confirm the number of cards equals 4 exactly, with
no duplicated or missing cards, confirm that no card carries a number,
numbered circle or any numbering, confirm there is no intro
illustration or paragraph block between the header and the cards, confirm
that no card contains a full sentence of explanatory prose -
every card's takeaway must read as a short heading + a short conclusion
tag, at a glance - confirm that no illustration contains any text other
than its "Words allowed" words (no pseudo-writing) and that each allowed word is clearly legible. Confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind - the image ends immediately after the last card). Confirm the canvas is exactly 1080x1350 pixels (4:5), that all essential elements are inside the 54 px / 72 px safe margins, that the cards are in two columns as described, and that there is no footer, account name, URL, hashtag or call-to-action text anywhere in the image.
Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

文字が崩れるときは、絵の中の小さな語（「所有者らしい」「甲区」など）から外し、タイトル・見出し・結論の帯だけを残して再生成する。直すときは、最後に「次の点だけを直して、ほかは変えない：…」と1文足す。
