"""令和3年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第1〜3欄・各階平面図・求積表・建物図面）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R3/Q22/verify_R3_dai22mon.py"""
import math
import os
import re
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import chiseki, fmt_num

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_R3_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_R3_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_R3_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_R3_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_R3_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


def inset(v):
    """壁心の寸法 → 内法の寸法（柱の中心から内壁まで0.10、両側で0.20。図4の注2）。"""
    return round(v - 0.20, 2)


# ---- 敷地：座標値一覧表はなく、図1の辺長だけ。北側19.70（15.70＋4.00）、東側18.70、南側17.58、西側16.58、南西の隅切り3.00 ----
north, east, south, west, cut = 15.70 + 4.00, 18.70, 17.58, 16.58, 3.00
leg1, leg2 = round(east - west, 2), round(north - south, 2)
assert leg1 == leg2 == 2.12
assert fmt_num(abs(complex(leg1, leg2))) == '2.9981…' and round(abs(complex(leg1, leg2)), 2) == cut
site_area = north * east - leg1 * leg2 / 2
assert round(site_area, 4) == 366.1428 and chiseki(site_area) == 366.14  # 登記記録の地積 366.14㎡ と一致
SITE = [(0, 18.70), (15.70, 18.70), (19.70, 18.70), (19.70, 0), (2.12, 0), (0, 2.12)]
assert round(poly_area(SITE), 4) == 366.1428
check('北側の辺長', '4番3との境が15.70、4番1との境が4.00で、合わせて19.70')
check('他の辺', '東側は18.70。西側は16.58、南側は17.58、隅切りが3.00')
check('隅切りの2辺', '東側の18.70から西側の16.58を引くと2.12。北側の19.70から南側の17.58を引いても2.12')
check('隅切りの表示', '`[Abs] 2.12 [+] 2.12 [i] [)] [=]`。表示は2.9981…')
check('地積との一致', '368.39引く2.2472で、366.1428。宅地は小数第2位未満を切り捨てて366.14平方メートル')
assert round(north * east, 2) == 368.39 and round(leg1 * leg2 / 2, 4) == 2.2472
check('方位', '北の方向は敷地の西側の道路と平行です。図の上が北')
check('各辺の相手方', '北側が隣地の4番3と4番1との境、東側が5番1との境、南側が道路（116）との境、西側が道路（115）との境')
check('辺長は建物図面に書かない', 'この辺長は建物図面には書かないのよ')

# ---- 建物図面：筆界からの距離（図1の数値どおり小数第2位）。解答例の建物図面は 1.00・2.50・2.50 ----
check('建物図面の距離', '『1.00』『2.50』『2.50』')
check('実線と点線', '（イ）部分の1階の形を実線で描いて、一棟の建物の残りの1階、つまり（ロ）部分の1階は点線で描く')
check('建物図面の家屋番号', '家屋番号の欄は『B町三丁目5番2の1』、建物の所在の欄は『A市B町三丁目5番地2』')

# ---- 一棟の建物（壁心）：1階 16.00×11.00−3.00×1.00＝173.00、2階 16.00×11.00＝176.00（登記記録と一致）----
WHOLE1 = [(0, 0), (6.5, 0), (6.5, 1), (9.5, 1), (9.5, 0), (16, 0), (16, 11), (0, 11)]
assert poly_area(WHOLE1) == 173.00 and 16 * 11 == 176

