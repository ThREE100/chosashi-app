"""平成21年度 第22問（建物）の解説図20枚を、寸法から作図してPNGに書き出す。

`../prompt_H21_dai22mon_kaisetsuzu.md` の図1〜図20どおり（番号は記事の挿入順。画像の中に図番は入れない）。作図の共通部品は `tools/zu_helpers.py`。
- 座標値一覧表がない年度なので、敷地は〔配置図〕の筆界点間の距離（東西10.00×南北13.10の長方形）から描く
- 形は (東, 南) で持ち、P() で zu_helpers の複素数 (北 + 東i) に変換する
  - 敷地（図4〜図6）：原点＝3番4の北西の角（道路境界線と西の筆界の交点）
  - 各階（図10〜図14・図19）：原点＝建物の北西の角（壁の中心線）
- 断面（図9）：原点＝ロフトの床の西の端（押入の外壁の中心）、(東, 高さ)。Q() で (北＝高さ, 東) にする
- 図8（建物図面）と図19（各階平面図）は、答案用紙（その2）の問3の欄（A3横）の枠の中に、縮尺どおりの大きさで描く。
  枠・欄の位置は試験の答案用紙（`../touan_youshi/H21_dai22mon_touan_youshi_p2.png`。1400px幅なので1px＝0.3mm）の罫線から測った
  図7・図17・図15・図16・図18・図2・図3・図1・図20は座標を使わない整理図（固定配置）で、重なりの自動検査の対象外。目で見て確かめる
実行: python3 note-articles-Kijyutsu/H21/Q22/zu/draw_H21_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
INK = '#1a3a8f'   # 答案用紙への記入（濃い青）


def P(e, s):
    """(東, 南) の点を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def Q(e, h):
    """断面図の (東, 高さ) の点を複素数 (北＝高さ + 東i) にする。"""
    return complex(h, e)


def rect(e0, s0, e1, s1):
    return [P(e0, s0), P(e1, s0), P(e1, s1), P(e0, s1)]


def shift(pts, de, ds):
    return [p + complex(-ds, de) for p in pts]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def trunc2(v):
    return math.floor(v * 100 + 1e-9) / 100


def hatch(z, pts, color=GRAY, pattern='///'):
    z.ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch=pattern, edgecolor=color, lw=0, zorder=1))


