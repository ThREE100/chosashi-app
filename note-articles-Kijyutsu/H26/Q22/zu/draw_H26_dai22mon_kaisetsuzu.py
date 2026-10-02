"""平成26年度 第22問（建物）の解説図9枚を、頂点座標から作図してPNGに書き出す。

`../prompt_H26_dai22mon_kaisetsuzu.md` の図1〜図9どおり（番号は記事の挿入順）。作図の共通部品は `tools/zu_helpers.py`。
敷地は座標値一覧表がないので、〔見取図〕の辺長と〔見取図〕の（注）4（全て直交）・（注）5（北は道路に直角）から組み立てた座標
（原点＝1番8の南西の角。S(東, 北)）を使う。建物の平面は (東, 南)（原点＝事務所の1階の北西の角）で持ち、
zu_helpers の (北, 東) には B() で変換する（北 ＝ −南）。
図4（建物図面）と図8（各階平面図）の完成形は、試験の答案用紙の第5欄（右半分が建物図面〈申請人（略）・縮尺1/500〉、
左半分が各階平面図〈作成者（略）（平成何年何月何日作成）・縮尺1/250〉、右上に家屋番号・建物の所在）の形の枠の中に描く。
実行: python3 note-articles-Kijyutsu/H26/Q22/zu/draw_H26_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
INK = '#1a3a8f'   # 答案用紙への記入（濃い青）


def S(e, n):
    """敷地の (東, 北) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(n, e)