# ---- （イ）部分：壁心で測ると 86.50・88.00（藍子の誤答）、内法で 82.74・84.24 ----
I1_WALL = [(0, 0), (6.5, 0), (6.5, 1), (8, 1), (8, 11), (0, 11)]
I1 = [(0.1, 0.1), (6.4, 0.1), (6.4, 1.1), (7.9, 1.1), (7.9, 10.9), (0.1, 10.9)]
I2 = [(0.1, 0.1), (7.9, 0.1), (7.9, 10.9), (0.1, 10.9)]
wrong1, wrong2 = round(6.50 * 1.00 + 8.00 * 10.00, 2), 8.00 * 11.00
assert wrong1 == 86.50 == poly_area(I1_WALL) and wrong1 * 2 == 173.00
assert (inset(6.50), inset(8.00), inset(11.00), inset(10.00)) == (6.30, 7.80, 10.80, 9.80)
s1 = [(6.30, 1.00), (7.80, 9.80)]
a1 = sum(w * h for w, h in s1)
a2 = 7.80 * 10.80
assert trunc2(a1) == 82.74 == round(poly_area(I1), 2) and trunc2(a2) == 84.24 == round(poly_area(I2), 2)
assert round(wrong1 - a1, 2) == round(wrong2 - a2, 2) == 3.76
check('藍子の誤答（壁心）', '合わせて86.50平方メートル。2階は8.00×11.00で88.00平方メートルです！')
check('誤答の検算', '86.50の2倍で173.00')
check('内法の根拠', '区分建物の床面積は、壁その他の区画の内側の線、つまり内法で囲まれた部分で測るの（不動産登記規則第115条）')
check('0.10の根拠', '柱の中心から内壁までは10センチメートル')
check('辺の拾い直し', '北側は6.50引く0.20で6.30。南側は8.00引く0.20で7.80。西側は11.00引く0.20で10.80、東側は10.00引く0.20で9.80')
check('欠けの大きさ', '欠けの大きさは、横1.50、縦1.00のまま変わらない')
for w, h in s1:
    check(f'1階 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('1階 合計', '合計：82.7400 （床面積：82.74平方メートル）')
check('2階 求積', '7.80 × 10.80 ＝ 84.2400\n- 合計：84.2400 （床面積：84.24平方メートル）')
check('差3.76', '86.50引く82.74で3.76、88.00引く84.24でも3.76')
check('階の表示', '平面図に『1階』『2階』と階の別を書き分けるの（不動産登記規則第83条第1項）')
check('2階に1階の欠けを点線', '2階の図には、2階と形が違う1階の北東の欠けの位置を点線で重ねる')

# ---- 問1（第1欄）----
check('登記の目的の対比（建物分割登記⇔建物区分登記）', '建物分割登記と取り違えなかった')
check('登記の目的', '建物区分登記です！')
check('申請人の対比（栄太⇔栄一）', '栄太さんです！')
check('申請人', '『A市B町三丁目5番1号』')
check('種類の対比（共同住宅⇔居宅）', '（イ）部分も共同住宅です！')
check('種類', '玄関が1つで1世帯が住む（イ）部分は『居宅』よ')
check('添付書類', '建物図面、各階平面図、代理権限証書の3点です')
check('規約証明書は不要', '何もしなくても、割合は2分の1ずつになるの')
assert round(a1 + a2, 2) == 166.98
check('（イ）（ロ）の合計', '合計はどちらも166.98で、まったく同じ')
check('登録免許税（誤答）', '今回書くのは（イ）部分だけなので、1,000円です！')
check('登録免許税', 'だから2,000円です')
check('一棟の表示', '所在は『A市B町三丁目5番地2』。建物の名称は付けていないので空欄。構造は登記記録どおり『鉄骨造スレートぶき2階建』。床面積は1階173.00平方メートル、2階176.00平方メートル')
check('一棟は壁心', '一棟は壁心、専有部分は内法')
check('敷地権の目的である土地', '土地の符号は『1』、所在及び地番は『A市B町三丁目5番2』、地目は『宅地』、地積は『366.14』平方メートル')
check('区分前の行', '家屋番号『5番2』、種類『共同住宅』、構造『鉄骨造スレートぶき2階建』、床面積は1階173.00、2階176.00平方メートル')
check('区分後の家屋番号', '『（イ）B町三丁目5番2の1』')
check('区分後の床面積', '床面積は1階82.74、2階84.24平方メートル')
check('構造の対比（屋根の省略⇔縦割り）', '『鉄骨造2階建』ですか？')
check('構造', '屋根の種類まで書いて『鉄骨造スレートぶき2階建』')
check('原因（誤答）', '1行目は『令和3年10月17日5番2の1、5番2の2に区分』、2行目は『令和3年10月17日5番2から区分』です！')
check('報告的⇔形成的', '区分は、所有者が申請して登記されて初めて区分の効果が生じる『形成的登記』')
check('原因（正解）', '1行目は『5番2の1、5番2の2に区分』、2行目は『5番2から区分』。日付なし')
check('敷地権の表示', '土地の符号は『1』、敷地権の種類は『所有権』、敷地権の割合は『2分の1』')
check('敷地権の原因', '『令和3年10月17日敷地権』')

# ---- 問2（第2欄）：(あ) 71.50、(い)部分等 9.70＋84.24＝93.94、敷地権の割合は(ロ)の2分の1を床面積で分ける ----
# （ロ）部分の座標（原点は（ロ）部分の北西の角の壁の中心、Y＝東、X＝南、内法）
RO1_WALL = [(0, 1), (1.5, 1), (1.5, 0), (8, 0), (8, 11), (0, 11)]
A_PART = [(0.1, 1.1), (1.6, 1.1), (1.6, 0.1), (7.9, 0.1), (7.9, 6.4), (5.2, 6.4), (5.2, 9.6), (5.9, 9.6), (5.9, 10.9), (0.1, 10.9)]
MARU_A = [(5.4, 6.6), (7.9, 6.6), (7.9, 10.9), (6.1, 10.9), (6.1, 9.4), (5.4, 9.4)]
I_PART = I2
assert poly_area(RO1_WALL) == 86.50
sa = [(6.30, 1.00), (7.80, 5.30), (5.10, 3.20), (5.80, 1.30)]
aa = sum(w * h for w, h in sa)
am = 2.50 * 2.80 + 1.80 * 1.50
ai = am + a2
assert trunc2(aa) == 71.50 == round(poly_area(A_PART), 2)
assert trunc2(am) == 9.70 == round(poly_area(MARU_A), 2) and trunc2(ai) == 93.94
assert (inset(1.50 + 1.20), inset(2.30 + 2.20), inset(2.00), inset(3.00)) == (2.50, 4.30, 1.80, 2.80)
assert round(a1 + a2 - aa - ai, 2) == 1.54
for w, h in sa:
    check(f'（あ）{w:.2f}×{h:.2f}', f'{w:.2f}×{h:.2f}で{w * h:.2f}')
check('（あ）合計', '合計71.50平方メートルです')
check('Ⓐの内法', '北側は1.50足す1.20の2.70から0.20引いて2.50。東側は2.30足す2.20の4.50から0.20引いて4.30。南側は2.00から0.20引いて1.80')
check('Ⓐ', 'Ⓐ部分は9.70平方メートル')
check('（い）部分等', '1階のⒶ部分9.70と合わせて、93.94平方メートルです')
check('壁の分1.54', '166.98より1.54少ない')
check('問2①（対比）', '問1と同じ建物区分登記です！')
check('問2①', '『区分建物区分登記』ですね')
r_a = Fraction(7150, 7150 + 9394) * Fraction(1, 2)
r_i = Fraction(9394, 7150 + 9394) * Fraction(1, 2)
assert (7150 + 9394) * 2 == 33088 and r_a == Fraction(7150, 33088) == Fraction(325, 1504) and r_i == Fraction(427, 1504)
assert r_a + r_i == Fraction(1, 2) and Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4)
check('問2②（誤答）', '（あ）部分は16544分の7150、（い）部分等は16544分の9394です！')
check('問2②', '（あ）部分は16544分の7150に2分の1をかけて33088分の7150、（い）部分等は33088分の9394')
check('約分', '約分すると1504分の325と1504分の427')
check('問2③', '『敷地権の割合を定めた規約証明書』')
check('問2③ 等しくすると', 'どちらも4分の1ずつ')

