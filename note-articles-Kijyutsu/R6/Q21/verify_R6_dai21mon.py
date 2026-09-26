"""令和6年度 第21問：記事の数値・電卓表示の照合スクリプト。
実行: python3 note-articles-Kijyutsu/R6/Q21/verify_R6_dai21mon.py
記事中の「表示：」の文字列と、キー操作を再現した計算結果が一致するかを確認する。"""
import cmath, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import *

ART = os.path.join(os.path.dirname(__file__), 'note_R6_dai21mon_tochi_kijutsu_kaisetsu.md')
text = open(ART, encoding='utf-8').read()
ng = 0
def check(label, s):
    global ng
    ok = s in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label + ' : ' + s)

T1, T2 = P(16.63, 61.67), P(26.91, 64.19)
C, H, I, J = P(27.49, 60.92), P(21.83, 54.17), P(21.83, 60.90), P(19.83, 60.93)
A0 = P(25.09, 48.35)
check('arg(T1−T2)', '表示：' + to_dms(cmath.phase(T1 - T2)))
Bx = radial(T2, T1, 10.03, dms(78, 58, 8)); check('B', '表示：' + disp(Bx))
Dx = radial(T2, T1, 4.60, dms(118, 24, 27)); check('D', '表示：' + disp(Dx))
B, D = r2(Bx), r2(Dx)
check('B丸め', '（27.39, 54.17）' if B == P(27.39, 54.17) else 'x')
check('D丸め', '（30.00, 60.78）' if D == P(30.00, 60.78) else 'x')
check('BH・DJ', f'表示：{fmt_num(abs(H - B), 2)}（1行目）、{fmt_num(abs(J - D))}（2行目）')
check('AB', f'{abs(B - A0):.3f} → {abs(B - A0):.2f}')
check('BDIH', '表示：' + disp(double_area_sum([B, D, I, H])))
check('BDIH地積', f'{chiseki(area([B, D, I, H])):.2f}㎡')
Pp, t, num, den = intersect(B, C, D, J)
check('交点分子', '表示：' + disp(num)); check('交点分母', '表示：' + disp(den))
check('t', f'＝ {t:.6f}')
check('P', '表示：' + disp(B + (C - B) * 67.6152 / 68.6625))
Pr = r2(Pp); check('P丸め', '（27.49, 60.82）' if Pr == P(27.49, 60.82) else 'x')
check('△BDP', '表示：' + disp(tri_conj(B, D, Pr)))
check('BPIH', '表示：' + disp(double_area_sum([B, Pr, I, H])))
check('3番3地積', f'{chiseki(area([B, D, Pr])):.2f}㎡')
check('3番1地積', f'{chiseki(area([B, Pr, I, H])):.2f}㎡')
for n, a, b in [('BP', B, Pr), ('PD', Pr, D), ('DB', D, B), ('PI', Pr, I), ('IH', I, H), ('HB', H, B)]:
    check('辺長' + n, f'{n}' + ('（分筆線）' if n == 'BP' else '') + f'：{abs(b - a):.2f}')
print('NG件数:', ng)
