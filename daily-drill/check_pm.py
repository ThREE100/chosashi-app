"""夜の記述式ドリル（evening/problems/*.json）の機械チェック。
- 計算：シードから作り直して保存内容と一致、別の方法（実数の連立方程式・射影・外積・ガウスの公式）で解き直して答えが一致
- 申請書の欄：根拠の引用が法令の原文に一字一句あること（計算だけの欄は根拠なしでよい）
- 個人の演習結果・過去問の出典を入れていないこと
使い方: python3 daily-drill/check_pm.py"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'evening'))
from lawtext import article, normalize  # noqa: E402
import calc_types as ct  # noqa: E402

BANNED = re.compile(r'誤答|正答率|回答回数|復習中|演習結果|令和[0-9０-９元]+年度|平成[0-9０-９元]+年度|第[0-9０-９]+問')
nerr = 0


def err(pid, msg):
    global nerr
    nerr += 1
    print(f'NG {pid}: {msg}')


def quote_ok(pid, where, b):
    art = article(b['law'], b['article'])
    if art is None:
        err(pid, f"{where}: {b['law']}{b['article']} が原文にない")
    elif normalize(b['quote']) not in normalize(art):
        err(pid, f"{where}: 引用が原文と一致しない「{b['quote'][:30]}…」")


def main():
    files = sorted(glob.glob(os.path.join(HERE, 'evening', 'problems', '*.json')))
    for fp in files:
        p = json.load(open(fp, encoding='utf-8'))
        pid = p['id']
        if BANNED.search(json.dumps(p, ensure_ascii=False)):
            err(pid, '禁止語（個人の演習結果・過去問の出典は入れない）')
        if p['kind'] == 'calc':
            again = ct.GEN[p['type']](p['seed'])
            for k in ('given', 'answers'):
                if again[k] != p[k]:
                    err(pid, f'シードから作り直した{k}と一致しない')
            for e in ct.VERIFY[p['type']](p):
                err(pid, '別の方法の検算：' + e)
            for b in p.get('basis', []):
                quote_ok(pid, '根拠', b)
        else:
            for i, f in enumerate(p['fields']):
                if not f['basis'] and not f['calc']:
                    err(pid, f'欄{i + 1}: 根拠も計算の印もない')
                for b in f['basis']:
                    quote_ok(pid, f'欄{i + 1}', b)
    print(f'{len(files)}問を確認。NG {nerr}件')
    return nerr


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
