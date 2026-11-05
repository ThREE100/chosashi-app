#!/usr/bin/env python3
"""topics/ の個別テーマ記事すべてに、note用の見出し画像プロンプト(1280x670)を作って記事本文に入れる。
文字は instagram/data.json の l1/l2/emph/band を使う。背景は「壮麗な図書館の館内」(2026-11-05 ユーザー指示)。
使い方: python3 note-articles/topics/gen_note_header.py   (data.json か、このスクリプトを直して作り直す。冪等)
"""
import json, os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'instagram', 'data.json'), encoding='utf-8'))
H2 = '## 見出し画像プロンプト（note用・1280×670）'

def kanji_of(*ts):
    seen = []
    for c in ''.join(ts):
        if '一' <= c <= '鿿' and c not in seen: seen.append(c)
    return '・'.join(seen)

GEN = '''Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with clean outlines, light and gentle brushwork, consistent with the note.com explainer-column header images of the same series.

BACKGROUND (critical): the whole canvas is the interior of a magnificent, elegant library, drawn softly in the same pastel watercolor style. Show tall bookshelves filled with books, stone arched windows, heavy wooden interior, an ornamented ceiling, and soft warm lighting. Give the background depth (receding shelves and arches) and a bright, refined, calm atmosphere. Keep the colors pale and gentle (warm cream, light wood brown, soft gold, pale stone gray); never dark, heavy or dramatic. The library fills the canvas to every edge.

LEFT AND RIGHT BACKGROUND: only library architecture and shelves on both sides. Do NOT add people, animals, props that explain the topic, items on a desk, icons or diagrams. The side shelves and windows must stay quiet and never stand out more than the title or the character.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic, and choose a different pose each time this image is generated. Place her at the bottom center, fully visible, with her face clear of the title text. Keep her human anatomy strictly correct: exactly one head, one torso, two arms and two hands in total, each hand with exactly five fingers; no extra or floating hands or arms.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese or Traditional Chinese characters; every glyph must match the standard Japanese form exactly. Reproduce the exact text strings given below verbatim; do not paraphrase or substitute any character. No stray or decorative glyphs of any kind. Draw no text on the books, signs or walls.

BACKGROUND OPACITY (critical): the entire canvas must be fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a bright, clean, soft white cloud-shaped glow so that the area behind the title is light and uncluttered. Line 1 is dark navy with a pale yellow marker stroke behind it:
{l1}
Line 2 is larger; the phrase {emph} is red-orange and the rest is dark navy:
{l2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{band}
Do not write any other text anywhere in the image.

LAYOUT: title block at the top center, the single character at the bottom center, library on both sides and behind. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, arrow between boxes, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text is the two title lines and the subtitle, exactly as written; scan every kanji ({kanji}) for Simplified or Traditional Chinese forms; confirm the background is a bright, elegant library interior with no people, animals or topic props on the sides; confirm the MC character is the only character; confirm the canvas is fully opaque.'''

EDIT = '''添付した見出し画像をもとに、note.comの記事用ヘッダー画像を編集してください。画像サイズは横長の1280×670ピクセルです。

【変更する部分】
背景を、壮麗な図書館の館内にしてください。高い本棚、石造りのアーチ窓、木を使った重厚な内装、装飾のある天井、柔らかな暖色の照明を描きます。元画像の構図や落ち着いた雰囲気を生かしつつ、シリーズの水彩風イラストになじむ、淡く柔らかな描写にしてください。背景全体に奥行きを持たせ、明るく上品な印象にします。

【そのまま維持する部分】
元画像のタイトル文字、書体、色、サイズ、配置を変えないでください。文字を追加・削除・言い換えたり、文字の形を変えたりしないでください。
元画像の女性キャラクターも、顔、髪型、髪色、服装、ポーズ、サイズ、配置を維持してください。キャラクターは一人だけにします。

【左右の背景】
左右には、図書館の内装だけを描きます。人物、動物、テーマを説明する小物、机上の物、アイコン、図解は追加しないでください。左右の本棚や窓は背景として自然に配置し、タイトルやキャラクターより目立たせないでください。

【仕上げ】
タイトルの背後は明るくすっきりさせ、文字を読みやすく保ちます。画像の端まで背景を描き、透明部分や未着色部分を残さないでください。元画像のタイトルとキャラクターの位置関係は変えず、背景だけを差し替えてください。'''

def section(i):
    d = D[i]
    p = GEN.format(l1=d['l1'], l2=d['l2'], emph=d['emph'], band=d['band'], kanji=kanji_of(d['l1'], d['l2'], d['band']))
    return f'''{H2}

noteの見出し画像（アイキャッチ）用です。キャラクターシート `キャラクターシート_MC-01〜MC-04` の4枚を添付してから貼ります。キャラクターはMC1人だけです（トリ先生・藍子は描きません）。背景は壮麗な図書館の館内（2026-11-05 ユーザー指示）で、左右には図書館の内装だけを描き、人物・動物・テーマを説明する小物・アイコンは入れません。画像の生成と目視確認は未実施です。

| 行 | 文字 |
|---|---|
| 1行目 | {d['l1']} |
| 2行目 | {d['l2']}（強調：{d['emph']}） |
| 帯 | {d['band']} |

確かめること：大きさが1280×670か／文字が上の表と1字ずつ一致しているか（簡体字・繁体字・余計な文字・数字・英字がないか）／背景が明るい図書館の館内で、左右に人物・動物・小物がないか／キャラクターがMC1人だけか／手や腕の数が合っているか／タイトルの背後が明るくすっきりしているか／背景が不透明か。

### A. 新規に生成する（ChatGPTに貼る）

```
{p}
```

### B. すでにある見出し画像の背景だけを差し替える（元の見出し画像を添付して貼る）

```
{EDIT}
```

文字が崩れるときは、Aの「TEXT」を「No text」に書き換えて文字なしで作らせ、文字はCanvaなどで重ねる。直すときは、最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

'''

def split(s):
    """## で始まる節に分ける。先頭(タイトル行など)を含む。"""
    parts = re.split(r'(?m)^(?=## )', s)
    return parts

def apply(path, i):
    s = open(path, encoding='utf-8').read()
    parts = split(s)
    parts = [x for x in parts if not x.startswith('## 見出し画像プロンプト')]
    new = section(i)
    idx = None
    for pat in ('## インフォグラフィック プロンプト', '## 見出し画像用フレーズ', '## 参照した', '## 関連'):
        for k, x in enumerate(parts):
            if x.startswith(pat): idx = k; break
        if idx is not None: break
    if idx is None:
        if not parts[-1].endswith('\n'): parts[-1] += '\n'
        parts.append('\n' + new if not parts[-1].endswith('\n\n') else new)
    else:
        if not parts[idx-1].endswith('\n\n'): parts[idx-1] = parts[idx-1].rstrip('\n') + '\n\n'
        parts.insert(idx, new)
    out = ''.join(parts)
    open(path, 'w', encoding='utf-8').write(out)

n = 0
for path in sorted(glob.glob(os.path.join(HERE, 'K*_*.md'))):
    i = os.path.basename(path)[:5]
    if i not in D: print('data.jsonにない', i); continue
    apply(path, i); n += 1
print(n, 'files')
