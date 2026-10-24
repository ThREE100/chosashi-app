"""統合問題 s03：区分建物（階層的に区分した2階の（ロ）部分）の建物図面（1/500）と各階平面図（1/250）。
建物図面：敷地（2筆）と隣接地、一棟の建物の1階を点線、（ロ）部分の存する階（地上の最低階＝2階）の形状を実線、
建物の位置を示す距離、「建物の存する部分　2階」（規則第82条第1項、準則第52条第2項）。
各階平面図：（ロ）部分の2階部分の形状（内法）、周囲の長さ、床面積と求積方法（規則第83条第1項）。
spec：site_lots（{地番: 頂点}）、lot_labels、adj、toh1（一棟の1階・壁心）、unit（専有部分の存する階の形状）、unit_floor（'2階'）、
dists、addr、lots_text、house、loc、plan（内法の頂点）、plan_name、areas（求積の行）。"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import draw_forms as DF  # noqa: E402
from draw_forms import frame, Map, _t, _l, _poly, north_mark, dist_label, svg_wrap, BD_H, FP_H, ACC, MUTE  # noqa: E402


def solved(s):
    # ---- 建物図面
    cells = [(70, '土地の所在', s['addr']), (36, '地番', ''), (36, '家屋番号', ''), (40, '縮尺', '1/500')]
    p1, ar = frame(BD_H, '建　物　図　面', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    p1.append(_t(70.2 + 18, 7.2 + 6.4, s['lots_text'], 2.9, 'middle', weight='700'))
    p1.append(_t(106.2 + 18, 7.2 + 6.4, s['house'], 2.6, 'middle', weight='700'))
    allp = [c for v in s['site_lots'].values() for c in v]
    Xs, Ys = [c[0] for c in allp], [c[1] for c in allp]
    m = Map((ar[0], ar[1], ar[2], ar[3] - 8), 500, (min(Xs) - 2.5, max(Xs) + 2.5, min(Ys) - 3.0, max(Ys) + 3.0))
    for name, pts in s['site_lots'].items():
        p1.append(_poly(m, pts, 0.5))
    p1.append(_poly(m, s['toh1'], 0.45, '1.2 0.9'))                 # 一棟の建物の1階（点線）
    p1.append(_poly(m, s['unit'], 0.75, fill='#e8f4f0'))             # （ロ）部分の存する階（実線）
    for a, b, t in s['dists']:
        qa, qb = m(*a), m(*b)
        p1.append(_l(qa[0], qa[1], qb[0], qb[1], 0.3, ACC))
        if abs(qa[0] - qb[0]) < 0.01:
            p1.append(_t(qa[0] + 1.0, (qa[1] + qb[1]) / 2 + 0.9, t, 2.6, 'start', color=ACC))
        else:
            p1.append(_t((qa[0] + qb[0]) / 2, qa[1] - 0.9, t, 2.6, 'middle', color=ACC))
    for t, xy, w in s['lot_labels']:
        x, y = m(*xy)
        p1.append(_t(x, y, t, 3.2 if w else 3.0, 'middle', weight='700' if w else '400', color=DF.INK if w else MUTE))
    for t, xy in s['adj']:
        x, y = m(*xy)
        p1.append(_t(x, y, t, 3.0, 'middle', color=MUTE))
    for t, xy in s.get('marks', []):
        x, y = m(*xy)
        p1.append(_t(x, y, t, 2.6, 'middle', weight='700'))
    yb = ar[1] + ar[3] - 3.0
    p1.append(_t(ar[0] + 3, yb, '建物の存する部分　' + s['unit_floor'], 3.2, weight='700'))
    p1.append(_t(ar[0] + ar[2] - 3, yb, '実線：' + s['unit_name'] + '　点線：一棟の建物の1階', 2.5, 'end', color=MUTE))
    p1.append(north_mark(ar[0] + ar[2] - 8, ar[1] + 12))
    # ---- 各階平面図
    cells2 = [(70, '建物の所在', ''), (36, '家屋番号', ''), (36, '', ''), (40, '縮尺', '1/250')]
    p2, ar2 = frame(FP_H, '各　階　平　面　図', cells2, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    p2.append(_t(0.2 + 35, 7.2 + 6.4, s['loc'], 2.9, 'middle', weight='700'))
    p2.append(_t(70.2 + 18, 7.2 + 6.4, s['house'], 2.6, 'middle', weight='700'))
    ax, ay, aw, ah = ar2
    pts = s['plan']
    bn0, bn1 = min(c[0] for c in pts), max(c[0] for c in pts)
    bx0, bx1 = min(c[1] for c in pts), max(c[1] for c in pts)
    mm = Map((ax, ay + 8, aw, ah * 0.55), 250, (bn0 - 0.5, bn1 + 0.5, bx0 - 0.5, bx1 + 0.5))
    p2.append(_poly(mm, pts, 0.7, fill='#e8f4f0'))
    scr = [mm(*c) for c in pts]
    for j in range(len(pts)):
        u, v = pts[j], pts[(j + 1) % len(pts)]
        L = math.hypot(u[0] - v[0], u[1] - v[1])
        sd = DF._outside(scr, mm(*u), mm(*v))
        p2.append(dist_label(mm, u, v, f'{L:.2f}', side=sd, off=2.4, size=2.6))
    x0 = min(c[0] for c in scr)
    y0 = min(c[1] for c in scr)
    p2.append(_t(x0, y0 - 6.5, s['plan_name'], 3.4, weight='700'))
    y = ay + ah * 0.55 + 16
    p2.append(_l(ax, y - 4.0, ax + aw, y - 4.0, 0.2, MUTE))
    p2.append(_t(ax + 3, y, '床面積と求積方法', 3.0, weight='700'))
    for i, line in enumerate(s['areas']):
        p2.append(_t(ax + 3, y + 4.8 + i * 4.3, line, 2.8))
    p2.append(north_mark(ax + aw - 8, ay + 12))
    return svg_wrap(BD_H, p1), svg_wrap(FP_H, p2)
