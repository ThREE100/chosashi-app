"""平成29年度 第22問（建物）：記事の数値・計算・付属プロンプト・体裁の照合スクリプト。
アガルートの解答例（第22問 解答例、第1欄・第2欄・第3欄の各階平面図・求積表・建物図面）と一致することを確認済み。
日付は試験問題の本文どおり（平成29年）。アガルートの過去問集の再掲は日付が平成30年に置き換わっているため、日付だけは照合の対象外。
実行: python3 note-articles-Kijyutsu/H29/Q22/verify_H29_dai22mon.py"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import fmt_num

HERE = os.path.dirname(__file__)


def read(name):
    return open(os.path.join(HERE, name), encoding='utf-8').read()


text = read('note_H29_dai22mon_tatemono_kaisetsu.md')
fig = read('prompt_H29_dai22mon_kaisetsuzu.md')
form = read('prompt_H29_dai22mon_toukishinseisho_gazou.md')
fix = read('prompt_H29_dai22mon_toukishinseisho_machigai.md')
thumb = read('prompt_H29_dai22mon_miidashi_gazou.md')
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


# ---- 敷地：見取図（東西40.00・南北40.00、1番2は南西の12.00×15.00、隅切りは底辺〈斜めの辺〉2.00の直角二等辺三角形）----
leg = 2 / math.sqrt(2)                         # 直角をはさむ辺
assert fmt_num(leg) == '1.4142…'
cut = 2.00 * (2.00 / 2) / 2                    # 斜めの辺2.00 × 高さ1.00 ÷ 2
assert cut == 1.00 and abs(leg * leg / 2 - cut) < 1e-12
lot2 = 12.00 * 15.00 - cut
lot1 = 40.00 * 40.00 - 12.00 * 15.00 - 3 * cut
assert (lot2, lot1) == (179.00, 1417.00)       # 登記記録の地積と一致
assert (12.00 * 15.00 - 2.00, 40.00 * 40.00 - 180.00 - 3 * 2.00) == (178.00, 1414.00)  # 隅切りを「2辺が2.00」と誤読した場合
check('藍子の誤答（隅切り）', '2.00かける2.00割る2で2.00。180.00引く2.00で……178.00')
check('底辺＝斜めの辺', '直角二等辺三角形の底辺は、直角の向かい側の斜めの辺')
check('隅切りの面積', '面積は2.00かける1.00割る2で1.00よ')
check('1番2の検算', '180.00引く1.00で179.00。登記記録と一致しました')
check('1番1の検算', '全体の1600.00から1番2の四角の180.00と、残り3つの隅切りの3.00を引いて、1417.00')
check('直角をはさむ辺の表示', '`2 [÷] [√] 2 [)] [=]`。表示は1.4142…')
n_side = 40 - 2 * leg
w_side = 40 - 15 - leg
s_side = 40 - 12 - leg
assert (fmt_num(n_side), fmt_num(w_side), fmt_num(s_side)) == ('37.1715…', '23.5857…', '26.5857…')
check('北の辺', '`40 [−] 2 [×] [ALPHA] [A] [=]` で37.1715…')
check('西の辺', '`40 [−] 15 [−] [ALPHA] [A] [=]` で23.5857…')
check('南の辺', '`40 [−] 12 [−] [ALPHA] [A] [=]` で26.5857…')
assert round(n_side * 100 / 500, 1) == 7.4
check('縮尺換算', '北側の37.17メートルなら図面の上では約7.4センチ')
check('辺長は建物図面に書かない', 'この辺長は建物図面には書かないのよ')

# 解説図2の多角形（s＝1.4142）が地積と一致すること
s = 1.4142
LOT1 = [(0, 15), (0, 40 - s), (s, 40), (40 - s, 40), (40, 40 - s), (40, s), (40 - s, 0), (12, 0), (12, 15)]
LOT2 = [(0, s), (0, 15), (12, 15), (12, 0), (s, 0)]
assert round(poly_area(LOT1), 2) == 1417.00 and round(poly_area(LOT2), 2) == 179.00
for label, pts in [('図2 1番1', LOT1), ('図2 1番2', LOT2)]:
    st = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', st, fig, '解説図')
for lbl in ['「37.17m」', '「26.59m」', '「23.59m」', '「15.00m」', '「12.00m」', '「13.59m」', '「10.59m」', '「2.00m」', '「1.41m」',
            '12.00×15.00−1.00＝179.00', '40.00×40.00−180.00−3.00＝1417.00', '2.00×1.00÷2＝1.00㎡']:
    check('図2の数値', lbl, fig, '解説図')
assert (round(40 - 15 - leg, 2), round(40 - 12 - leg, 2), round(15 - leg, 2), round(12 - leg, 2)) == (23.59, 26.59, 13.59, 10.59)

# ---- 建物図面：甲建物（北2.00×2・西3.00）、丙建物（北3.00・東4.00×2）。敷地座標は Y＝東・X＝北、原点は区画の南西 ----
KOU_SITE = [(3, 36.18), (6.64, 36.18), (6.64, 38), (21.18, 38), (21.18, 27.08), (6.64, 27.08), (6.64, 28.9), (3, 28.9)]
HEI_SITE = [(28, 37), (36, 37), (36, 29.5), (28, 29.5)]
OTSU_SITE = [(2, 12.92), (9.28, 12.92), (9.28, 2), (2, 2)]
assert round(40 - 38, 2) == 2.00 and KOU_SITE[0][0] == 3.00 and round(40 - 37, 2) == 3.00 and 40 - 36 == 4.00
assert round(38 - 1.82, 2) == 36.18 and round(36.18 - 7.28, 2) == 28.90 and round(28.90 - 27.08, 2) == 1.82
assert round(3 + 3.64, 2) == 6.64 and round(6.64 + 14.54, 2) == 21.18 and round(38 - 10.92, 2) == 27.08
assert 36 + 37 < 80 - s                        # 丙建物の北東の角は北東の隅切りより内側
for y, x in KOU_SITE + HEI_SITE:               # 甲建物・丙建物は1番1の中（1番2〈Y＜12かつX＜15〉にかからない）
    assert 0 < y < 40 and 0 < x < 40 and not (y < 12 and x < 15)
for y, x in OTSU_SITE:                         # 乙建物は1番2の中だけ
    assert 0 < y < 12 and 0 < x < 15
assert round(poly_area(OTSU_SITE), 4) == 79.4976 and trunc2(poly_area(OTSU_SITE)) == 79.49
for label, pts in [('図3 甲建物', KOU_SITE), ('図3 丙建物', HEI_SITE), ('図1 乙建物', OTSU_SITE)]:
    st = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', st, fig, '解説図')
check('建物図面の距離', '『2.00』『2.00』『3.00』と『3.00』『4.00』『4.00』')
check('甲建物の北の距離', '北の筆界から東の部分の北の外壁まで、その北西の角と北東の角の2か所でどちらも2.00メートル')
check('丙建物の東の距離', '東の筆界から東の外壁まで、北東の角と南東の角の2か所でどちらも4.00メートル')
check('建物図面の記載事項', '不動産登記規則第82条第2項')
check('乙建物は描かない', '乙建物はもう別の建物だから描かないわ')
check('図3の距離ラベル', '甲建物「2.00」×2、「3.00」×1、丙建物「3.00」×1、「4.00」×2', fig, '解説図')

# ---- 甲建物（主である建物）：3.64×7.28＋14.54×10.92＝185.2760 → 185.27（切り捨て。四捨五入なら185.28）----
KOU = [(0, 1.82), (3.64, 1.82), (3.64, 0), (18.18, 0), (18.18, 10.92), (3.64, 10.92), (3.64, 9.1), (0, 9.1)]
s1 = [(3.64, 7.28), (14.54, 10.92)]
a1 = sum(w * h for w, h in s1)
assert round(a1, 4) == 185.2760 == round(poly_area(KOU), 4)
assert trunc2(a1) == 185.27 and round(a1, 2) == 185.28
assert round(10.92 - 2 * 1.82, 2) == 7.28
for w, h in s1:
    check(f'甲 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('甲 合計', '合計：185.2760 （床面積：185.27平方メートル）')
check('甲 切り捨て', '四捨五入すると185.28になって登記記録の185.27とずれる')
check('段の検算', '10.92から1.82を2つ引くと7.28')
check('乙 検算', '7.28かける10.92で79.4976、切り捨てて登記記録の79.49')
check('甲も各階平面図に', '主である建物と附属建物を合わせた変更後の建物全体のものよ（不動産登記令別表14の項、添付情報欄ハ）')

# ---- 丙建物（符号2）：1室の一部が1.5m未満でも算入（準則82条1号ただし書）→ 8.00×7.50＝60.00。誤答は8.00×6.90＝55.20 ----
HEI = [(0, 0), (8, 0), (8, 7.5), (0, 7.5)]
HEI_WRONG = [(0, 0.3), (8, 0.3), (8, 7.2), (0, 7.2)]
assert round(7.50 - 2 * 0.30, 2) == 6.90
assert round(8.00 * 7.50, 4) == 60.00 and round(8.00 * 6.90, 4) == 55.20 and round(60.00 - 55.20, 2) == 4.80
check('藍子の誤答（丙）', '8.00かける6.90で、55.20平方メートル！')
check('準則82条1号本文', '『天井の高さ1.5メートル未満の地階及び屋階（特殊階）は、床面積に算入しない』')
check('準則82条1号ただし書', '『ただし、1室の一部が天井の高さ1.5メートル未満であっても、その部分は、当該1室の面積に算入する』')
check('測定値は板の中心', '発泡ポリスチレン板の中心だから、8.00と7.50をそのまま使います。8.00かける7.50で、60.00平方メートルです')
check('差', '4.80平方メートルも取りこぼすわよ')
check('丙 求積表', '8.00 × 7.50 ＝ 60.0000\n- 合計：60.0000 （床面積：60.00平方メートル）')
check('立面図の数値', '真ん中は高さ3.75メートル')
for label, pts, want in [('図4 甲建物', KOU, 185.276), ('図3 甲建物（敷地）', KOU_SITE, 185.276), ('図3 丙建物（敷地）', HEI_SITE, 60.00),
                         ('図5・図6 丙建物', HEI, 60.00), ('図5 誤り', HEI_WRONG, 55.20)]:
    assert round(poly_area(pts), 4) == round(want, 4), label
for label, pts in [('図4 甲建物', KOU), ('図6 丙建物', HEI), ('図5 誤り', HEI_WRONG)]:
    st = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', st, fig, '解説図')
for lbl in ['8.00×6.90＝55.20㎡', '8.00×7.50＝60.00㎡', '床面積：185.27㎡（185.2760の100分の1未満を切り捨て）', '床面積：60.00㎡',
            '長方形①（西の張り出し）：Y：0〜3.64、X：1.82〜9.10（横3.64m×縦7.28m、面積26.4992）',
            '長方形②（東の部分）：Y：3.64〜18.18、X：0〜10.92（横14.54m×縦10.92m、面積158.7768）']:
    check('図の数値', lbl, fig, '解説図')

# ---- 問1（第1欄）----
reason = ('甲建物と乙建物が登記記録上一個の建物として登記されており、その一部である甲建物のみについて所有権の移転の登記をすることは'
          'できないため、乙建物を甲建物の登記記録から分割して、登記記録上別の一個の建物とする必要がある。')
assert reason.count('一個の建物') == 2
check('②の理由', '『主である建物のみについて所有権の移転の登記を行うためには、' + reason + '』')
check('②の理由', reason, form, '申請書（第1欄）')
check('①登記の目的（誤答：区分）', '登記の目的は『建物区分登記』です！')
check('①登記の目的', '登記の目的は『建物分割登記』ですね')
check('分割の定義', '不動産登記法第54条第1項第1号')
check('登記記録は一個の建物ごと', '一筆の土地、または一個の建物ごとです（不動産登記法第2条第5号）')
check('③（誤答：建物図面だけ）', '各階平面図は添付しなくていいと思います')
check('③の根拠', '不動産登記令の別表16の項、添付情報欄イ')
check('③の答え', '③は『添付しなければならない』です')
check('分割の図面の単位', '不動産登記規則第81条')
check('分割の登録免許税', '甲と乙の2個で2,000円')
check('第1欄 ①', '**①登記の目的**：建物分割登記', form, '申請書（第1欄）')
check('第1欄 ③', '**③当該登記の申請に各階平面図を添付しなければならないかどうか**：添付しなければならない。', form, '申請書（第1欄）')
check('分割後の所在', '分割で所在が変わったときは、登記官が変更後の所在を記録します（不動産登記規則第127条第3項）')
check('附属建物の判断', '不動産登記事務取扱手続準則第78条第1項')

# ---- 問2（第2欄）----
check('登記の目的', '「建物表題部変更登記です。')
check('添付書類', '建物図面、各階平面図、所有権証明書、登記事項証明書、代理権限証書の5点')
check('所有権証明書の根拠', '不動産登記令別表14の項、添付情報欄ハ）。種類の変更のほうは')
check('登記事項証明書の根拠', '不動産登記規則第36条第1項第1号・第2項')
check('申請人', '『A市C町二丁目6番2号　社会福祉法人C福祉会　理事長　人権岩男』')
check('期限', '不動産登記法第51条第1項')
check('所在（誤答）', '所在は、登記記録のとおり『A市B町三丁目1番地1、1番地2』')
check('所在（正解）', '所在は『A市B町三丁目1番地1』です')
check('調査日は分割の前', '調査日は……平成29年4月28日。あっ、分割の登記が終わった5月19日より前です')
check('変更前の主', '『主』、集会所、軽量鉄骨造亜鉛メッキ鋼板ぶき平家建、185.27平方メートル')
check('変更後の主', '『①平成29年7月20日種類変更』')
check('符号（誤答）', '丙建物は『符号1』です！')
check('符号の根拠', '不動産登記規則第127条第2項')
check('符号2', '符号2、倉庫、発泡ポリスチレン造平家建、60.00平方メートル。原因は『平成29年8月10日新築』')
check('構造', '構成材料と階数だけで『発泡ポリスチレン造平家建』')
check('構造の3要素', '主な部分の構成材料、屋根の種類、階数で決まる（不動産登記規則第114条）')
check('登記の目的', '**登記の目的**：建物表題部変更登記', form, '申請書')
check('添付書類', '建物図面　各階平面図　所有権証明書　登記事項証明書　代理権限証書', form, '申請書')
check('申請人', 'Ａ市Ｃ町二丁目６番２号　社会福祉法人Ｃ福祉会（2行目に、字下げして）理事長　人権岩男', form, '申請書')
check('申請日', '平成29年８月18日　申請　Ａ地方法務局', form, '申請書')
check('所在', '上段に「Ａ市Ｂ町三丁目１番地１」', form, '申請書')
check('家屋番号', '左の枠に「１番１」', form, '申請書')
check('変更前の床面積', '「185｜27」', form, '申請書')
check('変更後の原因', '「①平成29年７月20日種類変更」', form, '申請書')
check('符号2', '「符号２」', form, '申請書')
check('符号2の構造', '「発泡ポリスチレン造平家建」', form, '申請書')
check('符号2の床面積', '「60｜00」', form, '申請書')
check('符号2の原因', '「平成29年８月10日新築」', form, '申請書')
check('見出しの印刷文字', '「登記原因及びその日付」', form, '申請書')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')
check('誤答（所在）', '①誤答：所在の上段「Ａ市Ｂ町三丁目１番地１、１番地２」', fix, '添削')
check('誤答（符号）', '①誤答：記入行3の1列目「符号１」', fix, '添削')
check('誤答（構造）', '①誤答：記入行3の構造「発泡ポリスチレン造発泡ポリスチレンぶき平家建」', fix, '添削')
check('正解（所在）', '③正解：所在の上段「Ａ市Ｂ町三丁目１番地１」', fix, '添削')
check('正解（符号）', '③正解：記入行3の1列目「符号２」', fix, '添削')
check('正解（構造）', '③正解：記入行3の構造「発泡ポリスチレン造平家建」', fix, '添削')
check('添削の3段共通', '「①平成29年７月20日種類変更」', fix, '添削')
check('添削の3段共通', '「平成29年８月10日新築」', fix, '添削')

# ---- 日付：試験問題の本文どおり平成29年（アガルートの再掲の平成30年を写していない）----
for d in ['平成29年4月28日', '5月19日', '6月2日', '平成29年7月20日', '8月10日', '平成29年8月18日']:
    check('日付', d)
for src, name in [(text, '記事'), (form, '申請書'), (fix, '添削'), (fig, '解説図')]:
    absent('再掲の日付', '平成30年', src, name)

# ---- 形状・向き（図面の上＝北。見取図・調査図素図の方位記号で確認）----
check('1番2の位置', '1番2はその南西の角にあって、東西12.00メートル、南北15.00メートル')
check('丙建物の位置', '1番1の土地の北東の部分に8月10日に新築')
check('甲建物の張り出し', '西に張り出した小さな長方形')
check('0.30の帯', '北と南の壁ぎわは天井が低くなっています')
assert KOU[0][0] == 0 and max(y for y, _ in KOU) == 18.18   # 張り出し（Y＝0〜3.64）が西
assert HEI_SITE[1] == (36, 37)                              # 丙建物は北東
for bad in ['PDF', '創設的登記', '右上', '左下', '右側', '左側', '✕', '✓', '名変', '1冊']:
    absent('誤記・混入', bad)

# ---- note向けの体裁：話者名の行末に半角スペース2つ、名前とセリフの間に空行なし ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
ok = n_marker == 20
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカー（引用形式）: {n_marker}個（解説図15＋第1欄1＋添削3＋第2欄完成形1＝計20か所の想定）')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')
n_rule = sum(1 for l in lines if l == '---')
n_chap = len(re.findall(r'^## 第\d章', text, re.M))
ok = n_rule == 2 + (n_chap - 1) + 1
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'区切り線の数: {n_rule}（照合済みの後1＋登場人物の後1＋章の間{n_chap - 1}＋最後1）')

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成29年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜\n', thumb, '見出し画像')
check('見出し画像のタイトル', '\n平成29年度問題22（建物）\n', thumb, '見出し画像')
for src, name in [(fig, '解説図'), (form, '申請書'), (fix, '添削'), (thumb, '見出し画像')]:
    check('記事タイトル', title[2:], src, name)


# ---- 2026-09-29の追加作業（最新の依頼文・執筆プロンプトとの照らし合わせ）で足した内容 ----
# 日付の対応表：アガルートの過去問集の再掲（改題）→ 試験問題の本文。すべて1年2か月ずらしてある
DATES = [('平成30年6月28日', '平成29年4月28日', '依頼・調査日'), ('平成30年7月19日', '平成29年5月19日', '分割の登記の完了'),
         ('平成30年8月2日', '平成29年6月2日', '所有権の移転の登記の完了'), ('平成30年9月20日', '平成29年7月20日', '内装工事の完了（種類変更）'),
         ('平成30年10月10日', '平成29年8月10日', '丙建物の新築'), ('平成30年10月18日', '平成29年8月18日', '申請日（答案用紙の印刷）'),
         ('平成18年12月1日', '平成17年10月1日', '本件建物の登記記録の新築日')]
for kai, hon, what in DATES:
    y1, m1 = map(int, re.match(r'平成(\d+)年(\d+)月', kai).groups())
    y0, m0 = map(int, re.match(r'平成(\d+)年(\d+)月', hon).groups())
    assert (y1 * 12 + m1) - (y0 * 12 + m0) == 14, what
    absent('再掲の日付（' + what + '）', kai)
check('時系列メモ（甲）', '平成29年4月28日 B町自治会からの依頼（登記記録の調査日）、5月19日 分割の登記の完了（所在が1番地1だけになる）、6月2日 C福祉会への所有権の移転の登記の完了、7月20日 内装工事の完了（保育所に種類変更）')
check('時系列メモ（乙）', '5月19日 分割で1番1の登記記録から抜け、別の一個の建物になる')
check('時系列メモ（丙）', '8月10日 1番1の土地の北東の部分に新築（符号2の附属建物になる）')
# 所在の確認（座標）：甲建物の南の外壁は南の筆界から27.08、西の張り出しは28.90、丙建物は西の筆界から28.00〜36.00
assert round(40.00 - 2.00 - 10.92, 2) == 27.08 and round(40.00 - 2.00 - 1.82 - 7.28, 2) == 28.90
assert (40 - 4 - 8, 40 - 4) == (28, 36) and (round(2.00 + 10.92, 2), round(2.00 + 7.28, 2)) == (12.92, 9.28)
check('所在の確認（甲）', '南の外壁は40.00−2.00−10.92で、南の筆界から27.08メートルのところです')
check('所在の確認（張り出し）', '西の張り出しも、南の外壁は南の筆界から28.90メートルです')
check('所在の確認（丙）', '西の筆界から28.00〜36.00メートルのところで、1番2（西の筆界から12.00メートルまで）からは遠く離れています')
check('所在の確認（乙）', '南の筆界から12.92メートルまで、西の筆界から9.28メートルまで。1番2の中に収まっているの')
check('第3欄の上の欄', '建物図面の上の欄には、家屋番号『1番1』、建物の所在『A市B町三丁目1番地1』を書くの')
check('第3欄の（略）', '作成者と申請人の欄は（略）と印刷されているので、書くのは家屋番号と建物の所在ですね')
check('規則第83条第1項', '主である建物か附属建物かの別と附属建物の符号も書く事項よ（不動産登記規則第83条第1項）')
check('用紙の配置', '第3欄は1枚の枠を真ん中で仕切って、各階平面図と建物図面を並べて描くんですね。家屋番号と建物の所在の欄は建物図面の側の上に1つだけで、両方に共通です')
check('縮尺（問題文の注3）', '縮尺は250分の1（問題文の注3）')
check('準則第94条第2項', '準則第94条第2項に『③令和何年何月何日増築』のような欄番号の例があります')
check('登録免許税法別表第一', '分筆・合筆と建物の分割・区分・合併（一（十三））だけで、建物の表題部の変更の登記は載っていません')
check('解く順番（問を先に）', '前文と問題文の注と問1〜問3を、事実関係より先に読むの')
check('解く順番（累計のメモ）', '寸法線を足した累計（東西は0・3.64・18.18、南北は0・1.82・9.10・10.92）')
check('解く順番（まとめ）', '問を先に読む、問1と計算のいらない欄を先に埋める、累計をメモしてから作図する')
assert round(3.64 + 14.54, 2) == 18.18 and round(1.82 + 7.28, 2) == 9.10

# 注の書き分け：問題文の注は「問題文の注N」、図の注は「〔見取図〕の（注）N」「〔調査図素図〕の（注）N」
bare = [text[max(0, m.start() - 8):m.end()] for m in re.finditer(r'(?<!（)注[0-9]', text)
        if text[max(0, m.start() - 4):m.start()] != '問題文の']
ng += bool(bare)
print(('OK ' if not bare else 'NG ') + f'注の書き分け（「問題文の」のない「注N」）: {bare}')
for m in re.finditer(r'（注）[0-9]+', text):
    ctx = text[max(0, m.start() - 12):m.start()]
    ok = '〔見取図〕の' in ctx or '〔調査図素図〕の' in ctx
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '図の（注）の書き分け : ' + text[max(0, m.start() - 10):m.end()])

# 同じ話者のセリフの連続（画像挿入マーカー・求積表をはさんでも1つの連続とみなす）
prev, cont = None, []
for i, line in enumerate(lines):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        if line == prev:
            cont.append(i + 1)
        prev = line
ng += bool(cont)
print(('OK ' if not cont else 'NG ') + f'同じ話者の連続 : {cont}')
for bad in ['奥側', '手前側', '見取図の注', '調査図素図の注']:
    absent('向き・注の書き方', bad)

# ---- 画像（2026-09-29生成、2026-10-02に図3の描き直しと図7の新設）：記事の画像挿入マーカー11か所に対応するPNGがそろっているか ----
from PIL import Image
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('分割の前後比較図', 'H29_dai22mon_zu01_bunkatsu_zengo'), ('建物区分登記と建物分割登記の比較図', 'H29_dai22mon_zu02_kubun_bunkatsu'),
        ('各階平面図の添付の要否の比較図', 'H29_dai22mon_zu03_kakukai_youhi'), ('答案用紙の第1欄（問1）の完成形', 'H29_dai22mon_dai1ran_kansei'),
        ('建物ごとの時系列メモの図', 'H29_dai22mon_zu04_jikeiretsu'), ('注の仕分けの図', 'H29_dai22mon_zu05_chuu_shiwake'),
        ('隅切りの読み違いの比較図', 'H29_dai22mon_zu06_sumikiri_ayamari'),
        ('辺長確認図（作図チェック用）', 'H29_dai22mon_zu07_shikichi_henchou'), ('所在の確認図', 'H29_dai22mon_zu08_shozai_kakunin'),
        ('建物図面の完成形', 'H29_dai22mon_zu09_tatemono_zumen'),
        ('甲建物（主である建物）の床面積求積図', 'H29_dai22mon_zu10_kou_kyuuseki'), ('準則第82条第1号の読み方の流れ図', 'H29_dai22mon_zu11_jousoku82'),
        ('丙建物の誤り比較図', 'H29_dai22mon_zu12_hei_ayamari_hikaku'),
        ('丙建物（附属建物符号2）の床面積求積図', 'H29_dai22mon_zu13_hei_kyuuseki'),
        ('各階平面図の完成形', 'H29_dai22mon_zu14_kakukai_heimenzu'),
        ('登記申請書の「所在」欄の①誤答', 'H29_dai22mon_toukishinseisho_machigai_shozai'),
        ('「主である建物又は附属建物」欄の①誤答', 'H29_dai22mon_toukishinseisho_machigai_fugou'),
        ('「②構造」欄の①誤答', 'H29_dai22mon_toukishinseisho_machigai_kouzou'),
        ('登記申請書（問2）の完成形', 'H29_dai22mon_toukishinseisho_kansei'), ('本番で解く順番の図', 'H29_dai22mon_zu15_toku_junban')]
ok = len(markers) == len(PNGS) and all(k in m for m, (k, _) in zip(markers, PNGS))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーとPNGの対応（記事の順） : {len(markers)}か所')
for _, name in PNGS:
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path)
    if ok and 'toukishinseisho' in name:
        w, h = Image.open(path).size
        ok = w == 1200 and h > w          # 申請書・添削は横1200pxの縦長
    elif ok and 'dai1ran' in name:
        ok = Image.open(path).size[0] == 1200
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


html_has('H29_dai22mon_dai1ran_kansei', '建物分割登記', '主である建物のみについて所有権の移転の登記を行うためには，', reason,
         '添付しなければならない。')
h = html_has('H29_dai22mon_toukishinseisho_kansei', '建物表題部変更登記', '建物図面　各階平面図　所有権証明書　登記事項証明書',
             '代理権限証書', '平成29年８月18日　申請　　Ａ地方法務局', 'Ａ市Ｃ町二丁目６番２号　社会福祉法人Ｃ福祉会', '理事長　人権岩男',
             '不動産番号', 'Ａ市Ｂ町三丁目１番地１', '１番１', '登記原因及びその日付', '集会所', '保育所', '倉庫', '>185<', '>27<',
             '>60<', '符号２', '①平成29年７月20日種類変更', '平成29年８月10日新築', '発泡ポリスチレン造<br>平家建',
             'width:4.1%', 'width:15.5%', 'width:11.2%', 'width:19.3%', 'width:8.9%', 'width:8.4%', 'width:8.2%', 'width:24.4%',
             '<td class="val" colspan="2"></td><td class="val" colspan="4"></td>', '<td class="val" colspan="3">',
             '土地家屋調査士　法　務　守')
for bad in ['登録免許税', '住所証明書', '登記識別情報', '>55<', '>20<', '１番地２', '符号１', '>79<', '平成30年']:
    absent('申請書のHTML', bad, h, '申請書HTML')
html_has('H29_dai22mon_toukishinseisho_machigai_shozai', 'Ａ市Ｂ町三丁目１番地１、１番地２', '<span class="ink strike">、１番地２</span>',
         '調査日（4/28）の登記記録は、分割の登記（5/19）の前', '甲建物の所在は１番地１だけ', '不動産番号', '<svg class="check"')
html_has('H29_dai22mon_toukishinseisho_machigai_fugou', '符号１', '<span class="ink strike">１</span><span class="red">２</span>',
         '抹消の記号付きで甲建物の登記記録に残っている（規則第127条第2項）', '符号２', '<svg class="check"')
html_has('H29_dai22mon_toukishinseisho_machigai_kouzou', '発泡ポリスチレン造<br>発泡ポリスチレンぶき<br>平家建',
         '<span class="ink strike">発泡ポリスチレンぶき</span>', '屋根の種類はこしらえない', '発泡ポリスチレン造<br>平家建', '<svg class="check"')
for bad in ['✓', '✕', '横1600']:
    absent('添削・申請書プロンプトの記号', bad, form + fix, 'プロンプト')
    absent('解説図プロンプトの記号', bad, fig.replace('横1600px × 縦1200px', ''), '解説図')
check('添削は縦に3段', '横1200pxの縦長。上から「①誤答」「②添削（赤ペン）」「③正解」', fix, '添削')
drw = open(os.path.join(ZU, 'draw_H29_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
n_fit = len(re.findall(r"\bfit\(", drw))
ok = n_fit > 0 and drw.count('pad_aspect=True') == n_fit
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit はすべて pad_aspect=True : {n_fit}か所')
for n in ['assert round(area(LOT1), 2) == 1417.00 and round(area(LOT2), 2) == 179.00',
          "assert round(area([P(*v) for v in KOU]), 4) == 185.2760",
          'assert round(area([P(*v) for v in HEI]), 2) == 60.00 and round(area([P(*v) for v in HEI_WRONG]), 2) == 55.20',
          'assert 0 < p.imag < 12 and 0 < p.real < 15']:
    check('作図スクリプトの検算', n, drw, '作図')
for bad in ['✕', '✓', '右上', '左下']:
    absent('作図スクリプトの文字', bad, drw, '作図')


# ---- 2026-10-02の照らし直し（図面の完成形は答案用紙の第3欄の枠の中、各階平面図の完成形、穴埋め・記述の答えの明示） ----
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - set(n for _, n in PNGS))
ng += bool(extra)
print(('OK ' if not extra else 'NG ') + f'zu/ に記事で使わないPNGがない : {extra}')
for name in ['H29_dai22mon_zu09_tatemono_zumen', 'H29_dai22mon_zu14_kakukai_heimenzu']:
    w, h_ = Image.open(os.path.join(ZU, name + '.png')).size
    ok = w >= 1400 and h_ > w          # 第3欄の半分（縦長）を縮尺どおりに
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'PNGの大きさ : {name} {w}×{h_}')
# 答案用紙の第3欄の欄（試験の答案用紙 public/kijutsu/H29-tatemono/a2.webp の印刷どおり）
z03 = drw[drw.index('def zu09():'):drw.index('def P250(')]
z07 = drw[drw.index('def zu14():'):drw.index('def fixed(')]
for n in ["'家屋番号'", "'1番1'", "'建物の所在'", "'A市B町三丁目1番地1'", "'申 請 人'", "'（略）'", "'縮尺'", "'500')",
          "'建　物　図　面'", "half_frame(ax, cut='left')", "assert abs(abs(Sp(40, 0) - Sp(0, 0)) - 80.0) < 1e-9"]:
    check('建物図面の欄（図9）', n, z03, '作図')
absent('建物図面の所在に1番地2', '1番地1、1番地2', z03, '作図')
for n in ["'作 成 者'", "（平成29年○月○日作成）", "'250')", "'各　階　平　面　図'", "half_frame(ax, cut='right')",
          "3.64×7.28＝26.4992\\n14.54×10.92＝158.7768\\n計　185.2760\\n床面積　185.27m²",
          "8.00×7.50＝60.0000\\n床面積　60.00m²", "'主である建物'", "'附属建物　符号2'",
          "assert round(area(k) / 16, 4) == 185.276 and round(area(h) / 16, 4) == 60.0"]:
    check('各階平面図の欄（図14）', n, z07, '作図')
absent('各階平面図に家屋番号の欄', "'家屋番号'", z07, '作図')
# 答案用紙の第3欄の寸法（a2.webp、1px＝0.3mm）：半分の枠 150.9mm × 205.2mm、中央の目印 上9.9mm・下9.6mm
check('第3欄の寸法', 'HALF_W, SHEET_H = 150.9, 205.2', drw, '作図')
check('第3欄の目印', 'TICK_TOP, TICK_BOTTOM = 9.9, 9.6', drw, '作図')
check('答案用紙の欄（プロンプト）', '`public/kijutsu/H29-tatemono/a2.webp`', fig, '解説図')
check('各階平面図の完成形（記事のマーカー）', '主である建物（甲建物）と附属建物符号2（丙建物）の外形と周りの長さを同じ縮尺で描き、それぞれの横に求積表と床面積（185.27㎡・60.00㎡）')
check('建物図面の完成形（記事のマーカー）', '答案用紙の第3欄の右半分の建物図面の欄（家屋番号「1番1」・建物の所在「A市B町三丁目1番地1」・申請人（略）・縮尺1/500）の枠の中')
# 問1（第1欄）の①②③の答えを、会話の中で語のまま言っているか（穴埋め・記述の答えの明示。R5/Q22の照らし直しの教訓）
for lbl, w_ in [('①', '登記の目的は『建物分割登記』ですね'), ('②の語句', '一個の建物'), ('③', '③は『添付しなければならない』です')]:
    check('問1の答えの明示 ' + lbl, w_)
for lbl, w_ in [('①', '建物分割登記'), ('③', '添付しなければならない。')]:
    check('第1欄の画像の答え ' + lbl, w_, open(os.path.join(ZU, 'H29_dai22mon_dai1ran_kansei.html'), encoding='utf-8').read(), '第1欄HTML')


# ---- 2026-10-08の照らし直し（最新の執筆指示書：誤答・確認計算・注の仕分け・時系列メモの図、欄ごとの添削、図番なし、電卓のキー列） ----
check('区分と分割の図の位置', '登記の目的は『建物分割登記』ですね」\n\n> 【画像挿入】建物区分登記と建物分割登記の比較図')
check('各階平面図の要否の図の位置', '③は『添付しなければならない』です」\n\n> 【画像挿入】各階平面図の添付の要否の比較図')
check('分割の前後比較図の位置', '別の一個の建物にしておく必要があるの」\n\n> 【画像挿入】分割の前後比較図')
check('時系列メモの図の位置', '乙建物は5月19日で話が終わっているわ」\n\n> 【画像挿入】建物ごとの時系列メモの図')
check('隅切りの図の位置', 'こちらも一致です」\n\n> 【画像挿入】隅切りの読み違いの比較図')
check('所在の確認図の位置', '1番地2と書かないこと」\n\n> 【画像挿入】所在の確認図')
check('準則の流れ図の位置', '切り落とさないの」\n\n> 【画像挿入】準則第82条第1号の読み方の流れ図')
check('注の仕分け（会話）', '問題文の注1〜4、〔見取図〕の（注）1〜6、〔調査図素図〕の（注）1〜6')
check('注の仕分け（問題文の注3）', '問題文の注3は、建物図面が500分の1、各階平面図が250分の1という縮尺で、問3の作図に効きます')
check('注の仕分け（見取図の注6）', '〔見取図〕の（注）6は、隅切りが底辺2メートルの直角二等辺三角形だということで、敷地の地積の検算に使います')
check('注の仕分け（調査図素図の注4・6）', '〔調査図素図〕の（注）4は、測定値が軽量鉄骨の柱の中心か発泡ポリスチレン板の中心だということ、〔調査図素図〕の（注）6は')
check('構造（藍子の誤答）', '『発泡ポリスチレン造発泡ポリスチレンぶき平家建』です！')
check('構造（訂正）', '――屋根の種類をこしらえないの。')
check('第3欄の両半分（各階平面図のマーカー）', '答案用紙の第3欄の左半分の各階平面図の欄')
check('隅切りの斜めの辺の検算（複素数）', '`[Abs] [ALPHA] [A] [+] [ALPHA] [A] [i] [)] [=]` で、表示は2')
check('複素数モード', 'モードの2番でCPLXにしてから始めます')

# 電卓のキー列を記事の順にそのまま実行して、直後の「表示」と比べる（F-789SG。[√]・[Abs] は開きかっこを兼ねる＝第22問の記事の書き方）
import cmath
mem = {}


def run_keys(seq):
    toks = re.findall(r'\[[^\]]+\]|[0-9]+(?:\.[0-9]+)?', seq)
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t == '[ALPHA]':
            out.append(f"mem['{toks[i + 1][1:-1]}']")
            i += 2
            continue
        if t == '[SHIFT]' and toks[i + 1] == '[STO]':
            mem[toks[i + 2][1:-1]] = run_keys.last
            i += 3
            continue
        if t == '[i]':
            out[-1] = f'({out[-1]}*1j)'
        elif t == '[=]':
            run_keys.last = eval(''.join(out), {'mem': mem, 'sqrt': cmath.sqrt, 'absf': abs})
            out = []
        else:
            m_ = {'[÷]': '/', '[×]': '*', '[−]': '-', '[+]': '+', '[√]': 'sqrt(', '[Abs]': 'absf(', '[(]': '(', '[)]': ')'}
            if t.startswith('[') and t not in m_:
                raise ValueError('要点にないキー ' + t)
            out.append(m_.get(t, t))
        i += 1
    return run_keys.last


run_keys.last = None
keyseq = re.findall(r'`([^`]*\[[^`]*)`(?:。表示は| で、表示は| で)([0-9.]+…?)', text)
want = [('2 [÷] [√] 2 [)] [=]', '1.4142…'), ('40 [−] 2 [×] [ALPHA] [A] [=]', '37.1715…'),
        ('40 [−] 15 [−] [ALPHA] [A] [=]', '23.5857…'), ('40 [−] 12 [−] [ALPHA] [A] [=]', '26.5857…'),
        ('[Abs] [ALPHA] [A] [+] [ALPHA] [A] [i] [)] [=]', '2')]
ok = keyseq == want
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'記事のキー列と表示の組 : {keyseq}')
for seq, disp_ in keyseq:
    v = run_keys(seq)
    if seq.startswith('2 [÷]'):
        run_keys(seq + ' [SHIFT] [STO] [A]')     # 記事のとおり、表示した値を A に記憶する
    v = complex(v)
    got = fmt_num(v.real) if abs(v.imag) < 1e-12 else str(v)
    if got.endswith('…') is False and abs(v.real - round(v.real)) < 1e-9:
        got = str(int(round(v.real)))
    ok = got == disp_
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'電卓のキー列 {seq} → 表示 {got}（記事 {disp_}）')

# 画像の中に図の番号を書かない（題・見出し・画像の中の文字）
titles = re.findall(r"(?:new_figure|fixed|suptitle|set_title)\(\s*'([^']*)'", drw) + re.findall(r"SHEET_H \+ 27, '([^']*)'", drw)
bad_t = [t for t in titles if re.search(r'図\s*[0-9０-９]', t)]
ng += bool(bad_t) or len(titles) < 15
print(('OK ' if not bad_t else 'NG ') + f'画像の題に図の番号がない（{len(titles)}件） : {bad_t}')
mk = open(os.path.join(ZU, 'make_H29_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
absent('申請書・添削の画像に図の番号', '図1', mk, '申請書作成')
check('添削は欄ごとに3枚（プロンプト）', '欄ごとの3枚に分け', fix, '添削')
for nm in ['machigai_shozai', 'machigai_fugou', 'machigai_kouzou']:
    check('添削のファイル名', 'H29_dai22mon_toukishinseisho_' + nm, fix, '添削')
check('答案用紙の列の幅（プロンプト）', '建物の表示（縦書き）4.1・主である建物又は附属建物15.5・①種類11.2・②構造28.2・③床面積16.6', form, '申請書')
print('NG件数:', ng)
