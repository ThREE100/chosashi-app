"""S05（本番形式の統合問題）の分合筆の地積測量図：draw_forms.chiseki_solved と同じ描き方で、細長い（ロ）の符号・地積を引出し線で区画の外に書く（spec の lots の label_xy）。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from draw_forms import CH_H, INK, ACC, MUTE, frame, Map, _t, _l, dist_label, north_mark, svg_wrap  # noqa: E402,F401


def solved(s):
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
        if 'label_xy' in lot:                 # 細長い区画は、文字を区画の外の引出しの先に置く
            tx, ty = m(*lot['label_xy'])
            p.append(_l(cx, cy, tx, ty - 1.2, 0.25, MUTE))
            cx, cy = tx, ty
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
