"""記述式（土地・第21問）解説図の作図ヘルパー。

`prompt_kaisetsuzu-gazou_kihon-form_tochi.md`（第21問の解説用インフォグラフィック 共通・基本フォーム）の
作図ルールを Python（matplotlib）で実装したもの。問題ごとの作図スクリプト（`{年度}/Q21/zu/draw_*.py`）から使う。

座標の約束（測量の座標系）:
    点は (X, Y) = (北, 東)。作図では 横軸＝Y（東）、縦軸＝X（北）。縦横の縮尺は必ず同じ。

文字の置き方（基本フォームの「文字の配置ルール」）:
    - 辺長：辺の中点から、図形の外側へ（外向きの法線方向へ）ずらし、辺と平行に書く。上下逆さまにしない
    - 点名：隣り合う2辺の外角の二等分線の方向（図形の外側）へずらす
    - 座標値：引き出し線付きの吹き出しで、図形から離れた余白に置く
    - 描いたあとに check_overlaps() で、文字どうし・文字と線・文字と点の重なりを機械的に検査する。
      place_* 系の関数は、候補位置を順に試して重ならない位置を自動で選ぶ

このファイルは問題に依存しない。
"""
import math

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Polygon, Arc, FancyArrowPatch  # noqa: E402
from matplotlib.transforms import Bbox  # noqa: E402
from matplotlib.text import Text  # noqa: E402

# ---- フォント -------------------------------------------------------------
_JP_FONTS = ['Noto Sans CJK JP', 'Noto Sans JP', 'IPAGothic', 'IPAexGothic', 'TakaoGothic']


def setup_font():
    names = {f.name for f in font_manager.fontManager.ttflist}
    for n in _JP_FONTS:
        if n in names:
            plt.rcParams['font.family'] = n
            return n
    raise RuntimeError('日本語フォントがありません（Noto Sans CJK JP 等をインストールすること）')


# ---- 色（基本フォームの配色） -------------------------------------------
BLACK = '#111111'
GRAY = '#8a8a8a'
RED = '#d62728'
BLUE = '#1f77b4'
ORANGE = '#ff7f0e'
GREEN = '#2ca02c'
PURPLE = '#9467bd'
FILL_ALPHA = 0.22


def xy(p):
    """(X, Y) の点を作図用の (横, 縦) = (Y, X) にする。p は複素数 X+Yi またはタプル。"""
    if isinstance(p, complex):
        return (p.imag, p.real)
    return (p[1], p[0])


