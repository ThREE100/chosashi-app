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
for fp in sorted(glob.glob(os.path.join(HERE, 'morning', 'problems', '*.json'))):
    p = json.load(open(fp, encoding='utf-8'))
    print(f"=== {p['id']} ===")
    print(p['stem'])
    for s in p['statements']:
        print(f"{s['label']} {s['text']}")
    seen = []
    for s in p['statements']:
        for b in s['basis']:
            k = (b['law'], b['article'])
            if k not in seen:
                seen.append(k)
    print('--- 条文の原文 ---')
    for law, art in seen:
        print(f'【{law}】')
        print(article(law, art))
    print()