def B(e, s):
    """建物の平面の (東, 南) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def P(pts, de=0.0, ds=0.0):
    return [B(e + de, s + ds) for e, s in pts]


def rect(e0, s0, e1, s1):
    return [(e0, s0), (e1, s0), (e1, s1), (e0, s1)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def save(fig, zs, name):
    for t in fig.texts:
        t.set_linespacing(1.5)   # 2行の説明文の行間
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=14, ref=None, color=BLACK, inward=()):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, color=color, outward=i not in inward)


def dist_arrow(z, p, q, text, side, fs=15):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    z.ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=BLACK, lw=1.5,
                                                           mutation_scale=13, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    return z.free_text(m, text, fs=fs, offsets=(side, (side[0] * 1.5, side[1] * 1.5), (-side[0], -side[1])))


def maru(z, p, text, color=BLACK, fs=16):
    """丸囲みの記号（「主」「附1」）。"""
    return z.free_text(p, text, fs=fs, color=color, weight='bold',
                       offsets=((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0)),
                       bbox=dict(boxstyle='circle,pad=0.25', fc='white', ec=color, lw=1.6))


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


# ---- 敷地（〔見取図〕の辺長。1番8・1番10 は東西20.00×南北23.47、1番3 は40.00×50.00） ----
LOT3 = [S(-40, 0), S(0, 0), S(0, 50), S(-40, 50)]
LOT7 = [S(0, 23.47), S(20, 23.47), S(20, 50), S(0, 50)]
LOT8 = [S(0, 0), S(20, 0), S(20, 23.47), S(0, 23.47)]
LOT9 = [S(20, 23.47), S(40, 23.47), S(40, 50), S(20, 50)]
LOT10 = [S(20, 0), S(40, 0), S(40, 23.47), S(20, 23.47)]
assert round(area(LOT8), 2) == round(area(LOT10), 2) == 469.40      # 登記記録の地積と一致
assert round(area(LOT3), 2) == 2000.00 and round(area(LOT7), 2) == round(area(LOT9), 2) == 530.60

# ---- 建物（外壁。〔見取図〕の（注）3：距離は筆界線から外壁まで） ----
E_OF, N_OF = round(40 - 2.51, 2), round(23.47 - 1.72, 2)          # 事務所の東の外壁・北の外壁
W_OF, S_OF = round(E_OF - 14.56, 2), round(N_OF - 14.56, 2)
STEP_E, STEP_N = round(E_OF - 6.37, 2), round(N_OF - 8.19, 2)
OFFICE = [S(W_OF, N_OF), S(E_OF, N_OF), S(E_OF, S_OF), S(STEP_E, S_OF), S(STEP_E, STEP_N), S(W_OF, STEP_N)]
E_WH, S_WH = round(20 - 1.85, 2), 1.41                                # 倉庫の東の外壁・南の外壁
WAREHOUSE = [S(E_WH - 15, S_WH), S(E_WH, S_WH), S(E_WH, S_WH + 6), S(E_WH - 15, S_WH + 6)]
assert (E_OF, N_OF, W_OF, S_OF, STEP_E, STEP_N) == (37.49, 21.75, 22.93, 7.19, 31.12, 13.56)
assert round(area(OFFICE), 4) == 159.8233 and round(area(WAREHOUSE), 4) == 90.0
assert W_OF > 20 and S_OF > 0 and round(E_WH - 15, 2) == 3.15 > 0 and S_WH + 6 < 23.47   # 自分の筆の中に収まる

# ---- 各階平面図（1番10・1番8の各階平面図の抜粋。(東, 南)、原点は1階の北西の角） ----
F1 = [(0, 0), (14.56, 0), (14.56, 14.56), (8.19, 14.56), (8.19, 8.19), (0, 8.19)]
F2 = [(2.73, 0), (14.56, 0), (14.56, 8.19), (9.10, 8.19), (9.10, 6.37), (2.73, 6.37)]
F2_WRONG = [(0, 0), (11.83, 0), (11.83, 8.19), (6.37, 8.19), (6.37, 6.37), (0, 6.37)]
FA = rect(0, 0, 15.00, 6.00)
assert round(area(P(F1)), 4) == 159.8233 and round(area(P(F2)), 4) == round(area(P(F2_WRONG)), 4) == 85.2943
assert round(area(P(FA)), 4) == 90.0
# 1階の外形のうち、2階と重ならない部分（2階の図に点線で重ねる）
F1_DOTS = [((0, 0), (2.73, 0)), ((0, 0), (0, 8.19)), ((0, 8.19), (8.19, 8.19)), ((8.19, 8.19), (8.19, 14.56)),
           ((8.19, 14.56), (14.56, 14.56)), ((14.56, 14.56), (14.56, 8.19))]


# ---- 図1：事実関係の時系列 ----
def zu01():
    """時系列。固定配置の図（日付を上下に互い違いに置く）なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('事実関係の時系列　登記原因の日付になるのはどの日か', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.17, 0.96, 0.72])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ev = [
        ('4月30日', '理事会で\n売却の議題', 'まだ決まっていない', GRAY),
        ('6月30日', '総会で規約廃止\n（全員一致）', '問1・問2の\n登記原因の日付', RED),
        ('7月10日', '売買契約', '', GRAY),
        ('7月22日', '問1の申請\n区分建物表題部\n変更登記\n（敷地権抹消）', '', BLUE),
        ('7月24日', '問2の申請\n建物表題登記\n（共用部分廃止）', '', BLUE),
        ('8月1日', '代金支払・\n引渡し', '', GRAY),
        ('8月8日', '丙川建設へ\n所有権の移転\nの登記', '', GRAY),
        ('8月10日', 'ブロック塀撤去・\n倉庫への\n内装工事完了', '問3の種類変更\nの日付', ORANGE),
        ('8月22日', '問3の申請\n建物表題部変更・\n合併登記', '', BLUE),
    ]
    ax.annotate('', xy=(99, 50), xytext=(1, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
    ax.text(99, 46, '平成26年', fontsize=15, ha='right', va='top')
    for i, (d, t, tag, col) in enumerate(ev):
        x = 6 + i * 11
        up = i % 2 == 0
        ax.plot([x], [50], 'o', ms=13 if col in (RED, ORANGE) else 10, color=col, zorder=5)
        ax.plot([x, x], [50, 62 if up else 38], color=col, lw=1.6)
        ax.text(x, 64 if up else 36, d, ha='center', va='bottom' if up else 'top', fontsize=17, weight='bold', color=col)
        ax.text(x, 72 if up else 28, t, ha='center', va='bottom' if up else 'top', fontsize=13.5, color=BLACK,
                linespacing=1.35)
        if tag:
            ax.text(x, 46 if up else 54, tag, ha='center', va='top' if up else 'bottom', fontsize=12.5, color=col,
                    weight='bold', linespacing=1.3,
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=col, lw=1.4))
    fig.text(0.5, 0.075, '規約の設定・変更・廃止は、理事会ではなく集会（総会）の決議でする（区分所有法第31条第1項）。\n'
             '問1・問2の登記原因の日付は6月30日。問3の種類変更は工事が終わった8月10日。合併には日付を付けない',
             ha='center', va='center', fontsize=15, linespacing=1.6)
    path = os.path.join(OUT, 'H26_dai22mon_zu01_jikeiretsu.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図1: 時系列（固定配置）\n  →', path)


# ---- 図2：主である建物と附属建物の比較図 ----
def zu02():
    fig, axes = new_figure('どちらが主？　所有者の希望ではなく、どちらがどちらの効用を補うかで決まる',
                           '附属建物＝主である建物に附属する建物（不動産登記法第2条第23号）。「所有者の意思に反しない限り」（準則第78条第1項）は\n'
                           '1個の建物として扱うかどうかの話。倉庫は事務所の仕事を補うので、事務所（1番10）が主、倉庫（1番8）が附属建物符号1',
                           w=16, h=9, ncols=2)
    fig.subplots_adjust(top=0.84, bottom=0.16, wspace=0.12)
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=14)
        fit(ax, LOT8 + LOT10, margin=0.08, extra=[xy(S(-2, -4)), xy(S(42, 27))], pad_aspect=True)
        z.poly(LOT8, color=GRAY, lw=1.4)
        z.poly(LOT10, color=GRAY, lw=1.4)
        col = RED if k == 0 else GREEN
        z.poly(OFFICE, color=BLACK, lw=2.2, fill=col, alpha=0.18)
        z.poly(WAREHOUSE, color=BLACK, lw=2.2, fill=col, alpha=0.18)
        z.free_text(S(10, 17), '1番8', fs=14, color=GRAY)
        z.free_text(S(26, 3.4), '1番10', fs=14, color=GRAY)
        if k == 0:
            maru(z, S(10.65, 4.41), '主', color=RED)
            maru(z, S(29.5, 17.6), '附', color=RED)
            z.free_text(S(34.3, 10.4), '事務所', fs=13)
            z.free_text(S(6.0, 4.41), '倉庫', fs=13)
            ax.set_title('誤り：倉庫を主、事務所を附属', fontsize=18, weight='bold', color=RED, pad=10)
            z.free_text(S(20, -2.6), '所有者の意思だけでは主従は決まらない', fs=14, color=RED)
        else:
            maru(z, S(29.5, 17.6), '主', color=GREEN)
            maru(z, S(10.65, 4.41), '附1', color=GREEN, fs=14)
            z.free_text(S(34.3, 10.4), '事務所', fs=13)
            z.free_text(S(6.0, 4.41), '倉庫', fs=13)
            ax.annotate('', xy(S(24.5, 16.0)), xytext=xy(S(14.0, 7.41)),
                        arrowprops=dict(arrowstyle='-|>', lw=2.4, color=GREEN, mutation_scale=20), zorder=6)
            z.segments.append((xy(S(14.0, 7.41)), xy(S(24.5, 16.0))))
            z.free_text(S(12.0, 14.2), '作業道具を置いて\n事務所の仕事を補う', fs=13, color=GREEN,
                        offsets=((0, 0), (-10, 8), (0, 14)))
            ax.set_title('正しい：事務所を主、倉庫を附属建物符号1', fontsize=18, weight='bold', color=GREEN, pad=10)
            z.free_text(S(20, -2.6), '附属建物＝主である建物の効用を補う建物', fs=14, color=GREEN)
        zs.append(z)
    zs[1].north_arrow()
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.17, 0.86], transform=fig.transFigure, color=GRAY, lw=1.2))
    save(fig, zs, 'H26_dai22mon_zu02_shujuu_hikaku')


