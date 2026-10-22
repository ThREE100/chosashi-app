"""夜の記述式ドリル：土地の境界点の計算の類題を作る・検算する。

座標は Z = X + Yi（X=北、Y=東）。複素数の反時計回り = 地図上の時計回り。
- gen_*()  : 乱数（シード固定）で問題を作り、複素数の式で答えを出す（方法A）
- verify() : 保存された問題を、実数の連立方程式・内積・外積など別の方法（方法B）で解き直し、答えと一致するか確かめる
答えは小数第2位まで（第3位を四捨五入）。四捨五入の境目に近い問題は作り直す。
"""
import cmath
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'note-articles-Kijyutsu', 'tools'))
from calc_helpers import to_dms  # noqa: E402

TOL = 0.0051  # 方法AとBの差の許容（丸めの範囲）


def fmt(x):
    return f'{x:.2f}'


def fz(z):
    return f'X = {z.real:.2f}、Y = {z.imag:.2f}'


def margin_ok(*vals):
    """四捨五入の境目（x.xx5）から 0.0008 以上離れている。"""
    for v in vals:
        r = (abs(v) * 100) % 1
        if abs(r - 0.5) < 0.08:
            return False
    return True


def dms_parts(deg):
    d = int(deg)
    m = int((deg - d) * 60)
    s = round(((deg - d) * 60 - m) * 60)
    if s == 60:
        s, m = 0, m + 1
    if m == 60:
        m, d = 0, d + 1
    return d, m, s


def dms_str(d, m, s):
    return f'{d}°{m:02d}′{s:02d}″'


def dms_rad(d, m, s):
    return math.radians(d + m / 60 + s / 3600)


def cross(u, v):
    return u.real * v.imag - u.imag * v.real


def dot(u, v):
    return u.real * v.real + u.imag * v.imag


def pt(rng, lo=100.0, hi=600.0):
    return complex(round(rng.uniform(lo, hi), 2), round(rng.uniform(lo, hi), 2))


# ---------- ① 放射 ----------
def gen_radial(seed):
    rng = random.Random(seed)
    while True:
        t1 = pt(rng)
        L = rng.uniform(20, 60)
        a = rng.uniform(0, 2 * math.pi)
        t2 = complex(round(t1.real + L * math.cos(a), 2), round(t1.imag + L * math.sin(a), 2))
        obs = []
        for _ in range(2):
            ang = (rng.randint(20, 340), rng.randint(0, 59), rng.randint(0, 59))
            d = round(rng.uniform(8, 45), 2)
            obs.append({'angle': list(ang), 'dist': d})
        base = cmath.phase(t2 - t1)
        ans = []
        for o in obs:
            z = t1 + cmath.rect(o['dist'], base + dms_rad(*o['angle']))
            ans.append(z)
        if margin_ok(*[c for z in ans for c in (z.real, z.imag)]):
            break
    names = ['A', 'B']
    return {
        'type': 'radial', 'title': '放射（後視点からの観測角と距離で点を出す）',
        'given': {'T1': [t1.real, t1.imag], 'T2': [t2.real, t2.imag], 'obs': [dict(name=n, **o) for n, o in zip(names, obs)]},
        'ask': [f'点{n}の座標' for n in names],
        'answers': [[fmt(z.real), fmt(z.imag)] for z in ans],
        'steps': _radial_steps(t1, t2, obs, names, ans),
        'trap': '観測角は後視方向から「時計回り」に足す（引くと反対側の点になる）。方向角は arg(後視点 − 器械点) で取り直す。',
    }


def _radial_steps(t1, t2, obs, names, ans):
    base = cmath.phase(t2 - t1)
    out = [f'方向角 arg(T2 − T1) ＝ {to_dms(base)}']
    for n, o, z in zip(names, obs, ans):
        out.append(f'{n} ＝ T1 ＋ {o["dist"]:.2f}∠(arg(T2 − T1) ＋ {dms_str(*o["angle"])}) ＝ {z.real:.4f} ＋ {z.imag:.4f}i → {fz(z)}')
    out.append('検算：余弦定理 A–T2間の距離² ＝ d² ＋ L² − 2dL・cos(観測角)。L ＝ |T2 − T1|。')
    return out


