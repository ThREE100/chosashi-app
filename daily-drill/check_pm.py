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


def check_module(p, items):
    """書式ひな形ドリル（evening/forms/pmNN.py）の共通チェック。"""
    pid = p['id']
    c = p.get('calc', {})
    tables = {it['id']: it for it in items if it['kind'] == 'table'}
    if not tables:
        err(pid, '表（土地／建物の表示など）がない')
    P_ = {k: tuple(v) for k, v in c.get('points', {}).items()}
    for ck_ in c.get('area_checks', []):
        tb = tables[ck_.get('table', next(iter(tables)))]
        rows = {r['name']: r['cells'] for r in tb['rows']}
        vals = []
        for v in ck_['values']:
            if isinstance(v, list) and all(isinstance(x, str) for x in v):
                vals.append(floor2(_tri_area([P_[n] for n in v])))
            elif isinstance(v, list):          # 複数の多角形を合わせた面積（合わせてから1回切り捨て）
                vals.append(floor2(sum(_tri_area([P_[n] for n in poly]) for poly in v)))
            else:
                vals.append(floor2(v) if ck_.get('floor', True) else v)
        want = ck_['fmt'].format(*vals)
        if ck_['row'] not in rows:
            err(pid, f"面積チェックの行「{ck_['row']}」が表にない")
        elif rows[ck_['row']][ck_['col']] != want:
            err(pid, f"{ck_['row']}の値が座標・寸法から求めた値と合わない（計算 {want!r}、記入 {rows[ck_['row']][ck_['col']]!r}）")
    if 'tax_count' in c:
        tx = [it for it in items if it['id'] == 'tax']
        n_ = c['tax_count']
        if n_ and (not tx or tx[0]['answer'] != f'金{n_ * 1000:,}円'):
            err(pid, f'登録免許税が{n_}個分（金{n_ * 1000:,}円）でない')
        if not n_ and tx:
            err(pid, '課税されない登記に登録免許税の欄がある')
    # 申請人などの住所・氏名が問題文（事実関係・登記記録）に書いてあること（答えにしかない住所を防ぐ）
    exam_txt = json.dumps(p['exam'], ensure_ascii=False)
    for it in items:
        if it['kind'] == 'field' and not it.get('copy') and ('申請人' in it['label'] or '代位' in it['label'] or '所有者' in it['label']):
            for tok in re.split(r'[　\n、（）]', it['answer']):
                if len(tok) >= 4 and re.search(r'[町市村]|番|号', tok) and tok not in exam_txt:
                    err(pid, f"欄「{it['label']}」の「{tok}」が問題文にない")
    for k in ('lead', 'facts', 'register', 'notes'):
        if not p['exam'].get(k):
            err(pid, f'exam.{k} がない')
    if len(p['exam']['facts']) < 4:
        err(pid, '事実関係が少ない（4項目以上）')
    if not any('約束' in n or '書く' in n for n in p['exam']['notes']):
        err(pid, '注に答案用紙の書き方の約束がない')