class Zu:
    """1枚の図（または1つのパネル）を描くためのクラス。文字は台帳に登録して重なり検査に使う。"""

    def __init__(self, ax, fontsize=15):
        self.ax = ax
        self.fs = fontsize
        self.labels = []      # 重なり検査の対象の文字
        self.segments = []    # 重なり検査の対象の線分（データ座標）
        self.markers = []     # 点（データ座標）
        self.polys = []       # 区画（方位記号を区画の中に置かないための判定用）
        # 縦横の縮尺は同じ。adjustable='datalim' で、パネルの枠いっぱいまで表示範囲を広げる（文字を置く余白を確保する）
        ax.set_aspect('equal', adjustable='datalim')
        ax.axis('off')

    # ---- 線・面 ---------------------------------------------------------
    def poly(self, pts, color=BLACK, lw=2.0, fill=None, alpha=FILL_ALPHA, ls='-', closed=True, zorder=2,
             check=True):
        v = [xy(p) for p in pts]
        if closed and len(v) >= 3:
            self.polys.append(v)
        if fill:
            self.ax.add_patch(Polygon(v, closed=True, facecolor=fill, alpha=alpha, edgecolor='none', zorder=1))
        vv = v + [v[0]] if closed else v
        self.ax.plot([a for a, _ in vv], [b for _, b in vv], color=color, lw=lw, ls=ls, zorder=zorder,
                     solid_capstyle='round')
        if check:
            for i in range(len(vv) - 1):
                self.segments.append((vv[i], vv[i + 1]))

    def line(self, p, q, color=BLACK, lw=2.0, ls='-', zorder=2, check=True):
        self.poly([p, q], color=color, lw=lw, ls=ls, closed=False, zorder=zorder, check=check)

    def point(self, p, kind='dot', size=7, color=BLACK):
        """点の記号。kind: dot（黒丸）/ concrete（白抜き丸に中黒＝コンクリート杭）/ metal（黒丸＝金属標）
        / kijun（三角＝基準点）/ stone（白抜きの四角＝石杭。2026-09-29、H25/Q21で追加）"""
        a, b = xy(p)
        if kind == 'stone':
            self.ax.plot(a, b, 's', ms=size + 3, mfc='white', mec=color, mew=1.6, zorder=5)
        elif kind == 'concrete':
            self.ax.plot(a, b, 'o', ms=size + 4, mfc='white', mec=color, mew=1.6, zorder=5)
            self.ax.plot(a, b, 'o', ms=2.6, color=color, zorder=6)
        elif kind == 'kijun':
            self.ax.plot(a, b, '^', ms=size + 5, mfc='white', mec=color, mew=1.6, zorder=5)
            self.ax.plot(a, b, 'o', ms=2.2, color=color, zorder=6)
        else:
            self.ax.plot(a, b, 'o', ms=size, color=color, zorder=5)
        self.markers.append((a, b))

    # ---- 文字（候補位置を試して重ならない位置に置く） -----------------
    def _try_place(self, make_candidates):
        """候補の文字を順に作り、既存の文字・線・点に重ならない最初の候補を採用する。
        全部重なる場合は、重なりが最小の候補を採用して警告を残す。"""
        fig = self.ax.figure
        best, best_score = None, None
        for t in make_candidates():
            fig.canvas.draw()
            score = self._overlap_score(t)
            if score == 0:
                if best is not None:
                    best.remove()
                self.labels.append(t)
                return t
            if best_score is None or score < best_score:
                if best is not None:
                    best.remove()
                best, best_score = t, score
            else:
                t.remove()
        self.labels.append(best)
        print(f'  [警告] 重ならない位置が見つからない文字: {best.get_text()!r}（重なり {best_score}）')
        return best

    def edge_label(self, p, q, text, inside_ref, color=BLACK, fs=None, dists=(9, 15, 22),
                   ts=(0.5, 0.38, 0.62, 0.28, 0.72), outward=True, rotate=True):
        """辺pqの長さなどを、辺と平行に、図形の外側（inside_ref の反対側）に置く。
        inside_ref: 図形の内側の代表点（重心など）。outward=False なら内側に置く。"""
        fs = fs or self.fs
        (x1, y1), (x2, y2) = xy(p), xy(q)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if ang > 90:
            ang -= 180
        if ang <= -90:
            ang += 180
        dx, dy = x2 - x1, y2 - y1
        n = math.hypot(dx, dy)
        nx, ny = -dy / n, dx / n
        cx, cy = xy(inside_ref)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if (cx - mx) * nx + (cy - my) * ny > 0:   # 法線が内側を向いていたら反転
            nx, ny = -nx, -ny
        if not outward:
            nx, ny = -nx, -ny
        rot = ang if rotate else 0   # 隣接地番・道路などの文字は rotate=False で水平に書く

        def cands():
            for d in dists:
                for t in ts:
                    px, py = x1 + dx * t, y1 + dy * t
                    yield self.ax.annotate(text, (px, py), xytext=(nx * d, ny * d), textcoords='offset points', annotation_clip=False,
                                           ha='center', va='center', rotation=rot, rotation_mode='anchor',
                                           fontsize=fs, color=color, zorder=8)
        return self._try_place(cands)

    def point_label(self, p, text, away=None, color=BLACK, fs=None, dists=(13, 19, 26), weight='bold'):
        """点名。away（図形の内側の代表点）から離れる向きを第一候補に、8方向を試す。"""
        fs = fs or self.fs
        a, b = xy(p)
        if away is not None:
            ca, cb = xy(away)
            base = math.atan2(b - cb, a - ca)
        else:
            base = math.radians(45)
        angs = [base + math.radians(k) for k in (0, 35, -35, 70, -70, 110, -110, 180)]

        def cands():
            for d in dists:
                for th in angs:
                    yield self.ax.annotate(text, (a, b), xytext=(math.cos(th) * d, math.sin(th) * d),
                                           textcoords='offset points', annotation_clip=False, ha='center', va='center',
                                           fontsize=fs, color=color, weight=weight, zorder=8)
        return self._try_place(cands)

    def callout(self, p, text, dirs, color=BLACK, fs=None, dists=(55, 75, 95, 120), box_color='white'):
        """座標値などの吹き出し。引き出し線付きで、dirs（度。0＝東、90＝北）の方向の余白へ置く。"""
        fs = fs or self.fs - 1
        a, b = xy(p)

        def cands():
            for d in dists:
                for deg in dirs:
                    th = math.radians(deg)
                    c, s_ = math.cos(th), math.sin(th)
                    # 吹き出しの箱は、引き出し線の反対側に寄せる（箱が点や線にかぶって引き出し線が隠れないように）
                    ha = 'left' if c > 0.35 else ('right' if c < -0.35 else 'center')
                    va = 'bottom' if s_ > 0.35 else ('top' if s_ < -0.35 else 'center')
                    yield self.ax.annotate(
                        text, (a, b), xytext=(c * d, s_ * d), textcoords='offset points', annotation_clip=False,
                        ha=ha, va=va, fontsize=fs, color=color, zorder=9,
                        bbox=dict(boxstyle='round,pad=0.3', fc=box_color, ec=color, lw=1.0),
                        arrowprops=dict(arrowstyle='-', color=color, lw=0.9, shrinkA=0, shrinkB=4))
        return self._try_place(cands)

    def free_text(self, p, text, color=BLACK, fs=None, ha='center', va='center', offsets=((0, 0),), **kw):
        """区画名・面積などの文字（データ座標の位置 p を基準に、offsets〈pt〉の候補を試す）。"""
        fs = fs or self.fs
        a, b = xy(p)

        def cands():
            for ox, oy in offsets:
                yield self.ax.annotate(text, (a, b), xytext=(ox, oy), textcoords='offset points', annotation_clip=False, ha=ha, va=va,
                                       fontsize=fs, color=color, zorder=8, **kw)
        return self._try_place(cands)

    # ---- 記号 -----------------------------------------------------------
    def angle_arc(self, center, r, bearing_from, bearing_to, color=BLACK, lw=1.4, ls='-', arrow=True, check=True):
        """方向角（北から時計回り）の弧。bearing_from から bearing_to へ時計回りに描く。
        check=True なら、弧を細かい線分に分けて重なり検査の対象に登録する（2026-09-29、R6/Q21で追加。
        登録しないと、座標値の吹き出しが弧の上に置かれても検査で見つからなかった）。"""
        a, b = xy(center)
        th2 = 90 - bearing_from
        th1 = 90 - bearing_to
        self.ax.add_patch(Arc((a, b), 2 * r, 2 * r, theta1=th1, theta2=th2, color=color, lw=lw, ls=ls, zorder=3))
        if check:
            n = max(8, int(abs(th2 - th1) / 6))
            pts = [(a + r * math.cos(math.radians(th1 + (th2 - th1) * k / n)),
                    b + r * math.sin(math.radians(th1 + (th2 - th1) * k / n))) for k in range(n + 1)]
            self.segments += list(zip(pts[:-1], pts[1:]))
        if arrow:
            end = math.radians(th1)
            ex, ey = a + r * math.cos(end), b + r * math.sin(end)
            tx, ty = math.sin(end), -math.cos(end)   # 時計回りの接線
            self.ax.annotate('', (ex, ey), xytext=(ex - tx * r * 0.08, ey - ty * r * 0.08),
                             arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, mutation_scale=14), zorder=3)

    def right_angle(self, foot, along, toward, size=0.8, color=GRAY):
        """直角の記号。foot：垂線の足、along：足を通る直線上の別の点、toward：垂線のもう一方の端。"""
        f = complex(*xy(foot))
        u = complex(*xy(along)) - f
        v = complex(*xy(toward)) - f
        u, v = u / abs(u) * size, v / abs(v) * size
        pts = [f + u, f + u + v, f + v]
        self.ax.plot([z.real for z in pts], [z.imag for z in pts], color=color, lw=1.2, zorder=3)

    def parallel_marks(self, p, q, n=1, color=BLACK, size=16):
        """平行の記号（辺の中央に「＞」をn個、pからqの向き）。"""
        (x1, y1), (x2, y2) = xy(p), xy(q)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        s = '>' * n
        self.ax.annotate(s, (mx, my), ha='center', va='center', rotation=ang, rotation_mode='anchor',
                         fontsize=size, color=color, weight='bold', zorder=7)

    def parallel_chevron(self, p, q, color=BLACK, size=0.45, lw=2.0):
        """平行の記号を線で描く（辺の中央に「＞」の形の折れ線を、pからqの向きで。size はデータ座標の長さ）。
        文字の「>」を45°前後に回転させると字形が崩れて「⊥」のように見えるので（2026-09-29、R2/Q21）、
        斜めの辺ではこちらを使う。"""
        (x1, y1), (x2, y2) = xy(p), xy(q)
        u = complex(x2 - x1, y2 - y1)
        u = u / abs(u)
        m = complex((x1 + x2) / 2, (y1 + y2) / 2)
        tip = m + u * size / 2
        for s in (1, -1):
            tail = tip - u * size + u * 1j * s * size * 0.6
            self.ax.plot([tail.real, tip.real], [tail.imag, tip.imag], color=color, lw=lw, zorder=7)

    def north_arrow(self, pos=None, length=0.10):
        """方位記号（真上＝X軸の正の方向＝北）。図形の線に重ならず区画の外にある位置を自動で選ぶ（右上→左上→右下→左下の隅、なければ余白を上から探す）。
        他の文字より先に描き、「N」の文字と矢印を重なり検査の対象に登録する。表示範囲を決めた（fit）直後に呼ぶこと。"""
        ax = self.ax
        fig = ax.figure
        fig.canvas.draw()
        to_data = (ax.transAxes + ax.transData.inverted()).transform
        corners = [(0.93, 0.80), (0.07, 0.80), (0.93, 0.08), (0.07, 0.08)]
        grid = [(gx / 100, gy / 100) for gy in range(80, 4, -6) for gx in range(95, 4, -5)]
        cands = [pos] if pos else corners + grid
        for x, y in cands:
            seg = (tuple(to_data((x, y))), tuple(to_data((x, y + length))))
            bb = Bbox.from_extents(*(ax.transAxes.transform((x - 0.03, y - 0.01))),
                                   *(ax.transAxes.transform((x + 0.03, y + length + 0.07))))
            mid = to_data((x, y + length / 2))
            inside = any(_point_in_poly(mid, pg) for pg in self.polys)
            if not inside and not any(_seg_hits_bbox(a, b, bb) for a, b in self._seg_disp()):
                break
        else:
            print('  [警告] 方位記号を置く空きがない。pos を指定すること')
        ax.annotate('', xy=(x, y + length), xytext=(x, y), xycoords='axes fraction',
                    arrowprops=dict(arrowstyle='-|>', lw=2.2, color=BLACK, mutation_scale=22))
        t = ax.text(x, y + length + 0.02, 'N', transform=ax.transAxes, ha='center', va='bottom',
                    fontsize=self.fs + 3, weight='bold')
        self.labels.append(t)
        self.segments.append(seg)

    # ---- 重なり検査 -----------------------------------------------------
    PAD = 4.0   # 文字の周りに確保する余白（px）。線・点・他の文字に「触れているだけ」も重なりとみなす

    def _bbox(self, t, pad=None):
        pad = self.PAD if pad is None else pad
        # Annotation.get_window_extent は引き出し線まで含むので、文字の部分（Text）だけの範囲を使う
        bb = Text.get_window_extent(t, self.ax.figure.canvas.get_renderer())
        return Bbox.from_extents(bb.x0 - pad, bb.y0 - pad, bb.x1 + pad, bb.y1 + pad)

    def _seg_hits_text(self, a, b, t):
        """線分abが文字tに重なるか。回転した文字は、外接矩形ではなく回転した長方形そのもので判定する
        （外接矩形だと斜めの辺長ラベルで誤検出が出る）。"""
        rot = t.get_rotation()
        if abs(rot) < 1e-6:
            return _seg_hits_bbox(a, b, self._bbox(t))
        r = self.ax.figure.canvas.get_renderer()
        t.set_rotation(0)
        bb0 = Text.get_window_extent(t, r)
        t.set_rotation(rot)
        w, h = bb0.width / 2 + self.PAD, bb0.height / 2 + self.PAD
        cb = Text.get_window_extent(t, r)
        cx, cy = (cb.x0 + cb.x1) / 2, (cb.y0 + cb.y1) / 2
        th = -math.radians(rot)
        def loc(p):   # 文字の中心・向きを基準にした座標へ
            dx, dy = p[0] - cx, p[1] - cy
            return (dx * math.cos(th) - dy * math.sin(th), dx * math.sin(th) + dy * math.cos(th))
        return _seg_hits_bbox(loc(a), loc(b), Bbox.from_extents(-w, -h, w, h))

    def _seg_disp(self):
        tr = self.ax.transData
        return [(tr.transform(a), tr.transform(b)) for a, b in self.segments]

    def _overlap_score(self, t):
        bb = self._bbox(t)
        score = 0
        for o in self.labels:
            if o is t:
                continue
            if bb.overlaps(self._bbox(o)):
                score += 3
        for a, b in self._seg_disp():
            if self._seg_hits_text(a, b, t):
                score += 2
        tr = self.ax.transData
        for m in self.markers:
            mx, my = tr.transform(m)
            if bb.x0 - 3 < mx < bb.x1 + 3 and bb.y0 - 3 < my < bb.y1 + 3:
                score += 2
        fb = self.ax.figure.bbox
        if bb.x0 < fb.x0 or bb.y0 < fb.y0 or bb.x1 > fb.x1 or bb.y1 > fb.y1:
            score += 5
        ab = self.ax.get_window_extent()
        if bb.x0 < ab.x0 or bb.y0 < ab.y0 or bb.x1 > ab.x1 or bb.y1 > ab.y1:
            score += 1   # 軸（パネル）の外。隣のパネル・タイトル・説明文と重なりうる
        return score

    def check_overlaps(self, name=''):
        """描画後の最終検査。重なりの一覧を返す（空なら合格）。"""
        self.ax.figure.canvas.draw()
        problems = []
        for i, t in enumerate(self.labels):
            bb = self._bbox(t)
            for o in self.labels[i + 1:]:
                if bb.overlaps(self._bbox(o)):
                    problems.append(f'文字どうし: {t.get_text()!r} と {o.get_text()!r}')
            for a, b in self._seg_disp():
                if self._seg_hits_text(a, b, t):
                    problems.append(f'文字と線: {t.get_text()!r}')
                    break
            ab = self.ax.get_window_extent()
            if bb.x0 < ab.x0 or bb.y0 < ab.y0 or bb.x1 > ab.x1 or bb.y1 > ab.y1:
                problems.append(f'作図範囲からのはみ出し: {t.get_text()!r}')
            tr = self.ax.transData
            for m in self.markers:
                mx, my = tr.transform(m)
                if bb.x0 - 3 < mx < bb.x1 + 3 and bb.y0 - 3 < my < bb.y1 + 3:
                    problems.append(f'文字と点: {t.get_text()!r}')
                    break
        print(f'[重なり検査] {name}: ' + ('問題なし' if not problems else f'{len(problems)}件'))
        for p in problems:
            print('   ', p)
        return problems


