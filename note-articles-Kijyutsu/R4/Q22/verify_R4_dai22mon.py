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


# 距離は外壁まで（〔調査図〕の（注）4）。木造の壁の中心線は外壁から0.075内側（壁厚0.15、同（注）7）、
# 車庫の鉄骨柱の外面は外壁から0.15内側（胴縁0.10＋被覆材0.05、図4）
HALF, COVER = 0.075, 0.15
main_s = A.real + 3.0                      # 主である建物の南の外壁（辺ABから3.0）X＝53.00
main_e = bc_y(main_s) - 2.0                # 南東の角の東の外壁 Y＝76.30
main_w = main_e - 18.00 - 2 * HALF         # 西の外壁 Y＝58.15
N0, W0 = main_s + HALF + 8.00, main_e - HALF - 18.00   # 壁の中心線の北西の角 (X＝61.075, Y＝58.225)
gar_n = D.real - 1.0                       # 車庫の北の外壁（辺CDから1.0）X＝69.00
gar_s = gar_n - COVER - 4.00 - COVER       # 車庫の南の外壁 X＝64.70
gar_e = bc_y(gar_s) - 2.0                  # 車庫の南東の角の東の外壁 Y＝77.47
G_N, G_E = gar_n - COVER, gar_e - COVER    # 柱の外面の北東の角 (X＝68.85, Y＝77.32)
assert (round(main_s, 2), round(main_e, 2), round(main_w, 2), round(N0, 3), round(W0, 3)) == (53.0, 76.3, 58.15, 61.075, 58.225)
assert (round(gar_n, 2), round(gar_s, 2), round(gar_e, 2), round(G_N, 2), round(G_E, 2)) == (69.0, 64.7, 77.47, 68.85, 77.32)
assert round(bc_y(gar_n) - gar_e, 1) == 2.4  # 車庫の北東の角から測ると約2.4
assert round(main_w - D.imag, 2) == 8.15     # 西の辺DAまで8メートル以上
check('所在の確認（主）', '南東の角の高さで辺BCはY＝78.00＋3.00×0.1＝78.30だから、東の外壁はY＝76.30')
check('所在の確認（西の端）', '壁の厚さ0.15（両側の半分ずつ）を引いたY＝58.15で、西の辺DA（Y＝50.00）まで8メートル以上')
check('所在の確認（車庫）', '南の外壁は、柱の外面どうしの4.00と、外側の胴縁・被覆材の厚さ0.15（両側）を引いたX＝64.70で、その高さで辺BCはY＝79.47だから、東の外壁はY＝77.47')
check('所在は5番地3だけ', '所在は『A市B町一丁目5番地3』だけで、ほかの地番は出てこない')
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
SITE_BLDG = [(round(W0 + y, 3), round(N0 - x, 3)) for y, x in F1]
GARAGE_SITE = [(round(G_E - 5, 2), round(G_N, 2)), (round(G_E, 2), round(G_N, 2)), (round(G_E, 2), round(G_N - 4, 2)),
               (round(G_E - 5, 2), round(G_N - 4, 2))]
GARAGE = [(0, 0), (5, 0), (5, 4), (0, 4)]
GARAGE_WRONG = [(-0.05, -0.05), (5.05, -0.05), (5.05, 4.05), (-0.05, 4.05)]
assert max(x for _, x in SITE_BLDG) == round(N0, 3) and min(x for _, x in SITE_BLDG) == round(main_s + HALF, 3)
assert max(y for y, _ in SITE_BLDG) == round(main_e - HALF, 3)
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
          '5.10×4.10＝20.91㎡', '5.00×4.00＝20.00㎡', 'Y＝78＋（53−50）×0.1＝78.3', 'Y＝78＋（64.70−50）×0.1＝79.47', '南西の角〈Y＝58.15〉', '北西の角〈Y＝72.17〉',
          'E：14.095〜19.095、S：−7.775〜−3.775']:
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
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# ---- 2026-09-29の追加作業で足した内容（最新の執筆プロンプト・依頼文との照らし合わせ） ----
check('準則第94条第2項（欄番号）', '不動産登記事務取扱手続準則第94条第2項の書き方')
check('準則第95条（附属建物合体）', '準則第95条に書き方があって、例として『③令和何年何月何日増築及び附属建物合体』、附属建物の側は『主たる建物に合体』')
check('規則第83条第1項（主・附属の別と符号）', '主である建物か附属建物かの別と附属建物の符号も、各階平面図に書く事項よ（不動産登記規則第83条第1項）')
check('第4欄の家屋番号・建物の所在', '家屋番号は『5番3』、建物の所在は『A市B町一丁目5番地3』。作成者と申請人の欄は（略）と印刷されている')
check('所有権証明書の欄', '不動産登記令別表14の項添付情報欄ロ（2）・ハ')
check('登録免許税の根拠', '建物の表題部の変更の登記は、登録免許税法別表第一に載っていない')
check('解く順番（問を先に）', '前文と問題文の注と問1〜問4を、別紙より先に読むの')
check('解く順番（1枚の申請書から附属建物の見当）', '問1の申請書が『本件建物及び本件車庫に関する登記』の1枚だとわかった時点で')
check('解く順番（寸法の累計のメモ）', '寸法線を足した累計（東西は0・5・9・18、南北は0・3・4・8）')
check('各階平面図は左・建物図面は右', '各階平面図は用紙の左、建物図面は右の、同じ1枚の用紙に描く')
assert [0, 5, 9, 18] == [0, 5, 5 + 4, 5 + 4 + 9] and [0, 3, 4, 8] == [0, 8 - 5, 8 - 4, 8]  # 北西の角からの累計

