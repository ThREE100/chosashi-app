"""毎日ドリル（朝の択一）から、Xの朝・夜の投稿文を作る。

使い方：
    python3 note-unei/x/make_x_posts.py            # 全日を posts.md に書き出す
    python3 note-unei/x/make_x_posts.py 1 7        # 第1日〜第7日だけ画面に出す

朝：問題のテーマと「答えは夜に」。問題文は長いので画像（daily-drill/out/dayNNN-am.html の画面写し）を添える。
夜：正解の番号と、解説記事のタイトルの「～～」の部分（ひとことの要点）、noteの解説記事のURL（{URL} を貼りかえる）。

正解は問題データ（daily-drill/morning/problems/AM-NNN.json）の各肢の正誤から計算し、
解説記事（daily-drill/kaisetsu/dayNNN-am-kaisetsu.md）の「正解：…（選択肢N番）」と一致することを確かめる。
Xの文字数は、日本語などの全角を2、半角を1、URLを23として数え、280以下であることを確かめる。
"""
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROB = os.path.join(ROOT, 'daily-drill', 'morning', 'problems')
KAI = os.path.join(ROOT, 'daily-drill', 'kaisetsu')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'posts.md')

TAGS = '#土地家屋調査士 #調査士試験'
CIRCLED = '①②③④⑤'


def x_len(text):
    """Xの文字数（URLは23、全角は2、半角は1）。"""
    text = re.sub(r'https?://\S+|\{URL\}', 'x' * 23, text)
    n = 0
    for ch in text:
        n += 2 if unicodedata.east_asian_width(ch) in 'WFA' else 1
    return n


def answer_of(prob):
    want = prob['mode'] == '正しい'
    picked = sorted(s['label'] for s in prob['statements'] if s['truth'] == want)
    for i, c in enumerate(prob['choices']):
        if sorted(c) == picked:
            return i + 1, picked
    raise ValueError(f"{prob['id']}: 正解の組合せが選択肢にない {picked}")


def kaisetsu_info(day):
    path = os.path.join(KAI, f'day{day:03d}-am-kaisetsu.md')
    if not os.path.exists(path):
        return None, None
    text = open(path, encoding='utf-8').read()
    title = re.search(r'^## .*?～(.+?)～\s*$', text, re.M)
    ans = re.search(r'正解：.*?（選択肢(\d)番）', text)
    return (title.group(1) if title else None), (int(ans.group(1)) if ans else None)


def short_theme(theme, limit=40):
    """末尾の条文番号の括弧書きを外し、長いものは「・」の切れ目で縮めて「など」を付ける。"""
    t = re.sub(r'（[^（）]*(条|先例|判例|別表)[^（）]*）\s*$', '', theme).strip()
    if len(t) <= limit:
        return t
    head = t[:limit]
    cut = max(head.rfind('・'), head.rfind('、'), head.rfind('（'))
    t = (head[:cut] if cut > 10 else head).rstrip('・、')
    while t.count('（') > t.count('）'):
        t = t[:t.rfind('（')]
    return t + 'など'


def posts_for(day):
    prob = json.load(open(os.path.join(PROB, f'AM-{day:03d}.json'), encoding='utf-8'))
    no, picked = answer_of(prob)
    point, kai_no = kaisetsu_info(day)
    if kai_no is not None and kai_no != no:
        raise ValueError(f'第{day}日：問題データの正解{no}と解説記事の正解{kai_no}が食い違う')
    kind = '正しいもの' if prob['mode'] == '正しい' else '誤っているもの'
    morning = (
        f'【毎朝ドリル Day{day:03d}】\n'
        f'テーマ：{short_theme(prob["theme"])}\n'
        f'{kind}の組合せは①〜⑤のどれ？\n'
        f'答えと解説は今夜。\n'
        f'{TAGS}'
    )
    night = (
        f'【毎朝ドリル Day{day:03d} 答え】\n'
        f'正解は{CIRCLED[no - 1]}（{"・".join(picked)}）\n'
        + (f'ポイント：{point}\n' if point else '')
        + '各肢の解説はnoteで。\n{URL}\n'
        f'{TAGS}'
    )
    for label, t in (('朝', morning), ('夜', night)):
        if x_len(t) > 280:
            raise ValueError(f'第{day}日の{label}の投稿が長すぎる（{x_len(t)}）')
    return morning, night


def main():
    days = sorted(int(re.search(r'AM-(\d+)', p).group(1)) for p in glob.glob(os.path.join(PROB, 'AM-*.json')))
    if len(sys.argv) == 3:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        for d in days:
            if a <= d <= b:
                m, n = posts_for(d)
                print(f'===== 第{d}日 朝 ({x_len(m)}/280)\n{m}\n===== 第{d}日 夜 ({x_len(n)}/280)\n{n}\n')
        return
    lines = ['# Xの投稿文（毎日ドリル・朝の択一）', '',
             '`make_x_posts.py` で作る（手で直さない）。夜の `{URL}` は、その日のnoteの解説記事のURLに貼りかえる。',
             '朝の投稿には、問題の画像（`daily-drill/out/dayNNN-am.html` の問題部分の画面写し）を添える。', '']
    for d in days:
        m, n = posts_for(d)
        lines += [f'## Day{d:03d}', '', f'朝（{x_len(m)}/280）', '', '```', m, '```', '',
                  f'夜（{x_len(n)}/280）', '', '```', n, '```', '']
    open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'{len(days)}日分を書き出した：{OUT}')


if __name__ == '__main__':
    main()