def check_shinsei2(p):
    pid = p['id']
    items = p['form']['items']
    for it in items:
        if it['kind'] == 'field':
            if not it['basis'] and not it.get('copy'):
                err(pid, f"欄「{it['label']}」に根拠も転記の印もない")
        for b in it.get('basis', []):
            quote_ok(pid, it['label'], b)
    # 合筆・合体による登記等・建物の合併を所有権の登記名義人が申請するとき（登記識別情報を提供するとき）は、印鑑証明書も要る
    # （令第18条第2項、規則第47条第3号イ（6）。会社法人等番号を提供するときは規則第48条第1号で省略できる）
    fl = {it['id']: it for it in items if it['kind'] == 'field'}
    pu, at = fl.get('purpose', {}).get('answer', ''), fl.get('attach', {}).get('answer', '')
    if re.search('合筆|合併|合体', pu) and '登記識別情報' in at and '会社法人等番号' not in at and '印鑑証明書' not in at:
        err(pid, '合筆・合体・合併で登記識別情報を提供するのに、添付情報に印鑑証明書がない（規則第47条第3号イ（6））')
    if '提供しないものとして答える' in json.dumps(p['exam']['notes'], ensure_ascii=False) and '印鑑証明書' in json.dumps(p['exam']['notes'], ensure_ascii=False) and re.search('合筆|合併|合体', pu):
        err(pid, '合筆・合体・合併の問で「印鑑証明書は提供しないものとして答える」の約束がある（本番の答案と逆の癖がつく）')
    # 所有権の登記がある建物の合体（登記識別情報を提供する）なら、令別表十三の項申請情報欄ロの「所有権の登記の表示」の表が要る
    if '合体' in pu and '登記識別情報' in at and not any('所有権登記の表示' in it['label'] for it in items if it['kind'] == 'table'):
        err(pid, '所有権の登記がある建物の合体なのに「合体前の建物の所有権登記の表示」の表がない（令別表十三の項申請情報欄ロ）')
    if p.get('module'):
        check_module(p, items)
        return
    table = [it for it in items if it['kind'] == 'table'][0]
    if p.get('layout') == 'generic' and p['form_type'] == 'land' and 'merge' in p['calc']:      # 土地合筆（PM-15）
        c = p['calc']
        P_ = {k: tuple(v) for k, v in c['points'].items()}
        m_ = c['merge']
        a5 = floor2(_tri_area([P_[k] for k in m_['lot5']])); a6 = floor2(_tri_area([P_[k] for k in m_['lot6']]))
        if (a5, a6) != (m_['reg5'], m_['reg6']):
            err(pid, f'登記記録の地積と座標が合わない（計算 {a5}, {a6}）')
        rows = {r['name']: r['cells'] for r in table['rows']}
        if rows['合筆後'][3] != f'{a5 + a6:.2f}' or rows['合筆前（合筆先）'][3] != f'{a5:.2f}' or rows['合筆前（6番）'][3] != f'{a6:.2f}':
            err(pid, '合筆の表の地積が合わない')
        regs = {s_['name']: dict(map(tuple, s_['rows'])) for s_ in p['exam']['register']}
        if regs['5番の土地 権利部（甲区・乙区）']['乙区 1番'] != regs['6番の土地 権利部（甲区・乙区）']['乙区 1番']:
            err(pid, '2筆の抵当権が同一でない（規則第105条第2号の設計が崩れる）')
        if [it for it in items if it['id'] == 'tax'][0]['answer'] != '金1,000円':
            err(pid, '登録免許税が合筆後の1個分でない')
    elif p.get('layout') == 'generic' and p['form_type'] == 'land':
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
    elif p.get('layout') == 'generic' and 'area_checks' in p['calc']:      # 建物の分割・合体（PM-12・PM-14）
        P_ = {k: tuple(v) for k, v in p['calc']['points'].items()}
        rows = {r['name']: r['cells'] for r in table['rows']}
        for ck_ in p['calc']['area_checks']:
            vals = [floor2(_tri_area([P_[n] for n in ck_['values'][0]]))]
            if len(ck_['values']) > 1:
                vals.append(floor2(ck_['values'][1]))
            want = ck_['fmt'].format(*vals)
            if rows[ck_['row']][ck_['col']] != want:
                err(pid, f"{ck_['row']}の床面積が座標と合わない（計算 {want!r}、記入 {rows[ck_['row']][ck_['col']]!r}）")
        regs = {s_['name']: dict(map(tuple, s_['rows'])) for s_ in p['exam']['register']}
        own = [v for s_ in regs.values() for k, v in s_.items() if '甲区' in k]
        if len({o.split('所有者')[-1].strip() for o in own}) != 1:
            err(pid, '所有者が同一でない')
        tx = [it for it in items if it['id'] == 'tax']
        n_ = p['calc']['tax_count']
        if n_ and (not tx or tx[0]['answer'] != f'金{n_ * 1000:,}円'):
            err(pid, f'登録免許税が{n_}個分でない')
        if not n_ and tx:
            err(pid, '課税されない登記に登録免許税の欄がある')
    elif p.get('layout') == 'generic' and 'unit' in p['calc']:      # 建物の区分（PM-13）
        u = p['calc']['unit']
        tb_ = [it for it in items if it['kind'] == 'table' and it['id'] == 'bld'][0]
        rows = {r['name']: r['cells'] for r in tb_['rows']}
        want_u = floor2((6.00 - 0.10 - 0.10) * (6.00 - 0.10 - 0.10))
        if abs(u['area'] - want_u) > 1e-9:
            err(pid, '専有部分の内法の面積が合わない')
        for k_ in ('（イ）部分', '（ロ）部分'):
            if rows[k_][3] != f'1階　{want_u:.2f}\n2階　{want_u:.2f}':
                err(pid, f'{k_}の床面積が合わない')
        P_ = {k: tuple(v) for k, v in p['calc']['points'].items()}
        tot = floor2(_tri_area([P_[k] for k in P_ if k.startswith('u')]))
        if rows['区分前'][3] != f'1階　{tot:.2f}\n2階　{tot:.2f}':
            err(pid, '区分前の床面積が座標と合わない')
        tx = [it for it in items if it['id'] == 'tax'][0]['answer']
        if tx != '金2,000円':
            err(pid, '登録免許税が区分後の2個分でない')
    elif p.get('layout') == 'generic':      # 建物の合併（PM-11）
        P_ = {k: tuple(v) for k, v in p['calc']['points'].items()}
        o1 = floor2(poly_area([P_[k] for k in P_ if k.startswith('p')]))
        o2 = floor2(poly_area([P_[k] for k in P_ if k.startswith('q')]))
        kk_ = floor2(poly_area([P_[k] for k in P_ if k.startswith('k')]))
        rows = {r['name']: r['cells'] for r in table['rows']}
        if f'{kk_:.2f}' != rows['甲建物'][4] or f'{kk_:.2f}' != rows['附属建物 符号1'][4]:
            err(pid, f'甲建物の床面積が座標と合わない（計算 {kk_}）')
        for k in ('乙建物', '合併後の主である建物'):
            if f'1階　{o1:.2f}\n2階　{o2:.2f}' != rows[k][4]:
                err(pid, f'{k}の床面積が座標と合わない（計算 {o1}, {o2}）')
        regs = {s_['name']: dict(map(tuple, s_['rows'])) for s_ in p['exam']['register']}
        m_otsu = {k: v for k, v in regs['乙建物 権利部（甲区・乙区）'].items() if k.startswith('乙区')}
        m_kou = {k: v for k, v in regs['甲建物 権利部（甲区・乙区）'].items() if k.startswith('乙区')}
        if m_otsu != m_kou:
            err(pid, '2つの建物の抵当権が同一でない（規則第131条第1号の設計が崩れる）')
        own = [v for s_ in regs.values() for k, v in s_.items() if k.startswith('甲区')]
        if len({o.split('所有者')[-1].strip() for o in own}) != 1:
            err(pid, '所有者が同一でない')
        if [it for it in items if it['id'] == 'tax'][0]['answer'] != '金1,000円':
            err(pid, '登録免許税が合併後の1個分（1,000円）でない')
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


