"""作図ドリル（地積測量図・建物図面・各階平面図）の答案用紙の枠と、模範の作図（SVG）を作る。
単位は mm（viewBox の1単位＝1mm）。印刷時の幅は 182mm（A4の内側）なので、1/250 の 4mm/m、1/500 の 2mm/m はそのまま実寸になる。
作図は座標（X北・Y東）から機械で行い、辺長・方位・境界標の符号・求積表などの記載事項を入れる。"""
import math
from html import escape as E

INK, MUTE, ACC, SOFT = '#1d2b27', '#7a8782', '#c8461a', '#f2f8f6'
FONT = 'Noto Sans JP, Hiragino Sans, Yu Gothic, Meiryo, sans-serif'
W = 182.0


def _t(x, y, s, size=3.2, anchor='start', color=INK, weight='400', rot=None):
    tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot is not None else ''
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}"{tr} '
            f'stroke="#fff" stroke-width="0.9" paint-order="stroke" stroke-linejoin="round">{E(s)}</text>')


def _l(x1, y1, x2, y2, w=0.35, color=INK, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" stroke-width="{w}"{d} stroke-linecap="round"/>'


def _r(x, y, w, h, fill='none', stroke=INK, sw=0.35):
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def svg_wrap(h, parts, bg='#fff'):
    return (f'<svg class="fig draw" viewBox="0 0 {W} {h}" width="{W}mm" height="{h}mm" xmlns="http://www.w3.org/2000/svg" role="img" font-family="{FONT}">'
            f'<rect x="0" y="0" width="{W}" height="{h}" fill="{bg}"/>' + ''.join(parts) + '</svg>')


def frame(h, title, cells, footer, top_h=14.0, foot_h=16.0, y0=0.0):
    """答案用紙の枠。cells=[(幅, ラベル, 印刷する値 or '')]。footer=[(幅, ラベル, 印刷する値)]。描画領域の (x, y, w, h) を返す。"""
    p = [_r(0.2, y0 + 0.2, W - 0.4, h - 0.4, sw=0.6)]
    p.append(_t(W / 2, y0 + 5.4, title, 4.4, 'middle', weight='700'))
    x = 0.2
    yy = y0 + 7.2
    p.append(_l(0.2, yy, W - 0.2, yy))
    for w, lab, val in cells:
        p.append(_l(x, yy, x, yy + top_h - 7.2))
        p.append(_t(x + 1.2, yy + 3.4, lab, 2.6, color=MUTE))
        if val:
            p.append(_t(x + w / 2, yy + 6.0, val, 3.4, 'middle', weight='700'))
        x += w
    yb = y0 + top_h
    p.append(_l(0.2, yb, W - 0.2, yb))
    yf = y0 + h - foot_h
    p.append(_l(0.2, yf, W - 0.2, yf))
    x = 0.2
    for w, lab, val in footer:
        p.append(_l(x, yf, x, y0 + h - 0.2))
        p.append(_t(x + 1.2, yf + 3.6, lab, 2.6, color=MUTE))
        if val:
            p.append(_t(x + w / 2, yf + 10.5, val, 3.4, 'middle'))
        x += w
    return p, (0.2, yb, W - 0.4, yf - yb)


class Map:
    """実座標（X北・Y東, m）→ 枠内の mm。scale=縮尺の分母。area=(x, y, w, h)。bounds=(Xmin, Xmax, Ymin, Ymax)。"""
    def __init__(self, area, scale, bounds, align='center'):
        self.k = 1000.0 / scale
        ax, ay, aw, ah = area
        X0, X1, Y0, Y1 = bounds
        self.x0 = ax + (aw - (Y1 - Y0) * self.k) / 2
        self.y0 = ay + (ah - (X1 - X0) * self.k) / 2 + (X1 - X0) * self.k
        self.X0, self.Y0 = X0, Y0

    def __call__(self, X, Y):
        return self.x0 + (Y - self.Y0) * self.k, self.y0 - (X - self.X0) * self.k


def north_mark(x, y):
    return (_l(x, y + 9, x, y, 0.5) + f'<polygon points="{x:.2f},{y - 1.6:.2f} {x - 1.4:.2f},{y + 1.6:.2f} {x + 1.4:.2f},{y + 1.6:.2f}" fill="{INK}"/>' + _t(x, y - 2.6, 'N', 3.2, 'middle', weight='700'))


def dist_label(m, p, q, text, side=1, off=2.2, size=2.7, color=INK):
    """辺 p→q の中点に、辺の外側（side=1 なら進行方向の左、-1 なら右）へ寄せて距離を書く。pq は実座標。"""
    a, b = m(*p), m(*q)
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    ln = math.hypot(dx, dy) or 1
    nx, ny = -dy / ln * side, dx / ln * side
    ang = math.degrees(math.atan2(dy, dx))
    if ang > 90 or ang < -90:
        ang += 180
    return _t(mx + nx * off, my + ny * off + 0.9, text, size, 'middle', color=color, rot=round(ang, 1))


# ---------------- 地積測量図 ----------------
CH_H = 232.0


def chiseki_blank():
    cells = [(72, '土地の所在', ''), (50, '地番', ''), (60, '縮尺', '1/250')]
    p, area = frame(CH_H, '地　積　測　量　図', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')])
    return svg_wrap(CH_H, p)


def chiseki_solved(s):
    cells = [(72, '土地の所在', s['addr']), (50, '地番', s['lot_label']), (60, '縮尺', '1/250')]
    p, area = frame(CH_H, '地　積　測　量　図', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')])
    pts = {k: tuple(v) for k, v in s['pts'].items()}
    datum = {k: tuple(v) for k, v in s['datum'].items()}
    allp = list(pts.values()) + list(datum.values())
    Xs, Ys = [q[0] for q in allp], [q[1] for q in allp]
    ax, ay, aw, ah = area
    top = (ax, ay, aw, ah * 0.60)
    m = Map(top, s['scale'], (min(Xs) - 1.5, max(Xs) + 1.5, min(Ys) - 1.5, max(Ys) + 1.5))
    # 区画
    for lot in s['lots']:
        q = [m(*pts[n]) for n in lot['poly']]
        p.append('<polygon points="' + ' '.join(f'{a:.2f},{b:.2f}' for a, b in q) + f'" fill="none" stroke="{INK}" stroke-width="0.6" stroke-linejoin="round"/>')
        cx = sum(a for a, _ in q) / len(q)
        cy = sum(b for _, b in q) / len(q)
        p.append(_t(cx, cy, lot['name'], 4.2, 'middle', weight='700'))
        p.append(_t(cx, cy + 4.6, f"{lot['area']:.2f}㎡", 3.2, 'middle'))
    a, b = m(*pts[s['split'][0]]), m(*pts[s['split'][1]])
    p.append(_l(a[0], a[1], b[0], b[1], 0.6, ACC))
    # 辺長
    for (u, v, d, side) in s['sides']:
        p.append(dist_label(m, pts[u], pts[v], f'{d:.2f}', side))
    # 境界標・符号
    for n, q in pts.items():
        x, y = m(*q)
        p.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.0" fill="{INK}"/>')
        dx, dy = s['label_off'].get(n, (1.6, -1.6))
        p.append(_t(x + dx, y + dy, n, 3.4, 'start' if dx >= 0 else 'end', weight='700'))
    # 隣接地・道路の表示
    for t, xy in s['adj']:
        x, y = m(*xy)
        p.append(_t(x, y, t, 3.4, 'middle', color=MUTE))
    # 基準点
    for n, q in datum.items():
        x, y = m(*q)
        p.append(f'<polygon points="{x:.2f},{y - 1.8:.2f} {x - 1.6:.2f},{y + 1.2:.2f} {x + 1.6:.2f},{y + 1.2:.2f}" fill="none" stroke="{INK}" stroke-width="0.4"/>')
        p.append(_t(x + 2.2, y + 0.5, n, 3.0))
    d = list(datum.items())
    for i in range(len(d) - 1):
        a_, b_ = m(*d[i][1]), m(*d[i + 1][1])
        p.append(_l(a_[0], a_[1], b_[0], b_[1], 0.3, MUTE, '1.2 0.8'))
    p.append(north_mark(ax + aw - 10, ay + 14))
    # 下段：凡例と求積表
    y = ay + ah * 0.60 + 4
    p.append(_l(ax, y - 2, ax + aw, y - 2, 0.2, MUTE))
    p.append(_t(ax + 2, y + 2, '境界標（符号・種類）', 3.0, weight='700'))
    for i, (n, kind) in enumerate(s['markers']):
        p.append(_t(ax + 2, y + 6.4 + i * 4.2, f'{n}　{kind}', 2.9))
    xc = ax + aw * 0.40
    p.append(_t(xc, y + 2, '筆界点の座標値（X北・Y東, m）', 3.0, weight='700'))
    for i, (n, q) in enumerate(pts.items()):
        p.append(_t(xc, y + 6.4 + i * 4.2, f'{n}　{q[0]:.2f}　{q[1]:.2f}', 2.9))
    for i, (n, q) in enumerate(datum.items()):
        p.append(_t(xc, y + 6.4 + (len(pts) + i) * 4.2, f'基準点{n}　{q[0]:.2f}　{q[1]:.2f}', 2.9))
    xd = ax + aw * 0.72
    p.append(_t(xd, y + 2, '地積と求積方法', 3.0, weight='700'))
    for i, lot in enumerate(s['lots']):
        p.append(_t(xd, y + 6.4 + i * 4.2, f"{lot['name']}　{lot['area']:.2f}㎡", 2.9))
    p.append(_t(xd, y + 6.4 + len(s['lots']) * 4.2, f"求積方法：{s['method']}", 2.9))
    p.append(_t(xd, y + 6.4 + (len(s['lots']) + 1) * 4.2, f"測量年月日　{s['date']}", 2.9))
    p.append(_t(xd, y + 6.4 + (len(s['lots']) + 2) * 4.2, '方位：図の上が北', 2.9))
    return svg_wrap(CH_H, p)


# ---------------- 建物図面・各階平面図 ----------------
BD_H = 112.0
FP_H = 122.0


def tatemono_blank():
    p1, _ = frame(BD_H, '建　物　図　面', [(70, '土地の所在', ''), (36, '地番', ''), (36, '家屋番号', ''), (40, '縮尺', '1/500')], [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    p2, _ = frame(FP_H, '各　階　平　面　図', [(70, '建物の所在', ''), (36, '家屋番号', ''), (36, '', ''), (40, '縮尺', '1/250')], [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    return svg_wrap(BD_H, p1), svg_wrap(FP_H, p2)


def _poly(m, pts, w=0.6, dash=None, fill='none'):
    q = [m(*c) for c in pts]
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return '<polygon points="' + ' '.join(f'{a:.2f},{b:.2f}' for a, b in q) + f'" fill="{fill}" stroke="{INK}" stroke-width="{w}" stroke-linejoin="round"{d}/>'


def tatemono_solved(s):
    """s: site（敷地の頂点 (X,Y)）、bld1/bld2（外形の頂点 (X,Y)）、dists（建物の位置を示す距離 [(建物側の点,敷地側の点,テキスト)]）、adj、addr、lot、house"""
    cells = [(70, '土地の所在', s['addr']), (36, '地番', s['lot']), (36, '家屋番号', s['house']), (40, '縮尺', '1/500')]
    p1, area = frame(BD_H, '建　物　図　面', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    site = [tuple(c) for c in s['site']]
    Xs, Ys = [c[0] for c in site], [c[1] for c in site]
    m = Map(area, 500, (min(Xs) - 2.5, max(Xs) + 2.5, min(Ys) - 3.0, max(Ys) + 3.0))
    p1.append(_poly(m, site, 0.5))
    p1.append(_poly(m, s['bld1'], 0.7, fill='#e8f4f0'))
    for a, b, t in s['dists']:
        qa, qb = m(*a), m(*b)
        p1.append(_l(qa[0], qa[1], qb[0], qb[1], 0.3, ACC))
        p1.append(_t((qa[0] + qb[0]) / 2, (qa[1] + qb[1]) / 2 - 0.9, t, 2.6, 'middle', color=ACC))
    for t, xy in s['adj']:
        x, y = m(*xy)
        p1.append(_t(x, y, t, 3.0, 'middle', color=MUTE))
    x, y = m(*s['lot_xy'])
    p1.append(_t(x, y, s['lot'], 3.4, 'middle', weight='700'))
    p1.append(north_mark(area[0] + area[2] - 8, area[1] + 12))
    # 各階平面図
    cells2 = [(70, '建物の所在', s['addr'] + s['lot'] + '地'), (36, '家屋番号', s['house']), (36, '', ''), (40, '縮尺', '1/250')]
    p2, area2 = frame(FP_H, '各　階　平　面　図', cells2, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    ax, ay, aw, ah = area2
    half = (aw - 4) / 2
    allb = [c for c in s['bld1']]
    bx0, bx1 = min(c[1] for c in allb), max(c[1] for c in allb)
    bn0, bn1 = min(c[0] for c in allb), max(c[0] for c in allb)
    fl = []
    for i, (name, pts_, extra) in enumerate((('1階', s['bld1'], None), ('2階', s['bld2'], s['bld1']))):
        sub = (ax + 2 + i * (half + 0), ay + 6, half, ah * 0.58)
        mm = Map(sub, 250, (bn0 - 0.5, bn1 + 0.5, bx0 - 0.5, bx1 + 0.5))
        if extra:
            p2.append(_poly(mm, extra, 0.35, '1.4 1.0'))
        p2.append(_poly(mm, pts_, 0.7, fill='#e8f4f0'))
        n = len(pts_)
        cxy = (sum(c[0] for c in pts_) / n, sum(c[1] for c in pts_) / n)
        for j in range(n):
            u, v = pts_[j], pts_[(j + 1) % n]
            L = math.hypot(u[0] - v[0], u[1] - v[1])
            a, b = mm(*u), mm(*v)
            mx, my = (u[0] + v[0]) / 2, (u[1] + v[1]) / 2
            side = 1 if ((v[1] - u[1]) * (cxy[0] - u[0]) - (v[0] - u[0]) * (cxy[1] - u[1])) < 0 else -1
            p2.append(dist_label(mm, u, v, f'{L:.2f}', side=-side, off=2.4, size=2.6))
        p2.append(_t(sub[0] + 1, sub[1] + 3.4, name, 3.6, weight='700'))
    y = ay + ah * 0.58 + 10
    p2.append(_t(ax + 2, y, '床面積と求積方法', 3.0, weight='700'))
    for i, line in enumerate(s['areas']):
        p2.append(_t(ax + 2, y + 4.4 + i * 4.1, line, 2.8))
    p2.append(north_mark(ax + aw - 8, ay + 12))
    return svg_wrap(BD_H, p1), svg_wrap(FP_H, p2)
