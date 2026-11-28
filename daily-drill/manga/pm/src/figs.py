"""毎日ドリル（夜）の学習まんがに差し込む図を、問題データ（evening/problems/PM-NN.json の fig）から正確に作る。
図は daily-drill/figure.py の svg_generic（ドリルの問題・解答ページと同じ作図）で描き、SVG と PNG の両方を fig/ に保存する。
命名：fig/<問題ID>_<種類>.svg / .png（例 PM-01_mondai）。PNG は漫画の枠の2倍の大きさ（枠 944×661 なら 1888×1322）。
使い方：python3 daily-drill/manga/pm/src/figs.py [日 ...]（台本の fig を全部作る。Chromium で SVG を PNG に書き出す）"""
import json
import os
import sys
from html import escape as E

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import DD, FIG, problem, scripts  # noqa: E402
sys.path.insert(0, DD)
import figure  # noqa: E402

VH = 700   # 図の縦（viewBox 1000×700）。枠は 944×661（同じ縦横比）


def _coord_labels(fig, pts_xy, pos):
    """答えの点に座標（X, Y）を書き足す（svg_generic と同じ縮尺を作り直して位置を出す）。pts_xy: {名: (値X, 値Y) の文字列}。
    pos: {名: (dx, dy)}（台本の coord_pos。dx が負なら右寄せ）。ラベルが重ならない位置を台本で決め、画像を目で確かめる。"""
    P = {k: tuple(v['xy']) for k, v in fig['points'].items()}
    extra = [tuple(t['xy']) for t in fig.get('texts', [])]
    if 'road' in fig:
        extra += [tuple(fig['road']['a']), tuple(fig['road']['b'])]
    h0 = figure.H
    figure.H = VH
    try:
        f = figure.Fig(list(P.values()) + extra)
        out = []
        for nm, (x, y) in pts_xy.items():
            px, py = f.xy(P[nm])
            dx, dy = pos.get(nm, (16, 42))
            out.append(f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" font-size="28" fill="{figure.ACC}" font-weight="700" '
                       f'text-anchor="{"end" if dx < 0 else "start"}" stroke="#fff" stroke-width="7" paint-order="stroke" '
                       f'stroke-linejoin="round">{E(f"（{x}, {y}）")}</text>')
        return ''.join(out)
    finally:
        figure.H = h0


def make_svg(spec, P):
    """spec: 台本の fig（name, kind, rect, …）。kind：mondai＝問題の図、kotae＝答えの図（座標つき）、sub＝問題の図の一部（points・lines を絞る）"""
    fig = P['fig']
    kind = spec['kind']
    if kind == 'mondai':
        return figure.svg_generic(fig, reveal=False, vh=VH)
    if kind == 'kotae':
        s = figure.svg_generic(fig, reveal=True, vh=VH)
        ans = {a['label'].replace('点', ''): a['value'] for a in P['answers'] if a['kind'] == 'xy'}
        return s.replace('</svg>', _coord_labels(fig, ans, spec.get('coord_pos', {})) + '</svg>')
    if kind == 'sub':
        keep = spec['points']
        sub = dict(points={k: dict(fig['points'][k], kind=spec.get('kinds', {}).get(k, fig['points'][k]['kind'])) for k in keep},
                   polys=[pg for pg in fig.get('polys', []) if all(n in keep for n in pg['pts'])],
                   lines=spec['lines'], texts=fig.get('texts', []))
        if 'road' in fig:
            sub['road'] = fig['road']
        return figure.svg_generic(sub, reveal=True, vh=VH)
    raise ValueError(kind)


def specs():
    """[(台本, fig の指定)]"""
    return [(M, p['fig']) for M in scripts() for pg in M['pages'] for p in pg['panels'] if p.get('fig')]


def write_all(days=()):
    from playwright.sync_api import sync_playwright
    todo = [(M, f) for M, f in specs() if not days or M['day'] in days]
    with sync_playwright() as pw:
        import glob
        exe = (glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome') + glob.glob('/opt/pw-browsers/chromium'))
        br = pw.chromium.launch(executable_path=exe[0]) if exe else pw.chromium.launch()
        pg = br.new_page()
        for M, f in todo:
            P = problem(M['problem'])
            svg = make_svg(f, P)
            open(os.path.join(FIG, f['name'] + '.svg'), 'w', encoding='utf-8').write(svg)
            w, h = f['rect'][2] * 2, f['rect'][3] * 2
            pg.set_viewport_size({'width': w, 'height': h})
            sized = svg.replace('<svg ', '<svg width="%d" height="%d" preserveAspectRatio="xMidYMid meet" ' % (w, h), 1)
            pg.set_content('<html><body style="margin:0;background:#fff"><div style="width:%dpx;height:%dpx">%s</div></body></html>' % (w, h, sized))
            pg.screenshot(path=os.path.join(FIG, f['name'] + '.png'), clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            print('図', f['name'], f'{w}×{h}')
        br.close()


if __name__ == '__main__':
    write_all({int(x) for x in sys.argv[1:]})
