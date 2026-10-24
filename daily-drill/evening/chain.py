"""夜の記述式デイリー（計算の連鎖）の共通エンジン。1問は SPEC（データ）で書き、ここで
  ①方法A（複素数）で答えを出す、②方法B（三角関数・クラメルの公式・射影・二分法・三角形分割）で別に検算する、
  ③F-789SG のキー列を作り、電卓のシミュレータで表示を再現する、④答えが一つに決まるかを確かめる、
  ⑤問題・解答のページ用の JSON（kind: calc2）を作る。
点は X＝北・Y＝東、複素数 Z ＝ X ＋ Yi。各手順で求めた点は小数第3位を四捨五入して小数第2位にし、後の手順は丸めた値を使う（本番の答案の作り方）。

手順（steps）の op：
  radial       放射。station・back、true（設計上の位置。観測値はここから逆算）か angle・dist。backread（後視の読み）も可
  inter        直線 a-b と直線 c-d の交点
  along        frm から to の向きに dist（m）
  ratio        frm から to へ num／den の点
  offset_inter 直線 a-b に平行で side（east/west/north/south）へ off 離れた直線と、直線 c-d の交点
  foot         点 p から直線 a-b への垂線の足
  area_point   frm-to 上の点で、poly（'*' がその点）の面積が target になる点
  transform    共通点2つ（a↔a2、b↔b2）で、任意座標の p2 を直す
出力（outputs）の kind：xy（点）・area（poly、mode＝floor2〈宅地など〉／int〈1㎡未満切捨て〉）・dist（a-b）・
  arith（寸法の式 expr。outline〈建物の外形の寸法の頂点〉か alt〈別の式〉で検算）・tol（誤差の限度 F・cls）・
  num（{id} で前の出力を使う式）・text（when の条件で value_true／value_false）"""
import cmath
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import calc_keys as CK  # noqa: E402

SIDE = {'east': 1j, 'west': -1j, 'north': 1, 'south': -1}


class SpecError(Exception):
    pass


def r2(z):
    return complex(round(z.real + 1e-12, 2), round(z.imag + 1e-12, 2))


def dms(rad):
    deg = math.degrees(rad) % 360
    d = int(deg)
    m = int((deg - d) * 60)
    s = round(((deg - d) * 60 - m) * 60)
    if s == 60:
        s, m = 0, m + 1
    if m == 60:
        m, d = 0, d + 1
    return [d, m, s]


def drad(a):
    return math.radians(a[0] + a[1] / 60 + a[2] / 3600)


def floor2(v):
    return math.floor(v * 100 + 1e-7) / 100


def sarea2(pts):
    """符号つき倍面積（Σ Im(Conjg(Pi)·Pi+1)）"""
    return sum((pts[i].conjugate() * pts[(i + 1) % len(pts)]).imag for i in range(len(pts)))


def angle_between(u, v):
    return abs(math.degrees(cmath.phase(v / u)))


# ---------------------------------------------------------------- 方法A（複素数）
def design(spec):
    """radial の true から観測値（角は秒まで、距離は小数第2位）を決める。SPEC を直接書き換える"""
    pts = {k['name']: complex(*k['xy']) for k in spec['known']}
    for st in spec['steps']:
        if st['op'] == 'radial' and 'true' in st:
            S, Bk = pts.get(st['station']), pts.get(st['back'])
            if S is None or Bk is None:
                raise SpecError(f"{st['name']}: 器械点・後視点が既知でない（放射の器械点に、計算で出した点を使うときは angle・dist を書く）")
            T = complex(*st['true'])
            br = drad(st.get('backread', [0, 0, 0]))
            st['angle'] = dms(cmath.phase(T - S) - cmath.phase(Bk - S) + br)
            st['dist'] = round(abs(T - S), 2)
            del st['true']
        pts[st['name']] = None   # 以後の design では使わない
    return spec


