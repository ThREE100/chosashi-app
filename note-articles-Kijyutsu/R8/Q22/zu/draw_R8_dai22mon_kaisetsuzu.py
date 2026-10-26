"""令和8年度 第22問（建物）の解説図19枚を、寸法・座標から作図してPNGに書き出す。

`../prompt_R8_dai22mon_kaisetsuzu.md` の図1〜図19どおり（番号は記事の挿入順。番号は管理用で、画像の中には書かない）。
作図の共通部品は `tools/zu_helpers.py`。座標を使わない整理図（固定配置）は check_fixed で文字の重なりと
図の外へのはみ出しを調べ、目視でも確かめる。

建物の座標は (東, 南) で持ち、zu_helpers の (北, 東) には P() で変換する（北 ＝ −南）。
建物の中の座標は、Y1通り・X1通り（壁の中心線）の交点を原点にした「建物座標」（東へ Y1＝0、Y2＝5.30、Y3＝8.15、Y4＝14.20、
南へ X1＝0、X2＝1.00、X3＝11.00、X4＝12.50）。敷地の上では、本件土地の北西の角（A点）を原点にした「敷地座標」で、
建物座標に (0.86, 0.66) を足す（1階の西の外壁は筆界ADから0.8、北の外壁は筆界ABから0.6、壁厚12cmの半分0.06）。

各階平面図の完成形（図14）は、アガルートの解答例（答案用紙の再現）の第3欄の左半分の枠の中に、1/250の実際の大きさで置く。
建物図面は、記述の説明（図8。図面の部分を拡大）と記入の完成形（図9。答案用紙〈A3横〉の右半分＝A4を実寸）に分ける。
実行: python3 note-articles-Kijyutsu/R8/Q22/zu/draw_R8_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
INK = '#1a3a8f'   # 答案に記入する文字（濃い青）


def P(e, s):
    """(東, 南) の点を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def rect(e0, s0, e1, s1):
    return [P(e0, s0), P(e1, s0), P(e1, s1), P(e0, s1)]


def shift(pts, de, ds, k=1.0):
    """建物座標の点を k 倍して (de, ds) ずらす（敷地座標・図面の mm 座標へ）。"""
    return [P(p.imag * k + de, -p.real * k + ds) for p in pts]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def hatch(ax, pts, color=GRAY, pattern='///'):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch=pattern, edgecolor=color, lw=0, zorder=1))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ---- 建物座標（壁の中心線） ----
Y1, Y2, Y3, Y4 = 0.0, 5.30, 8.15, 14.20
X1, X2, X3, X4 = 0.0, 1.00, 11.00, 12.50
F1 = [P(Y1, X1), P(Y4, X1), P(Y4, X4), P(Y3, X4), P(Y3, X3), P(Y1, X3)]          # 1階（X1通りから）
F7 = [P(Y1, X2), P(Y4, X2), P(Y4, X4), P(Y3, X4), P(Y3, X3), P(Y1, X3)]          # 7階（X2通りから。北の1.00はバルコニー）
D_C = rect(Y1, X2, Y2, X3)                     # Dタイプ（壁心）
E_C = rect(Y2, X2, Y3, X3)                     # Eタイプ（壁心）
F_C = [P(Y3, X2), P(Y4, X2), P(Y4, X4), P(Y3, X4)]
PS_C = rect(0, 10, 1.00, 11)                    # Dの南西の角のPS（壁心）
MBD_C = rect(4.35, 10, 5.30, 11)                # DのMB・PS（1.000＋0.900＋1.050＋1.400＝4.35から）
MBE_C = rect(7.05, 10, 8.15, 11)                # EのMB・PS（Y2＋1.750＝7.05から）
T = 0.06                                         # 壁厚12cmの半分
# 内法（専有部分の床面積を測る線）
D_IN = [P(0.06, 1.06), P(5.24, 1.06), P(5.24, 9.94), P(4.29, 9.94), P(4.29, 10.94), P(1.06, 10.94), P(1.06, 9.94),
        P(0.06, 9.94)]
E_IN = [P(5.36, 1.06), P(8.09, 1.06), P(8.09, 9.94), P(6.99, 9.94), P(6.99, 10.94), P(5.36, 10.94)]
WALL = rect(5.24, 1.06, 5.36, 9.94)              # 平成12年に撤去し、令和8年9月30日に設け直した壁（MB・PSより北の部分）
assert round(area(D_IN), 4) == 49.2284 and round(area(E_IN), 4) == 25.8724 and round(area(WALL), 4) == 1.0656
assert round(area(D_IN) + area(E_IN) + area(WALL), 4) == 76.1664
# 敷地（敷地座標。A点が原点、東へ17.00、南へ13.75）
SITE = rect(0, 0, 17.00, 13.75)
OE, OS = 0.86, 0.66                              # 建物座標 → 敷地座標
assert round(area(SITE), 2) == 233.75


def dims(z, pts, labels, fs=13, ref=None):
    """多角形の各辺に寸法（None は書かない）を外側に書く。"""
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


# ======================================================================
# 固定配置の図の部品（R7/Q22 と同じ）
# ======================================================================

def fixed_figure(title, w=16, h=10, rect_=(0.02, 0.04, 0.96, 0.86)):
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.975)
    ax = fig.add_axes(list(rect_))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax


def check_fixed(fig, name):
    """固定配置の図の重なり検査（文字どうしの重なりと、図の外へのはみ出し）。"""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    texts = list(fig.texts)
    if fig._suptitle is not None and fig._suptitle not in texts:
        texts.append(fig._suptitle)
    for ax in fig.axes:
        texts += list(ax.texts) + [ax.title]
    texts = [t for t in texts if t.get_visible() and t.get_text().strip()]
    bbs = []
    for t in texts:
        bb = t.get_window_extent(r)
        if hasattr(t, 'get_bbox_patch') and t.get_bbox_patch() is not None:
            bb = t.get_bbox_patch().get_window_extent(r)
        bbs.append(bb)
    W, H = fig.bbox.width, fig.bbox.height
    probs = []
    for i, (t, bb) in enumerate(zip(texts, bbs)):
        if bb.x0 < 2 or bb.y0 < 2 or bb.x1 > W - 2 or bb.y1 > H - 2:
            probs.append(f'{name} 図の外へのはみ出し: {t.get_text()!r}')
        for t2, bb2 in zip(texts[i + 1:], bbs[i + 1:]):
            if bb.overlaps(bb2):
                probs.append(f'{name} 文字どうし: {t.get_text()!r} と {t2.get_text()!r}')
    print(f'[重なり検査] {name}（固定配置）: ' + ('問題なし' if not probs else f'{len(probs)}件'))
    for q in probs:
        print('   ', q)
    PROBLEMS.extend(probs)


def save_fixed(fig, name):
    check_fixed(fig, name)
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def rbox(ax, x, y, w, h, col, alpha=0.12, lw=1.8, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=to_rgba(col, alpha) if alpha else 'none',
                                edgecolor=col, lw=lw, ls=ls))


def vline(fig, x, y0=0.10, y1=0.86):
    fig.add_artist(plt.Line2D([x, x], [y0, y1], transform=fig.transFigure, color=GRAY, lw=1.2))


def lines(ax, x, y, items, fs=15, step=6.2, ha='left'):
    """(文字, 色, 太字か) の並びを上から順に書く。"""
    for k, (t, col, bold) in enumerate(items):
        ax.text(x, y - step * k, t, ha=ha, va='center', fontsize=fs, color=col, weight='bold' if bold else 'normal')