# ---- 図3：敷地の辺長確認図（作図チェック用） ----
def zu03():
    fig, axes = new_figure('敷地の辺長確認図（作図チェック用。建物図面には辺長を書かない）',
                           '〔見取図〕の（注）4（全て直交）で形を決める。20.00×23.47＝469.40（1番8・1番10）、40.00×50.00＝2000.00（1番3）。\n'
                           'どれも登記記録の地積と一致する。道路の向こう側の線の位置は模式', w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, LOT3 + LOT9, margin=0.06, extra=[xy(S(-56, -7)), xy(S(56, 57))], pad_aspect=True)
    for lot in (LOT3, LOT7, LOT9):
        z.poly(lot, color=BLACK, lw=1.8, fill=GRAY, alpha=0.06)
    for lot in (LOT8, LOT10):
        z.poly(lot, color=BLACK, lw=2.4, fill=BLUE, alpha=0.14)
    for n in (0, 23.47, 50):
        z.line(S(-54, n), S(-40, n), color=GRAY, lw=1.2)
        z.line(S(40, n), S(54, n), color=GRAY, lw=1.2)
    z.line(S(-54, -5), S(54, -5), color=GRAY, lw=1.2)        # 道路（39）の向こう側の線（位置は模式）
    z.line(S(-54, 55), S(54, 55), color=GRAY, lw=1.2)        # 道路（38）の向こう側の線（位置は模式）
    z.north_arrow()
    c3, c8, c10 = centroid(LOT3), centroid(LOT8), centroid(LOT10)
    z.edge_label(LOT3[0], LOT3[1], '40.00', c3, fs=15)
    z.edge_label(LOT3[2], LOT3[3], '40.00', c3, fs=15)
    z.edge_label(S(-40, 23.47), S(-40, 50), '26.53', c3, fs=15)
    z.edge_label(S(-40, 0), S(-40, 23.47), '23.47', c3, fs=15)
    z.edge_label(LOT8[0], LOT8[1], '20.00', c8, fs=15)
    z.edge_label(LOT10[0], LOT10[1], '20.00', c10, fs=15)
    z.edge_label(LOT7[2], LOT7[3], '20.00', centroid(LOT7), fs=15)
    z.edge_label(LOT9[2], LOT9[3], '20.00', centroid(LOT9), fs=15)
    z.edge_label(S(0, 23.47), S(20, 23.47), '20.00', c8, fs=15, outward=False)
    z.edge_label(S(20, 23.47), S(40, 23.47), '20.00', c10, fs=15, outward=False)
    z.edge_label(LOT10[1], LOT10[2], '23.47', c10, fs=15)
    z.edge_label(S(0, 0), S(0, 23.47), '23.47', c8, fs=15, outward=False)
    z.edge_label(S(0, 23.47), S(0, 50), '26.53', centroid(LOT7), fs=15, outward=False)
    z.free_text(S(10, 11.0), '1番8\n469.40㎡', fs=16, weight='bold')
    z.free_text(S(30, 11.0), '1番10\n469.40㎡', fs=16, weight='bold')
    z.free_text(S(-20, 25), '1番3\n2000.00㎡\n（甲マンション）', fs=16)
    z.free_text(S(10, 37), '1番7', fs=15)
    z.free_text(S(30, 37), '1番9', fs=15)
    for p, t in [(S(-49, 37), '1-1'), (S(-49, 11), '1-2'), (S(49, 37), '1-11'), (S(49, 11), '1-12'),
                 (S(0, -2.5), '道路（39）'), (S(0, 52.5), '道路（38）')]:
        z.free_text(p, t, fs=14, color=GRAY, offsets=((0, 0), (0, 10), (0, -10)))
    save(fig, [z], 'H26_dai22mon_zu03_shikichi_henchou')