def step_a(st, P):
    op = st['op']
    g = lambda k: P[st[k]]
    if op == 'radial':
        S, Bk = g('station'), g('back')
        return S + cmath.rect(st['dist'], cmath.phase(Bk - S) + drad(st['angle']) - drad(st.get('backread', [0, 0, 0])))
    if op == 'inter':
        a, b, c, d = g('a'), g('b'), g('c'), g('d')
        den = ((d - c).conjugate() * (b - a)).imag
        if abs(den) < 1e-9:
            raise SpecError(f"{st['name']}: 2直線が平行で交点がない")
        return a + (b - a) * ((d - c).conjugate() * (c - a)).imag / den
    if op == 'along':
        a, b = g('frm'), g('to')
        return a + (b - a) / abs(b - a) * st['dist']
    if op == 'ratio':
        a, b = g('frm'), g('to')
        return a + (b - a) * st['num'] / st['den']
    if op == 'offset_inter':
        a, b, c, d = g('a'), g('b'), g('c'), g('d')
        u = (b - a) / abs(b - a)
        n = u * 1j
        want = SIDE[st['side']]
        if (n * want.conjugate()).real < 0:
            n = -n
        a2, b2 = a + n * st['off'], b + n * st['off']
        den = ((d - c).conjugate() * (b2 - a2)).imag
        return a2 + (b2 - a2) * ((d - c).conjugate() * (c - a2)).imag / den
    if op == 'foot':
        a, b, p = g('a'), g('b'), g('p')
        w = (p - a) / (b - a)
        return a + (b - a) * w.real
    if op == 'area_point':
        a, b = g('frm'), g('to')
        poly = lambda F: [F if n == '*' else P[n] for n in st['poly']]
        s0, s1 = sarea2(poly(a)), sarea2(poly(b))
        sg = 1 if (s0 + s1) > 0 else -1
        t = (sg * 2 * st['target'] - s0) / (s1 - s0)
        if not 0.02 < t < 0.98:
            raise SpecError(f"{st['name']}: 面積の条件を満たす点が辺 {st['frm']}{st['to']} の上にない（t＝{t:.3f}。解がない）")
        return a + (b - a) * t
    if op == 'transform':
        a, b, a2, b2, p2 = g('a'), g('b'), g('a2'), g('b2'), g('p2')
        return a + (p2 - a2) * (b - a) / (b2 - a2)
    raise SpecError(f'未知の op {op}')


def outputs_eval(spec, P, area_fn, step_fn_name='A'):
    out = {}
    for o in spec['outputs']:
        k = o['kind']
        oid = o.get('id') or o.get('pt') or o['label']
        if k == 'xy':
            out[oid] = P[o['pt']]
        elif k == 'area':
            v = area_fn([P[n] for n in o['poly']])
            out[oid] = floor2(v) if o.get('mode', 'floor2') == 'floor2' else float(math.floor(v + 1e-7))
            out[oid + '__raw'] = v
        elif k == 'dist':
            out[oid] = round(abs(P[o['a']] - P[o['b']]) + 1e-12, 2)
        elif k == 'arith':
            v = eval(o['expr'], {'__builtins__': {}})
            out[oid] = floor2(v) if o.get('mode', 'floor2') == 'floor2' else round(v + 1e-12, 2)
            out[oid + '__raw'] = v
        elif k == 'tol':
            F = o['F']
            t = (0.05 + 0.01 * F ** 0.25) * math.sqrt(F) * (2 if o.get('cls') == '甲3' else 1)
            out[oid] = floor2(t)
        elif k == 'num':
            v = eval(o['expr'].format(**{kk: vv for kk, vv in out.items() if not isinstance(vv, complex)}), {'__builtins__': {}, 'abs': abs})
            out[oid] = round(v + 1e-12, 2)
        elif k == 'text':
            cond = eval(o['when'].format(**{kk: vv for kk, vv in out.items() if not isinstance(vv, complex)}), {'__builtins__': {}, 'abs': abs})
            out[oid] = o['value_true'] if cond else o['value_false']
    return out


def solve_a(spec):
    P = {k['name']: complex(*k['xy']) for k in spec['known']}
    raw = {}
    for st in spec['steps']:
        z = step_a(st, P)
        raw[st['name']] = z
        P[st['name']] = r2(z)
    return P, raw, outputs_eval(spec, P, lambda pts: abs(sarea2(pts)) / 2)


