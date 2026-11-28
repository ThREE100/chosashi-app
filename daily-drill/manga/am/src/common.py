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
