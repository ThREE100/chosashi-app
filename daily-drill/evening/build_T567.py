"""PM-82（T5：任意座標→平面直角座標の変換）・PM-83（T6：結合トラバースとコンパスの法則）・PM-84（T7：世界測地系の大きな座標）。
方法A（複素数）で答えを出す。check_pm.py が方法B（三角関数・回転行列・クラメルの公式・三角形分割）で検算し、
calc_keys.py が F-789SG のキー列を実行して表示を再現する。
使い方: python3 daily-drill/evening/build_T567.py"""
import cmath
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from calc_exam import P, r2, shoelace, floor2, inter, dms, dms_rad, fmt, pt_row, pack  # noqa: E402

ser = lambda z: [z.real, z.imag]


def away(nm, z):
    """四捨五入の境目（x.xx5）から離れていること"""
    for u in (z.real, z.imag):
        assert abs((u * 100) % 1 - 0.5) > 0.08, (nm, u)


def ang_s(a):
    return f'{a[0]}°{a[1]:02d}′{a[2]:02d}″'


# ======================================================================
# PM-82 T5：道路境界確認図（任意座標）の点を、共通点2つで平面直角座標に直す
# ======================================================================
def build_pm82():
    A, D = P(612.40, 405.30), P(593.17, 404.62)            # 西隣14番の地積測量図（平面直角座標）＝本件土地の北西・南西の角
    B_t, C_t = P(613.06, 422.46), P(594.25, 421.83)        # 本件土地の北東・南東の角（真の位置）
    th = math.radians(-3.75)                                 # 確認図の任意座標の軸の回転
    O = P(100.00, 100.00)
    to_arb = lambda z: r2((z - A) * cmath.exp(-1j * th) + O)
    Aa, Ba, Ca, Da = (to_arb(z) for z in (A, B_t, C_t, D))
    k = (D - A) / (Da - Aa)                                  # 共通点2つの比（回転を含む。大きさは1に近い）
    Bz, Cz = A + (Ba - Aa) * k, A + (Ca - Aa) * k
    away('B', Bz); away('C', Cz)
    B, C = r2(Bz), r2(Cz)
    wrong_B = r2(A + (Ba - Aa))                              # 平行移動だけで直す誤り
    assert abs(wrong_B - B) > 0.5
    bc = round(abs(C - B), 2)
    assert abs(bc - round(abs(Ca - Ba), 2)) < 0.011          # 確認図の辺長と一致（検算）
    area = floor2(shoelace([A, B, C, D]))
    ans = [{'label': '点B', 'kind': 'xy', 'value': fmt(B)}, {'label': '点C', 'kind': 'xy', 'value': fmt(C)},
           {'label': '辺BCの長さ（m）', 'kind': 'area', 'value': f'{bc:.2f}'}, {'label': '本件土地の地積（㎡）', 'kind': 'area', 'value': f'{area:.2f}'}]
    text = {
     'lead': '土地家屋調査士の斉藤一郎は、甲田三郎から、A市B町四丁目15番の土地（以下「本件土地」という。宅地）の地積に関する更正の登記の依頼を受け、令和8年10月20日に調査を行った。【条件】、【聞き取り結果】、【注】及び次のページの図・表に基づき、解答欄の点B・点Cの座標（平面直角座標系）、辺BCの長さ、本件土地の地積を答えなさい。',
     'conditions': [
      '本件土地は、点A・B・C・Dを順に結んだ範囲である。点Aと点Dは、西隣の14番の土地の地積測量図（平成20年作成）に記載された座標値（平面直角座標系）のとおりである。',
      '本件土地の東側は市道に接している。市が作成した道路境界確認図（平成5年作成）には、本件土地の4つの角A′・B′・C′・D′が、任意の座標系の座標値で記載されている。A′はAと、D′はDと、同じ境界標である。',
      '点Bと点Cは、道路境界確認図の点B′・C′を、点A・Dと点A′・D′の2組の共通点を使って、平面直角座標系に直して求める。',
      '地積は、求めた座標値（小数第2位まで）から座標法で求め、小数第2位未満を切り捨てる。',
     ],
     'hearing': [
      '甲田三郎の話：「東側の境界は、市の確認図どおりのコンクリート杭だ。登記記録の地積は、昔の測量のものだと聞いている。」',
      '市の道路管理担当者の話：「確認図は、現地に任意の基準を置いて測ったもので、座標の軸の向きは平面直角座標系とは合わせていない。杭は入れ直していない。」',
      '西隣（14番）の所有者乙野花子の話：「うちの地積測量図の点A・Dの杭は動いていない。」',
     ],
     'notes': [
      '座標は、Xが北（任意の座標系ではその軸の向き）、Yが東、単位はメートルである。点の座標値は、計算の結果を小数第3位で四捨五入し、小数第2位まで求める。',
      '座標の変換は、2組の共通点による（拡大・縮小の補正はしない。共通点2つの比の大きさが1に近いことを確かめる）。任意の座標系の座標値を、平行移動だけで平面直角座標系に直してはならない。',
     ],
    }
    tables = [
     {'title': '14番の地積測量図（平成20年作成）に記載された座標値（平面直角座標系）', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('A', A, '本件土地の北西の角'), pt_row('D', D, '本件土地の南西の角')]},
     {'title': '道路境界確認図（平成5年作成）に記載された座標値（任意の座標系）', 'cols': ['点', 'X′', 'Y′', '備考'],
      'rows': [pt_row('A′', Aa, 'Aと同じ杭'), pt_row('B′', Ba, '北東の角'), pt_row('C′', Ca, '南東の角'), pt_row('D′', Da, 'Dと同じ杭')]},
    ]
    fig = {
     'points': {'A': {'xy': A, 'kind': 'ref', 'dx': -14, 'dy': -10}, 'D': {'xy': D, 'kind': 'ref', 'dx': -14, 'dy': 20}, 'B': {'xy': B, 'kind': 'unknown'}, 'C': {'xy': C, 'kind': 'unknown', 'dx': 14, 'dy': 20}},
     'polys': [{'pts': ['A', 'B', 'C', 'D'], 'fill': '#e8f4f0', 'label': '15番'}],
     'lines': [], 'texts': [{'xy': P(603.5, 427.5), 'text': '市道'}, {'xy': P(603.5, 399.0), 'text': '14番'}],
     'road': {'a': P(616.0, 425.0), 'b': P(590.0, 424.0)},
    }
    steps = [
     '比 k ＝ (D − A) ÷ (D′ − A′)（共通点2つ。回転を含む複素数。Abs(k) が1に近いことを確かめる）',
     'B ＝ A ＋ (B′ − A′) × k、C ＝ A ＋ (C′ − A′) × k',
     f'辺BC ＝ Abs(C − B) ＝ {bc:.2f}。確認図の Abs(C′ − B′) と一致（変換しても長さは変わらない＝検算）',
     f'地積 ＝ 四角形A・B・C・Dの対角線 Conjg(C − A) × (D − B) のiの係数の絶対値 ÷ 2 → {area:.2f}（小数第2位未満切捨て）',
    ]
    traps = [f'平行移動だけで B ＝ A ＋ (B′ − A′) とすると（{wrong_B.real:.2f}, {wrong_B.imag:.2f}）になり、軸の回転（約3°45′）の分だけずれる。比 k は複素数のまま掛ける。',
             '比は共通点どうしで取る（(D − A) ÷ (D′ − A′)）。分子と分母を逆にすると、元の任意座標の向きに戻ってしまう。',
             '検算：変換の前後で辺の長さは変わらない。BCの長さが確認図のB′C′と0.01以内で一致しなければ、比の取り方を誤っている。']
    verify = {'type': 'pm82', 'A': ser(A), 'D': ser(D), 'Aa': ser(Aa), 'Ba': ser(Ba), 'Ca': ser(Ca), 'Da': ser(Da)}
    return text, tables, fig, ans, steps, traps, verify