def verify_radial(p):
    g = p['given']
    t1, t2 = complex(*g['T1']), complex(*g['T2'])
    L = abs(t2 - t1)
    errs = []
    for o, a in zip(g['obs'], p['answers']):
        z = complex(float(a[0]), float(a[1]))
        d = o['dist']
        ang = dms_rad(*o['angle'])
        if abs(abs(z - t1) - d) > TOL * 2:
            errs.append(f"{o['name']}: T1からの距離が合わない")
        # 余弦定理（観測角は0〜360度なので cos は向きの区別がつかない → 外積の符号で時計回りを確かめる）
        d2 = d * d + L * L - 2 * d * L * math.cos(ang)
        if abs(abs(z - t2) - math.sqrt(d2)) > 0.02:
            errs.append(f"{o['name']}: 余弦定理の検算が合わない")
        # 地図上で時計回り = (T2−T1) から (z−T1) への外積(X北,Y東)が… 北をX・東をYとした座標で、時計回りに回ると 外積 cross(u,v)=u.x*v.y-u.y*v.x は正
        s = cross(t2 - t1, z - t1)
        want_pos = math.sin(ang) > 0
        if (s > 0) != want_pos:
            errs.append(f"{o['name']}: 回転の向きが合わない")
    return errs


# ---------- ② 2直線の交点 ----------
def gen_intersection(seed):
    rng = random.Random(seed)
    while True:
        a = pt(rng, 100, 300)
        b = a + complex(round(rng.uniform(20, 60), 2), round(rng.uniform(-30, 50), 2))
        c = a + complex(round(rng.uniform(-10, 40), 2), round(rng.uniform(20, 60), 2))
        dd = c + complex(round(rng.uniform(15, 60), 2), round(rng.uniform(-50, 10), 2))
        den = (dd - c).conjugate() * (b - a)
        if abs(den.imag) < 400:
            continue
        t = ((dd - c).conjugate() * (c - a)).imag / den.imag
        p = a + (b - a) * t
        if 0.15 < t < 0.9 and margin_ok(p.real, p.imag):
            break
    return {
        'type': 'intersection', 'title': '2直線の交点',
        'given': {'A': [a.real, a.imag], 'B': [b.real, b.imag], 'C': [c.real, c.imag], 'D': [dd.real, dd.imag]},
        'ask': ['直線ABと直線CDの交点Pの座標'],
        'answers': [[fmt(p.real), fmt(p.imag)]],
        'steps': [
            't ＝ Im(Conjg(D − C) × (C − A)) ÷ Im(Conjg(D − C) × (B − A))',
            f'  Conjg(D − C) × (C − A) の虚部 ＝ {((dd - c).conjugate() * (c - a)).imag:.4f}',
            f'  Conjg(D − C) × (B − A) の虚部 ＝ {den.imag:.4f}',
            f't ＝ {t:.6f}',
            f'P ＝ A ＋ t × (B − A) ＝ {p.real:.4f} ＋ {p.imag:.4f}i → {fz(p)}',
            '検算：Pは直線CD上にあるので、Im(Conjg(D − C) × (P − C)) ≒ 0。',
        ],
        'trap': 'Im（虚部）を取るのは、2つの Conjg の積の「iの係数」。実部（内積）を使うと直角の判定になってしまう。',
    }


def verify_intersection(p):
    g = p['given']
    a, b, c, d = (complex(*g[k]) for k in 'ABCD')
    # 方法B：実数の連立方程式 a + t(b-a) = c + s(d-c) をクラメルの公式で解く
    r1, r2 = b - a, c - d
    rhs = c - a
    det = r1.real * r2.imag - r1.imag * r2.real
    t = (rhs.real * r2.imag - rhs.imag * r2.real) / det
    px, py = a.real + t * r1.real, a.imag + t * r1.imag
    ans = p['answers'][0]
    errs = []
    if abs(px - float(ans[0])) > TOL or abs(py - float(ans[1])) > TOL:
        errs.append(f'交点が合わない（連立方程式の解 {px:.3f}, {py:.3f}）')
    z = complex(float(ans[0]), float(ans[1]))
    if abs(cross(d - c, z - c)) / abs(d - c) > 0.01:
        errs.append('Pが直線CD上にない')
    if abs(cross(b - a, z - a)) / abs(b - a) > 0.01:
        errs.append('Pが直線AB上にない')
    return errs


