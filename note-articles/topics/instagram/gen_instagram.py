#!/usr/bin/env python3
"""topics/ の個別テーマ記事ごとに、Instagram用の見出し画像プロンプトとキャプションを作る。
原稿データは data.json（IDをキーに l1/l2/emph/band/sub/scene/hook/lead/points/close/tags）。
使い方: python3 note-articles/topics/instagram/gen_instagram.py   （data.json を直して作り直す。生成物は手で直さない）
"""
import json, os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.dirname(HERE)
D = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
SHELF = {'KA':'土台','KB':'担い手','KC':'記録','KD':'共通手続','KE':'表示','KF':'権利','KG':'確かめる','KH':'周辺','KM':'民法','KT':'土地家屋調査士法'}

PROMPT = '''Create an Instagram feed cover image, portrait layout, EXACTLY {size} pixels ({ratio}).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

INSTAGRAM FEED FORMAT (critical): the profile grid crops the image, so keep every text and every important drawing inside a safe margin of 54px on the left and right and 72px at the top and bottom. Do not draw any account name, handle, URL, hashtag or call-to-action text, and no logo or watermark.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind.

BACKGROUND REQUIREMENT (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else), centered in the upper part of the canvas between y={ty0}px and y={ty1}px, over a soft white cloud-shaped glow, bold rounded font. Line 1, large, dark navy with a pale yellow marker stroke behind it:
{l1}
Line 2, very large; the phrase {emph} is red-orange and the rest is dark navy:
{l2}
Line 3, in a light blue rounded pill-shaped band with navy text:
{band}
{sub_block}Do not write any other text anywhere in the image.

SCENE: the MC character stands at the bottom center (about y={cy0}px to y={cy1}px). Behind and beside her, drawn simply and softly: {scene} No text on any object; props stay soft so they never compete with the title or the character.

LAYOUT: keep a clear, uncluttered zone behind the title block. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly {size} portrait; confirm the only text is the {n} title lines, exactly as written; scan every kanji ({kanji}) for Simplified or Traditional Chinese forms; confirm the MC character is the only character; confirm nothing important lies within the outer safe margin; confirm the canvas is fully opaque.'''

def kanji_of(*ts):
    seen = []
    for c in ''.join(ts):
        if '一' <= c <= '鿿' and c not in seen: seen.append(c)
    return '・'.join(seen)

VAR = {'34': dict(size='1080x1440', ratio='3:4', ty0=120, ty1=620, cy0=760, cy1=1360),
       '45': dict(size='1080x1350', ratio='4:5', ty0=100, ty1=570, cy0=700, cy1=1280)}

def build(i, d, fname):
    title = open(os.path.join(TOPICS, fname + '.md'), encoding='utf-8').readline().strip().lstrip('# ')
    sub = d.get('sub', '')
    sub_block = ('Line 4, smaller, dark navy, below the band:\n' + sub + '\n') if sub else ''
    n = 4 if sub else 3
    def mk(v): return PROMPT.format(l1=d['l1'], l2=d['l2'], emph=d['emph'], band=d['band'], sub_block=sub_block,
                       scene=d['scene'].strip().rstrip('.。')+'.', n=n, kanji=kanji_of(d['l1'], d['l2'], d['band'], sub), **VAR[v])
    pr, pr45 = mk('34'), mk('45')
    cap = [d['hook'], '', d['lead'], '']
    cap += ['・' + p for p in d['points']]
    cap += ['', d['close'], '', ' '.join(d['tags'])]
    cap = '\n'.join(cap)
    out = f'''# {i} Instagram用 見出し画像のプロンプトとキャプション

- 画像は3:4と4:5の2種類（どちらもキャラクターシートMC-01〜MC-04を添付して貼る）。
- 対象の記事：`note-articles/topics/{fname}.md`
- 記事の見出し：{title}
- 分類：{i[:2]} {SHELF[i[:2]]}
- 画像の生成と目視確認はChatGPTで行う（未実施）。キャラクターシート `キャラクターシート_MC-01〜MC-04` の4枚を添付してから貼る。

## 画像の文字（1字ずつ確かめる）

| 行 | 文字 |
|---|---|
| 1行目 | {d['l1']} |
| 2行目 | {d['l2']}（強調：{d['emph']}） |
| 帯 | {d['band']} |
| 4行目 | {sub or '（なし）'} |

## 見出し画像プロンプト 3:4（1080×1440・ChatGPTに貼る）

```
{pr}
```

## 見出し画像プロンプト 4:5（1080×1350・Instagram投稿用）

3:4版と同じ文字・同じ絵柄で、縦横比だけを4:5にしたもの。キャラクターは、キャラクターシート（MC-01〜MC-04）を添付して参照させる。

```
{pr45}
```

文字が崩れるときは、「TEXT」の部分を「No text」に書き換えて文字なしで作らせ、文字はCanvaなどで重ねる。直すときは、最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

## キャプション案（{len(cap)}字）

```
{cap}
```

- Instagramは本文のリンクを押せないので、noteへは「プロフィールのリンク」で案内している（`note-unei/instagram/caption-template.md`）。
- 画像の中には、アカウント名・URL・ハッシュタグ・案内の文字を入れない。
'''
    return out, len(cap)

def main():
    files = {os.path.basename(p)[:5]: os.path.basename(p)[:-3] for p in glob.glob(os.path.join(TOPICS, 'K*_*.md'))}
    rows = []
    for i in sorted(files):
        if i not in D: raise SystemExit('data.json に %s がない' % i)
        out, n = build(i, D[i], files[i])
        open(os.path.join(HERE, f'{i}.md'), 'w', encoding='utf-8').write(out)
        rows.append((i, files[i], D[i]['l1'] + D[i]['l2'], n))
    idx = ['# 個別テーマ記事のInstagram用 見出し画像プロンプトとキャプション', '',
           '2026-11-04 作成。`topics/` の個別テーマ記事（KA〜KT、' + str(len(rows)) + '本）ごとに、Instagram（1080×1440）の見出し画像（表紙）のプロンプトと、キャプション案を保存した。',
           '`gen_instagram.py` が `data.json`（原稿データ）から作る。**生成物は手で直さず、`data.json` を直して作り直す**。つなぎ（F2：個別テーマ）の枠に、1日1枚ずつ出す使い方を想定している（`note-unei/instagram/README.md`）。', '',
           '| ID | 画像の文字 | キャプション字数 | ファイル |', '|---|---|---|---|']
    for i, f, t, n in rows: idx.append(f'| {i} | {t} | {n} | [{i}.md]({i}.md) |')
    open(os.path.join(HERE, 'README.md'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
    print(len(rows), 'files')
main()