# ---- 図4：建物図面の完成形（答案用紙の第5欄の右半分の枠の中） ----
def zu04():
    setup_font()
    fig = plt.figure(figsize=(16, 13), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第5欄の右半分・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙の欄（第5欄の右上の家屋番号・建物の所在、下の申請人・縮尺）
    fig.text(0.24, 0.915, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.40, 0.893, 0.53, 0.938, '家屋番号', fs=15)
    cell(fig, 0.53, 0.893, 0.94, 0.938, '1番10', fs=16, ha='left', color=INK)
    cell(fig, 0.40, 0.848, 0.53, 0.893, '建物の所在', fs=15)
    cell(fig, 0.53, 0.848, 0.94, 0.893, 'A市B町一丁目1番地10、1番地8', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.095, 0.94, 0.848, lw=1.8)
    cell(fig, 0.06, 0.040, 0.20, 0.095, '申　請　人', fs=15)
    cell(fig, 0.20, 0.040, 0.74, 0.095, '（略）', fs=15)
    cell(fig, 0.74, 0.040, 0.83, 0.095, '縮尺', fs=15)
    cell(fig, 0.83, 0.040, 0.94, 0.095, '1/500', fs=15)
    ax = fig.add_axes([0.08, 0.11, 0.84, 0.72])
    z = Zu(ax, fontsize=15)
    fit(ax, LOT8 + LOT10, margin=0.06, extra=[xy(S(-6, -7)), xy(S(46, 29))], pad_aspect=True)
    z.poly(LOT8, color=BLACK, lw=2.2)
    z.poly(LOT10, color=BLACK, lw=2.2)
    for p, q in [(S(0, 23.47), S(0, 28)), (S(20, 23.47), S(20, 28)), (S(40, 23.47), S(40, 28)),
                 (S(0, 0), S(-5, 0)), (S(40, 0), S(45, 0)), (S(40, 23.47), S(45, 23.47)),
                 (S(-5, -5), S(45, -5))]:
        z.line(p, q, color=BLACK, lw=1.4)
    z.poly(OFFICE, color=BLACK, lw=2.6)
    z.poly(WAREHOUSE, color=BLACK, lw=2.6)
    z.north_arrow()
    dist_arrow(z, S(W_OF, N_OF), S(W_OF, 23.47), '1.72', side=(-20, 0))
    dist_arrow(z, S(E_OF, N_OF), S(40, N_OF), '2.51', side=(0, -14))
    dist_arrow(z, S(E_OF, S_OF), S(40, S_OF), '2.51', side=(0, 14))
    dist_arrow(z, S(E_WH, S_WH + 6), S(20, S_WH + 6), '1.85', side=(-22, 12))
    dist_arrow(z, S(E_WH - 15, S_WH), S(E_WH - 15, 0), '1.41', side=(-20, 0))
    dist_arrow(z, S(E_WH, S_WH), S(E_WH, 0), '1.41', side=(20, 0))
    maru(z, S(30.0, 17.5), '主')
    maru(z, S(10.65, 4.41), '附1', fs=14)
    OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))
    z.free_text(S(10, 15.5), '1－8', fs=17, offsets=OFFS)
    z.free_text(S(26.5, 4.0), '1－10', fs=17, offsets=OFFS)
    for p, t in [(S(-3.2, 12), '1－3'), (S(10, 26), '1－7'), (S(30, 26), '1－9'), (S(43, 26), '1－11'),
                 (S(43, 12), '1－12'), (S(20, -2.6), '道路　39')]:
        z.free_text(p, t, fs=15, offsets=OFFS)
    z.free_text(S(39, -6.3), '（単位：m）', fs=13, offsets=OFFS)
    save(fig, [z], 'H26_dai22mon_zu04_tatemono_zumen')


