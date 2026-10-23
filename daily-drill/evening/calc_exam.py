"""夜の計算ドリル（本番レベル）：条件・聞き取り結果・地積測量図の座標・観測値から、筆界点と地積を求める。
座標は Z = X + Yi（X=北、Y=東）。答えは、点の座標を小数第3位で四捨五入して小数第2位まで、地積は求めた座標値（小数第2位）から座標法で求めて小数第2位未満を切り捨てる（宅地）。
check_pm.py が、別の方法（三角関数・連立方程式・靴ひも公式）で答えを検算する。
使い方: python3 daily-drill/evening/calc_exam.py"""
import cmath
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'problems')


def r2(z):
    return complex(round(z.real + 1e-12, 2), round(z.imag + 1e-12, 2))


def P(x, y):
    return complex(x, y)


def shoelace(pts):
    s = 0.0
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        s += a.real * b.imag - b.real * a.imag
    return abs(s) / 2


def floor2(v):
    return math.floor(v * 100 + 1e-9) / 100


def cross(u, v):
    return u.real * v.imag - u.imag * v.real


def inter(a, b, c, d):
    """直線abと直線cdの交点（複素数の式）"""
    t = ((d - c).conjugate() * (c - a)).imag / ((d - c).conjugate() * (b - a)).imag
    return a + (b - a) * t


def dms(rad):
    deg = math.degrees(rad) % 360
    d = int(deg)
    m = int((deg - d) * 60)
    s = round(((deg - d) * 60 - m) * 60)
    if s == 60:
        s, m = 0, m + 1
    if m == 60:
        m, d = 0, d + 1
    return d, m, s


def dms_rad(a):
    return math.radians(a[0] + a[1] / 60 + a[2] / 3600)


def fmt(z):
    return [f'{z.real:.2f}', f'{z.imag:.2f}']


def pt_row(name, z, remark=''):
    return [name, f'{z.real:.2f}', f'{z.imag:.2f}', remark]


