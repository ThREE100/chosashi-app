"""令和6年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第1〜4欄・建物図面・各階平面図・求積表）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R6/Q22/verify_R6_dai22mon.py"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, area

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_R6_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_R6_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_R6_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_R6_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_R6_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
ng = 0


def check(label, s, src=None, name='記事'):
    global ng
    ok = s in (text if src is None else src)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[{name}] {label} : {s}')


def absent(label, s, src=None, name='記事'):
    global ng
    ok = s not in (text if src is None else src)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[{name}] 禁止語なし（{label}） : {s}')


def poly_area(pts):
    n = len(pts)
    return abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2


def trunc2(v):
    """床面積の端数処理：1平方メートルの100分の1未満を切り捨て（不動産登記規則115条）。"""
    return math.floor(v * 100 + 1e-9) / 100


# ---- 敷地：〔座標値一覧表〕A〜E（X＝北、Y＝東）。図1は傾いて見えるが座標では長方形 ----
A, B, C, D, E = P(50.00, 15.00), P(50.00, 25.00), P(50.00, 35.00), P(37.00, 35.00), P(37.00, 15.00)
assert A.real == B.real == C.real == 50.00 and D.real == E.real == 37.00
assert A.imag == E.imag == 15.00 and C.imag == D.imag == 35.00
assert abs(B - A) == 10 and abs(C - B) == 10 and abs(D - C) == 13 and abs(E - D) == 20 and abs(A - E) == 13
assert round(area([A, B, C, D, E]), 2) == 260.00  # 登記記録の地積 260.00㎡ と一致
check('A・B・Cが一直線', 'A、B、CのX座標は3つとも50.00、DとEは37.00')
check('CDの表示', '[Abs] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]` で、表示は13')
check('DE', '南側の辺DEは同じように20')
check('AB・BC・EA', '北側はABもBCも10、西側のEAは13')
check('地積との一致', '20かける13で260。登記記録の地積260.00平方メートルとぴったり一致')
assert round(20.0 * 100 / 500, 1) == 4.0
check('縮尺換算', '20メートルなら図面上は4センチ')
check('北側の境の切り替わり', 'AからBまでは隣地の16番11との境、BからCまでは道路（100番9）との境')

# ---- 建物図面：筆界からの距離は小数第1位（問題文の注4）。解答例の建物図面は 1.5・1.5・1.0 ----
check('建物図面の距離', '『1.5』『1.5』『1.0』')
# 建物の位置：和室の北の外壁が辺ABから1.5、ウォークインクローゼットの西の外壁が辺EAから1.0
bx0, bx_n = E.imag + 1.0, A.real - 1.5  # 建物座標の原点（西の壁のY、和室の北の壁のX）
assert (bx0, bx_n) == (16.0, 48.5)

# ---- 1階：母屋のみ（車庫＝周壁なし、出窓＝下端0.90・高さ1.10、ポーチは外）----
F1 = [(0.9, 0), (4.5, 0), (4.5, 0.9), (11.25, 0.9), (11.25, 2.7), (10.8, 2.7), (10.8, 8.1),
      (6.3, 8.1), (6.3, 6.75), (4.5, 6.75), (4.5, 6.3), (0, 6.3), (0, 3.6), (0.9, 3.6)]
s1 = [(0.90, 2.70), (3.60, 6.30), (1.80, 5.85), (4.50, 7.20), (0.45, 1.80)]
a1 = sum(w * h for w, h in s1)
assert round(a1, 4) == 68.85 == round(poly_area(F1), 2)
# 寸法線からの拾い方
assert round(0.90 + 1.80 + 0.90 + 2.70, 2) == 6.30
assert round(1.80 + 0.90 + 2.70 + 0.45, 2) == 5.85
assert round(1.35 + 3.15, 2) == 4.50
assert round(8.1 - 0.9, 2) == 7.20
for w, h in s1:
    check(f'1階 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('1階 合計', '合計：68.8500 （床面積：68.85平方メートル）')
check('和室・洋室の列の縦', '縦6.30メートル（0.90足す1.80足す0.90足す2.70）')
check('ホール・玄関の列の縦', '1.80足す0.90足す2.70足す0.45）')
check('キッチン・LDの列の横', '横4.50メートル（1.35足す3.15）')
check('出窓の高さ', '床から0.90メートル上から始まって、高さは1.10メートル')
check('出窓の算入要件', '高さが1.5メートル以上で、しかも下の端が床面と同じ高さにあるものだけ')
check('車庫の寸法（藍子の誤答）', '車庫3.15かける4.50')
# 藍子の誤り：車庫を足すと 83.025（記事では数値を出さず、比較図で示す）
assert round(a1 + 3.15 * 4.50, 3) == 83.025

# ---- 2階：母屋＋（あ）部分の洋室（屋外廊下・バルコニーは外気と分断されていない）----
F2 = [(0.9, 0), (4.5, 0), (4.5, 0.9), (7.65, 0.9), (7.65, 2.7), (10.8, 2.7), (10.8, 8.1),
      (7.2, 8.1), (7.2, 6.3), (0.9, 6.3)]
AA = [(12.6, -0.9), (15.75, -0.9), (15.75, 3.6), (12.6, 3.6)]
s2 = [(3.60, 6.30), (2.70, 5.40), (0.45, 7.20), (3.15, 5.40), (3.15, 4.50)]
a2 = sum(w * h for w, h in s2)
assert round(a2, 4) == 71.685 == round(poly_area(F2) + poly_area(AA), 3)
assert round(poly_area(F2), 2) == 57.51
assert trunc2(a2) == 71.68 and round(a2 + 1e-9, 2) == 71.69  # 四捨五入なら71.69になる＝わな
for w, h in s2:
    check(f'2階 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('2階 合計', '合計：71.6850')
check('2階 床面積（切り捨て）', '71.685の5は切り捨てて、71.68平方メートルよ')
# 0.45の列：上の寸法線（トイレの東の壁）と下の寸法線（東の洋室の西の壁）の差
top = 3.60 + 1.80 + 1.35
bottom = 2.70 + 1.80 + 0.90 + 0.90
assert round(top, 2) == 6.75 and round(bottom, 2) == 6.30 and round(top - bottom, 2) == 0.45
check('上の寸法線', '3.60足す1.80足す1.35で、6.75')
check('下の寸法線', '2.70足す1.80足す0.90足す0.90で、6.30')
check('0.45のずれ', '6.75と6.30で、0.45ずれてます')
# 藍子の誤り：東の洋室の西の壁（下の寸法線）でそろえ、トイレの東の端 0.45×1.80 を落とす
wrong = 3.60 * 6.30 + 2.70 * 5.40 + 3.60 * 5.40 + 3.15 * 4.50
assert round(wrong, 4) == 70.875 and round(a2 - wrong, 2) == round(0.45 * 1.80, 2) == 0.81
check('藍子の2階（誤答）', '東の洋室の列が3.60かける5.40')
check('藍子の2階 合計（誤答）', '合計70.8750です')
check('落とした部分', '横0.45メートル×縦1.80メートルの部分が抜け落ちるの。0.81平方メートルの損')
check('（あ）の縦', '縦4.50メートル（0.90足す2.70足す0.90）')
assert round(0.90 + 2.70 + 0.90, 2) == 4.50

# ---- 問1（第1欄）・問4（第4欄）----
check('第1欄', 'ア＝確認、イ＝検査、ウ＝建築請負人、エ＝固定資産税')
check('第4欄', 'だから①構造上、②利用上')
check('問1 エの対比', '登録免許税は、登記を受けるときに納める税金よ')
check('問4 の対比', '構造上と利用上を入れ替えて覚えてるわね')

# ---- 問2（第2欄）----
check('登記の目的', '建物表題登記です')
check('添付書類', '建物図面、各階平面図、所有権証明書、住所証明書、代理権限証書の5点')
check('登記識別情報は不要', '登記識別情報は、所有権の登記をしたときに登記名義人に通知されるもの')
check('所在', '『A市B町三丁目16番地13』')
check('種類', '種類は『居宅』')
check('構造', '『木造合金メッキ鋼板ぶき2階建』')
check('床面積', '床面積は1階68.85平方メートル、2階71.68平方メートル')
check('原因及びその日付', '『令和6年9月30日新築』')
check('共有者', '『共有者　A市B町三丁目16番地13　持分5分の3　甲野松雄』『A市B町三丁目16番地13　5分の2　甲野桜子』')
check('申請人と共有者の区別', '申請人は、実際に申請の手続をする人。表題部所有者は、登記記録に建物の持ち主として載る人')

# ---- 付属プロンプトとの整合 ----
check('添付書類', '建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書', form, '申請書')
check('床面積', '「1階　68｜85」「2階　71｜68」', form, '申請書')
check('原因', '「令和６年９月30日新築」', form, '申請書')
check('共有者1', '持分　５分の３　　甲野松雄', form, '申請書')
check('共有者2', '５分の２　　甲野桜子', form, '申請書')
check('正解1', '持分　５分の３　　甲野松雄', fix, '添削')
check('正解2', '５分の２　　甲野桜子', fix, '添削')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')

# 解説図プロンプトの頂点座標（Y＝東、X＝南、上が北）が求積表と一致すること
BAL = [(0.9, 6.3), (7.2, 6.3), (7.2, 8.1), (10.8, 8.1), (10.8, 9), (6.3, 9), (6.3, 7.2), (0.9, 7.2)]
SITE_BLDG = [(bx0 + y, bx_n - x) for y, x in F1]
for label, pts, want in [('図5 1階', F1, 68.85), ('図6 2階（母屋）', F2, 57.51),
                         ('図6 バルコニー', BAL, None), ('図3 建物図面の1階', SITE_BLDG, 68.85)]:
    if want is not None:
        assert round(poly_area(pts), 2) == want, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
# 建物図面：建物が敷地（Y 15〜35、X 37〜50）の内側にあり、北から1.5・西から1.0
assert all(15 < y < 35 and 37 < x < 50 for y, x in SITE_BLDG)
assert max(x for _, x in SITE_BLDG) == 48.5 and min(y for y, _ in SITE_BLDG) == 16.0
for s in ['辺AB：「10.0m」', '辺BC：「10.0m」', '辺CD：「13.0m」', '辺DE：「20.0m」', '辺EA：「13.0m」',
          '「1.5」×2、「1.0」×1', '1階 床面積：68.85㎡', '2階 床面積：71.68㎡（合計71.685を切り捨て）',
          'Y：7.2〜7.65、X：0.9〜2.7。横0.45m×縦1.80m、面積0.81', 'Y：12.6〜15.75、X：−0.9〜3.6（横3.15m×縦4.50m、面積14.175）']:
    check('図の数値', s, fig, '解説図')

# ---- 形状・向き（図面の上＝北。問題の図1の方位記号と注6で確認）----
check('（あ）部分の位置', '屋外廊下で隔てられた東側の（あ）部分')
check('浴室の出っ張り', '浴室の東の出っ張り：横0.45メートル × 縦1.80メートル')
for bad in ['PDF', '創設的登記', '『1.50』『1.50』', '列を丸ごと', 'トイレの北東にある', '北側の線も東側の線も']:
    absent('誤記・混入', bad)

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = text.splitlines()[0]
prefix = '# 【土地家屋調査士受験生向け】令和6年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和6年度問題22（建物）', thumb, '見出し画像')

print('NG件数:', ng)