# ---------------------------------------------------------------- 方法B（複素数を使わない）
def step_b(st, P):
    op = st['op']
    g = lambda k: P[st[k]]
    if op == 'radial':
        S, Bk = g('station'), g('back')
        az = math.atan2(Bk[1] - S[1], Bk[0] - S[0]) + drad(st['angle']) - drad(st.get('backread', [0, 0, 0]))
        return (S[0] + st['dist'] * math.cos(az), S[1] + st['dist'] * math.sin(az))
    if op in ('inter', 'offset_inter'):
        a, b, c, d = g('a'), g('b'), g('c'), g('d')
        if op == 'offset_inter':
            L = math.hypot(b[0] - a[0], b[1] - a[1])
            nx, ny = -(b[1] - a[1]) / L, (b[0] - a[0]) / L     # 進む向きに対して左
            wx, wy = {'east': (0, 1), 'west': (0, -1), 'north': (1, 0), 'south': (-1, 0)}[st['side']]
            if nx * wx + ny * wy < 0:
                nx, ny = -nx, -ny
            a, b = (a[0] + nx * st['off'], a[1] + ny * st['off']), (b[0] + nx * st['off'], b[1] + ny * st['off'])
        a1, b1, c1 = b[1] - a[1], a[0] - b[0], (b[1] - a[1]) * a[0] + (a[0] - b[0]) * a[1]
        a2, b2, c2 = d[1] - c[1], c[0] - d[0], (d[1] - c[1]) * c[0] + (c[0] - d[0]) * c[1]
        det = a1 * b2 - a2 * b1
        return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)
    if op == 'along':
        a, b = g('frm'), g('to')
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        return (a[0] + (b[0] - a[0]) / L * st['dist'], a[1] + (b[1] - a[1]) / L * st['dist'])
    if op == 'ratio':
        a, b = g('frm'), g('to')
        return (a[0] + (b[0] - a[0]) * st['num'] / st['den'], a[1] + (b[1] - a[1]) * st['num'] / st['den'])
    if op == 'foot':
        a, b, p = g('a'), g('b'), g('p')
        t = ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    if op == 'area_point':
        a, b = g('frm'), g('to')
        def ar(t):
            F = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
            return fan([F if n == '*' else P[n] for n in st['poly']])
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if (ar(mid) - st['target']) * (ar(lo) - st['target']) <= 0:
                hi = mid
            else:
                lo = mid
        t = (lo + hi) / 2
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    if op == 'transform':
        a, b, a2, b2, p2 = g('a'), g('b'), g('a2'), g('b2'), g('p2')
        th = math.atan2(b[1] - a[1], b[0] - a[0]) - math.atan2(b2[1] - a2[1], b2[0] - a2[0])
        sc = math.hypot(b[0] - a[0], b[1] - a[1]) / math.hypot(b2[0] - a2[0], b2[1] - a2[1])
        dx, dy = p2[0] - a2[0], p2[1] - a2[1]
        return (a[0] + sc * (dx * math.cos(th) - dy * math.sin(th)), a[1] + sc * (dx * math.sin(th) + dy * math.cos(th)))
    raise SpecError(op)


def fan(pts):
    o = pts[0]
    s = 0.0
    for i in range(1, len(pts) - 1):
        u = (pts[i][0] - o[0], pts[i][1] - o[1])
        v = (pts[i + 1][0] - o[0], pts[i + 1][1] - o[1])
        s += (u[0] * v[1] - u[1] * v[0]) / 2
    return abs(s)


def solve_b(spec):
    P = {k['name']: tuple(k['xy']) for k in spec['known']}
    for st in spec['steps']:
        x, y = step_b(st, P)
        P[st['name']] = (round(x + 1e-12, 2), round(y + 1e-12, 2))
    Pc = {k: complex(*v) for k, v in P.items()}
    out = outputs_eval(spec, Pc, lambda pts: fan([(z.real, z.imag) for z in pts]))
    for o in spec['outputs']:                      # 建物の床面積：寸法の式と、外形の頂点からの面積を照らす
        oid = o.get('id') or o.get('pt') or o['label']
        if o['kind'] == 'arith' and 'outline' in o:
            v = fan(o['outline'])
            out[oid] = floor2(v) if o.get('mode', 'floor2') == 'floor2' else round(v + 1e-12, 2)
        elif o['kind'] == 'arith' and 'alt' in o:
            env = {'__builtins__': {}, 'hypot': math.hypot, 'abs': abs, 'P': P}
            v = eval(o['alt'], env)
            out[oid] = floor2(v) if o.get('mode', 'floor2') == 'floor2' else round(v + 1e-12, 2)
    return Pc, out