# ======================================================================
# Day1：放射で道路側の筆界点P・Qを出し、地積測量図の直線の交点でRを出し、地積を求める
# ======================================================================
def build_pm01():
    T1, T2 = P(545.28, 409.64), P(543.90, 388.15)
    P_true, Q_true, R_true, S = P(541.02, 400.35), P(540.49, 416.10), P(521.62, 416.48), P(521.78, 400.86)
    # 観測値：後視T2から時計回りの水平角（秒まで）と水平距離（0.01m）
    obs = {}
    base = cmath.phase(T2 - T1)
    for name, tp in (('P', P_true), ('Q', Q_true)):
        ang = (cmath.phase(tp - T1) - base) % (2 * math.pi)
        obs[name] = {'angle': dms(ang), 'dist': round(abs(tp - T1), 2)}
    Pp = r2(T1 + cmath.rect(obs['P']['dist'], base + dms_rad(obs['P']['angle'])))
    Qp = r2(T1 + cmath.rect(obs['Q']['dist'], base + dms_rad(obs['Q']['angle'])))
    # 11番の地積測量図：東側の筆界（Q-R）上の点K1・K2、13番〜14番の地積測量図：南側の筆界上の点S・M
    K1 = r2(Q_true + (R_true - Q_true) * 0.30)
    K2 = r2(Q_true + (R_true - Q_true) * 0.70)
    M = r2(S + (R_true - S) * 0.45)
    R = r2(inter(K1, K2, S, M))
    area = floor2(shoelace([Pp, Qp, R, S]))
    ans = [
        {'label': '点P', 'kind': 'xy', 'value': fmt(Pp)},
        {'label': '点Q', 'kind': 'xy', 'value': fmt(Qp)},
        {'label': '点R', 'kind': 'xy', 'value': fmt(R)},
        {'label': '12番の地積（㎡）', 'kind': 'area', 'value': f'{area:.2f}'},
    ]
    a1, a2 = obs['P']['angle'], obs['Q']['angle']
    text = {
     'lead': '土地家屋調査士の斉藤一郎は、甲野一郎から、A市B町一丁目12番の土地（以下「本件土地」という。宅地）の測量を依頼され、令和8年10月8日に現地で次の調査・測量を行った。【条件】、【聞き取り結果】、【注】及び次のページの図・表に基づき、解答欄の点P・点Q・点Rの座標と、本件土地の地積を求めなさい。',
     'conditions': [
      '本件土地は、北側が市道に接し、点P・Qは市道との境界を示す境界標（コンクリート杭）である。点P・Qは、本件土地の北西・北東の筆界点であり、道路境界確認書（市作成）で確認されている。',
      f'点P・Qは、既知点T1に器械を据え、既知点T2を後視して観測した。観測値は【観測値】の表のとおりであり、水平角は後視T2から時計回りに測った角である。',
      '点Rは、本件土地の南東の角の筆界点である。東側の筆界（点Qと点Rを結ぶ線）は、11番の地積測量図（平成12年作成）に記載された点K1と点K2を結ぶ直線上にあり、南側の筆界（点Rと点Sを結ぶ線）は、13番及び14番の地積測量図（昭和63年作成）に記載された点Sと点Mを結ぶ直線上にある。点Rは、この2つの直線の交点である。',
      '点Sは、本件土地の南西の角の筆界点であり、13番の地積測量図（昭和63年作成）に記載された座標値のとおりである。',
      '本件土地の地積は、点P・Q・R・Sで囲まれた範囲を、求めた座標値（小数第2位まで）から座標法で求める。',
     ],
     'hearing': [
      '本件土地の所有者甲野一郎の話：「道路側の杭は、数年前に市が道路を広げたときに入れ直したもので、市の担当者の立会いで確認した。東側の隣地との間には昔からブロック塀があるが、塀は11番の所有者が自分の敷地内に造ったものと聞いている。」',
      '11番の所有者乙川花子の話：「ブロック塀は、たしか地積測量図を作ったときの測量の線から少し内側（本件土地の側ではなく、うちの側）に寄せて造った。筆界は、地積測量図のとおりでよい。塀の位置にこだわらない。」',
      '14番の所有者丙山次郎の話：「南側は、地積測量図を作ったときに、13番の所有者と一緒に杭を確認した。その後、杭は動かしていない。」',
      '市の道路管理担当者の話：「市道との境界は、道路境界確認書のとおり、点Pと点Qの杭で確定している。」',
     ],
     'notes': [
      '座標は平面直角座標系のものであり、Xが北、Yが東、単位はメートルである。',
      '点の座標値は、計算の結果を小数第3位で四捨五入し、小数第2位まで求める。面積は、求めた座標値（小数第2位まで）を用いて座標法で求め、地積は、小数第2位未満の端数を切り捨てる。',
      '地積測量図に記載された座標値は、現地の杭の位置と一致していることを確認済みである。ブロック塀の位置は、筆界の判断に用いない。',
     ],
    }
    tables = [
     {'title': '既知点の座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'],
      'rows': [pt_row('T1', T1, '器械点'), pt_row('T2', T2, '後視点')]},
     {'title': '観測値（T1に器械を据え、T2を後視）', 'cols': ['点', '水平角（T2から時計回り）', '水平距離（m）'],
      'rows': [[n, f'{o["angle"][0]}°{o["angle"][1]:02d}′{o["angle"][2]:02d}″', f'{o["dist"]:.2f}'] for n, o in obs.items()]},
     {'title': '11番の地積測量図（平成12年作成）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'],
      'rows': [pt_row('K1', K1, '11番と12番の筆界上'), pt_row('K2', K2, '11番と12番の筆界上')]},
     {'title': '13番・14番の地積測量図（昭和63年作成）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'],
      'rows': [pt_row('S', S, '12番・13番・14番の境'), pt_row('M', M, '12番と14番の筆界上')]},
    ]
    fig = {
     'points': {'T1': {'xy': T1, 'kind': 'given'}, 'T2': {'xy': T2, 'kind': 'given'},
                'K1': {'xy': K1, 'kind': 'ref'}, 'K2': {'xy': K2, 'kind': 'ref'}, 'S': {'xy': S, 'kind': 'ref'}, 'M': {'xy': M, 'kind': 'ref'},
                'P': {'xy': Pp, 'kind': 'unknown'}, 'Q': {'xy': Qp, 'kind': 'unknown'}, 'R': {'xy': R, 'kind': 'unknown'}},
     'polys': [{'pts': ['P', 'Q', 'R', 'S'], 'fill': '#e8f4f0', 'label': '12番'}],
     'lines': [{'a': 'T1', 'b': 'T2', 'style': 'solid'}, {'a': 'T1', 'b': 'P', 'style': 'dash'}, {'a': 'T1', 'b': 'Q', 'style': 'dash'},
               {'a': 'Q', 'b': 'K1', 'style': 'solid'}, {'a': 'K1', 'b': 'K2', 'style': 'solid'}, {'a': 'K2', 'b': 'R', 'style': 'dash'},
               {'a': 'S', 'b': 'M', 'style': 'solid'}, {'a': 'M', 'b': 'R', 'style': 'dash'}],
     'texts': [{'xy': P(551.0, 392.0), 'text': '市道'}, {'xy': P(531.0, 392.0), 'text': '13番'}, {'xy': P(531.0, 428.0), 'text': '11番'}, {'xy': P(515.0, 408.0), 'text': '14番'}],
     'road': {'a': P(547.5, 380.0), 'b': P(542.0, 430.0)},
    }
    steps = [
     '方向角 arg(T2 − T1)（後視の向き）を出し、観測した水平角を「時計回り」に足す。',
     f'点P ＝ T1 ＋ {obs["P"]["dist"]:.2f}∠(arg(T2 − T1) ＋ {a1[0]}°{a1[1]:02d}′{a1[2]:02d}″) ＝ {Pp.real:.2f} ＋ {Pp.imag:.2f}i',
     f'点Q ＝ T1 ＋ {obs["Q"]["dist"]:.2f}∠(arg(T2 − T1) ＋ {a2[0]}°{a2[1]:02d}′{a2[2]:02d}″) ＝ {Qp.real:.2f} ＋ {Qp.imag:.2f}i',
     '検算：点Qは直線K1K2の延長上（11番との筆界上）にある。',
     't ＝ Im(Conjg(M − S) × (S − K1)) ÷ Im(Conjg(M − S) × (K2 − K1))、点R ＝ K1 ＋ t × (K2 − K1)',
     f'点R ＝ {R.real:.2f} ＋ {R.imag:.2f}i（直線K1K2と直線SMの交点）',
     f'面積：P→Q→R→Sの順に座標法で求める ＝ {shoelace([Pp, Qp, R, S]):.4f} ㎡ → 地積 {area:.2f} ㎡（小数第2位未満切捨て）',
    ]
    traps = ['観測角は後視から「時計回り」に足す（引くと反対側の点になる）。', 'ブロック塀の位置は筆界の根拠にしない。東の筆界は11番の地積測量図の点K1・K2、南の筆界は点S・Mを通る直線。', '地積は、求めた座標値（小数第2位）で座標法を使い、切り捨てる（四捨五入しない）。']
    verify = {'type': 'pm01', 'T1': [T1.real, T1.imag], 'T2': [T2.real, T2.imag], 'obs': obs,
              'K1': [K1.real, K1.imag], 'K2': [K2.real, K2.imag], 'S': [S.real, S.imag], 'M': [M.real, M.imag]}
    return text, tables, fig, ans, steps, traps, verify


