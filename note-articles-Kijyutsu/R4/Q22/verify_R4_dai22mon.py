"""令和4年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第1〜3欄・各階平面図・求積表・建物図面）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R4/Q22/verify_R4_dai22mon.py"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, area, fmt_num

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_R4_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_R4_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_R4_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_R4_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_R4_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


# ---- 敷地：〔座標値一覧表〕A〜D（X＝北、Y＝東）。図1では東側が縦線に見えるが、座標では辺BCだけが斜め ----
A, B, C, D = P(50.00, 50.00), P(50.00, 78.00), P(70.00, 80.00), P(70.00, 50.00)
assert A.imag == D.imag == 50.00 and B.imag != C.imag  # 西側ADは真北向き、東側BCは斜め
assert abs(B - A) == 28 and abs(D - C) == 30 and abs(A - D) == 20
bc = abs(C - B)
assert fmt_num(bc) == '20.0997…' and round(bc, 1) == 20.1
check('座標の読み取り', 'A点が（50.00、50.00）、B点が（50.00、78.00）、C点が（70.00、80.00）、D点が（70.00、50.00）')
check('辺BCが斜め', '東側のBとCは、Y座標が78.00と80.00で違います')
check('BCの表示', '[Abs] [ALPHA] [C] [−] [ALPHA] [B] [)] [=]` で、表示は20.0997…')
check('他の辺', 'ABが28、CDが30、DAが20')
check('A点の記憶', '`50 [+] 50 [i] [SHIFT] [STO] [A]`')
assert round(30.0 * 100 / 500, 1) == 6.0
check('縮尺換算', '30メートルの北側の辺なら図面上は6センチ')
check('辺長は建物図面に書かない', 'この辺長は建物図面には書かないのよ')
check('各辺の相手方', '南側の辺ABは道路（102）との境、東側の辺BCは道路（5番4）との境、北側の辺CDは隣地の5番2との境、西側の辺DAは隣地の5番1との境')

# ---- 建物図面：筆界からの距離は小数第1位（問題文の注4）。解答例の建物図面は 3.0・3.0・2.0／1.0・1.0・2.0 ----
def bc_y(x):
    """辺BC上で、X座標がxの点のY座標。"""
    return B.imag + (x - B.real) * (C.imag - B.imag) / (C.real - B.real)


main_s = A.real + 3.0                      # 主である建物の南の外壁（辺ABから3.0）
main_e = bc_y(main_s) - 2.0                # 南東の角から辺BCまで2.0
gar_n = D.real - 1.0                       # 車庫の北の外壁（辺CDから1.0）
gar_s = gar_n - 4.00                       # 車庫の南北4.00
gar_e = bc_y(gar_s) - 2.0                  # 車庫の南東の角から辺BCまで2.0
assert (round(main_s, 2), round(main_e, 2), round(gar_n, 2), round(gar_s, 2), round(gar_e, 2)) == (53.0, 76.3, 69.0, 65.0, 77.5)
assert round(bc_y(gar_n) - gar_e, 1) == 2.4  # 車庫の北東の角から測ると約2.4
check('建物図面の距離（主）', '『3.0』『3.0』『2.0』')
check('建物図面の距離（車庫）', '『1.0』『1.0』『2.0』')
check('東側の2.0は南東の角から', '東側の2.0は、主である建物も車庫も、南東の角から測っている')
check('北東の角からだと約2.4', '車庫なら北東の角から辺BCまでは約2.4メートル')

# ---- 1階：元の附属建物5.00×5.00＋増築部分4.00×4.00＋元の主である建物9.00×8.00（壁心。注7の0.15は引かない）----
F1 = [(0, 3), (5, 3), (5, 4), (9, 4), (9, 0), (18, 0), (18, 8), (0, 8)]
s1 = [(5.00, 5.00), (4.00, 4.00), (9.00, 8.00)]
a1 = sum(w * h for w, h in s1)
assert round(a1, 4) == 113.00 == round(poly_area(F1), 2)
assert round(5.00 - 1.00, 2) == round(8.00 - 4.00, 2) == 4.00  # 増築部分の南北は2通りで一致
assert round(5.00 + 4.00 + 9.00, 2) == 18.00                   # 下の寸法線18.00と一致
assert 5.00 * 5.00 == 25.00 and 9.00 * 8.00 == 72.00           # 登記記録の床面積と一致
for w, h in s1:
    check(f'1階 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('1階 合計', '合計：113.0000 （床面積：113.00平方メートル）')
check('増築部分の南北', '附属建物の5.00から、北の壁の段差の1.00を引いて4.00。主である建物の8.00から、北側の4.00を引いても4.00')
check('東西の合計', '5.00足す4.00足す9.00で18.00')
check('壁心（内法ではない）', '壁の内側、つまり内法で測るのは区分建物のときよ')
check('0.15は引かない', '0.15は引かなくていいのよ')

# ---- 2階：元の附属建物の2階 5.00×5.00（〇印＝注6の重なる部分）----
F2 = [(0, 3), (5, 3), (5, 8), (0, 8)]
assert poly_area(F2) == 25.00
check('2階 求積', '5.00 × 5.00 ＝ 25.0000\n- 合計：25.0000 （床面積：25.00平方メートル）')
check('1階の位置の点線', '1階の位置の表示は省略できないことになっているわ')

# ---- 車庫（符号2）：胴縁の中心から0.05内側＝鉄骨柱の外面（注8・注9・図4）----
dobuchi = 0.10
w_c, h_c = 5.10, 4.10                          # 図3の寸法（胴縁の中心）
w_g, h_g = round(w_c - dobuchi, 2), round(h_c - dobuchi, 2)
assert (w_g, h_g) == (5.00, 4.00) and trunc2(w_g * h_g) == 20.00
wrong = round(w_c * h_c, 4)
assert wrong == 20.91 and round(wrong - w_g * h_g, 2) == 0.91
check('藍子の誤答', '5.10かける4.10で、20.91平方メートル！')
check('胴縁の中心から柱の外面', '胴縁の中心から柱の外面までは、胴縁の厚さの半分の0.05メートル')
check('柱の外面の寸法', '横は5.10引く0.10で5.00メートル、縦は4.10引く0.10で4.00メートル。5.00かける4.00で、20.00平方メートルです')
check('差', '0.91平方メートルも差がつく')
check('車庫 求積表', '5.00 × 4.00 ＝ 20.0000\n- 合計：20.0000 （床面積：20.00平方メートル）')

# ---- 問2（第2欄）・問3（第3欄）----
check('第2欄', 'ア＝効用上一体、イ＝所有者の意思、ウ＝1個の建物、エ＝所有者')
check('第3欄', '①所有者、②従、③付合、④権原')
check('問2 エの対比（種類⇔所有者）', 'エは『種類』です')
check('問2 エの訂正', '1個の建物として登記できなくなるのは、持ち主が違うとき')
check('問3 ④の対比（権限⇔権原）', '④権限です')
check('問3 ④の訂正', 'ここで使うのは『権原』')
check('問3 増築部分の帰属', '増築部分は、建物の所有者の令子さんのものになるの')
check('償金', '民法第248条')

# ---- 問1（第1欄）----
check('登記の目的の対比（合体登記⇔表題部変更登記）', '建物合体登記です')
check('合体の登記の根拠', '不動産登記法第49条の合体の登記')
check('登記の目的', '申請するのは『建物表題部変更登記』よ')
check('添付書類', '建物図面、各階平面図、所有権証明書、代理権限証書の4点')
check('所有権証明書の根拠', '不動産登記令別表14の項')
check('申請人', '『A市B町一丁目5番3号　和田令子』')
check('所在', '所在は『A市B町一丁目5番地3』')
check('家屋番号', '家屋番号は『5番3』のまま')
check('変更前の主', '『主』、事務所、木造スレートぶき平家建、72.00平方メートル')
check('変更後の主', '種類は居宅、構造は木造スレートぶき2階建、床面積は1階113.00平方メートル、2階25.00平方メートル')
check('原因（誤答）', '『③令和4年9月30日増築、符号1の附属建物合体』です！')
check('原因（正解）', '『①②③令和4年9月30日種類・構造変更、増築、符号1の附属建物合体』')
check('構造の3要素', '主な部分の構成材料、屋根の種類、階数の3つで決まるの（不動産登記規則第114条）')
check('符号1', '『符号1』、倉庫、木造スレートぶき2階建、1階25.00平方メートル、2階25.00平方メートル。原因は『令和4年9月30日主である建物に合体』')
check('符号2', '『符号2』。車庫、鉄骨造亜鉛メッキ鋼板ぶき平家建、20.00平方メートル、原因は『令和4年9月30日新築』')
check('符号1を使わない理由', '符号1はその附属建物の番号として使い終わったの')

# ---- 付属プロンプトとの整合 ----
check('登記の目的', '**登記の目的**：建物表題部変更登記', form, '申請書')
check('添付書類', '建物図面　各階平面図　所有権証明書　代理権限証書', form, '申請書')
check('申請人', 'Ａ市Ｂ町一丁目５番３号　和田令子', form, '申請書')
check('所在', 'Ａ市Ｂ町一丁目５番地３', form, '申請書')
check('変更前の主', '「72｜00」', form, '申請書')
check('変更後の床面積', '「1階　113｜00」「2階　25｜00」', form, '申請書')
cause = '①②③令和４年９月30日種類・構造変更、増築、符号１の附属建物合体'
check('原因', cause, form, '申請書')
check('符号1の原因', '令和４年９月30日主である建物に合体', form, '申請書')
check('符号2の床面積', '「20｜00」', form, '申請書')
check('符号2の原因', '「令和４年９月30日新築」', form, '申請書')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')
check('正解', cause, fix, '添削')
check('誤答', '③令和４年９月30日増築、符号１の附属建物合体', fix, '添削')

# 解説図プロンプトの頂点座標（建物＝Y東・X南、敷地＝Y東・X北）が求積表と一致すること
SITE_BLDG = [(round(58.3 + y, 1), round(61 - x, 1)) for y, x in F1]
GARAGE_SITE = [(72.5, 69), (77.5, 69), (77.5, 65), (72.5, 65)]
GARAGE = [(0, 0), (5, 0), (5, 4), (0, 4)]
GARAGE_WRONG = [(-0.05, -0.05), (5.05, -0.05), (5.05, 4.05), (-0.05, 4.05)]
assert max(x for _, x in SITE_BLDG) == 61 and min(x for _, x in SITE_BLDG) == main_s
assert max(y for y, _ in SITE_BLDG) == round(main_e, 1)
assert GARAGE_SITE[1] == (gar_e, gar_n) and GARAGE_SITE[2] == (gar_e, gar_s)
for label, pts, want in [('図4 1階', F1, 113.00), ('図5 2階', F2, 25.00), ('図3 建物図面の1階', SITE_BLDG, 113.00),
                         ('図3 車庫', GARAGE_SITE, 20.00), ('図6 正解', GARAGE, 20.00), ('図6 誤り', GARAGE_WRONG, 20.91)]:
    assert round(poly_area(pts), 2) == want, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
# 建物図面：建物が敷地の内側にある（辺BCより西、辺ABより北、辺CDより南、辺DAより東）
for y, x in SITE_BLDG + GARAGE_SITE:
    assert 50 < x < 70 and 50 < y < bc_y(x)
for s in ['辺AB：「28.0m」', '辺BC：「20.1m」', '辺CD：「30.0m」', '辺DA：「20.0m」',
          '「3.0」×2、「2.0」×2、「1.0」×2', '1階 床面積：113.00㎡', '2階 床面積：25.00㎡',
          '5.10×4.10＝20.91㎡', '5.00×4.00＝20.00㎡', 'Y＝78＋（53−50）×0.1＝78.3', 'Y＝78＋（65−50）×0.1＝79.5']:
    check('図の数値', s, fig, '解説図')

# ---- 形状・向き（図面の上＝北。問題の注3と図1の方位記号で確認）----
check('建物の並び', '西から東へ3つの長方形に分けます')
check('2階の位置', '1階と2階の北西の角に付いています')
check('北側の段の向き', '北側は増築部分だけが元の附属建物より1.00m南へ引っ込み、元の主である建物が一番北まで出ている')
check('北側の段の向き', '北側は増築部分だけが元の附属建物より1.00m南へ引っ込み、元の主である建物が一番北まで出ている', fig, '解説図')
assert F1[1][1] < F1[2][1] and F1[4][1] < F1[0][1]  # 増築部分(X=4)は附属(X=3)より南、主(X=0)は最も北
check('BCの向き', '東側の辺BCは、北へ行くほど東へ2メートル開いていく斜めの線です')
for bad in ['PDF', '創設的登記', '段々', '『3.00』', '『2.00』', '『1.00』', '右上', '左下', '右側', '左側']:
    absent('誤記・混入', bad)

# ---- note向けの体裁：話者名の行末に半角スペース2つ、名前とセリフの間に空行なし ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
ok = n_marker == 8
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカー（引用形式）: {n_marker}個（解説図6＋添削1＋完成形1＝計8か所の想定）')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和4年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和4年度問題22（建物）', thumb, '見出し画像')

print('NG件数:', ng)