# ---- 図5：主である建物の1階と附属建物符号1の求積図 ----
def zu05():
    fig, axes = new_figure('主である建物の1階と附属建物符号1の求積図',
                           '1階：14.56×8.19＋6.37×6.37＝159.8233 → 159.82㎡　　符号1：15.00×6.00＝90.0000 → 90.00㎡\n'
                           '（どちらも登記記録と一致。本問は求積表を答案に書かない）',
                           w=16, h=10, ncols=2, width_ratios=[1.0, 1.0])
    fig.subplots_adjust(top=0.86, bottom=0.14, wspace=0.10)
    z = Zu(axes[0], fontsize=14)
    axes[0].set_title('主である建物　1階', fontsize=18, weight='bold', pad=10)
    fit(axes[0], P(F1), margin=0.22, pad_aspect=True)
    z.poly(P(rect(0, 0, 14.56, 8.19)), color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(P(rect(8.19, 8.19, 14.56, 14.56)), color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z.line(B(8.19, 8.19), B(14.56, 8.19), color=GRAY, lw=1.2, ls='-.')
    z.poly(P(F1), color=BLACK, lw=2.4)
    dims(z, P(F1), ['14.56', '14.56', '6.37', '6.37', '8.19', '8.19'], ref=B(10.0, 4.0))
    z.free_text(B(7.28, 4.1), '①14.56×8.19\n＝119.2464', fs=15)
    z.free_text(B(11.375, 11.4), '②6.37×6.37\n＝40.5769', fs=14)
    z.north_arrow()
    z2 = Zu(axes[1], fontsize=14)
    axes[1].set_title('附属建物　符号1（倉庫）', fontsize=18, weight='bold', pad=10)
    fit(axes[1], P(rect(0, -4.5, 15.0, 10.5)), margin=0.15, pad_aspect=True)
    z2.poly(P(FA), color=BLACK, lw=2.4, fill=GREEN, alpha=0.22)
    dims(z2, P(FA), ['15.00', '6.00', '15.00', '6.00'])
    z2.free_text(B(7.5, 3.0), '15.00×6.00＝90.0000', fs=15)
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.15, 0.86], transform=fig.transFigure, color=GRAY, lw=1.2))
    save(fig, [z, z2], 'H26_dai22mon_zu05_1kai_fuzoku_kyuuseki')


