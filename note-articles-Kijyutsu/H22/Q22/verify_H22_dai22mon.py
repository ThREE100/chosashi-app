"""平成22年度 第22問（建物）：記事の数値・計算・付属プロンプト・生成画像・体裁の照合スクリプト。
アガルートの解答例（第22問 解答例：問1の登記の目的・添付書類・代位原因、問2(1)の登記申請書、問2(2)の各階平面図・建物図面）と
一致することを確認済み。アガルートの過去問集は日付（工事完了・申請・登記記録の受付）と答案用紙の欄の名前（添付情報→添付書類、
表の見出し）を書き換えた改題版なので、下の ANSWER は本試験の日付に戻した形で持ち、改題で変わった欄は照合から外している（作業の中だけ）。
実行: python3 note-articles-Kijyutsu/H22/Q22/verify_H22_dai22mon.py"""
import cmath
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, area, to_dms

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_H22_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_H22_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_H22_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_H22_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_H22_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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
    """床面積の端数処理：1平方メートルの100分の1未満を切り捨て（不動産登記規則第115条）。"""
    return math.floor(v * 100 + 1e-9) / 100


# ---- 敷地：調査結果1の表1（X＝北、Y＝東）。傾いた長方形 ----
A, B, C, D, E, F, G = (P(186.65, 163.48), P(180.65, 153.09), P(171.65, 137.50), P(167.32, 140.00),
                       P(150.00, 150.00), P(159.00, 165.59), P(165.00, 175.98))
lot21, lot22 = [C, B, F, E, D], [B, A, G, F]
fe, ce = F - E, C - E
assert (round(abs(fe), 4), round(abs(ce), 4)) == (18.0013, 24.9994)
assert to_dms(cmath.phase(fe)) == '60°00′08.84″' and to_dms(cmath.phase(ce)).startswith('−30°00′')
cj = fe.conjugate() * ce
assert (round(cj.real, 3), round(cj.imag, 4)) == (-0.025, -450.0235)
for a_, b_, want in [(C, B, 18.00), (B, A, 12.00), (A, G, 25.00), (G, F, 12.00), (F, E, 18.00), (E, D, 20.00),
                     (D, C, 5.00), (B, F, 25.00)]:
    assert round(abs(b_ - a_), 2) == want
assert (round(area(lot21), 2), round(area(lot22), 2)) == (450.02, 299.94)
check('F−E の表示', 'F − E は 9 ＋ 15.59i。[Abs] で18.0013…、[arg] で約60度')
check('C−E の表示', 'C − E は 21.65 − 12.5i で、[Abs] で24.9994…')
check('直角の確認', '表示は −0.025 − 450.0235i。実部がほぼ0だから直角')
check('長方形', '21番は、座標の軸に対して傾いた18.00×25.00の長方形。22番も同じ向きの12.00×25.00の長方形')
check('C・D・E一直線', 'C・D・Eは一直線（DCが5.00、EDが20.00）')
check('面積と登記記録', '21番が450.02、22番が299.94平方メートル。登記記録の449.00・301.00')
check('辺長は建物図面に書かない', '辺長も作図のチェック用で、建物図面には書かないの')
check('方位の言い方', '図面の上が北北西、右が東北東、下の道路の側が南南東、左の12番・13番の側が西南西')

