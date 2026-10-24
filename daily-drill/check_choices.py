"""択一の照合：各問の正解の組合せが、選択肢の中にちょうど1つ含まれているかを、3つの方向から確かめる。
1) 問題ファイルの正誤（truth）と問う向き（mode）から出した正解の組合せが、選択肢にちょうど1つある。
2) 独立に解いた担当の肢ごとの判定（morning/review・saturday/review の verdicts）から出した正解の組合せも、選択肢にちょうど1つあり、1) と同じ番号になる。
3) 印刷用のHTML（out/）の問題ページに出ている選択肢が問題ファイルと同じで、解答ページの正解の番号が 1) と同じ。
あわせて、選択肢が5つとも2肢の組合せで互いに異なること。結果は coverage/choices_check.md に書く。
使い方: python3 daily-drill/check_choices.py"""
import glob
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NUM = '①②③④⑤'
ng, rows = [], []


def combo(verdicts, mode):
    want = mode == '正しい'
    return {k for k, v in verdicts.items() if v == want}


def where(chs, s):
    return [i + 1 for i, c in enumerate(chs) if set(c) == s]


def one(pid, kind, mode, sts, chs, verdicts, page_q, page_a):
    truth = {s['label']: s['truth'] for s in sts}
    a1 = combo(truth, mode)
    h1 = where(chs, a1)
    if len(chs) != 5 or len({frozenset(c) for c in chs}) != 5 or any(len(c) != 2 for c in chs):
        ng.append(f'{pid}: 選択肢が「互いに異なる2肢の組合せ5つ」でない')
    if len(h1) != 1:
        ng.append(f'{pid}: 正解の組合せ {"・".join(sorted(a1))} が選択肢に{len(h1)}つ')
    if verdicts is None:
        ng.append(f'{pid}: 独立に解いた判定がない')
        a2, h2 = set(), []
    else:
        a2 = combo(verdicts, mode)
        h2 = where(chs, a2)
        if h2 != h1:
            ng.append(f'{pid}: 独立の判定からの正解 {"・".join(sorted(a2))}（{h2}）が問題ファイルの正解（{h1}）と違う')
    if page_q is not None:
        t = html.unescape(re.sub(r'<[^>]+>', ' ', page_q))
        for i, c in enumerate(chs):
            if not re.search(NUM[i] + r'\s*' + r'\s*・\s*'.join(c), t):
                ng.append(f'{pid}: 問題ページに選択肢 {NUM[i]} {"・".join(c)} が見当たらない')
    if page_a is not None and h1:
        t = html.unescape(re.sub(r'<[^>]+>', ' ', page_a))
        if not re.search(r'正解\s*[:：]?\s*' + NUM[h1[0] - 1], t):
            ng.append(f'{pid}: 解答ページの正解の番号が {NUM[h1[0] - 1]} になっていない')
    rows.append(f'| {pid} | {mode} | {"・".join(sorted(a1))} | {NUM[h1[0] - 1] if len(h1) == 1 else "×"} | {NUM[h2[0] - 1] if len(h2) == 1 else "×"} | {"一致" if h1 == h2 and len(h1) == 1 else "不一致"} |')


def rd(fp):
    return open(fp, encoding='utf-8').read() if os.path.exists(fp) else None


for fp in sorted(glob.glob(os.path.join(HERE, 'morning', 'problems', 'AM-*.json'))):
    p = json.load(open(fp, encoding='utf-8'))
    rv = os.path.join(HERE, 'morning', 'review', p['id'] + '.json')
    v = json.load(open(rv, encoding='utf-8'))['verdicts'] if os.path.exists(rv) else None
    d = p['day']
    one(p['id'], '朝', p['mode'], p['statements'], p['choices'], v,
        rd(os.path.join(HERE, 'out', f'day{d:03d}-am.html')), rd(os.path.join(HERE, 'out', f'day{d:03d}-am-ans.html')))
for rp in sorted(glob.glob(os.path.join(HERE, 'saturday', 'review', 'SAT*.json'))):
    sid = os.path.basename(rp)[:-5]
    rv = json.load(open(rp, encoding='utf-8'))
    q, a = rd(os.path.join(HERE, 'out', sid.lower() + '.html')), rd(os.path.join(HERE, 'out', sid.lower() + '-ans.html'))
    for fp in sorted(glob.glob(os.path.join(HERE, 'saturday', 'q', sid + '-Q*.json'))):
        p = json.load(open(fp, encoding='utf-8'))
        pid = os.path.basename(fp)[:-5]
        one(pid, '土曜', p['mode'], p['statements'], p['choices'], rv.get(pid, {}).get('verdicts'), None, None)

out = ['# 択一の選択肢の照合（check_choices.py で自動生成）', '',
       '正解の組合せが選択肢にちょうど1つあるかを、問題ファイルの正誤と、独立に解いた担当の判定の両方から確かめた結果。朝は印刷用のページ（out/）の選択肢と正解の番号も照らした。', '',
       f'- 対象：{len(rows)}問　NG：{len(ng)}件', '']
out += ['## NG', ''] + [f'- {x}' for x in ng] + [''] if ng else []
out += ['| 問 | 問う向き | 正解の組合せ | 問題ファイルの番号 | 独立の判定の番号 | 照合 |', '|---|---|---|---|---|---|'] + rows
open(os.path.join(HERE, 'coverage', 'choices_check.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
for x in ng:
    print('NG ' + x)
print(f'択一の選択肢の照合：{len(rows)}問、NG {len(ng)}件（coverage/choices_check.md）')
sys.exit(1 if ng else 0)