def _point_in_poly(pt, poly):
    """点が多角形の内側にあるか（交差数判定）。"""
    x, y = pt
    inside = False
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            inside = not inside
    return inside


def _seg_hits_bbox(a, b, bb):
    """線分abが矩形bbに入る・横切るか（Liang–Barsky）。"""
    x0, y0 = a
    x1, y1 = b
    dx, dy = x1 - x0, y1 - y0
    p = [-dx, dx, -dy, dy]
    q = [x0 - bb.x0, bb.x1 - x0, y0 - bb.y0, bb.y1 - y0]
    u1, u2 = 0.0, 1.0
    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return False
        else:
            t = qi / pi
            if pi < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)
    return u1 <= u2


def new_figure(title, caption, w=16, h=12, dpi=100, ncols=1, width_ratios=None):
    """横1600×縦1200px（既定）の白背景の図。上にタイトル、下に説明文。"""
    setup_font()
    fig, axes = plt.subplots(1, ncols, figsize=(w, h), dpi=dpi,
                             gridspec_kw={'width_ratios': width_ratios} if width_ratios else None)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.975)
    fig.text(0.5, 0.03, caption, ha='center', va='bottom', fontsize=16, wrap=True)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.90, bottom=0.12, wspace=0.08)
    return fig, (axes if ncols > 1 else [axes])


