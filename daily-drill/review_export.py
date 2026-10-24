"""独立照合用の資料を作る。問題文と肢（正誤は伏せる）と、関係する条文の原文だけを出力する。
照合者にはこの出力だけを渡し、問題作成者の結論・解説は見せない。
使い方: python3 daily-drill/review_export.py > packet.txt"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lawtext import article  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ONLY = set(sys.argv[1:])          # 例：python3 review_export.py AM-009 AM-010（省くと全部）
for fp in sorted(glob.glob(os.path.join(HERE, 'morning', 'problems', '*.json'))):
    p = json.load(open(fp, encoding='utf-8'))
    if ONLY and p['id'] not in ONLY:
        continue
    print(f"=== {p['id']} ===")
    print(p['stem'])
    for s in p['statements']:
        print(f"{s['label']} {s['text']}")
    seen = []
    for s in p['statements']:
        for b in s['basis']:
            k = ('doc', b['doc'], b['quote']) if 'doc' in b else (b['law'], b['article'])
            if k not in seen:
                seen.append(k)
    print('--- 条文の原文・過去問の解説の記載 ---')
    for k in seen:
        if k[0] == 'doc':                # 先例など：解説の記載の前後（正誤は伏せたまま）
            t = open(os.path.join(os.path.dirname(HERE), k[1]), encoding='utf-8').read()
            i = t.find(k[2][:20])
            print(f'【過去問の解説 {k[1]}】')
            print(t[max(0, i - 300): i + 500])
        else:
            print(f'【{k[0]}】')
            print(article(k[0], k[1]))
    print()