# ---- 建物（柱の中心線。(x, s)：原点＝1階の西南西の辺と北北西の辺の交点） ----
B21 = [(1.80, 0), (9.90, 0), (9.90, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
EXT = [(9.90, 0), (14.90, 0), (14.90, 9.00), (9.90, 9.00)]
B22 = [(14.90, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40), (21.65, 9.00), (14.90, 9.00)]
F1 = [(1.80, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40), (21.65, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
F1_WRONG = [(1.80, 0), (23.00, 0), (23.00, 3.60), (21.65, 3.60), (21.65, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
F2 = [(1.80, 0), (9.00, 0), (9.00, 7.20), (1.80, 7.20)]
a21, aext, a22 = round(poly_area(B21), 4), round(poly_area(EXT), 4), round(poly_area(B22), 4)
a1, a2, aw = round(poly_area(F1), 4), round(poly_area(F2), 4), round(poly_area(F1_WRONG), 4)
assert (a21, aext, a22, a1, a2, aw) == (81.00, 45.00, 68.04, 194.04, 51.84, 191.61)
assert round(a21 + aext + a22, 2) == a1 and trunc2(a1) == 194.04 and trunc2(a2) == 51.84
assert round(1.80 * 4.50 + 19.85 * 9.00 + 1.35 * 5.40, 4) == 194.04
assert round(9.90 * 4.50 + 8.10 * 4.50, 2) == 81.00 and round(6.75 * 9.00 + 1.35 * 5.40, 2) == 68.04
assert round(21.20 + 1.80, 2) == round(21.65 + 1.35, 2) == 23.00 and round(4.50 + 4.50, 2) == round(5.40 + 3.60, 2) == 9.00
check('誤答（全体から引く、5.40）', '22番の欠け1.35×5.40 ＝ 7.29を引いて、191.61平方メートル！')
check('欠けの奥行き', '欠けている側の辺の長さだから……3.60！5.40は欠けていないほうの辺でした')
check('全体から引く正しい値', '207.00 − 8.10 − 4.86 ＝ 194.04です')
check('1階 求積表', '- 1.80 × 4.50 ＝ 8.1000\n- 19.85 × 9.00 ＝ 178.6500\n- 1.35 × 5.40 ＝ 7.2900\n- 合計：194.0400 （床面積：194.04平方メートル）')
check('合体前後の検算', '81.00 ＋ 45.00 ＋ 68.04 ＝ 194.04。ぴったりです')
check('元の21番', '道路側の9.90×4.50 ＝ 44.55と、北北西側の8.10×4.50 ＝ 36.45で81.00')
check('元の22番', '6.75×9.00 ＝ 60.75と1.35×5.40 ＝ 7.29で68.04')
check('2階 求積表', '- 7.20 × 7.20 ＝ 51.8400\n- 合計：51.8400 （床面積：51.84平方メートル）')
check('2階の位置', '東北東へは元の21番の壁より0.90、道路の側へは1.80短いです')
assert round(9.90 - 9.00, 2) == 0.90 and round(9.00 - 7.20, 2) == 1.80
check('中心線のまま', '測定値は柱の中心線からなので、そのまま壁の中心線の長さです')
check('形が閉じる検算', '北北西の21.20と西南西の段1.80を足すと23.00、道路側の21.65と東北東の段1.35を足しても23.00')
check('各階平面図の省略', '各階平面図は求積とその方法、床面積の表示を省略してよい')
check('1階の点線', '1階の形を点線で重ねて位置を示すのよ（不動産登記規則第83条第1項）')

# ---- 建物図面の位置・所在 ----
U0 = 4.40 + 0.10                                  # 西南西の柱の中心線（境から）
assert round(30.00 - (4.40 + 0.10 + 21.65 + 0.10), 2) == 3.75
check('東北東の食い違い', '4.40 ＋ 0.10 ＋ 21.65 ＋ 0.10 ＝ 26.25。21番と22番の幅を足すと18.00 ＋ 12.00 ＝ 30.00だから、東北東の境までは3.75。3.85と0.10合わない！')
line = 18.00 - U0
on21 = round(a21 + (line - 9.90) * 9.00, 2)
assert (round(U0 + 9.90, 2), round(U0 + 14.90, 2), on21, round(a1 - on21, 2)) == (14.40, 19.40, 113.40, 80.64)
check('境の位置', '西南西の端が4.50、元の21番の東北東の壁が14.40、増築部分の東北東の端が19.40')
check('所在の計算', '21番の上は81.00 ＋ 3.60×9.00 ＝ 113.40、22番の上は1.40×9.00 ＋ 68.04 ＝ 80.64')
check('所在', '所在は『21番地、22番地』です')
check('所在の根拠', '不動産登記事務取扱手続準則第88条第2項')
check('建物図面の申請人欄', '申請人の欄は（略）と印刷されていないから、『大面太郎　大面健一郎』と書くの')
check('図面の記名の根拠', '不動産登記規則第74条第2項')

# ---- 問1 ----
check('問1 誤答（増築だけ）', '健一郎さんは22番の建物表題部変更登記（増築）をすればいい')
check('区分建物の根拠', '建物の区分所有等に関する法律第1条')
check('一括申請', '一括して申請しなければならない（不動産登記法第52条第3項）')
check('問1(1) 登記の目的', '登記の目的は『建物表題部変更登記』')
check('問1(1) 添付情報の根拠', '不動産登記令別表14の項')
check('問1(1) 添付情報', '建物図面、各階平面図、所有権証明情報、代理権限証明情報の4つです')
check('問1(2) 誤答', '『民法第423条』！')
check('問1(2) 代位原因', '代位原因は『不動産登記法第52条第4項』')

# ---- 問2(1) 申請書 ----
check('合体の根拠', '『合体による登記等』よ（不動産登記法第49条第1項）')
check('登記の目的の誤答', '『合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消』です！')
check('第4号・後段', '（不動産登記法第49条第1項第4号）')
check('一の申請情報', '不動産登記令第5条第1項')
check('登記の目的', '『合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消並びに所有権の保存の登記』です！')
check('（あ）（い）は付けない', '今年の太郎さんと健一郎さんは、最初から別の人よ')
check('申請人', '『A市D町一丁目2番1号　持分10分の4　大面太郎』と『A市D町一丁目2番2号　10分の6　大面健一郎』')
check('構造の誤答', '構造は木造スレートぶき2階建……')
check('瓦葺の転写', '登記記録どおり『木造瓦葺2階建』。2行目の22番は『木造セメント瓦葺平家建』')
check('合体後の家屋番号', '家屋番号は空欄（不動産登記令第3条第8号ロ）')
check('建物の表示の原因', '1行目が『平成22年7月30日22番と合体』、2行目が『平成22年7月30日21番と合体』、3行目が『平成22年7月30日21番、22番を合体』です')
check('欄番号を付けない', '不動産登記事務取扱手続準則第94条第2項')
check('所有権登記の表示', '21番、順位番号1番、昭和51年2月17日第1110号、大面太郎。22番の行は書きません')
check('存続登記の誤答', '1番のA銀行の抵当権、2番のB信用金庫の抵当権、3番の永野さんの賃借権を全部書きます！')
check('消滅の承諾', '（不動産登記法第50条、不動産登記規則第120条第5項）')
check('賃借権は存続登記に入らない', '賃借権は入っていません')
check('存続登記', '21番、乙区2番、抵当権設定、昭和51年2月17日第1113号、B信用金庫。目的とする権利は『大面太郎持分』')
check('移記の根拠', '不動産登記規則第120条第4項')
check('住所証明情報の根拠', '同項添付情報欄リ')
check('登記識別情報', '不動産登記令第8条第1項第2号')
check('登記済証', '不動産登記法附則第7条')
check('印鑑証明書（太郎）', '不動産登記規則第47条第3号イ（6）')
check('印鑑証明書（健一郎は不要）', '同規則第48条第1項第4号・第49条第2項第4号')
check('承諾証明情報', '不動産登記令別表13の項添付情報欄ト')
check('添付情報', '建物図面、各階平面図、所有権証明情報、住所証明情報、登記済証、印鑑証明書、承諾証明情報、抵当権消滅承諾証明情報、代理権限証明情報の9つです')
v21, v22, vext = 1200, 530, 45 * 6
total = v21 + v22 + vext
kazei = total * 6 // 10
assert (vext, total, kazei, kazei * 10000 * 4 // 1000) == (270, 2000, 1200, 48000)
wrong_kazei = (v21 + v22 + 370) * 6 // 10
assert (wrong_kazei, wrong_kazei * 10000 * 4 // 1000) == (1260, 50400)
check('課税価格の誤答', '課税価格は1,260万円。登録免許税は1000分の4で5万400円です！')
check('課税標準の根拠', '登記のときの建物の価額（登録免許税法第10条第1項）')
check('合体後の価額', '1,200万円 ＋ 530万円 ＋ 270万円 ＝ 2,000万円')
check('持分', '2,000万円×10分の6 ＝ 1,200万円（登録免許税法第10条第2項）')
check('税率', '同法別表第一の一（一）')
check('登録免許税', '課税価格は金1,200万円、登録免許税は金4万8,000円です')
check('太郎さんの分は非課税', '登記官がそのまま移す分（不動産登記規則第120条第2項）')
check('申請の期限', '合体の日の7月30日から1月以内の申請だから')

# ---- 予備校の解答例との照合（本試験の日付に戻した値。問1・問2(1)・問2(2)） ----
ANSWER = {
    '問1 登記の目的': '建物表題部変更登記',
    '問1 代位原因': '不動産登記法第52条第4項',
    '問2 登記の目的': '合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消並びに所有権の保存の登記',
    '問2 申請人1': '持分10分の4　大面太郎',
    '問2 申請人2': '10分の6　大面健一郎',
    '21番の床面積': '1階81.00・2階51.84',
    '22番の床面積': '68.04',
    '合体後の床面積': '1階194.04・2階51.84',
    '21番の原因': '平成22年7月30日22番と合体',
    '22番の原因': '平成22年7月30日21番と合体',
    '合体後の原因': '平成22年7月30日21番、22番を合体',
    '合体後の構造': '木造スレートぶき2階建',
    '所有権登記の受付': '昭和51年2月17日第1110号',
    '存続登記の受付': '昭和51年2月17日第1113号',
    '目的とする権利': '大面太郎持分',
    '課税価格': '金1,200万円',
    '登録免許税': '金4万8,000円',
    '建物の所在': '21番地、22番地',
    '各階平面図 1階': '1階21.20・5.40・1.35・3.60・21.65・4.50・1.80・4.50',
    '建物図面の距離': '4.40・4.40・12.00',
}
for k, v in ANSWER.items():
    check('解答例 ' + k, v)
for item in ['建物図面', '各階平面図', '所有権証明情報', '住所証明情報', '登記済証', '印鑑証明書', '承諾証明情報',
             '抵当権消滅承諾証明情報', '代理権限証明情報']:
    check('解答例の添付書類（情報で書く）', item)
# 改題で変わった要素（平成30年の日付・添付書類の欄名）は記事に使わない
for bad in ['平成30年9月', '平成30年10月', '昭和55年', '添付書類', '所有権登記特定事項', '存続登記特定事項', '改題']:
    absent('改題の要素', bad)

# ---- 付属プロンプト（登記申請書・添削） ----
for s_ in ['**建物表題部変更登記**', '**建物図面　各階平面図　所有権証明情報　代理権限証明情報**', '**不動産登記法第52条第4項**',
           '合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消並びに所有権の保存の登記',
           '建物図面　各階平面図　所有権証明情報　住所証明情報　登記済証　印鑑証明書　承諾証明情報　抵当権消滅承諾証明情報　代理権限証明情報',
           '平成22年８月22日　申請　Ａ地方法務局', 'Ａ市Ｄ町一丁目２番１号　持分　10分の４　大面太郎',
           'Ａ市Ｄ町一丁目２番２号　　　　　10分の６　大面健一郎', '構造「木造瓦葺２階建」', '構造「木造セメント瓦葺平家建」',
           '構造「木造スレートぶき２階建」', '「1階　81｜00」「2階　51｜84」', '床面積「68｜04」', '「1階　194｜04」「2階　51｜84」',
           '平成22年７月30日22番と合体', '平成22年７月30日21番と合体', '平成22年７月30日21番、22番を合体',
           '「昭和51年２月17日第1110号」', '「昭和51年２月17日第1113号」', '目的とする権利「大面太郎持分」',
           '課税価格：金1,200万円', '登録免許税：金４万8,000円', '二　抵当権等の登記で合体後の登記建物につき存続すべきものの表示']:
    check('申請書の記入', s_, form, '申請書')
for s_ in ['**「金1,260万円」**', '**「金５万400円」**', '「金1,200万円」「金４万8,000円」', '45.00㎡×６万円＝270万円']:
    check('添削の記入', s_, fix, '添削')

# ---- 解説図プロンプトの頂点座標（面積を計算して求積表と一致させる） ----
for label, pts, want in [('1階（合体後）', F1, 194.04), ('元の21番', B21, 81.00), ('増築部分', EXT, 45.00),
                         ('元の22番', B22, 68.04), ('2階', F2, 51.84), ('図4左 誤り', F1_WRONG, 191.61)]:
    assert round(poly_area(pts), 4) == want, label
    fm = lambda v: '0' if v == 0 else f'{v:.2f}'
    s = ' → '.join(f'({fm(x)}, {fm(y)})' for x, y in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
for s_ in ['「4.40」を2か所', '「12.00」', '「18.00m」', '「12.00m」', '「25.00m」', '「20.00m」', '「5.00m」',
           '1階 床面積：194.04㎡', '2階 床面積：51.84㎡', '207.00－8.10－7.29＝191.61㎡', '1,200万円', '4万8,000円',
           '21番450.02㎡・22番299.94㎡', '113.40㎡', '80.64㎡', '（22番の古い建物図面の3.85）は書かない',
           'E（0, 0）、F（18.00, 0）、G（30.00, 0）、C（0, 25.00）、D（0, 20.00）、B（18.00, 25.00）、A（30.00, 25.00）']:
    check('図の数値', s_, fig, '解説図')

# ---- 形状・向き ----
check('21番の欠けの位置', '西北西の角に元の21番の欠け（1.80×4.50）、東南東の角に元の22番の欠け（1.35×3.60）がある', fig, '解説図')
check('22番の欠けの位置', '欠けは……道路の側、東南東の角です')
for bad in ['PDF', '創設的登記', '名変', '✕', '✓', '右上の', '左下', '右側', '左側', '（あ）持分', '5万400円が正', '木造かわらぶき']:
    absent('誤記・混入', bad)

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
markers = re.findall(r'^> 【画像挿入】(.*)$', text, re.M)
ZU = os.path.join(HERE, 'zu')
PAIRS = [('問1の考え方の流れ図', 'H22_dai22mon_zu01_toi1_nagare.png'),
         ('問1（障壁を残す', 'H22_dai22mon_zu02_toi1_toi2.png'),
         ('問1の添付情報の図', 'H22_dai22mon_zu03_toi1_tenpu.png'),
         ('問1(2)「代位原因」欄の①誤答', 'H22_dai22mon_toi1_machigai.png'),
         ('問1の完成形', 'H22_dai22mon_toi1_kansei.png'),
         ('答案用紙の方位記号と同じ向き', 'H22_dai22mon_zu04_shikichi_henchou.png'),
         ('東北東の境までの距離の検算図', 'H22_dai22mon_zu05_touhokutou_kenzan.png'),
         ('所在の確認図', 'H22_dai22mon_zu06_shozai_kakunin.png'),
         ('建物図面の完成形', 'H22_dai22mon_zu07_tatemono_zumen.png'),
         ('1階の誤り比較図', 'H22_dai22mon_zu08_1kai_ayamari_hikaku.png'),
         ('1階の床面積求積図', 'H22_dai22mon_zu09_1kai_kyuuseki.png'),
         ('合体前の2つと増築部分の検算図', 'H22_dai22mon_zu10_gattaizen_kenzan.png'),
         ('2階の床面積求積図', 'H22_dai22mon_zu11_2kai_kyuuseki.png'),
         ('各階平面図の完成形', 'H22_dai22mon_zu12_kakai_heimenzu.png'),
         ('合体後の甲区（所有権の登記）の行き先の図', 'H22_dai22mon_zu13_kouku_yukisaki.png'),
         ('「登記の目的」欄の①誤答', 'H22_dai22mon_toukishinseisho_machigai_mokuteki.png'),
         ('「申請人」欄の①誤答', 'H22_dai22mon_toukishinseisho_machigai_shinseinin.png'),
         ('「建物の表示」の合体前の2行の構造の①誤答', 'H22_dai22mon_toukishinseisho_machigai_kouzou.png'),
         ('原因及びその日付の図', 'H22_dai22mon_zu14_genin_ranbangou.png'),
         ('A銀行の抵当権の図', 'H22_dai22mon_zu15_a_ginkou_shoumetsu.png'),
         ('存続登記に当たるかの図', 'H22_dai22mon_zu16_sonzoku_hani.png'),
         ('「二　抵当権等の登記で', 'H22_dai22mon_toukishinseisho_machigai_sonzoku.png'),
         ('印鑑証明書の要否の図', 'H22_dai22mon_zu17_inkan_shoumei.png'),
         ('添付情報9つと根拠の表', 'H22_dai22mon_zu18_tenpu_jouhou.png'),
         ('課税価格と登録免許税の組み立て図', 'H22_dai22mon_zu19_touroku_menkyozei.png'),
         ('3コマ添削画像', 'H22_dai22mon_toukishinseisho_machigai.png'),
         ('登記申請書（問2(1)）の完成形', 'H22_dai22mon_toukishinseisho_kansei.png'),
         ('本番で解く順番', 'H22_dai22mon_zu20_toku_junban.png')]
ok = len(markers) == len(PAIRS) == 28
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカー（引用形式）: {len(markers)}個（想定28）')
from PIL import Image
pngs = sorted(f for f in os.listdir(ZU) if f.endswith('.png'))
ok = sorted(f for _, f in PAIRS) == pngs
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'zu/ のPNG {len(pngs)}枚とマーカーの対応先が一致')
for m, (key, f) in zip(markers, PAIRS):
    w, h = Image.open(os.path.join(ZU, f)).size
    ok = key in m and (h > w if 'toukishinseisho' in f else True)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'マーカー→{f}（{w}×{h}px） : {m[:30]}…')
prev, dup = None, []
for i, l in enumerate(lines):
    t = l.rstrip()
    if t in ('**トリ先生**', '**藍子**'):
        if t == prev:
            dup.append(i + 1)
        prev = t
    elif l.startswith('## '):
        prev = None
ng += bool(dup)
print(('OK ' if not dup else 'NG ') + f'同じ話者の連続: {dup}')
bare = [m.start() for m in re.finditer(r'(?<!問題文の)(?<!（)注\d', text)]
ng += bool(bare)
print(('OK ' if not bare else 'NG ') + f'書き分けのない「注N」: {len(bare)}か所')
check('注の書き分け（見取図）', '〔見取図〕の（注）1・2で')
check('注の書き分け（縮尺）', '縮尺500分の1（問題文の注2）は答案用紙に印刷済み')
check('方位記号は印刷済み', '敷地をその方位記号の向きに合わせて描くの')
check('作成者の欄は印刷済み', '作成者の欄は、波臼さんの住所・氏名と『平成22年8月10日作成』まで印刷済みです')
check('時間配分（いちばん時間を食うもの）', 'いちばん時間を食うのは（その3）の作図よ')
check('時間配分（計算は軽い）', '今年の計算は長方形の掛け算と足し算だけで、課税価格も暗算で出る')
check('解く順番（問を先に）', 'まず問を先に読んで、問1と問2の前提の違い')
check('時系列メモ', '昭和51年2月17日に21番の所有権保存とA銀行・B信用金庫の抵当権、平成7年6月14日に永野さんの賃借権、平成22年7月30日に工事完了（合体の日）、8月10日に図面の作成、8月22日に申請')

# ---- 生成画像のHTML（記入内容） ----
H = {n: open(os.path.join(ZU, n + '.html'), encoding='utf-8').read() for n in
     ['H22_dai22mon_toi1_kansei', 'H22_dai22mon_toi1_machigai', 'H22_dai22mon_toukishinseisho_kansei',
      'H22_dai22mon_toukishinseisho_machigai', 'H22_dai22mon_toukishinseisho_machigai_mokuteki',
      'H22_dai22mon_toukishinseisho_machigai_shinseinin',
      'H22_dai22mon_toukishinseisho_machigai_kouzou', 'H22_dai22mon_toukishinseisho_machigai_sonzoku']}
for s_ in ['建物表題部変更登記', '建物図面　各階平面図　所有権証明情報　代理権限証明情報', '不動産登記法第52条第4項', '添　付　情　報']:
    check('問1HTML', s_, H['H22_dai22mon_toi1_kansei'], '問1HTML')
k = H['H22_dai22mon_toukishinseisho_kansei']
for s_ in ['合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消並びに所有権の保存の登記', '抵当権消滅承諾証明情報',
           '登記済証　印鑑証明書　承諾証明情報', '持分　10分の４　大面太郎', '10分の６　大面健一郎', '平成22年８月22日　　申請　　Ａ地方法務局',
           '木造瓦葺<br>２階建', '木造セメント<br>瓦葺平家建', '木造スレート<br>ぶき２階建', '1階　194', '>04</span>', '21番地<br>22番地',
           '平成22年７月30日21番、<br>22番を合体', '昭和51年２月17日第1110号', '第1113号', '大面太郎<br>持分', '目的とする権利',
           '金1,200万円', '金４万8,000円', '０＊＊－＊＊＊＊－１２３４', '合体後の登記建物につき存続すべきもの']:
    check('完成形HTML', s_, k, '申請書HTML')
for bad in ['添付書類', '（略）', 'Ａ銀行', '永野', '（あ）', '1,260']:
    absent('完成形HTML', bad, k, '申請書HTML')
assert k.index('平成22年８月22日') < k.index('申　　請　　人') < k.index('代　　理　　人')   # 答案用紙どおりの順序
m_ = H['H22_dai22mon_toukishinseisho_machigai']
for s_ in ['金1,260万円', '金５万400円', '金1,200万円', '金４万8,000円', '①誤答', '②添削', '③正解', '270万円']:
    check('添削HTML', s_, m_, '添削HTML')
# 本文の誤答ごとの添削（2026-10-05追加。標準セットで足りるかを本文から見直した）
for n_, ss in [('H22_dai22mon_toi1_machigai', ['民法第423条', '不動産登記法第52条第4項', '①誤答', '②添削', '③正解']),
               ('H22_dai22mon_toukishinseisho_machigai_mokuteki', ['並びに所有権の保存の登記', '①誤答', '②添削', '③正解']),
               ('H22_dai22mon_toukishinseisho_machigai_shinseinin', ['（あ）', '（い）', '10分の４', '①誤答', '②添削', '③正解']),
               ('H22_dai22mon_toukishinseisho_machigai_kouzou', ['木造瓦葺', '木造セメント', 'スレート', '①誤答', '②添削', '③正解']),
               ('H22_dai22mon_toukishinseisho_machigai_sonzoku', ['第1112号', '第1113号', '第5567号', '①誤答', '②添削', '③正解'])]:
    for s_ in ss:
        check('添削HTML', s_, H[n_], n_)
draw = open(os.path.join(ZU, 'draw_H22_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
n_fit = len(re.findall(r'\bfit\(ax', draw))
n_pad = draw.count('pad_aspect=True')
ok = n_fit == n_pad and n_fit > 0
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit {n_fit}か所がすべて pad_aspect=True（{n_pad}）')
# 図面の完成形は答案用紙（その3）の1枚の枠（左半分が各階平面図、右半分が建物図面）に実際の大きさで描く（2026-10-26。H25/Q22の見本）
for s_ in ["'家屋番号'", "'建物の所在'", "SHOZAI = 'A市D町一丁目21番地、22番地'", "SHINSEININ = '大面太郎　大面健一郎'",
           "'申　請　人'", "'作　成　者'", "'250'", "'500'", "'（平成22年8月10日作成）'", "'職印'", "'土地家屋調査士　波臼良子'",
           "'建　　物　　図　　面'", "'各　階　平　面　図'", "'（単位：m）'", "1m ＝ 2mm", "1m ＝ 4mm",
           "（答案用紙（その3）の建物図面の側・縮尺1/500の実際の大きさ）", "（答案用紙（その3）の各階平面図の側・縮尺1/250の実際の大きさ）"]:
    check('図面の欄の枠', s_, draw, '作図')
for key in ['答案用紙（その3）の1枚の枠の建物図面の側', '答案用紙（その3）の1枚の枠の各階平面図の側']:
    check('マーカーに欄の枠', key)
for s_ in ['答案用紙（その3）の1枚の枠', '縮尺1/500の実際の大きさ', '縮尺1/250の実際の大きさ', 'public/kijutsu/H22-tatemono/a3.webp']:
    check('図のプロンプトに欄の枠', s_, fig, '解説図')
# fit は文字より先（2026-09-30、H21/Q22）：各関数の中で fit が最初の文字の配置より前にあるか
for fn in re.findall(r'def (zu\d\d)\(\):(.*?)(?=\ndef |\nif __name__)', draw, re.S):
    body = fn[1]
    if 'box_fig' in body or 'sheet_figure' in body:   # 枠と文字だけの図（目視）と、軸の範囲を mm で決める答案用紙の図
        continue
    i_fit = body.find('fit(')
    i_txt = min([body.find(k) for k in ['free_text(', 'edge_label(', 'callout(', 'dims(', 'dist_arrow('] if body.find(k) >= 0] or [10**9])
    ok = 0 <= i_fit < i_txt
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[作図] {fn[0]}：fit が文字の配置より先')
for s_ in ['(B21, 81.00)', '(F1, 194.04)', '(F1_WRONG, 191.61)', '(F2, 51.84)', '113.40, 80.64', '== 450.02']:
    check('作図スクリプトの検算', s_, draw, '作図')
for f in ['prompt_H22_dai22mon_kaisetsuzu.md', 'prompt_H22_dai22mon_toukishinseisho_gazou.md',
          'prompt_H22_dai22mon_toukishinseisho_machigai.md']:
    src = open(os.path.join(HERE, f), encoding='utf-8').read()
    absent('記号', '✕', src, f)
    absent('記号', '✓', src, f)
for f_ in [f for _, f in PAIRS if '_zu' in f]:
    check('生成済みのファイル名', 'zu/' + f_, fig, '解説図')
for f_ in [f for _, f in PAIRS if 'machigai' in f]:
    check('生成済みのファイル名', 'zu/' + f_, fix, '添削')
check('生成済みのファイル名', 'zu/H22_dai22mon_toukishinseisho_kansei.png', form, '申請書')
# ---- 2026-10-26 照らし直しで足した検査（qa-checklist-kijutsu.md の6-2・6-3） ----
# まとめのわな→図の対応表：(まとめの項目の決め手の語, 誤答・迷いの会話の語, 図のPNG, 図のマーカーの直前の行にある決め手の語)
TRAPS = [
    ('22番の増築だけではなく', '21番の太郎さんは何も工事をしていないから、登記はいりません！', 'H22_dai22mon_zu01_toi1_nagare',
     '22番だけ変更して、21番を放っておくことはできないわ'),
    ('住所証明情報・登記識別情報は要らない', '住所証明情報と登記識別情報も要りますか？', 'H22_dai22mon_zu03_toi1_tenpu',
     '建物図面、各階平面図、所有権証明情報、代理権限証明情報の4つです'),
    ('民法第423条ではなく', '『民法第423条』！', 'H22_dai22mon_toi1_machigai', '代位原因は『不動産登記法第52条第4項』'),
    ('軸に対して傾いた長方形', 'どの辺も両端でX座標もY座標もそろっていない', 'H22_dai22mon_zu04_shikichi_henchou', '座標の見た目にだまされるところでした'),
    ('3.85は書かない', '3.85は書かないんですか？', 'H22_dai22mon_zu05_touhokutou_kenzan', '位置の決め手には21番の側の距離'),
    ('床面積の多い21番地が先', '所在はどうなりますか？', 'H22_dai22mon_zu06_shozai_kakunin', '床面積の多い部分がある土地の地番を先に書く'),
    ('5.40ではなく3.60', '191.61平方メートル！', 'H22_dai22mon_zu08_1kai_ayamari_hikaku', '答案の求積は長方形に分けて足しなさい'),
    ('「並びに所有権の保存の登記」まで書く', '合体だから、『合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消』です！',
     'H22_dai22mon_zu13_kouku_yukisaki', '並びに所有権の保存の登記』です！'),
    ('（あ）（い）は付けない', '（あ）と（い）を付けて', 'H22_dai22mon_toukishinseisho_machigai_shinseinin', '合意した持分をそのまま書きます'),
    ('登記記録どおりの瓦葺', '構造は木造スレートぶき2階建……', 'H22_dai22mon_toukishinseisho_machigai_kouzou', 'スレートぶきは合体後の行だけ'),
    ('欄の番号を付けない', '欄の番号は付けないのね？', 'H22_dai22mon_zu14_genin_ranbangou', '合体後の建物は新しく表題登記をするから、付けません'),
    ('A銀行の抵当権は消滅の承諾', '全部書きます！', 'H22_dai22mon_zu15_a_ginkou_shoumetsu', 'その代わり、添付情報に抵当権消滅承諾証明情報'),
    ('賃借権は存続登記に当たらない', 'この2つは書きますか？', 'H22_dai22mon_zu16_sonzoku_hani', '賃借権は存続登記に当たらないから'),
    ('印鑑証明書は太郎さんの分だけ', '印鑑証明書は？', 'H22_dai22mon_zu17_inkan_shoumei', '申請書にも委任状にも印鑑証明書はいりません'),
    ('工事費の370万円ではなく', '工事費の370万円を足して2,100万円', 'H22_dai22mon_zu19_touroku_menkyozei', '課税価格は金1,200万円、登録免許税は金4万8,000円です'),
]
matome = text.split('今日のまとめよ。わなを1つずつ並べるわ」')[1].split('**藍子**')[0]
items = [l[2:] for l in matome.splitlines() if l.startswith('- ')]
ok = len(items) == len(TRAPS) == len({p for _, _, p, _ in TRAPS}) and all(k in it for (k, _, _, _), it in zip(TRAPS, items))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'まとめのわな{len(items)}項目と、わな→図の対応表{len(TRAPS)}組（図の重複なし・同じ順）')
ok = all(it.count('。') <= 1 and it.count('、') <= 3 for it in items)
ng += (not ok)
print(('OK ' if ok else 'NG ') + 'まとめの1項目に1つのわな')
mk_pos = [m.start() for m in re.finditer(r'^> 【画像挿入】.*$', text, re.M)]
order_png = [f[:-4] for _, f in PAIRS]
for key, phrase, png, word in TRAPS:
    pos = text.find(phrase)
    after = [k for k, p_ in enumerate(mk_pos) if p_ > pos][:2]
    k_png = order_png.index(png)
    ok = pos >= 0 and k_png in after and '\n## ' not in text[pos:mk_pos[k_png]]
    prev = [l for l in text[:mk_pos[k_png]].splitlines() if l.strip()][-1]
    ok2 = word in prev
    ng += (not ok) + (not ok2)
    print(('OK ' if ok else 'NG ') + f'わなの会話のあと2つ以内のマーカーに図がある : {phrase[:16]}… → {png}')
    print(('OK ' if ok2 else 'NG ') + f'わなの図のマーカーの直前の行に決め手の語 : {word[:20]}')
# 画像の題に図番がない（作図スクリプトのタイトル、申請書・添削のHTML）
titles = re.findall(r"(?:new_figure|box_fig|sheet_figure|suptitle)\(\s*'([^']*)'", draw)
bad = [t for t in titles if re.search(r'図\s*[0-9０-９]', t)] + [n for n, h in H.items() if re.search(r'[図画]像?\s*[0-9０-９]+[　 ：]', h)]
ng += bool(bad) or len(titles) < 20
print(('OK ' if not bad and len(titles) >= 20 else 'NG ') + f'画像の題（{len(titles)}個）とHTMLに図番がない : {bad}')
mk = open(os.path.join(ZU, 'make_H22_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
ok = 'style="height:' not in mk and not any('style="height:' in h for h in H.values())
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書・添削のHTMLに style="height: がない（min-height）')
# 答案用紙の原本から罫線を測り直して、作図・HTMLの値と比べる（H25/Q22の見本にならう）
import numpy as np
ROOT = os.path.join(HERE, '..', '..', '..', 'public', 'kijutsu', 'H22-tatemono')


def vlines(im, y0, y1, thr=200, frac=0.7):
    d = im < thr
    xs = [x for x in range(im.shape[1]) if d[y0:y1, x].sum() >= frac * (y1 - y0)]
    out = []
    for x in xs:
        if out and x - out[-1][-1] <= 3:
            out[-1].append(x)
        else:
            out.append([x])
    return [sum(g) / len(g) for g in out]


a2 = np.array(Image.open(os.path.join(ROOT, 'a2.webp')).convert('L'))
for name, (y0, y1), extra in [('COLS_PCT', (472, 508), [575.0]), ('S1_COLS_PCT', (780, 808), []), ('S2_COLS_PCT', (972, 1000), [])]:
    xs = sorted(vlines(a2, y0, y1) + extra)
    pct = [100 * (b_ - a_) / (xs[-1] - xs[0]) for a_, b_ in zip(xs, xs[1:])]
    got = [float(v) for v in re.search(name + r' = \(([^)]*)\)', mk).group(1).split(',')]
    ok = len(pct) == len(got) and all(abs(u - v) < 0.6 for u, v in zip(pct, got))
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'表の列の幅の比 {name}：答案用紙（その2）から測ると {[round(v, 1) for v in pct]}')
a3 = np.array(Image.open(os.path.join(ROOT, 'a3.webp')).convert('L'))
PX = a3.shape[1] / 420.0                               # A3横 420mm
def mm_x(px): return px / PX
def mm_y(py): return 297.0 - py / PX
fr = re.search(r"FR_L, FR_R, FR_B, FR_T = ([\d.]+), ([\d.]+), ([\d.]+), ([\d.]+)", draw).groups()
FR = [float(v) for v in fr]
v_sh = [x for x in vlines(a3, 147, 182) if x < 1150]                            # 建物の所在の欄の高さで縦の罫線（枠の左右・欄の仕切り）
h_rows = [y for y in range(a3.shape[0]) if (a3[y, 80:560] < 150).sum() > 380]   # 枠の上下・作成者の欄の下（横の罫線）
meas = {'枠の左': mm_x(v_sh[0]), '枠の右': mm_x(v_sh[-1]), '枠の上': mm_y(min(h_rows)), '図の枠の下': mm_y(sorted(set(h_rows))[2])}
want = {'枠の左': FR[0], '枠の右': FR[1], '枠の上': FR[3], '図の枠の下': FR[2]}
for k_ in meas:
    ok = abs(meas[k_] - want[k_]) < 0.8
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'（その3）の{k_}：原本 {meas[k_]:.1f}mm・作図 {want[k_]}mm')
mid = [x for x in vlines(a3, 145, 156, frac=0.8) if 500 < x < 620]
ok = len(mid) == 1 and abs(mm_x(mid[0]) - float(re.search(r'^MID = ([\d.]+)', draw, re.M).group(1))) < 0.8
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'（その3）の中央の仕切り：原本 {[round(mm_x(x), 1) for x in mid]}mm')
for k_, (y0, y1), xs_draw in [('家屋番号・建物の所在の仕切り', (104, 140), [190.1, 217.8, 254.9]),
                              ('作成者・申請人の欄の仕切り', (789, 834), [20.3, 45.6, 134.7, 146.4, 170.9, 191.7, 217.1, 306.3, 317.7, 342.3])]:
    got = [mm_x(x) for x in vlines(a3, y0, y1, thr=185, frac=0.8) if x < 1150]
    ok = all(any(abs(g - w) < 0.8 for g in got) for w in xs_draw)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'（その3）の{k_}：原本 {[round(g, 1) for g in got]}mm')
for v_ in ['kaoku_div=217.8', 'sakusei_div=(45.6, 134.7, 146.4)', 'shinsei_div=(217.1, 306.3, 317.7)', 'kaoku=(190.1, 254.9']:
    check('作図の枠の値', v_, draw, '作図')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')

# ---- タイトルの基本形 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成22年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成22年度問題22（建物）', thumb, '見出し画像')
for src, name in [(fig, '解説図'), (form, '申請書'), (fix, '添削')]:
    check('記事タイトルの引用', title[2:], src, name)

print('NG件数:', ng)