# ---------- ③ 垂線の足 ----------
def gen_foot(seed):
    rng = random.Random(seed)
    while True:
        f = pt(rng, 100, 300)
        h = f + complex(round(rng.uniform(15, 50), 2), round(rng.uniform(15, 50), 2))
        w0 = rng.uniform(0.2, 0.85)
        off = rng.uniform(4, 15) * rng.choice([-1, 1])
        base = f + (h - f) * w0
        n = 1j * (h - f) / abs(h - f)
        e0 = base + n * off
        e = complex(round(e0.real, 2), round(e0.imag, 2))
        w = (e - f) / (h - f)
        g = f + (h - f) * w.real
        if 0.1 < w.real < 0.9 and margin_ok(g.real, g.imag):
            break
    return {
        'type': 'foot', 'title': '垂線の足',
        'given': {'F': [f.real, f.imag], 'H': [h.real, h.imag], 'E': [e.real, e.imag]},
        'ask': ['点Eから直線FHに下ろした垂線の足Gの座標'],
        'answers': [[fmt(g.real), fmt(g.imag)]],
        'steps': [
            'w ＝ (E − F) ÷ (H − F)',
            f'  w ＝ {w.real:.6f} ＋ {w.imag:.6f}i（実部が「FからGまでがFHの何倍か」、虚部は垂線の長さの比）',
            f'G ＝ F ＋ (H − F) × Re(w) ＝ {g.real:.4f} ＋ {g.imag:.4f}i → {fz(g)}',
            f'検算：GE ⊥ FH（内積 ≒ 0）。垂線の長さ ＝ |Im(w)| × |H − F| ＝ {abs(w.imag) * abs(h - f):.3f} m。',
        ],
        'trap': '「真南に下ろした点」や「真西に下ろした点」と取り違えない。FHが傾いていると、垂線の足はEの真横にはならない。',
    }


def verify_foot(p):
    g_ = p['given']
    f, h, e = complex(*g_['F']), complex(*g_['H']), complex(*g_['E'])
    ans = p['answers'][0]
    z = complex(float(ans[0]), float(ans[1]))
    errs = []
    # 方法B：射影 t = ((E-F)·(H-F)) / |H-F|² を実数で
    t = dot(e - f, h - f) / abs(h - f) ** 2
    gx, gy = f.real + t * (h - f).real, f.imag + t * (h - f).imag
    if abs(gx - z.real) > TOL or abs(gy - z.imag) > TOL:
        errs.append(f'垂線の足が合わない（射影 {gx:.3f}, {gy:.3f}）')
    if abs(dot(e - z, h - f)) / abs(h - f) > 0.01:
        errs.append('GE と FH が直交していない')
    if abs(cross(h - f, z - f)) / abs(h - f) > 0.01:
        errs.append('Gが直線FH上にない')
    return errs


# ---------- ④ 平行線の離れ ----------
def gen_parallel(seed):
    rng = random.Random(seed)
    while True:
        a = pt(rng, 100, 300)
        b = a + complex(round(rng.uniform(30, 60), 2), round(rng.uniform(-8, 8), 2))   # ほぼ南北
        d_off = rng.choice([1.00, 1.50, 2.00, 2.50, 3.00])
        c = a + complex(round(rng.uniform(5, 25), 2), round(rng.uniform(-20, -12), 2))   # 西側
        dd = c + complex(round(rng.uniform(-10, 10), 2), round(rng.uniform(25, 45), 2))   # 東へ延びる線
        u = (b - a) / abs(b - a)
        n = -1j * u                      # 西側（Yが小さい側）の単位法線
        assert n.imag < 0
        a2 = a + n * d_off
        den = (dd - c).conjugate() * (b - a)
        if abs(den.imag) < 300:
            continue
        t = ((dd - c).conjugate() * (c - a2)).imag / den.imag
        p = a2 + (b - a) * t
        if margin_ok(p.real, p.imag) and 0 < t < 1:
            break
    return {
        'type': 'parallel', 'title': '平行で離れた直線との交点',
        'given': {'A': [a.real, a.imag], 'B': [b.real, b.imag], 'C': [c.real, c.imag], 'D': [dd.real, dd.imag], 'off': d_off},
        'ask': [f'直線ABに平行で、その西側に{d_off:.2f}m離れた直線と、直線CDとの交点Pの座標'],
        'answers': [[fmt(p.real), fmt(p.imag)]],
        'steps': [
            f'ABの単位ベクトル u ＝ (B − A) ÷ Abs(B − A)。西側（Yが小さい側）への単位法線 n ＝ −i × u（|n| ＝ 1、Im(n) ＝ {n.imag:.4f} ＜ 0 を確認）',
            f'A′ ＝ A ＋ {d_off:.2f} × n ＝ {a2.real:.4f} ＋ {a2.imag:.4f}i（ABを西へ{d_off:.2f}m平行移動した直線は A′ を通り、向きは B − A）',
            f't ＝ Im(Conjg(D − C) × (C − A′)) ÷ Im(Conjg(D − C) × (B − A)) ＝ {t:.6f}',
            f'P ＝ A′ ＋ t × (B − A) ＝ {p.real:.4f} ＋ {p.imag:.4f}i → {fz(p)}',
            f'検算：Pと直線ABとの距離 ＝ {abs(cross(b - a, p - a)) / abs(b - a):.3f} m（＝{d_off:.2f}m）。',
        ],
        'trap': '離れは「直角に測る」。X（またはY）の座標だけを{0:.2f}ずらす方法は、ABが傾いていると誤差が出る。'.format(d_off),
    }


