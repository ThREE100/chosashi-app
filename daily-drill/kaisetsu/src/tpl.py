"""解説記事の図解プロンプトの共通部分（雛形）。記事ごとの文言は dayNNN.py に書く。"""

TEXT_REQ_SHORT = """CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind. Reproduce the exact text strings given below verbatim."""

TEXT_REQ_LONG = """CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Pay special attention to the kanji {kanji} — always
draw the standard Japanese (Jōyō) form."""

BG_REQ = """BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the {what} — with a solid or illustrated opaque
background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image."""


def header(n, t1, t2, topic, left, right, kanji, pose):
    """見出し画像（1280x670）。背景は朝日の差し込む部屋で固定。ポーズ・表情は記事ごとに変える（pose）。"""
    kanji = list(kanji) + [c for c in '朝' if c not in kanji]
    k = '・'.join(kanji)
    sub = f'毎朝ドリル　Day{n:03d}　{topic}'
    day = f'Day{n:03d}'
    dspell = '-'.join(day)
    digits = ', '.join(day[3:])
    return f"""Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration of a peaceful morning room. A large window lets in warm early-morning sunlight; white curtains sway gently, and long golden rays fall across a wooden desk. Use cream, warm yellow, pale green, and light blue tones, with clean outlines and a calm, fresh mood. Keep the same overall layout as the other headers in this series: title block at the top center, one character at the bottom center, and soft topic scenes fading toward the left and right edges. Fill the entire canvas with the morning room, including the window, walls, and desk.

CHARACTERS (critical): Show ONE character only: the main character (MC) from the attached character-specification sheets (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Follow the sheets closely for her face, hairstyle, hair color, outfit, and proportions; the outfit and hairstyle must stay exactly the same in every image of the series. Do not include トリ先生, 藍子, any other person, or any animal, and do not invent new accessories.

POSE AND EXPRESSION (changes every time): The pose and facial expression change in each image of the series; do not copy the pose of another header. Only the pose and expression change, never her design. For this image: {pose}

BACKGROUND (critical): The entire canvas must be fully opaque edge to edge. Do not generate a transparent or alpha-channel background, and do not leave blank white areas, checkerboard patterns, partially transparent areas, or unpainted edges.

TEXT (critical): Render only the following text, exactly as written, in standard Japanese glyph forms: hiragana, katakana, and Jōyō kanji. Do NOT use Simplified Chinese or Traditional Chinese character forms, and render no other script, no stray or decorative glyphs, no other words, no numbers, no labels, no signs, and no watermark.

Line 1, large bold rounded Japanese type in dark navy, with a pale yellow marker stroke behind it:
{t1}

Line 2, larger bold rounded Japanese type in red-orange:
{t2}

Below the title, place a light blue rounded pill-shaped subtitle band with navy text:
{sub}

The exact string {day} is required as shown (capital D, lowercase a, y, then the digits {digits}). It is the only Latin text and the only digits allowed anywhere in the image. Preserve the punctuation and spacing exactly.

TOPIC SCENES (illustration only, no text on objects):
Left side: {left}
Right side: {right}
Keep these details soft and slightly faded so they do not compete with the title or character.

LAYOUT: Keep the title and subtitle over a clear, softly glowing area near the top center. Keep the character and all important content away from the extreme edges so the image remains readable when center-cropped. Do not add flowcharts, diamonds, arrows, check marks, or cross marks.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, with {day} spelled exactly {dspell} and no other Latin letters or digits anywhere (cartoon expression marks such as ！ and ？ beside the character's face are decoration and are allowed); scan every kanji glyph, paying special attention to {k}, and confirm each is the standard Japanese (Jōyō) form; scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji and remove it; confirm the pose and expression follow the POSE AND EXPRESSION line while her face, hairstyle, and outfit match the character sheets; and confirm the entire canvas is filled with a fully opaque background."""


