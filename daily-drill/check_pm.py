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


def poly_area(pts):
    s = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        s += x0 * y1 - x1 * y0
    return abs(s) / 2


def floor2(v):
    import math
    return math.floor(v * 100 + 1e-9) / 100


def check_shinsei2(p):
    pid = p['id']
    items = p['form']['items']
    for it in items:
        if it['kind'] == 'field':
            if not it['basis'] and not it.get('copy'):
                err(pid, f"欄「{it['label']}」に根拠も転記の印もない")
        for b in it.get('basis', []):
            quote_ok(pid, it['label'], b)
    table = [it for it in items if it['kind'] == 'table'][0]
    if p['form_type'] == 'land':
        c = p['calc']
        P = {k: tuple(v) for k, v in c['points'].items()}
        # 方法B：分筆線の端点が筆界線上にあること（外積がほぼ0）と、面積を靴ひも公式で計算し直す
        def off(a, b, q):
            ax, ay = P[a]; bx, by = P[b]; qx, qy = P[q]
            return abs((bx - ax) * (qy - ay) - (by - ay) * (qx - ax)) / (((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5)
        if off('B', 'C', 'E') > 0.02 or off('A', 'D', 'F') > 0.02:
            err(pid, '分筆線の端点が筆界線上にない')
        ai = floor2(poly_area([P[n] for n in c['polys']['i']]))
        ar = floor2(poly_area([P[n] for n in c['polys']['ro']]))
        at = poly_area([P[n] for n in c['polys']['total']])
        rows = {r['name']: r['cells'] for r in table['rows']}
        if abs(float(rows['（イ）'][3]) - ai) > 1e-9 or abs(float(rows['（ロ）'][3]) - ar) > 1e-9:
            err(pid, f'分筆後の地積が合わない（計算 {ai}, {ar}）')
        if abs(at - c['registry_area']) > 0.05:
            err(pid, f'分筆前の座標の面積{at:.4f}と登記記録の地積{c["registry_area"]}の差が大きい')
        if abs(float(rows['分筆前'][3]) - c['registry_area']) > 1e-9:
            err(pid, '分筆前の地積が登記記録と一致しない')
        tax = [it for it in items if it['id'] == 'tax'][0]['answer']
        if tax != '金2,000円':
            err(pid, '登録免許税が分筆後の2個分（2,000円）でない')
    else:
        fl = {f['name']: floor2(poly_area(f['outline'])) for f in p['plan']['floors']}
        cell = table['rows'][0]['cells'][3]
        if f"1階　{fl['1階']:.2f}" not in cell or f"2階　{fl['2階']:.2f}" not in cell:
            err(pid, f'床面積が合わない（計算 {fl}）')
    # 禁止語
    if BANNED.search(json.dumps(p, ensure_ascii=False)):
        err(pid, '禁止語')


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
        elif p['kind'] == 'shinsei2':
            check_shinsei2(p)
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
