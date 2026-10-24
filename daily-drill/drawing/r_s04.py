"""s04（合体後の建物）の建物図面・各階平面図。2筆（5番・6番）にまたがる敷地、合体後の建物の1階、各階平面図（1階・2階。2階の図に1階を点線）。
spec：lots [[地番, [(X,Y)…], 地番を書く位置]]・split（筆界の2点）・bld1・bld2・dists・adj・addr・lot（地番欄）・loc（建物の所在）・house・areas（求積の行）。
実寸：建物図面1/500（2mm/m）、各階平面図1/250（4mm/m）。不動産登記規則第82条・第83条の記載事項を描く。"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from draw_forms import (frame, Map, _t, _l, _poly, north_mark, dist_label, _outside, svg_wrap, BD_H, FP_H, INK, MUTE, ACC)  # noqa: E402


def solved(s):
    # ---- 建物図面（1/500）
    cells = [(70, '土地の所在', s['addr']), (36, '地番', s['lot']), (36, '家屋番号', s['house']), (40, '縮尺', '1/500')]
    p1, ar = frame(BD_H, '建　物　図　面', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    allp = [c for _, poly, _ in s['lots'] for c in poly]
    Xs, Ys = [c[0] for c in allp], [c[1] for c in allp]
    m = Map(ar, 500, (min(Xs) - 2.5, max(Xs) + 2.5, min(Ys) - 3.0, max(Ys) + 3.0))
    for name, poly, xy in s['lots']:
        p1.append(_poly(m, poly, 0.5))
    a, b = m(*s['split'][0]), m(*s['split'][1])
    p1.append(_l(a[0], a[1], b[0], b[1], 0.5))
    p1.append(_poly(m, s['bld1'], 0.7, fill='#e8f4f0'))
    for name, poly, xy in s['lots']:
        x, y = m(*xy)
        p1.append(_t(x, y, name, 3.4, 'middle', weight='700'))
    for qa_, qb_, t in s['dists']:
        qa, qb = m(*qa_), m(*qb_)
        p1.append(_l(qa[0], qa[1], qb[0], qb[1], 0.3, ACC))
        if abs(qa[0] - qb[0]) < 0.01:          # 南北の距離（画面の縦線）は右に
            p1.append(_t(qa[0] + 1.0, (qa[1] + qb[1]) / 2 + 0.9, t, 2.6, 'start', color=ACC))
        else:
            p1.append(_t((qa[0] + qb[0]) / 2, qa[1] - 0.9, t, 2.6, 'middle', color=ACC))
    for t, xy in s['adj']:
        x, y = m(*xy)
        p1.append(_t(x, y, t, 3.0, 'middle', color=MUTE))
    p1.append(north_mark(ar[0] + ar[2] - 8, ar[1] + 12))

    # ---- 各階平面図（1/250）：上段に1階、下段に2階（1階の位置を点線）。右の列に床面積と求積方法
    cells2 = [(70, '建物の所在', s['loc']), (36, '家屋番号', s['house']), (36, '', ''), (40, '縮尺', '1/250')]
    p2, ar2 = frame(FP_H, '各　階　平　面　図', cells2, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    ax, ay, aw, ah = ar2
    ref = s['bld1']
    bn0, bn1 = min(c[0] for c in ref), max(c[0] for c in ref)
    bx0, bx1 = min(c[1] for c in ref), max(c[1] for c in ref)
    wl = (bx1 - bx0 + 1.6) * 4 + 2
    rh = ah / 2
    for i, (name, pts_, under) in enumerate((('1階', s['bld1'], None), ('2階', s['bld2'], s['bld1']))):
        sub = (ax + 1, ay + i * rh, wl, rh)
        mm = Map(sub, 250, (bn0 - 0.9, bn1 + 0.7, bx0 - 0.8, bx1 + 0.8))
        if under:
            p2.append(_poly(mm, under, 0.35, '1.4 1.0'))
        p2.append(_poly(mm, pts_, 0.7, fill='#e8f4f0'))
        n = len(pts_)
        scr = [mm(*c) for c in pts_]
        for j in range(n):
            u, v = pts_[j], pts_[(j + 1) % n]
            L = math.hypot(u[0] - v[0], u[1] - v[1])
            p2.append(dist_label(mm, u, v, f'{L:.2f}', side=_outside(scr, mm(*u), mm(*v)), off=2.2, size=2.5))
        p2.append(_t(sub[0] + 1.5, sub[1] + 4.0, name, 3.4, weight='700'))
        if i == 0:
            p2.append(_l(ax, ay + rh, ax + wl + 2, ay + rh, 0.2, MUTE, '0.8 0.8'))
    xr = ax + wl + 3
    p2.append(_l(xr - 1.5, ay + 1, xr - 1.5, ay + ah - 1, 0.2, MUTE))
    p2.append(_t(xr, ay + 5, '床面積と求積方法', 3.0, weight='700'))
    for i, line in enumerate(s['areas']):
        p2.append(_t(xr, ay + 10 + i * 4.3, line, 2.5))
    p2.append(north_mark(ax + aw - 5, ay + ah - 14))
    return svg_wrap(BD_H, p1), svg_wrap(FP_H, p2)
