"""令和7年度 第21問：記事の数値・電卓表示の照合スクリプト。
実行: python3 note-articles-Kijyutsu/R7/Q21/verify_R7_dai21mon.py"""
import cmath, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import *

ART = os.path.join(os.path.dirname(__file__), 'note_R7_dai21mon_tochi_kijutsu_kaisetsu.md')
text = open(ART, encoding='utf-8').read()
ng = 0
def check(label, s):
    global ng
    ok = s in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label + ' : ' + s)

T1, T2 = P(185.31, 135.37), P(188.60, 92.18)
C, E, F, G, H = P(219.57, 117.56), P(184.31, 114.41), P(184.31, 130.08), P(193.50, 131.88), P(217.00, 131.88)
check('arg(T1−T2)', '表示：' + to_dms(cmath.phase(T1 - T2)))
Dx = radial(T2, T1, 25.81, dms(325, 6, 51)); check('D', '表示：' + disp(Dx))
D = r2(Dx)
s6 = double_area_sum([C, H, G, F, E, D]); check('乙面積', f'表示：（実部）− {abs(s6.imag):.3f}i')
check('△DCH', '表示：' + disp(tri_conj(D, C, H)))
hk = (area([C, H, G, F, E, D]) / 2 - area([D, C, H])) * 2 / (H.imag - D.imag)
check('HK', '表示：' + fmt_num((561.1905 / 2 - 131.92535) * 2 / 17.47))
K = r2(H - round(hk, 2)); check('K', '（199.98, 131.88）' if K == P(199.98, 131.88) else 'x')
s4 = double_area_sum([C, H, K, D]); check('10番1', f'表示：（実部）− {abs(s4.imag):.4f}i')
J = C + (D - C) * 3.5 / 17.86; check('J', '表示：' + disp(J))
a = abs(K - D); check('a', '表示：' + fmt_num(a))
Cp = (C - D) * (K - D).conjugate() / a; check("C′", '表示：' + disp(Cp))
KH = (H - K) * (K - D).conjugate() / a; check("(K→H)′", '表示：' + disp(KH))
cd, ck = Cp.real / -Cp.imag, -KH.real / -KH.imag
check('cot(D)', f'{math.floor(Cp.real*1e6)/1e6:.6f}… ÷ {math.floor(-Cp.imag*1e6)/1e6:.6f}… ＝ {cd:.6f}')
check('cot(K)', f'{math.floor(-KH.real*1e6)/1e6:.6f}… ÷ {math.floor(-KH.imag*1e6)/1e6:.6f}… ＝ {ck:.6f}')
s = (17.5554 - math.sqrt(17.5554 ** 2 - 2 * 0.175044 * 62.72)) / 0.175044; check('s', '表示：' + fmt_num(s))
L = K + (H - K) * 3.6387 / 16.9372; check('L', '表示：' + disp(L))
M = D + (C - D) * 3.6387 / 18.0835; check('M', '表示：' + disp(M))
check('10番1地積', f'{chiseki(area([C, H, K, D])):.2f}')
print('NG件数:', ng)
