"""PM-116：分筆線が2本以上ある地積測量図。共有の chiseki_solved で描いたうえで、spec['splits'] の分筆線を全部、外周と区別できる色の太線で描き足す
（共有の関数は分筆線を1本だけ色分けするため）。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import draw_forms as DF  # noqa: E402


def solved(s):
    s2 = {k: v for k, v in s.items() if k != 'renderer'}
    svg = DF.chiseki_solved(s2)
    # chiseki_solved と同じ位置合わせを作り直す
    _, area = DF.frame(DF.CH_H, '', [], [])
    pts = {k: tuple(v) for k, v in s['pts'].items()}
    allp = list(pts.values()) + [tuple(v) for v in s['datum'].values()]
    Xs, Ys = [q[0] for q in allp], [q[1] for q in allp]
    ax, ay, aw, ah = area
    m = DF.Map((ax, ay, aw, ah * 0.60), s['scale'], (min(Xs) - 1.5, max(Xs) + 1.5, min(Ys) - 1.5, max(Ys) + 1.5))
    add = []
    for u, v in s['splits']:
        a, b = m(*pts[u]), m(*pts[v])
        add.append(DF._l(a[0], a[1], b[0], b[1], 0.6, DF.ACC))
    for n in [n for uv in s['splits'] for n in uv]:      # 点の黒丸を線の上に描き直す
        x, y = m(*pts[n])
        add.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.0" fill="{DF.INK}"/>')
    return svg.replace('</svg>', ''.join(add) + '</svg>')
