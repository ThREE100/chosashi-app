"""毎日ドリル（夜）の学習まんが：共通の読み込み。問題データ（daily-drill/evening/problems/PM-NN.json）は読むだけ。"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)                                   # daily-drill/manga/pm
FIG = os.path.join(OUT, 'fig')
DD = os.path.abspath(os.path.join(OUT, '..', '..'))           # daily-drill
REPO = os.path.dirname(DD)
sys.path.insert(0, os.path.join(REPO, 'tools', 'gakushu_manga'))
REL = 'daily-drill/manga/pm/'
RAW = 'https://raw.githubusercontent.com/ThREE100/chosashi-app/main/'


def problem(pid):
    return json.load(open(os.path.join(DD, 'evening', 'problems', pid + '.json'), encoding='utf-8'))


def scripts():
    out = []
    for f in sorted(os.listdir(HERE)):
        if re.fullmatch(r'day\d{3}\.py', f):
            spec = importlib.util.spec_from_file_location('manga_pm_' + f[:-3], os.path.join(HERE, f))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            out.append(m.MANGA)
    return out


def fig_rel(name):
    return f"{REL}fig/{name}.png"


def fig_url(f):
    return RAW + fig_rel(f['name'])
