"""条文の逆引き図鑑 note記事シリーズの共通部品。
データ（dNN.py）から、記事・図解プロンプト・見出し画像プロンプトを組み立てる。
数字・正誤・条文の原文は、図鑑のデータ（../data/）・一問一答バンク・note-articles/laws/ から取り、手で書き写さない。"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERIES = os.path.dirname(HERE)
ZUKAN = os.path.dirname(SERIES)
ROOT = os.path.dirname(os.path.dirname(ZUKAN))
sys.path.append(os.path.join(ROOT, 'daily-drill'))
sys.path.append(os.path.join(ROOT, 'note-unei', 'instagram'))
import lawtext  # noqa: E402
from header_lock_text import HEADER_LOCK_PARA, FINAL_SENTENCE  # noqa: E402

SHI = {s['id']: s for s in json.load(open(os.path.join(ZUKAN, 'data', 'shi.json'), encoding='utf-8'))}
JOBUN = {(j['law'], j['article']): j for j in json.load(open(os.path.join(ZUKAN, 'data', 'jobun.json'), encoding='utf-8'))}
BANK = {i['id']: i for i in json.load(open(os.path.join(ROOT, 'tools', 'drill', 'data', 'items.json'), encoding='utf-8'))['items']}

SLUG = {'不動産登記法': 'hou', '不動産登記令': 'rei', '不動産登記規則': 'kisoku', '不動産登記事務取扱手続準則': 'junsoku',
        '区分所有法': 'kubun', '土地家屋調査士法': 'chousashi', '土地家屋調査士法施行規則': 'chousashi-kisoku', '民法': 'minpou'}
SHORT = {'不動産登記事務取扱手続準則': '準則'}
SITE_BASE = 'https://three100.github.io/chosashi-app/jobun/'  # 公開前（README）。公開したらこのURLで開ける見込み


def total_counts():
    shi_all = len(SHI)
    shi_cited = sum(1 for s in SHI.values() if s['cites'])
    return {'jobun': len(JOBUN), 'shi_all': shi_all, 'shi_cited': shi_cited}


def year_ja(code):
    era = '平成' if code[0] == 'h' else '令和'
    n = int(code[1:])
    return f"{era}{'元' if (era == '令和' and n == 1) else n}年度"


def shi_ref(sid):
    """'H28-Q09-イ' → '平成28年度 第9問 イ'（肢が数字なら「肢1」）。"""
    s = SHI[sid]
    lab = s['label']
    lab = f"肢{lab}" if re.fullmatch(r'[0-9①-⑩]+', lab) else lab
    return f"{s['year_ja']} 第{s['q']}問 {lab}"


def truth(sid):
    s = SHI[sid]
    b = BANK.get(s.get('bank_id') or '')
    if b is None or b.get('truth') is None:
        raise ValueError(f'{sid}: 一問一答バンクに正誤がない（令和8年度などは使わない）')
    return b['truth']


def band(law, art):
    """出た年度の帯（文字）。"""
    j = JOBUN[(law, art)]
    ys = j['year_list']
    hs = [y for y in ys if y[0] == 'h']
    rs = [y for y in ys if y[0] == 'r']
    parts = []
    if hs:
        parts.append('平成' + '・'.join(str(int(y[1:])) for y in hs))
    if rs:
        parts.append('令和' + '・'.join(('元' if y == 'r1' else str(int(y[1:]))) for y in rs))
    return f"{'、'.join(parts)}年度（{j['years']}年度・{j['shi']}肢）"


def jn(art):
    b, _, sub = art.partition('の')
    return f"第{b}条" + (f"の{sub}" if sub else "")


def law_name(law):
    return SHORT.get(law, law)


def article_text(law, art):
    return lawtext.article(law, jn(art))


def caption(law, art):
    t = article_text(law, art) or ''
    first = t.split('\n')[0]
    m = re.search(r'（([^）]+)）', first)
    return m.group(1) if m else ''


def quote_ok(law, art, frag):
    t = article_text(law, art)
    if t is None:
        return False
    nt = lawtext.normalize(t)
    return all(lawtext.normalize(p) in nt for p in frag.split('…') if p.strip())


def page_url(law, art):
    return f"{SITE_BASE}j/{SLUG[law]}-{art.replace('の', '-')}.html"


# ---------------------------------------------------------------- 画像プロンプト

JP_TEXT = ("CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only (hiragana, katakana, Jōyō kanji). "
           "Do NOT use Simplified Chinese or Traditional Chinese character forms; every glyph must match the standard Japanese form exactly, "
           "stroke-for-stroke. No Korean Hangul, no other script, no stray or decorative glyphs, even as small background elements. "
           "Reproduce the exact strings given below verbatim; do not paraphrase, translate, summarize or substitute any character. "
           "Half-width Arabic digits are allowed ONLY inside the given strings (for example 第39条). No Latin letters anywhere.")
TEXT_RULE = ("ILLUSTRATION TEXT RULE (critical): the only text allowed anywhere in the image is the strings written in 「」 in this prompt "
             "(絵の中に入れる文字は、指定した語だけ). This is an instruction, never text to draw. Do not invent or add any other text, number, "
             "caption, pseudo-writing, inscription on props, logo, watermark or URL. A prop that is not given a word keeps a blank surface "
             "or shows its meaning with an icon.")
NO_NUM = ("NO NUMBERING (critical): do not draw any number, numbered circle, badge or sequence mark that is not inside a given string. "
          "No figure number, no panel number, no page number.")
BG = ("BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge. No transparent or alpha-channel "
      "background, no checkerboard, no unpainted edge. Fill every corner and margin with the pale warm-cream background (#F7F3EE).")
MARKS = ("MARK COLORS: a correct rule or 'yes' is shown with a blue circle mark or blue arrow; a mistaken belief or 'no' is shown with a red "
         "cross mark or red arrow. Never put a circle and a cross in the same box. Never use green for yes.")
STYLE = ("clean flat-design illustration style with soft pastel colors (blue, beige, gray, pale orange), rounded card sections, "
         "a friendly explainer-graphic feel, dark navy text on light cards, generous margins (at least 48px), large readable type")
LAYOUT_LOCK = ("LAYOUT LOCK (critical): keep the header exactly as fixed below; align the bottom edges of cards placed side by side on the "
               "same baseline and absorb spare height inside the cards; when there are five cards, place cards 1 to 4 in a 2x2 grid and "
               "card 5 as one full-width card; never leave an empty grid cell.")
TREE_NG = re.compile(r'決定木|判定木|ツリー|木に当て|木では')

IG_SIZE = 'Instagram feed image, 1080x1440 pixels (3:4 portrait). Keep 54px side margins and 72px top and bottom margins free of text.'
IG_TAIL = 'Do not add any account name, URL, hashtag or the word note anywhere in the image.'


def strings_in(text):
    return re.findall(r'「([^」]+)」', text)


def kanji_list(text):
    hard = '号録権地番建物登記所請還筆図積続滅効準則規敷産変区画'
    return '、'.join(sorted({c for c in ''.join(strings_in(text)) if c in hard}))


def _final(text, extra=''):
    return ("Final check before rendering: confirm every string in 「」 appears exactly once where specified and verbatim, and no other text "
            "exists; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional "
            f"Chinese, paying special attention to the kanji {kanji_list(text) or '条、文'}; confirm there is no figure number or panel number; "
            "confirm blue marks only mean yes or correct and red marks only mean no or mistaken, with never both marks in one box; "
            f"{extra}confirm the entire canvas, edge to edge, is fully opaque with no transparency or alpha channel anywhere.")


def poster_prompt(title, topics, sub, cards, size='1080x1920', note=True):
    """総論（俯瞰カードポスター）。cards = [(見出し, 結論タグ, 絵の説明（英語）)]"""
    head = (f"--- HEADER ---\nTitle line 1: 「{title}」\nTitle line 2: 「{topics}」\nSubtitle: 「{sub}」\n")
    body = ['--- CARDS (each card: a short heading, a simple illustration, and one short conclusion tag; no sentences) ---']
    for i, (h, tag, ill) in enumerate(cards):
        body.append(f"Card {i + 1}: heading 「{h}」; illustration: {ill}; conclusion tag 「{tag}」")
    core = '\n'.join(body)
    canvas = (f"Create a Japanese-language infographic poster, portrait layout, {size} pixels," if note
              else f"Create a Japanese-language infographic poster for an {IG_SIZE}")
    txt = '\n\n'.join([
        canvas + '\n' + STYLE + '. Use a warm library and bookshelf motif for the frame, drawn simply.',
        'GLANCEABLE-POSTER REQUIREMENT: each card shows only its heading, one illustration and one short conclusion tag; no sentences, '
        'no quoted article text inside the cards.',
        LAYOUT_LOCK, HEADER_LOCK_PARA, JP_TEXT, TEXT_RULE, NO_NUM, BG, MARKS, head, core,
        _final(head + core, FINAL_SENTENCE + ' ') + ('' if note else '\n' + IG_TAIL)])
    return txt


def explainer_prompt(title, sub, layout, footer, size='1080x1500', note=True):
    """各論（条文の仕組みの解説図）。layout は英語の指示文で、画像に入れる語は「」で書く。"""
    canvas = (f"Create a Japanese-language explainer infographic, portrait layout, {size} pixels," if note
              else f"Create a Japanese-language explainer infographic for an {IG_SIZE}")
    head = f"--- HEADER ---\nTitle (large, bold): 「{title}」\nSubtitle (smaller, in a pale-yellow band): 「{sub}」\n"
    body = f"--- BODY ---\n{layout}\n\n--- FOOTER ---\nSmall note at the bottom: 「{footer}」"
    return '\n\n'.join([
        canvas + '\n' + STYLE + '. The image explains how one article of law works, so it may use short labels inside boxes and '
        'arrows, but keep each label short.',
        JP_TEXT, TEXT_RULE, NO_NUM, BG, MARKS, head, body,
        _final(head + body, 'confirm nothing is drawn below the footer note; ') + ('' if note else '\n' + IG_TAIL)])


def inner(s):
    """画像に入れる文字の中のかぎかっこを二重かぎかっこにする（「」は文字列の区切りに使うため）。"""
    return s.replace('「', '『').replace('」', '』')


def mistake_prompt(m, note=True):
    """間違いノート（④型）。m は dict：title, sub, wrong, right, steps, callout, footer"""
    m = {k: ([inner(x) for x in v] if isinstance(v, list) else inner(v) if isinstance(v, str) else v) for k, v in m.items()}
    canvas = ("Create a Japanese-language infographic, portrait layout, 1080x1920 pixels," if note
              else f"Create a Japanese-language infographic for an {IG_SIZE}")
    head = f"--- HEADER ---\nTitle (large, bold): 「{m['title']}」\nSubtitle (smaller): 「{m['sub']}」\n"
    steps = '\n'.join(f"  Step box {i + 1}: 「{s}」" for i, s in enumerate(m['steps']))
    body = (
        "--- TOP: TWO BOXES SIDE BY SIDE (IMPORTANT: the two boxes must show DIFFERENT marks; do not draw the same mark on both sides) ---\n"
        f"Left box, pale red background, label 「よくある思い込み」, text 「{m['wrong']}」, with ONE red cross mark only.\n"
        f"Right box, pale blue background, label 「正しい判断」, text 「{m['right']}」, with ONE blue circle mark only.\n\n"
        "--- MIDDLE: HOW TO DECIDE (vertical flow of rounded boxes joined by downward navy arrows) ---\n"
        f"{steps}\n\n"
        f"--- CALLOUT (yellow sticky-note style box) ---\nLabel 「誤りやすいポイント」, text 「{m['callout']}」\n\n"
        f"--- FOOTER ---\nSmall note: 「{m['footer']}」")
    return '\n\n'.join([
        canvas + '\n' + STYLE + '. Use a notebook-page motif (a ruled notebook page with a red margin line).',
        "MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: this image resolves one specific point of confusion; written conditions in the flow and "
        "a 1-3 sentence callout are allowed. Prioritize clarity of the reasoning.",
        JP_TEXT, TEXT_RULE, NO_NUM, BG, MARKS, head, body,
        _final(head + body, 'confirm the left box has only a red cross and the right box only a blue circle, and that nothing is drawn '
               'below the footer (no recap panel, no trophy, no extra text block); ') + ('' if note else '\n' + IG_TAIL)])


HEADER_COMMON = """CHARACTERS (critical): this header image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, or fused hands.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. No stray or decorative glyphs of any kind, even on book spines, signs or shelves: every book spine, sign, poster and label in the bookstore is blank or shows only color blocks. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances. Fill the full canvas, including every corner and margin, with the bookstore scene. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere."""


def header_prompt(h, ig=False):
    """見出し画像。h = dict(l1, l2, sub, scene, pose, face, prop)"""
    size = ('Create an Instagram feed image, 1080x1440px (3:4 portrait aspect ratio). Keep 54px side margins and 72px top and bottom '
            'margins free of text.' if ig else
            'Create a note.com article header image (eyecatch thumbnail), 1280x670px (1.91:1 landscape aspect ratio).')
    lay = ('Layout for portrait: the title block in the upper third, the character in the lower half at the center, the bookstore around her.'
           if ig else 'Layout: the title block at the top center, the character at the lower center or slightly right of center, the '
           'bookstore filling the whole canvas behind them; keep important elements inside the central 1280x454 area so the image survives cropping.')
    style = ("STYLE: soft Japanese watercolor-like illustration with clean outlines and warm light. This series uses a NEW background mood, "
             "different from the pastel-sky headers of the other series: an interior inspired by the atmosphere of a famous bookstore "
             f"(an homage only: do not copy any real logo, sign, name or exact layout). {h['scene']}")
    who = (f"POSE AND EXPRESSION (this image only, chosen so that each article in the series looks different): {h['pose']} "
           f"Her expression: {h['face']} Prop: {h['prop']} Keep her fully visible, with her face clear of the title text, and keep her "
           "hairstyle exactly as in the attached images.")
    text = ("TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top, over a soft cream "
            "glow so it reads clearly against the bookstore.\n"
            f"Line 1 (smaller, dark navy, with a pale yellow marker stroke behind it):\n{h['l1']}\n"
            f"Line 2 (larger, dark navy; the last word may be deep red-brown):\n{h['l2']}\n"
            f"Below the title, a cream rounded pill-shaped subtitle band with navy text:\n{h['sub']}\n"
            "Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no book titles, no watermark.")
    kan = '、'.join(sorted({c for c in h['l1'] + h['l2'] + h['sub'] if '一' <= c <= '鿿'}))
    fin = (f"Final check before rendering: confirm the image is exactly {'1080x1440 portrait' if ig else '1280x670 landscape'}; confirm the "
           "only text in the whole image is the two title lines and the subtitle, reproduced exactly as written, and that every book "
           f"spine and sign is blank; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, paying special attention "
           f"to the kanji {kan}; confirm the MC character is the only character in the image and matches the attached sheets; and confirm "
           "the entire canvas is fully opaque with no transparency or alpha channel anywhere.")
    parts = [size, style, lay, HEADER_COMMON, who, text, fin]
    if ig:
        parts.append(IG_TAIL)
    return '\n\n'.join(parts)