# ---- 付属プロンプトとの整合 ----
check('登記の目的', '**登記の目的**：建物区分登記', form, '申請書')
check('添付書類', '建物図面　各階平面図　代理権限証書', form, '申請書')
check('登録免許税', '金2,000円', form, '申請書')
check('申請人', 'Ａ市Ｂ町三丁目５番１号　田宮栄一', form, '申請書')
check('一棟の所在', 'Ａ市Ｂ町三丁目５番地２', form, '申請書')
check('一棟の床面積', '左のセルに「1階　173｜00」、右のセルに「2階　176｜00」', form, '申請書')
check('敷地の地積', '「366｜14」', form, '申請書')
check('区分後の床面積', '「1階　82｜74」「2階　84｜24」', form, '申請書')
check('区分後の家屋番号', '「（イ）」「Ｂ町三丁目」「５番２の１」', form, '申請書')
check('区分後の種類', '①種類：「居宅」', form, '申請書')
c1, c2 = '５番２の１、５番２の２に区分', '５番２から区分'
check('原因1', f'「{c1}」（日付は書かない。', form, '申請書')
check('原因2', f'「{c2}」（日付は書かない）', form, '申請書')
check('敷地権', '「令和３年10月17日敷地権」', form, '申請書')
check('敷地権の割合', '「２分の１」', form, '申請書')
check('正解1', f'「{c1}」', fix, '添削')
check('正解2', f'「{c2}」', fix, '添削')
check('誤答1', f'「令和３年10月17日{c1}」', fix, '添削')
check('誤答2', f'「令和３年10月17日{c2}」', fix, '添削')

# 解説図プロンプトの頂点座標が求積表と一致すること（建物＝Y東・X南、敷地＝Y東・X北）
SITE_I = [(round(2.5 + y, 1), round(17.7 - x, 1)) for y, x in I1_WALL]
SITE_RO = [(10.5, 16.7), (12, 16.7), (12, 17.7), (18.5, 17.7), (18.5, 6.7), (10.5, 6.7)]
assert max(x for _, x in SITE_I) == round(18.70 - 1.00, 2) and min(y for y, _ in SITE_I) == 2.50
assert max(y for y, _ in SITE_RO) < 19.70 and min(x for _, x in SITE_I) > 2.12
assert round(poly_area(SITE_I) + poly_area(SITE_RO), 2) == 173.00
figs = [('図1・図3 一棟1階', WHOLE1, 173.00), ('図4 壁心', I1_WALL, 86.50), ('図4・図5 内法1階', I1, 82.74),
        ('図6 2階', I2, 84.24), ('図7 （あ）部分', A_PART, 71.50), ('図7 Ⓐ部分', MARU_A, 9.70),
        ('図7 （ロ）壁心', RO1_WALL, 86.50), ('図3 （イ）', SITE_I, 86.50), ('図3 （ロ）', SITE_RO, 86.50)]
for label, pts, want in figs:
    assert round(poly_area(pts), 2) == want, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
for s in ['（Y, X）＝（0, 18.70）', '（15.70, 18.70）', '（19.70, 18.70）', '（19.70, 0）', '（2.12, 0）', '（0, 2.12）',
          '「1.00」×1、「2.50」×2', '6.50×1.00＋8.00×10.00＝86.50㎡', '6.30×1.00＋7.80×9.80＝82.74㎡',
          '（イ）部分2階 床面積：84.24㎡', '（あ）部分：71.50㎡', 'Ⓐ部分9.70＋（い）部分84.24＝93.94㎡',
          '19.70×18.70−2.12×2.12÷2＝366.14㎡']:
    check('図の数値', s, fig, '解説図')

# ---- 形状・向き（図面の上＝北。図1の注5と方位記号で確認）----
check('（イ）は西半分', '西半分の（イ）部分')
check('1階の欠けの位置', '北東の角が、横1.50、縦1.00だけ欠けた形です')
check('隅切りの位置', '南西の角だけ、斜めに3.00の隅切りがあります')
check('Ⓐの位置', '（ロ）部分の南東の角にある玄関と階段と収納')
check('Ⓐの欠け', '南西の角が横0.70、縦1.50欠けていて')
assert I1[1][0] < I1[3][0] and I1[2][1] > I1[1][1]  # 欠けは北東（Y大・X小）
assert min(y for y, _ in MARU_A) > 4 and max(x for _, x in MARU_A) == 10.9  # Ⓐは南東
for bad in ['PDF', '創設的登記', '右上', '左下', '右側', '左側', '『1.0』', '『2.5』', '令和3年10月17日区分']:
    absent('誤記・混入', bad)

# ---- note向けの体裁：話者名の行末に半角スペース2つ、名前とセリフの間に空行なし ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
ok = n_marker == 33
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカー（引用形式）: {n_marker}個（解説図30＋添削1＋第1欄の完成形1＋第2欄の完成形1＝計33か所の想定）')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和3年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和3年度問題22（建物）', thumb, '見出し画像')
check('解説図のタイトル', title[2:], fig, '解説図')
check('申請書のタイトル', title[2:], form, '申請書')
check('添削のタイトル', title[2:], fix, '添削')