def mini_plan(ax, x0, y0, k, ar, d_col, e_col, wall_ok, labels):
    """7階のDタイプ・Eタイプの小さな平面図（固定配置の図の中）。k は東西1mあたりの作業座標、ar は縦の倍率
    （作業座標の縦横の長さの比を図の縦横比で直す）。(x0, y0) は北西の角（X2・Y1）。"""
    ky = k * ar

    def R(e0, s0, e1, s1, **kw):
        ax.add_patch(Rectangle((x0 + e0 * k, y0 - (s1 - 1) * ky), (e1 - e0) * k, (s1 - s0) * ky, **kw))
    R(0, 1, 5.3, 11, facecolor=to_rgba(d_col, 0.18), edgecolor=BLACK, lw=2.2)
    R(5.3, 1, 8.15, 11, facecolor=to_rgba(e_col, 0.18), edgecolor=BLACK, lw=2.2)
    if not wall_ok:   # 壁を撤去した部分を白く抜いて点線
        R(5.22, 1.25, 5.38, 9.9, facecolor='white', edgecolor='none', lw=0)
        ax.plot([x0 + 5.3 * k] * 2, [y0 - 0.25 * ky, y0 - 8.9 * ky], color=GRAY, lw=1.4, ls=':')
    for b in (PS_C, MBD_C, MBE_C):
        (e0, s0), (e1, s1) = (b[0].imag, -b[0].real), (b[2].imag, -b[2].real)
        R(e0, s0, e1, s1, facecolor='#dddddd', edgecolor=BLACK, lw=1.2)
    for e, s_, t in labels:
        ax.text(x0 + e * k, y0 - (s_ - 1) * ky, t, ha='center', va='center', fontsize=14, weight='bold', linespacing=1.3)


# ======================================================================
# 図1：区分と分割（登記の目的のわな）
# ======================================================================

