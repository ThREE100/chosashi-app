"""noteに貼る毎日ドリルの、タイトルと見出し画像のプロンプトを note/ に作る。
本文は、out/ のHTML（またはそれを画像にしたもの）をそのまま貼るので作らない。
タイトルの番号は day001-AM / day001-PM。見出し画像にも同じ番号を入れる。
見出し画像は、女性のMCキャラクター1人だけ（トリ先生・藍子は入れない）。キャラクターシート MC-01〜MC-04 を添付して使う。
使い方: python3 daily-drill/note_build.py 1      （第1日の分を作る。1〜7）"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'note')

# noteタイトルの設定ルール（固定。番号は day001 のように3けた）
TITLE_AM = '【土地家屋調査士試験】Day{day:03d}-AM_毎朝10分ドリル ｜択一＋条文の空欄補充'
TITLE_PM = '【土地家屋調査士試験】Day{day:03d}-PM_毎日これだけ ｜記述式演習'
TITLE_RE = re.compile(r'^【土地家屋調査士試験】Day\d{3}-(AM_毎朝10分ドリル ｜択一＋条文の空欄補充|PM_毎日これだけ ｜記述式演習)$')

PM_TOPIC = {   # 夜の内容ごとの見出し画像の文言と情景
    'radial': ('記述式の計算練習', '計算練習', 'a sketch of a survey instrument (total station) on a tripod and a coordinate grid with a few survey points', 'a plain calculator, a pencil and a sheet of scratch paper with only drawn lines (no numbers or letters)'),
    'intersection': ('記述式の計算練習', '計算練習', 'two straight boundary lines crossing on a coordinate grid, the crossing point marked by a small circle', 'a plain calculator, a pencil and a sheet of scratch paper with only drawn lines (no numbers or letters)'),
    'foot': ('記述式の計算練習', '計算練習', 'a straight boundary line on a coordinate grid with a perpendicular dropped from a point, a small right-angle mark', 'a plain calculator, a pencil and a sheet of scratch paper with only drawn lines (no numbers or letters)'),
    'parallel': ('記述式の計算練習', '計算練習', 'two parallel lines on a coordinate grid and a third line crossing them', 'a plain calculator, a pencil and a sheet of scratch paper with only drawn lines (no numbers or letters)'),
    'area': ('記述式の計算練習', '計算練習', 'a quadrilateral land parcel on a coordinate grid with its two diagonals drawn', 'a plain calculator, a pencil and a sheet of scratch paper with only drawn lines (no numbers or letters)'),
    'draw': ('記述式の作図練習', '作図練習', 'a drafting table with a scale ruler, a triangle ruler and a pencil, and a plain sheet with only a ruled frame (no letters)', 'a plain survey map style sketch with only lines and small dots (no numbers or letters), and a compass-like north arrow shape'),
    'shinsei': ('記述式の申請書練習', '申請書練習', 'a stack of blank application forms and a stamp, no text on them', 'a fountain pen, a seal (inkan) and an official-looking blank form with only ruled boxes (no letters)'),
}

AM_LEFT = 'a softly faded open law book with a ribbon bookmark and a pencil, no text on the pages'
AM_RIGHT = 'a softly faded worksheet sheet with several empty bracket-shaped blanks drawn as plain underlined gaps (no letters inside), and a pencil'


NIGHT_STYLE = ("STYLE: soft Japanese watercolor-like illustration of a calm, cozy NIGHT scene (this is the evening drill): a deep navy-to-indigo night sky with a gentle crescent moon, "
               "a scattering of soft twinkling stars and faint wisps of night clouds, with a warm golden desk-lamp glow near the character. Clean outlines, consistent with the note.com explainer-column "
               "header images of the same series (same watercolor touch, same layout), only the time of day is night. Keep exactly the same overall layout: the title block at the top center, "
               "the single character at the bottom center, and topic scenes fading softly into the left and right edges.\n"
               "Fill the whole canvas with the night sky (navy and indigo, soft stars, crescent moon); do not draw a daytime sky, a sun, or a bright blue sky. Light the character softly with the warm lamp light so her face stays clear and friendly.")


def _night(p):
    """見出し画像のプロンプトを夜の背景にする（夜の記述式用）。昼の空の指定を夜空に置き換え、文字が夜空でも読めるよう、題の後ろの光を明るくする。"""
    a = p.index('STYLE:')
    b = p.index('Fill the whole canvas with the pastel sky and soft clouds.') + len('Fill the whole canvas with the pastel sky and soft clouds.')
    p = p[:a] + NIGHT_STYLE + p[b:]
    p = p.replace('over a soft white cloud-shaped glow so it reads clearly', 'over a soft, bright cream-white moonlit cloud-shaped glow panel so the dark navy text reads clearly against the night sky')
    return p


def prompt(badge, l1, l2, hl, sub, left, right, kj, night=False):
    out = f"""Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this header image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: The title and the subtitle must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, with no Latin letters and no digits. There are exactly two exceptions: (1) the numbering badge described below, which is half-width Latin letters, digits, and a hyphen, written exactly as given; and (2) the number 10 in the subtitle band, which must be the half-width Arabic digits 1 and 0 (never kanji numerals), written exactly as given. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
{l1}
Line 2 is larger; the phrase {hl} is red-orange and the rest is dark navy:
{l2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{sub}
NUMBERING BADGE: in the top-left corner, a small rounded green (#009775) pill with white bold half-width text, exactly this string and nothing else (a capital letter D, lowercase "ay", then the three digits, a hyphen, and capital letters):
{badge}
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: {left}
Right side: {right}

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character, the title, and the numbering badge away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the numbering badge ({badge}), the two title lines, and the subtitle (whose number 10 is written with Arabic digits), reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the character's face are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji {kj}; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the MC character is the only character in the image (no トリ先生, no 藍子), that she matches the attached MC character sheets, and that she keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is."""
    if night:
        out = _night(out)
    return out


def pm_sentence(p):
    """夜（記述式）のnote本文の冒頭に書く、どのような問題かの説明（1文）"""
    m = p.get('minutes') or 15
    t = p['title']
    if p['kind'] == 'shinsei2':
        form = t.split('の申請書')[0]
        return f'今夜の記述式は、問題文・登記記録などの資料を読み取って、{form}の申請書の各欄（登記の目的・添付情報・申請人・土地や建物の表示など）を完成させる問題です（目安{m}分）。'
    if p['kind'] == 'draw':
        what = '地積測量図' if '地積測量図' in t else '建物図面・各階平面図'
        return f'今夜の記述式は、与えられた座標・寸法から{what}を縮尺どおりに作図し、図面に書く事項（辺の長さ・地積や床面積・距離など）を判断する作図問題です（目安{m}分）。'
    head, _, rest = t.partition('：')
    topic = f'{head}（{rest}）' if rest else head
    return f'今夜の記述式は、地積測量図や観測値などの資料から、{topic}を関数電卓の座標計算で求める計算問題です（目安{m}分）。'


def build(day):
    os.makedirs(OUT, exist_ok=True)
    pm = [json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(HERE, 'evening', 'problems', 'PM-*.json'))]
    pm = [p for p in pm if p['day'] == day][0]
    items = []
    for ampm, title, l1, l2, hl, sub, left, right, kj, body in (
        ('AM', TITLE_AM.format(day=day),
         '毎朝ドリル', '択一と条文の空欄補充', '空欄補充', '土地家屋調査士　毎朝10分', AM_LEFT, AM_RIGHT, '択、筆、界、補、充、欄', f'out/day{day:03d}-am.html（問題）／out/day{day:03d}-am-ans.html（解答）'),
        ('PM', None, '毎日これだけ', None, None, '土地家屋調査士　記述式　毎晩15分', None, None, '記、述、練、習', f'out/day{day:03d}-pm.html（問題）／out/day{day:03d}-pm-ans.html（解答）')):
        if ampm == 'PM':
            key = {'PM-01': 'radial', 'PM-04': 'foot', 'PM-07': 'area', 'PM-08': 'intersection'}.get(pm['id'], 'shinsei') if pm['kind'] == 'calc2' else ('draw' if pm['kind'] == 'draw' else 'shinsei')
            l2, hl, left, right = PM_TOPIC[key]
            l2, hl, left, right = PM_TOPIC[key][0], PM_TOPIC[key][1], PM_TOPIC[key][2], PM_TOPIC[key][3]
            what = '座標計算の練習' if pm['kind'] == 'calc2' else '申請書の欄の練習'
            title = TITLE_PM.format(day=day)
        assert TITLE_RE.match(title), title
        badge = f'Day{day:03d}-{ampm}'
        pr = prompt(badge, l1, l2, hl, sub, left, right, kj, night=(ampm == 'PM'))
        md = f"""# {badge}

## noteタイトル

{title}

## 見出し画像

- 画像に入れる番号：`{badge}`（左上の緑のバッジ）
- キャラクター：女性のMC1人だけ（トリ先生・藍子は入れない）。ChatGPTにはキャラクターシート MC-01〜MC-04 の4枚を添付して、次のプロンプトを貼る。
- 画像の文字：1行目「{l1}」／2行目「{l2}」（「{hl}」を赤橙）／サブタイトル「{sub}」

### 見出し画像のプロンプト（ChatGPTに貼る）

```
{pr}
```

## 本文

{pm_sentence(pm) + chr(10) + chr(10) + '（このあとに問題の画像を貼る：images/day%03d-pm-1.png・-2.png）' % day if ampm == 'PM' else '不要（HTMLまたはHTMLを画像にしたものを貼る）。'}

元：{body}
"""
        fn = os.path.join(OUT, f'day{day:03d}-{ampm.lower()}.md')   # ファイル名は小文字のまま
        open(fn, 'w', encoding='utf-8').write(md)
        items.append(fn)
        # 簡易チェック：番号のバッジ以外に英数字が画像の文字に入っていない
        for s in (l1, l2):
            assert not re.search(r'[0-9A-Za-z０-９]', s), s
    return items


def index():
    """note/README.md（タイトル・ファイルの一覧）を作り直す。"""
    rows = ['# note投稿の一覧（タイトルと見出し画像プロンプト）', '',
            '各ファイルに、noteタイトルと、ChatGPTに貼る見出し画像のプロンプト（女性のMC1人だけ・左上に番号バッジ）が入っている。本文は `out/` のHTML（または画像にしたもの）を貼る。キャラクターシート MC-01〜MC-04 の4枚を添付して使う。', '',
            '| 番号 | noteタイトル | ファイル | 本文の元 |', '|---|---|---|---|']
    for f in sorted(glob.glob(os.path.join(OUT, 'day*.md'))):
        t = open(f, encoding='utf-8').read().split('\n')
        title = t[4]
        m = re.search(r'Day(\d{3})-(AM|PM)', title)
        n = int(m.group(1))
        rows.append(f"| Day{m.group(1)}-{m.group(2)} | {title} | `{os.path.basename(f)}` | `out/day{n:03d}-{m.group(2).lower()}.html`・`-ans.html` |")
    open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(rows) + '\n')


if __name__ == '__main__':
    for a in sys.argv[1:] or ['1']:
        for fn in build(int(a)):
            print(fn)
    index()
