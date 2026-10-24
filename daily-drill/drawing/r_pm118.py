"""PM-118〜PM-120（作図だけの夜の問題・建物図面と各階平面図）の模範の作図。
共有の tatemono_solved では描けない形（数筆の敷地と筆界、附属建物2棟、各階平面図の区画を3つ以上）を、spec のデータだけで描く。
PM-119・PM-120 の r_pm119.py・r_pm120.py は、この render をそのまま使う。

spec の形：
  addr・lot・house・loc（各階平面図の「建物の所在」）
  lots   = [{'poly': [[X, Y], …], 'label': '15番', 'xy': [X, Y]}, …]   … 敷地の各筆（2筆なら筆界も描かれる）
  blds   = [{'poly': [[X, Y], …], 'mark': '主である建物', 'xy': [X, Y], 'size': 2.6, 'fill': '#e8f4f0'}, …] … 建物図面に描く1階
  lotlines = [[[X, Y], [X, Y]], …]               … 建物の下を通る筆界（建物の塗りの上に重ねる）
  dists  = [[[X, Y], [X, Y], '3.92'], …]          … 建物の位置を示す距離（外壁の面 → 筆界）
  adj    = [['市道', [X, Y]], …]                   … 隣接地の地番
  panels = [{'name': '1階', 'poly': …, 'under': None または1階の poly, 'w': 区画の幅の割合, 'fill': …, 'inner': [辺の番号…], 'offs': {辺の番号: 辺からの離れ(mm)}}, …]
  areas  = ['床面積の行', …]、area_cols = 1 または 2
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import draw_forms as DF  # noqa: E402
from draw_forms import frame, Map, _t, _l, _poly, north_mark, dist_label, svg_wrap, ACC, MUTE, BD_H, FP_H  # noqa: E402


def render(s):
    cells = [(70, '土地の所在', s['addr']), (36, '地番', s['lot']), (36, '家屋番号', s['house']), (40, '縮尺', '1/500')]
    p1, ar = frame(BD_H, '建　物　図　面', cells, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    allp = [tuple(c) for lot in s['lots'] for c in lot['poly']]
    Xs, Ys = [c[0] for c in allp], [c[1] for c in allp]
    m = Map(ar, 500, (min(Xs) - 2.5, max(Xs) + 2.5, min(Ys) - 3.0, max(Ys) + 3.0))
    for lot in s['lots']:
        p1.append(_poly(m, lot['poly'], 0.5))
    for b in s['blds']:
        p1.append(_poly(m, b['poly'], 0.7, fill=b.get('fill', '#e8f4f0')))
        if b.get('mark'):
            x, y = m(*b['xy'])
            p1.append(_t(x, y, b['mark'], b.get('size', 2.6), 'middle', weight='700'))
    for a, b in s.get('lotlines', []):        # 建物の下を通る筆界は、建物の塗りの上に重ねて描く
        qa, qb = m(*a), m(*b)
        p1.append(_l(qa[0], qa[1], qb[0], qb[1], 0.5))
    for a, b, t in s['dists']:
        qa, qb = m(*a), m(*b)
        p1.append(_l(qa[0], qa[1], qb[0], qb[1], 0.3, ACC))
        if abs(qa[0] - qb[0]) < 0.01:          # 南北の距離（画面の縦の線）は線の右に
            p1.append(_t(qa[0] + 1.0, (qa[1] + qb[1]) / 2 + 0.9, t, 2.6, 'start', color=ACC))
        else:                                   # 東西の距離は線の上に
            p1.append(_t((qa[0] + qb[0]) / 2, qa[1] - 0.9, t, 2.6, 'middle', color=ACC))
    for t, xy in s['adj']:
        x, y = m(*xy)
        p1.append(_t(x, y, t, 3.0, 'middle', color=MUTE))
    for lot in s['lots']:
        x, y = m(*lot['xy'])
        p1.append(_t(x, y, lot['label'], 3.4, 'middle', weight='700'))
    p1.append(north_mark(ar[0] + ar[2] - 8, ar[1] + 12))

    cells2 = [(70, '建物の所在', ''), (36, '家屋番号', s['house']), (36, '', ''), (40, '縮尺', '1/250')]
    p2, ar2 = frame(FP_H, '各　階　平　面　図', cells2, [(91, '作成者', '（略）'), (91, '申請人', '（略）')], top_h=14.0, foot_h=12.0)
    p2.append(_t(0.2 + (14 + 70) / 2, 7.2 + 6.0, s['loc'], 3.4 if len(s['loc']) <= 14 else 3.0, 'middle', weight='700'))   # 長い所在は欄の名前と重ならないよう右に寄せて小さく
    ax, ay, aw, ah = ar2
    top = s.get('panel_h', 0.62)
    x0 = ax
    n_p = len(s['panels'])
    for i, pn in enumerate(s['panels']):
        w = aw * pn['w']
        pts_ = pn['poly']
        under = pn.get('under')
        ref = list(pts_) + list(under or [])
        sub = (x0, ay + 6, w, ah * top - 4)
        bn0, bn1 = min(c[0] for c in ref), max(c[0] for c in ref)
        bx0, bx1 = min(c[1] for c in ref), max(c[1] for c in ref)
        mm = Map(sub, 250, (bn0 - 0.5, bn1 + 0.5, bx0 - 0.5, bx1 + 0.5))
        p2.append(_poly(mm, pts_, 0.7, fill=pn.get('fill', '#e8f4f0')))
        if under:                               # 1階の位置の点線は、上の階の塗りに隠れないよう後から重ねる
            p2.append(_poly(mm, under, 0.35, '1.4 1.0'))
        scr = [mm(*c) for c in pts_]
        for j in range(len(pts_)):
            u, v = pts_[j], pts_[(j + 1) % len(pts_)]
            L = math.hypot(u[0] - v[0], u[1] - v[1])
            sd = DF._outside(scr, mm(*u), mm(*v))
            if j in pn.get('inner', []):
                sd = -sd
            p2.append(dist_label(mm, u, v, f'{L:.2f}', side=sd, off=pn.get('offs', {}).get(str(j), pn.get('offs', {}).get(j, 2.4)), size=2.6))
        p2.append(_t(sub[0] + 2, sub[1] - 1.4, pn['name'], 3.0, weight='700'))
        if i < n_p - 1:
            p2.append(_l(x0 + w, ay + 2, x0 + w, ay + ah * top, 0.2, MUTE, '0.8 0.8'))
        x0 += w
    y = ay + ah * top + 5
    p2.append(_l(ax, y - 3.5, ax + aw, y - 3.5, 0.2, MUTE))
    p2.append(_t(ax + 2, y, '床面積と求積方法', 3.0, weight='700'))
    cols = s.get('area_cols', 1)
    for i, line in enumerate(s['areas']):
        p2.append(_t(ax + 2 + (i % cols) * aw / cols, y + 4.6 + (i // cols) * 4.2, line, 2.8))
    p2.append(north_mark(ax + aw - 6, ay + ah * top + 6))
    return svg_wrap(BD_H, p1), svg_wrap(FP_H, p2)


solved = render