# ---------------------------------------------------------------- 答えが一つに決まるか
def robustness(spec, raw, outA):
    errs = []
    P = {k['name']: complex(*k['xy']) for k in spec['known']}
    for st in spec['steps']:
        z = raw[st['name']]
        for u in (z.real, z.imag):           # 四捨五入の境目（x.xx5）に近いと、計算の順で答えが割れる
            if abs((u * 100) % 1 - 0.5) < 0.06:
                errs.append(f"{st['name']}: 座標 {u:.5f} が四捨五入の境目に近い")
        if st['op'] in ('inter', 'offset_inter'):
            a, b, c, d = (P.get(st[k], raw.get(st[k])) for k in 'abcd')
            if angle_between(b - a, d - c) % 180 < 8 or angle_between(b - a, d - c) % 180 > 172:
                errs.append(f"{st['name']}: 2直線の交わる角が8°未満（ほぼ平行で、少しの誤差で交点が大きく動く）")
        if st['op'] == 'foot':
            a, b = P[st['a']], P[st['b']]
            t = ((raw[st['name']] - a) / (b - a)).real
            if not -0.001 < t < 1.001:
                errs.append(f"{st['name']}: 垂線の足が線分 {st['a']}{st['b']} の外にある")
        P[st['name']] = r2(z)
    for o in spec['outputs']:
        oid = o.get('id') or o.get('pt') or o['label']
        if o['kind'] in ('area', 'arith') and oid + '__raw' in outA:
            v = outA[oid + '__raw']
            q = v * 100 if o.get('mode', 'floor2') == 'floor2' else v
            if abs(q - round(q)) < 0.01:
                errs.append(f"{o['label']}: 面積 {v:.5f} が切捨ての境目に近い（丸めの誤差で答えが割れる）")
    return errs