def floor1_dots(z, lw=1.6):
    for p, q in F1_DOTS:
        z.line(B(*p), B(*q), color=BLACK, lw=lw, ls=':')


# ---- 図6：2階の誤り比較図 ----
def zu06():
    fig, axes = new_figure('2階はどこにそろう？　1階の北西の角ではなく、北と東にそろえる',
                           '点線は1階の外形。どちらに描いても2階は11.83×6.37＋5.46×1.82＝85.29㎡で同じなので、床面積では誤りに気づけない。\n'
                           '問題の1番10の各階平面図の点線で位置を確かめる',
                           w=16, h=9.5, ncols=2)
    fig.subplots_adjust(top=0.85, bottom=0.15, wspace=0.10)
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=14)
        fit(ax, P(F1), margin=0.18, pad_aspect=True)
        if k == 0:
            z.poly(P(F1), color=BLACK, lw=1.6, ls=':')
            z.poly(P(F2_WRONG), color=RED, lw=2.4, fill=RED, alpha=0.22)
            ax.set_title('誤り：1階の北西の角に合わせた', fontsize=18, weight='bold', color=RED, pad=10)
            z.free_text(B(4.5, 3.0), '2階？', fs=16, color=RED, weight='bold')
            z.callout(B(11.83, 7.0), '2階の東の辺が\n1階の東の辺から\n2.73離れてしまう', dirs=(-120, -135, -105), fs=13,
                      color=RED, dists=(70, 90, 110))
        else:
            floor1_dots(z)
            z.poly(P(F2), color=GREEN, lw=2.4, fill=GREEN, alpha=0.22)
            ax.set_title('正しい：1階の北と東にそろえる', fontsize=18, weight='bold', color=GREEN, pad=10)
            z.free_text(B(8.5, 3.0), '2階', fs=16, color=GREEN, weight='bold')
            z.dim_line(B(0, -1.2), B(2.73, -1.2), color=BLACK)
            z.line(B(0, 0), B(0, -1.6), color=GRAY, lw=1.0)
            z.line(B(2.73, 0), B(2.73, -1.6), color=GRAY, lw=1.0)
            z.free_text(B(1.365, -1.2), '2.73', fs=14, offsets=((0, 12), (0, 16)))
            z.line(B(9.10, 8.19), B(9.10, 10.6), color=GRAY, lw=1.0, ls='--')
            z.line(B(8.19, 8.19), B(8.19, 10.6), color=GRAY, lw=1.0, ls='--', check=False)
            z.dim_line(B(8.19, 10.2), B(9.10, 10.2), color=BLACK)
            z.callout(B(8.645, 10.2), '0.91', dirs=(-60, -40, -80), fs=14, dists=(35, 45, 60))
        zs.append(z)
    zs[1].north_arrow()
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.16, 0.86], transform=fig.transFigure, color=GRAY, lw=1.2))
    save(fig, zs, 'H26_dai22mon_zu06_2kai_ayamari_hikaku')