# ======================================================================
# PM-83 T6：結合トラバース（T2→T101→T3）の閉合差をコンパスの法則で配り、T101から放射
# ======================================================================
def build_pm83():
    T1, T2, T3 = P(512.36, 287.14), P(498.27, 302.55), P(521.84, 335.62)
    T101_t = P(489.62, 318.93)
    a_T2 = cmath.phase(T1 - T2)
    b1 = dms((cmath.phase(T101_t - T2) - a_T2) % (2 * math.pi))
    d1 = round(abs(T101_t - T2) + 0.045, 2)                      # 観測の誤差（距離）
    b2t = (cmath.phase(T3 - T101_t) - cmath.phase(T2 - T101_t)) % (2 * math.pi)
    b2 = dms(b2t + math.radians(75 / 3600))                      # 観測の誤差（角 75″）
    d2 = round(abs(T3 - T101_t) - 0.006, 2)
    T101p = T2 + cmath.rect(d1, a_T2 + dms_rad(b1))
    T1p_r = r2(T101p)
    away('T101′', T101p)
    T3p = T1p_r + cmath.rect(d2, cmath.phase(T2 - T1p_r) + dms_rad(b2))   # 注のとおり、丸めたT101′から計算する
    away('T3′', T3p)
    T3p_r = r2(T3p)
    corr = T3 - T3p_r                                             # 補正量（正しい値 − 計算した値）
    assert 0.04 < abs(corr) < 0.15, corr
    T101z = T1p_r + corr * d1 / (d1 + d2)
    away('T101', T101z)
    T101 = r2(T101z)
    # 境界点P・Q（補正後のT101に器械、T2を後視）
    Pt, Qt = P(483.95, 312.48), P(481.13, 327.70)
    base = cmath.phase(T2 - T101)
    aP, aQ = dms((cmath.phase(Pt - T101) - base) % (2 * math.pi)), dms((cmath.phase(Qt - T101) - base) % (2 * math.pi))
    dP, dQ = round(abs(Pt - T101), 2), round(abs(Qt - T101), 2)
    Pz, Qz = T101 + cmath.rect(dP, base + dms_rad(aP)), T101 + cmath.rect(dQ, base + dms_rad(aQ))
    away('P', Pz); away('Q', Qz)
    Pp, Qp = r2(Pz), r2(Qz)
    # 調整前のT101・調整前の向きを使った誤り
    wP = r2(r2(T101p) + cmath.rect(dP, cmath.phase(T2 - r2(T101p)) + dms_rad(aP)))
    assert wP != Pp
    ans = [{'label': '点T3′（計算した位置）', 'kind': 'xy', 'value': fmt(T3p_r)},
           {'label': '補正量（T3 − T3′）', 'kind': 'xy', 'value': [f'{corr.real:.2f}', f'{corr.imag:.2f}']},
           {'label': '点T101（補正後）', 'kind': 'xy', 'value': fmt(T101)},
           {'label': '点P', 'kind': 'xy', 'value': fmt(Pp)}, {'label': '点Q', 'kind': 'xy', 'value': fmt(Qp)}]
    text = {
     'lead': '土地家屋調査士の斉藤一郎は、A市C町一丁目7番の土地の分筆の登記の依頼を受け、令和8年10月21日に現地で測量を行った。筆界点P・Qは既知点から見通せないため、多角点T101を設けて結合トラバースを組んだ。【条件】、【注】及び次のページの表に基づき、解答欄の各点の座標と補正量を答えなさい。',
     'conditions': [
      'T1・T2・T3は既知点である（座標は【既知点の座標値】のとおり）。',
      'T2に器械を据えてT1を後視し、多角点T101を観測した。次にT101に器械を据えてT2を後視し、T3と筆界点P・Qを観測した（【観測値】の表）。水平角は、後視点から時計回りに測った角である。',
      'T2→T101→T3の結合トラバースの閉合差は、コンパスの法則（各点までの測線の長さの合計に比例して配る）で配り、T101の座標を補正する。',
      '筆界点P・Qは、補正したT101の座標から、T2を後視した観測値で求める。',
     ],
     'hearing': [
      '補助者の話：「T101のくいは、T2・T3の両方が見える場所に打った。P・Qの観測は、T101の座標を補正する前に済ませてある。」',
      '依頼者の話：「P・Qの位置には石杭がある。隣地の人とも立ち会って確認した。」',
     ],
     'notes': [
      '座標は平面直角座標系のものであり、Xが北、Yが東、単位はメートルである。点の座標値・補正量は、計算の結果を小数第3位で四捨五入し、小数第2位まで求める。',
      'T3′はT3を観測値から計算した位置（丸めて小数第2位）、補正量はT3 − T3′（正しい値 − 計算した値）とする。T101の補正は、補正前のT101（丸めて小数第2位）に、補正量 ×（T2からT101までの距離）÷（全長）を加える。',
      '点P・Qの方向角は、補正したT101から見たT2の方向角を基準にする（補正前の方向角を使い回さない）。',
     ],
    }
    tables = [
     {'title': '既知点の座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('T1', T1, ''), pt_row('T2', T2, '出発点'), pt_row('T3', T3, '到着点')]},
     {'title': '観測値', 'cols': ['器械点', '後視点', '視準点', '水平角（時計回り）', '水平距離（m）'],
      'rows': [['T2', 'T1', 'T101', ang_s(b1), f'{d1:.2f}'], ['T101', 'T2', 'T3', ang_s(b2), f'{d2:.2f}'],
               ['T101', 'T2', 'P', ang_s(aP), f'{dP:.2f}'], ['T101', 'T2', 'Q', ang_s(aQ), f'{dQ:.2f}']]},
    ]
    fig = {
     'points': {'T1': {'xy': T1, 'kind': 'given'}, 'T2': {'xy': T2, 'kind': 'given', 'dx': -18, 'dy': 16}, 'T3': {'xy': T3, 'kind': 'given'},
                'T101': {'xy': T101, 'kind': 'unknown', 'dx': 12, 'dy': 20}, 'P': {'xy': Pp, 'kind': 'unknown', 'dx': -14, 'dy': 20}, 'Q': {'xy': Qp, 'kind': 'unknown', 'dx': 12, 'dy': 20}},
     'polys': [], 'lines': [{'a': 'T1', 'b': 'T2', 'style': 'solid'}, {'a': 'T2', 'b': 'T101', 'style': 'dash'}, {'a': 'T101', 'b': 'T3', 'style': 'dash'},
                            {'a': 'T101', 'b': 'P', 'style': 'dash'}, {'a': 'T101', 'b': 'Q', 'style': 'dash'}, {'a': 'P', 'b': 'Q', 'style': 'bold'}],
     'texts': [{'xy': P(478.0, 320.0), 'text': '7番'}],
    }
    L = d1 + d2
    steps = [
     f'T101′ ＝ T2 ＋ {d1:.2f}∠( arg(T1 − T2) ＋ {ang_s(b1)} ) → ({r2(T101p).real:.2f}, {r2(T101p).imag:.2f})（補正前）',
     f'T3′ ＝ T101′ ＋ {d2:.2f}∠( arg(T2 − T101′) ＋ {ang_s(b2)} ) → ({T3p_r.real:.2f}, {T3p_r.imag:.2f})',
     f'補正量 ＝ T3 − T3′ ＝ {corr.real:.2f} ＋ {corr.imag:.2f}i（正しい値 − 計算した値）',
     f'T101 ＝ T101′ ＋ 補正量 × {d1:.2f} ÷ ({d1:.2f} ＋ {d2:.2f}) ＝ T101′ ＋ 補正量 × {d1 / L:.4f}（コンパスの法則）',
     'P・Q ＝ T101 ＋ 距離∠( arg(T2 − T101) ＋ 水平角 )（補正したT101から、向きも取り直す）',
    ]
    traps = ['補正量の符号：T3 − T3′（正しい値 − 計算した値）を足す。T3′ − T3 を足すと誤差が2倍になる。',
             f'配る比は、T2からT101までの距離 ÷ 全長（{d1:.2f} ÷ {L:.2f}）。T101からT3までの距離で割り振らない（比が逆）。',
             f'P・Qを補正前のT101′と補正前の向きで出すと、Pは（{wP.real:.2f}, {wP.imag:.2f}）になる。補正したT101から、arg(T2 − T101) を取り直す。']
    verify = {'type': 'pm83', 'T1': ser(T1), 'T2': ser(T2), 'T3': ser(T3),
              'obs': {'T101': {'angle': list(b1), 'dist': d1}, 'T3': {'angle': list(b2), 'dist': d2}, 'P': {'angle': list(aP), 'dist': dP}, 'Q': {'angle': list(aQ), 'dist': dQ}}}
    return text, tables, fig, ans, steps, traps, verify


# ======================================================================
# PM-84 T7：世界測地系の大きな座標を、ずらした座標で計算して戻す
# ======================================================================
OFF84 = P(-38500.00, 22700.00)


def build_pm84():
    T1, T2 = P(-38462.18, 22753.40), P(-38441.75, 22729.86)
    K1, K2 = P(-38428.52, 22741.07), P(-38452.33, 22742.96)      # 西隣の地積測量図（K1・K2は西の筆界の上）
    Pt, Qt = P(-38429.47, 22758.70), P(-38450.60, 22762.33)
    base = cmath.phase(T2 - T1)
    aP, aQ = dms((cmath.phase(Pt - T1) - base) % (2 * math.pi)), dms((cmath.phase(Qt - T1) - base) % (2 * math.pi))
    dP, dQ = round(abs(Pt - T1), 2), round(abs(Qt - T1), 2)
    s = lambda z: z - OFF84
    Pz, Qz = s(T1) + cmath.rect(dP, base + dms_rad(aP)), s(T1) + cmath.rect(dQ, base + dms_rad(aQ))
    away('P', Pz); away('Q', Qz)
    Ps, Qs = r2(Pz), r2(Qz)                                         # ずらした座標
    # R＝直線K1K2と、Qを通りPQに直角な直線の交点ではなく：Qから真西（Y減少）ではなく直線K1K2とQ→Sの交点
    S = P(-38451.10, 22735.24)                                      # 南隣の地積測量図の点S（南の筆界の延長上）
    Rz = inter(s(K1), s(K2), Qs, s(S))
    away('R', Rz)
    Rs = r2(Rz)
    back = lambda z: r2(z + OFF84)
    Pp, Qp, Rp = back(Ps), back(Qs), back(Rs)
    area = floor2(shoelace([s(K1), Ps, Qs, Rs]))
    assert abs(area - floor2(shoelace([K1, Pp, Qp, Rp]))) < 0.011
    wrongP = r2(Ps - OFF84)                                         # 戻すときの符号の誤り
    ans = [{'label': '点P', 'kind': 'xy', 'value': fmt(Pp)}, {'label': '点Q', 'kind': 'xy', 'value': fmt(Qp)},
           {'label': '点R', 'kind': 'xy', 'value': fmt(Rp)}, {'label': '本件土地の地積（㎡）', 'kind': 'area', 'value': f'{area:.2f}'}]
    text = {
     'lead': '土地家屋調査士の斉藤一郎は、A市D町五丁目22番の土地（以下「本件土地」という。宅地）の地積に関する更正の登記の依頼を受け、令和8年10月22日に現地で測量を行った。【条件】、【注】及び次のページの表に基づき、解答欄の点P・Q・Rの座標（世界測地系の平面直角座標系の値）と本件土地の地積を答えなさい。',
     'conditions': [
      '本件土地は、点K1・P・Q・Rを順に結んだ範囲である。点K1は、西隣の21番の地積測量図（令和2年作成）に記載された点で、本件土地の北西の角である。西側の筆界は、同図の点K1と点K2を結ぶ直線上にある。',
      '点P（北東の角）と点Q（南東の角）は、既知点T1に器械を据え、既知点T2を後視して観測した（【観測値】の表）。水平角は後視T2から時計回りに測った角である。',
      '点R（南西の角）は、南側の筆界（点Qと、南隣の23番の地積測量図〈平成30年作成〉に記載された点Sを結ぶ直線）と、西側の筆界（直線K1K2）の交点である。',
      '地積は、求めた座標値（小数第2位まで）から座標法で求め、小数第2位未満を切り捨てる。',
     ],
     'hearing': [
      '補助者の話：「座標の値が大きいので、電卓に入れるときは桁を打ち間違えやすい。全部の点から同じ値を引いた座標で計算しておいた。」',
      '南隣（23番）の所有者丙川次郎の話：「点Sの杭は動いていない。境はその杭と本件土地の南東の角を結ぶ線だ。」',
     ],
     'notes': [
      '座標は世界測地系の平面直角座標系（第IX系）のものであり、Xが北、Yが東、単位はメートルである。点の座標値は、計算の結果を小数第3位で四捨五入し、小数第2位まで求める。',
      '計算は、すべての点の座標から（X −38500.00、Y 22700.00）を引いた座標（以下「ずらした座標」）で行い、答えは元の座標に戻して書く。面積は、ずらしても変わらない。',
     ],
    }
    tables = [
     {'title': '既知点の座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('T1', T1, '器械点'), pt_row('T2', T2, '後視点')]},
     {'title': '観測値（T1に器械を据え、T2を後視）', 'cols': ['点', '水平角（T2から時計回り）', '水平距離（m）'], 'rows': [['P', ang_s(aP), f'{dP:.2f}'], ['Q', ang_s(aQ), f'{dQ:.2f}']]},
     {'title': '21番の地積測量図（令和2年作成）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('K1', K1, '本件土地の北西の角'), pt_row('K2', K2, '21番と22番の筆界上')]},
     {'title': '23番の地積測量図（平成30年作成）に記載された座標値', 'cols': ['点', 'X（北）', 'Y（東）', '備考'], 'rows': [pt_row('S', S, '22番と23番の筆界の延長上')]},
    ]
    fig = {
     'points': {'T1': {'xy': s(T1), 'kind': 'given'}, 'T2': {'xy': s(T2), 'kind': 'given'}, 'K1': {'xy': s(K1), 'kind': 'ref', 'dx': -16, 'dy': -8}, 'K2': {'xy': s(K2), 'kind': 'ref', 'dx': -16, 'dy': 16},
                'S': {'xy': s(S), 'kind': 'ref', 'dx': -14, 'dy': 20}, 'P': {'xy': Ps, 'kind': 'unknown'}, 'Q': {'xy': Qs, 'kind': 'unknown', 'dx': 12, 'dy': 20}, 'R': {'xy': Rs, 'kind': 'unknown', 'dx': 12, 'dy': 20}},
     'polys': [{'pts': ['K1', 'P', 'Q', 'R'], 'fill': '#e8f4f0', 'label': '22番'}],
     'lines': [{'a': 'T1', 'b': 'T2', 'style': 'solid'}, {'a': 'T1', 'b': 'P', 'style': 'dash'}, {'a': 'T1', 'b': 'Q', 'style': 'dash'}, {'a': 'K1', 'b': 'K2', 'style': 'solid'}, {'a': 'R', 'b': 'S', 'style': 'solid'}],
     'texts': [{'xy': s(P(-38440.0, 22735.0)), 'text': '21番'}, {'xy': s(P(-38457.0, 22748.0)), 'text': '23番'}],
    }
    steps = [
     'ずらした座標 ＝ 元の座標 − (−38500.00 ＋ 22700.00i)。例：T1 → (37.82, 53.40)、T2 → (58.25, 29.86)',
     'P・Q ＝ T1 ＋ 距離∠( arg(T2 − T1) ＋ 水平角 )（ずらした座標で計算）',
     'R ＝ 直線K1K2と直線QSの交点：R ＝ K1 ＋ (K2 − K1) × [Conjg(S − Q) × (Q − K1) のiの係数] ÷ [Conjg(S − Q) × (K2 − K1) のiの係数]',
     f'地積 ＝ 四角形K1・P・Q・Rの対角線 Conjg(Q − K1) × (R − P) のiの係数の絶対値 ÷ 2 → {area:.2f}（ずらした座標のまま求めてよい）',
     '答えの座標 ＝ ずらした座標 ＋ (−38500.00 ＋ 22700.00i)（戻すときは足す）',
    ]
    traps = [f'戻すときに引いてしまうと、Pは（{wrongP.real:.2f}, {wrongP.imag:.2f}）になる。ずらすときに引いたものは、戻すときに足す（Xは負の数なので、絶対値が大きくなる向き）。',
             '大きな座標のまま電卓に入れると桁を打ち間違えやすい。ずらした座標で計算し、面積はずらしたまま求める（平行移動で面積は変わらない）。',
             '点Rは直線K1K2と直線QSの交点。点Qから真西に下ろした点ではない。']
    verify = {'type': 'pm84', 'off': ser(OFF84), 'T1': ser(T1), 'T2': ser(T2), 'K1': ser(K1), 'K2': ser(K2), 'S': ser(S),
              'obs': {'P': {'angle': list(aP), 'dist': dP}, 'Q': {'angle': list(aQ), 'dist': dQ}}}
    return text, tables, fig, ans, steps, traps, verify


BASIS = {
 'PM-82': [{'law': '不動産登記規則', 'article': '第77条', 'quote': '基本三角点等に基づく測量の成果による筆界点の座標値'},
           {'law': '不動産登記規則', 'article': '第77条', 'quote': '近傍の恒久的な地物に基づく測量の成果による筆界点の座標値を記録しなければならない'}],
 'PM-83': [{'law': '不動産登記規則', 'article': '第77条', 'quote': '基本三角点等に基づく測量の成果による筆界点の座標値'}],
 'PM-84': [{'law': '不動産登記規則', 'article': '第77条', 'quote': '国土調査法施行令第二条第一項第一号に規定する平面直角座標系の番号又は記号'}],
}

if __name__ == '__main__':
    for pid, day, title, fn in (('PM-82', 82, '座標の変換：任意座標の道路境界確認図を、共通点2つで平面直角座標に直す', build_pm82),
                                ('PM-83', 83, '結合トラバース：閉合差をコンパスの法則で配り、多角点から筆界点を放射', build_pm83),
                                ('PM-84', 84, '世界測地系の大きな座標：ずらした座標で放射・交点・地積を求めて元に戻す', build_pm84)):
        p = pack(pid, day, title, fn)
        p['minutes'] = 20
        p['basis'] = BASIS[pid]
        json.dump(p, open(os.path.join(HERE, 'problems', pid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(pid, [(a['label'], a['value']) for a in p['answers']])