def poster(title, sub, col_a, col_b, cards, kanji, n_a):
    k = '・'.join(kanji)
    out = f"""Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric houses, land plots,
record sheets, deed documents, stamps, simple person figures, etc.).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the cards. Every card must communicate its point almost entirely
through the illustration (icons, check marks, small embedded labels) plus
one short heading and one short conclusion tag. Do NOT render any
full-sentence explanation, legal citation, or paragraph of body text
anywhere on the poster. If a piece of information cannot be expressed as a
short label (a few words) or drawn as an icon, leave it out rather than
writing it as prose.

{TEXT_REQ_LONG.format(kanji=k)}

ILLUSTRATION TEXT RULE (critical): the only text allowed inside the illustrations is the
specified words (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw.
Inside every illustration (on objects, signs, papers, documents, stamps and
any other prop), render ONLY the words written in 「」 in that card's
Illustration line (and repeated on the "Words allowed" line under it), each
one large, clear and exactly as written. Do not invent or add any other
text inside an illustration: no extra signs, labels, captions, numbers or
pseudo-writing. If a prop needs no specified word, leave its surface blank
or show its meaning with an icon or a mark instead. The title, subtitle,
column headers, card headings and conclusion tags are the only other text
on the poster.

{BG_REQ.format(what='cards/columns')}

NO NUMBERING (critical): do not draw any number, numbered circle, badge or
sequence mark on or near any card. The cards are not numbered.

COLOR RULE FOR MARKS: any check mark is drawn in green and any cross or
prohibition mark is drawn in red, regardless of the color of the column it
sits in. Draw only the legally correct rule on every card; never draw a
sentence that states a wrong rule. This poster uses no cross marks.

--- HEADER ---
Title (large, bold, 1行):
{title}

Subtitle (smaller, centered, 1行):
{sub}

（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文のブロックは置かない。）
"""
    for i, c in enumerate(cards):
        col, color = ('A', 'green') if i < n_a else ('B', 'blue')
        if i == 0:
            out += f"\n--- COLUMN A HEADER (pill-shaped badge, color: green) ---\n{col_a}\n"
        if i == n_a:
            out += f"\n--- COLUMN B HEADER (pill-shaped badge, color: blue) ---\n{col_b}\n"
        words = ''.join(f'「{w}」' for w in c['words']) if c['words'] else '（なし。絵の中には文字を入れない）'
        out += f"""
--- COLUMN {col}, CARD {i + 1} ---
Heading (bold, ONE line, ~20 Japanese characters or fewer):
{c['h']}
Illustration: {c['ill']} Write every word that may appear inside the illustration in 「」 in this line.
Words allowed inside this illustration (verbatim, nothing else): {words}
Conclusion tag (a short colored banner/pill directly below the illustration, {color}, 5-15 Japanese characters, a keyword phrase — NOT a sentence, NOT a legal citation):
{c['tag']}
"""
    out += f"""
--- FOOTER ---

Final check before rendering: scan every kanji glyph, paying special attention to {k}, and confirm each is in standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese. Scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji and remove it. Confirm the number of cards equals 5 exactly, with no duplicated or missing cards, confirm that no card carries a number, numbered circle or any numbering, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose — every card's takeaway must read as a short heading + a short conclusion tag, at a glance — confirm that no illustration contains any text other than its "Words allowed" words and that each allowed word is clearly legible, confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind — the poster ends immediately after the last card), and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere."""
    return out


def notebook(title, sub, req, layout, callout, footer, kanji, what, check):
    """④ 間違いノート。req=この画像で使う要素の説明、layout=本体の指定、check=Final checkの追加確認。"""
    k = '・'.join(kanji)
    return f"""Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with the
same visual language as the whole-problem poster for this article, but
built as a single detailed explainer panel rather than a multi-card
poster.

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: This image exists to resolve one
specific point of confusion, not to be a glanceable summary. Unlike a
quick-reference poster, this image MAY include {req} with written
labels and short explanatory sentences (1-3 sentences per
callout box) labeled 「誤りやすいポイント」. Prioritize clarity and
completeness of the reasoning over brevity.

{TEXT_REQ_LONG.format(kanji=k)}

ILLUSTRATION TEXT RULE (critical): the only text allowed inside the
illustrations is the specified words (絵の中に入れる文字は、指定した語だけ).
This is an instruction, never text to draw. Inside the illustrations and
diagrams, render ONLY the words that are written in this prompt (the labels,
table text and callout text given below), each one large, clear and exactly
as written. Do not add any other text, inscriptions, signs, numbers or
pseudo-writing; leave other surfaces blank or use an icon or mark instead.

{BG_REQ.format(what=what)}

--- HEADER ---
Title (large, bold):
{title}

Subtitle (smaller, centered):
{sub}

{layout}

--- CALLOUT: 誤りやすいポイント ---
誤りやすいポイント
{callout}

--- FOOTER ---
{footer}

Final check before rendering: scan every kanji glyph, paying special attention to {k}, and confirm each is in standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji, and remove or redraw it. Confirm every heading, label and callout text matches the Japanese text given above verbatim, with no paraphrasing and no substituted characters, {check}confirm nothing is rendered below the FOOTER's small footnote text (no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind), and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere."""