def check_draw(p):
    pid, v = p['id'], p['verify']
    sys.path.insert(0, os.path.join(HERE, 'evening'))
    import calc_keys as ck
    if v['type'] == 'pm09':
        pts = {k: tuple(x) for k, x in v['pts'].items()}
        sides = ['AB', 'BF', 'FC', 'CD', 'DE', 'EA', 'EF']
        for s_, a in zip(sides, [a for a in p['answers'] if a['label'].startswith('辺')]):
            want = round(math.hypot(pts[s_[0]][0] - pts[s_[1]][0], pts[s_[0]][1] - pts[s_[1]][1]) + 1e-9, 2)
            _near(pid, f'辺{s_}', float(a['value']), want, 1e-9)
        fr = lambda names: [(Fraction(str(pts[n][0])), Fraction(str(pts[n][1]))) for n in names]
        def shoe(f):
            return abs(sum(f[i][0] * f[(i + 1) % len(f)][1] - f[(i + 1) % len(f)][0] * f[i][1] for i in range(len(f)))) / 2
        a1 = math.floor(shoe(fr('ABFE')) * 100) / 100
        a2 = math.floor(shoe(fr('EFCD')) * 100) / 100
        _near(pid, '12番1', float(_ans(p, '12番1')), a1, 1e-9); _near(pid, '12番2', float(_ans(p, '12番2')), a2, 1e-9)
        if abs(a1 + a2 - v['reg']) > 1.0:
            err(pid, '分筆後の合計と登記記録の地積の差が大きい')
        _, got = ck.pm09(p)
        for s_, w in zip(sides, got['lens']):
            _near(pid, f'キー列の辺{s_}', float(_ans(p, f'辺{s_}')), w, 1e-9)
        _near(pid, 'キー列12番1', float(_ans(p, '12番1')), got['a1'], 1e-9); _near(pid, 'キー列12番2', float(_ans(p, '12番2')), got['a2'], 1e-9)
        sp = p['spec']
        if [l['area'] for l in sp['lots']] != [a1, a2] or len(sp['sides']) != 7:
            err(pid, '作図の仕様と答えが合わない')
    else:
        b1 = [tuple(x) for x in v['b1']]; b2 = [tuple(x) for x in v['b2']]
        f1 = floor2(poly_area(b1)); f2 = floor2(poly_area(b2))
        _near(pid, '1階', float(_ans(p, '1階の床面積')), f1, 1e-9); _near(pid, '2階', float(_ans(p, '2階の床面積')), f2, 1e-9)
        # 表（e, n）から三角形分割で求め直す
        tabs = {t['title'][:12]: t for t in p['tables']}
        def from_table(key):
            t = [t for t in p['tables'] if key in t['title']][0]
            return [(float(r[1]), float(r[2])) for r in t['rows']]
        t1, t2 = from_table('1階の外形'), from_table('2階の外形')
        _near(pid, '表から1階', float(_ans(p, '1階の床面積')), floor2(_tri_area(t1)), 1e-9)
        _near(pid, '表から2階', float(_ans(p, '2階の床面積')), floor2(_tri_area(t2)), 1e-9)
        site = v['site']
        ne = max(b1, key=lambda c: c[0] + c[1])
        _near(pid, '北', float(_ans(p, '1階の北東の角から北側の筆界')), round(max(c[0] for c in site) - max(c[0] for c in b1) + 1e-9, 2), 1e-9)
        _near(pid, '東', float(_ans(p, '1階の北東の角から東側の筆界')), round(max(c[1] for c in site) - max(c[1] for c in b1) + 1e-9, 2), 1e-9)
        _, got = ck.pm10(p)
        _near(pid, 'キー列1階', f1, got['f1'], 1e-9); _near(pid, 'キー列2階', f2, got['f2'], 1e-9)
        _near(pid, 'キー列北', float(_ans(p, '1階の北東の角から北側の筆界')), got['dn'], 1e-9); _near(pid, 'キー列東', float(_ans(p, '1階の北東の角から東側の筆界')), got['de'], 1e-9)
        if not all(min(c[0] for c in site) < c[0] < max(c[0] for c in site) and min(c[1] for c in site) < c[1] < max(c[1] for c in site) for c in b1):
            err(pid, '建物が敷地の外にある')
    if len(p['rubric']) < 8:
        err(pid, '自己採点の項目が少ない')
    if p.get('keys') is None:
        err(pid, '電卓のキー列がない')


def main():
    files = sorted(glob.glob(os.path.join(HERE, 'evening', 'problems', '*.json')))
    only = set(a for a in sys.argv[1:] if a.startswith('PM-'))
    if only:
        files = [f for f in files if os.path.basename(f)[:-5] in only]
    for fp in files:
        p = json.load(open(fp, encoding='utf-8'))
        pid = p['id']
        if BANNED.search(json.dumps(p, ensure_ascii=False)):
            err(pid, '禁止語（個人の演習結果・過去問の出典は入れない）')
        if p['kind'] == 'draw':
            check_draw(p)
        elif p['kind'] == 'calc2':
            check_calc2(p)
        elif p['kind'] == 'shinsei2':
            check_shinsei2(p)
    print(f'{len(files)}問を確認。NG {nerr}件')
    return nerr


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
