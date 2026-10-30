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
カードが7枚以上ある3問は、**2枚に分けて作る**（1つの投稿に2枚。複数枚をめくる投稿＝カルーセル）。
分け方は SPLITS に決めてある。分けた2枚は、それぞれ別のプロンプトになる（カードの中身は記事のまま）。
そのほか、カードが4〜6枚でない問、グループが3つの問は「要手作業」と印を付ける。
"""
import csv
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'prompts')

YEARS = [('R', n) for n in range(8, 0, -1)] + [('H', n) for n in range(30, 16, -1)]

IG_HEAD = '''INSTAGRAM FEED FORMAT (critical — this overrides every other statement about size or layout in this prompt):
the canvas is EXACTLY 1080x1440 pixels, portrait 3:4 (NOT 9:16). It is for an Instagram feed post and is
shown as a 3:4 thumbnail on the profile grid, so nothing important may touch the edges.
- Safe area: keep the title, subtitle, every card heading, every illustration and every conclusion tag inside
  a margin of 54 px on the left and right and 72 px at the top and bottom. Fill the margin with the
  opaque background only.
'''

LAYOUT_TWO = '''- Layout: a header band at the top (title and subtitle, about 16% of the height), then the cards.
  Arrange the cards in TWO columns, reading left column first, top to bottom, then the right column.
  If column or group headers are specified below, keep them as pill-shaped badges above their cards.
  If three groups are specified, place the first two groups side by side and the third group as a
  full-width row at the bottom. If only ONE group header is specified, make it a full-width pill-shaped
  badge above all the cards. The cards are compact: the illustration takes about 55% of the card
  height, the heading is ONE line and the conclusion tag is ONE line. The layout must not need more than
  1440 px of height: shrink the illustrations, never the text.
'''

LAYOUT_ONE = '''- Layout: a header band at the top (title and subtitle, about 16% of the height), then the group header
  (a full-width pill-shaped badge) and the cards as ONE column of wide, stacked, full-width cards: in each
  card the illustration is on the left (about 45% of the card width) and the heading and the conclusion
  tag are on the right. Use the extra space to make the illustrations larger. The layout must not need
  more than 1440 px of height.
'''

IG_TAIL = '''- Text size for a phone screen (1080 px wide): title 72 px or larger, subtitle 36 px or larger, card
  heading 36 px or larger, conclusion tag 32 px or larger, any word inside an illustration 32 px or
  larger. If the text does not fit, shorten nothing: make the illustrations smaller.
- Do NOT draw any footer, account name, URL, hashtag, logo, watermark or call-to-action text anywhere in
  the image. The only text on the canvas is the title, the subtitle, the column or group headers, the
  card headings, the conclusion tags and the words allowed inside the illustrations.
'''

# 年度コード・問 → 2枚に分ける（カード番号の組）。サブタイトルの末尾に（前半）（後半）を付ける。
SPLITS = {
    ('H30', 'Q11'): {'parts': [[1, 2, 3, 4, 5, 6], [7, 8, 9]], 'why': '区分建物の語句（6）と敷地権の語句（3）に、種類で分ける'},
    ('H19', 'Q19'): {'parts': [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                     'why': '「建物として扱えるもの」7つは1枚に収まらないので5と5に分け、2枚目に扱えるもの2つと扱えないもの3つを並べる'},
    ('H18', 'Q07'): {'parts': [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 'why': '「宅地になる」（5）と「宅地・雑種地以外／雑種地」（5）に、種類で分ける'},
}

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


GROUP_RE = re.compile(r'^--- COLUMN [A-Z] HEADER[^\n]*---$', re.M)
CARD_RE = re.compile(r'^--- (?:COLUMN [A-Z], )?CARD (\d+)[^\n]*? ---$', re.M)


def parse(p):
    """プロンプトを、前置き・見出し部・（グループ見出し／カード）の並び・末尾に分ける。"""
    h = p.index('--- HEADER ---')
    f = re.search(r'^--- FOOTER ---$', p, re.M).start()
    marks = sorted([(m.start(), 'group', None) for m in GROUP_RE.finditer(p)] +
                   [(m.start(), 'card', int(m.group(1))) for m in CARD_RE.finditer(p)])
    first = marks[0][0]
    items = []
    for k, (pos, kind, num) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else f
        items.append({'kind': kind, 'n': num, 'text': p[pos:end]})
    return p[:h], p[h:first], items, p[f:]


def ig_block(layout, badge_ignore):
    return (IG_HEAD + (LAYOUT_ONE if layout == 'one' else LAYOUT_TWO) + IG_TAIL
            + (BADGE_ADD if badge_ignore else '') + '\n')


def finish(pre, head, body, foot, layout, badge_ignore, suffix=None, cards=None, badge_range=None):
    """前置きにInstagram用の指示を入れ、大きさと最後の確認を直して、1つのプロンプトにする。"""
    notes = []
    pre, k = re.subn(r'portrait layout, \d+[x×]\d+ pixels', 'portrait layout, 3:4 aspect ratio, 1080x1440 pixels', pre, count=1)
    if k != 1:
        notes.append('大きさの指定を読み取れない')
    anchor = next((a for a in ('GLANCEABLE-POSTER REQUIREMENT', 'CRITICAL TEXT REQUIREMENT') if a in pre), None)
    if anchor is None:
        notes.append('差し込む位置を読み取れない')
    else:
        x = pre.index(anchor)
        pre = pre[:x] + ig_block(layout, badge_ignore) + pre[x:]
    if suffix:
        head, k = re.subn(r'(Subtitle[^\n]*:\n)(.+)', lambda m: m.group(1) + m.group(2).rstrip() + suffix, head, count=1)
        if k != 1:
            notes.append('サブタイトルを読み取れない')
    if cards is not None:
        foot, k = re.subn(r'number of cards\s+equals\s+\d+\s+exactly', f'number of cards equals {cards} exactly', foot, count=1)
        if k != 1:
            notes.append('最後の確認のカード数を読み取れない')
        if badge_range:
            foot, k = re.subn(r'badge numbers run \d+-\d+ continuously\s+across both columns without\s+resetting',
                              f'badge numbers run {badge_range[0]}-{badge_range[1]} continuously within this image '
                              f'(the first badge reads {badge_range[0]}, not 1)', foot, count=1)
            if k != 1:
                notes.append('最後の確認のバッジ番号を読み取れない')
    j = foot.rfind('Confirm the entire canvas')
    foot = foot[:j] + FINAL_ADD + foot[j:] if j != -1 else foot.rstrip('\n') + '\n' + FINAL_ADD
    return pre + head + body + foot, notes


def convert(p, code=None, item=None):
    """戻り値：([プロンプト（2枚に分けるときは2つ）], 元のカード数, 注意, 分け方の説明)"""
    pre, head, items, foot = parse(p)
    n_cards = sum(1 for it in items if it['kind'] == 'card')
    n_groups = sum(1 for it in items if it['kind'] == 'group')
    notes = []
    n_heads = len(HEAD_RE.findall(p))
    if n_heads != n_cards:
        notes.append(f'カードの見出しが{n_heads}個で、カード数{n_cards}と合わない：キャプション案を確かめる')
    split = SPLITS.get((code, item))
    has_badge = 'Badge:' in p
    if split:
        prompts = []
        for k, nums in enumerate(split['parts']):
            body, cur_group = '', None
            groups = [it for it in items if it['kind'] == 'group']
            # カードの直前にあるグループ見出しを、その部分で最初に使うときだけ付ける
            last_group = None
            used = set()
            for it in items:
                if it['kind'] == 'group':
                    last_group = it
                elif it['n'] in nums:
                    if last_group is not None and id(last_group) not in used:
                        body += last_group['text']
                        used.add(id(last_group))
                    body += it['text']
            layout = 'one' if len(nums) <= 3 else 'two'
            suffix = '（前半）' if k == 0 else '（後半）'
            # 番号つきバッジは、元のまま残して、2枚をまたいで続ける（空欄の番号と対応するため）
            text, nt = finish(pre, head, body, foot, layout, False, suffix=suffix, cards=len(nums),
                              badge_range=(nums[0], nums[-1]) if has_badge else None)
            notes += nt
            prompts.append(text)
        return prompts, n_cards, notes, split['why']
    text, nt = finish(pre, head, ''.join(it['text'] for it in items), foot, 'two', has_badge)
    notes += nt
    if n_cards < 4 or n_cards > 6:
        notes.append(f'カードが{n_cards}枚：3:4では4〜6枚に絞る必要がある（絞り方を決めてから使う）')
    if n_groups >= 3:
        notes.append('グループが3つ：配置を確かめる')
    return [text], n_cards, notes, ''


def captions(label, q, title, p, slides=1):
    heads = HEAD_RE.findall(p)
    tag = '#' + label
    lines = [f'【{label} 問{q}】{title}', '', 'この問題の確認ポイント：']
    lines += [f'・{h.strip()}' for h in heads]
    if slides > 1:
        lines += ['', f'（{slides}枚。スワイプでつづきを見られます）']
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
            item = f'Q{q:02d}'
            prompts, nc, notes, why = convert(p, code, item)
            for x in prompts:
                assert '```' not in x
            slides = len(prompts)
            src = os.path.relpath(hits[0], ROOT)
            status = '要手作業' if notes else ('プロンプト作成済み（2枚に分割）' if slides > 1 else 'プロンプト作成済み')
            if notes:
                flagged += 1
            out += [f'## {label} 第{q}問｜{title}', '',
                    f'- 出典の記事：`{src}`', f'- 元のカード数：{nc}', f'- 状態：{status}']
            if slides > 1:
                out.append(f'- **2枚に分けて作る**（1つの投稿に2枚。複数枚をめくる投稿）：{why}')
            for x in notes:
                out.append(f'- ⚠ {x}')
            for si, x in enumerate(prompts, start=1):
                ttl = '3:4画像プロンプト（ChatGPTに貼る）' if slides == 1 else f'3:4画像プロンプト　{si}枚目／{slides}枚（ChatGPTに貼る）'
                out += ['', f'### {ttl}', '', '```', x.rstrip('\n'), '```']
            out += ['', '### キャプション案', '', '```', captions(label, q, title, p, slides), '```', '', '---', '']
            index.append([code, item, title, nc, slides, status, '；'.join(notes), src])
        with open(os.path.join(OUTDIR, f'{code}.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out))
    with open(os.path.join(OUTDIR, 'index.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['year', 'item', 'title', 'cards', 'slides', 'status', 'notes', 'source'])
        w.writerows(index)
    print(f'{len(index)}問のプロンプトを書き出した（要手作業 {flagged}問、2枚に分けた問 {sum(1 for r in index if r[4] > 1)}問）：{OUTDIR}')


if __name__ == '__main__':
    main()
