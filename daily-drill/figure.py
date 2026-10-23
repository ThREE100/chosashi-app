"""夜の計算ドリルの図（インライン SVG）を作る。
座標は X＝北（図の上）、Y＝東（図の右）。与えられた点は黒丸、求める点は赤い白抜きの丸（解答では赤丸＋座標）。
座標の数値は図に重ねず、別の表（build.py）に出す。"""
import cmath
import math
from html import escape as E

W, H = 1000, 700          # viewBox（A4の横幅いっぱいに出す）
PAD = 70                  # 図形のまわりの余白
PAD_B = 105               # 下は点の座標・ラベル用に広く
PAD_R = 150               # 右は方位記号用に広く
INK, MUTE, ACC = '#1d2b27', '#7a8782', '#c8461a'


class Fig:
    def __init__(self, pts):
        ys = [y for _, y in pts]
        xs = [x for x, _ in pts]
        self.y0, self.y1, self.x0, self.x1 = min(ys), max(ys), min(xs), max(xs)
        sw = max(self.y1 - self.y0, 1e-6)
        sh = max(self.x1 - self.x0, 1e-6)
        self.s = min((W - PAD - PAD_R) / sw, (H - PAD - PAD_B) / sh)
        self.ox = PAD + (W - PAD - PAD_R - sw * self.s) / 2
        self.oy = PAD_B + (H - PAD - PAD_B - sh * self.s) / 2

    def xy(self, p):
        """(X北, Y東) → 画面座標"""
        return self.ox + (p[1] - self.y0) * self.s, H - (self.oy + (p[0] - self.x0) * self.s)


def _line(a, b, dash=False, color=INK, w=3):
    d = ' stroke-dasharray="14 9"' if dash else ''
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{color}" stroke-width="{w}"{d} stroke-linecap="round"/>'


def _label(pos, text, dx=14, dy=-14, size=34, color=INK, anchor='start', weight='700'):
    return (f'<text x="{pos[0] + dx:.1f}" y="{pos[1] + dy:.1f}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="7" paint-order="stroke" stroke-linejoin="round">{E(text)}</text>')


def _pt(pos, name, kind, coord=None):
    if kind == 'given':
        c = f'<circle cx="{pos[0]:.1f}" cy="{pos[1]:.1f}" r="9" fill="{INK}"/>'
    elif kind == 'unknown':
        c = f'<circle cx="{pos[0]:.1f}" cy="{pos[1]:.1f}" r="11" fill="#fff" stroke="{ACC}" stroke-width="5"/>'
    else:   # 解答で求めた点
        c = f'<circle cx="{pos[0]:.1f}" cy="{pos[1]:.1f}" r="11" fill="{ACC}"/>'
    color = ACC if kind != 'given' else INK
    t = _label(pos, name, color=color)
    if coord:
        t += _label(pos, coord, dy=34, size=26, color=ACC, weight='500')
    return c + t


def _extend(a, b, k0, k1):
    """直線 a→b を、a から k0 倍・b を超えて k1 倍まで延長した両端（実座標）"""
    za, zb = complex(*a), complex(*b)
    d = zb - za
    p, q = za + d * k0, za + d * k1
    return (p.real, p.imag), (q.real, q.imag)


def _north(x=930, y=110):
    return (f'<g><line x1="{x}" y1="{y + 60}" x2="{x}" y2="{y}" stroke="{INK}" stroke-width="4"/>'
            f'<polygon points="{x},{y - 14} {x - 11},{y + 14} {x + 11},{y + 14}" fill="{INK}"/>'
            f'<text x="{x}" y="{y - 24}" font-size="32" font-weight="700" text-anchor="middle" fill="{INK}" stroke="#fff" stroke-width="6" paint-order="stroke">北</text></g>')


def _dms(a):
    return f'{a[0]}°{a[1]:02d}′{a[2]:02d}″'