# ---- 2026-09-29 追加：最新の執筆プロンプト・依頼文に合わせた照合 ----
# 同じ話者のセリフが続いていないか（章の頭で区切る。画像挿入マーカーをはさんでも続きとみなす）
prev = None
for i, line in enumerate(lines):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        ok = line != prev
        ng += (not ok)
        if not ok:
            print('NG 同じ話者の連続 :', i + 1)
        prev = line
# 注の書き分け：問題文の注（1〜4）、図1の（注）（1〜6）、図4の（注）（1〜5）
bare = [m.start() for m in re.finditer(r'注[0-9]|（注）[0-9]', text)
        if not text[:m.start()].endswith(('問題文の', '図1の', '図4の'))]
ok = not bare
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'注の書き分け（「問題文の注N」「図1の（注）N」「図4の（注）N」） : 書き分けていない箇所 {len(bare)}')
for bad in ['✕', '✓', '名変']:
    absent('記号・略語', bad)

# 条文（note-articles/laws の原典で確認したもの）
for s in ['同条第3項で当てはめられる', '登録免許税法別表第一の一（十三）イ', '不動産登記事務取扱手続準則第81条第3項',
          '不動産登記令別表16の項添付情報欄イ', '不動産登記令別表16の項添付情報欄ハ（2）', '不動産登記規則第84条',
          '不動産登記規則第82条第1項、不動産登記事務取扱手続準則第52条第2項', '不動産登記事務取扱手続準則第53条']:
    check('条文', s)
check('建物の存する部分は不要', '（イ）部分は1階から始まるから要らないわ')

# 所在：配置図の距離から建物の位置を出し、5番2の1筆に収まることを確かめる（外壁と壁の中心線の差は無視）
east_wall = 2.50 + 16.00
south_wall = 1.00 + 11.00
assert round(19.70 - east_wall, 2) == 1.20 and round(18.70 - south_wall, 2) == 6.70
assert 2.50 > 0 and south_wall < 18.70 - 2.12   # 隅切り（南の線から北へ2.12まで）にかからない
check('所在の確認', '東の外壁は西側の筆界からおよそ18.5。東隣の5番1との境（19.70）まで、まだ約1.2あります')
check('所在の確認', '南側の道路（116）との境（18.70）まで約6.7')
check('所在', '所在は『A市B町三丁目5番地2』の1筆です')
check('解く順番', '床面積がいらない欄 → 求積と作図 → 問2の②')
check('寸法の累計メモ', '東へ6.50、8.00、南へ1.00、11.00と足した累計でメモ')

# ---- 画像（2026-09-29生成、2026-10-02更新）：記事の画像挿入マーカー12か所と zu/ のPNGの対応 ----
from PIL import Image
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R3_dai22mon_zu01_jikeiretsu', '事実関係の時系列メモ'),
        ('R3_dai22mon_zu02_kubun_bunkatsu', '建物区分登記（1個の建物を壁で切り分けて'),
        ('R3_dai22mon_zu03_shinseinin', '申請人の比較図'),
        ('R3_dai22mon_zu04_shurui', '区分後の種類の比較図'),
        ('R3_dai22mon_zu05_kubun_zentaizou', '縦割りで区分される様子'),
        ('R3_dai22mon_zu06_chuu_shiwake', '注の仕分けの図'),
        ('R3_dai22mon_zu07_shikichi_henchou', '辺長確認図'),
        ('R3_dai22mon_zu08_kaku_kakanai', '建物図面（イ）に書くもの'),
        ('R3_dai22mon_zu09_shozai_kakunin', '建物が本件土地（5番2）の中だけに収まる'),
        ('R3_dai22mon_zu10_tatemono_zumen', '建物図面（イ）の完成形'),
        ('R3_dai22mon_zu11_kensan_wana', '検算の罠の比較図'),
        ('R3_dai22mon_zu12_hiroinaoshi', '辺ごとに壁心から内法へ拾い直す表'),
        ('R3_dai22mon_zu13_ayamari_hikaku', '誤り比較図'),
        ('R3_dai22mon_zu14_1kai_kyuuseki', '（イ）部分1階の床面積求積図'),
        ('R3_dai22mon_zu15_2kai_kyuuseki', '（イ）部分2階の床面積求積図'),
        ('R3_dai22mon_zu16_kakukai_kaku', '各階平面図（イ）に書くもの'),
        ('R3_dai22mon_zu17_kakukai_heimenzu', '原本の罫線から測った寸法で、縮尺1/250の実際の大きさ（1m＝4mm）'),
        ('R3_dai22mon_zu18_shikichiken', '敷地権の割合の図。①区分すると'),
        ('R3_dai22mon_zu19_tenpu', '添付書類の要る・要らない'),
        ('R3_dai22mon_zu20_tourokumenkyozei', '登録免許税の図'),
        ('R3_dai22mon_zu21_ittou_kabe_uchinori', '一棟の建物の表示は壁心のまま転写'),
        ('R3_dai22mon_zu22_kouzou_tatewari', '構造の比較図'),
        ('R3_dai22mon_toukishinseisho_machigai', '①誤答'),
        ('R3_dai22mon_zu23_kubun_hyouji', '区分した建物の表示（イ）の2行の書き方'),
        ('R3_dai22mon_zu24_shikichiken_genin', '敷地権の表示の原因の図'),
        ('R3_dai22mon_toukishinseisho_kansei', '登記申請書（問1）の完成形'),
        ('R3_dai22mon_zu25_kubun_kubun', '問1（普通の建物を区分する'),
        ('R3_dai22mon_zu26_maruA_yukamenseki', 'Ⓐ部分の比較図'),
        ('R3_dai22mon_zu27_maruA_kyuuseki', 'Ⓐ部分の寸法を壁心'),
        ('R3_dai22mon_zu28_toi2_kyuuseki', '問2の求積図'),
        ('R3_dai22mon_zu29_shikichiken_wariai', '敷地権の割合の図。土地全体'),
        ('R3_dai22mon_dai2ran_kansei', '第2欄（問2）の完成形'),
        ('R3_dai22mon_zu30_toku_junban', '本番で解く順番の図')]
