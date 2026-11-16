"""ChatGPT用のプロンプト（見出し画像・イラスト図解）を作る。記事に埋め込む。
ルールの正本：note-articles/infographic-prompt-template.md（②③）、r8-mondai/src/lib.py の header_prompt（見出し画像）、
note-unei/instagram/header_lock_text.py（3行の見出し）。"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'note-unei', 'instagram'))
from header_lock_text import HEADER_LOCK_BODY, FINAL_SENTENCE  # noqa: E402
from catalog import FIELDS  # noqa: E402

COLOR_EN = {'A': 'blue', 'B': 'teal', 'C': 'purple', 'D': 'orange', 'E': 'green', 'F': 'brown', 'G': 'slate blue-gray', 'H': 'red'}
_old = '(the year and question number only, e.g. 令和3年度 第3問; never write 午後の部 or 午前の部)'
assert _old in HEADER_LOCK_BODY
HEADER_LOCK_SERIES = HEADER_LOCK_BODY.replace(_old, '(the series tag and the field name only, written exactly as given; no year, no question number, never write 午後の部 or 午前の部)')
FINAL_SERIES = FINAL_SENTENCE.replace('no 午後の部 or 午前の部', 'no year or question number, no 午後の部 or 午前の部')

ATT = re.compile(r'[一-龥]')


def kanji(*texts, limit=30):
    seen = []
    for t in texts:
        for ch in ATT.findall(t):
            if ch not in seen:
                seen.append(ch)
    return '、'.join(seen[:limit])


def sub_line(c):
    return '一枚まとめ　' + FIELDS[c['field']][0]


def check_text_no_ascii(*ss):
    """見出し画像用：数字・英字を入れない。"""
    for s in ss:
        assert not re.search(r'[0-9A-Za-z０-９]', s), s


def check_no_latin(*ss):
    """図解用：英字は入れない（半角の数字は、与えた文字列の中だけ許す）。"""
    for s in ss:
        assert not re.search(r'[A-Za-zＡ-Ｚａ-ｚ０-９]', s), s


def header_prompt(c, h):
    l1, l2, hl = h['l1'], h['l2'], h['hl']
    assert hl in l2 and len(l1) <= 14 and len(l2) <= 14, (c['id'], l1, l2)
    sub = sub_line(c)
    check_text_no_ascii(l1, l2, sub)
    rest = l2.replace(hl, '')
    line2 = ('Line 2 is larger; the phrase %s is red-orange and the rest is dark navy:' % hl) if rest else 'Line 2 is larger and red-orange:'
    kj = kanji(l1, l2, sub)
    return """Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this header image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
%(l1)s
%(line2)s
%(l2)s
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
%(sub)s
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no numbers, no watermark.

TOPIC SCENES (illustration only, no text and no numbers on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: %(left)s
Right side: %(right)s

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the character's face are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji %(kj)s; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the MC character is the only character in the image (no トリ先生, no 藍子), that she matches the attached MC character sheets, and that she keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.""" % dict(
        l1=l1, line2=line2, l2=l2, sub=sub, left=h['left'], right=h['right'], kj=kj)


def header_prompt_ig(c, h):
    p = header_prompt(c, h)
    p = p.replace("Create a note.com article header image (eyecatch thumbnail), 1280x670px\n(1.91:1 landscape aspect ratio).",
                  "Create an Instagram feed image, portrait layout, EXACTLY 1080x1440 pixels (3:4).")
    p = p.replace("Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.",
                  "Layout: the title block in the upper part (between y=120px and y=620px), the single character at the bottom center (about y=760px to y=1360px), and the topic scenes fading softly into the left and right edges.")
    p = p.replace("LAYOUT: keep a clear, uncluttered zone behind the title and subtitle.",
                  "INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text. Make the title letters slightly larger than in the note version.\n\nLAYOUT: keep a clear, uncluttered zone behind the title and subtitle.")
    p = p.replace('confirm the image is exactly 1280x670 landscape', 'confirm the image is exactly 1080x1440 portrait (3:4)')
    assert '1280x670' not in p and '1080x1440' in p
    return p


