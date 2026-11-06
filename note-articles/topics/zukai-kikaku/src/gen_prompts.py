"""図解プロンプト（zukai-prompts-0N.md）、見出し画像プロンプト（header-image-prompts.md）、
Instagramキャプション案（instagram-captions.md）を作る。手で直さず、data.py を直して作り直す：
  python3 note-articles/topics/zukai-kikaku/src/gen_prompts.py
図解は、すべて note用（縦長・図ごとのサイズ）と Instagram用（1080x1350・4:5）の2種類を作る。
見出し画像も note用（1280x670）と Instagram用（1080x1350・4:5）の2種類。
共通の英語の定型文は、既存の kigen-suuji-zukan/src/gen_prompts.py と topics/instagram/gen_instagram.py から読み込む（文面をそろえるため）。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NA = os.path.dirname(os.path.dirname(ROOT))
sys.path.insert(0, HERE)
from data import TOPICS  # noqa: E402

# ---- 既存の定型文を読み込む
kg = open(os.path.join(NA, 'kigen-suuji-zukan', 'src', 'gen_prompts.py'), encoding='utf-8').read()
ns = {'__file__': os.path.join(NA, 'kigen-suuji-zukan', 'src', 'gen_prompts.py')}
exec(kg[:kg.index('FIGS = []')], ns)
COMMON, FINAL, IG_EXTRA = ns['COMMON'], ns['FINAL'], ns['IG_EXTRA']

# kigen 固有のモチーフと色の約束を、この企画用に差し替える
COMMON = re.sub(r'Use a "picture book / specimen drawer" motif[^\n]*?drawn simply\.', 'Use the motif given at the end of this sentence: {motif}.', COMMON)
COMMON = re.sub(r'Color code used in every poster of this set:[^\n]*', 'Color code used in every poster of this set: blue = 表示に関する登記 (state of land and buildings), pale orange = 権利に関する登記 (rights), pale yellow and light blue = steps and neutral cards, dark navy = text.', COMMON)
assert '{motif}' in COMMON and 'pale orange = 権利' in COMMON

gi = open(os.path.join(NA, 'topics', 'instagram', 'gen_instagram.py'), encoding='utf-8').read()
a = gi.index("PROMPT = '''") + len("PROMPT = '''")
IGH = gi[a:gi.index("'''", a)]
VAR34 = dict(size='1080x1350', ratio='4:5', ty0=100, ty1=570, cy0=700, cy1=1280)   # Instagramは4:5に固定（変数名は旧名のまま）


def kanji_of(*ts):
    seen = []
    for t in ts:
        for c in t:
            if '一' <= c <= '鿿' and c not in seen:
                seen.append(c)
    return '・'.join(seen)


def words_of(body):
    ws = []
    for w in re.findall(r'「([^」]+)」', body):
        if w not in ws:
            ws.append(w)
    return ws


def build_fig(t, f, ig):
    size = '1080x1350' if ig else f['size']
    ws = words_of(f['body'])
    kj = ''.join(dict.fromkeys(re.findall(r'[一-龥]', ''.join(ws))))
    p = COMMON.format(size=size, motif=t['motif']) + f['body']
    if ig:
        p += '\n' + IG_EXTRA
    p += '\n\nWords allowed on this poster (exactly these strings, nothing else): ' + ' / '.join('「%s」' % w for w in ws) + '\n'
    p += FINAL.format(size=size) + ' Pay special attention to the kanji: ' + '、'.join(kj) + '.'
    return p


def gen_zukai():
    for i, t in enumerate(TOPICS, 1):
        if not t['figs']:
            continue
        n = t['id'][-2:]
        L = ['# %s 図解画像のプロンプト（ChatGPT用・note用とInstagram用）' % t['title'].split('〜')[0], '',
             '作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。記事 `%s.md` に差し込む図%d枚について、**note用（縦長・図ごとのサイズ）とInstagram用（1080×1350・4:5）の2種類**を用意した。' % (t['slug'], len(t['figs'])),
             '', '## 使い方', '',
             '1. 図ごとに、noteに使うなら「note用」、Instagramに使うなら「Instagram用」のコードブロックを、そのままChatGPTに貼る。文字は同じで、大きさと余白だけ違う。',
             '2. 画像の中に図番は入れない（管理番号は、PNG名と記事のマーカーだけ）。',
             '3. 色の約束：**表示に関する登記＝青、権利に関する登記＝薄い橙**。ほかの色は意味を持たせない（手順は薄い黄と水色）。同じ企画の図を並べたとき、色がそろっているか確かめる。',
             '4. ファイル名は、note用が `kz%s_zu01.png` から、Instagram用が `kz%s_ig01.png` から。' % (n, n),
             '5. 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。',
             '', '## 確かめること', '',
             '- 大きさが指定どおりか（note用は図ごとに違う、Instagram用は1080×1350）。',
             '- 文字が、各プロンプトの「Words allowed」と**1字ずつ**一致しているか（簡体字・繁体字になっていないか、余計な文字・数字がないか）。',
             '- 条文番号・項番号が正しく出ているか。',
             '- 図番（図1など）が画像に入っていないか。',
             '- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下68px）の内側にあるか。アカウント名・URLが入っていないか。',
             '- 背景が不透明か。', '',
             '文字が何度やっても崩れるときは、「Words allowed」の行を残したまま「No text」の版（文字なしの枠と絵だけ）を作らせて、文字はCanvaで入れる。', '',
             '## 図の一覧', '', '| 管理番号 | 内容 | note用のサイズ | Instagram用のサイズ |', '|---|---|---|---|']
        for f in t['figs']:
            L.append('| %s | %s | %s | 1080x1350 |' % (f['key'], f['title'], f['size']))
        L.append('')
        for j, f in enumerate(t['figs'], 1):
            L += ['## 図%d：%s（%s）' % (j, f['title'], f['key']), '',
                  '### note用（%s）' % f['size'], '', '```', build_fig(t, f, False), '```', '',
                  '### Instagram用（1080x1350・4:5）', '', '```', build_fig(t, f, True), '```', '']
        L += ['## 見出し画像', '', '見出し画像（note用 1280x670・Instagram用 1080x1350）は `header-image-prompts.md`、キャプションは `instagram-captions.md`。', '']
        open(os.path.join(ROOT, 'zukai-prompts-%s.md' % n), 'w', encoding='utf-8').write('\n'.join(L))


NOTE_HEADER = '''Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow. Line 1 is dark navy with a pale yellow marker stroke behind it:
{l1}
Line 2 is larger; the phrase {emph} is red-orange and the rest is dark navy:
{l2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{band}
Do not write any other text anywhere in the image.

TOPIC SCENES (illustration only, no text on any object; soft and slightly faded): {scene}

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji ({kanji}) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm the canvas is fully opaque.'''


def gen_header():
    L = ['# 図解企画6本 見出し画像のプロンプト（note用・Instagram用）', '',
         '作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。企画ごとに、**note用（1280×670）とInstagram用（1080×1350・4:5）の2種類**。',
         '画像の生成と目視確認はChatGPTで行う（未実施）。キャラクターシート `キャラクターシート_MC-01〜MC-04` の4枚を添付してから貼る。見出し画像のキャラクターはMC1人だけ（トリ先生・藍子は入れない）。', '',
         '## 確かめること', '',
         '- 大きさが指定どおりか（note用 1280×670、Instagram用 1080×1350）。',
         '- 文字が、各表の文面と**1字ずつ**一致しているか（簡体字・繁体字・余計な文字・数字・英字がないか）。',
         '- キャラクターがMC1人だけか。手や腕の数が合っているか。',
         '- Instagram用は、文字と主要な絵が外側の余白（左右54px・上下68px）の内側にあるか。アカウント名・URLが入っていないか。',
         '- 背景が不透明か。',
         '- 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。', '',
         '文字が崩れるときは、「TEXT」の部分を「No text」に書き換えて文字なしで作らせ、文字はCanvaなどで重ねる。', '']
    for t in TOPICS:
        h = t['header']
        L += ['## %s　%s' % (t['id'], t['title'].split('〜')[0]), '',
              '| 用途 | サイズ | 文字 |', '|---|---|---|',
              '| note用 | 1280×670 | 「%s」／「%s」／「%s」 |' % (h['l1'], h['l2'], h['band']),
              '| Instagram用 | 1080×1350 | 「%s」／「%s」／「%s」／「%s」 |' % (h['l1'], h['l2'], h['band'], h['sub']), '']
        pn = NOTE_HEADER.format(l1=h['l1'], l2=h['l2'], emph=h['emph'], band=h['band'], scene=h['scene_note'],
                                kanji=kanji_of(h['l1'], h['l2'], h['band']))
        pi = IGH.format(l1=h['l1'], l2=h['l2'], emph=h['emph'], band=h['band'],
                        sub_block='Line 4, smaller, dark navy, below the band:\n' + h['sub'] + '\n', n=4,
                        scene=h['scene_ig'].rstrip('.') + '.', kanji=kanji_of(h['l1'], h['l2'], h['band'], h['sub']), **VAR34)
        L += ['### note用（1280×670）', '', '```', pn, '```', '', '### Instagram用（1080×1350・4:5）', '', '```', pi, '```', '']
    open(os.path.join(ROOT, 'header-image-prompts.md'), 'w', encoding='utf-8').write('\n'.join(L))


def gen_captions():
    L = ['# 図解企画6本 Instagramキャプション案', '',
         '作成 2026-11-05（`src/gen_prompts.py` で作る。手で直さない）。画像のプロンプトは `zukai-prompts-0N.md`（図）と `header-image-prompts.md`（見出し）、第6回の四コマは `06-yonkoma-prompt.md`。',
         '', '## 書き方の決まり', '',
         '- Instagramの本文のリンクは押せないので、noteへは「プロフィールのリンクから」と案内する。URLは本文に書かない。',
         '- ハッシュタグは4〜5個。キャプションは2200字以内。',
         '- 個人の演習結果（誤答の回数など）と問題番号は載せない。', '']
    for t in TOPICS:
        L += ['## %s　%s' % (t['id'], t['title'].split('〜')[0]), '']
        for name, text in t['captions']:
            L += ['### %s（%d字）' % (name, len(text)), '', '```', text.rstrip('\n'), '```', '']
    open(os.path.join(ROOT, 'instagram-captions.md'), 'w', encoding='utf-8').write('\n'.join(L))


gen_zukai()
gen_header()
gen_captions()
print('ok')