# 注の書き分け：「注N」は必ず「問題文の注N」、〔調査図〕の注は「（注）N」と書く
bare = [m.start() for m in re.finditer(r'(?<!（)注[0-9]', text) if text[max(0, m.start() - 4):m.start()] != '問題文の']
ng += bool(bare)
print(('OK ' if not bare else 'NG ') + f'注の書き分け（「問題文の」のない「注N」）: {len(bare)}か所')
for m in re.finditer(r'（注）[0-9]+', text):
    ctx = text[max(0, m.start() - 12):m.start()]
    ok = '〔調査図〕の' in ctx or ctx.endswith('と') or ctx.endswith('同')
    ng += (not ok)
    if not ok:
        print('NG 〔調査図〕の（注）の書き分け :', text[m.start() - 12:m.end()])
print('OK 〔調査図〕の（注）の書き分け（直前の確認）')

# 同じ話者のセリフの連続（画像挿入マーカーをはさんでも1つの連続とみなす）
prev = None
cont = []
for i, line in enumerate(lines):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        if line == prev:
            cont.append(i + 1)
        prev = line
ng += bool(cont)
print(('OK ' if not cont else 'NG ') + f'同じ話者の連続 : {cont}')
for bad in ['✕', '✓', '名変', '奥側', '手前側']:
    absent('記号・略語・向き', bad)

# ---- 画像（2026-09-29生成）：記事の画像挿入マーカー8か所に対応するPNGがそろっているか ----
from PIL import Image
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('工事前（家屋番号5番3', 'R4_dai22mon_zu01_kouji_zengo'), ('本件土地をA・B・C・D点で結んだ台形', 'R4_dai22mon_zu02_shikichi_henchou'),
        ('建物図面の完成形', 'R4_dai22mon_zu03_tatemono_zumen'), ('1階の床面積求積図', 'R4_dai22mon_zu04_1kai_kyuuseki'),
        ('2階の床面積求積図', 'R4_dai22mon_zu05_2kai_kyuuseki'), ('車庫の誤り比較図', 'R4_dai22mon_zu06_shako_ayamari_hikaku'),
        ('「原因及びその日付」欄の①誤答', 'R4_dai22mon_toukishinseisho_machigai'),
        ('登記申請書（問1）の完成形', 'R4_dai22mon_toukishinseisho_kansei')]
ok = len(markers) == len(PNGS) and all(k in m for m, (k, _) in zip(markers, PNGS))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーとPNGの対応（記事の順） : {len(markers)}か所')
for _, name in PNGS:
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path)
    if ok and 'toukishinseisho' in name:
        w, h = Image.open(path).size
        ok = w == 1200 and h > w    # 申請書・添削は横1200pxの縦長
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + 'PNG : ' + name)
    check('解説図・申請書プロンプトのファイル名', name, fig + form + fix, 'プロンプト')


def html_has(name, *needles):
    global ng
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        ok = n in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : {n}')
    return h


h = html_has('R4_dai22mon_toukishinseisho_kansei', '建物表題部変更登記', '建物図面　各階平面図　所有権証明書　代理権限証書',
             '令和４年10月17日　申請　　Ｅ地方法務局', 'Ａ市Ｂ町一丁目５番３号　和田令子', 'Ａ市Ｂ町一丁目５番地３', '５番３',
             '原因及びその日付', '事務所', '居宅', '倉庫', '車庫', '>72<', '1階　113', '2階　25', '>20<', '符号１', '符号２',
             '①②③令和４年９月30日種類・<br>構造変更、増築、符号１の附属<br>建物合体', '令和４年９月30日主である<br>建物に合体',
             '令和４年９月30日新築', '鉄骨造亜鉛<br>メッキ鋼板<br>ぶき平家建')
for bad in ['登録免許税', '住所証明書', '登記識別情報', '20.91', '登記原因及びその日付', '建物合体登記']:
    absent('申請書のHTML', bad, h, '申請書HTML')
html_has('R4_dai22mon_toukishinseisho_machigai', '③令和４年９月30日増築、符号１<br>の附属建物合体', '∨①②', '∨種類・構造変更、',
         '①②③令和４年９月30日種類・<br>構造変更、増築、符号１の附属<br>建物合体', '<svg class="check"')
for bad in ['✓', '✕', '横1600']:
    absent('添削・申請書プロンプトの記号', bad, form + fix, 'プロンプト')
check('添削は縦に3段', '横1200px（縦長', fix, '添削')
drw = open(os.path.join(ZU, 'draw_R4_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
n_fit = len(re.findall(r"\bfit\(", drw))
ok = n_fit > 0 and drw.count('pad_aspect=True') == n_fit
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit はすべて pad_aspect=True : {n_fit}か所')
for n in ['assert round(area([P(*v) for v in F1]), 2) == 113.00', 'assert round(area([P(*v) for v in GAR_WRONG]), 2) == 20.91',
          '(61.075, 58.225, 68.85, 64.7, 77.47, 72.32)']:
    check('作図スクリプトの検算', n, drw, '作図')

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