def arrow(z, p, q, both=False):
    """寸法の矢印（p→q）。線分を重なり検査に登録する。"""
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<|-|>' if both else '-|>', lw=1.2, color=BLACK, mutation_scale=11))
    z.segments.append((xy(p), xy(q)))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=13, outward=True):
    """多角形の各辺に寸法（None は書かない）を書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


# ---- 固定配置の整理図（座標を使わない。0〜100の座標に箱と文字を置く） ----
def fixed_fig(title, caption, w=16, h=9):
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=23, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.13, 0.96, 0.74])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.text(0.5, 0.045, caption, ha='center', va='center', fontsize=15, linespacing=1.6)
    return fig, ax


def card(ax, x, y, w, h, color, alpha=0.14, lw=1.8, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.0,rounding_size=1.2', facecolor=color, alpha=alpha,
                                edgecolor='none'))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.0,rounding_size=1.2', facecolor='none', edgecolor=color,
                                lw=lw, ls=ls))


def put(ax, x, y, s, fs=15, color=BLACK, ha='left', va='top', weight='normal', ls=1.55, **kw):
    ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va=va, weight=weight, linespacing=ls, **kw)


def save_fixed(fig, name):
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('[固定配置の図]', path)


# ---- 各階の形（原点＝建物の北西の角の壁の中心、(東, 南)） ----
F1 = [P(0, 0), P(6.37, 0), P(6.37, 1.82), P(5.46, 1.82), P(5.46, 7.28), P(0, 7.28)]
F2 = [P(0, 0), P(4.55, 0), P(4.55, 1.82), P(5.46, 1.82), P(5.46, 6.37), P(0, 6.37)]
F3 = rect(0, 0, 4.55, 1.82)
R1_N, R1_S = rect(0, 0, 6.37, 1.82), rect(0, 1.82, 5.46, 7.28)
R2_N, R2_S = rect(0, 0, 4.55, 1.82), rect(0, 1.82, 5.46, 6.37)
FUKINUKE, BERANDA = rect(4.55, 0, 5.46, 1.82), rect(0, 6.37, 5.46, 7.28)
OSHIIRE, LOFT = rect(0, 0, 0.91, 1.82), rect(0.91, 0, 4.55, 1.82)
KOYANE = rect(5.46, 0, 6.37, 1.82)            # 玄関の張り出し（0.91×1.82）の上の小屋根
assert round(area(F1), 4) == 41.405 and trunc2(area(F1)) == 41.40 and round(area(F1) + 1e-9, 2) == 41.41
assert round(area(R1_N), 4) == 11.5934 and round(area(R1_S), 4) == 29.8116
assert round(area(F2), 4) == 33.124 and trunc2(area(F2)) == 33.12
assert round(area(R2_N), 4) == 8.281 and round(area(R2_S), 4) == 24.843
assert round(area(F3), 4) == 8.281 and trunc2(area(F3)) == 8.28
assert round(area(LOFT), 4) == 6.6248 and trunc2(area(LOFT)) == 6.62
assert round(5.46 * 6.37, 4) == 34.7802 and round(5.46 * 7.28, 4) == 39.7488
assert round(area(KOYANE), 4) == 1.6562 and round(area(KOYANE) / area(F1), 3) == 0.04   # 玄関の小屋根は約4％（30％未満）
assert round(area(R1_N) - area(KOYANE), 4) + round(area(KOYANE), 4) == round(area(R1_N), 4)

# ---- 敷地と建物の位置（原点＝3番4の北西の角、(東, 南)） ----
LOT = rect(0, 0, 10.00, 13.10)
T = 0.18                                  # 壁厚（問題文の注2）
DE, DS = 1.00 + T / 2, 1.10 + 2.00 + T / 2   # 壁の中心線：西の筆界から1.09、道路境界線から3.19
B1 = shift(F1, DE, DS)
assert round(area(LOT), 2) == 131.00
assert round(DE, 2) == 1.09 and round(DS, 2) == 3.19
E_OUT, S_OUT = DE + 6.37 + T / 2, DS + 7.28 + T / 2        # 東の外壁 7.55、南の外壁 10.56
assert round(10.00 - E_OUT, 2) == 2.45 and round(13.10 - S_OUT, 2) == 2.54
OUTER = [P(1.00, 3.10), P(E_OUT, 3.10), P(E_OUT, 5.10), P(6.64, 5.10), P(6.64, S_OUT), P(1.00, S_OUT)]   # 外壁の外側の形


def neighbors(z, fs=14):
    """隣接地の地番（〔配置図〕どおり）。"""
    for e, s, t in [(-2.2, 6.5, '3－3'), (12.2, 6.5, '3－5'), (5.0, 14.6, '3－11'), (-2.2, 14.6, '3－12'), (12.2, 14.6, '3－10')]:
        z.free_text(P(e, s), t, fs=fs, color=GRAY)


def lot_lines(z):
    """敷地と、筆界の延長（隣接地との境）。"""
    z.poly(LOT, color=BLACK, lw=2.2)
    z.line(P(0, 13.10), P(0, 16.0), color=BLACK, lw=1.4)
    z.line(P(10, 13.10), P(10, 16.0), color=BLACK, lw=1.4)
    z.line(P(-3.6, 13.10), P(0, 13.10), color=BLACK, lw=1.4)
    z.line(P(10, 13.10), P(13.6, 13.10), color=BLACK, lw=1.4)


def right_angles(z):
    for p, q, r in [(P(0, 0), P(10, 0), P(0, 13.1)), (P(10, 0), P(0, 0), P(10, 13.1)),
                    (P(0, 13.1), P(10, 13.1), P(0, 0)), (P(10, 13.1), P(0, 13.1), P(10, 0))]:
        z.right_angle(p, q, r, size=0.55)


# =====================================================================================
# 図1：時系列メモ（第1章）
# =====================================================================================
def zu01():
    fig, ax = fixed_fig('日付を並べる：原因の日付は工事完了の日、申請の期限は9月8日',
                        '1月以内の期間は、翌日（8月9日）から数え、1月後の応当日（9月9日）の前日に満了する。\n'
                        '引渡し（所有権の取得）の日は書かれていないが、8月8日より前ではないので、8月8日から数えても8月23日の申請は期限内',
                        w=16, h=8.6)
    ax.annotate('', xy=(97, 52), xytext=(3, 52), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=BLACK))
    days = {'8/8': 0, '8/10': 2, '8/23': 15, '9/8': 31}
    X = {k: 8 + v * 2.7 for k, v in days.items()}
    for k, x in X.items():
        ax.plot([x], [52], 'o', ms=11, color=RED if k == '9/8' else BLUE, zorder=5)
    ax.text(X['8/8'], 56.5, '8月8日', fontsize=17, weight='bold', ha='center', color=BLUE)
    ax.text(X['8/10'] + 6.5, 47.0, '8月10日', fontsize=17, weight='bold', ha='center', color=GRAY)
    ax.text(X['8/23'], 56.5, '8月23日', fontsize=17, weight='bold', ha='center', color=BLUE)
    ax.text(X['9/8'], 56.5, '9月8日', fontsize=17, weight='bold', ha='center', color=RED)
    card(ax, 3, 66, 33, 28, GREEN)
    put(ax, 4.5, 92, '工事完了（調査結果6）', fs=16, weight='bold', color=GREEN)
    put(ax, 4.5, 84, '原因及びその日付に書く日付\n「平成21年8月8日新築」\n（依頼の日や申請の日ではない）', fs=15)
    card(ax, 3, 8, 30, 30, GRAY)
    put(ax, 4.5, 36, '家野さんに依頼（前文）', fs=16, weight='bold', color=GRAY)
    put(ax, 4.5, 28, '原因の日付ではない\n土野さんが建築代金を払い、\n引渡しを受けた日は書かれていない\n（調査結果3）', fs=14)
    card(ax, 40, 66, 28, 28, BLUE)
    put(ax, 41.5, 92, '申請（答案用紙に印刷）', fs=16, weight='bold', color=BLUE)
    put(ax, 41.5, 84, '8月8日から数えて\n15日目。期限の前', fs=15)
    card(ax, 68, 8, 30, 36, RED)
    put(ax, 69.5, 42, '申請の期限（法第47条第1項）', fs=16, weight='bold', color=RED)
    put(ax, 69.5, 34, '所有権を取得した日から1月以内\n8月9日から数え始め、\n9月9日の前日の9月8日に満了', fs=14)
    save_fixed(fig, 'H21_dai22mon_zu01_jikeiretsu')


# =====================================================================================
# 図2：注の仕分け（第1章）
# =====================================================================================
def zu02():
    fig, ax = fixed_fig('番号のついたものは3種類：注・調査結果・書き添え',
                        '記事では「問題文の注3」「調査結果11」のように、どれのことかを必ず書き分ける。調査結果は注ではない',
                        w=16, h=9.4)
    cols = [
        (2, 38, BLUE, '問題文の（注）1〜8',
         '1　建物の測定値は柱の中心線から\n2　建物の壁厚はすべて18cm\n3　敷地区域から建物までの距離は\n　　すべて外壁まで\n4　距離の単位はメートル\n5　[ ]は地番、（ ）は筆界点間の距離\n6　建物図面1/500、各階平面図1/250\n7　訂正等の押印・字数の記載は不要\n8　本件申請は書面による'),
        (41, 40, GREEN, '〔調査結果〕1〜12',
         '1 居宅　2 建倉工務店の住所　3 代金支払済み・引渡し\n4 工事は建倉工務店（現場責任者は社員）\n5 附帯設備は丸田電気・中山設備\n6 工事完了は8月8日\n7 大屋根は洋かわらぶき、玄関の小屋根は\n　 ガルバリウム板ぶき（合金メッキ鋼板）\n8 玄関に吹抜け、階段室とは壁で隔てる\n9 ロフトは固定式ハシゴ階段\n10 ロフトの天井の高さは断面図のとおり\n11 道路幅1.80、後退線は中心線から2.00\n　　（後退部分の分筆は不要）\n12 北の方向は敷地北側道路と直角'),
        (83, 15, ORANGE, '〔ロフト平面図〕\nの書き添え', '※ただし、'),
    ]
    for x, w, c, t, body in cols:
        card(ax, x, 6, w, 88, c)
        put(ax, x + 1.5, 92, t, fs=16, weight='bold', color=c)
        put(ax, x + 1.5, 82 if x != 83 else 76, body, fs=13.5 if x != 83 else 15)
    ax.add_patch(Rectangle((84.7, 68.6), 2.6, 4.2, fill=False, ec=BLACK, lw=1.6))      # 四角にバツの記号（通し柱）
    ax.plot([84.7, 87.3], [68.6, 72.8], color=BLACK, lw=1.6)
    ax.plot([84.7, 87.3], [72.8, 68.6], color=BLACK, lw=1.6)
    put(ax, 87.9, 70.7, 'は通し柱。', fs=15, va='center')
    put(ax, 84.5, 56, '四角にバツの記号。\n材料が書かれていない\nこの問題では、構造を\n決める手がかりになる', fs=13.5, color=ORANGE)
    save_fixed(fig, 'H21_dai22mon_zu02_chuu_shiwake')


# =====================================================================================
# 図3：通し柱から木造（第1章）
# =====================================================================================
def zu03():
    fig, ax = fixed_fig('構成材料が書かれていない：通し柱の記号から木造と判断する',
                        '構造は「構成材料・屋根の種類・階数」で書く（不動産登記規則第114条）。材料は、平面図の通し柱の記号から木造とする',
                        w=16, h=8.4)
    card(ax, 2, 10, 28, 80, GRAY)
    put(ax, 3.5, 87, '問題文・調査結果', fs=17, weight='bold', color=GRAY)
    put(ax, 3.5, 76, '屋根は洋かわらぶき・\nガルバリウム板ぶき\n（調査結果7）\n\n階数は断面図と\n平面図から\n\n構成材料は…\n木造とも鉄骨造とも\n書かれていない', fs=15)
    ax.annotate('', xy=(36, 50), xytext=(30.5, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
    card(ax, 36, 10, 28, 80, ORANGE)
    put(ax, 37.5, 87, '〔ロフト平面図〕の下', fs=17, weight='bold', color=ORANGE)
    put(ax, 37.5, 76, '※ただし、', fs=15)
    ax.add_patch(Rectangle((44.6, 71.6), 3.0, 5.0, fill=False, ec=BLACK, lw=1.8))      # 四角にバツの記号（通し柱）
    ax.plot([44.6, 47.6], [71.6, 76.6], color=BLACK, lw=1.8)
    ax.plot([44.6, 47.6], [76.6, 71.6], color=BLACK, lw=1.8)
    put(ax, 48.3, 74.1, 'は通し柱。', fs=15, va='center')
    put(ax, 37.5, 62, '平面図の外壁の角や\n壁の途中にある\n四角にバツの記号\n（1階にも2階にも）', fs=15)
    ax.annotate('', xy=(70, 50), xytext=(64.5, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
    card(ax, 70, 10, 28, 80, GREEN)
    put(ax, 71.5, 87, '通し柱は木造の柱', fs=17, weight='bold', color=GREEN)
    put(ax, 71.5, 76, '1階から2階まで\n1本で通した、\n木造の軸組の柱\n\n→ 構成材料は木造\n\n構造は\n「木造かわら…3階建」\nの形で書く', fs=15)
    save_fixed(fig, 'H21_dai22mon_zu03_tooshibashira')


# =====================================================================================
# 図4：敷地の形（作図チェック用）
# =====================================================================================
def zu04():
    fig, axes = new_figure('3番4の敷地の形（作図チェック用。辺長は建物図面には書かない）',
                           '〔配置図〕：東西10.00×南北13.10の長方形。4つの角に直角の記号がある。問題文の注5：（　）の数字は筆界点間の距離。\n'
                           '辺がそろい角が直角なので、F-789SGの複素数モードは使わない。面積は10.00×13.10＝131.00㎡',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT, margin=0.10, extra=[xy(P(-5.5, -3.6)), xy(P(16.5, 16.2))], pad_aspect=True)
    z.poly(LOT, color=BLACK, lw=0, fill=BLUE, alpha=0.08, check=False)
    lot_lines(z)
    z.line(P(-3.6, -1.80), P(13.6, -1.80), color=BLACK, lw=1.6)
    z.line(P(-3.6, 0), P(0, 0), color=BLACK, lw=1.6)
    z.line(P(10, 0), P(13.6, 0), color=BLACK, lw=1.6)
    right_angles(z)
    z.north_arrow()
    c = centroid(LOT)
    z.edge_label(P(0, 0), P(10, 0), '（10.00）', c, fs=14, outward=False)
    z.edge_label(P(0, 13.1), P(10, 13.1), '（10.00）', c, fs=14)
    z.edge_label(P(0, 0), P(0, 13.1), '（13.10）', c, fs=14, ts=(0.62, 0.72, 0.5))
    z.edge_label(P(10, 0), P(10, 13.1), '（13.10）', c, fs=14, ts=(0.62, 0.72, 0.5))
    z.free_text(P(5.0, 6.5), '3－4\n10.00×13.10＝131.00㎡', fs=16)
    z.free_text(P(5.0, -0.9), '道　路（幅1.80）', fs=14, color=GRAY)
    neighbors(z)
    save(fig, [z], 'H21_dai22mon_zu04_shikichi_kakunin')


# =====================================================================================
# 図5：道路後退線は筆界ではない
# =====================================================================================
def zu05():
    fig, axes = new_figure('道路後退線は筆界ではない：建物図面の北の距離は道路境界線から測る',
                           '〔配置図〕：道路の幅1.80、中心線は道路境界線から0.90北。道路後退線は中心線から2.00（道路境界線から1.10南）。\n'
                           '後退部分は分筆しない（調査結果11）ので、筆界は道路境界線のまま。距離は 1.10＋2.00＝3.10（問題文の注3：外壁まで）',
                           w=16, h=13)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT, margin=0.10, extra=[xy(P(-5.5, -3.6)), xy(P(16.5, 16.2))], pad_aspect=True)
    z.poly(LOT, color=BLACK, lw=0, fill=BLUE, alpha=0.08, check=False)
    lot_lines(z)
    z.line(P(-3.6, -1.80), P(10.6, -1.80), color=BLACK, lw=1.6)
    z.line(P(-3.6, 0), P(0, 0), color=BLACK, lw=1.6)
    z.line(P(10, 0), P(10.6, 0), color=BLACK, lw=1.6)
    z.line(P(-3.6, -0.90), P(10.6, -0.90), color=GRAY, lw=1.3, ls='-.')
    z.line(P(0, 1.10), P(10, 1.10), color=RED, lw=1.6, ls='--')
    z.poly(B1, color=GRAY, lw=1.4, ls=':')
    z.north_arrow()
    arrow(z, P(11.6, -1.80), P(11.6, 0), both=True)
    arrow(z, P(11.6, 0), P(11.6, 1.10), both=True)
    arrow(z, P(13.8, -0.90), P(13.8, 1.10), both=True)
    z.line(P(10.6, -1.80), P(14.3, -1.80), color=GRAY, lw=0.8)
    z.line(P(10.6, -0.90), P(14.3, -0.90), color=GRAY, lw=0.8)
    z.line(P(10.6, 0), P(14.3, 0), color=GRAY, lw=0.8)
    z.line(P(10.0, 1.10), P(14.3, 1.10), color=GRAY, lw=0.8)
    z.free_text(P(11.6, -1.35), '1.80', fs=12, ha='left', offsets=((8, 0), (10, 0)))
    z.free_text(P(11.6, 0.55), '1.10', fs=12, ha='left', offsets=((8, 0), (10, 0)))
    z.free_text(P(13.8, 0.3), '2.00', fs=12, ha='left', offsets=((8, 0), (10, 0)))
    arrow(z, P(1.6, 1.10), P(1.6, 3.10))
    arrow(z, P(3.2, 0), P(3.2, 3.10))
    z.free_text(P(1.6, 2.1), '2.00', fs=12, ha='right', offsets=((-8, 0), (-10, 0)))
    z.free_text(P(3.2, 2.55), '1.10＋2.00＝3.10', fs=13, color=RED, ha='left', offsets=((10, 0), (12, 0)))
    z.free_text(P(4.0, -2.55), '道　路（幅1.80）', fs=14, color=GRAY)
    z.free_text(P(-3.5, -1.35), '道路の中心線', fs=12, color=GRAY, ha='left')
    z.free_text(P(-3.5, 0.55), '道路境界線＝筆界', fs=12, color=BLUE, ha='left')
    z.free_text(P(3.7, 1.55), '道路後退線（筆界ではない）', fs=12, color=RED, ha='left')
    z.free_text(P(4.2, 11.6), '3－4', fs=15)
    z.free_text(P(3.8, 7.0), '建物の位置（点線）', fs=12, color=GRAY)
    neighbors(z)
    save(fig, [z], 'H21_dai22mon_zu05_koutai_sen')


# =====================================================================================
# 図6：建物が敷地に収まるか（所在の確認）
# =====================================================================================
def zu06():
    fig, axes = new_figure('建物は3番4の中に収まるか（所在の確認）：外壁と筆界の間が全部プラス',
                           '建物の寸法は柱の中心から、距離は外壁まで（問題文の注1・注3）。壁厚18cm（注2）なので外壁の面は中心線から0.09外。\n'
                           '東西：1.00＋（6.37＋0.18）＋2.45＝10.00　　南北：3.10＋（7.28＋0.18）＋2.54＝13.10 → 所在は「A市B町二丁目3番地4」だけ',
                           w=16, h=13)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT, margin=0.10, extra=[xy(P(-4.5, -3.0)), xy(P(14.5, 16.2))], pad_aspect=True)
    z.poly(LOT, color=BLACK, lw=2.2, fill=BLUE, alpha=0.06)
    z.line(P(0, 13.10), P(0, 16.0), color=BLACK, lw=1.4)
    z.line(P(10, 13.10), P(10, 16.0), color=BLACK, lw=1.4)
    z.poly(OUTER, color=BLACK, lw=2.4)
    z.north_arrow()
    arrow(z, P(0, 4.0), P(1.00, 4.0), both=True)
    arrow(z, P(E_OUT, 4.0), P(10.0, 4.0), both=True)
    arrow(z, P(2.2, 0), P(2.2, 3.10), both=True)
    arrow(z, P(2.2, S_OUT), P(2.2, 13.10), both=True)
    arrow(z, P(1.0, 9.6), P(E_OUT - 0.91, 9.6), both=True)
    z.free_text(P(0.5, 4.0), '1.00', fs=12, offsets=((0, 16), (0, -16)))
    z.free_text(P(8.8, 4.0), '2.45', fs=13, color=RED, weight='bold', offsets=((0, 16), (0, -16)))
    z.free_text(P(2.2, 1.55), '3.10', fs=13, ha='left', offsets=((10, 0), (12, 0)))
    z.free_text(P(2.2, 11.85), '2.54', fs=13, color=RED, weight='bold', ha='left', offsets=((10, 0), (12, 0)))
    z.free_text(P(3.8, 9.6), '6.55（外壁から外壁）', fs=12, offsets=((0, 12), (0, -12)))
    z.free_text(P(3.5, 7.4), '1階の外形\n（外壁の外側）', fs=13, color=GRAY)
    z.free_text(P(5.0, 12.5), '3－4', fs=14)
    z.free_text(P(5.0, -0.9), '道　路', fs=14, color=GRAY)
    z.line(P(-3.6, 0), P(0, 0), color=BLACK, lw=1.6)
    z.line(P(10, 0), P(13.6, 0), color=BLACK, lw=1.6)
    z.line(P(-3.6, 13.10), P(0, 13.10), color=BLACK, lw=1.4)
    z.line(P(10, 13.10), P(13.6, 13.10), color=BLACK, lw=1.4)
    neighbors(z, fs=13)
    save(fig, [z], 'H21_dai22mon_zu06_shozai_kakunin')


# =====================================================================================
# 図7：建物図面に書くもの・書かないもの（固定配置）
# =====================================================================================
def zu07():
    fig, ax = fixed_fig('建物図面に書くもの・書かないもの',
                        '建物図面は、建物の敷地と1階の位置・形を示す図（不動産登記規則第82条）。建物の寸法・求積は各階平面図（第83条）の仕事',
                        w=16, h=9)
    card(ax, 2, 8, 47, 86, GREEN)
    put(ax, 3.5, 91, '書くもの', fs=19, weight='bold', color=GREEN)
    put(ax, 3.5, 82, '方位（北の向き）\n縮尺　500分の1（印刷済み）\n敷地の地番「3－4」と敷地の形\n隣接地の地番（3－3・3－5・3－10・\n　3－11・3－12）と北の道路\n1階の形（壁の中心線）\n北の道路境界線から外壁まで　3.10\n西の筆界から外壁まで　1.00（2か所）\n建物の所在　A市B町二丁目3番地4\n申請人　土野一郎（（略）の印刷なし）', fs=15)
    card(ax, 51, 8, 47, 86, RED)
    put(ax, 52.5, 91, '書かないもの', fs=19, weight='bold', color=RED)
    put(ax, 52.5, 82, '敷地の辺長（10.00・13.10）\n　→ 作図チェック用の数字\n道路後退線\n　→ 筆界ではない。距離の起点にしない\n建物の辺長（6.37・7.28など）\n　→ 各階平面図に書く\n主である建物・附属建物の別と符号\n　→ 附属建物がないので不要\n家屋番号\n　→ 登記所が付ける。欄は空けておく', fs=15)
    save_fixed(fig, 'H21_dai22mon_zu07_zumen_kisai')


# =====================================================================================
# 答案用紙（その2）の問3の欄：図8（建物図面）と図19（各階平面図）で共通の枠（mm）
# =====================================================================================
PX = 0.3                                              # 1px＝0.3mm（A3横の答案用紙の画像は1400px幅）
PAGE_H = 297.3


def pxm(x, y):
    """答案用紙の画像のピクセル位置 (x, y)（y は下向き）を、用紙の mm（x：右向き、y：上向き）にする。"""
    return x * PX, PAGE_H - y * PX


FR_L, FR_T = pxm(80.5, 144.5)
FR_R, FR_B = pxm(1153.0, 786.5)
MID = 615.5 * PX                                     # 中央の仕切り
SH_X0, SH_X1, SH_Y0, SH_Y1 = 14.0, 410.0, 16.0, 288.0   # 画像に入れる範囲（mm）


def M(x, y):
    """用紙の mm の位置（x：右向き、y：上向き）を zu_helpers の複素数（北＝縦、東＝横）にする。"""
    return complex(y, x)


# 建物図面（縮尺1/500、1m ＝ 2mm）：敷地の北西の角（道路境界線と西の筆界の交点）を用紙の (X0, Y0) mm に置く
S_X0, S_Y0 = 252.0, 204.0


def S500(e, s):
    """敷地の (東, 南) [m] を用紙の mm に置く。"""
    return M(S_X0 + 2 * e, S_Y0 - 2 * s)


# 各階平面図（縮尺1/250、1m ＝ 4mm）：建物の北西の角（壁の中心線）を用紙の (x0, y0) mm に置く
def S250(p, x0, y0):
    """建物の点 P(東, 南) [m]（zu_helpers の複素数）を用紙の mm に置く。"""
    return M(x0 + 4 * p.imag, y0 + 4 * p.real)


def sheet_figure(title):
    setup_font()
    w_mm, h_mm = SH_X1 - SH_X0, SH_Y1 - SH_Y0
    fig = plt.figure(figsize=(22, 22 * h_mm / w_mm), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    z = Zu(ax, fontsize=10)
    ax.set_xlim(SH_X0, SH_X1)
    ax.set_ylim(SH_Y0, SH_Y1)
    ax.text((SH_X0 + SH_X1) / 2, 281.0, title, ha='center', va='center', fontsize=21, weight='bold')
    return fig, ax, z


def sheet3(ax, kaoku='', shozai='', seisha='', shinseinin=''):
    """答案用紙（その2）の問3の欄の印刷（試験の答案用紙どおり）と記入（家屋番号は空欄。建物の所在・作成者・申請人を記入）。"""
    def rc(x0, y0, x1, y1, lw=1.3):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, lw=lw, ec=BLACK, zorder=3))

    def ln(x0, y0, x1, y1, lw=1.0, **kw):
        ax.plot([x0, x1], [y0, y1], color=kw.pop('color', BLACK), lw=lw, zorder=3, **kw)

    def txt(x, y, s, fs=12, ha='center', **kw):
        ax.text(x, y, s, ha=ha, va='center', fontsize=fs, zorder=4, family='Noto Serif CJK JP', **kw)

    rc(FR_L, FR_B, FR_R, FR_T, lw=1.6)                       # 図を描く枠
    ln(MID, FR_T, MID, FR_T - 4.5, lw=1.6)                   # 中央の仕切り（上下の短い線だけが印刷）
    ln(MID, FR_B, MID, FR_B + 4.5, lw=1.6)
    txt(*pxm(92, 114), '問3', fs=13, ha='left', weight='bold')
    txt(*pxm(360, 125), '各　階　平　面　図', fs=15)
    txt(*pxm(1000, 120), '建　物　図　面', fs=15)
    xa, ya = pxm(642.5, 100)
    xb, yb = pxm(859.5, 144.5)
    rc(xa, yb, xb, ya)                                       # 家屋番号の箱（枠の外の上）
    ln(pxm(736, 0)[0], yb, pxm(736, 0)[0], ya)
    txt(*pxm(689, 122), '家 屋 番 号', fs=11)
    xc, yc = pxm(1153.0, 185)
    rc(xa, yc, xc, yb)                                       # 建物の所在の欄（枠の中の上端）
    ln(pxm(736, 0)[0], yc, pxm(736, 0)[0], yb)
    txt(*pxm(689, 164), '建物の所在', fs=11)
    # 作成者・縮尺 1/250
    x0, y0 = pxm(81, 843.5)
    x1, y1 = pxm(583, 789)
    rc(x0, y0, x1, y1)
    for px_ in (166, 463, 502):
        ln(pxm(px_, 0)[0], y0, pxm(px_, 0)[0], y1)
    txt(*pxm(124, 817), '作 成 者', fs=11)
    rc(*pxm(418, 812), *pxm(459, 795))
    txt(*pxm(438.5, 803.5), '職印', fs=9)
    txt(*pxm(460, 828), '（平成21年8月23日作成）', fs=10, ha='right')
    txt(*pxm(482.5, 815), '縮尺', fs=10)
    ln(*pxm(510, 833), *pxm(576, 797), lw=0.9)
    txt(*pxm(531, 806), '1', fs=10)
    txt(*pxm(559, 823), '250', fs=10)
    # 申請人・縮尺 1/500
    x0, y0 = pxm(653, 838)
    x1, y1 = pxm(1154, 784.5)
    rc(x0, y0, x1, y1)
    for px_ in (738, 1036, 1078):
        ln(pxm(px_, 0)[0], y0, pxm(px_, 0)[0], y1)
    txt(*pxm(695, 813), '申 請 人', fs=11)
    txt(*pxm(1057, 812), '縮尺', fs=10)
    ln(*pxm(1085, 830), *pxm(1148, 793), lw=0.9)
    txt(*pxm(1103, 802), '1', fs=10)
    txt(*pxm(1128, 820), '500', fs=10)
    # 記入（濃い青）
    if kaoku:
        ax.text(*pxm(745, 122), kaoku, ha='left', va='center', fontsize=12, color=INK, zorder=4)
    if shozai:
        ax.text(*pxm(748, 164), shozai, ha='left', va='center', fontsize=12, color=INK, zorder=4)
    if seisha:
        ax.text(*pxm(176, 817), seisha, ha='left', va='center', fontsize=12, color=INK, zorder=4)
    if shinseinin:
        ax.text(*pxm(750, 811), shinseinin, ha='left', va='center', fontsize=12, color=INK, zorder=4)


def zumen_content(z):
    """右半分：建物図面（縮尺1/500、1m ＝ 2mm）。1階の位置・形状と、筆界からの距離（小数第1位）、地番・道路・方位。"""
    for e in (0.0, 10.0):                                               # 敷地の西・東の筆界と、その延長（隣接地との境）
        z.line(S500(e, 0), S500(e, 13.1 + 3.5), lw=1.2)
    for s, e0, e1 in ((0, -4.0, 14.0), (13.1, -4.0, 14.0)):             # 道路境界線と南の筆界
        z.line(S500(e0, s), S500(e1, s), lw=1.2)
    z.line(S500(-4.0, -1.8), S500(14.0, -1.8), lw=1.2)                  # 道路の向こう側の線
    z.poly([S500(0, 0), S500(10, 0), S500(10, 13.1), S500(0, 13.1)], lw=2.0)
    b = [P(1.0 + 0.09 + e, 3.10 + 0.09 + s) for e, s in [(0, 0), (6.37, 0), (6.37, 1.82), (5.46, 1.82), (5.46, 7.28), (0, 7.28)]]
    z.poly([S500(p.imag, -p.real) for p in b], lw=2.2)                    # 1階の形（壁の中心線）
    z.north_arrow(pos=(0.86, 0.66), length=0.05)
    dim_line(z, S500(1.7, 0), S500(1.7, 3.10), '3.10', fs=10, offsets=((14, 0), (-14, 0)))
    dim_line(z, S500(0, 3.19 + 0.7), S500(1.00, 3.19 + 0.7), '1.00', fs=10, dirs=(140, 160, 120))
    dim_line(z, S500(0, 3.19 + 6.2), S500(1.00, 3.19 + 6.2), '1.00', fs=10, dirs=(-140, -120, -160))
    z.free_text(S500(5.0, 11.6), '3－4', fs=11)
    for e, s, t in [(-2.6, 6.5, '3－3'), (12.6, 6.5, '3－5'), (5.0, 15.3, '3－11'), (-2.6, 15.3, '3－12'), (12.6, 15.3, '3－10')]:
        z.free_text(S500(e, s), t, fs=10)
    z.free_text(S500(15.6, -0.9), '道路', fs=10, ha='left')
    z.free_text(M(S_X0 + 40, 68.0), '（単位：m）', fs=9)


def dim_line(z, p, q, text, color=BLACK, ls='-', dirs=None, offsets=None, fs=15):
    """寸法線（両矢印）と数値。短くて文字が入らない寸法は dirs を指定して引き出し線で外に書く。"""
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<->', lw=1.3, color=color, ls=ls, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=fs - 1, dists=(30, 40, 50, 65, 80, 100), color=color)
    return z.free_text(m, text, fs=fs, color=color, offsets=offsets or ((16, 0), (-16, 0), (0, 14), (0, -14)))


def zu08():
    """建物図面の完成形：問3の欄の右半分。用紙の大きさと縮尺1/500の実際の大きさで描く。"""
    fig, ax, z = sheet_figure('建物図面の完成形（答案用紙（その2）の問3の欄の右半分・縮尺1/500の実際の大きさ）')
    sheet3(ax, shozai='A市B町二丁目3番地4', shinseinin='土野一郎')
    zumen_content(z)
    ax.text(212.0, 35.0, '筆界から外壁までの距離は小数第1位（問題文の注3）。北の3.10は道路後退線ではなく道路境界線から。敷地の辺長・建物の辺長は書かない',
            ha='center', va='center', fontsize=13)
    ax.text(212.0, 27.5, '家屋番号は登記所が付けるので空欄。申請人の欄は（略）の印刷がないので氏名を書く。左半分の各階平面図は第5章で描く',
            ha='center', va='center', fontsize=12, color=GRAY)
    save(fig, [z], 'H21_dai22mon_zu08_tatemono_zumen')


# =====================================================================================
# 図9：ロフトは何階？
# =====================================================================================
SLOPE = (1.20 - 0.80) / 0.91


def roof_h(e):
    return 2.00 - SLOPE * abs(e - 2.73)


assert round(roof_h(0), 2) == 0.80 and round(roof_h(0.91), 2) == 1.20 and round(roof_h(4.55), 2) == 1.20
assert round(roof_h(2.73), 2) == 2.00 and round(roof_h(5.46), 2) == 0.80
E15 = 2.73 - (2.00 - 1.50) / SLOPE           # 天井の高さが1.5mになる位置 1.5925
assert round(E15, 4) == 1.5925


def zu09():
    fig, axes = new_figure('ロフトは何階？　天井の最高部で1.5mを判定する（断面の模式図）',
                           '天井の高さ1.5m未満の屋階（特殊階）は階数・床面積に入れない（準則第81条第4項・第82条第1号）。\n'
                           'このロフトは最高部2.00で1.5m以上 → 特殊階ではない → 3階に数え、押入も含めて4.55×1.82＝8.28㎡（1室の一部が低くても算入）',
                           w=16, h=8.6)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, [Q(-3.0, -0.9), Q(8.9, 3.1)], margin=0.03, pad_aspect=True)
    roof = [Q(-0.35, roof_h(0) - 0.35 * SLOPE), Q(2.73, 2.00), Q(5.81, roof_h(5.46) - 0.35 * SLOPE)]
    z.poly(roof, color=BLACK, lw=2.6, closed=False)
    loft_area = [Q(0, 0), Q(0, 0.80), Q(2.73, 2.00), Q(4.55, 1.20), Q(4.55, 0)]
    z.poly(loft_area, color=BLACK, lw=0, fill=GREEN, alpha=0.14, check=False)
    high = [Q(E15, 1.5), Q(2.73, 2.00), Q(2.73 + (2.73 - E15), 1.5)]
    z.poly(high, color=GREEN, lw=0, fill=GREEN, alpha=0.30, check=False)
    z.line(Q(0, 0), Q(5.46, 0), color=BLACK, lw=2.4)                  # ロフトの床（2階の天井）
    z.line(Q(0, -0.6), Q(0, 0.80), color=BLACK, lw=2.4)               # 西の外壁
    z.line(Q(0.91, 0), Q(0.91, 1.20), color=BLACK, lw=1.6)            # 押入とロフトの境
    z.line(Q(4.55, -0.6), Q(4.55, 1.20), color=BLACK, lw=1.6)         # ロフトの東の端（吹抜との境）
    z.line(Q(5.46, -0.6), Q(5.46, 0.80), color=BLACK, lw=2.4)         # 東の外壁
    z.line(Q(-0.6, 1.5), Q(6.1, 1.5), color=RED, lw=1.8, ls='--')
    z.free_text(Q(6.1, 1.5), '天井の高さ1.5m', fs=13, color=RED, ha='left', offsets=((8, 0), (8, 10)))
    for e, t_, off, ha in [(0.14, '0.80', (-10, 0), 'right'), (1.05, '1.20', (8, 0), 'left'), (2.87, '2.00', (8, -12), 'left'),
                           (4.41, '1.20', (-8, 0), 'right')]:
        arrow(z, Q(e, 0), Q(e, roof_h(e) - 0.02), both=True)
        tx = e if e != 0.14 else -0.05
        z.free_text(Q(tx, roof_h(e) / 2), t_, fs=13, ha=ha, offsets=(off, (off[0] * 1.5, off[1])))
    z.free_text(Q(0.455, 0.22), '押入', fs=12)
    z.free_text(Q(3.7, 0.30), 'ロフト（3階）', fs=14, weight='bold')
    z.free_text(Q(5.0, -0.3), '吹抜', fs=12, color=GRAY)
    z.free_text(Q(2.3, -0.35), '2階（ウォークインクローゼット）', fs=12, color=GRAY)
    z.free_text(Q(-2.9, 2.55), '誤り：「ロフト」だから数えない\n→ 2階建（3階の8.28が抜ける）', fs=14, color=RED, ha='left')
    z.free_text(Q(5.0, 2.65), '正解：最高部2.00は1.5m以上\n→ 特殊階ではない → 3階建', fs=14, color=GREEN, ha='left')
    save(fig, [z], 'H21_dai22mon_zu09_loft_ayamari_hikaku')


def zu10():
    fig, axes = new_figure('1階の求積図（2つの長方形に分けて足す）',
                           '6.37×1.82＝11.5934（北の帯、北東の角の玄関の張り出しを含む）＋ 5.46×5.46＝29.8116（南の本体）\n'
                           '＝ 41.4050 → 41.40㎡（1平方メートルの100分の1未満は切り捨て。四捨五入の41.41ではない）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, extra=[xy(P(2.73, 9.6))], pad_aspect=True)
    z.poly(R1_N, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(R1_S, color=GREEN, lw=0, fill=GREEN, check=False)
    z.line(P(0, 1.82), P(5.46, 1.82), color=GRAY, lw=1.2, ls='--')
    z.poly(F1, color=BLACK, lw=2.4)
    z.north_arrow()
    dims(z, F1, ['6.37', '1.82', None, '5.46', '5.46', '7.28'])
    z.free_text(P(5.915, 1.82), '0.91', fs=14, offsets=((0, -16), (0, -20)))
    z.free_text(P(3.2, 0.91), '6.37×1.82＝11.5934', fs=14, color=BLUE)
    z.free_text(P(2.73, 4.55), '5.46×5.46\n＝29.8116', fs=16, color=GREEN)
    z.free_text(P(2.73, 9.0), '合計 41.4050 → 41.40㎡', fs=17, weight='bold')
    save(fig, [z], 'H21_dai22mon_zu10_1kai_kyuuseki')


# =====================================================================================
# 図11：2階で床面積に入れるもの・入れないもの
# =====================================================================================
def zu11():
    fig, axes = new_figure('2階の床面積：入れるもの・入れないもの',
                           '階段室は壁で囲まれていれば各階の床面積に入れる（準則第82条第6号）。吹抜は上の階に入れない（第8号）。\n'
                           'ベランダは壁と屋根に囲まれていない屋外。階段室の位置・大きさは模式',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, extra=[xy(P(-1.0, 9.8)), xy(P(9.5, -1.0))], pad_aspect=True)
    z.poly(F1, color=GRAY, lw=1.3, ls='--')
    z.poly(R2_N, color=BLUE, lw=0, fill=BLUE, alpha=0.20, check=False)
    z.poly(rect(0, 1.82, 3.0, 3.64), color=BLUE, lw=0, fill=BLUE, alpha=0.20, check=False)
    z.poly(rect(3.0, 1.82, 5.46, 3.64), color=GREEN, lw=0, fill=GREEN, alpha=0.30, check=False)
    z.poly(rect(0, 3.64, 5.46, 6.37), color=BLUE, lw=0, fill=BLUE, alpha=0.20, check=False)
    hatch(z, FUKINUKE, color=RED)
    hatch(z, BERANDA, color=RED)
    z.poly(F2, color=BLACK, lw=2.4)
    z.line(P(0, 1.82), P(5.46, 1.82), color=GRAY, lw=1.0)
    z.line(P(0, 3.64), P(5.46, 3.64), color=GRAY, lw=1.0)
    z.line(P(3.0, 1.82), P(3.0, 3.64), color=GRAY, lw=1.0)
    z.north_arrow()
    z.free_text(P(2.27, 0.91), 'ウォークインクローゼット', fs=13)
    z.free_text(P(1.5, 2.73), '多目的スペース', fs=12)
    z.free_text(P(4.23, 2.73), '階段室', fs=14, weight='bold', color=GREEN)
    z.free_text(P(2.73, 5.0), '洋室・洋室', fs=14)
    z.callout(P(5.0, 0.9), '吹抜（0.91×1.82）\n床がない → 入れない', dirs=(20, 0, 40), dists=(80, 100, 120), fs=13, color=RED)
    z.callout(P(2.73, 6.82), 'ベランダ（南の0.91）\n壁と屋根に囲まれていない → 入れない', dirs=(-90, -70, -110), dists=(45, 60, 75), fs=13,
              color=RED)
    z.callout(P(4.23, 2.4), '階段室\n壁で囲まれている → 入れる', dirs=(0, 20, -20), dists=(70, 90, 110), fs=13, color=GREEN)
    z.free_text(P(2.73, 9.4), '床面積に入る部分：4.55×1.82 ＋ 5.46×4.55', fs=16, weight='bold')
    save(fig, [z], 'H21_dai22mon_zu11_2kai_irenai')


def zu12():
    fig, axes = new_figure('2階の求積図（2つの長方形に分けて足す）',
                           '4.55×1.82＝8.2810（北の帯。北東の吹抜は含まない）＋ 5.46×4.55＝24.8430（階段室・洋室を含む。ベランダは含まない）\n'
                           '＝ 33.1240 → 33.12㎡。点線は1階の位置',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, extra=[xy(P(-1.0, 9.8)), xy(P(9.5, -1.0))], pad_aspect=True)
    z.poly(F1, color=GRAY, lw=1.3, ls='--')
    z.poly(R2_N, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(R2_S, color=GREEN, lw=0, fill=GREEN, check=False)
    z.line(P(0, 1.82), P(4.55, 1.82), color=GRAY, lw=1.2, ls='--')
    z.poly(F2, color=BLACK, lw=2.4)
    z.north_arrow()
    dims(z, F2, ['4.55', None, None, '4.55', None, '6.37'])
    z.free_text(P(2.3, 0.91), '4.55×1.82＝8.2810', fs=14, color=BLUE)
    z.free_text(P(2.73, 4.1), '5.46×4.55\n＝24.8430', fs=16, color=GREEN)
    z.free_text(P(2.73, 9.4), '合計 33.1240 → 33.12㎡', fs=17, weight='bold')
    save(fig, [z], 'H21_dai22mon_zu12_2kai_kyuuseki')


def zu13():
    fig, axes = new_figure('3階（ロフト）の求積図（押入も含める）',
                           '2階のウォークインクローゼットの真上、北西の角の4.55×1.82＝8.2810 → 8.28㎡。点線は1階の位置。\n'
                           '押入（0.91）の天井が低くても、1室の一部が1.5m未満の部分は算入する（準則第82条第1号ただし書）。3.64×1.82＝6.62は誤り',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, pad_aspect=True)
    z.poly(F1, color=GRAY, lw=1.3, ls='--')
    z.poly(OSHIIRE, color=ORANGE, lw=0, fill=ORANGE, alpha=0.30, check=False)
    z.poly(LOFT, color=BLUE, lw=0, fill=BLUE, check=False)
    z.line(P(0.91, 0), P(0.91, 1.82), color=GRAY, lw=1.2, ls='--')
    z.poly(F3, color=BLACK, lw=2.4)
    z.north_arrow()
    dims(z, F3, ['4.55', '1.82', None, None])
    z.free_text(P(0.455, 0.91), '押入', fs=12)
    z.free_text(P(2.73, 0.91), 'ロフト', fs=14)
    z.callout(P(2.73, 1.82), '南の辺は手すり（固定式ハシゴ階段で2階へ）', dirs=(-90, -70, -110), dists=(40, 55, 70), fs=12, color=GRAY)
    z.free_text(P(2.73, 4.9), '4.55×1.82＝8.2810 → 8.28㎡', fs=17, weight='bold')
    z.free_text(P(2.73, 6.1), '誤り：押入を除く 3.64×1.82＝6.6248 → 6.62', fs=14, color=RED)
    save(fig, [z], 'H21_dai22mon_zu13_3kai_kyuuseki')


# =====================================================================================
# 図14：屋根の種類ごとの割合（30％未満は書かない）
# =====================================================================================
def zu14():
    fig, axes = new_figure('屋根が2種類でも、30％未満の種類の屋根は構造に書かない',
                           '床面積に算入する部分の屋根面積のうち30％未満の種類の屋根は表示しない（昭和63年3月24日民三第1826号）。\n'
                           '玄関の小屋根は 0.91×1.82＝1.6562 ÷ 41.405 ＝ 約4％（屋根を真上から見た広さを1階の外形とみた概算）→ 書かない',
                           w=17, h=8.6, ncols=2, width_ratios=[1.0, 1.0])
    fig.subplots_adjust(top=0.84, wspace=0.12)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, F1, margin=0.22, extra=[xy(P(2.73, 9.4)), xy(P(13.0, -1.0))], pad_aspect=True)
    z.poly(F1, color=BLACK, lw=2.2, fill=BLUE, alpha=0.16)
    z.poly(KOYANE, color=ORANGE, lw=0, fill=ORANGE, alpha=0.65, check=False)
    z.poly(F1, color=BLACK, lw=2.2, fill=None)
    z.north_arrow()
    z.free_text(P(2.7, 4.6), '大屋根\n（洋かわらぶき）\n約96％', fs=13, color=BLUE, weight='bold')
    z.callout(P(5.915, 0.91), '玄関の小屋根\n（ガルバリウム＝合金メッキ鋼板）\n0.91×1.82＝1.6562', dirs=(15, 0, 30), dists=(60, 80, 100), fs=12,
              color=ORANGE)
    ax.set_title('屋根を真上から見た図（模式）', fontsize=16, weight='bold')
    # 右：割合の帯
    ax2 = axes[1]
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title('屋根の種類ごとの割合', fontsize=16, weight='bold')
    x0, w, y0, h = 6, 88, 46, 14
    ax2.add_patch(Rectangle((x0, y0), w * 0.96, h, fc=BLUE, alpha=0.25, ec=BLUE, lw=2))
    ax2.add_patch(Rectangle((x0 + w * 0.96, y0), w * 0.04, h, fc=ORANGE, alpha=0.8, ec=ORANGE, lw=2))
    ax2.text(x0 + w * 0.48, y0 + h / 2, 'かわらぶき 約96％', ha='center', va='center', fontsize=17, color=BLUE, weight='bold')
    ax2.plot([x0 + w * 0.3] * 2, [y0 - 6, y0 + h + 6], color=RED, lw=2.2, ls='--')
    ax2.text(x0 + w * 0.3, y0 + h + 9, '30％の線', ha='center', va='center', fontsize=15, color=RED, weight='bold')
    ax2.annotate('合金メッキ鋼板ぶき\n約4％', xy=(x0 + w * 0.98, y0), xytext=(x0 + w * 0.78, y0 - 12), ha='center', va='center',
                 fontsize=15, color=ORANGE, weight='bold', arrowprops=dict(arrowstyle='-', color=ORANGE, lw=1.4))
    ax2.text(50, 14, '30％未満 → 構造には書かない\n構造は「木造かわらぶき3階建」', ha='center', va='center', fontsize=17, weight='bold',
             linespacing=1.6)
    ax2.text(50, 90, 'どちらの種類も30％以上なら\n「かわら・合金メッキ鋼板ぶき」のように並べて書く（準則第81条第2項）', ha='center',
             va='center', fontsize=14, color=GRAY, linespacing=1.6)
    save(fig, [z], 'H21_dai22mon_zu14_yane_wariai')


# =====================================================================================
# 図15：添付書類の要否（固定配置）
# =====================================================================================
def zu15():
    fig, ax = fixed_fig('添付書類：要るもの・要らないもの（建物の表題登記）',
                        '建物の表題登記の添付情報は不動産登記令別表12の項（建物図面・各階平面図・所有権証明・住所証明）と、代理人の権限を証する情報（令第7条第1項第2号）',
                        w=16, h=9)
    rows_yes = [('建物図面', '令別表12の項添付情報欄イ'), ('各階平面図', '同欄ロ'),
                ('所有権証明書', '同欄ハ（表題部所有者となる者が所有権を有することを証する情報）'),
                ('住所証明書', '同欄ニ（表題部所有者となる者の住所を証する情報）'), ('代理権限証書', '令第7条第1項第2号（代理人が申請するとき）')]
    card(ax, 2, 6, 57, 88, GREEN)
    put(ax, 3.5, 91, '書く（5つ）', fs=19, weight='bold', color=GREEN)
    for i, (a, b) in enumerate(rows_yes):
        y = 80 - i * 15.5
        put(ax, 3.5, y, a, fs=17, weight='bold')
        put(ax, 3.5, y - 6.5, b, fs=12.5, color=GRAY)
    card(ax, 61, 6, 37, 88, RED)
    put(ax, 62.5, 91, '書かない', fs=19, weight='bold', color=RED)
    put(ax, 62.5, 80, '登記識別情報', fs=17, weight='bold')
    put(ax, 62.5, 73.5, '権利に関する登記で、登記義務者が\n提供するもの。表題登記の添付情報には\n載っていない', fs=12.5, color=GRAY)
    put(ax, 62.5, 54, '印鑑証明書', fs=17, weight='bold')
    put(ax, 62.5, 47.5, '令別表12の項に載っていない', fs=12.5, color=GRAY)
    put(ax, 62.5, 30, '答案用紙の欄の名前は「添付書類」\n→ 「〜書」で書く', fs=14, color=BLACK)
    save_fixed(fig, 'H21_dai22mon_zu15_tenpu_shorui')


# =====================================================================================
# 図16：登録免許税（固定配置）
# =====================================================================================
def zu16():
    fig, ax = fixed_fig('表示に関する登記で登録免許税がかかるのは、一部だけ',
                        '登録免許税法別表第一の一（十三）：所有権の登記のある不動産の表示の変更の登記のうち、分筆・分割・区分と合筆・合併。\n'
                        '建物の表題登記はこの表に載っていないので、納めなくてよい。答案用紙に登録免許税の欄はない',
                        w=16, h=8.8)
    card(ax, 2, 8, 46, 86, ORANGE)
    put(ax, 3.5, 91, '課税される（別表第一の一（十三））', fs=17, weight='bold', color=ORANGE)
    put(ax, 3.5, 80, 'イ　土地の分筆・建物の分割・区分\n　　（分筆後などの不動産の個数×1,000円）\nロ　土地の合筆・建物の合併\n　　（合筆後などの不動産の個数×1,000円）\n\nどちらも「所有権の登記のある」不動産が対象', fs=15)
    card(ax, 52, 8, 46, 86, GREEN)
    put(ax, 53.5, 91, '課税されない（この表に載っていない）', fs=17, weight='bold', color=GREEN)
    put(ax, 53.5, 80, '建物の表題登記（本問）\n表題部の変更（種類・構造・床面積）\n建物の滅失の登記\n土地の地目・地積の変更\n\n本問は新築の表題登記なので、\n登録免許税は書かない', fs=15)
    save_fixed(fig, 'H21_dai22mon_zu16_touroku_menkyozei')


# =====================================================================================
# 図17：書く欄・空ける欄（答案用紙（その1）の模式図）
# =====================================================================================
def zu17():
    setup_font()
    fig = plt.figure(figsize=(16, 11), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('答案用紙で「書く欄」と「空ける欄」', fontsize=23, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.08, 0.60, 0.82])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    def fld(x, y, w, h, label, kind, fs=13):
        col = {'書く': INK, '空ける': GRAY, '印刷': BLACK}[kind]
        ax.add_patch(Rectangle((x, y), w, h, fill=(kind != '印刷'), fc=col if kind != '印刷' else 'none',
                               alpha=0.12 if kind != '印刷' else 1, ec='none', zorder=1))
        ax.add_patch(Rectangle((x, y), w, h, fill=False, ec=col, lw=1.8, zorder=2))
        ax.text(x + 1.2, y + h / 2, label, ha='left', va='center', fontsize=fs, color=col, zorder=3)

    ax.text(1, 98, '答案用紙（その1）　問1', fontsize=15, weight='bold', va='center')
    fld(2, 88, 94, 7, '登記の目的　建物表題登記', '書く')
    fld(2, 77, 94, 9, '添付書類　建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書', '書く')
    ax.text(2, 74, '平成21年8月23日　申請　D地方法務局B出張所', fontsize=13, va='center', color=BLACK)
    fld(2, 65, 94, 7, '申請人　A市B町二丁目3番地4　土野一郎', '書く')
    fld(2, 55, 86, 7, '代理人　A市C町五丁目6番地7　家野二郎', '書く')
    ax.text(92, 58.5, '印', fontsize=13, ha='center', va='center', color=BLACK)
    ax.text(30, 52.5, '（連絡先電話番号　略　）', fontsize=12, va='center', color=BLACK)
    fld(2, 46, 94, 4.5, '不動産番号（登記所が付ける）', '空ける', fs=12)
    fld(2, 40, 94, 5, '所在　A市B町二丁目3番地4（下の段は空欄）', '書く', fs=12)
    fld(2, 34.5, 94, 4.5, '家屋番号（記載不要）と印刷済み。右の枠は空欄', '空ける', fs=12)
    fld(2, 16, 94, 17, '1行目：居宅　木造かわらぶき3階建　1階41.40・2階33.12・3階8.28\n　　　　平成21年8月8日新築　（2・3行目と最下段は空欄）', '書く', fs=12)
    fld(44, 6, 38, 7, '土地家屋調査士　家野二郎（職印）', '書く', fs=12)
    # 凡例
    fig.text(0.65, 0.84, '凡例', fontsize=17, weight='bold')
    for i, (lab, col) in enumerate([('書く（濃い青）', INK), ('空けておく（灰色）', GRAY), ('印刷済み（黒）', BLACK)]):
        fig.patches.append(Rectangle((0.65, 0.78 - i * 0.045), 0.03, 0.03, transform=fig.transFigure, fill=False, ec=col, lw=2.2))
        fig.text(0.69, 0.795 - i * 0.045, lab, fontsize=15, va='center', color=col)
    fig.text(0.65, 0.60, '答案用紙（その2）　問3', fontsize=16, weight='bold')
    fig.text(0.65, 0.57, '　書く　建物の所在・作成者（土地家屋調査士　家野二郎）・\n　　　申請人（土野一郎）・図面\n　空ける　家屋番号\n　印刷済み　縮尺・作成年月日・職印の枠', fontsize=14,
             va='top', linespacing=1.7)
    fig.text(0.65, 0.33, '問2', fontsize=16, weight='bold')
    fig.text(0.65, 0.305, '　書く　具体的書面の例3つ', fontsize=14, va='top')
    fig.text(0.5, 0.025, '（略）と印刷されていない欄は書く。不動産番号・家屋番号は登記所が付けるので空けておく。※の欄には書かない', ha='center', fontsize=15)
    save_fixed(fig, 'H21_dai22mon_zu17_kakuran')


# =====================================================================================
# 図18：所有権証明書の当てはめ（固定配置）
# =====================================================================================
def zu18():
    fig, ax = fixed_fig('問2：所有権を証する書面は、事実に当てはめて選ぶ',
                        '建物の表題登記の所有権を証する情報の例（不動産登記事務取扱手続準則第87条第1項）。調査結果3〜5・2の事実で、選べるもの・選べないものを分ける',
                        w=16, h=9.4)
    rows = [
        ('確認済証', '建築基準法第6条の確認', '使える', GREEN),
        ('検査済証', '建築基準法第7条の検査', '使える', GREEN),
        ('建倉工務店の工事完了引渡証明書（印鑑証明書付き）', '建築請負人の証明（調査結果2・4）', '使える', GREEN),
        ('丸田電気・中山設備の証明書', '附帯設備の工事をしただけで、建物の建築請負人ではない（調査結果5）', '使えない', RED),
        ('現場責任者の建倉進さんの証明書', '会社の社員。請負人は株式会社建倉工務店（調査結果4）', '使えない', RED),
        ('敷地所有者の証明', '敷地は土野さん自身の土地。自分で自分を証明することになる', '使えない', RED),
        ('固定資産税の納付証明', '新築したばかりで、まだ納付がない', '使えない', RED),
    ]
    for i, (a, b, c, col) in enumerate(rows):
        y = 92 - i * 12.6
        card(ax, 2, y - 10.5, 96, 11, col, alpha=0.10, lw=1.6)
        put(ax, 3.5, y - 1.0, a, fs=15.5, weight='bold', va='top')
        put(ax, 3.5, y - 6.2, b, fs=13, color=GRAY, va='top')
        put(ax, 95, y - 5.5, c, fs=17, weight='bold', color=col, ha='right', va='center')
    save_fixed(fig, 'H21_dai22mon_zu18_shoyuuken_shoumei')


# =====================================================================================
# 図19：各階平面図の完成形（問3の欄の左半分と右半分）
# =====================================================================================
def heimen_content(z):
    """左半分：各階平面図（縮尺1/250、1m ＝ 4mm）。壁の中心線の辺長（小数第2位）、2階・3階には1階の位置を点線で。"""
    x0 = 44.0
    # 1階
    z.free_text(M(28.0, 241.0), '1階', fs=11, ha='left')
    f1 = [S250(p, x0, 238.0) for p in F1]
    z.poly(f1, lw=1.6)
    for i, t in enumerate(['6.37', '1.82', None, '5.46', '5.46', '7.28']):
        if t:
            z.edge_label(f1[i], f1[(i + 1) % 6], t, centroid(f1), fs=10, dists=(8, 12))
    z.callout(S250(P(5.915, 1.82), x0, 238.0), '0.91', dirs=(-10, 10, -30), dists=(24, 32, 42), fs=9)
    z.free_text(M(100.0, 232.0), '求積表\n6.37×1.82＝11.5934\n5.46×5.46＝29.8116\n計　41.4050\n床面積　41.40㎡', fs=11, ha='left',
                linespacing=1.6)
    # 2階（1階の位置を点線）
    y2 = 192.0
    z.free_text(M(28.0, y2 + 3.0), '2階', fs=11, ha='left')
    z.poly([S250(p, x0, y2) for p in F1], lw=1.1, ls=':')
    f2 = [S250(p, x0, y2) for p in F2]
    z.poly(f2, lw=1.6)
    for i, t in enumerate(['4.55', '1.82', None, '4.55', '5.46', '6.37']):
        if t == '5.46' and i == 4:                  # 南の辺の外側には1階の点線があるので、辺の内側に書く
            z.free_text((f2[i] + f2[(i + 1) % 6]) / 2, t, fs=10, offsets=((0, 12), (0, 17)))
        elif t:
            z.edge_label(f2[i], f2[(i + 1) % 6], t, centroid(f2), fs=10, dists=(8, 12))
    z.callout(S250(P(5.005, 1.82), x0, y2), '0.91', dirs=(40, 20, 60), dists=(24, 32, 42), fs=9)
    z.free_text(M(100.0, 186.0), '求積表\n4.55×1.82＝8.2810\n5.46×4.55＝24.8430\n計　33.1240\n床面積　33.12㎡', fs=11, ha='left',
                linespacing=1.6)
    # 3階（1階の位置を点線）
    y3 = 150.0
    z.free_text(M(28.0, y3 + 3.0), '3階', fs=11, ha='left')
    z.poly([S250(p, x0, y3) for p in F1], lw=1.1, ls=':')
    f3 = [S250(p, x0, y3) for p in F3]
    z.poly(f3, lw=1.6)
    for i, t in enumerate(['4.55', '1.82', None, None]):
        if t:
            z.edge_label(f3[i], f3[(i + 1) % 4], t, centroid(f3), fs=10, dists=(8, 12))
    z.free_text(M(100.0, 142.0), '求積表\n4.55×1.82＝8.2810\n床面積　8.28㎡', fs=11, ha='left', linespacing=1.6)


def zu19():
    fig, ax, z = sheet_figure('各階平面図の完成形（答案用紙（その2）の問3の欄・縮尺1/250と1/500の実際の大きさ）')
    sheet3(ax, shozai='A市B町二丁目3番地4', seisha='土地家屋調査士　家野二郎', shinseinin='土野一郎')
    heimen_content(z)
    zumen_content(z)
    ax.text(212.0, 35.0, '各階平面図は壁の中心線の寸法（小数第2位）。各階の別・形・1階の位置（2階・3階の点線）・各階の周囲の長さ・求積と床面積を書く（規則第83条第1項）',
            ha='center', va='center', fontsize=13)
    ax.text(212.0, 27.5, '方位は建物図面だけに書く（各階平面図に方位の記録事項はない）。作成者は（略）の印刷がないので氏名を書き、職印を押す。家屋番号は空欄',
            ha='center', va='center', fontsize=12, color=GRAY)
    assert round(area(F1), 4) == 41.405 and round(area(F2), 4) == 33.124 and round(area(F3), 4) == 8.281
    save(fig, [z], 'H21_dai22mon_zu19_kakai_heimenzu')


# =====================================================================================
# 図20：本番で解く順番
# =====================================================================================
def zu20():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　ロフトの階数を先に決める', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問を先に読む', '問1〜問3と\n問題文の注', BLUE),
        ('②', '調査結果と\n断面図のメモ', 'ロフト2.00・吹抜\n小屋根の割合・通し柱\n後退線', BLUE),
        ('③', '申請書の\n床面積以外\nと問2', '目的・添付書類\n申請人・原因の日付\n確認済証など', BLUE),
        ('④', '床面積3つ\nと階数', '41.40（切捨て）\n33.12・8.28\n3階建', GREEN),
        ('⑤', '各階平面図と\n建物図面', '（その2）\n3.10・1.00', RED),
        ('⑥', '見直し', '41.41にして\nいないか・\n30％未満の小屋根', GRAY),
    ]
    w, h, gap = 14.5, 42, 2.0
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 4, t, ha='center', va='center', fontsize=17)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, '計算しなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4 * (w + gap) - gap / 2, 76, '時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '計算は長方形5つだけ。ロフトを階に数えるかどうかは、構造の階数・床面積・各階平面図のすべてに響くので②で決める。\n'
             '申請書と問2を先に仕上げておけば、作図で時間が足りなくなっても点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H21_dai22mon_zu20_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[固定配置の図] 解く順番\n  →', path)


if __name__ == '__main__':
    for f in (zu01, zu02, zu03, zu04, zu05, zu06, zu07, zu08, zu09, zu10, zu11, zu12, zu13, zu14, zu15, zu16, zu17, zu18, zu19, zu20):
        f()
    print('重なり合計:', len(PROBLEMS))
