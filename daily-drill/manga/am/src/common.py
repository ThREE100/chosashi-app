"""毎日ドリル（朝）の学習まんが：共通の読み込み。問題データ（daily-drill/morning/problems/AM-NNN.json）は読むだけ。"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)                                   # daily-drill/manga/am
DD = os.path.abspath(os.path.join(OUT, '..', '..'))           # daily-drill
REPO = os.path.dirname(DD)
sys.path.insert(0, os.path.join(REPO, 'tools', 'gakushu_manga'))
REL = 'daily-drill/manga/am/'


def problem(pid):
    return json.load(open(os.path.join(DD, 'morning', 'problems', pid + '.json'), encoding='utf-8'))


def scripts():
    out = []
    for f in sorted(os.listdir(HERE)):
        if re.fullmatch(r'day\d{3}\.py', f):
            spec = importlib.util.spec_from_file_location('manga_' + f[:-3], os.path.join(HERE, f))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            out.append(m.MANGA)
    return out


def answer(P):
    """正解の選択肢の番号（1から）と、その組。mode は「正しい」か「誤り」。"""
    want = (P['mode'] == '正しい')
    pick = sorted(s['label'] for s in P['statements'] if s['truth'] == want)
    for i, c in enumerate(P['choices'], 1):
        if sorted(c) == pick:
            return i, pick
    raise ValueError('正解の選択肢がない：' + P['id'])


ASK = {'正しい': '正しいものを選ぶ問題', '誤り': '誤っているものを選ぶ問題'}


def kotae(pid, claims, s_end, t_end):
    """最後のページ（答え）。○×はこのページだけに出す（2026-11-28 ユーザー指示）。
    claims：{肢: 肢の記述が言っていること（条文の正しい内容ではなく、肢の文の主張を短く）}。
    ○×は問題データの truth から付ける（台本に書かない）。選ぶ肢には「（選ぶ）」を付ける。"""
    P = problem(pid)
    n, pick = answer(P)
    head = f"答え：選択肢{n}（{'・'.join(pick)}）"
    ask = ASK[P['mode']]
    legend = '○＝肢の記述が正しい　×＝肢の記述が誤り'
    lines = []
    for s in P['statements']:
        lb = s['label']
        lines.append(f"{lb} {'○' if s['truth'] else '×'} {claims[lb]}" + ('（選ぶ）' if lb in pick else ''))
    art = ('A large answer board. At the top the heading ' + head + ' on a yellow highlighter band; just below it, in smaller dark navy '
           'letters, the line ' + ask + ', then a small legend line ' + legend + '. Below, a plain five-row table, one row per option, in the '
           'listed order: the option letter, then the mark (○ in BLUE, × in RED), then the short text. The rows ending in （選ぶ） have a '
           'pale yellow band behind the whole row. No check boxes, no ticks, no stamps other than the ○ and × in the rows.')
    return dict(caption='まとめ：' + head, aim='問いの向き（正しい／誤っている）と、各肢の記述の正誤・選ぶ肢を一度に見せる。○×はこのページだけ。',
                layout='Two panels: one large panel filling the top two thirds, and one wide panel at the bottom.',
                panels=[dict(size='large, top two thirds', art=art, words=[head, ask, legend] + lines),
                        dict(size='wide, bottom', art='The student, relieved and determined, holds her pencil up; the teacher smiles warmly with wings on hips.',
                             chars='student left, teacher right', talk=[('S', s_end), ('T', t_end)])])
