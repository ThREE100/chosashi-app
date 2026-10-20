"""令和8年度 第21問（土地）計算過程の動画用素材（段階ごとのコマ・絵コンテ・試作の動画）を作る。

記事 `../note_R8_dai21mon_tochi_kaiwa_kaisetsu.md` の計算（点の座標・面積・辺長）を、1つの計算につき1本の動画にする。
1本の動画は、記事の「式・電卓操作・表示」の3点セットを細かい段階（ステップ）に分けたコマの連続で、
コマ k にはステップ1〜k の要素が積み上がる（前のステップの要素は灰色、いま説明しているステップの要素は赤）。

出力（このフォルダ）
- `D01_C_housha/step01.png …`：コマ（横1280×縦720、16:9）。動画編集ソフトにそのまま並べられる
- `D01_C_housha.mp4 …`：コマを絵コンテの秒数で並べた試作の動画（H.264、音声なし）
- `kontei_R8_dai21mon_douga.md`：絵コンテ（動画ごと・ステップごとの画面・ナレーション案・秒数・記事の位置）

文字の位置がコマごとに動かない（ちらつかない）ように、最初に全ステップを描いて文字の位置を自動で決め（重なりの自動検査つき）、
その位置を記録して各コマで同じ位置に描く。数値はすべて座標から計算し直し、記事の表示と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R8/Q21/douga/make_R8_dai21mon_douga.py [--no-video]
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, area, chiseki, radial, dms, disp, fmt_num, intersect, to_dms  # noqa: E402
from zu_helpers import Zu, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN, xy  # noqa: E402
import cmath  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc, FancyBboxPatch  # noqa: E402

plt.rcParams['figure.max_open_warning'] = 0
MAKE_VIDEO = '--no-video' not in sys.argv
W, H, DPI = 12.8, 7.2, 100
LIGHT = '#b5b5b5'

# ---- 座標（記事と同じ） --------------------------------------------------
T1, T2 = P(481.86, 471.43), P(481.75, 506.66)
A, B, D, E, F = P(484.35, 505.19), P(486.05, 505.19), P(510.78, 490.69), P(509.94, 475.79), P(486.05, 474.32)
Hp, I, J, M = P(486.05, 488.12), P(498.53, 494.70), P(510.78, 492.46), P(486.05, 491.31)
Craw = radial(T2, T1, 29.03, dms(90, 4, 40))
C = r2(Craw)
Cw = r2(radial(T2, T1, 29.03, -dms(90, 4, 40)))
Lraw = Hp + (I - Hp) * 6.05 / 12.48
L = r2(Lraw)
Lw = r2(Hp + (I - Hp) / abs(I - Hp) * 6.05)
num = (D - J).conjugate() * (I - D)
den = (L - J).conjugate() * (I - D)
Kraw = J + (L - J) * 21.6825 / 88.9943
K = r2(Kraw)
Kw = r2(D + (I - D) * (492.46 - D.imag) / (I - D).imag)
for got, want in [(C, P(510.78, 506.79)), (L, P(492.10, 491.31)), (K, P(506.23, 492.18)), (Cw, P(452.72, 506.61)),
                  (Lw, P(491.40, 490.94)), (Kw, P(505.37, 492.46))]:
    assert abs(got - want) < 1e-9, (got, want)
assert disp(Craw) == '510.7797… ＋ 506.7900…i' and disp(Lraw) == '492.10 ＋ 491.3098…i'
assert disp(num) == '−7.0977 − 21.6825i' and disp(den) == '224.2185 − 88.9943i' and disp(Kraw) == '506.2288… ＋ 492.1798…i'
KOU, RO, KOU1 = [E, D, I, Hp, F], [I, K, L], [E, D, K, L, Hp, F]
OTSU, URI, S58, S59 = [D, C, B, Hp, I], [J, C, B, M, L, K], [Hp, L, M], [D, J, K]
NAMES = {E: 'E', D: 'D', I: 'I', Hp: 'H', F: 'F', K: 'K', L: 'L', J: 'J', C: 'C', B: 'B', M: 'M'}


def terms(pts):
    """座標法の各項 P・Conjg(Q) の iの係数（記事の電卓と同じ順）"""
    return [(pts[i] * pts[(i + 1) % len(pts)].conjugate()).imag for i in range(len(pts))]


def f4(v):
    return fmt_num(v)


# ---- 1コマを描く仕組み ----------------------------------------------------
class Scene:
    """1コマ。layout=True のときは文字の位置を自動で決めて記録し、False のときは記録どおりに描く。"""

    def __init__(self, anim, k, layout, rec):
        setup_font()
        self.anim, self.k, self.layout, self.rec, self.n = anim, k, layout, rec, 0
        self.fig = plt.figure(figsize=(W, H), dpi=DPI)
        self.fig.patch.set_facecolor('white')
        self.ax = self.fig.add_axes([0.015, 0.05, 0.56, 0.80])
        self.z = Zu(self.ax, fontsize=13)
        x0, x1, y0, y1 = anim['view']
        self.ax.set_xlim(x0, x1)
        self.ax.set_ylim(y0, y1)
        self.ax.set_aspect('equal', adjustable='box')
        self.cur = False
        self.step = 0

    def col(self, base=BLACK):
        return RED if self.cur else (base if base != BLACK else '#555555')

    # 図形（重なり検査に登録される）
    def poly(self, pts, fill=None, color=None, lw=2.0, ls='-', closed=True, alpha=0.18):
        self.z.poly(pts, color=color or self.col(), lw=lw, ls=ls, closed=closed, fill=fill, alpha=alpha)

    def line(self, p, q, color=None, lw=2.0, ls='-'):
        self.z.line(p, q, color=color or self.col(), lw=lw, ls=ls)

    def dot(self, p, kind='dot', color=None):
        self.z.point(p, kind, color=color or self.col())

    # 文字（位置を記録・再現する）
    def _text(self, make, color, **style):
        key = (self.step, self.n)
        self.n += 1
        if self.layout:
            t = make()
            self.rec[key] = dict(xy=t.xy, xyann=t.xyann, ha=t.get_ha(), va=t.get_va(), rot=t.get_rotation(),
                                 fs=t.get_fontsize(), box=t.get_bbox_patch() is not None, arrow=t.arrow_patch is not None,
                                 weight=t.get_weight(), text=t.get_text())
            t.set_color(color)
            if t.get_bbox_patch() is not None:
                t.get_bbox_patch().set_edgecolor(color)
            return t
        r = self.rec[key]
        kw = dict(xytext=r['xyann'], textcoords='offset points', annotation_clip=False, ha=r['ha'], va=r['va'],
                  rotation=r['rot'], rotation_mode='anchor', fontsize=r['fs'], color=color, weight=r['weight'], zorder=9)
        if r['box']:
            kw['bbox'] = dict(boxstyle='round,pad=0.3', fc='white', ec=color, lw=1.0)
        if r['arrow']:
            kw['arrowprops'] = dict(arrowstyle='-', color=color, lw=0.9, shrinkA=0, shrinkB=4)
        t = self.ax.annotate(r['text'], r['xy'], **kw)
        self.z.labels.append(t)
        return t

    def name(self, p, text, away, color=None):
        c = color or self.col()
        return self._text(lambda: self.z.point_label(p, text, away=away, color=c), c)

    def callout(self, p, text, dirs, color=None, dists=(55, 75, 95, 120), fs=12):
        c = color or self.col()
        return self._text(lambda: self.z.callout(p, text, dirs=dirs, color=c, dists=dists, fs=fs), c)

    def edge(self, p, q, text, inside, color=None, fs=12, outward=True):
        c = color or self.col()
        return self._text(lambda: self.z.edge_label(p, q, text, inside, color=c, fs=fs, outward=outward), c)

    def free(self, p, text, color=None, fs=13, offsets=((0, 0),)):
        c = color or self.col()
        return self._text(lambda: self.z.free_text(p, text, color=c, fs=fs, offsets=offsets), c)

    def arc(self, center, r, b_from, b_to, color=None):
        a, b = xy(center)
        c = color or self.col()
        self.ax.add_patch(Arc((a, b), 2 * r, 2 * r, theta1=90 - b_to, theta2=90 - b_from, color=c, lw=1.8, zorder=3))

    def finish(self, path):
        """右の説明パネル（ステップの一覧と、いまのステップの式・電卓・表示）とタイトルを描いて保存する。"""
        a, k = self.anim, self.k
        f = self.fig
        f.text(0.015, 0.95, a['title'], fontsize=19, weight='bold', va='center')
        f.text(0.985, 0.95, f'ステップ {k}／{len(a["steps"])}', fontsize=14, ha='right', va='center', color=GRAY)
        f.add_artist(FancyBboxPatch((0.59, 0.05), 0.395, 0.82, boxstyle='round,pad=0.005', transform=f.transFigure,
                                    fc='#f7f7f7', ec='#cccccc', lw=1.2))
        y = 0.84
        for j, st in enumerate(a['steps'][:k], 1):
            if j < k:
                f.text(0.605, y, f'{j}. {st["short"]}', fontsize=11.5, color=GRAY, va='top')
                y -= 0.038
        f.text(0.605, y - 0.01, f'{k}. {a["steps"][k - 1]["short"]}', fontsize=14, color=RED, weight='bold', va='top')
        y -= 0.065
        for ln in a['steps'][k - 1]['lines']:
            big = ln.startswith('表示：') or ln.startswith('▶')
            f.text(0.612, y, ln, fontsize=(13.5 if big else 12.5), color=(BLUE if big else BLACK),
                   weight=('bold' if big else 'normal'), va='top')
            y -= 0.048
        assert y > 0.06, (a['id'], k, '説明パネルからはみ出す')
        f.savefig(path, dpi=DPI, facecolor='white')
        plt.close(f)


def render(anim, outdir):
    """layout パス（全ステップ）で文字の位置を決めて重なりを検査し、その位置で各コマを描く。"""
    rec = {}
    sc = Scene(anim, len(anim['steps']), True, rec)
    anim['base'](sc)
    for i, st in enumerate(anim['steps'], 1):
        sc.step, sc.n, sc.cur = i, 0, (i == len(anim['steps']))
        st['draw'](sc)
    probs = sc.z.check_overlaps(anim['id'] + '（全ステップを重ねた最後のコマ）')
    plt.close(sc.fig)
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir)
    for k in range(1, len(anim['steps']) + 1):
        sc = Scene(anim, k, False, rec)
        anim['base'](sc)
        for i, st in enumerate(anim['steps'][:k], 1):
            sc.step, sc.n, sc.cur = i, 0, (i == k)
            st['draw'](sc)
        sc.finish(os.path.join(outdir, f'step{k:02d}.png'))
    return probs


def view(pts, margin=0.12, ratio=0.80 * H / (0.56 * W)):
    """縦横同じ縮尺で、点が全部入る表示範囲（横＝Y、縦＝X）。"""
    ys, xs = [p.imag for p in pts], [p.real for p in pts]
    x0, x1, y0, y1 = min(ys), max(ys), min(xs), max(xs)
    w, h = (x1 - x0) * (1 + 2 * margin), (y1 - y0) * (1 + 2 * margin)
    if h / w < ratio:
        h = w * ratio
    else:
        w = h / ratio
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2)


def S(short, lines, sec, narr, draw):
    return dict(short=short, lines=lines, sec=sec, narr=narr, draw=draw)


def nothing(sc):
    pass


ANIMS = []

# =====================================================================
# D01：問4 C点（放射）
# =====================================================================
ctr = (D + C + B + Hp) / 4
ANIMS.append(dict(
    id='D01_C_housha', title='問4　C点を放射で求める（T2からT1を後視、時計回りに足す）', article='第7章',
    view=view([T1, T2, C, Cw, D], margin=0.06),
    base=lambda sc: sc.poly(OTSU, color=LIGHT, lw=1.0, fill='#dbe8f5', alpha=0.5),
    steps=[
        S('既知点T1・T2を置く', ['M市基準点成果表', 'T1（481.86, 471.43）', 'T2（481.75, 506.66）', '電卓：E＝T1、Y＝T2'], 6,
          'まずM市基準点のT1とT2を座標どおりに置きます。電卓ではT1をE、T2をYに記憶します。',
          lambda sc: (sc.dot(T1, 'kijun'), sc.dot(T2, 'kijun'), sc.name(T1, 'T1', ctr), sc.name(T2, 'T2', T2 - P(0, 5)))),
        S('T2からT1を見る向き（後視）', ['器械点T2、後視点T1', 'arg(T1 − T2) ＝ −89°49′15.97″', '（真西よりわずかに北）'], 7,
          'T2に器械を据えてT1を後視します。T2からT1を見た向きは、マイナス89度49分15.97秒です。',
          lambda sc: (sc.line(T2, T1, ls='--'),)),
        S('観測角を時計回りに足す', ['観測角 90°04′40″', '−89°49′15.97″ ＋ 90°04′40″', '＝ 0°15′24.03″（ほぼ真北）'], 8,
          '観測角の90度04分40秒を時計回りに足します。向きの注がない年度は時計回りとして扱います。0度15分24秒で、ほぼ真北です。',
          lambda sc: (sc.arc(T2, 4.0, 270 + 10 / 60 + 44.03 / 3600, 360 + 15 / 60 + 24.03 / 3600),
                      sc.callout(T2 + P(3.0, 2.5), '90°04′40″', dirs=(0, 30, -30), fs=12))),
        S('その向きに29.03m進む', ['C ＝ T2 ＋ 29.03∠(arg(T1 − T2) ＋ 90°04′40″)',
                                   '[ALPHA] [Y] [+] 29.03 [∠] [(] [Apps] [3] …', '表示：510.7797… ＋ 506.7900…i'], 9,
          'その向きに水平距離29.03メートル進んだ点がCです。電卓の表示は510.7797と506.7900です。',
          lambda sc: (sc.line(T2, C, lw=2.4), sc.edge(T2, C, '29.03', ctr, outward=False))),
        S('小数第3位を四捨五入', ['問題文の注3', '▶ C点（510.78, 506.79）'], 6,
          '問題文の注3で小数第3位を四捨五入して、C点は510.78、506.79です。',
          lambda sc: (sc.dot(C, 'concrete'), sc.callout(C, 'C（510.78, 506.79）', dirs=(-30, 0, -60), fs=12))),
        S('検算：D・J・Cは一直線', ['D（510.78, 490.69）・J（510.78, 492.46）', 'CもX＝510.78', '→ 調査図素図の注3と合う'], 7,
          'D点・J点とX座標が同じ510.78です。調査図素図の注3の「CからDは直線、Jはその上」と合うので、放射の検算になります。',
          lambda sc: (sc.dot(D), sc.dot(J), sc.name(D, 'D', ctr), sc.name(J, 'J', ctr), sc.line(D, C, ls=':', lw=1.6))),
        S('誤り：反時計回りに引くと', ['−89°49′15.97″ − 90°04′40″', '→（452.72, 506.61）', 'T2より29m南、市道の向こう'], 7,
          '反対に引いてしまうと、T2から29メートル南の市道の向こうに出てしまいます。これが誤りの形です。',
          lambda sc: (sc.line(T2, Cw, ls=':', lw=1.6), sc.dot(Cw),
                      sc.callout(Cw, '誤り（452.72, 506.61）', dirs=(180, 160, -160), fs=12))),
    ]))

# =====================================================================
# D02：問2の前提 L点
# =====================================================================
ctr2 = (D + Hp + I) / 3 + P(0, -3)
ANIMS.append(dict(
    id='D02_L_ten', title='問2の前提　L点（MからX軸方向に6.05m、HI上の点）', article='第3章',
    view=view([Hp, I, M, L, Lw, P(499.5, 487.0)], margin=0.10),
    base=nothing,
    steps=[
        S('H・I・Mを置く', ['H（486.05, 488.12）', 'I（498.53, 494.70）', 'M（486.05, 491.31）', '電卓：A＝H、C＝I'], 6,
          'H点・I点・M点を置きます。LはHとIを結ぶ直線の上にあります（調査図素図の注5）。',
          lambda sc: (sc.line(Hp, I, lw=2.0), sc.dot(Hp, 'concrete'), sc.dot(I, 'concrete'), sc.dot(M, 'concrete'),
                      sc.name(Hp, 'H', ctr2), sc.name(I, 'I', ctr2), sc.name(M, 'M', ctr2))),
        S('X軸方向は北', ['MからX軸方向に6.05m', 'LのX座標 ＝ 486.05 ＋ 6.05', '＝ 492.10'], 7,
          'X軸方向は北です。MからX軸方向に6.05メートルなので、LのX座標は486.05足す6.05で492.10です。',
          lambda sc: (sc.line(P(492.10, 487.6), P(492.10, 495.2), ls='--', lw=1.5),
                      sc.callout(P(492.10, 487.8), 'X＝492.10の線', dirs=(100, 120, 80), dists=(40, 55, 70), fs=12))),
        S('HからIへ進む割合', ['HからIへ X は', '498.53 − 486.05 ＝ 12.48 増える', '6.05だけ増やす → 6.05 ÷ 12.48'], 7,
          'HからIへ進むとX座標は12.48増えます。6.05だけ増やせばよいので、12.48分の6.05だけ進んだ点です。',
          lambda sc: (sc.callout(Hp + (I - Hp) * 0.8, '12.48 増える', dirs=(0, -20, 20), dists=(40, 55, 70), fs=12),)),
        S('L ＝ H ＋ (I − H) × 6.05 ÷ 12.48', ['[ALPHA] [A] [+] [(] [ALPHA] [C] [−]', '[ALPHA] [A] [)] [×] 6.05 [÷] 12.48 [=]',
                                              '表示：492.10 ＋ 491.3098…i'], 8,
          'H足すIマイナスHかける6.05割る12.48。表示は492.10と491.3098です。',
          lambda sc: (sc.dot(L),)),
        S('四捨五入：Mの真北', ['▶ L点（492.10, 491.31）', 'Y座標がMと同じ491.31', '→ LMは真北向きの6.05'], 7,
          '四捨五入してL点は492.10、491.31。Y座標がM点と同じなので、LはMの真北にあり、LMは6.05です。',
          lambda sc: (sc.line(M, L, lw=2.4), sc.edge(M, L, '6.05', I),
                      sc.callout(L, 'L（492.10, 491.31）', dirs=(0, 20, -20), fs=12))),
        S('誤り：Hから斜めに6.05m', ['H ＋ (I − H) ÷ Abs(I − H) × 6.05', '→（491.40, 490.94）', 'Mの真北にならない'], 7,
          'Hから斜めに6.05メートル測ると491.40、490.94になり、Mの真北に来ません。これが誤りです。',
          lambda sc: (sc.dot(Lw), sc.callout(Lw, '誤り（491.40, 490.94）', dirs=(-160, 180, -140), fs=12))),
    ]))

# =====================================================================
# D03：問2 K点（交点）
# =====================================================================
ctr3 = (D + I + L) / 3 + P(0, -3)
t_val = 21.6825 / 88.9943
assert fmt_num(t_val) == '0.2436…'
assert abs(((K - D).conjugate() * (I - D)).imag - 0.007) < 1e-9
ANIMS.append(dict(
    id='D03_K_kouten', title='問2　K点（直線JLと直線DIの交点）', article='第3章',
    view=view([D, J, I, L, Hp, Kw], margin=0.08),
    base=nothing,
    steps=[
        S('直線DIと直線JL', ['調査図素図の注4', 'KはJL上、かつDI上', '電卓：B＝L、C＝I、D＝D、F＝J'], 7,
          'K点は、JとLを結ぶ直線と、DとIを結ぶ直線の交点です（調査図素図の注4）。',
          lambda sc: (sc.poly([D, I, Hp], closed=False, lw=2.0), sc.line(J, L, ls='--', lw=1.8),
                      sc.dot(D, 'concrete'), sc.dot(I, 'concrete'), sc.dot(Hp, 'concrete'), sc.dot(J, 'metal'), sc.dot(L),
                      sc.name(D, 'D', ctr3), sc.name(I, 'I', ctr3), sc.name(Hp, 'H', ctr3), sc.name(J, 'J', ctr3),
                      sc.name(L, 'L', ctr3))),
        S('JLは真南ではない', ['J − L ＝ 18.68 ＋ 1.15i', '北へ18.68進む間に東へ1.15ずれる', '→ 交点の式で出す'], 7,
          'JとLの差を見ると、北へ18.68進む間に東へ1.15ずれています。真南ではないので、交点の式で求めます。',
          lambda sc: (sc.callout((J + L) / 2, 'J − L ＝ 18.68 ＋ 1.15i', dirs=(-20, 0, -40), fs=12),)),
        S('tの分子', ['Conjg(D − J) × (I − D)', '表示：−7.0977 − 21.6825i', 'iの係数 −21.6825 を使う'], 8,
          'tの分子は、共役のDマイナスJかけるIマイナスD。表示のiの係数、マイナス21.6825を使います。',
          lambda sc: (sc.line(J, D, lw=1.6, ls=':'),)),
        S('tの分母', ['Conjg(L − J) × (I − D)', '表示：224.2185 − 88.9943i', 'iの係数 −88.9943 を使う'], 8,
          'tの分母は、共役のLマイナスJかけるIマイナスD。iの係数はマイナス88.9943です。',
          lambda sc: ()),
        S('t ＝ 分子 ÷ 分母', ['t ＝ −21.6825 ÷ −88.9943', '＝ 21.6825 ÷ 88.9943 ＝ 0.2436…', '0と1の間 → JとLの間の点'], 7,
          'tは21.6825割る88.9943で、0.2436。0と1の間なので、KはJとLの間にあります。',
          lambda sc: ()),
        S('K ＝ J ＋ (L − J) × t', ['表示：506.2288… ＋ 492.1798…i', '▶ K点（506.23, 492.18）'], 8,
          'JにLマイナスJのt倍を足して、表示は506.2288と492.1798。四捨五入してK点は506.23、492.18です。',
          lambda sc: (sc.dot(K), sc.callout(K, 'K（506.23, 492.18）', dirs=(0, 20, -20), fs=12))),
        S('検算：KはDI上', ['Conjg(K − D) × (I − D)', 'iの係数 0.007（丸めのずれだけ）', '→ ほぼ0なのでDI上'], 6,
          '検算です。共役のKマイナスDかけるIマイナスDのiの係数は0.007で、ほぼ0。KはDIの上にあります。',
          lambda sc: ()),
        S('誤り：Jの真南に下ろす', ['Y＝492.46でDIと交わる点', '→（505.37, 492.46）', 'JLの線から外れる'], 7,
          'Jの真南に下ろしてしまうと505.37、492.46になり、JLの線から外れます。北に0.86メートルずれます。',
          lambda sc: (sc.line(J, Kw, ls=':', lw=1.4), sc.dot(Kw),
                      sc.callout(Kw, '誤り（505.37, 492.46）', dirs=(160, 180, 140), fs=12))),
    ]))


# =====================================================================
# 座標法の面積（項ごとに積み上げる）を作る共通の関数
# =====================================================================
def polygon_anim(aid, title, article, pts, label_area, first, last, extra=None, view_pts=None, narr_name=''):
    tv = terms(pts)
    total = sum(tv)
    names = [NAMES[p] for p in pts]
    cen = sum(pts) / len(pts)
    steps = [S('頂点を順に回る', [f'{"→".join(names)}→{names[0]}', '倍面積 ＝ P1・Conjg(P2) ＋ … ＋ Pn・Conjg(P1)',
                                   '読むのは iの係数だけ（実部は使わない）'], 8,
               f'{narr_name}の頂点を{"、".join(names)}の順に回ります。各項の、iの係数だけを足していきます。',
               lambda sc: (sc.poly(pts, lw=2.0, fill=BLUE),
                           *[sc.dot(p) for p in pts], *[sc.name(p, NAMES[p], cen) for p in pts]))]
    run = 0
    for i, v in enumerate(tv):
        p, q = pts[i], pts[(i + 1) % len(pts)]
        run += v
        steps.append(S(f'{NAMES[p]}・Conjg({NAMES[q]})', [f'{NAMES[p]}・Conjg({NAMES[q]}) の iの係数', f'＝ {f4(v)}',
                                                          f'ここまでの合計 {f4(run)}'], 6,
                       f'{NAMES[p]}と、{NAMES[q]}の共役の積。iの係数は{f4(v)}。ここまでの合計は{f4(run)}です。',
                       (lambda p=p, q=q: (lambda sc: (sc.line(p, q, lw=3.0),)))()))
    steps.append(S('合計と面積', [f'表示：（実部）{"−" if total < 0 else "＋"} {f4(abs(total))}i',
                                   f'{f4(abs(total))} ÷ 2 ＝ {f4(abs(total) / 2)}', last], 8,
                   f'iの係数の合計は{f4(abs(total))}。符号は回る向きで変わるので絶対値をとり、2で割って{f4(abs(total) / 2)}です。{last}',
                   lambda sc: (sc.free(cen, label_area, fs=15),)))
    if extra:
        steps.append(extra)
    return dict(id=aid, title=title, article=article, view=view(view_pts or pts, margin=0.10), base=first, steps=steps)


# D04：甲土地の面積（公差の判定）
assert abs(abs(sum(terms(KOU))) - 826.65) < 1e-6
ANIMS.append(polygon_anim(
    'D04_kou_menseki', '問3　甲土地の面積（座標法）と公差の判定', '第5章', KOU, '413.325㎡', nothing,
    '甲土地は413.325㎡',
    extra=S('公差の判定', ['登記記録 413.30との差 0.025', '甲2の公差 1.93（問題文の表）', '→ 範囲内、地積更正は要らない'], 8,
            '登記記録の413.30との差は0.025。市街地地域なので甲2の公差1.93の範囲内で、地積更正は要りません。',
            lambda sc: ()), narr_name='甲土地'))

# D05：（ロ）の三角形
tri = (K - I).conjugate() * (L - I)
assert disp(tri) == '−40.9682 − 42.3066i' and disp(K - I) == '7.70 − 2.52i' and disp(L - I) == '−6.43 − 3.39i'
ANIMS.append(dict(
    id='D05_ro_sankaku', title='問3　（ロ）三角形I・K・Lの面積', article='第5章',
    view=view([D, I, Hp, K, L], margin=0.10), base=lambda sc: sc.poly([D, I, Hp], closed=False, color=LIGHT, lw=1.2),
    steps=[
        S('三角形I・K・L', ['甲土地から切り離す部分', '電卓：B＝L、C＝I、X＝K'], 6,
          '甲土地から切り離して乙土地に移す三角形、I・K・Lの面積を求めます。',
          lambda sc: (sc.poly(RO, lw=2.0, fill=ORANGE), *[sc.dot(p) for p in RO],
                      *[sc.name(p, NAMES[p], (I + K + L) / 3) for p in RO])),
        S('Iから2辺を見る', ['K − I ＝ 7.70 − 2.52i', 'L − I ＝ −6.43 − 3.39i'], 7,
          'Iを起点に、KとLへの2つの辺を考えます。KマイナスIは7.70マイナス2.52i、LマイナスIはマイナス6.43マイナス3.39iです。',
          lambda sc: (sc.line(I, K, lw=3.0), sc.line(I, L, lw=3.0))),
        S('Conjg(K − I) × (L − I)', ['[Apps] [4] [ALPHA] [X] [−] [ALPHA] [C] [)]', '[×] [(] [ALPHA] [B] [−] [ALPHA] [C] [)] [=]',
                                      '表示：−40.9682 − 42.3066i'], 8,
          '共役のKマイナスIかけるLマイナスI。表示はマイナス40.9682マイナス42.3066iです。',
          lambda sc: ()),
        S('iの係数 ÷ 2', ['42.3066 ÷ 2 ＝ 21.1533', '宅地は小数第2位未満を切り捨て', '▶（ロ）21.15㎡'], 7,
          'iの係数42.3066を2で割って21.1533。宅地なので小数第2位未満を切り捨てて、（ロ）は21.15平方メートルです。',
          lambda sc: (sc.callout((I + K + L) / 3, '21.15㎡', dirs=(0, 20, -20, 40), fs=14),)),
    ]))

# D06：（イ）2番19の面積
assert abs(abs(sum(terms(KOU1))) - 784.3526) < 1e-6
ANIMS.append(polygon_anim(
    'D06_i_menseki', '問3　（イ）2番19の面積（座標法、6項）', '第5章', KOU1, '392.17㎡',
    lambda sc: sc.poly(RO, color=LIGHT, lw=1.0, fill=ORANGE, alpha=0.25),
    '宅地は切り捨てて 392.17',
    extra=S('引き算ではない', ['413.30 − 21.15 ＝ 392.15 は誤り', '分筆後の地積は座標で1筆ずつ', '▶（イ）392.17、合計413.32'], 8,
            '登記記録から引き算した392.15ではありません。分筆後の地積は座標で1筆ずつ出すので、（イ）は392.17です。',
            lambda sc: ()), view_pts=KOU1 + [I], narr_name='（イ）2番19'))

# D07：合筆後の2番42
ANIMS.append(dict(
    id='D07_gappei_go', title='問3　合筆後の2番42の地積（登記記録 ＋（ロ））', article='第5章',
    view=view(OTSU + [K, L], margin=0.10), base=nothing,
    steps=[
        S('合筆先の2番42', ['登記記録の地積 344.84', '（平成10年の三斜求積の値）', '座標の344.8221…とは別の値'], 7,
          '合筆先の2番42は、登記記録の344.84のままにします。平成10年の三斜求積の値で、今回の座標の値とは別です。',
          lambda sc: (sc.poly(OTSU, lw=2.0, fill=BLUE), sc.free(P(498.0, 501.0), '登記記録 344.84', fs=14, offsets=((0, 0), (0, 20), (0, -20), (20, 30))))),
        S('（ロ）を足す', ['（ロ）21.15（切り捨て後）', '344.84 ＋ 21.15'], 6,
          'そこに（ロ）の21.15を足します。',
          lambda sc: (sc.poly(RO, lw=2.0, fill=ORANGE),
                      sc.callout((I + K + L) / 3, '（ロ）21.15', dirs=(180, 160, -160), fs=12))),
        S('合筆後の地積', ['344.84 ＋ 21.15 ＝ 365.99', '▶ 合筆後の2番42 365.99㎡'], 6,
          '足して365.99。合筆後の2番42は365.99平方メートルです。',
          lambda sc: (sc.free((D + C + B + Hp) / 4, '365.99㎡', fs=15, offsets=((0, -26), (0, -40))),)),
        S('誤り：座標で計算し直す', ['合筆後の区画D・C・B・H・L・Kを', '座標で計算すると 365.97', '→ 合筆は測り直す登記ではない'], 7,
          '合筆後の区画を座標で計算し直すと365.97になりますが、合筆は測り直す登記ではないので書きません。',
          lambda sc: ()),
    ]))

# D08：11月の分筆の3筆の面積
assert abs(abs(sum(terms(URI))) - 704.5887) < 1e-6
t58, t59 = (L - Hp).conjugate() * (M - Hp), (J - D).conjugate() * (K - D)
assert disp(t58) == '10.1761 ＋ 19.2995i' and disp(t59) == '2.6373 ＋ 8.0535i'
d08 = polygon_anim('D08_sanpitsu_menseki', '問5　11月の分筆の3筆の面積と地番', '第8章', URI, '352.29㎡',
                   lambda sc: sc.poly([D, J, K], color=LIGHT, lw=1.0) or sc.poly([Hp, L, M], color=LIGHT, lw=1.0),
                   '2番42（売却部分）は 352.29', view_pts=URI + [D, Hp], narr_name='売却部分の2番42')
d08['steps'] += [
    S('三角形H・L・M', ['Conjg(L − H) × (M − H)', '表示：10.1761 ＋ 19.2995i', '19.2995 ÷ 2 ＝ 9.6497… → 9.64'], 8,
      '南の三角形H・L・M。共役のLマイナスHかけるMマイナスH、iの係数19.2995を2で割って9.64です。',
      lambda sc: (sc.poly(S58, lw=2.0, fill=ORANGE), sc.callout((Hp + L + M) / 3, '9.64㎡', dirs=(180, -160, 160), fs=12))),
    S('三角形D・J・K', ['Conjg(J − D) × (K − D)', '表示：2.6373 ＋ 8.0535i', '8.0535 ÷ 2 ＝ 4.0267… → 4.02'], 8,
      '北の三角形D・J・K。iの係数8.0535を2で割って4.02です。',
      lambda sc: (sc.poly(S59, lw=2.0, fill=ORANGE), sc.callout((D + J + K) / 3, '4.02㎡', dirs=(180, 160, -160), fs=12))),
    S('面積の大きい順に地番', ['問題文の注7：面積が大きい順', '9.64 → 2番58、4.02 → 2番59', '売却部分は2番42のまま'], 8,
      '問題文の注7は面積の大きい順です。南の9.64が2番58、北の4.02が2番59。売却部分は2番42のままです。',
      lambda sc: (sc.callout((Hp + L + M) / 3 + P(-0.6, 0), '2番58', dirs=(-150, -130, -170), fs=12),
                  sc.callout((D + J + K) / 3 + P(0.6, 0), '2番59', dirs=(150, 130, 170), fs=12))),
    S('分筆後の合計で公差', ['352.29 ＋ 9.64 ＋ 4.02 ＝ 365.95', '分筆前 365.99 との差 0.04', '→ 甲2の範囲内、地積更正は不要'], 7,
      '分筆後の合計は365.95で、分筆前の365.99との差は0.04。甲2の範囲内なので地積更正は要りません。',
      lambda sc: ()),
]
ANIMS.append(d08)

# D09：地積測量図の辺長10本
SIDES = [('DJ', D, J, '492.46 − 490.69 ＝ 1.77', '1.77', None), ('JC', J, C, '506.79 − 492.46 ＝ 14.33', '14.33', None),
         ('CB', C, B, 'Abs(B − C)', '24.78', '24.7817…'), ('BM', B, M, '505.19 − 491.31 ＝ 13.88', '13.88', None),
         ('MH', M, Hp, '491.31 − 488.12 ＝ 3.19', '3.19', None), ('HL', Hp, L, 'Abs(L − H)', '6.84', '6.8394…'),
         ('LK', L, K, 'Abs(K − L)', '14.16', '14.1567…'), ('KD', K, D, 'Abs(D − K)', '4.79', '4.7877…'),
         ('JK（分筆線）', J, K, 'Abs(J − K)', '4.56', '4.5586…'), ('LM（分筆線）', L, M, '492.10 − 486.05 ＝ 6.05', '6.05', None)]
d09_steps = [S('11月の分筆前の2番42', ['D→J→C→B→M→H→L→K', '分筆線はJKとLMの2本', '軸に平行な辺は引き算、斜めは電卓'], 7,
               '11月の分筆前の2番42を描き、辺の長さを1本ずつ出します。軸に平行な辺は座標の引き算、斜めの辺は電卓のAbsです。',
               lambda sc: (sc.poly([D, C, B, M, Hp, L, K], lw=1.6, color=LIGHT),
                           *[sc.dot(p) for p in [D, J, C, B, M, Hp, L, K]],
                           *[sc.name(p, NAMES[p], (D + C + B + Hp) / 4) for p in [D, C, B, Hp, L, K]],
                           sc.free(J, 'J', fs=13, offsets=((16, -16), (20, -22), (24, -10))),
                           sc.free(M, 'M', fs=13, offsets=((16, 16), (20, 22), (24, 10)))))]
for nm, p, q, how, ans, raw in SIDES:
    assert f'{round(abs(p - q) + 1e-9, 2):.2f}' == ans, nm
    if raw:
        assert fmt_num(abs(p - q)) == raw, nm
    lines = [how] + ([f'表示：{raw}'] if raw else []) + [f'▶ {nm.split("（")[0]} ＝ {ans}']
    narr = (f'{nm}は、{how.replace(" − ", "引く").replace(" ＝ ", "で")}。' if not raw
            else f'{nm}は斜めの辺なので電卓のAbsで{raw}。小数第3位を四捨五入して{ans}です。')
    inside = (D + C + B + Hp) / 4
    if nm.startswith('JK') or nm.startswith('LM'):
        inside = (J + C + B + M) / 4
    elif nm in ('HL', 'MH'):
        inside = (Hp + L + M) / 3
    elif nm in ('DJ', 'KD'):
        inside = (D + J + K) / 3
    d09_steps.append(S(f'{nm} ＝ {ans}', lines, 5, narr,
                       (lambda p=p, q=q, ans=ans, inside=inside, sep=nm.startswith('JK') or nm.startswith('LM'):
                        (lambda sc: (sc.line(p, q, lw=2.4), sc.edge(p, q, ans, inside, fs=12, outward=not sep))))()))
d09_steps.append(S('四捨五入の確認', ['斜めの辺は小数第3位を四捨五入', '24.7817…→24.78、14.1567…→14.16', '6.8394…→6.84、4.7877…→4.79、4.5586…→4.56'],
                   7, '斜めの辺は小数第3位を四捨五入します。14.1567は切り上がって14.16です。', lambda sc: ()))
ANIMS.append(dict(id='D09_henchou', title='問5　地積測量図の辺長10本', article='第8章',
                  view=view([D, C, B, Hp, K, L], margin=0.10), base=nothing, steps=d09_steps))


# D10：K点の別解（補助線で高さの比。2026-10-20追加、記事の「K点に全く手が出なかった人へ」）
UDI = (I - D) / abs(I - D)
FJ = D + UDI * ((J - D) / UDI).real
FL = D + UDI * ((L - D) / UDI).real
DIe0, DIe1 = D + (D - I) * 0.12, FL + (FL - D) / abs(FL - D) * 1.2
TJ, TL = ((J - D).conjugate() * (I - D)).imag, ((L - D).conjugate() * (I - D)).imag
assert disp((J - D).conjugate() * (I - D)) == '7.0977 ＋ 21.6825i' and disp((L - D).conjugate() * (I - D)) == '231.3162 − 67.3118i'
assert disp(J + (L - J) * 21.6825 / (21.6825 + 67.3118)) == '506.2288… ＋ 492.1798…i'
assert f'{abs(J - FJ):.2f}' == '1.68' and f'{abs(L - FL):.2f}' == '5.22'
ctr10 = K + P(0, -3)
ANIMS.append(dict(
    id='D10_K_hojosen', title='問2　K点の別解（DIを延ばし、J・Lから垂線を下ろす）', article='第3章（K点に全く手が出なかった人へ）',
    view=view([D, J, I, L, FJ, FL, DIe0, DIe1], margin=0.08),
    base=nothing,
    steps=[
        S('直線DIと点J・L', ['KはJL上、かつDI上（調査図素図の注4）', '交点の式を忘れたら、図に戻る', '電卓：B＝L、C＝I、D＝D、F＝J'], 7,
          '交点の式を忘れたときは、図に戻ります。直線DIと、JとLの2点を描きます。',
          lambda sc: (sc.line(D, I, lw=2.4), sc.dot(D, 'concrete'), sc.dot(I, 'concrete'), sc.dot(J, 'metal'), sc.dot(L),
                      sc.name(D, 'D', D + P(0.3, 3)), sc.name(I, 'I', I + P(0.3, -3)), sc.name(J, 'J', ctr10), sc.name(L, 'L', ctr10))),
        S('補助線：DIを延ばす', ['問題用紙の図は線がIで切れている', 'DIを両側に延ばしておく'], 6,
          '補助線として、直線DIを両側に長く延ばします。問題用紙の図では、線がIで切れているからです。',
          lambda sc: (sc.line(DIe0, DIe1, lw=1.4, ls='--'),)),
        S('Jから垂線（高さ1.68）', ['JからDIへ垂線を下ろす', 'DIからJまでの高さ 1.68'], 6,
          'JからDIへ垂線を下ろします。DIからJまでの高さは1.68です。',
          lambda sc: (sc.line(J, FJ, lw=1.8, ls=':'), sc.callout((J + FJ) / 2, '高さ1.68', dirs=(60, 80, 40, 100), dists=(50, 70, 90), fs=12))),
        S('Lから垂線（高さ5.22）', ['LからDIの延長へ垂線を下ろす', 'DIからLまでの高さ 5.22', 'JとLはDIの反対側'], 7,
          'Lからも、DIの延長へ垂線を下ろします。高さは5.22。JとLは、DIの線の反対側にあります。',
          lambda sc: (sc.line(L, FL, lw=1.8, ls=':'), sc.edge(L, FL, '高さ5.22', I, fs=12))),
        S('JLを結ぶと相似', ['JK：KL ＝ Jの高さ：Lの高さ', '垂線どうしは平行 → 相似な直角三角形', '高さは三角形の面積で比べる'], 8,
          'JとLを結ぶと、相似な直角三角形が2つできます。JKとKLの比は、高さの比です。高さは三角形の面積で比べます。',
          lambda sc: (sc.line(J, L, lw=2.2),)),
        S('△DIJの面積の2倍', ['Conjg(J − D) × (I − D)', '表示：7.0977 ＋ 21.6825i', 'iの係数 ＋21.6825'], 8,
          '三角形DIJの面積の2倍は、共役のJマイナスDかけるIマイナスDのiの係数で、プラス21.6825です。',
          lambda sc: (sc.poly([D, I, J], lw=1.0, fill=ORANGE),)),
        S('△DILの面積の2倍', ['Conjg(L − D) × (I − D)', '表示：231.3162 − 67.3118i', 'iの係数 −67.3118（符号が逆）'], 8,
          '三角形DILの面積の2倍は、iの係数がマイナス67.3118。符号が逆なのは、LがDIの反対側にあるからです。',
          lambda sc: (sc.poly([D, I, L], lw=1.0, fill=BLUE),)),
        S('t ＝ J側 ÷ 両側の合計', ['t ＝ 21.6825 ÷ (21.6825 ＋ 67.3118)', '＝ 21.6825 ÷ 88.9943 ＝ 0.2436…', '分母は交点の式と同じ88.9943'], 8,
          'tは、J側の21.6825を、両側の合計88.9943で割った0.2436。分母は、交点の式の分母と同じ数です。',
          lambda sc: ()),
        S('K ＝ J ＋ (L − J) × t', ['表示：506.2288… ＋ 492.1798…i', '▶ K点（506.23, 492.18）', '交点の式と同じ答え'], 8,
          'JにLマイナスJのt倍を足して、K点は506.23、492.18。交点の式と同じ答えになりました。',
          lambda sc: (sc.dot(K), sc.callout(K, 'K（506.23, 492.18）', dirs=(-150, -170, -130), dists=(80, 100, 120), fs=12))),
    ]))


# ---- 実行 -----------------------------------------------------------------
def main():
    total_probs = 0
    md = ['# 絵コンテ：令和8年度 第21問（土地）計算過程の動画\n',
          '記事 `../note_R8_dai21mon_tochi_kaiwa_kaisetsu.md` の計算を、1つの計算につき1本の動画にするための絵コンテ。'
          'このファイルとコマ（`D0N_*/stepNN.png`、横1280×縦720）と試作の動画（`D0N_*.mp4`）は、'
          '`make_R8_dai21mon_douga.py` で作り直す（手で直さない）。\n',
          '- コマ k には、ステップ1〜k の要素が積み上がる。いま説明しているステップの要素は赤、前のステップの要素は灰色\n'
          '- 右の説明パネルに、ステップの一覧と、いまのステップの式・電卓操作・表示を出す（記事の3点セットと同じ値）\n'
          '- 文字の位置は全コマで同じ（最後のコマで重なりの自動検査をして決めた位置）\n'
          '- 秒数は試作の動画の長さ。ナレーション案は、そのまま読み上げてもよい長さの文\n'
          '- 画像の中に図番は入れない\n']
    for a in ANIMS:
        out = os.path.join(HERE, a['id'])
        total_probs += len(render(a, out))
        secs = sum(s['sec'] for s in a['steps'])
        md.append(f'\n## {a["id"]}：{a["title"]}\n')
        md.append(f'- **記事の位置**：{a["article"]}\n- **コマ**：`{a["id"]}/step01.png`〜`step{len(a["steps"]):02d}.png`'
                  f'（{len(a["steps"])}コマ）\n- **試作の動画**：`{a["id"]}.mp4`（約{secs}秒）\n')
        for k, s in enumerate(a['steps'], 1):
            md.append(f'\n### ステップ{k}（{s["sec"]}秒）：{s["short"]}\n')
            md.append('- **画面の文字**：' + '／'.join(s['lines']) + '\n')
            md.append(f'- **ナレーション案**：{s["narr"]}\n')
        if MAKE_VIDEO and shutil.which('ffmpeg'):
            lst = os.path.join(out, 'concat.txt')
            with open(lst, 'w', encoding='utf-8') as fp:
                for k, s in enumerate(a['steps'], 1):
                    fp.write(f"file 'step{k:02d}.png'\nduration {s['sec']}\n")
                fp.write(f"file 'step{len(a['steps']):02d}.png'\n")
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                            '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-movflags', '+faststart',
                            os.path.join(HERE, a['id'] + '.mp4')], check=True)
            os.remove(lst)
        print(f'{a["id"]}: {len(a["steps"])}コマ、約{secs}秒')
    open(os.path.join(HERE, 'kontei_R8_dai21mon_douga.md'), 'w', encoding='utf-8').write(''.join(md))
    print('重なりの合計:', total_probs)


if __name__ == '__main__':
    main()