def fit(ax, pts, margin=0.12, extra=None, pad_aspect=False):
    """表示範囲を点の集合に合わせる（縦横同じ縮尺のまま、余白 margin の割合）。
    pad_aspect=True なら、パネルの縦横比に合わせて範囲を広げてから設定する（図形の端が切れるのを防ぐ）。"""
    v = [xy(p) for p in pts] + (extra or [])
    xs, ys = [a for a, _ in v], [b for _, b in v]
    w, h = max(xs) - min(xs), max(ys) - min(ys)
    x0, x1 = min(xs) - w * margin, max(xs) + w * margin
    y0, y1 = min(ys) - h * margin, max(ys) + h * margin
    # パネルの縦横比に合わせて、足りない方向の範囲を中央から広げる（2026-09-29追加、R2/Q21）。
    # 広げないと、adjustable='datalim' が縦横比を合わせるときに範囲を縮めることがあり、
    # 図形の端（R2/Q21の図7ではB点と基準点1）がパネルの外に切れてしまう。
    # 既存の年度（R7/Q21）の図の配置を変えないよう、新しい年度から pad_aspect=True で使う。
    if not pad_aspect:
        ax.set_xlim(x0, x1)
        ax.set_ylim(y0, y1)
        return
    fig = ax.figure
    pos = ax.get_position()
    fw, fh = fig.get_size_inches()
    ratio = (pos.height * fh) / (pos.width * fw)   # パネルの 縦 ÷ 横
    dw, dh = x1 - x0, y1 - y0
    if dh / dw < ratio:
        pad = (dw * ratio - dh) / 2
        y0, y1 = y0 - pad, y1 + pad
    else:
        pad = (dh / ratio - dw) / 2
        x0, x1 = x0 - pad, x1 + pad
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)


def centroid(pts):
    """多角形の重心（内側の代表点として使う）。"""
    v = [xy(p) for p in pts]
    a = cx = cy = 0.0
    for i in range(len(v)):
        x0, y0 = v[i]
        x1, y1 = v[(i + 1) % len(v)]
        c = x0 * y1 - x1 * y0
        a += c
        cx += (x0 + x1) * c
        cy += (y0 + y1) * c
    a /= 2
    return complex(cy / (6 * a), cx / (6 * a))   # (X, Y) に戻す