ok = len(markers) == len(PNGS)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}')
for (name, key), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        if name.endswith(('kansei', 'machigai')) and 'dai2ran' not in name:
            ok = w == 1200 and h > w          # 申請書・添削は横1200pxの縦長
        elif 'dai2ran' in name:
            ok = w == 1200                    # 第2欄は3行の表だけなので横1200px
        else:
            ok = (w, h) == (1504, 2320) if ('zu10' in name or 'zu17' in name) else w >= 1600 and h >= 800
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'PNG（マーカー順） : {name}')
    src = fig if '_zu' in name else form if ('kansei' in name) else None
    if src is not None:
        ok = f'zu/{name}.png' in src
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'プロンプトにファイル名 : zu/{name}.png')
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _ in PNGS})
ok = not extra
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'zu/ に記事で使わないPNGがない : {extra}')


def html_has(name, *needles, bad=()):
    global ng
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        ok = n in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : {n}')
    for n in bad:
        ok = n not in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html に無い : {n}')


html_has('R3_dai22mon_toukishinseisho_kansei', '建物区分登記', '建物図面　各階平面図　代理権限証書', '金2,000円',
         'Ａ市Ｂ町三丁目５番１号　田宮栄一', '令和３年10月17日　申請　Ｅ地方法務局', 'Ａ市Ｂ町三丁目５番地２',
         '鉄骨造スレー<br>トぶき２階建', '1階　173', '2階　176', 'Ａ市Ｂ町三丁目<br>５番２', '宅地', '366', '>14<',
         '共同住宅', '居宅', '（イ）<br>Ｂ町三丁目<br>５番２の１', '1階　82', '>74<', '2階　84', '>24<',
         '５番２の１、<br>５番２の２に区分', '５番２から区分', '所有権', '２分の１', '令和３年10月17日敷地権', '（略）',
         bad=('規約証明書', '所有権証明書', '86', '令和３年10月17日５番２'))
html_has('R3_dai22mon_dai2ran_kansei', '区分建物区分登記', '33088分の7150', '33088分の9394', '敷地権の割合を定めた規約証明書')
html_has('R3_dai22mon_toukishinseisho_machigai', '令和３年10月17日<br>５番２の１、', '令和３年10月17日<br>５番２から区分',
         '形成的登記', '令和３年10月17日敷地権', 'dstrike', '<svg class="check"')
check('添削：縦に積む', '3コマを縦に積み', fix, '添削')
absent('横1600px', '1600px', fix, '添削')
absent('記号', '✓', fix, '添削')
absent('横1800px', '1800px', form, '申請書')
for bad in ['✕', '✓', '○']:   # 答案用紙に印刷された作成の日付「（令和3年○月○日作成）」の○は記号ではないので除く
    absent('記号（解説図）', bad, fig.replace('（令和3年○月○日作成）', ''), '解説図')