def zu01():
    fig, ax = fixed_figure('1つの専有部分を2つに分ける登記は「区分」。附属建物を切り離す「分割」ではない', w=18, h=11,
                           rect_=(0.02, 0.10, 0.96, 0.79))
    AR = (0.96 * 18) / (0.79 * 11)   # 作業座標の縦1の長さを横1にそろえる倍率
    ax.text(24.5, 95, '平成12年〜令和8年9月　6番3の701は1個', ha='center', va='center', fontsize=15, weight='bold', color=BLUE)
    mini_plan(ax, 13, 89, 2.6, AR, BLUE, BLUE, False, [(2.65, 5, 'D'), (6.7, 5, 'E')])
    ax.text(24.5, 31, 'Dタイプ＋Eタイプで1つの専有部分\n間の壁の一部を撤去（行き来できる）\n床面積 7階部分 76.16㎡',
            ha='center', va='center', fontsize=13.5, linespacing=1.45)
    ax.annotate('', xy=(55, 62), xytext=(45, 62), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=GRAY))
    ax.text(50, 70, '9月30日\n壁を設け直す', ha='center', va='center', fontsize=13, color=GRAY, linespacing=1.4)
    ax.text(74.5, 95, '区分した後（令和8年10月18日申請）', ha='center', va='center', fontsize=15, weight='bold', color=GREEN)
    mini_plan(ax, 63, 89, 2.6, AR, GREEN, ORANGE, True, [(2.65, 5, 'D\n701'), (6.7, 5, 'E\n702')])
    ax.text(74.5, 31, '701（Dタイプ）は残り、702（Eタイプ）が新しくできる\nEタイプだけを安田結さんに売れるようになる',
            ha='center', va='center', fontsize=13.5, linespacing=1.45)
    rbox(ax, 2, 2, 45, 19, RED, alpha=0.07)
    ax.text(24.5, 16, '誤り：建物分割登記', ha='center', va='center', fontsize=17, weight='bold', color=RED)
    ax.text(24.5, 7.5, '附属建物を主である建物の登記記録から\n切り離すときの登記（不動産登記法第54条第1項第1号）',
            ha='center', va='center', fontsize=13, linespacing=1.4)
    rbox(ax, 53, 2, 45, 19, GREEN, alpha=0.07)
    ax.text(75.5, 16, '正解：区分建物区分登記', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(75.5, 7.5, '建物の部分で区分建物に当たるものを\n登記記録上区分建物とする登記（同項第2号）',
            ha='center', va='center', fontsize=13, linespacing=1.4)
    fig.text(0.5, 0.045, '701は附属建物のない1個の専有部分。Dタイプ・Eタイプのどちらも附属建物ではないので、切り離す「分割」は当てはまらない',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R8_dai22mon_zu01_kubun_bunkatsu')


# ======================================================================
# 図2：時系列メモ
# ======================================================================

def zu02():
    fig, ax = fixed_figure('時系列メモ　壁を設けた日は登記の原因の日付にならない', w=18, h=9.5,
                           rect_=(0.02, 0.13, 0.96, 0.75))
    ev = [(4, '平成12年\n6月17日', 'WK不動産が新築\n701をDとEの1つの\n専有部分として登記\n（敷地権も同じ日）', BLUE),
          (20.5, '令和8年\n9月1日', 'Eタイプを売ることに\nした\n（登記記録の調査日）', GRAY),
          (37, '令和8年\n9月30日', 'DとEの間に\nコンクリートの壁\n＋リフォーム', ORANGE),
          (53.5, '令和8年\n10月18日', '安田結さんと売買契約\n規約証明書で割合を確認\n承諾書など受領', PURPLE),
          (70, '令和8年\n10月18日', '区分建物区分登記を\n申請（問2）', GREEN)]
    ax.plot([2, 84], [62, 62], color=GRAY, lw=2)
    for x, d, t, col in ev:
        ax.plot([x + 7], [62], 'o', ms=14, color=col)
        ax.text(x + 7, 78, d, ha='center', va='center', fontsize=15, weight='bold', color=col, linespacing=1.3)
        ax.text(x + 7, 38, t, ha='center', va='center', fontsize=13.5, linespacing=1.45)
    rbox(ax, 86, 30, 12.5, 42, RED, alpha=0.06)
    ax.text(92.3, 51, '区分は\n形成的\n登記\n\n申請の\n義務も\n期限も\nない', ha='center', va='center', fontsize=13,
            color=RED, linespacing=1.35)
    ax.text(50, 8, '区分の原因には日付を書かない。敷地権の原因は、割合が変わる701が10月18日の変更、702が平成12年6月17日',
            ha='center', va='center', fontsize=15, weight='bold', color=GREEN)
    fig.text(0.5, 0.05, '登記記録の抜粋は令和8年9月1日現在。事実関係8で、それ以外の変更はないことを確かめている',
             ha='center', va='center', fontsize=14)
    save_fixed(fig, 'R8_dai22mon_zu02_jikeiretsu')


# ======================================================================
# 図3：注の仕分け
# ======================================================================

CHUU_MONDAI = [('注1', '行為は全て適法、書類も全て適法', None),
               ('注2', '書面申請', '申請書は「〜書」の形で書く'),
               ('注3', '建物図面1/500、各階平面図1/250', '第3欄の縮尺'),
               ('注4', '各階平面図は小数第2位、\n建物図面は小数第1位', '5.18など／1.6・0.8'),
               ('注5', '字画を明瞭に、訂正の方法', None),
               ('注6', '予定家屋番号　D＝701、E＝702', '区分した建物の家屋番号')]
CHUU_ZU = [('（注）1', '距離の単位はメートル', None),
           ('（注）2', '図1は筆界から外壁まで、図3は壁の中心線から。\n壁厚はすべて12cm', '内法は壁の中心線から0.06内側'),
           ('（注）3', 'MB・PSは法定共用部分', '専有部分の床面積から除く'),
           ('（注）4', '隅部は直角。◎印は各階の重なり部分', '1階と7階はY4・X4の角で重なる'),
           ('（注）5〜7', '地番、筆界点、北はX軸の正の方向', None),
           ('（注）8', '寸法値は備付けの図面と合致', None),
           ('（注）9', '天井高はすべて2.5m以上', '床面積から除く部分はない'),
           ('（注）10', '第3欄の建物図面の点線は1階の形状', '1階はもう描いてある')]


def zu03():
    fig, ax = fixed_figure('注は2か所。「問題文の注」と「図の（注）」を言い分ける', w=18, h=13,
                           rect_=(0.02, 0.08, 0.96, 0.82))
    rbox(ax, 1, 2, 45, 86, BLUE, alpha=0.06)
    rbox(ax, 50, 2, 49, 86, ORANGE, alpha=0.06)
    ax.text(23.5, 96.5, '問題文の注1〜注6', ha='center', va='center', fontsize=20, weight='bold', color=BLUE)
    ax.text(23.5, 92.0, '（問4の囲みの後ろ。答案の書き方の決まり）', ha='center', va='center', fontsize=13, color=BLUE)
    ax.text(74.5, 96.5, '図の（注）1〜10', ha='center', va='center', fontsize=20, weight='bold', color=ORANGE)
    ax.text(74.5, 92.0, '（登記記録の抜粋の後ろ。図1〜図3と第3欄の読み方）', ha='center', va='center', fontsize=13, color=ORANGE)

    def rows(items, x, y0, col, wrap, step=3.9):
        y = y0
        for no, body, use in items:
            n = body.count('\n') + 1
            c = BLACK if use else GRAY
            ax.text(x, y, no, ha='left', va='top', fontsize=14, weight='bold', color=col if use else GRAY)
            ax.text(x + wrap, y, body, ha='left', va='top', fontsize=13.5, color=c, linespacing=1.4)
            y -= step * n
            if use:
                ax.text(x + wrap, y, '→ ' + use, ha='left', va='top', fontsize=13.5, color=col, weight='bold')
                y -= step
            y -= 2.2
        return y
    rows(CHUU_MONDAI, 2.5, 86, BLUE, 4.5)
    rows(CHUU_ZU, 51.5, 86, ORANGE, 9.0)
    rbox(ax, 3.5, 5, 40, 17, RED, alpha=0.05, lw=1.4)
    ax.text(23.5, 18.5, '同じ「4」でも別の注', ha='center', va='center', fontsize=15, weight='bold', color=RED)
    ax.text(5, 12.5, '問題文の注4：距離の桁数', ha='left', va='center', fontsize=14, color=BLUE, weight='bold')
    ax.text(5, 7.5, '図の（注）4：◎印は重なり部分', ha='left', va='center', fontsize=14, color=ORANGE, weight='bold')
    fig.text(0.5, 0.035, '色付き＝答えに使う注（→の先が使う場面）、灰色＝本文では取り上げない注', ha='center', va='center', fontsize=14)
    save_fixed(fig, 'R8_dai22mon_zu03_chuu_shiwake')


# ======================================================================
# 図4：二つの独立性
# ======================================================================

def zu04():
    fig, ax = fixed_figure('問1　二つの独立性は「構造上」と「利用上」', w=18, h=10.5, rect_=(0.02, 0.09, 0.96, 0.79))
    for x, col, head, lines_ in [
            (1, BLUE, '構造上の独立性', ['壁・床・天井などで、ほかの部分と', 'しっかり区切られていること', '',
                                          '本問：9月30日にDとEの間へ', 'コンクリート構造の壁を設け、', '内部から行き来できなくした']),
            (51, GREEN, '利用上の独立性', ['その部分だけで、住居などの用途に', '独立して使えること（外へ直接出入りできる）', '',
                                          '本問：DとEのそれぞれに玄関があり', '共用廊下へ出られる。リフォームで', 'それぞれ居宅として使える'])]:
        rbox(ax, x, 26, 47, 62, col, alpha=0.08)
        ax.text(x + 23.5, 82, head, ha='center', va='center', fontsize=21, weight='bold', color=col)
        for k, t in enumerate(lines_):
            ax.text(x + 23.5, 72 - 7 * k, t, ha='center', va='center', fontsize=14.5,
                    weight='bold' if k >= 3 else 'normal')
    rbox(ax, 1, 2, 97, 16, RED, alpha=0.06)
    ax.text(49.5, 14, '誤り：「行き来できないこと」を利用上の独立性に入れる', ha='center', va='center', fontsize=16, weight='bold',
            color=RED)
    ax.text(49.5, 6, '内部で行き来できないのは、壁で仕切られた結果。構造上の独立性の話で、利用上の独立性は「単独で使えるか」',
            ha='center', va='center', fontsize=14)
    fig.text(0.5, 0.04, '建物の区分所有等に関する法律第1条（構造上区分された数個の部分で独立して住居等の用途に供することができるもの）、'
             '不動産登記事務取扱手続準則第78条第2項', ha='center', va='center', fontsize=13)
    save_fixed(fig, 'R8_dai22mon_zu04_dokuritsusei')


# ======================================================================
# 図5：敷地の辺長確認図
# ======================================================================

def zu05():
    fig, axes = new_figure('本件土地（6番3）の形と辺長の確認（作図チェック用）',
                           '座標一覧表：A（13.75, 0.00）、B（13.75, 17.00）、C（0.00, 17.00）、D（0.00, 0.00）。'
                           'Xが同じAB・DCは東西、Yが同じAD・BCは南北の辺で長方形。\n17.00×13.75＝233.75㎡は登記記録の地積と一致。辺長は建物図面には書かない',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    fit(ax, SITE, margin=0.32, pad_aspect=True)
    pts = {'A': P(0, 0), 'B': P(17, 0), 'C': P(17, 13.75), 'D': P(0, 13.75)}
    for n, p in pts.items():
        z.point(p)
        z.point_label(p, n, away=centroid(SITE))
    dims(z, SITE, ['AB＝17.00', 'BC＝13.75', 'CD＝17.00', 'DA＝13.75'], fs=15)
    z.free_text(P(8.5, 6.9), '6番3　宅地\n233.75㎡', fs=17)
    z.free_text(P(8.5, -3.3), '道', fs=15, color=GRAY)
    z.north_arrow()
    save(fig, [z], 'R8_dai22mon_zu05_shikichi_henchou')


# ======================================================================
# 図6：1階と7階の形（一点鎖線）
# ======================================================================

def site_base(z, lw=1.6):
    z.poly(SITE, color=BLACK, lw=lw)


def zu06():
    fig, axes = new_figure('7階の形は1階と違う → 一棟の7階の形を一点鎖線で描く',
                           '1階はX1通りから、7階はX2通りから（北の1.00はバルコニーで床面積に入らない）。◎印のY4・X4の角で1階と7階が重なる。'
                           '\n形が違うので、点線（一棟の1階）・一点鎖線（一棟の7階）・実線（Dタイプ）の3種類の線になる（不動産登記事務取扱手続準則第52条第2項・第3項）',
                           w=18, h=10, ncols=2)
    fig.subplots_adjust(top=0.86, bottom=0.16)
    zs = []
    for k, (ax, title, col, draw7) in enumerate([(axes[0], '誤り：点線と実線だけ（7階の形がない）', RED, False),
                                                 (axes[1], '正解：一棟の7階を一点鎖線で足す', GREEN, True)]):
        z = Zu(ax, fontsize=12)
        site_base(z)
        z.poly(shift(F1, OE, OS), color=BLACK, lw=1.6, ls=(0, (4, 3)))
        if draw7:
            z.poly(shift(F7, OE, OS), color=BLUE, lw=1.8, ls='-.')
        z.poly(shift(D_C, OE, OS), color=BLACK, lw=2.8, fill=GREEN if draw7 else RED, alpha=0.12)
        ax.set_title(title, fontsize=16, weight='bold', color=col)
        fit(ax, SITE, margin=0.14, pad_aspect=True)
        z.free_text(P(OE + 2.65, OS + 6.0), 'Dタイプ\n（実線）', fs=12)
        z.callout(shift([P(Y4, X4)], OE, OS)[0], '◎印（重なり）', dirs=(-60, -30, -90), fs=11)
        z.callout(shift([P(11.5, 0)], OE, OS)[0], '一棟の1階（点線）', dirs=(60, 90, 30), fs=11)
        if draw7:
            z.callout(shift([P(11.5, 1.0)], OE, OS)[0], '一棟の7階\n（一点鎖線）', dirs=(-100, -120, -80, -135),
                      dists=(45, 60, 75), fs=11, color=BLUE)
        zs.append(z)
    save(fig, zs, 'R8_dai22mon_zu06_ittensasen')


# ======================================================================
# 図7：北の距離 0.6 → 1.6
# ======================================================================

def zu07():
    fig, axes = new_figure('Dタイプを描く位置は北1.6（1階の0.6の位置に描かない）',
                           '図1〔調査図〕の0.6は1階の北の外壁まで。7階の北の外壁は、X1通りとX2通りの間の1.00だけ南にあるので0.6＋1.0＝1.6。'
                           '\n西の外壁は1階も7階もY1通りなので0.8のまま。答案用紙には1階の点線と0.6・0.8が記載済みなので、1.6は描く位置の確かめに使い、書き足さない',
                           w=16, h=11)
    fig.subplots_adjust(top=0.90, bottom=0.17)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    # 北西の角の拡大（敷地座標で東0〜8、南0〜5）
    z.line(P(-1, 0), P(9, 0), color=BLACK, lw=2.2)
    z.line(P(0, -1), P(0, 5.5), color=BLACK, lw=2.2)
    z.line(P(0.8, 0.6), P(9, 0.6), color=BLACK, lw=1.6, ls=(0, (4, 3)))
    z.line(P(0.8, 0.6), P(0.8, 5.5), color=BLACK, lw=1.6, ls=(0, (4, 3)))
    z.line(P(0.8, 1.6), P(9, 1.6), color=BLACK, lw=2.8)
    z.line(P(0.8, 1.6), P(0.8, 5.5), color=BLACK, lw=2.8)
    hatch(ax, rect(0.8, 0.6, 9, 1.6), color=GRAY, pattern='..')
    fit(ax, [P(-2.5, -2.2), P(10.5, 6.5)], margin=0.02, pad_aspect=True)
    z.dim_line(P(2.4, 0), P(2.4, 0.6), color=RED)
    z.dim_line(P(5.6, 0), P(5.6, 1.6), color=GREEN)
    z.dim_line(P(0, 3.6), P(0.8, 3.6), color=GREEN)
    z.callout(P(2.4, 0.3), '0.6（1階の北の外壁。ここに描くのは誤り）', dirs=(150, 170, 135), dists=(80, 100, 130), fs=13, color=RED)
    z.callout(P(5.6, 0.8), '1.6（7階のDタイプの北の外壁。正しい位置）', dirs=(30, 15, 45), dists=(70, 95), fs=13, color=GREEN)
    z.callout(P(0.4, 3.6), '0.8（西）', dirs=(200, 180, 220), dists=(60, 80), fs=13, color=GREEN)
    z.free_text(P(7.2, 1.1), 'バルコニー（7階）', fs=12, color=GRAY,
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none'))
    z.free_text(P(4.5, 4.4), 'Dタイプ（7階）', fs=14)
    z.free_text(P(4.5, -1.3), '道（筆界AB）', fs=13, color=GRAY)
    z.free_text(P(-1.2, 4.6), '筆界AD', fs=13, color=GRAY, ha='right')
    z.point(P(0, 0))
    z.point_label(P(0, 0), 'A', away=P(3, 3))
    save(fig, [z], 'R8_dai22mon_zu07_kita_kyori')


# ======================================================================
# 答案用紙の枠（仮の形）
# ======================================================================

def frame_fig(title, w_mm, h_mm, pad_top=34, pad_bottom=30):
    """図の中に、1mm＝10px の作業座標（mm）の軸を作る。軸の範囲は (0, w_mm) × (−pad_bottom, h_mm + pad_top)。"""
    setup_font()
    W = w_mm + 20
    H = h_mm + pad_top + pad_bottom
    fig = plt.figure(figsize=(W / 10, H / 10 + 0.9), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=19, weight='bold', y=0.985)
    ax = fig.add_axes([0, 0, 1, (H / 10) / (H / 10 + 0.9)])
    ax.set_xlim(-10, w_mm + 10)
    ax.set_ylim(-pad_bottom, h_mm + pad_top)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


def box(ax, x0, y0, x1, y1, text='', fs=12, ha='center', color=BLACK, lw=1.4):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 2
        ax.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


# 答案用紙の第3欄（アガルートの解答例〈答案用紙の再現〉の2ページ目から測った寸法。A3横で1px＝0.21mm）
# 1枚の枠（横301.8mm×縦231mm）の左半分が各階平面図、右半分が建物図面（イ）。家屋番号（印刷「（略）」）・建物の所在
# （記入済み）の欄は右上、作成者（略）・縮尺1/250と申請人（略）・縮尺1/250は枠の下。左右の境は枠の上下の短い線。
# 印刷の（略）の欄にも、自力で解いた答え（家屋番号・申請人）を記入する（ユーザー指示、2026-10-20）。
SW, SH, SMID = 301.8, 231.0, 150.9
MMPX = 7   # 1mm を 7px で描く


def sheet3(title, side, name):
    setup_font()
    x0, x1 = (-30, SMID + 6) if side == 'left' else (SMID - 6, SW + 8)
    y0, y1 = -24, SH + 20
    W, H = (x1 - x0) * MMPX / 100, (y1 - y0) * MMPX / 100
    fig = plt.figure(figsize=(W, H + 0.8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=17, weight='bold', y=0.99)
    ax = fig.add_axes([0, 0, 1, H / (H + 0.8)])
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_aspect('equal')
    ax.axis('off')
    box(ax, 0, 0, SW, SH, lw=1.8)
    for ya, yb in ((SH - 10, SH), (0, 10)):
        ax.plot([SMID, SMID], [ya, yb], color=BLACK, lw=1.8)
    z = Zu(ax, fontsize=9)
    ax.set_aspect('equal')
    if side == 'left':
        ax.text(-26, SH + 3, '第3欄', ha='left', va='center', fontsize=13, weight='bold')
        ax.text(80, SH + 3.5, '各　階　平　面　図', ha='center', va='center', fontsize=15)
        box(ax, 0, -14.5, 18.7, 0, '作 成 者', fs=11)
        box(ax, 18.7, -14.5, 108.6, 0)
        ax.text(63, -5, '（略）', ha='center', va='center', fontsize=11)
        ax.text(106, -11.5, '（令和8年○月○日作成）', ha='right', va='center', fontsize=9)
        box(ax, 108.6, -14.5, 118.7, 0, '縮尺', fs=10)
        box(ax, 118.7, -14.5, 142.8, 0)
        ax.plot([120.5, 141], [-13.5, -1], color=BLACK, lw=0.9)
        ax.text(123.5, -3.5, '1', ha='center', va='center', fontsize=10)
        ax.text(138, -11, '250', ha='center', va='center', fontsize=10)
        # Dタイプ7階の内法（1/250＝1mが4mm）。内法の北西の角を (68, 148.7) に置く
        k, ox, oy = 4.0, 68.0, 148.7
        dd = [complex(oy - (-q.real - 1.06) * k, ox + (q.imag - 0.06) * k) for q in D_IN]
        z.poly(dd, color=INK, lw=1.6)
        dims(z, dd, ['5.18', '8.88', '0.95', None, '3.23', None, '1.00', '8.88'], fs=9)
        z.edge_label(dd[3], dd[4], '1.00', centroid(dd), fs=8, outward=False)
        z.edge_label(dd[5], dd[6], '1.00', centroid(dd), fs=8, outward=False)
        ax.text(78.4, 155.5, '7階', ha='center', va='center', fontsize=11, color=INK, weight='bold')
        ax.text(52, 82, '求　積　表\n5.18 × 8.88 ＝ 45.9984\n3.23 × 1.00 ＝ 3.2300\n　合計　49.2284\n　床面積　49.22㎡', ha='left',
                va='center', fontsize=10, color=INK, linespacing=1.6)
        assert round(area(dd) / (k * k), 4) == 49.2284
        fig.text(0.5, 0.012, '内法の辺長（小数第2位まで。問題文の注4）と求積表を書く。専有部分は7階だけなので重ねる下の階はなく、方位も書かない',
                 ha='center', va='bottom', fontsize=10)
    save(fig, [z], name)


# ======================================================================
# 図8・図9：建物図面（記述の説明と記入の完成形を分ける。2026-10-21 ユーザー指示：
# 1/500の実際の大きさでは小さすぎるので、図面の部分を拡大して描く）
# ======================================================================

NEIGHBOR_LINES = [(-5, 0, 0, 0), (-5, 1.9, 0, 1.9), (17, 0, 21, 0), (-5, 13.75, 0, 13.75), (17, 13.75, 21, 13.75),
                  (7.0, 13.75, 7.2, 16.5), (14.9, 13.75, 15.1, 16.5)]
NEIGHBOR_NAMES = [(8.5, -3.2, '道'), (-3.0, 0.95, '6-10'), (-3.0, 7.0, '6-12'), (19.5, 7.0, '6-17'),
                  (3.5, 15.8, '6-5'), (11.0, 15.8, '6-1'), (18.5, 15.8, '6-7')]


def zumen_lines(z, lw=1.0, printed=GRAY, ink=INK, d_fill=None):
    """建物図面の線（敷地座標の Zu の上）。printed は記載済み、ink は記入するものの色。"""
    z.poly(SITE, color=printed, lw=1.6 * lw)
    for (e0, s0, e1, s1) in NEIGHBOR_LINES:
        z.line(P(e0, s0), P(e1, s1), color=printed, lw=1.2 * lw)
    z.poly(shift(F1, OE, OS), color=printed, lw=1.5 * lw, ls=(0, (4, 3)))
    z.poly(shift(F7, OE, OS), color=ink, lw=1.8 * lw, ls='-.')
    z.poly(shift(D_IN, OE, OS), color=ink, lw=2.8 * lw, fill=d_fill, alpha=0.10)


def zu08():
    """建物図面に書くもの（記述）の説明図。図面の部分を拡大し、線・数字ごとに引き出しで説明する。"""
    fig, axes = new_figure('建物図面（イ）に書くもの・書かないもの',
                           '灰色：答案用紙に記載済み（敷地・隣接地・一棟の1階の点線・距離0.6と0.8・方位）\n'
                           '青：記入するもの（一棟の7階の一点鎖線・Dタイプの実線・「建物の存する部分　7階」）　緑：位置の確かめに使うだけで書かないもの\n'
                           '図面の部分を拡大して描いている（答案用紙では縮尺1/500で、敷地は横34mm×縦27.5mmの大きさ）',
                           w=17, h=14)
    fig.subplots_adjust(top=0.93, bottom=0.14)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    zumen_lines(z, lw=1.3)
    for (e, s_, t) in NEIGHBOR_NAMES:
        z.free_text(P(13.5, -2.8) if t == '道' else P(e, s_), t, fs=14, color=GRAY)
    fit(ax, [P(-15, -7), P(32, 23)], margin=0.0, pad_aspect=True)
    # 記載済みの距離
    z.dim_line(P(2.6, 0), P(2.6, 0.66 - 0.06), color=GRAY)
    z.dim_line(P(0, 3.2), P(0.8, 3.2), color=GRAY)
    # 位置の確かめ（書かない）
    z.dim_line(P(4.4, 0), P(4.4, 1.6), color=GREEN)
    z.callout(P(2.6, 0.3), '0.6（記載済み）\n1階の北の外壁まで', dirs=(150, 135, 165), dists=(90, 120, 150), fs=13, color=GRAY)
    z.callout(P(4.4, 0.8), '1.6（書かない）\n7階のDタイプの北の外壁は\n0.6＋1.0＝1.6の位置に描く', dirs=(60, 75, 45),
              dists=(110, 140, 170), fs=13, color=GREEN)
    z.callout(P(0.4, 3.2), '0.8（記載済み）\n西の外壁まで。\n7階もY1通りで同じ', dirs=(165, 180, 150), dists=(90, 120, 150), fs=13,
              color=GRAY)
    z.callout(shift([P(12.0, 0)], OE, OS)[0], '点線：一棟の1階（記載済み。図の（注）10）', dirs=(70, 60, 80), dists=(80, 110, 140),
              fs=13, color=GRAY)
    z.callout(shift([P(Y4, 5.0)], OE, OS)[0], '記入①　一点鎖線：一棟の7階\n形が1階と違うので描く\n（準則第52条第3項）',
              dirs=(0, 15, -15), dists=(110, 140, 170), fs=13, color=INK)
    z.callout(shift([P(0.06, 7.5)], OE, OS)[0], '記入②　実線：Dタイプ（7階）\n専有部分の内法の形\n（規則第82条第1項）',
              dirs=(195, 210, 180), dists=(110, 140, 170), fs=13, color=INK)
    z.callout(shift([P(2.7, 10.94)], OE, OS)[0], 'PS・MB・PSの欠け\n（法定共用部分。壁ごと除く）', dirs=(-120, -135, -105),
              dists=(110, 140, 170), fs=13, color=INK)
    z.callout(shift([P(Y4, X4)], OE, OS)[0], '◎印のY4・X4の角で\n1階と7階が重なる', dirs=(-20, -35, -5), dists=(90, 120, 150), fs=13,
              color=BLACK)
    z.callout(P(17.0, 3.5), '敷地の辺長17.00・13.75は書かない\n（作図の確かめ用）', dirs=(20, 35, 5), dists=(150, 190, 230), fs=13,
              color=GREEN)
    z.free_text(P(8.5, 20.5), '記入③　建物の存する部分　7階', fs=17, color=INK, weight='bold',
                bbox=dict(boxstyle='round,pad=0.4', fc='white', ec=INK, lw=1.4))
    z.north_arrow()
    save(fig, [z], 'R8_dai22mon_zu08_tatemono_zumen_kisai')


# 答案用紙の第3欄（A3横 420×297mm）の右半分＝A4（210×297mm）。座標はA3の用紙の左上を原点にした mm（右へ x、下へ y）。
# アガルートの解答例（答案用紙の再現、A3のPDF）の線の座標を読んだ値。印刷の線の太さは pt（1.13・0.34・0.37）。
A4_X0, A4_X1, A4_Y1 = 210.0, 420.0, 297.0
PX_PER_MM = 8                                     # 1mm を 8px（1680×2376px。A4に印刷すると実寸）
SHEET_LINES = [                                   # (x0, y0, x1, y1, 太さpt)
    (232.33, 24.89, 383.53, 24.89, 1.13), (232.33, 255.89, 383.53, 255.89, 1.13),        # 枠の上下（右半分）
    (383.33, 24.89, 383.33, 255.89, 1.13),                                               # 枠の右
    (232.33, 24.89, 232.33, 34.89, 1.13), (232.33, 245.89, 232.33, 255.89, 1.13),        # 左右の境の短い線
    (241.13, 14.89, 303.53, 14.89, 1.13), (241.33, 14.89, 241.33, 34.89, 1.13),          # 家屋番号・建物の所在の欄
    (303.33, 14.89, 303.33, 24.89, 1.13), (241.13, 34.89, 383.53, 34.89, 1.13),
    (265.33, 14.89, 265.33, 34.89, 0.34),
    (240.13, 270.39, 383.53, 270.39, 1.13), (240.33, 255.89, 240.33, 270.39, 1.13),      # 申請人・縮尺の欄
    (383.33, 255.89, 383.33, 270.39, 1.13), (259.33, 255.89, 259.33, 270.39, 0.34),
    (349.09, 255.89, 349.09, 270.39, 0.34), (349.57, 255.89, 349.57, 270.39, 0.34),
    (359.33, 255.89, 359.33, 270.39, 0.34), (362.72, 268.35, 379.80, 257.93, 0.34),
    (345.57, 77.12, 345.57, 96.14, 0.37), (338.33, 87.57, 352.31, 87.57, 0.37),          # 方位
    (345.57, 77.12, 342.85, 81.55, 0.37), (342.85, 81.55, 346.83, 84.12, 0.37),
    (287.87, 132.14, 285.87, 132.14, 0.37), (287.87, 136.14, 285.87, 136.14, 0.37),      # 隣接地の境（短い線）
    (287.87, 159.64, 285.87, 159.64, 0.37), (321.87, 132.14, 323.87, 132.14, 0.37),
    (321.87, 159.64, 323.87, 159.64, 0.37), (301.67, 159.64, 301.50, 161.63, 0.37),
    (317.67, 159.64, 317.53, 161.63, 0.37),
    (287.87, 133.34, 289.47, 133.34, 0.37), (289.47, 132.14, 289.47, 133.34, 0.37),      # 距離0.8・0.6・0.8の寸法線と矢じり
    (287.87, 155.34, 289.47, 155.34, 0.37), (288.24, 132.95, 287.93, 133.27, 0.37),
    (289.47, 133.34, 289.16, 133.66, 0.37), (289.80, 132.45, 289.47, 132.14, 0.37),
    (289.48, 133.26, 289.16, 132.95, 0.37), (288.21, 154.99, 287.90, 155.31, 0.37),
    (289.44, 155.38, 289.13, 155.70, 0.37)]
SHEET_TEXTS = [                                   # (左端x, 中央y, 文字の大きさmm, 文字, 太字か)
    (243.7, 19.7, 3.88, '家屋番号'), (320.6, 20.9, 4.62, '建　物　図　面'), (358.6, 20.65, 4.62, '（イ）'),
    (243.7, 29.7, 3.88, '建物の所在'), (267.0, 30.2, 4.23, 'Ａ市Ｂ町四丁目６番地３'),
    (242.1, 262.95, 3.88, '申 請 人'), (350.6, 262.95, 3.88, '縮尺'), (351.1, 248.55, 3.53, '（単位：ｍ）'),
    (283.4, 133.25, 2.47, '0.8'), (282.2, 155.0, 3.0, '0.8'), (287.1, 128.8, 3.0, '0.6'), (275.3, 145.45, 3.0, '6-12'),
    (303.4, 126.8, 3.0, '道'), (326.0, 146.75, 3.0, '6-17'), (319.4, 163.85, 3.0, '6-7'), (307.6, 163.95, 3.0, '6-1'),
    (291.6, 163.95, 3.0, '6-5'), (275.1, 134.3, 3.0, '6-10'), (294.8, 157.3, 2.82, '6-3'),
    (368.3, 260.2, 3.53, '1'), (372.5, 265.6, 3.53, '500')]
SITE_A = (287.87, 132.14)                         # 本件土地の北西の角（A点）。1/500 で 1m＝2mm
FLOOR1 = [(289.47, 133.34), (317.87, 133.34), (317.87, 158.34), (305.77, 158.34), (305.77, 155.34), (289.47, 155.34)]


def zu09():
    """建物図面の記入の完成形。答案用紙（A3横）の右半分＝A4（210×297mm）を実寸で描く（2026-10-21 ユーザー指示）。"""
    setup_font()
    fig = plt.figure(figsize=((A4_X1 - A4_X0) / 25.4, A4_Y1 / 25.4), dpi=PX_PER_MM * 25.4)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(A4_X0, A4_X1)
    ax.set_ylim(A4_Y1, 0)
    ax.axis('off')
    pt = 72 / 25.4                                # 1mm＝2.835pt

    def L(x0, y0, x1, y1, lw, color=BLACK, **kw):
        ax.plot([x0, x1], [y0, y1], color=color, lw=lw, solid_capstyle='butt', **kw)

    def T(x, y, mm, s, color=BLACK, ha='left', weight='normal'):
        ax.text(x, y, s, ha=ha, va='center', fontsize=mm * pt, color=color, weight=weight)
    for r in ((56.28, 12.22, 406.88, 274.82), (57.08, 13.02, 406.08, 274.02)):     # 用紙の外枠（二重線）
        ax.add_patch(Rectangle((r[0], r[1]), r[2] - r[0], r[3] - r[1], fill=False, lw=1.13, ec=BLACK))
    for (x0, y0, x1, y1, lw) in SHEET_LINES:
        L(x0, y0, x1, y1, lw)
    ax.add_patch(Rectangle((SITE_A[0], SITE_A[1]), 34.0, 27.5, fill=False, lw=0.37, ec=BLACK))   # 本件土地 17.00×13.75m
    xs, ys = zip(*(FLOOR1 + FLOOR1[:1]))
    ax.plot(xs, ys, color=BLACK, lw=0.37, ls=(0, (1.0 * pt / 0.37, 0.5 * pt / 0.37)))         # 一棟の1階（点線、記載済み）
    for (x, y, mm, s) in SHEET_TEXTS:
        T(x, y, mm, s)
    # ---- 記入するもの（青） ----
    def W(e, s_):        # 壁の中心線の建物座標 (東, 南) → 用紙の mm。1階の外壁の西0.8・北0.6から
        return (SITE_A[0] + (0.8 + e) * 2, SITE_A[1] + (0.6 + s_) * 2)
    d = [W(Y1, X2), W(Y2, X2), W(Y2, 10.0), W(4.35, 10.0), W(4.35, X3), W(1.00, X3), W(1.00, 10.0), W(Y1, 10.0)]
    assert [tuple(round(v, 2) for v in p) for p in d] == [(289.47, 135.34), (300.07, 135.34), (300.07, 153.34), (298.17, 153.34),
                                                         (298.17, 155.34), (291.47, 155.34), (291.47, 153.34), (289.47, 153.34)]
    ax.add_patch(MPoly(d, closed=True, fill=False, lw=0.7, ec=INK, joinstyle='miter'))           # Dタイプ（実線）
    (x0, y0), (x1, _) = W(Y1, X2), W(Y4, X2)
    L(x0, y0, x1, y0, 0.7, color=INK, ls=(0, (5.0 * pt / 0.7, 1.0 * pt / 0.7, 1.0 * pt / 0.7, 1.0 * pt / 0.7)))  # 一棟の7階
    T(283.0, 178.5, 4.0, '建物の存する部分　７階', color=INK)
    T(284.3, 17.3, 2.4, '（略）', color=GRAY, ha='center')
    T(284.3, 21.8, 3.0, 'B町四丁目6番3の701', color=INK, ha='center')
    T(304.2, 258.6, 2.4, '（略）', color=GRAY, ha='center')
    T(304.2, 265.0, 3.88, '白石　恵', color=INK, ha='center')
    T(315.0, 6.5, 4.2, '建物図面（イ）の完成形', ha='center', weight='bold')
    T(315.0, 281.5, 2.9, '答案用紙（A3横）の右半分＝A4（210mm×297mm）の実寸。A4で印刷すると、縮尺1/500の大きさになる', ha='center')
    T(315.0, 286.5, 2.9, '黒：答案用紙に記載済み　青：記入するもの（家屋番号・申請人は（略）の印刷の欄に自分の答えを記入）', ha='center')
    save_fixed(fig, 'R8_dai22mon_zu09_tatemono_zumen_kansei')


# ======================================================================
# 図10：PSの欠けの誤り比較
# ======================================================================

def zoom_corner(ax, z, wrong):
    """Dタイプの南西の角（PS）の拡大。建物座標 東−0.4〜2.0、南8.8〜11.4。"""
    # 壁（壁厚0.12）を灰色の帯で
    for r_ in [rect(-0.06, 8.6, 0.06, 11.06), rect(-0.06, 10.94, 2.2, 11.06), rect(0.94, 9.94, 1.06, 11.0),
               rect(0.0, 9.94, 1.06, 10.06)]:
        ax.add_patch(MPoly([xy(p) for p in r_], closed=True, facecolor='#bdbdbd', edgecolor='none', zorder=1))
    if wrong:
        cut = rect(0.06, 10.06, 0.94, 10.94)       # PSの中の内法だけ
        z.poly(cut, color=RED, lw=2.4, fill=RED, alpha=0.25)
    else:
        cut = rect(0.06, 9.94, 1.06, 10.94)        # PSを囲む壁ごと
        z.poly(cut, color=GREEN, lw=2.4, fill=GREEN, alpha=0.25)
    fit(ax, [P(-0.7, 8.4), P(2.4, 11.6)], margin=0.02, pad_aspect=True)
    return cut


def zu10():
    fig, axes = new_figure('PS（共用部分）の欠けは、囲む壁ごと除く',
                           'Dタイプの内法の線は、PSを囲む壁のDタイプ側の面。PSの中の内法（0.88×0.88＝0.7744）だけを引くと、PSの壁がDタイプに入ってしまう。'
                           '\n正しくは1.00×1.00（南西の角なので、西と南は外壁の内側の面、北と東はPSの壁の外側の面）。MB・PSも同じく0.95×1.00を除く',
                           w=17, h=9.5, ncols=2)
    fig.subplots_adjust(top=0.86, bottom=0.17)
    zs = []
    for ax, wrong, title, col in [(axes[0], True, '誤り：PSの中だけ引く（49.67㎡）', RED),
                                  (axes[1], False, '正解：壁ごと引く（49.22㎡）', GREEN)]:
        z = Zu(ax, fontsize=13)
        cut = zoom_corner(ax, z, wrong)
        ax.set_title(title, fontsize=17, weight='bold', color=col)
        lab = '0.88' if wrong else '1.00'
        z.edge_label(cut[0], cut[1], lab, centroid(cut), fs=14, color=col)
        z.edge_label(cut[1], cut[2], lab, centroid(cut), fs=14, color=col)
        z.free_text(P(1.6, 9.2), 'Dタイプの床', fs=13)
        z.free_text(P(0.5, 11.35), '外壁（南）', fs=12, color=GRAY)
        z.callout(centroid(cut), 'PS', dirs=(45, 30, 60), dists=(60, 80), fs=13, color=col)
        zs.append(z)
    save(fig, zs, 'R8_dai22mon_zu10_ps_ayamari')


# ======================================================================
# 図11・図12：Dタイプ・Eタイプの求積図
# ======================================================================

def zu11():
    fig, axes = new_figure('Dタイプ（701）7階部分の床面積求積図（内法）',
                           '北の長方形 5.18×8.88＝45.9984　＋　南の帯 3.23×1.00＝3.2300　＝　49.2284 → 49.22㎡'
                           '\n（5.30−0.12＝5.18、10.00−0.12＝9.88、9.88−1.00＝8.88、5.18−1.00−0.95＝3.23）',
                           w=16, h=12)
    fig.subplots_adjust(top=0.90, bottom=0.14)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    north = rect(0.06, 1.06, 5.24, 9.94)
    south = rect(1.06, 9.94, 4.29, 10.94)
    z.poly(north, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(south, color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z.poly(D_C, color=GRAY, lw=1.0, ls=':')
    for b in (PS_C, MBD_C):
        z.poly(b, color=GRAY, lw=1.0)
        hatch(ax, b)
    z.poly(D_IN, color=BLACK, lw=2.4)
    fit(ax, D_C, margin=0.28, pad_aspect=True)
    dims(z, D_IN, ['5.18', '8.88', '0.95', None, '3.23', None, '1.00', '8.88'], fs=13)
    z.edge_label(D_IN[3], D_IN[4], '1.00', centroid(D_IN), fs=12, outward=False)
    z.edge_label(D_IN[5], D_IN[6], '1.00', centroid(D_IN), fs=12, outward=False)
    z.free_text(P(2.65, 5.0), '北の長方形\n5.18×8.88\n＝45.9984', fs=15)
    z.callout(P(2.67, 10.6), '南の帯\n3.23×1.00＝3.2300', dirs=(-90, -110, -70), dists=(45, 60), fs=12)
    z.callout(P(0.5, 10.5), 'PS（共用部分）', dirs=(200, 225, 180), fs=12)
    z.callout(P(4.8, 10.5), 'MB・PS（共用部分）', dirs=(-20, -45, 0), fs=12)
    z.free_text(P(2.65, -1.0), 'Dタイプ　7階部分　49.22㎡', fs=17, weight='bold')
    z.north_arrow()
    save(fig, [z], 'R8_dai22mon_zu11_D_kyuuseki')


def zu12():
    fig, axes = new_figure('Eタイプ（702）7階部分の床面積求積図（内法）',
                           '北の長方形 2.73×8.88＝24.2424　＋　南の帯 1.63×1.00＝1.6300　＝　25.8724 → 25.87㎡'
                           '\n（2.85−0.12＝2.73、1.75−0.06−0.06＝1.63。MB・PSの1.10×1.00を除く）',
                           w=16, h=12)
    fig.subplots_adjust(top=0.90, bottom=0.14)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    north = rect(5.36, 1.06, 8.09, 9.94)
    south = rect(5.36, 9.94, 6.99, 10.94)
    z.poly(north, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(south, color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z.poly(E_C, color=GRAY, lw=1.0, ls=':')
    z.poly(MBE_C, color=GRAY, lw=1.0)
    hatch(ax, MBE_C)
    z.poly(E_IN, color=BLACK, lw=2.4)
    fit(ax, E_C, margin=0.5, extra=[xy(P(1.5, 6)), xy(P(12, 6))], pad_aspect=True)
    dims(z, E_IN, ['2.73', '8.88', '1.10', None, '1.63', '9.88'], fs=13)
    z.edge_label(E_IN[3], E_IN[4], '1.00', centroid(E_IN), fs=12, outward=False)
    z.free_text(P(6.72, 5.0), '北の長方形\n2.73×8.88\n＝24.2424', fs=14)
    z.callout(P(6.17, 10.44), '1.63×1.00＝1.6300', dirs=(200, 225, 180), fs=12)
    z.callout(P(7.6, 10.5), 'MB・PS（共用部分）', dirs=(-20, -45, 0), fs=12)
    z.free_text(P(6.72, -1.0), 'Eタイプ　7階部分　25.87㎡', fs=17, weight='bold')
    z.north_arrow()
    save(fig, [z], 'R8_dai22mon_zu12_E_kyuuseki')


# ======================================================================
# 図13：合計の検算（76.16）
# ======================================================================

def zu13():
    fig, axes = new_figure('DとEを足しても76.16にならない。差は設け直した壁の面積',
                           '登記記録の76.16は、DとEの間の壁（MB・PSより北の8.88）を撤去していたときの床面積。'
                           '49.2284＋25.8724＋0.12×8.88（1.0656）＝76.1664 → 76.16\n'
                           'だからEを「76.16−49.22＝26.94」と引き算で出すと、設け直した壁の分だけ大きくなる（正しくは25.87）',
                           w=17, h=12)
    fig.subplots_adjust(top=0.90, bottom=0.15)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(D_IN, color=BLACK, lw=2.0, fill=BLUE, alpha=0.18)
    z.poly(E_IN, color=BLACK, lw=2.0, fill=ORANGE, alpha=0.25)
    z.poly(WALL, color=RED, lw=1.6, fill=RED, alpha=0.6)
    for b in (PS_C, MBD_C, MBE_C):
        hatch(ax, b)
    fit(ax, F7[:2] + [P(14.2, 11)], margin=0.06, extra=[xy(P(-1, 13)), xy(P(16, -1.5))], pad_aspect=True)
    z.free_text(P(2.65, 5.0), 'D\n49.2284', fs=16)
    z.free_text(P(6.72, 4.0), 'E\n25.8724', fs=15)
    z.callout(P(5.3, 7.5), '設け直した壁\n0.12×8.88＝1.0656', dirs=(-10, 10, -30), dists=(120, 150, 180), fs=13, color=RED)
    z.free_text(P(4.1, 12.3), '49.2284＋25.8724＝75.1008', fs=15)
    save(fig, [z], 'R8_dai22mon_zu13_kensan')


# ======================================================================
# 図14：各階平面図の完成形（答案用紙の第3欄の左半分・縮尺1/250）
# ======================================================================

def zu14():
    """各階平面図の完成形（答案用紙の第3欄の左半分）。"""
    sheet3('各階平面図の完成形（答案用紙の第3欄の左半分・縮尺1/250の実際の大きさ）', 'left', 'R8_dai22mon_zu14_kakukai_heimenzu')


# ======================================================================
# 図15：抵当権の行方
# ======================================================================

def zu15():
    fig, ax = fixed_figure('Eタイプの抵当権は「消滅の承諾」があって初めて消える', w=18, h=10.5,
                           rect_=(0.02, 0.10, 0.96, 0.78))
    for x, col, head, a, b in [(1, RED, '承諾がない場合', '701（D）：1番抵当権', '702（E）：1番抵当権が移される'),
                               (51, GREEN, '本問（承諾書あり）', '701（D）：1番抵当権', '702（E）：抵当権が消滅した旨を登記')]:
        rbox(ax, x, 22, 47, 66, col, alpha=0.07)
        ax.text(x + 23.5, 82, head, ha='center', va='center', fontsize=19, weight='bold', color=col)
        ax.text(x + 23.5, 70, '区分前　701：1番抵当権（蓮の花銀行）', ha='center', va='center', fontsize=14)
        ax.annotate('', xy=(x + 23.5, 56), xytext=(x + 23.5, 65), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
        ax.text(x + 23.5, 50, a, ha='center', va='center', fontsize=15)
        ax.text(x + 23.5, 40, b, ha='center', va='center', fontsize=15, weight='bold', color=col)
    ax.text(24.5, 29, '区分前の権利は区分後の各建物に移記\n（不動産登記規則第130条第1項）', ha='center', va='center', fontsize=13,
            linespacing=1.4)
    ax.text(74.5, 29, '抵当権者の承諾を証する情報を提供\n（不動産登記法第54条第3項で準用する第40条）', ha='center', va='center',
            fontsize=13, linespacing=1.4)
    ax.text(50, 10, '添付書類に「抵当権消滅承諾書」（蓮の花銀行の承諾書）を入れる。区分するだけなら承諾は要らない',
            ha='center', va='center', fontsize=15, weight='bold')
    fig.text(0.5, 0.045, '買主の安田結さんは、抵当権の付いていないEタイプを買える。Dタイプには1番抵当権が残る', ha='center', va='center',
             fontsize=14)
    save_fixed(fig, 'R8_dai22mon_zu15_teitouken')


# ======================================================================
# 図16：一棟の建物の表示（名称を書くので構造・床面積を省略）
# ======================================================================

def zu16():
    fig, ax = fixed_figure('一棟の建物の表示：名称を書くので、構造・床面積は書かない', w=18, h=8.2,
                           rect_=(0.02, 0.09, 0.96, 0.81))
    rbox(ax, 1, 22, 47, 66, RED, alpha=0.06)
    ax.text(24.5, 82, '誤り：9階分の床面積を計算して書く', ha='center', va='center', fontsize=18, weight='bold', color=RED)
    for y, t in [(68, '所在　A市B町四丁目6番地3'), (58, '名称　WKマンション'), (48, '構造　鉄筋コンクリート造陸屋根9階建'),
                 (38, '床面積　1階〜9階の9つ（平面図から求積）')]:
        ax.text(5, y, t, ha='left', va='center', fontsize=15, color=RED if y < 50 else BLACK)
    ax.text(24.5, 28, '本番の時間を使うだけで、書く必要がない', ha='center', va='center', fontsize=14, color=RED)
    rbox(ax, 51, 22, 47, 66, GREEN, alpha=0.07)
    ax.text(74.5, 82, '正解：所在と名称だけ', ha='center', va='center', fontsize=18, weight='bold', color=GREEN)
    for y, t in [(68, '所在　A市B町四丁目6番地3'), (58, '名称　WKマンション'), (48, '構造　省略'), (38, '床面積　省略')]:
        ax.text(55, y, t, ha='left', va='center', fontsize=15, color=GREEN if y < 50 else BLACK,
                weight='bold' if y < 50 else 'normal')
    ax.text(74.5, 28, '登記記録の抜粋も「床面積（省略）」', ha='center', va='center', fontsize=14, color=GREEN)
    ax.text(50, 12, '名称（ト）を申請情報の内容とするときは、一棟の建物の構造・床面積（ヘ）を省略できる（不動産登記令第3条第8号ヘ）',
            ha='center', va='center', fontsize=14, weight='bold')
    fig.text(0.5, 0.04, 'ただし、家屋番号を書かない申請（区分建物の表題登記など。同号ロに規定する場合）では省略できない',
             ha='center', va='center', fontsize=13)
    save_fixed(fig, 'R8_dai22mon_zu16_ittou_shouryaku')


# ======================================================================
# 図17：敷地権の割合
# ======================================================================

def zu17():
    fig, ax = fixed_figure('敷地権の割合は規約で70分の3・70分の2（床面積の割合ではない）', w=18, h=10,
                           rect_=(0.02, 0.10, 0.96, 0.78))
    rbox(ax, 1, 22, 47, 66, RED, alpha=0.06)
    ax.text(24.5, 82, '規約がなければ：床面積の割合', ha='center', va='center', fontsize=18, weight='bold', color=RED)
    ax.text(24.5, 68, '70分の5 を 49.22 ： 25.87 で分ける', ha='center', va='center', fontsize=15)
    ax.text(24.5, 56, 'Dタイプ　約70分の3.28', ha='center', va='center', fontsize=15)
    ax.text(24.5, 46, 'Eタイプ　約70分の1.72', ha='center', va='center', fontsize=15)
    ax.text(24.5, 32, '建物の区分所有等に関する法律\n第22条第2項本文・第14条第1項', ha='center', va='center', fontsize=13,
            linespacing=1.4, color=GRAY)
    rbox(ax, 51, 22, 47, 66, GREEN, alpha=0.07)
    ax.text(74.5, 82, '本問：規約で定めた割合', ha='center', va='center', fontsize=18, weight='bold', color=GREEN)
    ax.text(74.5, 68, '事実関係6の規約証明書', ha='center', va='center', fontsize=15)
    ax.text(74.5, 56, 'Dタイプ　70分の3', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(74.5, 46, 'Eタイプ　70分の2', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(74.5, 32, '同条第2項ただし書\n（合計は区分前と同じ70分の5）', ha='center', va='center', fontsize=13, linespacing=1.4,
            color=GRAY)
    ax.text(50, 10, '規約で決めた割合を登記するので、規約を設定したことを証する情報（規約証明書）を添付する（不動産登記令別表16の項添付情報欄ハ（2））',
            ha='center', va='center', fontsize=14, weight='bold')
    save_fixed(fig, 'R8_dai22mon_zu17_wariai')


# ======================================================================
# 図18：規約証明書
# ======================================================================

def zu18():
    fig, ax = fixed_figure('問4　規約証明書は「集会の議事録」か「全員の合意書」', w=18, h=10.5,
                           rect_=(0.02, 0.09, 0.96, 0.79))
    cols = [(1, GREEN, 'イ　議事録', ['区分所有者集会で規約を設定', '（第31条第1項の特別決議）', '議長と出席した区分所有者2人が署名',
                                         '（第42条第1項・第3項）']),
            (34, GREEN, 'ウ　合意書', ['区分所有者全員の書面又は', '電磁的方法による合意', '→ 書面による決議があった',
                                              'ものとみなす（第45条第2項）']),
            (67, RED, '本問では使えない：公正証書', ['最初に専有部分の全部を', '所有する者が設定する規約', '（第32条。分譲前の',
                                                   '分譲業者など）'])]
    for x, col, head, ls_ in cols:
        rbox(ax, x, 24, 31, 64, col, alpha=0.07)
        ax.text(x + 15.5, 82, head, ha='center', va='center', fontsize=17, weight='bold', color=col)
        for k, t in enumerate(ls_):
            ax.text(x + 15.5, 68 - 9 * k, t, ha='center', va='center', fontsize=13.5)
    ax.text(50, 13, 'ア　床面積：敷地権の割合は、規約がなければ専有部分の床面積の割合（第22条第2項本文・第14条第1項）',
            ha='center', va='center', fontsize=15, weight='bold', color=BLUE)
    fig.text(0.5, 0.04, '条文はすべて建物の区分所有等に関する法律。WKマンションは分譲済みで区分所有者が大勢いるので、集会の決議か全員の合意で規約を設定する',
             ha='center', va='center', fontsize=13.5)
    save_fixed(fig, 'R8_dai22mon_zu18_kiyaku_shoumei')


# ======================================================================
# 図19：本番で解く順番
# ======================================================================

def zu19():
    fig = plt.figure(figsize=(17, 8.5), dpi=100)
    setup_font()
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　求積と作図は後に回す', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.20, 0.96, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [('①', '問を全部読む', '区分建物区分\nと見当をつける', BLUE),
             ('②', '問1・問4', '第1欄・第4欄\n（知識だけ）', BLUE),
             ('③', '時系列メモ', '9月30日と\n10月18日', BLUE),
             ('④', '申請書の\n床面積以外', '目的・添付・\n税・敷地権', GREEN),
             ('⑤', 'DとEの求積', '内法・PSの欠け\n76.16で検算', RED),
             ('⑥', '建物図面・\n各階平面図', '一点鎖線と\n北の1.6', RED),
             ('⑦', '見直し', '原因の書き方\n割合・日付', GRAY)]
    w, h, gap = 12.2, 42, 1.8
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=16)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=13.5, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2 * (w + gap) - gap / 2, 76, '計算なしで書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 5 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 4 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '⑤は平面詳細図の寸法をDとEに分けて拾い、PSとMB・PSの欠けを壁ごと除く。⑥は7階の形が1階と違うことに気づけるかが勝負。'
             '\n①〜④を先に書いておけば、⑤⑥で時間が足りなくなっても、問1・問4と申請書の大部分の点は取れている',
             ha='center', va='center', fontsize=14.5, linespacing=1.6)
    check_fixed(fig, '解く順番')
    path = os.path.join(OUT, 'R8_dai22mon_zu19_toku_junban.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    zu08()
    zu09()
    zu10()
    zu11()
    zu12()
    zu13()
    zu14()
    zu15()
    zu16()
    zu17()
    zu18()
    zu19()
    print('重なり合計:', len(PROBLEMS))
