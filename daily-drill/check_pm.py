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
from lawtext import article, normalize  # noqa: E402
import math  # noqa: E402
from fractions import Fraction  # noqa: E402

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
    if p.get('layout') == 'generic':
        c = p['calc']
        P = {k: tuple(v) for k, v in c['points'].items()}
        at = poly_area([P[n] for n in 'ABCD'])
        rows = {r['name']: r['cells'] for r in table['rows']}
        if int(at) != c['registry_area'] or abs(float(rows['変更前'][3]) - c['registry_area']) > 1e-9:
            err(pid, f'登記記録の地積{c["registry_area"]}が座標の面積{at:.4f}の整数部分と合わない')
        if rows['変更後'][3] != f'{c["registry_area"]}.00':
            err(pid, '変更後の地積の表し方が宅地（小数第2位まで）でない')
        if any(not (0 < P[n][0] < 1e9) for n in P):
            err(pid, '座標が不正')
        inside = all(min(P[k][0] for k in 'ABCD') < P[n][0] < max(P[k][0] for k in 'ABCD') and min(P[k][1] for k in 'ABCD') < P[n][1] < max(P[k][1] for k in 'ABCD') for n in 'abcd')
        if not inside:
            err(pid, '建物の角が土地の外にある')
    elif p['form_type'] == 'land':
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
        cell = table['rows'][-1]['cells'][3]
        if f"1階　{fl['1階']:.2f}" not in cell or f"2階　{fl['2階']:.2f}" not in cell:
            err(pid, f'床面積が合わない（計算 {fl}）')
    # 禁止語
    if BANNED.search(json.dumps(p, ensure_ascii=False)):
        err(pid, '禁止語')


def _near(pid, label, got, want, tol=0.0051):
    if abs(got - want) > tol:
        err(pid, f'{label}: 別の方法 {want:.4f} と答え {got:.4f} が合わない')


def _line_pt(a, b, c, d):
    """直線abと直線cdの交点（連立一次方程式をクラメルの公式で解く。複素数は使わない）"""
    (ax, ay), (bx, by), (cx, cy), (dx, dy) = a, b, c, d
    a1, b1, c1 = by - ay, ax - bx, (by - ay) * ax + (ax - bx) * ay
    a2, b2, c2 = dy - cy, cx - dx, (dy - cy) * cx + (cx - dx) * cy
    det = a1 * b2 - a2 * b1
    return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)


def _tri_area(pts):
    """多角形を1点から三角形に割って求める（ガウスの公式とは別の方法）"""
    o = pts[0]
    s = 0.0
    for i in range(1, len(pts) - 1):
        u = (pts[i][0] - o[0], pts[i][1] - o[1])
        v = (pts[i + 1][0] - o[0], pts[i + 1][1] - o[1])
        s += (u[0] * v[1] - u[1] * v[0]) / 2
    return abs(s)


def _ans(p, label_start):
    return [a for a in p['answers'] if a['label'].startswith(label_start)][0]['value']