drw = open(os.path.join(ZU, 'draw_R3_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
fits = re.findall(r'\bfit\(ax[^\n]*', drw) + re.findall(r'\bfit\(axes\[[012]\][^\n]*', drw)
ok = fits and all('pad_aspect=True' in f for f in fits)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit はすべて pad_aspect=True（{len(fits)}か所）')
for s in ['== 173.00', '== 86.50', '== 82.74', '== 84.24', '== 71.50', '== 9.70', '== 93.94', '== 366.1428']:
    check('作図スクリプトの面積の assert', s, drw, '作図')
for s in ['zu/R3_dai22mon_zu05_kubun_zentaizou.png', 'zu/R3_dai22mon_zu28_toi2_kyuuseki.png']:
    check('生成済みのファイル名', s, fig, '解説図')
check('生成済みのファイル名', 'zu/R3_dai22mon_dai2ran_kansei.png', form, '申請書')


# ---- 2026-10-02 最新の執筆プロンプトに合わせた追加分：図面の完成形は答案用紙の第3欄の枠の中、各階平面図の完成形、解く順番の図 ----
check('各階平面図の求積方法', '床面積とその求積方法も記録する決まり（不動産登記規則第83条第1項）')
check('各階平面図の符号', '図に付けた符号の『（イ）』も入れるの（同規則第84条）')
check('時間配分', 'いちばん時間を食うのは、（イ）部分の内法の求積と第3欄の作図')
check('先に書ける欄（第1欄）', '- 第1欄：登記の目的、添付書類、登録免許税、申請人、一棟の建物の表示、敷地権の目的である土地の表示、区分前の行、区分後の行の家屋番号・種類・構造・原因、敷地権の表示')
check('先に書ける欄（第2欄）', '- 第2欄：①の登記の目的と、③の添付書類')
check('残る欄', '残るのは、第1欄の床面積と第3欄、それに問2の②だけなんですね')
for s_ in ["'B町三丁目5番2の1'", "'A市B町三丁目5番地2'", "(371.66, 267.6, 3.88, '500')", "(212.67, 267.6, 3.88, '250')",
           "'R3_dai22mon_zu17_kakukai_heimenzu'", "'R3_dai22mon_zu30_toku_junban.png'", '床面積　82.74㎡', '床面積　84.24㎡',
           'round(area_es(I1), 4) == 82.74 and round(area_es(I2), 4) == 84.24']:
    check('作図スクリプト（図10・図17の枠と記入、図30）', s_, drw, '作図')

# ---- 2026-10-02 試験の答案用紙（touan_youshi/）の実物で欄の形を確かめた分 ----
import pymupdf as fitz  # noqa: E402
_pdf = fitz.open(os.path.join(HERE, 'touan_youshi', 'R3_dai22mon_touan_youshi.pdf'))
_p1 = re.sub(r'\s+', '', _pdf[0].get_text())
_p2 = re.sub(r'\s+', '', _pdf[1].get_text())
# 答案用紙の印刷文字（実物のテキスト層）
for s_ in ['登記の目的', '添付書類', '登録免許税', '代理人', '（略）', '令和3年10月17日申請Ｅ地方法務局',
           '区分した建物の表示欄（イ）', '主である建物又は附属建物', '敷地権の割合', '（あ）部分', '（い）部分等']:
    ok_ = s_ in _p1
    ng += (not ok_)
    print(('OK ' if ok_ else 'NG ') + f'[答案用紙1ページ目] 印刷文字 : {s_}')
for s_ in ['各階平面図（イ）', '建物図面（イ）', '家屋番号', '建物の所在', '作成者（略）', '（令和3年○月○日作成）',
           '申請人（略）', '縮尺1250', '縮尺1500']:
    ok_ = s_ in _p2
    ng += (not ok_)
    print(('OK ' if ok_ else 'NG ') + f'[答案用紙2ページ目] 印刷文字 : {s_}')
# 登記申請書の項目の順序（実物）：登記の目的 → 添付書類 → 登録免許税 → 申請人 → 代理人 → 申請日
_ord = [_p1.index(k) for k in ['登記の目的', '添付書類', '登録免許税', '代理人', '令和3年10月17日']]
ok_ = _ord == sorted(_ord)
ng += (not ok_)
print(('OK ' if ok_ else 'NG ') + ' [答案用紙1ページ目] 項目の順序 : 登記の目的→添付書類→登録免許税→代理人→申請日')
# 作図スクリプト（図3・図7）の欄の形が実物どおりか
for s_ in ["'建　物　図　面　（イ）'", "'各　階　平　面　図　（イ）'", "'家屋番号'", "'建物の所在'", "'申 請 人'", "'作 成 者'",
           "'（令和3年○月○日作成）'", "'縮尺'", '答案用紙の右半分・縮尺1/500の実際の大きさ', '答案用紙の左半分・縮尺1/250の実際の大きさ']:
    check('作図スクリプト（第3欄の実物の欄の形）', s_, drw, '作図')
ok_ = drw.count("'（略）'") >= 2
ng += (not ok_)
print(('OK ' if ok_ else 'NG ') + ' [作図] 申請人・作成者の欄は「（略）」（印刷済みなので氏名を書かない）')
# 答案用紙2ページ目の罫線：作図スクリプトの SHEET_LINES が原本と一致するか（2026-10-26。get_drawings の mm 値）
import ast  # noqa: E402
_M = _pdf[1].rotation_matrix
_mm = 25.4 / 72
_pdf_lines = set()
for _d in _pdf[1].get_drawings():
    for _it in _d['items']:
        if _it[0] == 'l':
            _a, _b = _it[1] * _M, _it[2] * _M
            _c = [_a.x * _mm, _a.y * _mm, _b.x * _mm, _b.y * _mm]
            if all(56 <= _c[i_] <= 408 for i_ in (0, 2)) and all(10 <= _c[i_] <= 276 for i_ in (1, 3)):
                _pdf_lines.add(tuple(round(v_, 2) for v_ in _c))
_src = re.search(r'SHEET_LINES = (\[.*?\n\])', drw, re.S).group(1)
_mine = {tuple(r_[:4]) for r_ in ast.literal_eval(_src)}
ok_ = _mine == {tuple(round(v_, 2) for v_ in l_) for l_ in _pdf_lines} or len(_mine ^ _pdf_lines) == 0
ng += (not ok_)
print(('OK ' if ok_ else 'NG ') + f' [答案用紙2ページ目] 作図スクリプトの罫線 {len(_mine)}本が原本のPDFの罫線と一致')
# 枠の寸法（原本から測った値）
for s_ in ['80.58', '382.58', '25.77', '256.77', '231.58']:
    check('作図スクリプト（枠の座標）', s_, drw, '作図')
# 申請書のHTML（実物の欄の名前・順序）
_html = open(os.path.join(ZU, 'R3_dai22mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
_ordh = [_html.index(k) for k in ['登記の目的', '添付書類</span>', '登録免許税', '申請人</span>', '代理人</span>', '令和３年10月17日　申請　Ｅ地方法務局',
                                  '一棟の建物の表示', '敷地権の目的である土地の表示', '区分した建物の表示欄（イ）', '敷地権の表示']]
ok_ = _ordh == sorted(_ordh)
ng += (not ok_)
print(('OK ' if ok_ else 'NG ') + ' [申請書HTML] 欄の順序が答案用紙どおり')
_dai2 = open(os.path.join(ZU, 'R3_dai22mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['登記の目的', '敷地権の割合', '（あ）部分', '（い）部分等', '添付書類']:
    check('第2欄HTMLの印刷文字', s_, _dai2, '第2欄HTML')
check('答案用紙で確かめた（解説図）', '試験の答案用紙（`touan_youshi/R3_dai22mon_touan_youshi.pdf` の2ページ目、第3欄）で確かめた', fig, '解説図')
check('答案用紙で確かめた（申請書）', '試験の答案用紙（`touan_youshi/R3_dai22mon_touan_youshi.pdf` の1ページ目）で確かめた', form, '申請書')
check('記事：第3欄の形', '答案用紙の第3欄は1枚の枠で、左半分が各階平面図（イ）、右半分が建物図面（イ）')
check('記事：申請人の（略）', '申請人の欄は『（略）』と印刷済みだから、氏名は書かなくていいの')
check('記事：作成者の（略）', '作成者の欄は『（略）』、作成の日付も『（令和3年○月○日作成）』と印刷済み')
# 「仮」の文言が残っていないこと
for nm, src_ in [('記事', text), ('解説図', fig), ('申請書', form), ('添削', fix), ('作図', drw),
                 ('申請書スクリプト', open(os.path.join(ZU, 'make_R3_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read())]:
    for w_ in ['仮のもの', '仮の形', 'リポジトリにない', 'リポジトリになく', '令和何年何月何日']:
        absent(f'{nm}に「仮」の記述', w_, src_, nm)
check('図7の点線', '(6.4, 0.1)→(6.4, 1.1)→(7.9, 1.1)', fig, '解説図')
check('図16の求積表', '6.30×1.00＝6.3000／7.80×9.80＝76.4400／計　82.7400／床面積　82.74㎡', fig, '解説図')
check('図9の順番', '⑦問2の②と見直し（71.50・9.70→33088分の7150・9394）', fig, '解説図')

# ---- 6-2：まとめのわな21項目（1項目1わな）と、わな→図の対応表（TRAPS）----
body_ = text.split('今日のまとめよ。わなを1つずつ並べるわ」')[1]
items = [l_[2:] for l_ in body_.split('**藍子**')[0].splitlines() if l_.startswith('- ')]
TRAPS = [
    ('建物分割登記ではない', '建物区分登記です！', 'R3_dai22mon_zu02_kubun_bunkatsu', '区分よ'),
    ('栄太ではなく', '（イ）部分は栄太さんが相続するんだから', 'R3_dai22mon_zu03_shinseinin', '動機にすぎない'),
    ('区分前の共同住宅を写さない', '区分前が共同住宅なので、（イ）部分も共同住宅です', 'R3_dai22mon_zu04_shurui', '使い方を見直す'),
    ('3か所でかぶる', '注を仕分けなさい', 'R3_dai22mon_zu06_chuu_shiwake', '3か所でかぶっている'),
    ('敷地の辺長は作図チェック用', 'この辺長は建物図面には書かない', 'R3_dai22mon_zu07_shikichi_henchou', '作図のチェック用'),
    ('「建物の存する部分」を書かない', '専有部分が1階以外にだけあるなら', 'R3_dai22mon_zu08_kaku_kakanai', '氏名は書かなくていいの'),
    ('見た目ではなく距離で決め', '所在は見た目じゃなく、距離で決めるのよ', 'R3_dai22mon_zu09_shozai_kakunin', '建物が乗っている筆だけ'),
    ('壁心のままの床面積は誤り', '合ってるじゃないですか', 'R3_dai22mon_zu11_kensan_wana', '測り方が切り替わる'),
    ('辺ごとに0.20引き', '欠けを囲む壁も、同じ向きに0.10ずつずれる', 'R3_dai22mon_zu12_hiroinaoshi', '変わらないわ'),
    ('各階平面図には、階の別', '各階平面図の書き方も押さえなさい', 'R3_dai22mon_zu16_kakukai_kaku', '書くのは図と求積よ'),
    ('規約証明書は要らない', '規約証明書もいります', 'R3_dai22mon_zu18_shikichiken', '違う割合にしたい'),
    ('3点', '添付書類は？', 'R3_dai22mon_zu19_tenpu', '添付情報欄イ'),
    ('2個分で2,000円', '今回書くのは（イ）部分だけなので、1,000円です', 'R3_dai22mon_zu20_tourokumenkyozei', '分割・区分・合併は例外'),
    ('専有部分だけ内法で測り直す', '一棟の床面積は内法で測り直さないんですか', 'R3_dai22mon_zu21_ittou_kabe_uchinori', '原因及びその日付の欄は空欄'),
    ('屋根まで書いて', 'マンションの部屋みたいに、屋根の種類を省いて', 'R3_dai22mon_zu22_kouzou_tatewari', '鉄骨造スレートぶき2階建'),
    ('区分の原因には日付を書かない', '令和3年10月17日5番2の1、5番2の2に区分', 'R3_dai22mon_toukishinseisho_machigai', '日付なし'),
    ('「記載不要」は使わない', 'ここは『記載不要』ですか', 'R3_dai22mon_zu24_shikichiken_genin', '覚えました'),
    ('区分建物区分登記', '問1と同じ建物区分登記です', 'R3_dai22mon_zu25_kubun_kubun', '区分建物区分登記'),
    ('共用部分ではなく', '共用部分として床面積から外すんですか', 'R3_dai22mon_zu26_maruA_yukamenseki', '内法よ'),
    ('内法に直して求積し', 'Ⓐ詳細図の寸法は壁の中心からなので', 'R3_dai22mon_zu27_maruA_kyuuseki', '9.70平方メートル'),
    ('土地全体に対する', 'それは（ロ）部分の中での割合でしょう', 'R3_dai22mon_zu29_shikichiken_wariai', 'ちゃんと2分の1に戻ります'),
]
ok = len(items) == len(TRAPS) == len({p_ for _, _, p_, _ in TRAPS}) and all(k in it for (k, _, _, _), it in zip(TRAPS, items))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'まとめのわな{len(items)}項目と、わな→図の対応表{len(TRAPS)}組（図の重複なし・同じ順）')
ok = all(it.count('。') == 0 and it.count('、') <= 3 for it in items)
ng += (not ok)
print(('OK ' if ok else 'NG ') + 'まとめの1項目に1つのわな')
mk_pos = [m_.start() for m_ in re.finditer(r'^> 【画像挿入】.*$', text, re.M)]
order_png = [n_ for n_, _ in PNGS]
for key, phrase, png, word in TRAPS:
    pos = text.find(phrase)
    after = [k_ for k_, p_ in enumerate(mk_pos) if p_ > pos][:3]
    k_png = order_png.index(png)
    ok = pos >= 0 and k_png in after and '\n## ' not in text[pos:mk_pos[k_png]]
    prev = [l_ for l_ in text[:mk_pos[k_png]].splitlines() if l_.strip()][-1]
    ok2 = word in prev
    ng += (not ok) + (not ok2)
    print(('OK ' if ok else 'NG ') + f'わなの会話のあと3つ以内のマーカーに図がある : {phrase[:16]}… → {png}')
    print(('OK ' if ok2 else 'NG ') + f'わなの図のマーカーの直前の段落に決め手の語 : {word[:20]}')

# ---- 6-3：画像の決まり。図番なし・インラインの height なし・「第○欄」の見出しなし・列の幅を原本のPDFから測った比と照合 ----
titles_ = re.findall(r"(?:new_figure|fixed_figure|card_figure|table_figure|suptitle)\(\s*(?:'[^']*',\s*)?'([^']*)'", drw)
bad_ = [x_ for x_ in titles_ if re.match(r'図\d+[：:　 ]', x_)]
ok = not bad_
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図スクリプトのタイトルに図番がない : {bad_}')
mk_ = open(os.path.join(ZU, 'make_R3_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
for nm_ in ['R3_dai22mon_toukishinseisho_kansei', 'R3_dai22mon_dai2ran_kansei', 'R3_dai22mon_toukishinseisho_machigai']:
    h_ = open(os.path.join(ZU, nm_ + '.html'), encoding='utf-8').read()
    ok = 'style="height:' not in h_ and 'style="min-height' not in h_ or True
    ok = 'style="height:' not in h_
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{nm_}.html にインラインの height がない')
    ok = '第1欄' not in h_ and (nm_ == 'R3_dai22mon_dai2ran_kansei' or '第2欄' not in h_)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{nm_}.html に「第○欄」の見出しがない（解答欄の第2欄だけ印刷どおり）')
ok = 'style="height:' not in mk_ and 'min-height' in mk_
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書の作成スクリプトに inline の height がなく min-height のクラスがある')
# 表の列の幅（mm）を原本の1ページ目の縦罫線から測り、作成スクリプトの cols(...) と0.15mm以内で一致するか
_p0 = _pdf[0]
_M0 = _p0.rotation_matrix
_vx = []
for _d in _p0.get_drawings():
    for _it in _d['items']:
        if _it[0] == 'l':
            _a, _b = _it[1] * _M0, _it[2] * _M0
            if abs(_a.x - _b.x) < 0.3 * 72 / 25.4:
                _vx.append((_a.x * _mm, min(_a.y, _b.y) * _mm, max(_a.y, _b.y) * _mm))


def widths_in_band(y0_, y1_, x0_, x1_):
    xs_ = sorted({round(x_, 1) for x_, ya_, yb_ in _vx if ya_ <= y0_ + 0.5 and yb_ >= y1_ - 0.5 and x0_ - 0.2 <= x_ <= x1_ + 0.2})
    return [round(b_ - a_, 1) for a_, b_ in zip(xs_, xs_[1:])]


_cols = [[float(v_) for v_ in c_.split(',')] for c_ in re.findall(r'cols\(([0-9., ]+)\)', mk_)]
for label_, band_ in [('土地の表示（左）', (224, 250, 62.5, 228.8)), ('区分した建物の表示（右）', (55, 77, 237, 403.2)),
                      ('敷地権の表示（右）', (128, 150, 237, 403.2)), ('第2欄の①（右）', (188, 209, 237, 403.2))]:
    got_ = widths_in_band(*band_)
    if label_.startswith('土地'):
        got_ = [w_ for w_ in got_]
    ok = any(len(c_) == len(got_) and all(abs(a_ - b_) <= 0.15 for a_, b_ in zip(c_, got_)) for c_ in _cols)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'表の列の幅（原本から測った mm）{label_} {got_}')

# ---- 本文の「a×b＝c」を全部再計算（2026-10-26）----
_cnt = bad_ = 0
for m_ in re.finditer(r'(?<![\d.])(\d+(?:\.\d+)?) ?[×÷] ?(\d+(?:\.\d+)?)(?: ?[×÷] ?(\d+(?:\.\d+)?))? ?＝ ?(\d+(?:\.\d+)?)', text):
    seg_ = m_.group(0)
    pre_, post_ = text[max(0, m_.start() - 2):m_.start()], text[m_.end():m_.end() + 2]
    if re.search(r'[＋−]\s*$', pre_) or re.match(r'\s*[＋−]', post_) or re.match(r'[.\d]', post_):
        continue   # 合計式（a×b＋c×d＝e）の一部は、ここでは割り算・掛け算だけの式だけを見る
    nums_ = [float(g_) for g_ in m_.groups() if g_ is not None]
    ops_ = re.findall(r'[×÷]', seg_)
    val_ = nums_[0]
    for op_, n2_ in zip(ops_, nums_[1:-1]):
        val_ = val_ * n2_ if op_ == '×' else val_ / n2_
    _cnt += 1
    if abs(val_ - nums_[-1]) > 0.006:
        bad_ += 1
        print('   計算が合わない:', seg_, val_)
ng += bool(bad_)
print(('OK ' if not bad_ else 'NG ') + f'本文の「a×b＝c」{_cnt}か所を再計算')

print('NG件数:', ng)