def zukai_prompt(c, z, ig):
    """イラスト図解（②③の俯瞰カードポスター）。z: title, topics, cards[{h, illust, words, tag}]"""
    fname = FIELDS[c['field']][0]
    cards = z['cards']
    n = len(cards)
    assert 4 <= n <= 6, (c['id'], n)
    size = '1080x1440' if ig else '1080x1800'
    sub = sub_line(c)
    check_no_latin(z['title'], z['topics'], sub)
    col = COLOR_EN[c['field']]
    L = []
    a = L.append
    a('Create a Japanese-language infographic, portrait layout, %s pixels,' % size)
    a('clean flat-design isometric illustration style with soft pastel colors (blue, green, beige, gray), rounded card sections, a modern explainer-graphic aesthetic. The accent color of this poster is %s. Draw only simple, friendly icons that suit the topic.' % col)
    a('')
    a('GLANCEABLE-POSTER REQUIREMENT (critical): this is a quick-reference poster, NOT a text-heavy explainer document. There is NO intro illustration and NO paragraph of prose anywhere on this poster. Go straight from the header to the cards. Every card communicates its point almost entirely through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation or paragraph of body text. If a piece of information cannot be expressed as a short label or drawn as an icon, leave it out.')
    a('')
    a('LAYOUT LOCK (critical): the header, the bottom edge and a five-card set are fixed as follows.')
    a('- ' + HEADER_LOCK_SERIES)
    a('- BOTTOM ALIGNMENT: the cards fill the whole area from the header to the bottom margin line. The last card of each column ends on exactly the same horizontal line on that bottom margin line; cards in the same row have the same height; gaps between neighbouring cards are equal (about 24 px). Absorb spare height INSIDE the cards (larger illustration area, vertical centring, the card\'s own padding), never as an empty strip or a ragged bottom edge.')
    if n == 5:
        a('- FIVE CARDS: do NOT leave an empty slot in the grid. Place cards 1 to 4 in a 2 x 2 grid and card 5 as ONE full-width card across both columns at the bottom (illustration on the left, about 45% of the width; heading and conclusion tag on the right).')
    elif n == 4:
        a('- FOUR CARDS: place the cards in a 2 x 2 grid of equal size.')
    else:
        a('- SIX CARDS: place the cards in a 2 x 3 grid of equal size.')
    a('')
    a('CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. No Latin letters anywhere. Half-width Arabic digits and the characters 第・条・項・の are allowed ONLY inside the given strings.')
    a('')
    a('ILLUSTRATION TEXT RULE (critical): the only text allowed inside the illustrations is the specified words (絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Inside every illustration (on objects, signs, papers, documents, stones, buildings, stamps and any other prop), render ONLY the words written in 「」 in that card\'s Illustration line (and repeated on the "Words allowed" line under it), each one large, clear and exactly as written. Do not invent or add any other text inside an illustration: no inscriptions on boundary stones or markers, no extra signs, labels, captions, numbers or pseudo-writing. If a prop needs no specified word, leave its surface blank or show its meaning with an icon or a mark instead. The title, subtitle, card headings and conclusion tags are the only other text on the poster.')
    a('')
    a('NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark on or near any card. The cards are not numbered. No figure number, no panel number, no page number.')
    a('')
    a('BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background. Fill every corner and margin with a plain cream background (#F7F3EE). No checkerboard, no partially transparent area, no unpainted edge.')
    if ig:
        a('')
        a('INSTAGRAM FEED FORMAT (critical): the canvas is EXACTLY 1080x1440 pixels (3:4). Keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the bottom, because the profile grid crops the image (the header block is measured from the top edge as in HEADER LOCK). Do not draw any account name, handle, URL, hashtag or call-to-action text.')
    a('')
    a('--- HEADER ---')
    a('Title line 1 (the question title, ONE line):')
    a(z['title'])
    a('Title line 2 (the topic list, ONE line):')
    a(z['topics'])
    a('Subtitle (line 3):')
    a(sub)
    a('')
    words_all = [z['title'], z['topics'], sub]
    for i, cd in enumerate(cards, 1):
        check_no_latin(cd['h'], cd['tag'])
        assert len(cd['h']) <= 22 and 3 <= len(cd['tag']) <= 16, (c['id'], cd['h'], cd['tag'])
        a('--- CARD %d ---' % i)
        a('Heading (bold, ONE line, about 20 Japanese characters or fewer):')
        a(cd['h'])
        a('Illustration: %s' % cd['illust'])
        w = cd.get('words') or []
        a('Words allowed inside this illustration (verbatim, nothing else): %s' % (' / '.join('「%s」' % x for x in w) if w else 'none (no text of any kind inside this illustration)'))
        a('Conclusion tag (a short colored banner directly below the illustration, %s, a keyword phrase, NOT a sentence):' % col)
        a(cd['tag'])
        a('')
        words_all += [cd['h'], cd['tag']] + w
    a('--- FOOTER ---')
    a('')
    a('Final check before rendering: confirm the canvas is exactly %s pixels; %s Confirm the number of cards equals %d exactly, with no duplicated or missing cards; confirm that no card carries a number, numbered circle or any numbering; confirm there is no intro illustration or paragraph block between the header and the cards; confirm that no card contains a full sentence of explanatory prose; confirm that no illustration contains any text other than its "Words allowed" words (no inscriptions on stones or signs, no pseudo-writing) and that each allowed word is clearly legible; confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind); scan every kanji glyph, paying special attention to %s, and confirm each is the standard Japanese (Jōyō) form, not Simplified or Traditional Chinese, and remove any character that is not standard Japanese; confirm the entire canvas, edge to edge, is filled with a fully opaque background.' % (size, FINAL_SERIES, n, kanji(*words_all, limit=40)))
    return '\n'.join(L)
