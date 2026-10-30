"""各年度の記事の「インフォグラフィック プロンプト（問題全体）」から、
Instagram用（3:4、1080×1440）のプロンプトとキャプション案を作る。

使い方：
    python3 note-unei/instagram/make_ig_prompts.py

出力：
    prompts/R08.md … prompts/H17.md（年度ごとに問1〜問20）
    prompts/index.csv（年・問・タイトル・元のカード数・状態）

記事は編集しない。記事の「問題全体」のプロンプトを読み取り、次の3つだけを変える：
  1. 大きさの指定を 1080x1440（3:4）にする。
  2. Instagram用の指示（INSTAGRAM FEED FORMAT）を、スタイルの段落の直後に差し込む。
  3. 最後の確認に、大きさ・余白・画像内に案内の文字を入れないことの確認を足す。
カードの見出し・イラスト・許可する語・結論タグは、記事のまま変えない（結論は記事を正とする）。
カードが4〜6枚でない問は、3:4に収めるために絞り方の判断が要るので「要手作業」と印を付ける。
"""
import csv
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'prompts')

YEARS = [('R', n) for n in range(8, 0, -1)] + [('H', n) for n in range(30, 16, -1)]

IG_BLOCK = '''INSTAGRAM FEED FORMAT (critical — this overrides every other statement about size or layout in this prompt):
the canvas is EXACTLY 1080x1440 pixels, portrait 3:4 (NOT 9:16). It is for an Instagram feed post and is
shown as a 3:4 thumbnail on the profile grid, so nothing important may touch the edges.
- Safe area: keep the title, subtitle, every card heading, every illustration and every conclusion tag inside
  a margin of 54 px on the left and right and 72 px at the top and bottom. Fill the margin with the
  opaque background only.
- Layout: a header band at the top (title and subtitle, about 16% of the height), then the cards.
  Arrange the cards in TWO columns, reading left column first, top to bottom, then the right column.
  If column or group headers are specified below, keep them as pill-shaped badges above their cards.
  If three groups are specified, place the first two groups side by side and the third group as a
  full-width row at the bottom. The cards are compact: the illustration takes about 55% of the card
  height, the heading is ONE line and the conclusion tag is ONE line. The layout must not need more than
  1440 px of height: shrink the illustrations, never the text.
- Text size for a phone screen (1080 px wide): title 72 px or larger, subtitle 36 px or larger, card
  heading 36 px or larger, conclusion tag 32 px or larger, any word inside an illustration 32 px or
  larger. If the text does not fit, shorten nothing: make the illustrations smaller.
- Do NOT draw any footer, account name, URL, hashtag, logo, watermark or call-to-action text anywhere in
  the image. The only text on the canvas is the title, the subtitle, the column or group headers, the
  card headings, the conclusion tags and the words allowed inside the illustrations.

'''

FINAL_ADD = ('Confirm the canvas is exactly 1080x1440 pixels (3:4), that all essential elements are inside the '
             '54 px / 72 px safe margins, that the cards are in two columns as described, and that there is no '
             'footer, account name, URL, hashtag or call-to-action text anywhere in the image.\n')


HEAD_RE = re.compile(r'^Heading(?: \([^)]*\))?:[ \t]*\n?(.+)$', re.M)

BADGE_ADD = ('- Numbering: do NOT draw any number, numbered circle or numbered badge on any card. Ignore every '
             '"Badge" line below (the cards are not numbered).\n')


def year_label(k, n):
    return f'令和{n}年度' if k == 'R' else f'平成{n}年度'


def year_code(k, n):
    return f'{k}{n:02d}'


def extract(path):
    t = open(path, encoding='utf-8').read()
    head = t.split('\n', 1)[0]
    m = re.search(r'第(\d+)問(?:（改）)?[〜～](.+?)[〜～]\s*$', head)
    title = m.group(2) if m else ''
    mm = re.search(r'## インフォグラフィック プロンプト（問題全体）.*?\n```\n?(.*?)\n```', t, re.S)
    if not mm:
        raise SystemExit(f'「問題全体」のプロンプトが無い：{path}')
    return title, mm.group(1)