def svg(p, reveal=False):
    """p: 夜の計算問題。reveal=True で求める点を赤丸＋座標で描く。"""
    t, g = p['type'], p['given']
    ans = [tuple(float(v) for v in a) for a in p['answers']]
    parts = []

    def ptn(name):
        return tuple(g[name])

    if t == 'radial':
        t1, t2 = ptn('T1'), ptn('T2')
        us = [(o['name'], (ans[i][0], ans[i][1])) for i, o in enumerate(g['obs'])]
        f = Fig([t1, t2] + [u for _, u in us])
        a1, a2 = f.xy(t1), f.xy(t2)
        parts.append(_line(a1, a2))
        base = cmath.phase(complex(t2[1] - t1[1], t2[0] - t1[0]))   # 画面上の角度の基準は不要。実座標の方向角で弧を描く
        for o, (nm, u) in zip(g['obs'], us):
            au = f.xy(u)
            parts.append(_line(a1, au, dash=True, color=MUTE))
            # 後視 T2 から時計回り（地図上）の弧
            ang_t2 = math.atan2(a2[1] - a1[1], a2[0] - a1[0])      # 画面座標（y下向き）での T2 方向
            ang_u = math.atan2(au[1] - a1[1], au[0] - a1[0])
            r = 70 + 30 * (1 if nm == 'B' else 0)
            sweep = (ang_u - ang_t2) % (2 * math.pi)                 # 画面で時計回り＝地図で時計回り
            x1, y1 = a1[0] + r * math.cos(ang_t2), a1[1] + r * math.sin(ang_t2)
            x2, y2 = a1[0] + r * math.cos(ang_u), a1[1] + r * math.sin(ang_u)
            large = 1 if sweep > math.pi else 0
            parts.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f}" fill="none" stroke="{ACC}" stroke-width="3"/>')
            parts.append(_label(au, f'{_dms(o["angle"])}　{o["dist"]:.2f}m', dx=0, dy=(-42 if reveal else 58), size=26, color=INK, anchor='middle', weight='500'))
        parts.append(_pt(a1, 'T1', 'given'))
        parts.append(_pt(a2, 'T2', 'given'))
        for i, (nm, u) in enumerate(us):
            parts.append(_pt(f.xy(u), nm, 'reveal' if reveal else 'unknown', f'({ans[i][0]:.2f}, {ans[i][1]:.2f})' if reveal else None))
    elif t == 'intersection':
        A, B, C, D = (ptn(k) for k in 'ABCD')
        P = ans[0]
        f = Fig([A, B, C, D, P])
        for u, v in ((A, B), (C, D)):
            far = [P, u, v]
            # 交点まで延ばす点線
            for end in (u, v):
                if math.dist(end, P) > 1e-6:
                    pass
            parts.append(_line(f.xy(A), f.xy(B)))
            parts.append(_line(f.xy(C), f.xy(D)))
        # P に向けて延長（線分の外にあれば点線）
        for u, v in ((A, B), (C, D)):
            zu, zv, zp = complex(*u), complex(*v), complex(*P)
            k = ((zp - zu) / (zv - zu)).real
            if k > 1:
                parts.append(_line(f.xy(v), f.xy(P), dash=True, color=MUTE))
            elif k < 0:
                parts.append(_line(f.xy(u), f.xy(P), dash=True, color=MUTE))
        for nm in 'ABCD':
            parts.append(_pt(f.xy(ptn(nm)), nm, 'given'))
        parts.append(_pt(f.xy(P), 'P', 'reveal' if reveal else 'unknown', f'({P[0]:.2f}, {P[1]:.2f})' if reveal else None))
    elif t == 'foot':
        F_, H_, E_ = ptn('F'), ptn('H'), ptn('E')
        G = ans[0]
        f = Fig([F_, H_, E_, G])
        parts.append(_line(f.xy(F_), f.xy(H_)))
        parts.append(_line(f.xy(E_), f.xy(G), dash=True, color=MUTE))
        # 直角記号
        g_, e_, h_ = f.xy(G), f.xy(E_), f.xy(H_)
        ue = ((e_[0] - g_[0]), (e_[1] - g_[1]))
        uh = ((h_[0] - g_[0]), (h_[1] - g_[1]))
        ne, nh = math.hypot(*ue), math.hypot(*uh)
        s = 24
        ue = (ue[0] / ne * s, ue[1] / ne * s)
        uh = (uh[0] / nh * s, uh[1] / nh * s)
        parts.append(f'<polyline points="{g_[0] + ue[0]:.1f},{g_[1] + ue[1]:.1f} {g_[0] + ue[0] + uh[0]:.1f},{g_[1] + ue[1] + uh[1]:.1f} {g_[0] + uh[0]:.1f},{g_[1] + uh[1]:.1f}" fill="none" stroke="{ACC}" stroke-width="3"/>')
        for nm, v in (('F', F_), ('H', H_), ('E', E_)):
            parts.append(_pt(f.xy(v), nm, 'given'))
        parts.append(_pt(g_, 'G', 'reveal' if reveal else 'unknown', f'({G[0]:.2f}, {G[1]:.2f})' if reveal else None))
    elif t == 'parallel':
        A, B, C, D = (ptn(k) for k in 'ABCD')
        off = g['off']
        P = ans[0]
        zu = (complex(*B) - complex(*A))
        n = -1j * zu / abs(zu)
        A2 = complex(*A) + n * off
        B2 = complex(*B) + n * off
        f = Fig([A, B, C, D, P, (A2.real, A2.imag), (B2.real, B2.imag)])
        parts.append(_line(f.xy(A), f.xy(B)))
        parts.append(_line(f.xy(C), f.xy(D)))
        a2, b2 = f.xy((A2.real, A2.imag)), f.xy((B2.real, B2.imag))
        # 平行線（AB から西へ off）を P の先まで
        zp = complex(*P)
        k = ((zp - A2) / (B2 - A2)).real
        lo, hi = min(0, k), max(1, k)
        s_, e_ = _extend((A2.real, A2.imag), (B2.real, B2.imag), lo, hi)
        parts.append(_line(f.xy(s_), f.xy(e_), dash=True, color=MUTE))
        # 離れの寸法線（A→A'）
        aa, aa2 = f.xy(A), a2
        parts.append(_line(aa, aa2, color=ACC, w=4))
        parts.append(_label(((aa[0] + aa2[0]) / 2, (aa[1] + aa2[1]) / 2), f'AB から西へ {off:.2f}m（直角）', dx=-14, dy=46, size=28, color=ACC, anchor='end'))
        for nm in 'ABCD':
            parts.append(_pt(f.xy(ptn(nm)), nm, 'given'))
        parts.append(_pt(f.xy(P), 'P', 'reveal' if reveal else 'unknown', f'({P[0]:.2f}, {P[1]:.2f})' if reveal else None))
    elif t == 'area':
        pts = [ptn(k) for k in 'ABCD']
        f = Fig(pts)
        sp = [f.xy(q) for q in pts]
        parts.append('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in sp) + f'" fill="#e8f4f0" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
        parts.append(_line(sp[0], sp[2], dash=True, color=MUTE))
        parts.append(_line(sp[1], sp[3], dash=True, color=MUTE))
        for nm, q in zip('ABCD', sp):
            parts.append(_pt(q, nm, 'given'))
        cx = sum(x for x, _ in sp) / 4
        cy = sum(y for _, y in sp) / 4
        parts.append(_label((cx, cy), f'地積 {p["answers"][0][0]} ㎡' if reveal else '宅地', dx=0, dy=10, size=34, color=ACC if reveal else MUTE, anchor='middle'))
    parts.append(_north())
    return (f'<svg class="fig" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'font-family="Noto Sans JP, Hiragino Sans, Yu Gothic, Meiryo, sans-serif">'
            f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" fill="#fff" stroke="#cfd8d4" stroke-width="3" rx="14"/>'
            + ''.join(parts) + '</svg>')