def verify_parallel(p):
    g = p['given']
    a, b, c, d = (complex(*g[k]) for k in 'ABCD')
    off = g['off']
    ans = p['answers'][0]
    z = complex(float(ans[0]), float(ans[1]))
    errs = []
    # 方法B：Pは直線CD上、かつABから西側へ直角に off 離れた位置。符号付き距離（外積/長さ）と実数の連立方程式で確かめる
    sd = cross(b - a, z - a) / abs(b - a)     # 外積が正 = 進行方向の右側（東側）
    if abs(abs(sd) - off) > 0.01:
        errs.append(f'ABからの離れが{off}mでない（{abs(sd):.3f}）')
    if sd > 0:
        errs.append('ABの西側ではなく東側にある')
    if abs(cross(d - c, z - c)) / abs(d - c) > 0.01:
        errs.append('Pが直線CD上にない')
    return errs


# ---------- ⑤ 四角形の面積（対角線の式） ----------
def gen_area(seed):
    rng = random.Random(seed)
    while True:
        a = pt(rng, 100, 300)
        w, h = rng.uniform(18, 36), rng.uniform(14, 30)
        # 北から時計回り：A（南西）→B（北西）→C（北東）→D（南東）
        pts = [a,
               a + complex(round(h + rng.uniform(-4, 4), 2), round(rng.uniform(-3, 3), 2)),
               a + complex(round(h + rng.uniform(-4, 4), 2), round(w + rng.uniform(-4, 4), 2)),
               a + complex(round(rng.uniform(-3, 3), 2), round(w + rng.uniform(-4, 4), 2))]
        pts = [complex(round(z.real, 2), round(z.imag, 2)) for z in pts]
        # 時計回りの凸四角形
        cs = [cross(pts[(i + 1) % 4] - pts[i], pts[(i + 2) % 4] - pts[(i + 1) % 4]) for i in range(4)]
        if not all(c > 0 for c in cs):
            continue
        A, B, C, D = pts
        raw = abs(((C - A).conjugate() * (D - B)).imag) / 2
        if 0.05 < (raw * 100) % 1 < 0.95:   # 切捨ての境目（x.xx0）に近い問題は避ける
            break
    A, B, C, D = pts
    ans = math.floor(raw * 100) / 100
    return {
        'type': 'area', 'title': '四角形の面積（対角線の式）と地積',
        'given': {k: [z.real, z.imag] for k, z in zip('ABCD', pts)},
        'ask': ['四角形ABCD（A→B→C→Dの順に時計回り）の面積を求め、宅地の地積として答えなさい'],
        'answers': [[f'{ans:.2f}']],
        'steps': [
            'S ＝ |Im(Conjg(C − A) × (D − B))| ÷ 2（対角線AC・BDの外積の半分）',
            f'  Im(Conjg(C − A) × (D − B)) ＝ {((C - A).conjugate() * (D - B)).imag:.4f}',
            f'S ＝ {raw:.4f} ㎡',
            f'宅地の地積は、小数第2位未満の端数を切り捨てる（不動産登記規則第100条）→ {ans:.2f} ㎡',
            '検算：座標法（ガウスの公式）で ½|Σ(Xi・Yi+1 − Xi+1・Yi)| を求めて一致するか。',
        ],
        'trap': '地積は四捨五入ではなく切り捨て（宅地は小数第2位未満）。対角線の式は、頂点が一周する順に並んでいるときだけ使える。',
        'basis': [{'law': '不動産登記規則', 'article': '第100条', 'quote': '一平方メートルの百分の一（宅地及び鉱泉地以外の土地で十平方メートルを超えるものについては、一平方メートル）未満の端数は、切り捨てる'}],
    }


def verify_area(p):
    pts = [complex(*p['given'][k]) for k in 'ABCD']
    # 方法B：ガウスの公式（靴ひも）
    s = 0.0
    for i in range(4):
        z0, z1 = pts[i], pts[(i + 1) % 4]
        s += z0.real * z1.imag - z1.real * z0.imag
    raw = abs(s) / 2
    ans = float(p['answers'][0][0])
    errs = []
    if abs(math.floor(raw * 100) / 100 - ans) > 0.0001:
        errs.append(f'地積が合わない（ガウスの公式 {raw:.4f} → 切捨て {math.floor(raw * 100) / 100:.2f}）')
    return errs


GEN = {'radial': gen_radial, 'intersection': gen_intersection, 'foot': gen_foot, 'parallel': gen_parallel, 'area': gen_area}
VERIFY = {'radial': verify_radial, 'intersection': verify_intersection, 'foot': verify_foot, 'parallel': verify_parallel, 'area': verify_area}