def convert(p):
    """戻り値：(新しいプロンプト, 元のカード数, 問題があれば理由)"""
    notes = []
    n_cards = len(re.findall(r'^--- (?:COLUMN [A-Z], )?CARD \d+[^\n]*? ---', p, re.M))
    n_groups = len(re.findall(r'^--- COLUMN [A-Z] HEADER', p, re.M))
    new, k = re.subn(r'portrait layout, \d+[x×]\d+ pixels', 'portrait layout, 3:4 aspect ratio, 1080x1440 pixels', p, count=1)
    if k != 1:
        notes.append('大きさの指定を読み取れない')
    anchor = None
    for key in ('GLANCEABLE-POSTER REQUIREMENT', 'CRITICAL TEXT REQUIREMENT'):
        if key in new:
            anchor = key
            break
    if anchor is None:
        notes.append('差し込む位置を読み取れない')
    else:
        i = new.index(anchor)
        block = IG_BLOCK.rstrip('\n') + '\n' + (BADGE_ADD if 'Badge:' in p else '') + '\n'
        new = new[:i] + block + new[i:]
    # 最後の確認の直前に足す（最後の「Confirm the entire canvas」の段落の前）
    j = new.rfind('Confirm the entire canvas')
    if j == -1:
        new = new.rstrip('\n') + '\n' + FINAL_ADD
    else:
        new = new[:j] + FINAL_ADD + new[j:]
    if n_cards < 4 or n_cards > 6:
        notes.append(f'カードが{n_cards}枚：3:4では4〜6枚に絞る必要がある（絞り方を決めてから使う）')
    n_heads = len(HEAD_RE.findall(p))
    if n_heads != n_cards:
        notes.append(f'カードの見出しが{n_heads}個で、カード数{n_cards}と合わない：キャプション案を確かめる')
    if n_groups >= 3:
        notes.append('グループが3つ：配置を確かめる')
    return new, n_cards, notes


def captions(label, q, title, p):
    heads = HEAD_RE.findall(p)
    tag = '#' + label
    lines = [f'【{label} 問{q}】{title}', '', 'この問題の確認ポイント：']
    lines += [f'・{h.strip()}' for h in heads]
    lines += ['', '各肢の正誤は現行の法令で確かめ、根拠の条文は原文と照合した解説を、noteにまとめています。',
              'くわしくはプロフィールのリンクから。', '',
              f'#土地家屋調査士 #調査士試験 {tag} #過去問']
    return '\n'.join(lines)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    index = []
    flagged = 0
    for k, n in YEARS:
        code = year_code(k, n)
        label = year_label(k, n)
        folder = os.path.join(ROOT, 'note-articles', f'{k.lower()}{n}-mondai')
        out = [f'# {label}　Instagram用（3:4・1080×1440）のインフォグラフィック プロンプト', '',
               '記事の「インフォグラフィック プロンプト（問題全体）」を元に、`make_ig_prompts.py` で作る（手で直さない。直すときは記事か`make_ig_prompts.py`を直して作り直す）。',
               '使い方：ChatGPTなどに、下の「3:4画像プロンプト」のコードブロックをそのまま貼る。仕上がりは、文字を1字ずつ確かめ、記事の結論と食い違わないか確かめる。', '',
               '画像の保存名は `schedule.csv` の `feed_image`。本文は「キャプション案」を下書きにする（`caption-template.md`）。', '']
        for q in range(1, 21):
            hits = sorted(glob.glob(os.path.join(folder, f'q{q:02d}-*.md')))
            assert len(hits) == 1, (code, q)
            title, p = extract(hits[0])
            new, nc, notes = convert(p)
            assert '```' not in new
            src = os.path.relpath(hits[0], ROOT)
            status = '要手作業' if notes else 'プロンプト作成済み'
            if notes:
                flagged += 1
            out += [f'## {label} 第{q}問｜{title}', '',
                    f'- 出典の記事：`{src}`', f'- 元のカード数：{nc}', f'- 状態：{status}']
            for x in notes:
                out.append(f'- ⚠ {x}')
            out += ['', '### 3:4画像プロンプト（ChatGPTに貼る）', '', '```', new.rstrip('\n'), '```', '',
                    '### キャプション案', '', '```', captions(label, q, title, p), '```', '', '---', '']
            index.append([code, f'Q{q:02d}', title, nc, status, '；'.join(notes), src])
        with open(os.path.join(OUTDIR, f'{code}.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out))
    with open(os.path.join(OUTDIR, 'index.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['year', 'item', 'title', 'cards', 'status', 'notes', 'source'])
        w.writerows(index)
    print(f'{len(index)}問のプロンプトを書き出した（要手作業 {flagged}問）：{OUTDIR}')


if __name__ == '__main__':
    main()