# ---- 図7：主である建物の2階の求積図 ----
def zu07():
    fig, axes = new_figure('主である建物の2階の求積図（点線は1階の位置）',
                           '①11.83×6.37＝75.3571　＋　②5.46×1.82＝9.9372　＝　85.2943 → 85.29㎡（登記記録と一致）。\n'
                           '2階の西の端は1階の北西の角から東へ2.73', w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, P(F1), margin=0.16, pad_aspect=True)
    z.north_arrow()
    z.poly(P(rect(2.73, 0, 14.56, 6.37)), color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(P(rect(9.10, 6.37, 14.56, 8.19)), color=ORANGE, lw=0, fill=ORANGE, alpha=0.4, check=False)
    z.line(B(9.10, 6.37), B(14.56, 6.37), color=GRAY, lw=1.2, ls='-.')
    floor1_dots(z)
    z.poly(P(F2), color=BLACK, lw=2.4)
    dims(z, P(F2), ['11.83', '8.19', '5.46', '1.82', '6.37', '6.37'], ref=B(11.0, 3.0))
    z.free_text(B(8.0, 3.0), '①11.83×6.37\n＝75.3571', fs=16)
    z.callout(B(11.83, 7.28), '②5.46×1.82\n＝9.9372', dirs=(-90, -100, -80), fs=15, dists=(70, 90, 110))
    z.callout(B(4.0, 8.19), '点線＝1階の外形', dirs=(-120, -135, -105), fs=14, dists=(50, 65, 80))
    save(fig, [z], 'H26_dai22mon_zu07_2kai_kyuuseki')


# ---- 図8：各階平面図の完成形（答案用紙の第5欄の左半分の枠の中） ----
def zu08():
    setup_font()
    fig = plt.figure(figsize=(18, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第5欄の左半分・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.14, 0.96, 0.88, lw=1.8)
    cell(fig, 0.04, 0.07, 0.14, 0.14, '作　成　者', fs=15)
    cell(fig, 0.14, 0.07, 0.78, 0.14, '（略）　　　　　　　　　　　　（平成何年何月何日作成）', fs=15)
    cell(fig, 0.78, 0.07, 0.86, 0.14, '縮尺', fs=15)
    cell(fig, 0.86, 0.07, 0.96, 0.14, '1/250', fs=15)
    fig.text(0.5, 0.030, '主である建物の1階・2階と附属建物符号1を書き分け、2階には1階の位置を点線で示す。'
             '問5のなお書きどおり求積表は書かない（家屋番号・建物の所在の欄は第5欄の建物図面の側の上に1つだけ）',
             ha='center', va='center', fontsize=14)
    axes = [fig.add_axes([0.05, 0.17, 0.29, 0.62]), fig.add_axes([0.355, 0.17, 0.29, 0.62]),
            fig.add_axes([0.66, 0.17, 0.29, 0.62])]
    zs = []
    box = P(rect(-1.0, -1.0, 15.56, 15.56))          # 3枚とも同じ縮尺にするための表示範囲
    specs = [(F1, ['14.56', '14.56', '6.37', '6.37', '8.19', '8.19'], '主である建物　1階', 0.0),
             (F2, ['11.83', '8.19', '5.46', '1.82', '6.37', '6.37'], '主である建物　2階', 0.0),
             (FA, ['15.00', '6.00', '15.00', '6.00'], '附属建物　符号1', 4.0)]
    for k, (pts, labels, name, ds) in enumerate(specs):
        ax = axes[k]
        z = Zu(ax, fontsize=13)
        ax.set_title(name, fontsize=17, weight='bold')
        fit(ax, box, margin=0.04, pad_aspect=True)
        poly = P(pts, ds=ds)
        if k == 1:
            floor1_dots(z, lw=1.4)
        z.poly(poly, color=BLACK, lw=2.4)
        dims(z, poly, labels, fs=13, ref=[B(10.0, 4.0), B(11.0, 3.0), None][k])
        zs.append(z)
    zs[2].north_arrow()
    save(fig, zs, 'H26_dai22mon_zu08_kakukai_heimenzu')


# ---- 図9：本番で解く順番 ----
def zu09():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　計算のいらない欄を先に埋め、作図に時間を残す', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問1〜問5と\n問題文の注', '申請日3つ・\n1件の申請・\n求積表不要', BLUE),
        ('②', '日付の\n時系列メモ', '6月30日と\n8月10日に印', BLUE),
        ('③', '第1欄・第2欄', '非敷地権・\n表題登記', BLUE),
        ('④', '第4欄・\n第3欄の申請書', '床面積は\n登記記録を写す', BLUE),
        ('⑤', '第5欄の作図', '建物図面1/500\n各階平面図1/250', RED),
        ('⑥', '見直し', '合併に日付なし・\n2階の位置', GRAY),
    ]
    w, h, gap = 14.4, 42, 2.0
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=16)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col, linespacing=1.4)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2 * (w + gap) - gap / 2, 76, '計算なしで書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4.5 * (w + gap) - gap, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 4 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '床面積は登記記録の159.82・85.29・90.00がそのまま使えるので、求積は作図のチェックだけ。\n'
             '①〜④を手早く済ませて、⑤の作図（筆界からの距離・2階の点線）に時間を回す',
             ha='center', va='center', fontsize=15, linespacing=1.6)
    path = os.path.join(OUT, 'H26_dai22mon_zu09_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図9: 解く順番（固定配置）\n  →', path)


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
    print('重なり合計:', len(PROBLEMS))