# ======================================================================
# Day4：平行で離れた直線と2直線の交点（H・I）、垂線の足（J）と距離
# ======================================================================
def build_pm04():
    A, B = P(530.10, 300.55), P(509.30, 300.13)         # 21番の地積測量図：筆界（西側）上の2点
    C, D = P(531.50, 296.80), P(531.10, 330.60)          # 市道との境界線上の2点（道路境界確認書）
    E, F = P(508.30, 296.20), P(508.00, 330.10)          # 南側の隣地（23番）との筆界上の2点（23番の地積測量図）
    K = P(519.80, 306.10)                                 # 本件建物の南西の角
    off = 1.20
    u = (B - A) / abs(B - A)
    n = 1j * u                                            # 東側（Yが大きい側）の単位法線
    if n.imag < 0:
        n = -n
    A2 = A + n * off
    H = r2(inter(A2, A2 + u, C, D))
    I = r2(inter(A2, A2 + u, E, F))
    w = (K - H) / (I - H)
    J = r2(H + (I - H) * w.real)
    dist = round(abs(K - J), 2)
    ans = [
        {'label': '点H', 'kind': 'xy', 'value': fmt(H)},
        {'label': '点I', 'kind': 'xy', 'value': fmt(I)},
        {'label': '点J（点Kから直線HIに下ろした垂線の足）', 'kind': 'xy', 'value': fmt(J)},
        {'label': '点Kから筆界HIまでの距離（m）', 'kind': 'len', 'value': f'{dist:.2f}'},
    ]
    text = {
     'lead': '土地家屋調査士の斉藤一郎は、丁原三郎から、A市B町二丁目22番の土地（以下「本件土地」という。宅地）の分筆の登記のための測量を依頼され、令和8年10月15日に現地で調査・測量を行った。【条件】、【聞き取り結果】、【注】及び次のページの図・表に基づき、解答欄の点H・点I・点Jの座標と、点Kから筆界HIまでの距離を求めなさい。',
     'conditions': [
      '本件土地の西側は21番に、北側は市道に、南側は23番に接している。本件土地の西側の筆界（点Hと点Iを結ぶ線）は、21番の地積測量図（昭和58年作成）に記載された点Aと点Bを結ぶ直線に平行で、その東側に1.20メートル離れた直線上にある。',
      '点Hは、上の直線と、市道との境界線（道路境界確認書に記載された点Cと点Dを結ぶ直線）との交点であり、点Iは、上の直線と、23番の地積測量図（平成3年作成）に記載された点Eと点Fを結ぶ直線との交点である。',
      '点Kは、本件土地の上にある丁原三郎所有の建物の南西の角であり、現地で測量して座標値を求めた。点Jは、点Kから直線HIに下ろした垂線の足とし、点Kから筆界HIまでの距離は、点Kと点Jの距離とする。',
     ],
     'hearing': [
      '本件土地の所有者丁原三郎の話：「西側の21番との間には、昭和58年に21番の所有者が土留めの擁壁を造り、その東側に幅1.2メートルほどの犬走り（コンクリートの帯）を付けた。境は、その犬走りの東の端だと、当時の測量士から聞いている。」',
      '21番の所有者戊田正男の話：「擁壁は昭和58年にうちが造った。うちの地積測量図の点A・Bは、擁壁の東面を測った点で、いまも擁壁の位置と一致している。犬走りもうちの土地で、その東の端、つまり擁壁から1.2メートル東が境だと理解している。」',
      '23番の所有者己川美咲の話：「南側は、うちの地積測量図の点E・Fを結ぶ線が境界で、現地に杭が入っている。」',
     ],
     'notes': [
      '座標は平面直角座標系のものであり、Xが北、Yが東、単位はメートルである。「東側に1.20メートル離れた」は、直線ABに直角に測った距離である。',
      '点の座標値は、計算の結果を小数第3位で四捨五入し、小数第2位まで求める。距離は、求めた点の座標値（小数第2位）から求め、小数第3位を四捨五入して小数第2位まで答える。',
      '地積測量図及び道路境界確認書に記載された座標値は、現地の擁壁・境界標の位置と一致していることを確認済みである。',
     ],
    }
    tables = [
     {'title': '21番の地積測量図（昭和58年作成）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('A', A, '21番と22番の間の線上'), pt_row('B', B, '21番と22番の間の線上')]},
     {'title': '道路境界確認書（市道との境界）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('C', C, '市道との境界線上'), pt_row('D', D, '市道との境界線上')]},
     {'title': '23番の地積測量図（平成3年作成）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('E', E, '22番と23番の筆界上'), pt_row('F', F, '22番と23番の筆界上')]},
     {'title': '現地で測量した座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('K', K, '建物の南西の角')]},
    ]
    fig = {
     'points': {'A': {'xy': A, 'kind': 'ref', 'dx': -16, 'dy': 34}, 'B': {'xy': B, 'kind': 'ref', 'dx': -14, 'dy': -30}, 'C': {'xy': C, 'kind': 'ref'}, 'D': {'xy': D, 'kind': 'ref'},
                'E': {'xy': E, 'kind': 'ref', 'dx': -14, 'dy': 38}, 'F': {'xy': F, 'kind': 'ref'}, 'K': {'xy': K, 'kind': 'given'},
                'H': {'xy': H, 'kind': 'unknown', 'dx': 16, 'dy': -14}, 'I': {'xy': I, 'kind': 'unknown', 'dx': 16, 'dy': 34}, 'J': {'xy': J, 'kind': 'unknown', 'dx': 16, 'dy': -14}},
     'polys': [],
     'lines': [{'a': 'A', 'b': 'B', 'style': 'solid'}, {'a': 'C', 'b': 'D', 'style': 'solid'}, {'a': 'E', 'b': 'F', 'style': 'solid'},
               {'a': 'H', 'b': 'I', 'style': 'bold'}, {'a': 'K', 'b': 'J', 'style': 'dash'}],
     'texts': [{'xy': P(522.0, 291.0), 'text': '21番'}, {'xy': P(520.0, 318.0), 'text': '22番（本件土地）'}, {'xy': P(534.5, 315.0), 'text': '市道'}, {'xy': P(505.0, 313.0), 'text': '23番'}],
     'offset': {'a': A, 'b': B, 'n': [n.real, n.imag], 'off': off, 'to': 'H'},
    }
    steps = [
     'u ＝ (B − A) ÷ Abs(B − A)（ABの向きの単位ベクトル）。東側（Yが大きい側）への単位法線 n ＝ i × u（Im(n) ＞ 0 を確かめる）。',
     f'A′ ＝ A ＋ 1.20 × n ＝ {A2.real:.4f} ＋ {A2.imag:.4f}i（ABを東へ1.20m平行移動した直線は A′ を通り、向きは B − A）',
     f'点H ＝ 直線A′（向きB − A）と直線CDの交点 ＝ {H.real:.2f} ＋ {H.imag:.2f}i',
     f'点I ＝ 直線A′（向きB − A）と直線EFの交点 ＝ {I.real:.2f} ＋ {I.imag:.2f}i',
     'w ＝ (K − H) ÷ (I − H)、点J ＝ H ＋ (I − H) × Re(w)（垂線の足）',
     f'点J ＝ {J.real:.2f} ＋ {J.imag:.2f}i、KJ ＝ Abs(K − J) ＝ {abs(K - J):.4f} → {dist:.2f} m',
    ]
    traps = ['「離れ」は直角に測る。ABが傾いているので、Yだけに1.20を足してはいけない。', '垂線の足は「真西に下ろす」ではない。直線HIが傾いているので、w ＝ (K − H) ÷ (I − H) の実部で出す。', '通路の幅1.20mは、地積測量図の線（AB）から東へ測る。']
    verify = {'type': 'pm04', 'A': [A.real, A.imag], 'B': [B.real, B.imag], 'C': [C.real, C.imag], 'D': [D.real, D.imag],
              'E': [E.real, E.imag], 'F': [F.real, F.imag], 'K': [K.real, K.imag], 'off': off}
    return text, tables, fig, ans, steps, traps, verify


# ======================================================================
# Day7：分筆線の端点Eを距離で、端点Fを面積の条件で求め、分筆後の地積を求める
# ======================================================================
def build_pm07():
    A, B, C, D = P(540.20, 300.00), P(539.40, 326.10), P(515.60, 326.90), P(516.30, 300.60)
    total_exact = shoelace([A, B, C, D])
    total = floor2(total_exact)
    d_AE = 9.50
    E = r2(A + (D - A) / abs(D - A) * d_AE)
    target = 280.00
    # 面積（A→B→F→E）の条件で、BC上の点Fを求める。F = B + t(C − B)
    # 四角形ABFEの面積 = |Im(Conjg(F − A) × (E − B))| ÷ 2（対角線AFとBEの外積の半分）
    def f_of(t):
        return B + (C - B) * t
    def ar(t):
        F_ = f_of(t)
        return abs(((F_ - A).conjugate() * (E - B)).imag) / 2
    lo, hi = 0.0, 1.0
    # 面積は t の一次式なので、2点から直接解く
    a0, a1 = ar(0.0), ar(1.0)
    t = (target - a0) / (a1 - a0)
    F = r2(f_of(t))
    area_i_calc = shoelace([A, B, F, E])
    area_ro = round(total - target, 2)
    ans = [
        {'label': '点E', 'kind': 'xy', 'value': fmt(E)},
        {'label': '点F', 'kind': 'xy', 'value': fmt(F)},
        {'label': '分筆後の（ロ）の地積（㎡）', 'kind': 'area', 'value': f'{area_ro:.2f}'},
        {'label': '分筆線EFの長さ（m）', 'kind': 'len', 'value': f'{round(abs(F - E), 2):.2f}'},
    ]
    text = {
     'lead': '土地家屋調査士の斉藤一郎は、庚村四郎から、A市B町三丁目30番の土地（以下「本件土地」という。宅地）を2筆に分筆する登記の依頼を受け、令和8年10月20日に現地で調査・測量を行った。【条件】、【聞き取り結果】、【注】及び次のページの図・表に基づき、解答欄の点E・点Fの座標と、分筆後の（ロ）の地積、分筆線EFの長さを求めなさい。',
     'conditions': [
      '本件土地は、点A・B・C・Dを順に結んだ範囲であり、各点は境界標のある筆界点である。座標値は、現地で測量した結果と、31番の地積測量図（平成5年作成）及び道路境界確認書（市作成）の座標値が一致することを確認した。',
      '分筆線は、点Eと点Fを結ぶ直線である。点Eは、辺AD上にあり、点Aから点Dの方向へ9.50メートルの位置とする。点Fは、辺BC上にある。',
      '分筆後の土地のうち、点A・B・F・Eで囲まれた部分を（イ）、点E・F・C・Dで囲まれた部分を（ロ）とする。依頼者の希望により、（イ）の地積は、座標法による面積で280.00平方メートルとする。点Fは、この条件を満たす位置に定める。',
      '分筆前の本件土地の地積は、点A・B・C・Dの座標値から座標法で求めた面積の小数第2位未満を切り捨てたものとし、（ロ）の地積は、分筆前の地積から（イ）の地積280.00平方メートルを差し引いて求める。',
     ],
     'hearing': [
      '本件土地の所有者庚村四郎の話：「北側の（イ）には自宅を建て替える予定で、ちょうど280平方メートルになるように分筆線を決めてほしい。南側の（ロ）は駐車場として貸す予定だ。」',
      '東側の隣地（32番）の所有者辛島洋子の話：「うちとの境界は、市の道路拡幅のときに確認した線のままで、杭は動いていない。」',
      '西側の隣地（31番）の所有者壬生健太の話：「うちの地積測量図の点は、点A・点Dのことだ。現地の杭と一致していて問題ない。」',
     ],
     'notes': [
      '座標は平面直角座標系のものであり、Xが北、Yが東、単位はメートルである。',
      '点の座標値は、計算の結果を小数第3位で四捨五入し、小数第2位まで求める。点Fの位置は、四角形ABFEの面積が280.00平方メートルとなる条件から求める（辺BC上にあること）。',
      '距離は、求めた座標値（小数第2位）から求め、小数第3位を四捨五入して小数第2位まで答える。',
     ],
    }
    tables = [
     {'title': '本件土地（30番）の筆界点の座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('A', A, '北西の角（31番の地積測量図の点）'), pt_row('B', B, '北東の角'), pt_row('C', C, '南東の角'), pt_row('D', D, '南西の角（31番の地積測量図の点）')]},
     {'title': '分筆の条件', 'cols': ['項目', '値'], 'rows': [['点EのA→D方向の位置（A点から）', f'{d_AE:.2f} m'], ['（イ）の地積（座標法による面積）', f'{target:.2f} ㎡'], ['分筆前の地積（座標法の面積を切捨て）', f'{total:.2f} ㎡']]},
    ]
    fig = {
     'points': {'A': {'xy': A, 'kind': 'ref'}, 'B': {'xy': B, 'kind': 'ref'}, 'C': {'xy': C, 'kind': 'ref'}, 'D': {'xy': D, 'kind': 'ref'},
                'E': {'xy': E, 'kind': 'unknown'}, 'F': {'xy': F, 'kind': 'unknown'}},
     'polys': [{'pts': ['A', 'B', 'F', 'E'], 'fill': '#e8f4f0', 'label': '（イ）'}, {'pts': ['E', 'F', 'C', 'D'], 'fill': '#fdf3e3', 'label': '（ロ）'}],
     'lines': [{'a': 'E', 'b': 'F', 'style': 'bold'}],
     'texts': [{'xy': P(545.5, 313.0), 'text': '市道'}, {'xy': P(528.0, 291.0), 'text': '31番'}, {'xy': P(528.0, 332.0), 'text': '32番'}, {'xy': P(509.5, 313.0), 'text': '33番'}],
    }
    steps = [
     'E ＝ A ＋ (D − A) ÷ Abs(D − A) × 9.50（辺ADの向きに、Aから9.50m）',
     f'E ＝ {E.real:.2f} ＋ {E.imag:.2f}i',
     'F ＝ B ＋ t × (C − B)。四角形ABFEの面積 ＝ |Im(Conjg(F − A) × (E − B))| ÷ 2 ＝ 280.00 は、t の一次式。',
     f't ＝ (280.00 − Im(Conjg(B − A) × (E − B)) ÷ 2) ÷ ((Im(Conjg(C − A) × (E − B)) − Im(Conjg(B − A) × (E − B))) ÷ 2) ＝ {t:.6f}',
     f'F ＝ B ＋ t × (C − B) ＝ {F.real:.2f} ＋ {F.imag:.2f}i',
     f'検算：四角形ABFEを座標法で求める ＝ {area_i_calc:.4f} ㎡（求めた座標が小数第2位なので280.00に近い値）',
     f'分筆前の地積 ＝ {total_exact:.4f} → {total:.2f}。（ロ）＝ {total:.2f} − 280.00 ＝ {area_ro:.2f} ㎡',
     f'分筆線EFの長さ ＝ Abs(F − E) ＝ {abs(F - E):.4f} → {round(abs(F - E), 2):.2f} m',
    ]
    traps = ['点Fは「辺BC上」で面積の条件から出す。Fの位置を目分量で決めてはいけない。', '面積は、四角形の対角線の外積の半分で出せる。頂点の並びが一周する順であることを確かめる。', '（ロ）の地積は、座標法で別に求めた面積ではなく、分筆前の地積（切捨て後）から280.00を引いて求める。']
    verify = {'type': 'pm07', 'A': [A.real, A.imag], 'B': [B.real, B.imag], 'C': [C.real, C.imag], 'D': [D.real, D.imag], 'd_AE': d_AE, 'target': target}
    return text, tables, fig, ans, steps, traps, verify


def pack(pid, day, title, builder):
    text, tables, fig, ans, steps, traps, verify = builder()
    ser = lambda z: [z.real, z.imag]
    for p in fig['points'].values():
        p['xy'] = ser(p['xy'])
    for t in fig.get('texts', []):
        t['xy'] = ser(t['xy'])
    if 'road' in fig:
        fig['road'] = {'a': ser(fig['road']['a']), 'b': ser(fig['road']['b'])}
    if 'offset' in fig:
        fig['offset'] = {'a': ser(fig['offset']['a']), 'b': ser(fig['offset']['b']), 'n': fig['offset']['n'], 'off': fig['offset']['off'], 'to': fig['offset']['to']}
    return {'id': pid, 'day': day, 'kind': 'calc2', 'title': title, 'text': text, 'tables': tables, 'fig': fig, 'answers': ans,
            'steps': steps, 'trap': ' '.join(traps), 'verify': verify}


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    items = [pack('PM-01', 1, '筆界点の算出：放射・地積測量図の直線の交点・地積', build_pm01),
             pack('PM-04', 4, '筆界点の算出：平行で離れた直線・2直線の交点・垂線の足', build_pm04),
             pack('PM-07', 7, '分筆：距離と面積の条件から分筆線の端点を求める', build_pm07)]
    for p in items:
        with open(os.path.join(OUT, p['id'] + '.json'), 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
        print(p['id'], [(a['label'], a['value']) for a in p['answers']])