def check_calc2(p):
    pid, v = p['id'], p['verify']
    A = lambda k: tuple(v[k])
    if v['type'] == 'pm01':
        T1, T2 = A('T1'), A('T2')
        az = math.atan2(T2[1] - T1[1], T2[0] - T1[0])
        pts = {}
        for n, o in v['obs'].items():
            ang = math.radians(o['angle'][0] + o['angle'][1] / 60 + o['angle'][2] / 3600)
            pts[n] = (T1[0] + o['dist'] * math.cos(az + ang), T1[1] + o['dist'] * math.sin(az + ang))
            ans = _ans(p, '点' + n)
            _near(pid, f'点{n}X', float(ans[0]), pts[n][0]); _near(pid, f'点{n}Y', float(ans[1]), pts[n][1])
        R = _line_pt(A('K1'), A('K2'), A('S'), A('M'))
        ans = _ans(p, '点R')
        _near(pid, '点RX', float(ans[0]), R[0]); _near(pid, '点RY', float(ans[1]), R[1])
        pp = [tuple(map(float, _ans(p, '点P'))), tuple(map(float, _ans(p, '点Q'))), tuple(map(float, ans)), A('S')]
        fr = [(Fraction(str(x)), Fraction(str(y))) for x, y in pp]
        s = abs(sum(fr[i][0] * fr[(i + 1) % 4][1] - fr[(i + 1) % 4][0] * fr[i][1] for i in range(4))) / 2
        want = math.floor(s * 100) / 100
        _near(pid, '地積', float(_ans(p, '12番の地積')), want, 1e-9)
        _near(pid, '地積(三角形分割)', float(_ans(p, '12番の地積')), math.floor(_tri_area(pp) * 100 + 1e-7) / 100, 1e-9)
        # 点Rが2直線の上にあること（小数第2位に丸めた値で、直線からの距離が0.01以内）
        Rr = tuple(map(float, ans))
        for a, b in ((A('K1'), A('K2')), (A('S'), A('M'))):
            d = abs((b[0] - a[0]) * (Rr[1] - a[1]) - (b[1] - a[1]) * (Rr[0] - a[0])) / math.hypot(b[0] - a[0], b[1] - a[1])
            if d > 0.011:
                err(pid, f'点Rが筆界の直線上にない（{d:.4f}）')
    elif v['type'] == 'pm04':
        A_, B_, C_, D_, E_, F_, K = (A(k) for k in 'ABCDEFK')
        ux, uy = B_[0] - A_[0], B_[1] - A_[1]
        L = math.hypot(ux, uy)
        nx, ny = -uy / L, ux / L          # 左（進行方向に対して）法線
        if ny < 0:
            nx, ny = -nx, -ny              # 東側（Yが大きい側）
        a2 = (A_[0] + nx * v['off'], A_[1] + ny * v['off'])
        b2 = (B_[0] + nx * v['off'], B_[1] + ny * v['off'])
        H = _line_pt(a2, b2, C_, D_); I = _line_pt(a2, b2, E_, F_)
        for nm, q in (('点H', H), ('点I', I)):
            ans = _ans(p, nm)
            _near(p['id'], nm + 'X', float(ans[0]), q[0]); _near(p['id'], nm + 'Y', float(ans[1]), q[1])
        hx, hy = float(_ans(p, '点H')[0]), float(_ans(p, '点H')[1])
        ix, iy = float(_ans(p, '点I')[0]), float(_ans(p, '点I')[1])
        # 垂線の足：丸めたH・Iを使い、射影で求める（問題の手順どおり）
        t = ((K[0] - hx) * (ix - hx) + (K[1] - hy) * (iy - hy)) / ((ix - hx) ** 2 + (iy - hy) ** 2)
        J = (hx + (ix - hx) * t, hy + (iy - hy) * t)
        ans = _ans(p, '点J')
        _near(pid, '点JX', float(ans[0]), J[0]); _near(pid, '点JY', float(ans[1]), J[1])
        dj = math.hypot(K[0] - float(ans[0]), K[1] - float(ans[1]))
        _near(pid, '距離', float(_ans(p, '点Kから')), dj, 0.0051)
        # 平行線とABの距離が1.20、HIがABと平行
        cr = (ix - hx) * uy - (iy - hy) * ux
        if abs(cr) / (L * math.hypot(ix - hx, iy - hy)) > 0.002:
            err(pid, 'HIがABと平行でない')
        dd = abs((hx - A_[0]) * uy - (hy - A_[1]) * ux) / L
        _near(pid, 'ABからHIまでの距離', 1.20, dd, 0.01)
    elif v['type'] == 'pm07':
        A_, B_, C_, D_ = (A(k) for k in 'ABCD')
        d = math.hypot(D_[0] - A_[0], D_[1] - A_[1])
        E = (A_[0] + (D_[0] - A_[0]) / d * v['d_AE'], A_[1] + (D_[1] - A_[1]) / d * v['d_AE'])
        ans = _ans(p, '点E')
        _near(pid, '点EX', float(ans[0]), E[0]); _near(pid, '点EY', float(ans[1]), E[1])
        # 面積の条件を二分法で解く（連立方程式の解法とは別）
        lo, hi = 0.0, 1.0
        def ar(t):
            F = (B_[0] + (C_[0] - B_[0]) * t, B_[1] + (C_[1] - B_[1]) * t)
            return poly_area([A_, B_, F, E])
        for _ in range(60):
            mid = (lo + hi) / 2
            if (ar(mid) - v['target']) * (ar(lo) - v['target']) <= 0:
                hi = mid
            else:
                lo = mid
        t = (lo + hi) / 2
        F = (B_[0] + (C_[0] - B_[0]) * t, B_[1] + (C_[1] - B_[1]) * t)
        ans = _ans(p, '点F')
        _near(pid, '点FX', float(ans[0]), F[0]); _near(pid, '点FY', float(ans[1]), F[1])
        Fr = tuple(map(float, ans))
        if abs(poly_area([A_, B_, Fr, E]) - v['target']) > 0.1:
            err(pid, f'丸めたFで（イ）の面積が280から外れすぎ（{poly_area([A_, B_, Fr, E]):.3f}）')
        tot = floor2(poly_area([A_, B_, C_, D_]))
        _near(pid, '（ロ）', float(_ans(p, '分筆後の（ロ）')), tot - v['target'], 1e-9)
        _near(pid, 'EF', float(_ans(p, '分筆線EF')), math.hypot(Fr[0] - float(_ans(p, '点E')[0]), Fr[1] - float(_ans(p, '点E')[1])), 0.0051)
    for b_ in p.get('basis', []):
        quote_ok(pid, '根拠', b_)
    # 電卓（F-789SG）のキー列を実行して、答えと一致することを確かめる
    sys.path.insert(0, os.path.join(HERE, 'evening'))
    import calc_keys as ck
    _, got = {'pm01': ck.pm01, 'pm04': ck.pm04, 'pm07': ck.pm07, 'pm08': ck.pm08}[v['type']](p)
    def eq(label, have, want):
        if abs(float(have) - float(want)) > 1e-9:
            err(pid, f'電卓のキー列の結果と答えが違う: {label} {have} ≠ {want}')
    for nm, key in (('点P', 'P'), ('点Q', 'Q'), ('点R', 'R'), ('点H', 'H'), ('点I', 'I'), ('点J', 'J'), ('点E', 'E'), ('点F', 'F'), ('点C', 'C'), ('点D', 'D')):
        if key in got and any(a['label'].startswith(nm) for a in p['answers']):
            a = _ans(p, nm)
            eq(nm + 'X', a[0], got[key][0]); eq(nm + 'Y', a[1], got[key][1])
    for lab, key in (('12番の地積', 'area'), ('（イ）の地積', 'ai'), ('（ロ）の地積', 'ar'), ('分筆後の地積の合計', 'diff'), ('誤差の限度', 'kk'), ('点Kから', 'dist'), ('分筆後の（ロ）', 'ro'), ('分筆線EF', 'ef')):
        if key in got and any(a['label'].startswith(lab) for a in p['answers']):
            eq(lab, _ans(p, lab), got[key])
    if p.get('keys') is None:
        err(pid, '電卓のキー列がない（evening/calc_keys.py を実行する）')
    if v['type'] == 'pm08':
        T1, T2, A_, B_, K1, K2, S = (A(k) for k in ('T1', 'T2', 'A', 'B', 'K1', 'K2', 'S'))
        o = v['obs']['C']
        az = math.atan2(T2[1] - T1[1], T2[0] - T1[0])
        ang = math.radians(o['angle'][0] + o['angle'][1] / 60 + o['angle'][2] / 3600)
        Cc = (T1[0] + o['dist'] * math.cos(az + ang), T1[1] + o['dist'] * math.sin(az + ang))
        ans = _ans(p, '点C')
        _near(pid, '点CX', float(ans[0]), Cc[0]); _near(pid, '点CY', float(ans[1]), Cc[1])
        Cr = tuple(map(float, ans))
        Dd = _line_pt(K1, K2, Cr, S)
        ans = _ans(p, '点D')
        _near(pid, '点DX', float(ans[0]), Dd[0]); _near(pid, '点DY', float(ans[1]), Dd[1])
        Dr = tuple(map(float, ans))
        la = math.hypot(B_[0] - A_[0], B_[1] - A_[1])
        Ee = (A_[0] + (B_[0] - A_[0]) / la * v['d_AE'], A_[1] + (B_[1] - A_[1]) / la * v['d_AE'])
        ld = math.hypot(Cr[0] - Dr[0], Cr[1] - Dr[1])
        Ff = (Dr[0] + (Cr[0] - Dr[0]) / ld * v['d_DF'], Dr[1] + (Cr[1] - Dr[1]) / ld * v['d_DF'])
        ans = _ans(p, '点E'); _near(pid, '点EX', float(ans[0]), Ee[0]); _near(pid, '点EY', float(ans[1]), Ee[1])
        ans = _ans(p, '点F'); _near(pid, '点FX', float(ans[0]), Ff[0]); _near(pid, '点FY', float(ans[1]), Ff[1])
        Er, Fr = tuple(map(float, _ans(p, '点E'))), tuple(map(float, _ans(p, '点F')))
        ai = floor2(_tri_area([A_, Er, Fr, Dr])); ar = floor2(_tri_area([Er, B_, Cr, Fr]))
        _near(pid, '（イ）', float(_ans(p, '（イ）')), ai, 1e-9); _near(pid, '（ロ）', float(_ans(p, '（ロ）')), ar, 1e-9)
        diff = round(ai + ar - v['reg'], 2)
        _near(pid, '差', float(_ans(p, '分筆後の地積の合計')), diff, 1e-9)
        kk = (0.05 + 0.01 * v['reg'] ** 0.25) * math.sqrt(v['reg'])
        _near(pid, '誤差の限度', float(_ans(p, '誤差の限度')), math.floor(kk * 100 + 1e-9) / 100, 1e-9)
        need = abs(diff) > math.floor(kk * 100 + 1e-9) / 100
        if (_ans(p, '地積に関する更正') == '必要') != need:
            err(pid, '更正の要否が計算と合わない')
        if need and abs(diff) >= 2 * kk:
            err(pid, '甲3の範囲も超えている（トラップの設計が崩れる）')
        if need and _ans(p, '登記の目的') != '土地地積更正・分筆登記':
            err(pid, '登記の目的が合わない')
        for tb in p['tables']:
            if tb['title'].startswith('誤差の限度'):
                row = [r for r in tb['rows'] if abs(float(r[0]) - v['reg']) < 1e-9]
                if not row or abs(float(row[0][1]) - math.floor(kk * 100 + 1e-9) / 100) > 1e-9 or abs(float(row[0][2]) - math.floor(2 * kk * 100 + 1e-9) / 100) > 1e-9:
                    err(pid, '誤差の限度の表に登記記録の地積の行がない／値が合わない')
    # 構造チェック：回答欄が問題文の指示と合うこと、表に答えの点が載っていないこと
    names = {n for n, q in p['fig']['points'].items() if q['kind'] == 'unknown'}
    listed = {r[0] for t in p['tables'] for r in t['rows'] if t['cols'][0] == '点' and 'X（北）' in t['cols']}
    if names & listed:
        err(pid, f'求める点{names & listed}が与える表に載っている')
    for t in p['text']['conditions'] + p['text']['hearing'] + p['text']['notes'] + [p['text']['lead']]:
        if re.search(r'541\.02|540\.49', t):
            err(pid, '本文に答えが漏れている')
    if not p['text']['hearing'] or not p['text']['conditions']:
        err(pid, '条件・聞き取り結果がない')


def main():
    files = sorted(glob.glob(os.path.join(HERE, 'evening', 'problems', '*.json')))
    for fp in files:
        p = json.load(open(fp, encoding='utf-8'))
        pid = p['id']
        if BANNED.search(json.dumps(p, ensure_ascii=False)):
            err(pid, '禁止語（個人の演習結果・過去問の出典は入れない）')
        if p['kind'] == 'calc2':
            check_calc2(p)
        elif p['kind'] == 'shinsei2':
            check_shinsei2(p)
    print(f'{len(files)}問を確認。NG {nerr}件')
    return nerr


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