# ---------------------------------------------------------------- 電卓のキー列
def keys(spec):
    d = CK.Doc()
    P = {k['name']: complex(*k['xy']) for k in spec['known']}
    cx = lambda z: CK.cxs(z.real, z.imag)
    sto = lambda pairs: '\n'.join(f'{cx(P[n])} [SHIFT] [STO] [{v}]' for n, v in pairs)
    got = {}
    groups = []
    for st in spec['steps']:
        op, nm = st['op'], st['name']
        first = len(d.steps)
        if op == 'radial':
            ang = st['angle']
            br = st.get('backread', [0, 0, 0])
            brk = f' [−] {CK.dms_keys(br)}' if br != [0, 0, 0] else ''
            d.add(f'割り当て（点{nm}）', f'Y＝{st["station"]}（器械点）、X＝{st["back"]}（後視点）', sto([(st['station'], 'Y'), (st['back'], 'X')]), show=False)
            d.add(f'点{nm}（放射）', f'{nm} ＝ {st["station"]} ＋ {st["dist"]:.2f}∠( arg({st["back"]} − {st["station"]}) ＋ {CK.ang_s(ang)}{" − " + CK.ang_s(br) if brk else ""} )',
                  f'[ALPHA] [Y] [+] {CK.num(st["dist"])} [∠] [(] [Apps] [3] [ALPHA] [X] [−] [ALPHA] [Y] [)] [+] {CK.dms_keys(ang)}{brk} [)] [=]')
        elif op in ('inter', 'offset_inter'):
            d.add(f'割り当て（点{nm}）', f'A＝{st["a"]}、B＝{st["b"]}、C＝{st["c"]}、D＝{st["d"]}', sto([(st['a'], 'A'), (st['b'], 'B'), (st['c'], 'C'), (st['d'], 'D')]), show=False)
            if op == 'offset_inter':
                a, b = P[st['a']], P[st['b']]
                n = (b - a) / abs(b - a) * 1j
                sgn = 1 if (n * SIDE[st['side']].conjugate()).real > 0 else -1
                ik = f'{CK.num(st["off"])} [i]' if sgn > 0 else f'[(] 0 [−] {CK.num(st["off"])} [i] [)]'
                d.add('平行に離れた直線（A・Bをずらす）', f'E ＝ (B − A) ÷ Abs(B − A) × {"" if sgn > 0 else "(−"}{st["off"]:.2f}i{"" if sgn > 0 else ")"}（{ {"east": "東", "west": "西", "north": "北", "south": "南"}[st["side"]] }へ{st["off"]:.2f}m）、A′＝A＋E、B′＝B＋E',
                      f'[(] [ALPHA] [B] [−] [ALPHA] [A] [)] [÷] [Abs] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {ik} [=] [SHIFT] [STO] [E]\n[ALPHA] [A] [+] [ALPHA] [E] [=] [SHIFT] [STO] [A]\n[ALPHA] [B] [+] [ALPHA] [E] [=] [SHIFT] [STO] [B]', show=False)
            d.add(f'点{nm}の分子', 'Conjg(C − A) × (D − C)　のiの係数', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
            d.add(f'点{nm}の分母', 'Conjg(B − A) × (D − C)　のiの係数', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
            d.run()
            tn, td = CK.val(d.steps[-2], 1), CK.val(d.steps[-1], 1)
            d.add(f'点{nm}（交点）', f'{nm} ＝ A ＋ (B − A) × 分子 ÷ 分母', f'[ALPHA] [A] [+] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {CK.sn(tn)} [÷] {CK.sn(td)} [=]')
        elif op in ('along', 'ratio'):
            d.add(f'割り当て（点{nm}）', f'X＝{st["frm"]}、Y＝{st["to"]}', sto([(st['frm'], 'X'), (st['to'], 'Y')]), show=False)
            if op == 'along':
                d.add(f'点{nm}', f'{nm} ＝ {st["frm"]} ＋ ({st["to"]} − {st["frm"]}) ÷ Abs({st["to"]} − {st["frm"]}) × {st["dist"]:.2f}',
                      f'[ALPHA] [X] [+] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [÷] [Abs] [ALPHA] [Y] [−] [ALPHA] [X] [)] [×] {CK.num(st["dist"])} [=]')
            else:
                d.add(f'点{nm}', f'{nm} ＝ {st["frm"]} ＋ ({st["to"]} − {st["frm"]}) × {st["num"]} ÷ {st["den"]}',
                      f'[ALPHA] [X] [+] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [×] {CK.num(st["num"])} [÷] {CK.num(st["den"])} [=]')
        elif op == 'foot':
            d.add(f'割り当て（点{nm}）', f'X＝{st["a"]}、Y＝{st["b"]}、C＝{st["p"]}', sto([(st['a'], 'X'), (st['b'], 'Y'), (st['p'], 'C')]), show=False)
            d.add('w（Dに記憶）', f'w ＝ ({st["p"]} − {st["a"]}) ÷ ({st["b"]} − {st["a"]})', '[(] [ALPHA] [C] [−] [ALPHA] [X] [)] [÷] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [=] [SHIFT] [STO] [D]', show=False)
            d.add(f'点{nm}（垂線の足）', f'{nm} ＝ {st["a"]} ＋ ({st["b"]} − {st["a"]}) × (w ＋ Conjg(w)) ÷ 2',
                  '[ALPHA] [X] [+] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [×] [(] [ALPHA] [D] [+] [Apps] [4] [ALPHA] [D] [)] [)] [÷] 2 [=]')
        elif op == 'area_point':
            vs = [n for n in st['poly']]
            names = 'ABCDEF'
            for which, end in (('0', st['frm']), ('1', st['to'])):
                pairs = [(end if n == '*' else n, names[i]) for i, n in enumerate(vs)]
                d.add(f'割り当て（{nm}を{end}に置いたとき）', '、'.join(f'{v}＝{n}' for n, v in pairs), sto(pairs), show=False)
                d.add(f'倍面積（{nm}＝{end}）', 'Σ Conjg(Pi) × Pi+1　のiの係数（符号つき）', ' [+] '.join(f'[Apps] [4] [ALPHA] [{names[i]}] [)] [×] [ALPHA] [{names[(i + 1) % len(vs)]}]' for i in range(len(vs))) + ' [=]')
            d.run()
            s0, s1 = CK.val(d.steps[-3], 1), CK.val(d.steps[-1], 1)
            sg = 1 if s0 + s1 > 0 else -1
            d.add('t（辺の上の位置の比）', f't ＝ ({"" if sg > 0 else "−"}2 × {st["target"]:.2f} − 倍面積0) ÷ (倍面積1 − 倍面積0)',
                  f'[(] {CK.sn(sg * 2 * st["target"])} [−] {CK.sn(s0)} [)] [÷] [(] {CK.sn(s1)} [−] {CK.sn(s0)} [)] [=]')
            d.run()
            t = CK.val(d.steps[-1])
            d.add(f'割り当て（点{nm}）', f'X＝{st["frm"]}、Y＝{st["to"]}', sto([(st['frm'], 'X'), (st['to'], 'Y')]), show=False)
            d.add(f'点{nm}', f'{nm} ＝ {st["frm"]} ＋ ({st["to"]} − {st["frm"]}) × t', f'[ALPHA] [X] [+] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [×] {CK.num(round(t, 8))} [=]')
        elif op == 'transform':
            d.add(f'割り当て（点{nm}）', f'A＝{st["a"]}、B＝{st["b"]}、X＝{st["a2"]}、Y＝{st["b2"]}、C＝{st["p2"]}', sto([(st['a'], 'A'), (st['b'], 'B'), (st['a2'], 'X'), (st['b2'], 'Y'), (st['p2'], 'C')]), show=False)
            d.add('比 k（Eに記憶）', f'k ＝ ({st["b"]} − {st["a"]}) ÷ ({st["b2"]} − {st["a2"]})', '[(] [ALPHA] [B] [−] [ALPHA] [A] [)] [÷] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [=] [SHIFT] [STO] [E]', show=False)
            d.add(f'点{nm}（変換）', f'{nm} ＝ {st["a"]} ＋ ({st["p2"]} − {st["a2"]}) × k', '[ALPHA] [A] [+] [(] [ALPHA] [C] [−] [ALPHA] [X] [)] [×] [ALPHA] [E] [=]')
        d.run()
        z = complex(CK.r2(CK.val(d.steps[-1])), CK.r2(CK.val(d.steps[-1], 1)))
        P[nm] = z
        got[nm] = z
        groups.append((f'点{nm}', first, len(d.steps)))
    first = len(d.steps)
    for o in spec['outputs']:
        k = o['kind']
        oid = o.get('id') or o.get('pt') or o['label']
        if k == 'area':
            vs = o['poly']
            names = 'ABCDEF'
            d.add(f'割り当て（{o["label"]}）', '、'.join(f'{names[i]}＝{n}' for i, n in enumerate(vs)), sto([(n, names[i]) for i, n in enumerate(vs)]), show=False)
            if len(vs) == 4:
                d.add(o['label'] + '（倍面積）', f'四角形{"・".join(vs)}：Conjg(C − A) × (D − B)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [B] [)] [=]')
            else:
                d.add(o['label'] + '（倍面積）', 'Σ Conjg(Pi) × Pi+1　のiの係数の絶対値 ÷ 2', ' [+] '.join(f'[Apps] [4] [ALPHA] [{names[i]}] [)] [×] [ALPHA] [{names[(i + 1) % len(vs)]}]' for i in range(len(vs))) + ' [=]')
            d.run()
            v = abs(CK.val(d.steps[-1], 1)) / 2
            got[oid] = floor2(v) if o.get('mode', 'floor2') == 'floor2' else float(math.floor(v + 1e-7))
        elif k == 'dist':
            d.add(f'割り当て（{o["label"]}）', f'X＝{o["a"]}、Y＝{o["b"]}', sto([(o['a'], 'X'), (o['b'], 'Y')]), show=False)
            d.add(o['label'], f'Abs({o["b"]} − {o["a"]})', '[Abs] [ALPHA] [Y] [−] [ALPHA] [X] [)] [=]')
            d.run()
            got[oid] = round(CK.val(d.steps[-1]) + 1e-9, 2)
        elif k == 'arith':
            d.add(o['label'], o['expr'].replace('*', ' × ').replace('/', ' ÷ '), arith_keys(o['expr']))
            d.run()
            v = CK.val(d.steps[-1])
            got[oid] = floor2(v) if o.get('mode', 'floor2') == 'floor2' else round(v + 1e-9, 2)
        elif k == 'tol':
            F = CK.num(o['F'])
            d.add(o['label'], f'(0.05 ＋ 0.01 × ⁴√F) × √F{" × 2" if o.get("cls") == "甲3" else ""}（F＝{o["F"]:.2f}。小数第2位未満切捨て）',
                  f'[(] 0.05 [+] 0.01 [×] [√] [(] [√] [(] {F} [)] [)] [)] [×] [√] [(] {F} [)]{" [×] 2" if o.get("cls") == "甲3" else ""} [=]')
            d.run()
            got[oid] = floor2(CK.val(d.steps[-1]))
    if len(d.steps) > first:
        groups.append(('面積・距離など', first, len(d.steps)))
    return d.steps, groups, got


def arith_keys(expr):
    toks = re.findall(r'\d+(?:\.\d+)?|[-+*/()]', expr)
    m = {'+': '[+]', '-': '[−]', '*': '[×]', '/': '[÷]', '(': '[(]', ')': '[)]'}
    return ' '.join(m.get(t, t) for t in toks) + ' [=]'


# ---------------------------------------------------------------- 問題・解答の JSON（calc2）
def fmtv(v):
    return f'{v:.2f}' if isinstance(v, float) else str(v)


def build_problem(spec, day):
    spec = design(spec)
    P, raw, outA = solve_a(spec)
    errs = robustness(spec, raw, outA)
    if errs:
        raise SpecError(' ／ '.join(errs))
    answers = []
    for o in spec['outputs']:
        oid = o.get('id') or o.get('pt') or o['label']
        v = outA[oid]
        if o['kind'] == 'xy':
            answers.append({'label': o.get('label', '点' + o['pt']), 'kind': 'xy', 'value': [f'{v.real:.2f}', f'{v.imag:.2f}']})
        elif o['kind'] == 'text':
            answers.append({'label': o['label'], 'kind': 'text', 'value': v})
        else:
            unit_kind = 'area' if o['kind'] in ('area', 'arith') and o.get('unit', '㎡') == '㎡' else 'len'
            val = f'{int(v)}' if o['kind'] == 'area' and o.get('mode') == 'int' else f'{v:.2f}'
            answers.append({'label': o['label'], 'kind': unit_kind, 'value': val})
    # 表
    tables, seen = [], {}
    for k in spec['known']:
        if k.get('table') is None:
            continue
        if k['table'] not in seen:
            seen[k['table']] = {'title': k['table'], 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': []}
            tables.append(seen[k['table']])
        seen[k['table']]['rows'].append([k['name'], f'{k["xy"][0]:.2f}', f'{k["xy"][1]:.2f}', k.get('remark', '')])
    obs = {}
    for st in spec['steps']:
        if st['op'] == 'radial':
            key = (st['station'], st['back'], tuple(st.get('backread', [0, 0, 0])))
            obs.setdefault(key, []).append([st['name'], CK.ang_s(st['angle']), f'{st["dist"]:.2f}'])
    for (s, b, br), rows in obs.items():
        t = f'観測値（{s}に器械を据え、{b}を後視）' + (f'　後視{b}の読み {CK.ang_s(list(br))}' if br != (0, 0, 0) else '')
        tables.append({'title': t, 'cols': ['点', '水平角（時計回り）', '水平距離（m）'], 'rows': rows})
    tables += spec.get('tables_extra', [])
    # 図
    fig = {'points': {}, 'polys': [], 'lines': [], 'texts': []}
    for k in spec['known']:
        if k.get('fig', True):
            fig['points'][k['name']] = {'xy': list(k['xy']), 'kind': 'given' if '既知点' in (k.get('table') or '') else 'ref', **({kk: k[kk] for kk in ('dx', 'dy') if kk in k})}
    for st in spec['steps']:
        z = P[st['name']]
        fig['points'][st['name']] = {'xy': [z.real, z.imag], 'kind': 'unknown', **({kk: st[kk] for kk in ('dx', 'dy') if kk in st})}
        if st['op'] == 'radial':
            fig['lines'].append({'a': st['station'], 'b': st['name'], 'style': 'dash'})
    fills = ['#e8f4f0', '#fdf3e3', '#eef0fb']
    for i, o in enumerate([o for o in spec['outputs'] if o['kind'] == 'area' and o.get('fig', True)]):
        fig['polys'].append({'pts': o['poly'], 'fill': fills[i % 3], 'label': o.get('fig_label', '')})
    for k_, v_ in spec.get('fig', {}).items():
        if k_ == 'points':
            for n, pv in v_.items():
                fig['points'].setdefault(n, {}).update(pv)
        elif k_ in ('lines', 'texts', 'polys'):
            fig[k_] += v_
        else:
            fig[k_] = v_
    st_txt = spec.get('explain') or [auto_explain(st) for st in spec['steps']]
    verify = {'type': 'chain', 'spec': spec}
    ksteps, groups, got = keys(spec)
    p = {'id': spec['pid'], 'day': day, 'kind': 'calc2', 'title': spec['title'], 'text': spec['text'], 'tables': tables, 'fig': fig,
         'answers': answers, 'steps': st_txt, 'trap': ' '.join(spec['traps_text']), 'verify': verify, 'minutes': spec.get('minutes', 15),
         'basis': spec.get('basis', []),
         'keys': [{'title': t, 'steps': [{k: s[k] for k in ('title', 'formula', 'keys', 'display') if k in s} for s in ksteps[a:b]]} for t, a, b in groups]}
    return p, got, outA


def auto_explain(st):
    op, n = st['op'], st['name']
    return {'radial': f'{n} ＝ {st.get("station")} ＋ 距離∠( arg({st.get("back")} − {st.get("station")}) ＋ 水平角 )（後視から時計回り）',
            'inter': f'{n} ＝ 直線{st.get("a")}{st.get("b")}と直線{st.get("c")}{st.get("d")}の交点',
            'along': f'{n} ＝ {st.get("frm")} ＋ ({st.get("to")} − {st.get("frm")}) ÷ Abs(…) × {st.get("dist")}',
            'ratio': f'{n} ＝ {st.get("frm")} ＋ ({st.get("to")} − {st.get("frm")}) × {st.get("num")}／{st.get("den")}',
            'offset_inter': f'{n} ＝ 直線{st.get("a")}{st.get("b")}を{st.get("off")}m平行に移した直線と、直線{st.get("c")}{st.get("d")}の交点',
            'foot': f'{n} ＝ {st.get("p")}から直線{st.get("a")}{st.get("b")}への垂線の足（w ＝ ({st.get("p")} − {st.get("a")}) ÷ ({st.get("b")} − {st.get("a")}) の実部）',
            'area_point': f'{n} ＝ 辺{st.get("frm")}{st.get("to")}の上で、面積が{st.get("target")}㎡になる点（面積は辺の上の位置の比 t の一次式）',
            'transform': f'{n} ＝ {st.get("a")} ＋ ({st.get("p2")} − {st.get("a2")}) × ({st.get("b")} − {st.get("a")}) ÷ ({st.get("b2")} − {st.get("a2")})'}[op]


def verify_problem(p):
    """check_pm.py から呼ぶ。方法Bと電卓のキー列で答えを照らし、誤りのリストを返す"""
    spec = p['verify']['spec']
    errs = []
    Pb, outB = solve_b(spec)
    _, _, got = keys(spec)
    for o in spec['outputs']:
        oid = o.get('id') or o.get('pt') or o['label']
        ans = [a for a in p['answers'] if a['label'] == (o.get('label', '点' + o['pt']) if o['kind'] == 'xy' else o['label'])][0]['value']
        if o['kind'] == 'xy':
            b = Pb[o['pt']]
            if (f'{b.real:.2f}', f'{b.imag:.2f}') != tuple(ans):
                errs.append(f'点{o["pt"]}：方法B（{b.real:.2f}, {b.imag:.2f}）と答え（{ans[0]}, {ans[1]}）が違う')
            g = got.get(o['pt'])
            if g is None or (f'{g.real:.2f}', f'{g.imag:.2f}') != tuple(ans):
                errs.append(f'点{o["pt"]}：電卓のキー列の結果 {g} と答えが違う')
        elif o['kind'] == 'text':
            if outB[oid] != ans:
                errs.append(f'{o["label"]}：方法Bの判断 {outB[oid]} と答え {ans} が違う')
        else:
            bv = outB[oid]
            sb = f'{int(bv)}' if o['kind'] == 'area' and o.get('mode') == 'int' else f'{bv:.2f}'
            if sb != ans:
                errs.append(f'{o["label"]}：方法B {sb} と答え {ans} が違う')
            if oid in got:
                gv = got[oid]
                sg = f'{int(gv)}' if o['kind'] == 'area' and o.get('mode') == 'int' else f'{gv:.2f}'
                if sg != ans:
                    errs.append(f'{o["label"]}：電卓のキー列 {sg} と答え {ans} が違う')
    for st in spec['steps']:                       # 途中の点も方法Bと一致すること
        a = complex(*[float(x) for x in [p['fig']['points'][st['name']]['xy'][0], p['fig']['points'][st['name']]['xy'][1]]])
        b = Pb[st['name']]
        if abs(a - b) > 0.0051:
            errs.append(f'途中の点{st["name"]}：方法Aと方法Bが違う（{a} ／ {b}）')
    return errs
