"""令和8年度 第21問（土地）会話形式note記事の解説図33枚を、座標値から作図する。

`../prompt_R8_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
PNG名の番号（zu01〜zu33）は記事の挿入順の管理用で、画像の中のタイトルには図番を入れない。
第5欄の地積測量図の枠は、アガルートの解答例（2026-10-20受領）に再現された答案用紙の第5欄の形（令和7年度の第3欄と同じ形）。

実行: python3 note-articles-Kijyutsu/R8/Q21/zu/draw_R8_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, area, chiseki, radial, dms, disp, fmt_num  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN)
import matplotlib.pyplot as plt  # noqa: E402
plt.rcParams['figure.max_open_warning'] = 0
from matplotlib.patches import Rectangle  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(481.86, 471.43), P(481.75, 506.66)
A, B, D, E, F = P(484.35, 505.19), P(486.05, 505.19), P(510.78, 490.69), P(509.94, 475.79), P(486.05, 474.32)
G, H, I, J, M = P(484.35, 474.32), P(486.05, 488.12), P(498.53, 494.70), P(510.78, 492.46), P(486.05, 491.31)
C = r2(radial(T2, T1, 29.03, dms(90, 4, 40)))
Cw = r2(radial(T2, T1, 29.03, -dms(90, 4, 40)))
L = r2(H + (I - H) * 6.05 / 12.48)
Lw = r2(H + (I - H) / abs(I - H) * 6.05)
K = r2(J + (L - J) * 21.6825 / 88.9943)
Kw = r2(D + (I - D) * (492.46 - D.imag) / (I - D).imag)
N = P(484.35, 491.31)   # N点：問題文に座標なし。AとGの直線上（調査図素図の注1）、Mの真南に置いた模式の位置

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('C', C, P(510.78, 506.79)), ('Cw', Cw, P(452.72, 506.61)), ('L', L, P(492.10, 491.31)),
                     ('Lw', Lw, P(491.40, 490.94)), ('K', K, P(506.23, 492.18)), ('Kw', Kw, P(505.37, 492.46))]:
    assert abs(got - want) < 1e-9, (n, got, want)
KOU = [E, D, I, H, F]                # 甲土地（本件登記1の前）
OTSU = [D, C, B, H, I]               # 乙土地（本件登記1の前）
RO = [I, K, L]                       # （ロ）切り離す三角形
KOU1 = [E, D, K, L, H, F]            # （イ）甲土地（本件登記1の後）
OTSU1 = [D, C, B, M, H, L, K]        # 乙土地（本件登記1の後、11月の分筆前）
URI = [J, C, B, M, L, K]             # 2番42（本件売却部分）
S58 = [H, L, M]                      # 2番58
S59 = [D, J, K]                      # 2番59
assert abs(area(KOU) - 413.325) < 1e-6 and abs(area(RO) - 21.1533) < 1e-6 and abs(area(KOU1) - 392.1763) < 1e-6
assert abs(area(OTSU) - 344.82215) < 1e-6 and chiseki(area(URI)) == 352.29
assert chiseki(area(S58)) == 9.64 and chiseki(area(S59)) == 4.02 and chiseki(area(OTSU1)) == 365.97
assert round(344.84 + chiseki(area(RO)), 2) == 365.99 and round(413.30 - 21.15, 2) == 392.15
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'DJ': (D, J, '1.77'), 'JC': (J, C, '14.33'), 'CB': (C, B, '24.78'), 'BM': (B, M, '13.88'),
         'MH': (M, H, '3.19'), 'HL': (H, L, '6.84'), 'LK': (L, K, '14.16'), 'KD': (K, D, '4.79'),
         'JK': (J, K, '4.56'), 'LM': (L, M, '6.05')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
print('数値の照合: すべて一致')

KUI = {'A': 'concrete', 'C': 'concrete', 'D': 'concrete', 'E': 'concrete', 'F': 'concrete', 'H': 'concrete',
       'I': 'concrete', 'B': 'metal', 'G': 'concrete', 'M': 'concrete', 'N': 'concrete', 'K': 'concrete',
       'L': 'concrete', 'J': 'metal'}


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def board(h=9, title=''):
    setup_font()
    f = plt.figure(figsize=(16, h), dpi=100)
    f.patch.set_facecolor('white')
    f.suptitle(title, fontsize=24, weight='bold', y=0.965)
    a = f.add_axes([0.03, 0.08, 0.94, 0.82])
    a.set_xlim(0, 100)
    a.set_ylim(0, 100)
    a.axis('off')
    return f, a


def put_board(f, name):
    path = os.path.join(OUT, name)
    f.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {name}: 整理図（固定配置）\n  →', path)


def rbox(a, x, y, w, h, head, body, col, fs_h=16, fs_b=13.5, fc_alpha=0.10):
    a.add_patch(Rectangle((x, y), w, h, facecolor=col, alpha=fc_alpha, edgecolor=col, lw=2))
    a.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor=col, lw=2))
    a.text(x + 1.5, y + h - 2.5, head, ha='left', va='top', fontsize=fs_h, color=col, weight='bold')
    if body:
        a.text(x + 1.5, y + h - 10, body, ha='left', va='top', fontsize=fs_b, linespacing=1.6, color=BLACK)


def arrow(a, x0, y0, x1, y1, col=GRAY):
    a.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=col))


def pts_label(z, names, away, color=BLACK):
    for n in names:
        p = globals()[n]
        z.point(p, KUI.get(n, 'dot'), color=color)
        z.point_label(p, n, away=away, color=color)


ALL = []

# ---- zu01：時系列（第1章） ----
fig, ax = board(10, '時系列　日付が申請人の住所・記号欄・申請できる時期を決める')
EV = [(4, '平成18年9月28日', '相続で佑介・由里香が\n2分の1ずつ共有\n（受付第36714号）', GRAY, 1),
      (17, '令和6年7月4日', '由里香の持分を\n佑介が相続で取得\n（受付第22986号）', GRAY, -1),
      (30, '令和8年5月9日', '住所の変更の登記\n（N町→A町）', BLUE, 1),
      (42, '6月19日', '2番56・2番57の\n表題登記', GRAY, -1),
      (54, '7月14日', '鈴木純子と\n売買契約', GRAY, 1),
      (66, '8月20日', '本件登記1\n（分合筆）', RED, -1),
      (79, '10月19日', 'C点の筆界の\n認識が一致', BLUE, 1),
      (93, '11月5日', '本件登記2\n（乙土地の分筆）', RED, -1)]
ax.annotate('', xy=(99, 58), xytext=(1, 58), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, t, col, ud in EV:
    ax.plot([x], [58], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [58, 58 + ud * 7], color=col, lw=1.4)
    ax.text(x, 58 + ud * 8, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=13, color=col, weight='bold')
    ax.text(x, 58 + ud * 13.5, t, ha='center', va='bottom' if ud > 0 else 'top', fontsize=12, color=BLACK,
            linespacing=1.5)
rbox(ax, 1, 1, 48, 24, '8月20日の本件登記1に効くこと',
     '・申請人の住所は今のA町二丁目2番19号（5月9日に変更済み）\n・甲土地の登記識別情報は順位2（イ）と順位3（エ）\n・C点はまだ未確定でも、地積測量図は甲土地だけ', RED)
rbox(ax, 51, 1, 48, 24, '11月5日の本件登記2に効くこと',
     '・10月19日にC点の筆界が一致してから申請\n・分筆前の2番42は本件登記1の後の365.99㎡\n・I点は筆界点ではなくなっている', BLUE)
put_board(fig, 'R8_dai21mon_zu01_jikeiretsu.png')

# ---- zu02：全体図 ----
fig, (ax,) = new_figure('北を上にして描き直した全体図（依頼を受けた時点）',
                        '甲土地2番19と乙土地2番42の筆界は、D→I→Hの「く」の字。売る本件売却部分は、J・K・L・Mの線（赤の破線）より東。\n'
                        'D・J・CはX＝510.78、F・H・M・BはX＝486.05の真東向きの線の上。南の帯は2番56（東）・2番57（西）。N点の位置は模式。')
z = Zu(ax)
fit(ax, [A, B, C, D, E, F, G, H, I, J, M, T1, T2], margin=0.08, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly([A, B, M, N], color=GRAY, lw=1.2)
z.poly([N, M, H, F, G], color=GRAY, lw=1.2)
z.poly([J, K, L, M], closed=False, color=RED, lw=2.2, ls='--')
z.north_arrow()
z.free_text(centroid(KOU) + P(4, 0), '甲土地 2番19\n宅地 413.30㎡', fs=16)
z.free_text(centroid(OTSU) + P(-3, 3), '乙土地 2番42\n宅地 344.84㎡', fs=16)
z.free_text((A + M) / 2, '2番56', fs=12, color=GRAY)
z.free_text((G + H) / 2, '2番57', fs=12, color=GRAY)
for n in ['D', 'E', 'F', 'H', 'I', 'J', 'B', 'M', 'C']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=centroid(KOU + OTSU))
for n in ['K', 'L']:
    z.point(globals()[n], 'dot', color=RED)
    z.point_label(globals()[n], n, away=I, color=RED)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=centroid(OTSU))
z.edge_label(E, D, '2－18', centroid(KOU), fs=14, dists=(22, 30), rotate=False, ts=(0.4, 0.3))
z.edge_label(D, C, '2－41', centroid(OTSU), fs=14, dists=(22, 30), rotate=False)
z.edge_label(C, B, '2－43', centroid(OTSU), fs=14, dists=(24, 32), rotate=False)
z.edge_label(F, E, '3－14', centroid(KOU), fs=14, dists=(28, 36), rotate=False)
z.edge_label(G, A, '市道', centroid(KOU), fs=14, dists=(40, 50), rotate=False)
ALL += save(fig, [z], 'R8_dai21mon_zu02_zentaizu.png')

# ---- zu03：注の仕分け ----
fig, ax = board(11, '注は2系統　問題文の注1〜8と、調査図素図の注1〜5')
BOX = [
    (1, 55, 31, 41, '毎年ほぼ同じ決まり文句', '問題文の注1　行為・書類は全て適法\n問題文の注2　書面申請\n問題文の注8　訂正・加入・削除の\n　仕方', GRAY),
    (34, 55, 31, 41, '計算の条件', '問題文の注3　座標値は小数第3位を\n　四捨五入\n問題文の注4　縮尺250分の1、\n　筆界点間の距離は小数第3位を\n　四捨五入', BLUE),
    (67, 55, 32, 41, '地積測量図に書かないもの', '問題文の注5　座標値・座標系の番号・\n　地積と求積方法・測量年月日は不要\n問題文の注6　M市基準点は位置と\n　点名だけ（座標値は書かない）', GREEN),
    (1, 3, 40, 47, '今年の答えに効く指示', '問題文の注7　新しい地番が1つなら\n　2番58、複数なら面積が大きい順に\n　2番58、2番59\n→ 11月の分筆の三角形2つの地番', RED),
    (43, 3, 56, 47, '点の条件（調査図素図の注）', '調査図素図の注1　AとGの直線上にN\n調査図素図の注2　BとFの直線上にH・M\n調査図素図の注3　CとDの直線上にJ（C点の検算に使える）\n調査図素図の注4　KはJL上かつDI上（2直線の交点）\n調査図素図の注5　LはHI上で、MからX軸方向に6.05m', ORANGE),
]
for x, y, w, h, t, b, col in BOX:
    rbox(ax, x, y, w, h, t, b, col)
fig.text(0.5, 0.025, '記事では「問題文の注○」「調査図素図の注○」と言い分ける（「注3」だけでは、どちらの注か分からない）', ha='center',
         fontsize=14, color=GRAY)
put_board(fig, 'R8_dai21mon_zu03_chuu_shiwake.png')

# ---- zu04：規則第72条第1項（ア） ----
fig, ax = board(10, '問1　本人確認情報で明らかにすること（不動産登記規則第72条第1項）')
rbox(ax, 1, 66, 98, 26, '第1号（いつも）', '資格者代理人が申請人と面談した日時、場所及びその状況', GRAY)
rbox(ax, 1, 30, 48, 32, '第2号（氏名を知り、面識があるとき）', '氏名を知り、面識がある旨と、\nその面識が生じた経緯', GRAY)
rbox(ax, 51, 30, 48, 32, '第3号（氏名を知らず、又は面識がないとき）', '第2項の書類の提示を受けて、その内容と、\n申請の権限を有する（ア）登記名義人で\nあると認めた理由', RED)
rbox(ax, 1, 2, 98, 24, '（ア）は「登記名義人」', '本人確認情報は登記識別情報の代わり（不動産登記法第23条第4項第1号）。確かめるのは、申請に来た人が\n登記記録に載っている人かどうか。「所有者」ではなく「登記名義人」', RED)
put_board(fig, 'R8_dai21mon_zu04_kisoku72_1.png')

# ---- zu05：本人確認の書類（第2項第1号と第2号） ----
fig, ax = board(10, '問1　確認の書類　1つでよい第1号と、2つ以上要る第2号')
rbox(ax, 1, 34, 48, 58, '第72条第2項第1号（いずれか一以上）',
     '（イ）運転免許証\n（ウ）個人番号カード\n（エ）旅券等（旅券・乗員手帳）\n在留カード\n特別永住者証明書\n運転経歴証明書', RED, fs_b=15)
rbox(ax, 51, 34, 48, 58, '第72条第2項第2号（いずれか二以上）',
     '健康保険などの資格確認書（書面のもの）\n介護保険の被保険者証\n基礎年金番号通知書\n母子健康手帳、身体障害者手帳\nなど（氏名・住所・生年月日の記載）', GRAY, fs_b=15)
rbox(ax, 1, 2, 98, 26, '問題文の合図', '「（イ）、（ウ）、（エ）、又は在留カード、特別永住者証明書、運転経歴証明書があり、これらのいずれか一以上」\n→ 第1号の書類で、後ろの3つが書いてあるので、前の3つ（運転免許証・個人番号カード・旅券等）が入る。\n保険証（資格確認書）は第2号なので入らない', BLUE)
put_board(fig, 'R8_dai21mon_zu05_shorui.png')

# ---- zu06：L点 ----
fig, (ax,) = new_figure('問2　L点の求め方（Mから真北に6.05m、HI上の点）',
                        'X軸方向は北。LのX座標は 486.05 ＋ 6.05 ＝ 492.10。HからIへ進むとX座標は12.48増えるので、L ＝ H ＋ (I − H) × 6.05 ÷ 12.48。\n'
                        'L（492.10, 491.31）はMの真北。Hから斜めに6.05m測った点（491.40, 490.94）はMの真北にない（灰色）。')
z = Zu(ax)
fit(ax, [H, I, M, L, Lw, K, D, B], margin=0.10, pad_aspect=True)
z.poly([D, I, H], closed=False, lw=2.0)
z.line(H, B, color=GRAY, lw=1.4)
z.line(M, L, color=RED, lw=2.2)
z.north_arrow()
z.right_angle(M, H, L, size=0.5, color=RED)
for n in ['D', 'I', 'H', 'M']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=(H + I) / 2 + P(2, 3))
z.point(L, 'dot', color=RED)
z.callout(L, 'L（492.10, 491.31）', dirs=(0, 20, -20), color=RED, dists=(70, 90))
z.point(Lw, 'dot', color=GRAY)
z.callout(Lw, '誤り（491.40, 490.94）\nHから斜めに6.05m', dirs=(-160, 180, -140), color=GRAY, dists=(70, 90, 110))
z.edge_label(M, L, '6.05', I, color=RED, fs=15, dists=(16, 22))
ALL += save(fig, [z], 'R8_dai21mon_zu06_L_ten.png')

# ---- zu07：K点 ----
fig, (ax,) = new_figure('問2　K点の求め方（直線JLと直線DIの交点）',
                        't ＝ Conjg(D − J) × (I − D) のiの係数 ÷ Conjg(L − J) × (I − D) のiの係数 ＝ −21.6825 ÷ −88.9943。K ＝ J ＋ (L − J) × t ＝（506.23, 492.18）。\n'
                        'JLは北へ18.68進む間に東へ1.15ずれる。Jの真南に下ろした点（505.37, 492.46）はJLの線から外れる（灰色）。')
z = Zu(ax)
fit(ax, [D, J, I, L, K, Kw, H], margin=0.10, pad_aspect=True)
z.poly([D, I, H], closed=False, lw=2.0)
z.line(J, L, color=RED, lw=2.2, ls='--')
z.line(J, Kw, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
for n in ['D', 'I', 'H', 'J']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=(K + I) / 2)
z.point(L, 'dot', color=RED)
z.point_label(L, 'L', away=I, color=RED)
z.point(K, 'dot', color=RED)
z.callout(K, 'K（506.23, 492.18）', dirs=(0, 20, -20), color=RED, dists=(80, 100))
z.point(Kw, 'dot', color=GRAY)
z.callout(Kw, '誤り（505.37, 492.46）\nJの真南', dirs=(160, 180, 140), color=GRAY, dists=(70, 90, 110))
ALL += save(fig, [z], 'R8_dai21mon_zu07_K_ten.png')

# =====================================================================
# 2026-10-20追加（K点に全く手が出なかった人への会話に合わせた図。画像の中に図番は入れない）
#   zu08 条件の数え方、zu09 補助線（高さの比）、zu10 5つの型、zu11 手が止まったときの手順
# =====================================================================
UDI = (I - D) / abs(I - D)
FJ = D + UDI * ((J - D) / UDI).real           # Jから直線DIへの垂線の足
FL = D + UDI * ((L - D) / UDI).real           # Lから直線DIへの垂線の足
TJ = ((J - D).conjugate() * (I - D)).imag     # 三角形D・I・Jの面積の2倍
TL = ((L - D).conjugate() * (I - D)).imag     # 三角形D・I・Lの面積の2倍
assert round(TJ, 4) == 21.6825 and round(TL, 4) == -67.3118 and round(TJ - TL, 4) == 88.9943
assert abs(r2(J + (L - J) * TJ / (TJ - TL)) - K) < 1e-9
assert f'{abs(J - FJ):.2f}' == '1.68' and f'{abs(L - FL):.2f}' == '5.22'
assert abs(((K - D) / (I - D)).real - 0.3714) < 1e-3 and abs(21.6825 / 88.9943 - 0.2436) < 1e-4

# ---- zu08：条件を2つ探す ----
fig, ax = board(11, '問2　座標が省略された点は、条件を2つ探す')
ROWS8 = [('「AとBを結ぶ直線上」', '直線ABの上'), ('「ABの延長線上」', '直線ABをA・Bの先まで延ばした線の上'),
         ('「Aから○mの位置」', 'Aを中心とする半径○mの円の上\n（向きの条件がもう1つ要る）'),
         ('「X軸方向に○m」', 'X座標が決まる（真北・真南）'), ('「ABに平行で○m離れた」', 'ABに平行な直線の上'),
         ('「Aから直線BCへの垂線」', '垂線の足（直角）'), ('「面積が○㎡」「○倍」', '面積の式から t が決まる')]
ax.text(1, 95, '注の言い回しを、図形の言葉に訳す', fontsize=17, weight='bold', color=BLUE, va='center')
for i, (w1, w2) in enumerate(ROWS8):
    y = 87 - i * 9
    ax.add_patch(Rectangle((1, y - 4), 21, 8, facecolor='#eef3fb', edgecolor=BLUE, lw=1.2))
    ax.add_patch(Rectangle((22, y - 4), 30, 8, facecolor='white', edgecolor=BLUE, lw=1.2))
    ax.text(11.5, y, w1, ha='center', va='center', fontsize=12.5)
    ax.text(23, y, w2, ha='left', va='center', fontsize=12)
rbox(ax, 55, 62, 44, 34, 'K点（調査図素図の注4）',
     '条件1　JとLを結ぶ直線の上\n条件2　DとIを結ぶ直線の上\n→ 条件が2つ ＝ 2直線の交点', RED, fs_b=15)
rbox(ax, 55, 26, 44, 34, 'L点（調査図素図の注5）',
     '条件1　HとIを結ぶ直線の上\n条件2　MからX軸方向に6.05m（X＝492.10）\n→ 条件が2つ ＝ 線と線の交点', ORANGE, fs_b=15)
rbox(ax, 55, 2, 44, 22, '芋づる（分からない点を先に）', 'K ← L ← H・I・M\nK点の条件のうち座標がないのはLだけ', BLUE, fs_b=15)
ax.text(26, 13, '平面の点は、X座標とY座標の2つで決まる。\n条件が1つなら、まだ読んでいない文がある。\n3つあれば、余りは検算に使う', ha='center',
        va='center', fontsize=15, linespacing=1.7, weight='bold')
put_board(fig, 'R8_dai21mon_zu08_K_jouken.png')

# ---- zu09：補助線（高さの比） ----
DIe0, DIe1 = D + (D - I) * 0.12, FL + (FL - D) / abs(FL - D) * 1.2
fig, (ax,) = new_figure('問2　補助線で交点の式を作り直す（DIを延ばし、J・Lから垂線）',
                        '底辺DIが共通なので、面積の2倍の比 ＝ 高さの比。J側 ＋21.6825、L側 −67.3118（符号が逆 ＝ DIの反対側）。\n'
                        'JK：KL ＝ 21.6825：67.3118、t ＝ 21.6825 ÷ (21.6825 ＋ 67.3118) ＝ 21.6825 ÷ 88.9943 → K（506.23, 492.18）。分母は交点の式と同じ。')
z = Zu(ax)
fit(ax, [D, J, I, L, K, FJ, FL, DIe0, DIe1], margin=0.10, pad_aspect=True)
z.poly([D, I, J], lw=0.8, fill=ORANGE, color=ORANGE)
z.poly([D, I, L], lw=0.8, fill=BLUE, color=BLUE)
z.line(DIe0, DIe1, color=GRAY, lw=1.4, ls='--')
z.line(D, I, lw=2.4)
z.line(J, L, color=RED, lw=2.2)
z.line(J, FJ, color=ORANGE, lw=1.8, ls=':')
z.line(L, FL, color=BLUE, lw=1.8, ls=':')
z.right_angle(FJ, I, J, size=0.35, color=ORANGE)
z.right_angle(FL, D, L, size=0.45, color=BLUE)
z.north_arrow()
for n in ['D', 'I', 'J']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=K)
z.point(L, 'dot', color=BLUE)
z.point_label(L, 'L', away=K, color=BLUE)
z.point(K, 'dot', color=RED)
z.callout(K, 'K（506.23, 492.18）', dirs=(-150, -170, -130), color=RED, dists=(80, 100, 120))
z.callout((J + FJ) / 2, '高さ1.68', dirs=(60, 80, 40, 100), color=ORANGE, dists=(50, 70, 90), fs=14)
z.edge_label(L, FL, '高さ5.22', I, color=BLUE, fs=14)
z.callout((D + I + J) / 3, '△DIJ × 2 ＝ 21.6825', dirs=(20, 0, 40), color=ORANGE, dists=(90, 110, 130), fs=13)
z.callout((D + I + L) / 3 + (L - I) * 0.1, '△DIL × 2 ＝ 67.3118', dirs=(160, 180, 140), color=BLUE, dists=(90, 110, 130), fs=13)
z.free_text(DIe1, 'DIの延長（補助線）', fs=13, color=GRAY, ha='left', offsets=((12, 0), (12, 16), (12, -16)))
ALL += save(fig, [z], 'R8_dai21mon_zu09_K_hojosen.png')

# ---- zu10：5つの型 ----
fig, ax = board(12, '座標が省略された点の5つの型（第21問の過去問から）')
HD10 = ['型', '注の言い回し', '過去の出題', '式の形']
XS10, WS10 = [1, 17, 43, 73], [16, 26, 30, 26]
ROWS10 = [('2直線の交点', '「〜を結ぶ直線上で、かつ〜」\n「〜の延長と〜の交点」', 'R8 K点、R3 H点、\nH30 I点、H28 J点', 'J ＋ (L − J) × t\nt はiの係数の比'),
          ('直線上で\n決まった距離', '「〜の延長線上、〜から○m」\n「〜の方向に○m」', 'H24 K点、H22 K点、\nR8 L点（軸方向）', 'P ＋ (Q − P) ÷ Abs(Q − P)\n× 距離'),
          ('平行で決まった\n幅だけ離れた直線', '「〜に平行で、〜側に\n○m離れた直線」', 'R5 B点・H点、\nH29 H点・I点', '直角に離れた点を作り、\nそこから交点'),
          ('垂線の足', '「〜から〜への垂線」', 'R1 G点、H20 F点', 'F ＋ (H − F) × w の実部\nw ＝ (E − F) ÷ (H − F)'),
          ('面積の条件', '「面積が〜倍」「面積を\n変えない」「2等分」', 'H24 L点、H21 J点、\nR7 2等分', '面積の比例で t')]
for j, hd in enumerate(HD10):
    ax.add_patch(Rectangle((XS10[j], 88), WS10[j], 8, facecolor='#eeeeee', edgecolor=BLACK, lw=1.2))
    ax.text(XS10[j] + WS10[j] / 2, 92, hd, ha='center', va='center', fontsize=16, weight='bold')
for i, row in enumerate(ROWS10):
    y = 88 - (i + 1) * 14
    for j, t in enumerate(row):
        hl = (i == 0 and j == 2) or (i == 1 and j == 2)
        ax.add_patch(Rectangle((XS10[j], y), WS10[j], 14, facecolor=('#fdeeee' if hl else 'white'), edgecolor=BLACK, lw=1.0))
        ax.text(XS10[j] + WS10[j] / 2, y + 7, t, ha='center', va='center', fontsize=13.5, linespacing=1.5,
                weight=('bold' if j == 0 else 'normal'), color=(RED if hl else BLACK))
ax.text(50, 9, '型を覚えたら「どこをひねったか」を探す。ひねりがわなになる。\n'
        'R8のL点：Hからではなく Mから、斜めではなく軸方向。R8のK点：ほとんど真南だけど真南ではない',
        ha='center', va='center', fontsize=15, linespacing=1.7, weight='bold')
put_board(fig, 'R8_dai21mon_zu10_K_pattern.png')

# ---- zu11：手が止まったときの手順 ----
fig, ax = board(13, '本番で手が止まったときの手順（初見の点でも手を動かす）')
STEPS11 = [('① その点について書いた文を全部抜き出す', '調査図素図の注・問題文の注・図の書き込み・事実関係（K点なら調査図素図の注4）'),
           ('② 図形の言葉に訳す', '「直線上」→直線、「○mの位置」→円、「軸方向に○m」→X座標、「平行」「垂線」「面積」'),
           ('③ 条件を2つそろえる', '足りなければ、条件に出てくる分からない点を先に（芋づる K ← L ← H・I・M）'),
           ('④ 大きく描いて線を延ばし、補助線を引く', '問題用紙の図は線が途中で切れている。延長・垂線・平行線を描き足す'),
           ('⑤ 5つの型に当てる', '交点・直線上の距離・平行で離れた直線・垂線の足・面積の条件（組み合わせもある）'),
           ('⑥ 見当をつけてから計算し、検算する', '見当の近くか、t が0と1の間か、もう1つの条件の上にあるか')]
for i, (head, body) in enumerate(STEPS11):
    y = 89 - i * 14.2
    ec = RED if i in (1, 3) else BLUE
    ax.add_patch(Rectangle((4, y - 5.6), 92, 11.2, facecolor=ec, alpha=0.08, edgecolor=ec, lw=2))
    ax.text(6, y + 2.0, head, ha='left', va='center', fontsize=18, weight='bold', color=BLACK)
    ax.text(6, y - 2.7, body, ha='left', va='center', fontsize=14, color=BLACK)
    if i < len(STEPS11) - 1:
        arrow(ax, 50, y - 5.8, 50, y - 8.4)
        if i == 2:
            ax.text(52.5, y - 7.1, '←　ここまで3分。浮かばなければ、続けるか他の欄に移るかを判断', ha='left', va='center',
                    fontsize=14, weight='bold', color=RED)
fig.text(0.5, 0.05, '①〜③を3分やって浮かばなければ判断：K点にぶら下がる欄の多さと、K点なしで書ける欄（問1・問3の多くの欄・問4のC点）の残りを比べ、\n'
         '移るなら「K ← L ← H・I・M、交点？」とメモを残して、戻ったら続きから',
         ha='center', va='center', fontsize=15, weight='bold', linespacing=1.6)
put_board(fig, 'R8_dai21mon_zu11_K_mayottara.png')

# ---- zu12：申請件数と登録免許税 ----
fig, ax = board(9, '問3　本件登記1は分合筆の1件　登録免許税2,000円')
rbox(ax, 1, 50, 98, 42, '分筆してから合筆（2件）＝ 誤り',
     '① 甲土地から三角形I・K・Lを分筆：分筆後2筆 × 1,000円 ＝ 2,000円\n② 三角形を乙土地に合筆：合筆後1筆 × 1,000円 ＝ 1,000円　　合計 3,000円', GRAY)
rbox(ax, 1, 3, 98, 42, '分合筆（1件）＝ 正解',
     '甲土地の一部を分筆して、そのまま乙土地に合筆する。一の申請情報で申請できる（不動産登記規則第35条第1号）\n'
     '分合筆の後に残るのは（イ）2番19と合筆後の2番42の2筆 × 1,000円 ＝ 2,000円（登録免許税法別表第一の一の（十三））\n'
     '登記の目的は「土地分合筆登記」。三角形は地番を付けずに乙土地に入る', RED)
put_board(fig, 'R8_dai21mon_zu12_kensuu.png')

# ---- zu13：合筆の制限 ----
fig, ax = board(10, '問3　合筆の制限（不動産登記法第41条）に当たるか　甲土地と乙土地')
ROWS = [('第1号', '相互に接続していない土地', '接している（D→I→Hが共通の筆界）', '当たらない'),
        ('第2号', '地目又は地番区域が異なる', 'どちらも宅地、M市A町二丁目', '当たらない'),
        ('第3号', '所有権の登記名義人が異なる', 'どちらも佐藤佑介だけ', '当たらない'),
        ('第4号', '登記名義人の持分が異なる', '共有ではない（由里香の持分も取得済み）', '当たらない'),
        ('第5号', '所有権の登記がない土地とある土地', 'どちらも所有権の登記あり', '当たらない'),
        ('第6号', '所有権以外の権利の登記がある土地', '乙区はどちらも登記事項なし', '当たらない')]
xs_ = [1, 11, 41, 80]
ws_ = [10, 30, 39, 19]
for j, hd in enumerate(['号', '合筆できない土地', '甲土地・乙土地', '判定']):
    ax.add_patch(Rectangle((xs_[j], 86), ws_[j], 9, facecolor='#eeeeee', edgecolor=BLACK, lw=1.2))
    ax.text(xs_[j] + ws_[j] / 2, 90.5, hd, ha='center', va='center', fontsize=15, weight='bold')
for i, row in enumerate(ROWS):
    y = 86 - (i + 1) * 10
    for j, t in enumerate(row):
        fc = '#fdeeee' if i == 1 else 'white'
        ax.add_patch(Rectangle((xs_[j], y), ws_[j], 10, facecolor=fc, edgecolor=BLACK, lw=1.0))
        ax.text(xs_[j] + (ws_[j] / 2 if j in (0, 3) else 1.0), y + 5, t, ha='center' if j in (0, 3) else 'left', va='center',
                fontsize=13, color=(GREEN if j == 3 else BLACK), weight=('bold' if j == 3 else 'normal'))
ax.text(50, 14, '乙土地は「主に家庭菜園」でも、自宅の庭続きなら建物の効用を果たす土地で宅地（準則第68条第3号）。', ha='center',
        va='center', fontsize=14.5, color=RED, weight='bold')
ax.text(50, 6, '畑と決めつけて地目変更を付けない → 甲土地の一部と乙土地は合筆できる', ha='center', va='center', fontsize=15,
        weight='bold')
put_board(fig, 'R8_dai21mon_zu13_goppitsu_seigen.png')

# ---- zu14：8月と11月の地積測量図の範囲 ----
fig, (ax1, ax2) = new_figure('問3　8月の本件登記1は、C点が決まる前に申請できる',
                             '分合筆の地積測量図は、分筆される甲土地だけを描く（不動産登記規則第78条）。乙土地は三角形を受け取るだけなので、C点が要らない。\n'
                             '11月の本件登記2は乙土地を分筆するので、乙土地全体（C点を含む）を描く。だから10月19日の筆界の一致を待った。',
                             ncols=2)
zs = []
for ax, aug in [(ax1, True), (ax2, False)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [E, D, C, B, F, H, I], margin=0.16, pad_aspect=True)
    z.north_arrow(length=0.07)
    if aug:
        ax.set_title('8月20日 本件登記1（分合筆）', fontsize=18, color=RED, weight='bold', pad=6)
        z.poly(KOU, lw=2.4, fill=GREEN)
        z.poly(OTSU, color=GRAY, lw=1.0, ls=':')
        z.line(K, L, color=RED, lw=2.2)
        z.free_text(centroid(KOU), '描くのは\n甲土地だけ', fs=15)
        z.free_text(centroid(OTSU) + P(-6, 4), '乙土地は\n描かない', fs=13, color=GRAY, offsets=((0, 0), (0, -20), (10, 10), (-10, -30)))
        z.point(C, 'dot', color=GRAY)
        z.callout(C, 'C点は未確定\nでも申請できる', dirs=(-100, -120, -80, -140), color=GRAY, dists=(60, 80, 100, 130), fs=13)
    else:
        ax.set_title('11月5日 本件登記2（乙土地の分筆）', fontsize=18, color=BLUE, weight='bold', pad=6)
        z.poly(OTSU1, lw=2.4, fill=BLUE)
        z.poly(KOU1, color=GRAY, lw=1.0, ls=':')
        z.line(J, K, color=RED, lw=2.2)
        z.line(L, M, color=RED, lw=2.2)
        z.free_text(centroid(URI), '描くのは\n乙土地全体', fs=15)
        z.point(C, 'concrete')
        z.callout(C, 'C点が要る\n（10月19日に一致）', dirs=(-100, -120, -80, -140), color=BLUE, dists=(60, 80, 100, 130), fs=13)
    zs.append(z)
ALL += save(fig, zs, 'R8_dai21mon_zu14_chiseki_hani_8gatsu.png')

# ---- zu16：公差の判定 ----
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問3　地積更正が要るかの判定（市街地地域なので精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
for i, (name, reg, meas, k2, mlab) in enumerate([('甲土地 2番19', 413.30, 413.325, 1.93, '413.325'),
                                                 ('乙土地 2番42', 344.84, 344.82215, 1.73, '344.8221…')]):
    ax = fig.add_axes([0.06, 0.55 - i * 0.33, 0.88, 0.27])
    ax.set_xlim(reg - 2.6, reg + 2.6)
    ax.set_ylim(-1.6, 2.0)
    ax.axis('off')
    ax.plot([reg - 2.5, reg + 2.5], [0, 0], color=BLACK, lw=2)
    for j in range(-5, 6):
        v = reg + j * 0.5
        ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.0)
        ax.text(v, -0.3, f'{v:.2f}', ha='center', va='top', fontsize=12, color=GRAY)
    ax.axvspan(reg - k2, reg + k2, ymin=0.40, ymax=0.52, color=GREEN, alpha=0.30)
    ax.text(reg - 2.55, 0.55, name, ha='left', va='center', fontsize=20, weight='bold')
    ax.text(reg - k2, 0.62, f'甲2 の公差 ±{k2:.2f}㎡（問題文の表）', ha='left', va='bottom', fontsize=14, color=GREEN)
    ax.plot([reg], [0], 'o', ms=12, color=BLUE)
    ax.text(reg - 0.05, -0.75, f'登記記録 {reg:.2f}㎡', ha='right', va='top', fontsize=15, color=BLUE, weight='bold')
    ax.plot([meas], [0], 's', ms=10, color=RED)
    ax.text(reg + 0.05, -0.75, f'実測 {mlab}㎡', ha='left', va='top', fontsize=15, color=RED, weight='bold')
    ax.text(reg + 2.5, 0.62, f'差 {abs(meas - reg):.4f}㎡ → 範囲内', ha='right', va='bottom', fontsize=15, color=RED,
            weight='bold')
fig.text(0.5, 0.06, '本件各土地は市街地地域（不動産登記規則第10条第2項第1号）。誤差の限度は精度区分 甲2 まで（同条第4項第1号）。\n'
         'どちらも範囲内 → 地積更正の登記は要らない（準則第72条第1項）。分合筆後の（イ）392.17 ＋（ロ）21.15 ＝ 413.32 でも差0.02㎡',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R8_dai21mon_zu16_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu11: 数直線（固定配置）\n  →', path)

# ---- zu18：（イ）2番19の地積 ----
fig, (ax,) = new_figure('問3　（イ）2番19の地積は、座標で求めた392.17㎡',
                        '分筆後の各土地の地積は、それぞれ座標で求めた面積。登記記録の413.30から（ロ）21.15を引いた残り（392.15）ではない。\n'
                        '（イ）E・D・K・L・H・F ＝ 392.1763 → 392.17㎡、（ロ）I・K・L ＝ 21.1533 → 21.15㎡。合計413.32㎡（登記記録との差0.02㎡）。')
z = Zu(ax)
fit(ax, [E, D, I, H, F], margin=0.10, pad_aspect=True)
z.poly(KOU1, fill=GREEN)
z.poly(RO, color=RED, lw=1.6, ls='--', fill=ORANGE, alpha=0.35, check=False)
z.north_arrow()
for n in ['E', 'D', 'F', 'H', 'I']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=centroid(KOU))
for n in ['K', 'L']:
    z.point(globals()[n], 'dot', color=RED)
    z.point_label(globals()[n], n, away=centroid(KOU), color=RED)
z.free_text(centroid(KOU1), '（イ）2番19\nE・D・K・L・H・Fを座標で求積\n392.17㎡', fs=16, linespacing=1.6)
z.callout(centroid(RO), '（ロ）21.15㎡', dirs=(0, 20, -20), color=RED, dists=(80, 100, 120))
z.callout(E + (F - E) * 0.5, '413.30 − 21.15 ＝ 392.15 は書かない', dirs=(180, 160, -160), color=GRAY,
          dists=(50, 70, 90), fs=14)
ALL += save(fig, [z], 'R8_dai21mon_zu18_i_chiseki.png')

# ---- zu19：合筆後の2番42の地積 ----
fig, (ax1, ax2) = new_figure('問3　合筆後の2番42は、登記記録の344.84 ＋（ロ）21.15 ＝ 365.99㎡',
                             '合筆は合筆先の土地を測り直す登記ではない。乙土地の登記記録は平成10年の三斜求積の値（344.84）で、今回の座標の344.8221…とは別の値。\n'
                             '合筆後の区画D・C・B・H・L・Kを座標で計算した365.97㎡は書かない。',
                             ncols=2)
zs = []
for ax, ok in [(ax1, False), (ax2, True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [D, C, B, H, I, L, K], margin=0.12, pad_aspect=True)
    z.north_arrow(length=0.07)
    if not ok:
        ax.set_title('合筆後の区画を座標で計算（誤り）', fontsize=18, color=GRAY, weight='bold', pad=6)
        z.poly(OTSU1, color=GRAY, lw=2.0, fill=GRAY)
        z.free_text(centroid(OTSU1), '座標で 365.97㎡', fs=16, color=GRAY)
    else:
        ax.set_title('登記記録 ＋（ロ）（正しい）', fontsize=18, color=RED, weight='bold', pad=6)
        z.poly(OTSU, lw=2.0, fill=BLUE)
        z.poly(RO, color=RED, lw=1.6, ls='--', fill=ORANGE, alpha=0.35, check=False)
        z.free_text(centroid(OTSU) + P(0, 2), '登記記録\n344.84㎡', fs=16)
        z.callout(centroid(RO), '（ロ）21.15㎡', dirs=(180, 160, -160), color=RED, dists=(70, 90, 110))
        z.free_text(P(484.0, 497.0), '344.84 ＋ 21.15 ＝ 365.99㎡', fs=16, color=RED)
    for n in ['D', 'C', 'B', 'H']:
        z.point(globals()[n], KUI[n])
        z.point_label(globals()[n], n, away=centroid(OTSU))
    zs.append(z)
ALL += save(fig, zs, 'R8_dai21mon_zu19_gappei_go.png')

# ---- zu20：申請人の住所 ----
fig, ax = board(9, '問3　申請人の住所は、5月9日に変更の登記をした今の住所')
rbox(ax, 1, 52, 31, 40, '登記記録の抜粋', '甲区の佐藤佑介の住所\nM市N町一丁目25番3号\n（抜粋には変更の登記が\n載っていない）', GRAY)
rbox(ax, 35, 52, 30, 40, '令和8年5月9日', '住所についての変更の登記\n（4月20日申請。聴取結果の2）\n本件各土地の両方', BLUE)
rbox(ax, 68, 52, 31, 40, '8月20日の申請書', '申請人\nM市A町二丁目2番19号\n佐藤佑介', RED, fs_b=16)
arrow(ax, 32.5, 72, 34.5, 72)
arrow(ax, 65.5, 72, 67.5, 72)
rbox(ax, 1, 3, 98, 42, 'ワナ', '登記記録の抜粋の「M市N町一丁目25番3号」をそのまま写さない。\n'
     '申請の前（5月9日）に住所の変更の登記が済んでいるので、申請書は今の住所（聴取結果の1）で書き、\n住所の変更を証する情報も要らない', RED)
put_board(fig, 'R8_dai21mon_zu20_juusho.png')

# ---- zu22：甲区の持分の追いかけと記号欄 ----
fig, ax = board(11, '問3　甲土地の甲区を持分ごとに追う　記号欄は「イ、エ」')
rbox(ax, 1, 66, 30, 27, '順位1　昭和41年8月25日', '所有権移転（売買）\n佐藤啓次郎\n→ ア 登記済証', GRAY)
rbox(ax, 35, 66, 30, 27, '順位2　平成18年9月28日', '相続　共有\n佑介 2分の1 → イ\n由里香 2分の1 → ウ', BLUE)
rbox(ax, 69, 66, 30, 27, '順位3　令和6年7月4日', '由里香持分全部移転（相続）\n佑介 2分の1 → エ', BLUE)
arrow(ax, 31.5, 79, 34.5, 79)
arrow(ax, 65.5, 79, 68.5, 79)
rbox(ax, 1, 30, 98, 30, '佐藤佑介の所有権 ＝ 2分の1（順位2）＋ 2分の1（順位3）',
     '合筆の登記識別情報は、合筆に係る土地のうち1筆の分で足りる（不動産登記令第8条第1項第1号・第2項第1号）\n'
     '→ なくした乙土地の分は要らず、甲土地の分を出す。佑介の所有権は2回の登記で取得したので、イとエの両方', RED)
rbox(ax, 1, 2, 98, 23, '入れないもの', 'ア：昭和41年の佐藤啓次郎の登記済証（前の所有者）　ウ：由里香に通知されたもの（由里香の持分は佑介に移った）\n'
     'イだけ：佑介の持分2分の1の分しかない', GRAY)
put_board(fig, 'R8_dai21mon_zu22_kouku_mochibun.png')

# ---- zu25：C点の放射 ----
fig, (ax,) = new_figure('問4　C点の求め方（T2からT1を後視、時計回りに90°04′40″、29.03m）',
                        'arg(T1 − T2) ＝ −89°49′15.97″。90°04′40″を足すと0°15′24.03″でほぼ真北。C ＝ T2 ＋ 29.03∠(arg(T1 − T2) ＋ 90°04′40″) ＝（510.78, 506.79）。\n'
                        'D・J・CはX＝510.78の一直線（調査図素図の注3）で検算。反時計回りに引くと（452.72, 506.61）で市道の南に出る（灰色）。')
z = Zu(ax)
fit(ax, [T1, T2, C, D, Cw, E, B], margin=0.06, pad_aspect=True)
z.poly(OTSU, color=GRAY, lw=1.2, fill=BLUE, alpha=0.12)
z.poly(KOU, color=GRAY, lw=1.2)
z.line(T2, T1, color=GRAY, lw=1.4, ls='--')
z.line(T2, C, color=RED, lw=2.2)
z.line(T2, Cw, color=GRAY, lw=1.4, ls=':')
z.line(D, C, color=BLUE, lw=1.4, ls='--')
z.north_arrow()
z.angle_arc(T2, 4.0, 270 + 10 / 60 + 44.03 / 3600, 360 + 15 / 60 + 24 / 3600, color=RED)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=centroid(OTSU))
for n in ['D', 'J']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=centroid(OTSU))
z.point(C, 'concrete', color=RED)
z.callout(C, 'C（510.78, 506.79）', dirs=(-30, 0, -60), color=RED, dists=(60, 80))
z.point(Cw, 'dot', color=GRAY)
z.callout(Cw, '誤り（452.72, 506.61）\n反時計回りに引いた点', dirs=(180, 160, -160), color=GRAY, dists=(70, 90, 110))
z.edge_label(T2, C, '29.03', centroid(OTSU), color=RED, fs=15, dists=(16, 22))
z.callout(T2 + P(2.5, 3.2), '90°04′40″', dirs=(0, 30, -30), color=RED, dists=(40, 60, 80), fs=14)
ALL += save(fig, [z], 'R8_dai21mon_zu25_C_housha.png')

# ---- zu26：本件登記2は3筆 ----
fig, (ax1, ax2) = new_figure('問5　本件登記2は3筆への分筆（離れた2つの三角形は1筆にできない）',
                             'JKLMの線の西に残るのは、北のD・J・Kと南のH・L・M。間のK・Lは、本件登記1でできた甲土地との筆界で、2つの三角形は接していない。\n'
                             '佐藤さんは甲土地とまとめることも希望しない（聴取結果の9）→ 2番42と三角形2つの3筆。登録免許税は3個で3,000円。',
                             ncols=2)
zs = []
for ax, ok in [(ax1, False), (ax2, True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [D, C, B, H, L, K, M, J], margin=0.18, pad_aspect=True)
    z.north_arrow(length=0.07)
    z.poly(URI, fill=BLUE)
    if not ok:
        ax.set_title('西の残りを1筆にする（誤り）', fontsize=18, color=GRAY, weight='bold', pad=6)
        z.poly(S59, color=GRAY, lw=2.0, fill=GRAY)
        z.poly(S58, color=GRAY, lw=2.0, fill=GRAY)
        z.callout(centroid(S59), '2番58？', dirs=(180, 160), color=GRAY, dists=(60, 80))
        z.callout(centroid(S58), '2番58？', dirs=(180, -160, 160, -140), color=GRAY, dists=(50, 70, 90))
        z.free_text(centroid(URI), '2番42', fs=15)
    else:
        ax.set_title('3筆に分ける（正しい）', fontsize=18, color=RED, weight='bold', pad=6)
        z.poly(S59, color=RED, lw=2.0, fill=ORANGE)
        z.poly(S58, color=RED, lw=2.0, fill=ORANGE)
        z.callout(centroid(S59), '2番59', dirs=(180, 160), color=RED, dists=(60, 80))
        z.callout(centroid(S58), '2番58', dirs=(180, -160), color=RED, dists=(60, 80))
        z.free_text(centroid(URI), '2番42', fs=15)
    for n in ['D', 'J', 'K', 'L', 'M', 'H']:
        z.point(globals()[n], 'dot')
        z.point_label(globals()[n], n, away=centroid(URI))
    zs.append(z)
ALL += save(fig, zs, 'R8_dai21mon_zu26_sanpitsu.png')

# ---- zu27：新しい地番 ----
fig, (ax,) = new_figure('問5　新しい地番は面積の大きい順（問題文の注7）',
                        '本件売却部分は2番42のまま（支号のある土地の分筆は1筆に従来の地番を残す。準則第67条第1項第4号ただし書）。\n'
                        '三角形は面積の大きい順に、南のH・L・M（9.64㎡）が2番58、北のD・J・K（4.02㎡）が2番59。北から順ではない。')
z = Zu(ax)
fit(ax, [D, C, B, H, L, K, M, J], margin=0.10, pad_aspect=True)
z.poly(URI, fill=BLUE)
z.poly(S58, color=RED, lw=2.0, fill=ORANGE)
z.poly(S59, color=RED, lw=2.0, fill=ORANGE)
z.north_arrow()
z.free_text(centroid(URI), '2番42（本件売却部分）\n352.29㎡', fs=16)
z.callout(centroid(S58), '2番58\nH・L・M　9.64㎡', dirs=(180, -160, 160), color=RED, dists=(70, 90, 110))
z.callout(centroid(S59), '2番59\nD・J・K　4.02㎡', dirs=(180, 160, -160), color=RED, dists=(70, 90, 110))
for n in ['D', 'J', 'K', 'L', 'M', 'H', 'C', 'B']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=centroid(URI))
ALL += save(fig, [z], 'R8_dai21mon_zu27_chiban.png')

# ---- zu30：I点は描かない ----
fig, (ax1, ax2) = new_figure('問5　地積測量図に描くのは、11月の分筆前の2番42（I点は描かない）',
                             '本件登記1で、乙土地の西の筆界はD→I→HからD→K→L→Hに変わった。I点は筆界点ではなくなったので描かない。\n'
                             '描くのはD・J・C・B・M・H・L・Kの8点と、分筆線JK・LM。K・Lは甲土地との筆界（分筆線ではない）。',
                             ncols=2)
zs = []
for ax, ok in [(ax1, False), (ax2, True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [D, C, B, H, I], margin=0.12, pad_aspect=True)
    z.north_arrow(length=0.07)
    if not ok:
        ax.set_title('元の乙土地D・C・B・H・Iを描く（誤り）', fontsize=17, color=GRAY, weight='bold', pad=6)
        z.poly(OTSU, color=GRAY, lw=2.0, fill=GRAY)
        z.point(I, 'concrete', color=GRAY)
        z.point_label(I, 'I', away=centroid(OTSU), color=GRAY)
        for n in ['D', 'C', 'B', 'H']:
            z.point(globals()[n], 'dot', color=GRAY)
            z.point_label(globals()[n], n, away=centroid(OTSU), color=GRAY)
    else:
        ax.set_title('11月の分筆前の2番42を描く（正しい）', fontsize=17, color=RED, weight='bold', pad=6)
        z.poly(OTSU1, lw=2.2, fill=BLUE)
        z.line(J, K, color=RED, lw=2.2)
        z.line(L, M, color=RED, lw=2.2)
        z.point(I, 'dot', color='#cccccc')
        for n in ['D', 'J', 'C', 'B', 'M', 'H', 'L', 'K']:
            z.point(globals()[n], 'dot')
            z.point_label(globals()[n], n, away=centroid(URI))
    zs.append(z)
ALL += save(fig, zs, 'R8_dai21mon_zu30_I_egakanai.png')

# ---- zu32：第5欄 地積測量図の完成見本（解答例に再現された答案用紙の第5欄。罫線は解答例のPDFを get_drawings で測ったmm） ----
# 外枠 56.3〜406.9 × 12.2〜274.8mm、図を描く枠 81.3〜383.3 × 26.7〜257.7mm、地番の欄 241.3〜303.3 × 16.7〜26.7、
# 土地の所在の欄 241.3〜383.3 × 26.7〜36.7、下の欄 257.7〜272.2（作成者 81.3〜100.3〜224.3、申請人 240.3〜259.3〜349.1、縮尺 349.6〜359.3〜383.3）
setup_font()
PX0, PX1, PY0, PY1 = 50.0, 413.0, 5.0, 330.0          # 紙の範囲（mm、yは下向き）
fig = plt.figure(figsize=((PX1 - PX0) / 25.4, (PY1 - PY0) / 25.4), dpi=112)
fig.patch.set_facecolor('white')
pa = fig.add_axes([0, 0, 1, 1])
pa.set_xlim(PX0, PX1)
pa.set_ylim(PY1, PY0)
pa.axis('off')


def mrect(x0, y0, x1, y1, lw=1.2):
    pa.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, edgecolor=BLACK, lw=lw))


def mline(x0, y0, x1, y1, lw=1.2):
    pa.plot([x0, x1], [y0, y1], color=BLACK, lw=lw)


def mtext(x, y, s, fs=11, **kw):
    pa.text(x, y, s, fontsize=fs, va='center', **kw)


INKC = '#1a3a8f'
mrect(56.3, 12.2, 406.9, 274.8, lw=0.8)
mrect(57.1, 13.0, 406.1, 274.0, lw=2.0)
mrect(58.6, 16.7, 71.7, 24.4, lw=1.0)
mtext(65.1, 20.6, '第5欄', fs=12, ha='center', weight='bold')
mrect(81.3, 26.7, 383.3, 257.7, lw=1.6)                 # 図を描く枠
mline(232.3, 26.7, 232.3, 36.7)                         # 折り目の印
mline(232.3, 247.7, 232.3, 257.7)
mrect(241.3, 16.7, 303.3, 26.7)                         # 地番の欄
mline(265.3, 16.7, 265.3, 26.7, lw=0.6)
mtext(253.3, 21.7, '地　　番', fs=10.5, ha='center')
mtext(284.3, 21.7, '2番42、2番58、2番59', fs=9, ha='center', color=INKC, weight='bold')
mtext(341.4, 22.7, '地　積　測　量　図', fs=14, ha='center')
mrect(241.3, 26.7, 383.3, 36.7)                         # 土地の所在の欄
mline(265.3, 26.7, 265.3, 36.7, lw=0.6)
mtext(253.3, 31.5, '土地の所在', fs=10.5, ha='center')
mtext(267.5, 31.5, 'Ｍ市Ａ町二丁目', fs=11.5, ha='left', color=INKC, weight='bold')
mrect(81.3, 257.7, 224.3, 272.2)                        # 作成者の欄
mline(100.3, 257.7, 100.3, 272.2, lw=0.6)
mtext(90.8, 264.8, '作 成 者', fs=10, ha='center')
mtext(150.3, 264.8, '（略）', fs=10, ha='center')
mtext(224.0, 268.6, '（令和８年○月○日作成）', fs=9, ha='right')
mrect(240.3, 257.7, 383.3, 272.2)                       # 申請人・縮尺の欄
mline(259.3, 257.7, 259.3, 272.2, lw=0.6)
mtext(249.8, 264.8, '申 請 人', fs=10, ha='center')
mtext(304.2, 264.8, '（略）', fs=10, ha='center')
mline(349.1, 257.7, 349.1, 272.2, lw=0.6)
mline(359.3, 257.7, 359.3, 272.2, lw=0.6)
mtext(354.2, 264.8, '縮尺', fs=9, ha='center')
mline(362.7, 270.2, 379.8, 259.7, lw=0.6)
mtext(369.1, 262.0, '1', fs=9, ha='center')
mtext(374.3, 268.0, '250', fs=9, ha='center')
pa.text((PX0 + PX1) / 2, 305,
        '印刷済み：「第5欄」「地積測量図」、地番・土地の所在の欄の枠、作成者と申請人の「（略）」、作成日の欄、縮尺 1/250（原本の寸法どおり）\n'
        '書くもの：地番（2番42、2番58、2番59）、土地の所在（M市A町二丁目）、図（縮尺1/250で 1m ＝ 4mm）、辺長10本、分筆線JK・LM、符号（イ）（ロ）（ハ）、\n'
        '境界標の記号と凡例、「（単位：ｍ）」、方位記号、隣接地の地番（点で接する2－18・2－55も）、M市基準点T1・T2の位置と点名（問題文の注6）\n'
        '書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）、I点。辺長は小数第3位を四捨五入（LK は 14.1567… なので 14.16）',
        ha='center', va='center', fontsize=10.5, linespacing=1.6)
# 図を描く領域（枠の内側、所在の欄より下）。1/250 なので 1mm ＝ 0.25m
AX0, AX1, AY0, AY1 = 83.0, 381.0, 38.5, 255.5
ax = fig.add_axes([(AX0 - PX0) / (PX1 - PX0), (PY1 - AY1) / (PY1 - PY0), (AX1 - AX0) / (PX1 - PX0), (AY1 - AY0) / (PY1 - PY0)])
ax.axis('off')
ys_ = [p.imag for p in [D, C, B, H, L, K, J, M, T1, T2]]
xs_ = [p.real for p in [D, C, B, H, L, K, J, M, T1, T2]]
cyE, cxN = (min(ys_) + max(ys_)) / 2, (min(xs_) + max(xs_)) / 2
WM, HM = (AX1 - AX0) * 250 / 1000, (AY1 - AY0) * 250 / 1000
ax.set_xlim(cyE - WM / 2, cyE + WM / 2)
ax.set_ylim(cxN - HM / 2, cxN + HM / 2)
assert abs((max(ys_) - min(ys_)) * 4 - 141.44) < 0.1 and abs((max(xs_) - min(xs_)) * 4 - 116.12) < 0.1   # 横141mm・縦116mm
z = Zu(ax, fontsize=11)
z.poly(OTSU1, lw=1.6)
z.line(J, K, lw=1.6)
z.line(L, M, lw=1.6)
z.north_arrow()
cu = centroid(URI)
for n, (p, q, s) in SIDES.items():
    if n in ('JK', 'LM'):
        z.edge_label(p, q, s, cu, fs=10, outward=False, dists=(10, 15, 20))
    elif n in ('HL', 'MH'):
        z.edge_label(p, q, s, centroid(S58), fs=10, dists=(10, 15, 20))
    elif n in ('DJ', 'KD'):
        z.edge_label(p, q, s, centroid(S59), fs=10, dists=(10, 15, 20))
    else:
        z.edge_label(p, q, s, centroid(OTSU1), fs=10, dists=(10, 15, 20))
z.free_text(cu, '（イ）\n2－42', fs=12)
z.callout(centroid(S58), '（ロ）2－58', dirs=(-150, 180, -120), dists=(45, 60, 80), fs=10.5)
z.callout(centroid(S59), '（ハ）2－59', dirs=(-165, 180, -145), dists=(45, 60, 80), fs=10.5)
for n in ['D', 'J', 'C', 'B', 'M', 'H', 'L', 'K']:
    z.point(globals()[n], 'metal' if KUI[n] == 'metal' else 'concrete', size=(7 if KUI[n] == 'metal' else 6))
    z.point_label(globals()[n], n, away=cu, fs=10)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cu, dists=(16, 22, 30), fs=10)
z.edge_label(D, C, '2－41', cu, fs=10.5, dists=(26, 32), rotate=False, ts=(0.6, 0.7))
z.edge_label(C, B, '2－43', cu, fs=10.5, dists=(30, 38), rotate=False)
z.edge_label(B, M, '2－56', cu, fs=10.5, dists=(26, 34), rotate=False)
z.edge_label(M, H, '2－57', cu, fs=10.5, dists=(26, 34), rotate=False)
z.edge_label(L, K, '2－19', cu, fs=10.5, dists=(36, 44, 52), rotate=False)
z.free_text(D, '2－18', fs=10.5, offsets=((-30, 16), (-38, 8), (-24, 26), (-46, 0)))
z.free_text(B, '2－55', fs=10.5, offsets=((26, -18), (34, -10), (22, -28), (42, 0)))
z.free_text(P(cxN - HM / 2 + 1.0, cyE - WM / 2 + 1.0), '（単位：ｍ）\n◎ コンクリート杭：D・C・H・K・L・M\n● 金属標：B・J\n△ 基準点：T1・T2', fs=9.5,
            ha='left', va='bottom', offsets=((0, 0), (0, 14), (14, 0)))
ALL += save(fig, [z], 'R8_dai21mon_zu32_chiseki_sokuryouzu.png')

# ---- zu33：本番で解く順番 ----
fig, ax = board(12, '本番で解く順番　K点がなくても書ける欄を先に')
STEPS = [
    ('① 問1　本人確認情報の穴埋め', '登記名義人・運転免許証・個人番号カード・旅券等（規則第72条。2分）', BLUE),
    ('② 問3　申請書のK点が要らない欄', '登記の目的・添付書類・記号（イ エ）・申請人・登録免許税・所在・1行目413.30・4行目344.84・原因の文言', BLUE),
    ('③ 問4　C点', '放射1回（時計回りに足す）。D・Jと同じX＝510.78で検算', BLUE),
    ('④ 問2　L点・K点と、問3の地積', 'L（492.10, 491.31）→ K（506.23, 492.18）→ 392.17・21.15・365.99', ORANGE),
    ('⑤ 問5　面積3つと辺長10本、作図（いちばん重い）', '352.29・9.64・4.02で地番を決め、T1・T2まで入れて縦116mm × 横141mm', ORANGE),
]
for i, (head, body, ec) in enumerate(STEPS):
    y = 88 - i * 18
    ax.add_patch(Rectangle((5, y - 6.5), 90, 13, facecolor=ec, alpha=0.08, edgecolor=ec, lw=2))
    ax.text(7, y + 2.2, head, ha='left', va='center', fontsize=19, weight='bold', color=BLACK)
    ax.text(7, y - 3.0, body, ha='left', va='center', fontsize=14.5, color=BLACK)
    if i < len(STEPS) - 1:
        arrow(ax, 50, y - 6.8, 50, y - 11.0)
fig.text(0.5, 0.04, '青：K点がなくても書ける　／　橙：K点が要る。K点と作図で手間取っても、青の欄の点は先に取っておける',
         ha='center', va='center', fontsize=16)
put_board(fig, 'R8_dai21mon_zu33_kaku_junban.png')


# =====================================================================
# 2026-10-20追加（解答例との照合で直した会話に合わせた図。画像の中に図番は入れない）
#   zu23 （ロ）の原因は「分割して」、zu24 変わらない地目の欄、zu31 隣接地は角で接する2－18・2－55も
# =====================================================================

# ---- zu23：（ロ）の原因は「分割して」 ----
fig, ax = board(10, '問3　（ロ）の原因は「2番19から分割して2番42に合併する部分」')
rbox(ax, 1, 50, 48, 42, '分筆（11月の本件登記2の2番58・2番59）',
     '分けた土地ごとに地番と登記記録が作られる\n（不動産登記規則第101条第1項）\n→ 新しい行の原因は「2番42から分筆」\n　1筆として登記記録が残る', GRAY)
rbox(ax, 51, 50, 48, 42, '分合筆の（ロ）（8月の本件登記1の三角形I・K・L）',
     '地番も登記記録も作られず、すぐ2番42に入る\n（一度も1筆にならない）\n→ 原因は「2番19から分割して\n　2番42に合併する部分」', RED)
rbox(ax, 1, 3, 98, 40, '申請書の土地の表示（3行目）',
     '①地番：（ロ）（符号だけ）　②地目：書かない　③地積：21.15\n'
     '登記原因：「2番19から分割して2番42に合併する部分」（「分筆して」と書かない）\n'
     '同じ書き方の年度：令和2年度（32番5から分割して32番4に合併する部分）・平成28年度（40番2から分割して32番1に合併する部分）', BLUE)
put_board(fig, 'R8_dai21mon_zu23_bunkatsu.png')

# ---- zu24：変わらない地目の欄 ----
fig, ax = board(10, '問3　分合筆で変わるのは地番・地積・原因　地目は宅地のまま')
ROWS2 = [('1行目', '2番19', '宅地', '413.30', '（空欄）'),
         ('2行目', '（イ）2番19', '宅地（空欄でもよい）', '392.17', '③2番42に一部合併'),
         ('3行目', '（ロ）', '（書かない）', '21.15', '2番19から分割して2番42に合併する部分'),
         ('4行目', '2番42', '宅地', '344.84', '（空欄）'),
         ('5行目', '2番42', '宅地（空欄でもよい）', '365.99', '③2番19から一部合併')]
xs2 = [1, 10, 25, 45, 59]
ws2 = [9, 15, 20, 14, 40]
for j, hd in enumerate(['行', '①地番', '②地目', '③地積', '登記原因及びその日付']):
    ax.add_patch(Rectangle((xs2[j], 84), ws2[j], 9, facecolor='#eeeeee', edgecolor=BLACK, lw=1.2))
    ax.text(xs2[j] + ws2[j] / 2, 88.5, hd, ha='center', va='center', fontsize=15, weight='bold')
for i, row in enumerate(ROWS2):
    y = 84 - (i + 1) * 11
    for j, t in enumerate(row):
        fc = '#eef7ee' if (j == 2 and i in (1, 4)) else 'white'
        ax.add_patch(Rectangle((xs2[j], y), ws2[j], 11, facecolor=fc, edgecolor=BLACK, lw=1.0))
        col = GREEN if (j == 2 and i in (1, 4)) else (RED if j in (3, 4) and i in (1, 2, 4) else BLACK)
        ax.text(xs2[j] + ws2[j] / 2, y + 5.5, t, ha='center', va='center', fontsize=12.5, color=col,
                weight=('bold' if col != BLACK else 'normal'))
ax.text(50, 20, '赤：分合筆で変わる欄（地積・原因）。緑：変わらない地目。宅地と書いても空欄にしても、中身は同じ宅地', ha='center',
        va='center', fontsize=14.5, weight='bold')
ax.text(50, 11, '予備校の解答例は2行目・5行目の地目を空欄にしている（この記事の完成形は「宅地」と記入）。\n'
        '大事なのは、変わる地番・地積・原因を1つも落とさないこと', ha='center', va='center', fontsize=14, linespacing=1.6)
put_board(fig, 'R8_dai21mon_zu24_chimoku_ran.png')

# ---- zu31：隣接地は角で接する2－18・2－55も ----
DN, BE_ = D + P(4.0, 0.0), B + P(0.0, 5.0)     # 隣地の境界線の延長（位置は模式）
fig, (ax,) = new_figure('問5　隣接地の地番は、角（点）で接する2－18・2－55も書く',
                        '辺で接するのは2－41（北）・2－43（東）・2－56と2－57（南）・2－19（西）。D点は2－18の南東の角、B点は2－55の北西の角とも接している。\n'
                        'D点から北・B点から東へ延ばした隣地どうしの境界線（細い灰色）の位置は模式。')
z = Zu(ax)
fit(ax, [D, C, B, H, L, K, M, J, E, A, DN, BE_, F], margin=0.06, pad_aspect=True)
z.poly(OTSU1, lw=2.2, fill=BLUE)
for p, q in [(E, D), (D, DN), (B, BE_), (B, A), (F, H)]:
    z.line(p, q, color=GRAY, lw=1.2)
z.north_arrow()
for n in ['D', 'C', 'B', 'H', 'L', 'K', 'M', 'J']:
    z.point(globals()[n], 'dot', color=(RED if n in 'DB' else BLACK))
    z.point_label(globals()[n], n, away=centroid(OTSU1), color=(RED if n in 'DB' else BLACK))
z.free_text(centroid(OTSU1), '2番42\n（11月の分筆前）', fs=16)
z.free_text(D + P(2.0, -4.0), '2－18', fs=16, color=RED, offsets=((0, 0), (-20, 10), (0, 20)))
z.free_text(B + P(-1.5, 3.0), '2－55', fs=16, color=RED, offsets=((0, 0), (20, -10), (0, -20)))
z.free_text((D + C) / 2 + P(2.2, 0), '2－41', fs=15)
z.free_text((C + B) / 2 + P(0, 3.0), '2－43', fs=15)
z.free_text((B + M) / 2 + P(-1.8, 0), '2－56', fs=15)
z.free_text((M + H) / 2 + P(-1.8, -0.8), '2－57', fs=15)
z.free_text((K + L) / 2 + P(0, -4.0), '2－19', fs=15)
z.callout(D, '点で接する', dirs=(150, 170, 130), color=RED, dists=(70, 90, 110), fs=14)
z.callout(B, '点で接する', dirs=(-30, -10, -50), color=RED, dists=(70, 90, 110), fs=14)
ALL += save(fig, [z], 'R8_dai21mon_zu31_rinsetsu.png')


# =====================================================================
# 2026-10-26追加（品質チェック6-2：計算過程と図の連動、判断ごとの専用の図。画像の中に図番は入れない）
#   zu15 甲土地の面積（座標法5項）、zu17（ロ）三角形の面積、zu21 合筆の登記識別情報は1筆分、
#   zu28 11月の分筆後の合計と公差、zu29 辺長10本（引き算と電卓の使い分け）
# =====================================================================
def term(p, q):
    return (p * q.conjugate()).imag


def kou2(F_):
    """精度区分 甲2 の公差（㎡）。(0.05 ＋ 0.01 × Fの4乗根) × Fの平方根"""
    return (0.05 + 0.01 * F_ ** 0.25) * F_ ** 0.5


assert [f'{kou2(F_):.2f}' for F_ in (413.30, 344.84, 365.99)] == ['1.93', '1.73', '1.79']


def table_panel(ax2, head, rows, foot, foot_col=RED):
    """右側の表（固定配置）。rows は (左の文字, 右の文字, 色)。"""
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.text(2, 96, head, ha='left', va='top', fontsize=17, weight='bold', color=BLUE)
    y = 84
    for lt, rt, col in rows:
        ax2.add_patch(Rectangle((2, y - 5), 96, 9.5, facecolor='#f6f8fb', edgecolor='#c9d3e0', lw=1.0))
        ax2.text(5, y, lt, ha='left', va='center', fontsize=14.5, color=col)
        ax2.text(95, y, rt, ha='right', va='center', fontsize=15, color=col, weight='bold')
        y -= 11
    ax2.text(2, y + 1, foot, ha='left', va='top', fontsize=15, color=foot_col, weight='bold', linespacing=1.7)


# ---- zu15：甲土地の面積（座標法5項） ----
TK = [term(KOU[i], KOU[(i + 1) % 5]) for i in range(5)]
assert [round(v, 4) for v in TK] == [-7198.4424, -8059.1803, -2893.5286, 6707.49, 10617.0113] and round(sum(TK), 4) == -826.65
NK = ['E', 'D', 'I', 'H', 'F']
fig, (ax, ax2) = new_figure('問3　甲土地の実測の面積（座標法　E→D→I→H→Fの5項）',
                            '頂点を順に回り、P・Conjg(次の点) の iの係数だけを足す（実部は使わない）。①〜⑤は記事の電卓の5行と同じ順。\n'
                            '合計 −826.65 の絶対値を2で割って 413.325㎡。符号がマイナスなのは時計回りに回ったから（向きで符号が変わるだけ）。',
                            ncols=2, width_ratios=[1.15, 1])
z = Zu(ax)
fit(ax, KOU, margin=0.10, pad_aspect=True)
z.poly(KOU, lw=2.2, fill=BLUE)
z.north_arrow()
for i, n in enumerate(NK):
    p, q = KOU[i], KOU[(i + 1) % 5]
    z.point(p, KUI[n])
    z.point_label(p, n, away=centroid(KOU))
    z.edge_label(p, q, '①②③④⑤'[i], centroid(KOU), color=RED, fs=17, rotate=False)
z.free_text(centroid(KOU), '甲土地 2番19\n（本件登記1の前）', fs=16)
table_panel(ax2, '各項（P・Conjg(次の点) の iの係数）',
            [(f'{"①②③④⑤"[i]}　{NK[i]}・Conjg({NK[(i + 1) % 5]})', f'{fmt_num(TK[i])}', BLACK) for i in range(5)]
            + [('合計（表示の iの係数）', '−826.65', RED)],
            '|−826.65| ÷ 2 ＝ 413.325㎡\n登記記録 413.30㎡ との差 0.025㎡\n→ 次の図で公差と比べる')
ALL += save(fig, [z], 'R8_dai21mon_zu15_kou_menseki.png')

# ---- zu17：（ロ）三角形I・K・Lの面積 ----
assert disp(K - I) == '7.70 − 2.52i' and disp(L - I) == '−6.43 − 3.39i'
assert disp((K - I).conjugate() * (L - I)) == '−40.9682 − 42.3066i'
fig, (ax, ax2) = new_figure('問3　（ロ）三角形I・K・Lの面積（Iから出る2本の辺で求める）',
                            '三角形は、1つの頂点から出る2本の辺 u ＝ K − I、v ＝ L − I だけで面積が出る。Conjg(u) × v の iの係数が面積の2倍。\n'
                            '42.3066 ÷ 2 ＝ 21.1533 → 宅地は小数第2位未満を切り捨てて 21.15㎡。これが申請書の3行目（ロ）の地積。',
                            ncols=2, width_ratios=[1.0, 1])
z = Zu(ax)
fit(ax, [I, K, L, D, H], margin=0.10, pad_aspect=True)
z.poly([D, I, H], closed=False, color=GRAY, lw=1.2)
z.poly(RO, lw=1.0, fill=ORANGE, color=ORANGE)
z.line(I, K, color=RED, lw=3.0)
z.line(I, L, color=BLUE, lw=3.0)
z.line(K, L, color=GRAY, lw=1.4, ls='--')
z.north_arrow()
for n in ['I', 'D', 'H']:
    z.point(globals()[n], KUI[n])
    z.point_label(globals()[n], n, away=centroid(RO))
for n in ['K', 'L']:
    z.point(globals()[n], 'dot', color=RED)
    z.point_label(globals()[n], n, away=centroid(RO), color=RED)
z.callout((I + K) / 2, 'u ＝ K − I ＝ 7.70 − 2.52i', dirs=(30, 60, 0), color=RED, dists=(70, 90, 110), fs=13)
z.callout((I + L) / 2, 'v ＝ L − I ＝ −6.43 − 3.39i', dirs=(-30, -60, 0), color=BLUE, dists=(70, 90, 110), fs=13)
table_panel(ax2, '電卓の流れ（B＝L点、C＝I点、X＝K点）',
            [('Conjg(K − I) × (L − I)', '−40.9682 − 42.3066i', BLACK), ('読むのは iの係数', '−42.3066', RED),
             ('÷ 2（符号は外す）', '21.1533', BLACK), ('宅地は切り捨て', '21.15㎡', RED)],
            '（イ）を 413.30 − 21.15 で\n出さない（次の図）')
ALL += save(fig, [z], 'R8_dai21mon_zu17_ro_menseki.png')

# ---- zu21：合筆の登記識別情報は1筆分で足りる ----
fig, ax = board(10, '問3　合筆の登記識別情報は、合筆する土地のうち1筆分で足りる')
rbox(ax, 1, 62, 98, 30, '原則（不動産登記令第8条第1項第1号）',
     '合筆は、所有権の登記名義人の登記識別情報を出す登記\n→ そのままだと、甲土地と乙土地の両方の分が要りそうに見える', GRAY)
rbox(ax, 1, 28, 48, 30, '甲土地 2番19（出す）',
     '佐藤さんの持分2分の1ずつ2回の登記\n→ 記号欄はイとエの2つ（次の図）', BLUE)
rbox(ax, 51, 28, 48, 30, '乙土地 2番42（出さない）',
     '登記識別情報をなくしている（聴取結果の3）\n→ 1筆分で足りるので要らない', RED)
rbox(ax, 1, 2, 98, 22, '例外（同条第2項第1号）　合筆に係る土地のうち、いずれか1筆の分で足りる',
     'だから、なくした乙土地の分も、その代わりの本人確認情報（問1の第72条）も、本件登記1には要らない', RED)
put_board(fig, 'R8_dai21mon_zu21_shikibetsu_1hitsu.png')

# ---- zu28：11月の分筆後の合計と公差 ----
setup_font()
fig = plt.figure(figsize=(16, 7), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問5　11月の分筆も地積更正は要らない（分筆後の合計と登記記録を比べる）', fontsize=24, weight='bold', y=0.95)
reg, meas, k2 = 365.99, round(352.29 + 9.64 + 4.02, 2), round(kou2(365.99), 2)
assert meas == 365.95 and k2 == 1.79
ax = fig.add_axes([0.06, 0.42, 0.88, 0.38])
ax.set_xlim(reg - 2.6, reg + 2.6)
ax.set_ylim(-1.6, 2.0)
ax.axis('off')
ax.plot([reg - 2.5, reg + 2.5], [0, 0], color=BLACK, lw=2)
for j in range(-5, 6):
    v = reg + j * 0.5
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.0)
    ax.text(v, -0.3, f'{v:.2f}', ha='center', va='top', fontsize=12, color=GRAY)
ax.axvspan(reg - k2, reg + k2, ymin=0.40, ymax=0.52, color=GREEN, alpha=0.30)
ax.text(reg - 2.55, 0.55, '分筆前の2番42', ha='left', va='center', fontsize=20, weight='bold')
ax.text(reg - k2, 0.62, f'甲2 の公差（参考）±{k2:.2f}㎡', ha='left', va='bottom', fontsize=14, color=GREEN)
ax.plot([reg], [0], 'o', ms=12, color=BLUE)
ax.text(reg + 0.05, -0.75, f'登記記録 {reg:.2f}㎡（本件登記1の後）', ha='left', va='top', fontsize=15, color=BLUE, weight='bold')
ax.plot([meas], [0], 's', ms=10, color=RED)
ax.text(meas - 0.05, -0.75, f'分筆後の合計 {meas:.2f}㎡', ha='right', va='top', fontsize=15, color=RED, weight='bold')
ax.text(reg + 2.5, 0.62, '差 0.04㎡ → 範囲内', ha='right', va='bottom', fontsize=15, color=RED, weight='bold')
fig.text(0.5, 0.17, '分筆後の合計 ＝ 352.29（2番42）＋ 9.64（2番58）＋ 4.02（2番59）＝ 365.95㎡。比べる相手は、本件登記1で登記された365.99㎡。\n'
         '公差は甲2の式（0.05 ＋ 0.01 × Fの4乗根）× Fの平方根 に F ＝ 365.99 を入れた参考値（約1.79㎡）。差0.04㎡は範囲内 → 地積更正は要らない（準則第72条第1項）',
         ha='center', va='center', fontsize=15, linespacing=1.7)
path = os.path.join(OUT, 'R8_dai21mon_zu28_kousa_11gatsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu28: 数直線（固定配置）\n  →', path)

# ---- zu29：辺長10本（引き算と電卓の使い分け） ----
fig, (ax,) = new_figure('問5　地積測量図の辺長10本（軸に平行な辺は引き算、斜めの辺は電卓のAbs）',
                        '青：X座標かY座標が同じ（軸に平行）→ 座標の引き算。DJ 1.77・JC 14.33・BM 13.88・MH 3.19・LM 6.05。\n'
                        '赤：斜めの辺 → Abs で長さ。CB 24.78・LK 14.16（14.1567…の6で切り上げ）・JK 4.56・HL 6.84・KD 4.79。小数第3位を四捨五入（問題文の注4）。')
z = Zu(ax)
fit(ax, OTSU1 + [J], margin=0.08, pad_aspect=True)
z.poly(OTSU1, lw=0.0, fill=BLUE, alpha=0.08, color=BLUE)
AXIS = {'DJ', 'JC', 'BM', 'MH', 'LM'}
ins = {'DJ': (D + J + K) / 3, 'KD': (D + J + K) / 3, 'JK': (J + C + B + M) / 4, 'LM': (J + C + B + M) / 4,
       'MH': (H + L + M) / 3, 'HL': (H + L + M) / 3}
for nm, (p, q, ans) in SIDES.items():
    col = BLUE if nm in AXIS else RED
    z.line(p, q, color=col, lw=2.6)
    z.edge_label(p, q, ans, ins.get(nm, centroid(URI)), color=col, fs=14,
                 outward=nm not in ('JK', 'LM'))
for n in ['D', 'J', 'C', 'B', 'M', 'H', 'L', 'K']:
    z.point(globals()[n], KUI[n])
z.north_arrow()
z.free_text(centroid(URI), '2番42\n（本件売却部分）', fs=15)
for n, aw in [('D', D + P(0.5, -1)), ('J', J + P(-1, -0.6)), ('C', centroid(URI)), ('B', centroid(URI)),
              ('M', M + P(1, 0.6)), ('H', H + P(0, 1)), ('L', L + P(0, 1)), ('K', K + P(0.6, 1))]:
    z.point_label(globals()[n], n, away=aw)
ALL += save(fig, [z], 'R8_dai21mon_zu29_henchou.png')

print('重なりの合計:', len(ALL))
