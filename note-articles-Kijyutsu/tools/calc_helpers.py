"""記述式（土地）記事の検算用ヘルパー。

F-789SG の複素数モードでの計算を Python で再現し、記事に書いた「表示」の値と照合するための関数群。
座標は Z = X + Yi（X=北、Y=東）で扱う。複素平面の反時計回り = 地図上の時計回り。

使い方（例）:
    from calc_helpers import *
    T1, T2 = P(16.63, 61.67), P(26.91, 64.19)
    B = radial(T2, T1, 10.03, dms(78, 58, 8))
    print(disp(B))            # 記事に書くべき表示: 27.3899… ＋ 54.1714…i
    B = r2(B)                 # 注3の丸め（小数第3位四捨五入）

このファイルは問題に依存しない。問題ごとの照合スクリプトは、年度・問題フォルダに置く。
"""
import cmath
import math


def P(x, y):
    """座標 (X, Y) を複素数 X + Yi にする。"""
    return complex(x, y)


def dms(d, m=0, s=0):
    """度分秒をラジアンにする。"""
    return math.radians(d + m / 60 + s / 3600)


def to_dms(rad):
    """ラジアンを「±D°M′S.ss″」の文字列にする（F-789SG の arg 表示と同じく -180〜180 の範囲）。"""
    deg = math.degrees(rad)
    sign = '−' if deg < 0 else ''
    deg = abs(deg)
    d = int(deg)
    m_f = (deg - d) * 60
    m = int(m_f)
    s = (m_f - m) * 60
    return f"{sign}{d}°{m:02d}′{s:05.2f}″"


def r2(z):
    """座標の丸め（小数第3位を四捨五入し、小数第2位まで）。"""
    return complex(round(z.real + 1e-12, 2), round(z.imag + 1e-12, 2))


def radial(station, backsight, dist, obs_angle_rad):
    """放射計算: 器械点 + 距離∠(arg(後視点 − 器械点) + 観測角)。観測角は時計回り。"""
    base = cmath.phase(backsight - station)
    return station + cmath.rect(dist, base + obs_angle_rad)


def double_area_sum(pts):
    """P1・Conjg(P2) + P2・Conjg(P3) + … + Pn・Conjg(P1) をそのまま返す（記事の「表示」と照合用）。
    面積は abs(結果.imag) / 2。"""
    total = 0
    for i, p in enumerate(pts):
        total += p * pts[(i + 1) % len(pts)].conjugate()
    return total


def area(pts):
    """座標法の面積（丸めなし）。"""
    return abs(double_area_sum(pts).imag) / 2


def tri_conj(apex, a, b):
    """三角形の倍面積の式 Conjg(a − 頂点) × (b − 頂点) をそのまま返す。"""
    return (a - apex).conjugate() * (b - apex)


def intersect(p1, p2, q1, q2):
    """直線p1p2と直線q1q2の交点。
    t = (Conjg(q1 − p1) × (q2 − q1) のi係数) ÷ (Conjg(p2 − p1) × (q2 − q1) のi係数)、交点 = p1 + (p2 − p1) × t
    戻り値: (交点, t, 分子の複素数, 分母の複素数)"""
    num = (q1 - p1).conjugate() * (q2 - q1)
    den = (p2 - p1).conjugate() * (q2 - q1)
    t = num.imag / den.imag
    return p1 + (p2 - p1) * t, t, num, den


def chiseki(value, takuchi=True):
    """地積の端数処理。宅地・鉱泉地は小数第2位未満切り捨て、それ以外は1㎡未満切り捨て（10㎡以下の例外は別途確認）。"""
    if takuchi:
        return math.floor(value * 100 + 1e-9) / 100
    return math.floor(value + 1e-9)


def kousa_kou2(F):
    """精度区分 甲2 の公差（㎡）。問題文に公差表がある場合はそちらを優先する。"""
    return (0.05 + 0.01 * F ** 0.25) * math.sqrt(F)


def fmt_num(v, n=4):
    """記事の表示ルール: 小数第n位で割り切れる値は末尾の0を付けずにそのまま、それ以外は小数第n+1位以下を切り捨てて「…」を付ける。"""
    neg = v < 0
    a = abs(v)
    if abs(a * 10 ** n - round(a * 10 ** n)) < 1e-6:
        # 割り切れる値は末尾の0を付けずに書く（小数第2位までは残す。例: 216.07、1122.381、67.6152）
        s = f"{round(a, n):.{n}f}".rstrip('0')
        if len(s.split('.')[1]) < 2:
            s = f"{round(a, 2):.2f}"
        return ('−' if neg else '') + s
    t = math.floor(a * 10 ** n + 1e-9) / 10 ** n
    return ('−' if neg else '') + f"{t:.{n}f}…"


def disp(z, n=4):
    """複素数を記事の表示形式「a ＋ bi」にする（fmt_num のルールを適用）。"""
    re = fmt_num(z.real, n)
    im = fmt_num(abs(z.imag), n)
    op = '−' if z.imag < 0 else '＋'
    return f"{re} {op} {im}i"


if __name__ == '__main__':
    # 自己テスト（令和6年度第21問の値）
    T1, T2 = P(16.63, 61.67), P(26.91, 64.19)
    print('arg(T1−T2) =', to_dms(cmath.phase(T1 - T2)))            # −166°13′34.82″
    B = radial(T2, T1, 10.03, dms(78, 58, 8))
    print('B 表示 =', disp(B))                                      # 27.3899… ＋ 54.1714…i
    D = radial(T2, T1, 4.60, dms(118, 24, 27))
    print('D 表示 =', disp(D))                                      # 29.9987… ＋ 60.7812…i
    B, D = r2(B), r2(D)
    C, J = P(27.49, 60.92), P(19.83, 60.93)
    Pp, t, num, den = intersect(B, C, D, J)
    print('交点の分子 =', disp(num), ' 分母 =', disp(den), ' t =', round(t, 6))
    print('P 表示 =', disp(Pp))                                     # 27.4884… ＋ 60.8170…i
    print('地積(3番3) =', chiseki(area([B, D, r2(Pp)])))            # 8.34
