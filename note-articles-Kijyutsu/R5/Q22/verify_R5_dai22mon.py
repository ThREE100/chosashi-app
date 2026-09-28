"""令和5年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第3欄 各階平面図・求積表）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R5/Q22/verify_R5_dai22mon.py"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P

ART = os.path.join(os.path.dirname(__file__), 'note_R5_dai22mon_tatemono_kaisetsu.md')
text = open(ART, encoding='utf-8').read()
ng = 0


def check(label, s):
    global ng
    ok = s in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label + ' : ' + s)


# 敷地（本件土地）の辺長：〔座標値一覧表〕A〜D（複素数モードでの検算）
A, B, C, D = P(50.00, 75.00), P(68.00, 75.00), P(68.00, 89.50), P(52.00, 88.00)
assert abs(B - A) == 18.0 and abs(C - B) == 14.5 and round(abs(A - D), 1) == 13.2
cd = abs(D - C)
assert round(cd, 1) == 16.1
cd_trunc = math.floor(cd * 1e4) / 1e4  # 表示値の「…」は切り捨て（qa-checklist-kijutsu.md 5章）
check('AB・BC・DA', 'ABは18.0メートル、BCは14.5メートル、DAは13.2メートル')
check('CD（丸め前）', f'{cd_trunc:.4f}… なので、四捨五入して 16.1メートル')

# 1階の求積（壁心）：東側0.90×9.00 ＋ 西側6.40×11.80（アガルート解答例・求積表と同じ分割）
a1, a2 = 0.90 * 9.00, 6.40 * 11.80
assert round(a1 + a2, 2) == 83.62
check('1階 東側', '0.90 × 9.00 ＝ 8.1000')
check('1階 西側', '6.40 × 11.80 ＝ 75.5200')
check('1階 合計', '合計：83.6200 （床面積：83.62平方メートル）')

# 2階の求積（壁心）：東側2.70×12.70 ＋ 西側4.60×11.80
b1, b2 = 2.70 * 12.70, 4.60 * 11.80
assert round(b1 + b2, 2) == 88.57
check('2階 東側', '2.70 × 12.70 ＝ 34.2900')
check('2階 西側', '4.60 × 11.80 ＝ 54.2800')
check('2階 合計', '合計：88.5700 （床面積：88.57平方メートル）')

# 一棟の建物の表示（工事前）の床面積：2階＝7.30×7.30＋4.60×4.50＝73.99（アガルート解答例と一致）
c1, c2 = 7.30 * 7.30, 4.60 * 4.50
assert round(c1 + c2, 2) == 73.99
check('一棟(工事前)2階 上側', '7.30かける7.30が53.29')
check('一棟(工事前)2階 下側', '4.60かける4.50が20.70')
check('一棟(工事前)2階 合計', '合計73.99平方メートルです')
check('一棟(工事前) 1階・2階', '1階83.62、2階73.99')

print('NG件数:', ng)
