"""令和2年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第1〜4欄・各階平面図・求積表・建物図面）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R2/Q22/verify_R2_dai22mon.py"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_R2_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_R2_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_R2_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_R2_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_R2_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


# ---- 敷地：〔座標一覧表〕A〜J（X＝北、Y＝東）。すべて東西・南北の辺で、斜めの辺はない ----
A, B, C, D = P(46.60, 0.00), P(46.60, 19.20), P(0.00, 0.00), P(0.00, 19.20)
E, F, G, H = P(-11.20, 0.00), P(-11.20, 19.20), P(-17.40, 0.00), P(-17.40, 19.20)
I, J = P(-19.90, 0.00), P(-19.90, 19.20)
for w, e in [(A, B), (C, D), (E, F), (G, H), (I, J)]:
    assert w.real == e.real and w.imag == 0 and e.imag == 19.20  # 東西の辺は真東西、西の辺Y＝0・東の辺Y＝19.20
assert [round(abs(p - q), 2) for p, q in [(A, C), (C, E), (E, G), (G, I)]] == [46.60, 11.20, 6.20, 2.50]
check('座標の並び', 'A・C・E・G・IのY座標が全部0.00で、B・D・F・H・JのY座標が全部19.20')
check('辺長', '南北は、39番3が46.60、42番1が11.20、42番2が6.20、42番3が2.50メートル')
check('複素数モードは使わない', '複素数モードを使わなくても、座標の差で出ます')
check('辺長は建物図面に書かない', 'この辺長はあくまで作図のチェック用。建物図面には書かないのよ')
check('北の向き', '北の方向は西側の102番の道路と平行だから、図面の上が北です')

# ---- 建物の位置：〔3.9〕は道路（Y＝0）から、〔3.2〕は42番4との境（I・J、X＝−19.90）から ----
south = round(I.real + 3.2, 2)
north = round(south + 6.10, 2)
west, east = 3.9, round(3.9 + 12.00, 2)
assert (south, north, east) == (-16.70, -10.60, 15.90)
to_gh = round(south - G.real, 2)
into_421 = round(north - E.real, 2)
on_422 = round(E.real - south, 2)
assert (to_gh, into_421, on_422) == (0.70, 0.60, 5.50) and round(19.20 - east, 2) == 3.30
assert on_422 > into_421  # 床面積の多い部分は42番2 → 所在は42番地2が先
check('南の外壁', 'マイナス19.90足す3.2で、X＝マイナス16.70')
check('北の外壁', 'マイナス16.70足す6.10で、X＝マイナス10.60')
check('42番3との境まで', '42番3との境から0.70メートルしか離れていません')
check('42番1へのはみ出し', '北の0.60メートルだけ42番1にはみ出して、残りの5.50メートルは42番2の上')
check('建物図面の距離（南）', '南の距離は『0.7』を、南西の角と南東の角の2か所に書くの')
check('建物図面の距離（西）', '西は道路（102）との境から『3.9』')
check('小数第1位', '『0.70』とは書かないこと')
check('縮尺換算', '0.05メートルは図面上0.1ミリ')
assert round(0.05 * 1000 / 500, 2) == 0.1

# ---- 床面積：注3・注5（測定値は外壁の外側の隅角部、壁の中心線は0.05内側）----
w12, d12 = round(12.00 - 0.10, 2), round(6.10 - 0.10, 2)
assert (w12, d12) == (11.90, 6.00) and trunc2(w12 * d12) == 71.40
wrong1 = round(12.00 * 6.10, 2)
assert wrong1 == 73.20 and round(wrong1 - 71.40, 2) == 1.80
porch = round(1.50 * 3.50, 2)
assert porch == 5.25 and round(71.40 - porch, 2) == 66.15
check('藍子の誤答（外壁の外側）', '12.00かける6.10で、73.20平方メートルです！')
check('壁心', '11.90かける6.00で、71.40平方メートルです')
check('差', '1.80平方メートルも多くなるのよ')
check('旧ポーチ', '壁の中心線で横1.50メートル × 縦3.50メートル、5.25平方メートル')
check('新築時の1階', '1階は66.15平方メートルでした')
for fl in ['1階', '2階']:
    check(f'{fl} 求積表', f'＜{fl} 求積表＞\n\n- 11.90 × 6.00 ＝ 71.4000\n- 合計：71.4000 （床面積：71.40平方メートル）')

# 3階：南西の4.10×1.80（外側の寸法の値）が屋外。両端のずれの向きで壁心の寸法が決まる
#   4.10：西の壁も洋室の西の壁も中心線が東へ0.05 → 4.10のまま
#   1.80：LDKの南の壁も建物の南の壁も中心線が北へ0.05 → 1.80のまま
#   12.00・6.10・4.30・7.90：両端とも内側へ0.05 → 0.10減る
wW, dW = 4.10, round(4.30 - 0.10, 2)
wE, dE = round(7.90 - 0.10, 2), round(6.10 - 0.10, 2)
assert (wW, dW, wE, dE) == (4.10, 4.20, 7.80, 6.00)
assert round(wW + wE, 2) == w12 and round(dW + 1.80, 2) == dE  # 壁心の外周と一致
f3 = round(wW * dW + wE * dE, 4)
assert f3 == 64.02 and trunc2(f3) == 64.02
assert round(71.40 - 4.10 * 1.80, 2) == 64.02  # 全体から欠けを引いても同じ（検算のみ）
wrong3 = round(round(4.10 - 0.10, 2) * dW + wE * dE, 4)
assert wrong3 == 63.60 and round(f3 - wrong3, 2) == round(0.10 * 4.20, 2) == 0.42
check('3階の形', '南西の角が欠けたL字形です')
check('3階の欠け', '南西の角の横4.10メートル × 縦1.80メートルは、南のバルコニーとつながった屋外の部分')
check('3階の寸法', '西の辺が北から4.30と1.80、南の辺が西から4.10と7.90、東の辺が6.10')
check('藍子の誤答（全部から0.10）', '4.00かける4.20で16.80')
check('藍子の誤答の合計', '合計63.60平方メートルです！')
check('4.10のまま', '両端が同じ向きにずれるんだから、長さは変わらず4.10のまま')
check('1.80のまま', '壁の中心線は北向きに0.05ずれるから1.80のまま')
check('抜けた帯', '横0.10メートル × 縦4.20メートルの細い帯が消えていました')
check('差', '0.42平方メートルの損よ')
check('3階 求積表', '- 4.10 × 4.20 ＝ 17.2200\n- 7.80 × 6.00 ＝ 46.8000\n- 合計：64.0200 （床面積：64.02平方メートル）')
check('各階同型', '1階と2階を『各階同型』として1つの図にまとめてもいいわ')
check('縮尺', '縮尺は250分の1。建物図面の500分の1と取り違えないようにね')

# ---- 問1（第1欄）：建物滅失登記 ----
check('家屋番号の特定', '取り壊した本件旧建物は家屋番号39番3の4です！')
check('登記記録が同じ', '1階65.42平方メートル、2階26.49平方メートル』で、まったく同じです')
check('39番3の図面', '北の筆界から2.1メートル、道路から5.8メートルの四角い建物')
check('申請人（誤答）', '『A市B区T町三丁目39番地3　五輪松子』……')
check('申請人（正解）', '答えは『A市B区T町三丁目42番地2　五輪松子』')
check('住所証明書⇔変更証明書', '住所証明書は、表題登記で、新しく表題部所有者になる人の住所を示すための書類よ')
check('添付書類', '添付書類は、変更証明書と、調査士が代理で申請するので代理権限証書')
check('所在・家屋番号', '所在は『A市B区T町三丁目39番地3』、家屋番号は『39番3の4』です')
check('下線の行（誤答）', '居宅、木造瓦葺2階建、1階65.42平方メートル、2階26.49平方メートル！')
check('最新の行', '種類は平成16年の変更で『居宅・店舗』。構造は昭和62年の変更で『木造スレート葺2階建』。床面積は平成16年の増築で、1階84.05平方メートル、2階26.49平方メートルです')
check('葺の転写', '登記記録の文字どおりに『木造スレート葺2階建』と写すの')
check('符号1', '符号1は、車庫、鉄骨造合金メッキ鋼板葺平家建、50.45平方メートル')
check('原因', '主である建物の行に『令和2年10月12日取壊し』')
# 変更証明書の法令上の位置づけ（令第7条第1項・別表に通常の建物の滅失登記の項なし、法第25条第7号は権利に関する登記の登記義務者、法第57条）
check('令7条・別表', '別表に載っている建物の滅失の登記は、共用部分である旨の登記がある建物の滅失（別表の17の項）だけ')
check('法25条7号', '不動産登記法第25条第7号も、権利に関する登記の登記義務者などの話で、滅失登記には当てはまらない')
check('法定の添付情報ではない', '変更証明書は、条文で『必ず付けなさい』と決められた添付情報じゃないのよ')
check('法57条', '滅失登記を申請できるのは、表題部所有者か所有権の登記名義人だけ（不動産登記法第57条）')
# 名義変更（登記名義人住所変更登記）の要否：滅失登記は不要（法務局の記載例 注3・規則144条1項）、権利に関する登記は前提として必要（法25条7号）
check('法務局の記載例', '住所の移り変わりが分かる住民票の写しや戸籍の附票の写しを付けると書いてある')
check('名義変更は不要', '滅失登記なら、その必要はないわ')
check('規則144条1項', '登記記録は閉鎖される（不動産登記規則第144条第1項）')
check('権利に関する登記は名義変更が前提', '所有権移転や抵当権の抹消のような、権利に関する登記よ')
check('まとめ', '住所変更の登記を先にする必要はありません。')
absent('先例番号（原典未確認）', '登記研究')
absent('略語（名義変更と書く）', '名変')

# ---- 問2（第2欄）----
check('解体移転', '解体移転の場合：①有・建物滅失登記、建物表題登記　②解体によって建物の同一性が失われるため')
check('えい行移転', 'えい行移転の場合：①無　②建物の同一性は失われず、同じ土地の中での移動で所在に変更が生じないため')
check('えい行（誤答：表題部変更登記）', '所在の変更として、建物表題部変更登記の申請義務が『有』です！')
check('えい行（訂正）', '39番3の土地の中で北の端から南の端に動いても、所在は39番地3のまま')

# ---- 問3（第3欄）：建物表題登記 ----
check('添付書類', '建物図面、各階平面図、この建物が松子さんのものだと示す所有権証明書、表題部所有者になる松子さんの住所を示す住所証明書、それに代理権限証書の5点')
check('申請人', '『A市B区T町三丁目42番地2　五輪松子』。住所証明書の住所とそろいます')
check('所在（誤答）', '番号の順に『A市B区T町三丁目42番地1、42番地2』です！')
check('所在（正解）', '『A市B区T町三丁目42番地2、42番地1』')
check('家屋番号', '『（記載不要）』と印刷されているわ')
check('種類（誤答：居宅）', '『店舗・共同住宅・居宅』です！')
check('種類（正解）', '『共同住宅・店舗』ですね')
check('構造', '『鉄骨造合金メッキ鋼板ぶき3階建』')
check('床面積', '床面積は、1階71.40平方メートル、2階71.40平方メートル、3階64.02平方メートル')
check('原因（誤答）', '『令和2年9月18日新築』だけです！')
check('原因（正解）', '『令和2年9月18日新築　令和2年10月12日増築』')
check('申請は2件', '申請は2件ね')

# ---- 付属プロンプトとの整合 ----
check('滅失 登記の目的', '**登記の目的**：建物滅失登記', form, '申請書')
check('滅失 添付書類', '**添付書類**：変更証明書　代理権限証書', form, '申請書')
check('申請人', '**申請人**：Ａ市Ｂ区Ｔ町三丁目42番地２　五輪松子', form, '申請書')
check('滅失 所在', '**所在**：Ａ市Ｂ区Ｔ町三丁目39番地３', form, '申請書')
check('滅失 家屋番号', '**家屋番号**：39番３の４', form, '申請書')
check('滅失 主', '「木造スレート葺２階建」', form, '申請書')
check('滅失 主の床面積', '「1階　84｜05」「2階　26｜49」', form, '申請書')
check('滅失 原因', '「令和２年10月12日取壊し」', form, '申請書')
check('滅失 符号1', '「鉄骨造合金メッキ鋼板葺平家建」', form, '申請書')
check('滅失 符号1の床面積', '「50｜45」', form, '申請書')
check('表題 登記の目的', '**登記の目的**：建物表題登記', form, '申請書')
check('表題 添付書類', '建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書', form, '申請書')
check('表題 所在', '**所在**：Ａ市Ｂ区Ｔ町三丁目42番地２、42番地１', form, '申請書')
check('表題 種類', '「共同住宅・店舗」', form, '申請書')
check('表題 構造', '「鉄骨造合金メッキ鋼板ぶき３階建」', form, '申請書')
check('表題 床面積', '「1階　71｜40」「2階　71｜40」「3階　64｜02」', form, '申請書')
cause = '「令和２年９月18日新築」「令和２年10月12日増築」'
check('表題 原因', cause, form, '申請書')
check('日付と提出先', '令和２年10月16日　申請　Ａ地方法務局', form, '申請書')
check('欄名（答案用紙どおり）', '「原因及びその日付」', form, '申請書')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')
check('正解', cause, fix, '添削')
check('誤答', '**「令和２年９月18日新築」**', fix, '添削')
check('新築時の1階', '9月18日の新築時は66.15㎡', fix, '添削')

# 解説図プロンプトの頂点座標（建物＝Y東・X南、敷地＝Y東・X北）が求積表と一致すること
F12 = [(0, 0), (11.9, 0), (11.9, 6), (0, 6)]
PORCH = [(0, 0), (1.5, 0), (1.5, 3.5), (0, 3.5)]
OUTER = [(-0.05, -0.05), (11.95, -0.05), (11.95, 6.05), (-0.05, 6.05)]
F3 = [(0, 0), (11.9, 0), (11.9, 6), (4.1, 6), (4.1, 4.2), (0, 4.2)]
W3_OK = [(0, 0), (4.1, 0), (4.1, 4.2), (0, 4.2)]
W3_NG = [(0, 0), (4.0, 0), (4.0, 4.2), (0, 4.2)]
E3 = [(4.1, 0), (11.9, 0), (11.9, 6), (4.1, 6)]
SITE_BLDG = [(west, north), (east, north), (east, south), (west, south)]
for label, pts, want in [('図4 1・2階', F12, 71.40), ('図4 旧ポーチ', PORCH, 5.25), ('図4 外壁の外側', OUTER, 73.20),
                         ('図6 3階', F3, 64.02), ('図5・図6 西の列', W3_OK, 17.22), ('図5 誤りの西の列', W3_NG, 16.80),
                         ('図5・図6 東の列', E3, 46.80), ('図2・図3 建物の外形', SITE_BLDG, 73.20)]:
    assert round(poly_area(pts), 2) == want, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
assert round(poly_area(W3_NG) + poly_area(E3), 2) == 63.60
# 建物が42番1・42番2の区画の内側（道路・40番・42番3との境の内側）にある
for y, x in SITE_BLDG:
    assert 0 < y < 19.20 and G.real < x < C.real
for s in ['「3.9」×1、「0.7」×2', '「11.20m」（42-1）「6.20m」（42-2）', '0.7（42-3との境まで。建物図面に書く値）',
          '〔3.2〕（42-4との境まで。平面図の値）', '42-1にかかるのは北の0.60だけ', '床面積：71.40㎡（新築した9月18日の1階は66.15㎡）',
          '赤字で「4.00×4.20＋7.80×6.00＝63.60㎡」', '緑の文字で「4.10×4.20＋7.80×6.00＝64.02㎡」', '3階 床面積：64.02㎡', '抜け落ちた帯 0.10×4.20＝0.42㎡']:
    check('図の数値', s, fig, '解説図')

# ---- 形状・向き（図面の上＝北）----
check('3階の欠けは南西（図）', '欠けが南西の角にあり', fig, '解説図')
check('旧ポーチは北西（図）', '旧ポーチが北西の角にあるか', fig, '解説図')
assert F3[3][1] == 6 and F3[4] == (4.1, 4.2)  # 欠けはY小（西）・X大（南）
check('エントランスは北西', '北西の角のエントランス')
for bad in ['PDF', '創設的登記', '『3.2』を書けば完成', '右上', '左下', '右側', '左側', '『3.90』', '『0.70』を']:
    absent('誤記・混入', bad)

# ---- note向けの体裁：話者名の行末に半角スペース2つ、名前とセリフの間に空行なし ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
ok = n_marker == 22
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカー（引用形式）: {n_marker}個（解説図15＋添削4＋申請書の完成形2＋第2欄1＝計22か所の想定）')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和2年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和2年度問題22（建物）', thumb, '見出し画像')
for name, src in [('解説図', fig), ('申請書', form), ('添削', fix), ('見出し画像', thumb)]:
    absent('他年度の混入', '令和7年度', src, name)

# ---- 2026-09-29 最新の依頼文・執筆プロンプトに合わせた追加分 ----
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
# 注の書き分け：問題文の注（1〜5）、〔調査図〕の（注）（1〜5）、〔平面図〕の（注）（1〜9）を区別して書く
bare = [m.start() for m in re.finditer(r'注[0-9]', text) if not text[:m.start()].endswith('問題文の')]
bare += [m.start() for m in re.finditer(r'（注）[0-9]', text)
         if not text[:m.start()].endswith(('〔調査図〕の', '〔平面図〕の', 'と', '・', '同じく'))]
ok = not bare
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'注の書き分け（「問題文の注N」「〔調査図〕の（注）N」「〔平面図〕の（注）N」） : 書き分けていない箇所 {len(bare)}')
for bad in ['✕', '✓', '名変', '登記研究']:
    absent('記号・略語・未確認の先例', bad)
# 条文（note-articles/laws/ の原典で確認したもの）
check('準則88条2項', '床面積の多い部分がある土地の地番を先に書くのよ（不動産登記事務取扱手続準則第88条第2項）')
check('規則113条', '主な用途が2つ以上あれば2つ以上で定める（不動産登記規則第113条）')
check('現在の法令：法76条の5', '令和3年の改正（令和3年法律第24号）で不動産登記法第76条の5ができて')
check('現在の法令：附則', '改正の前に住所が変わった人にも、附則で当てはめられるわ')
check('現在の法令：過料', '怠れば5万円以下の過料（同法第164条第2項）')
check('現在の法令でも滅失登記の答えは同じ', '答案の添付書類は、今でも変更証明書と代理権限証書のまま')
# 予備校の解説と見比べて足した解く順番
check('解く順番', 'まず前文と問題文の注、問1〜問4を先に読んで')
check('問2は後回し', '問2は、一番北の建物をどこへ動かすのかが〔調査図〕と建物図面を読まないと決まらないから、後回し')
check('所在は作図のあと', '問3の所在の欄は作図のあとで書くこと')

# ---- 画像（2026-09-29生成、2026-10-02更新）：記事の画像挿入マーカー12か所と zu/ のPNGの対応 ----
from PIL import Image
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R2_dai22mon_zu01_kaoku_bangou', '建物図面3枚と〔調査図〕を突き合わせて家屋番号を特定する'),
        ('R2_dai22mon_zu02_chuu_shiwake', '注の仕分けの図'),
        ('R2_dai22mon_toukishinseisho_machigai_shinseinin', '第1欄の「申請人」欄の①誤答'),
        ('R2_dai22mon_toukishinseisho_machigai_tenpu', '第1欄の「添付書類」欄の①誤答'),
        ('R2_dai22mon_zu03_jyuusho_zentei', '登記記録の住所が古いときの比較図'),
        ('R2_dai22mon_zu04_jyuusho_gimuka', '本試験（令和2年）と今の法令の比較図'),
        ('R2_dai22mon_toukishinseisho_machigai_hyouji', '第1欄の建物の表示（主である建物の行）の①誤答'),
        ('R2_dai22mon_toukishinseisho_kansei_toi1', '問1（第1欄）の建物滅失登記の申請書の完成形'),
        ('R2_dai22mon_zu05_eikou_iten', '問2の比較図'),
        ('R2_dai22mon_dai2ran_kansei', '問2（第2欄）の完成形'),
        ('R2_dai22mon_zu06_shikichi_ichi', '確認図（作図チェック用）'),
        ('R2_dai22mon_zu07_tatemono_zumen', '第4欄の右半分の建物図面の枠（家屋番号と申請人は「（略）」と印刷、建物の所在「A市B区T町三丁目42番地2、42番地1」'),
        ('R2_dai22mon_zu08_1kai2kai_kyuuseki', '1階・2階の床面積求積図'),
        ('R2_dai22mon_zu09_3kai_ayamari_hikaku', '左に「誤り＝全部の寸法から0.10を引いた'),
        ('R2_dai22mon_zu10_3kai_kyuuseki', '3階の床面積求積図'),
        ('R2_dai22mon_zu11_kakukai_heimenzu', '問4の完成形（第4欄）。左半分の各階平面図の枠（作成者は「（略）」「（令和2年○月○日作成）」と印刷、縮尺1/250）'),
        ('R2_dai22mon_zu12_shozai_junjo', '所在の順序の図'),
        ('R2_dai22mon_zu13_shurui', '種類の図'),
        ('R2_dai22mon_zu14_zouchiku_heiki', '表題登記の前の増築の時系列の図'),
        ('R2_dai22mon_toukishinseisho_machigai', '「原因及びその日付」欄の①誤答'),
        ('R2_dai22mon_toukishinseisho_kansei_toi3', '問3（第3欄）の建物表題登記の申請書の完成形'),
        ('R2_dai22mon_zu15_toku_junban', '本番で解く順番の図')]
ok = len(markers) == len(PNGS)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーとPNGの数 : {len(markers)}／{len(PNGS)}')
for (name, key), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        ok = (w == 1200 and h > w) if ('toukishinseisho' in name or 'dai2ran' in name) else (w >= 1600 and h >= 900)
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


html_has('R2_dai22mon_toukishinseisho_kansei_toi1', '建物滅失登記', '変更証明書　代理権限証書', 'Ａ市Ｂ区Ｔ町三丁目42番地２', '五輪松子',
         '令和２年10月16日　申請　Ａ地方法務局', 'Ａ市Ｂ区Ｔ町三丁目39番地３', '39番３の４', '木造スレート葺', '1階　84', '>05<',
         '2階　26', '>49<', '令和２年10月12日', '取壊し', '符号１', '鉄骨造合金メッキ', '鋼板葺平家建', '>50<', '>45<', '原因及びその日付',
         '不動産登記法第76条の5', '出題当時はなかった', '記入は今の法令でも同じ',
         bad=('登録免許税', '住所証明書', '所有権証明書', '瓦葺', '65</span>', '39番地３</span><br>'))
html_has('R2_dai22mon_toukishinseisho_kansei_toi3', '建物表題登記', '建物図面　各階平面図　所有権証明書', '住所証明書　代理権限証書',
         'Ａ市Ｂ区Ｔ町三丁目42番地２、42番地１', '（記載不要）', '共同住宅', '店舗', '鋼板ぶき３階建', '1階　71', '2階　71', '3階　64',
         '>40<', '>02<', '令和２年９月18日新築', '令和２年10月12日増築',
         bad=('登録免許税', '居宅', '変更証明書', '73', '63', '42番地１、42番地２'))
html_has('R2_dai22mon_dai2ran_kansei', '解体移転の場合', 'えい行移転の場合', '建物滅失登記、建物表題登記',
         '解体によって建物の同一性が失われるため', '所在に変更が生じないため', '<span class="circ ink">有</span>',
         '<span class="circ ink">無</span>')
html_has('R2_dai22mon_toukishinseisho_machigai', '令和２年９月18日新築', '令和２年10月12日増築', '66.15', '5.25', '併記',
         '<svg class="check"', bad=('✓',))
html_has('R2_dai22mon_toukishinseisho_machigai_shinseinin', 'Ａ市Ｂ区Ｔ町三丁目39番地３', 'Ａ市Ｂ区Ｔ町三丁目42番地２', '五輪松子',
         '10月3日に42番地２へ転居', '<svg class="check"', '代　　理　　人', '令和２年10月16日　申請　Ａ地方法務局', bad=('✓',))
html_has('R2_dai22mon_toukishinseisho_machigai_tenpu', '住所証明書　代理権限証書', '変更証明書　代理権限証書', '建物滅失登記',
         '表題部所有者になる人の住所', '<svg class="check"', bad=('✓',))
html_has('R2_dai22mon_toukishinseisho_machigai_hyouji', '木造瓦葺', '木造スレート葺', '居宅・店舗', '1階　65', '1階　84', '>05<', '2階　26',
         '令和２年10月12日', '平成16年', '昭和62年', '<svg class="check"', bad=('✓',))
for nm_ in ['machigai_shinseinin', 'machigai_tenpu', 'machigai_hyouji']:
    check('添削のプロンプト', f'zu/R2_dai22mon_toukishinseisho_{nm_}.png', fix, '添削')
check('添削：縦に積む', '縦に積む（横に並べない）', fix, '添削')
absent('横1600px（旧版の横長）', '横1600px', fix, '添削')
absent('記号', '✓', fix, '添削')
absent('記号（図の見出し）', '✕', fig, '解説図')
absent('記号', '○ ', fig, '解説図')
check('第2欄の画像', '画像3（第2欄・問2の答え）', form, '申請書')
drw = open(os.path.join(ZU, 'draw_R2_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
fits = re.findall(r'\bfit\((?:ax|ax2|axes\[[0-2]\])[^\n]*', drw)
ok = bool(fits) and all('pad_aspect=True' in f for f in fits)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit がすべて pad_aspect=True : {len(fits)}か所')
for a in ['round(area(F3), 2) == 64.02', 'round(area(W3_NG) + area(E3), 2) == 63.60', 'round(area(SITE_BLDG), 2) == 73.20',
          'round(area(F12) - area(PORCH), 2) == 66.15']:
    check('作図スクリプトの面積の検算', a, drw, '作図')


# ---- 2026-10-02 最新の執筆プロンプトに合わせた追加分：図面の完成形は答案用紙の第4欄の枠の中、各階平面図の完成形 ----
check('第4欄の上の欄', '建物図面の上の家屋番号の欄には、はじめから『（略）』と印刷してあるから何も書かない。下の申請人の欄も『（略）』と印刷済み。書くのは建物の所在の欄だけで、問3の申請書の所在と同じものを書く')
check('第4欄の所在の順', '第4欄の建物図面の建物の所在の欄も、この順で書きます')
check('各階平面図の求積方法', '床面積とその求積方法も記録する決まりだもの（不動産登記規則第83条第1項）')
check('各階同型', '（不動産登記事務取扱手続準則第53条第2項）')
for s_ in ["'A市B区T町三丁目42番地2、42番地1'", "'（略）'", "'500', fs=10)", "'250', fs=10)", "'R2_dai22mon_zu11_kakukai_heimenzu'",
           "'R2_dai22mon_zu15_toku_junban.png'", "'1階・2階（各階同型）'", '床面積　64.02㎡', '床面積　71.40㎡',
           'round(area(F12), 4) == 71.40 and round(area(F3), 4) == 64.02']:
    check('作図スクリプト（図7・図11の枠と記入）', s_, drw, '作図')
check('枠の形は試験の答案用紙で確かめた', '欄の形の出典：**試験の答案用紙（`touan_youshi/R2_dai22mon_touan_youshi.pdf` の2ページ目）で確かめた**', fig, '解説図')

# ---- 2026-10-02 試験の答案用紙（touan_youshi/）の実物で確かめた欄の形 ----
import pymupdf as fitz  # noqa: E402
TY = os.path.join(HERE, 'touan_youshi', 'R2_dai22mon_touan_youshi.pdf')
_doc = fitz.open(TY)
sheet = [re.sub(r'\s+', '', pg.get_text()) for pg in _doc]
mkp = open(os.path.join(ZU, 'make_R2_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
# 1ページ目：第1欄・第2欄・第3欄（申請書2件と問2）
for n_ in ['第1欄', '第2欄', '第3欄', '登記の目的', '添付書類', '申請人', '代理人（略）', '令和2年10月16日申請Ａ地方法務局',
           '家屋番号（記載不要）', '主である建物又は附属建物', '①種類', '②構造', '③床面積', '原因及びその日付',
           '解体移転の場合有・無', 'えい行移転の場合有・無']:
    ok = n_ in sheet[0]
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[答案用紙p1] 印刷 : {n_}')
for n_ in ['登録免許税', '課税価格', '添付情報', '登記原因及びその日付']:
    ok = n_ not in sheet[0]
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[答案用紙p1] 欄なし : {n_}')
ok = sheet[0].count('（略）') == 2 and sheet[0].count('（記載不要）') == 1   # 代理人の（略）が2件分、記載不要は第3欄だけ
ng += (not ok)
print(('OK ' if ok else 'NG ') + '[答案用紙p1] 「（略）」は代理人の2か所、「（記載不要）」は第3欄の家屋番号だけ')
# 代理人 → 申請の日付と提出先 の順（R2は代理人の下に日付の行）
ok = sheet[0].count('代理人（略）令和2年10月16日申請Ａ地方法務局所在建物の表示') == 2
ng += (not ok)
print(('OK ' if ok else 'NG ') + '[答案用紙p1] 申請の日付と提出先の行は代理人の下')
# 2ページ目：第4欄（左半分が各階平面図、右半分が建物図面）
for n_ in ['第4欄', '各階平面図', '家屋番号（略）', '建物図面', '建物の所在', '作成者（略）', '（令和2年○月○日作成）', '申請人（略）']:
    ok = n_ in sheet[1]
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[答案用紙p2] 印刷 : {n_}')
ok = sheet[1].count('（略）') == 3 and '縮尺1250' in sheet[1] and '縮尺1500' in sheet[1]
ng += (not ok)
print(('OK ' if ok else 'NG ') + '[答案用紙p2] 「（略）」は家屋番号・作成者・申請人の3か所、縮尺は1/250（各階平面図）と1/500（建物図面）')
# 作図・申請書の画像がその形どおりか
for n_ in ["'家 屋 番 号'", "txt(283.2, 276.3, '（略）'", "'建物の所在'", "'申 請 人'", "'作 成 者'", "'第4欄'",
           "'（令和2年○月○日作成）'", 'FR_L, FR_R, FR_B, FR_T = 80.5, 382.3, 40.5, 271.4', 'MID = 231.3',
           'return M(287.0 + 2 * e, 165.0 + 2 * n)', 'return M(x0 + 4 * p.imag, y0 + 4 * p.real)',
           "'各　階　平　面　図'", "'建　物　図　面'", '1枚の枠の左半分が各階平面図、右半分が建物図面']:
    check('作図スクリプト（答案用紙の第4欄の形）', n_, drw, '作図')
absent('作成日の仮の印刷', '令和何年何月何日', drw, '作図')
absent('家屋番号を空欄とする古い形', '家屋番号は空欄', drw, '作図')
for n_ in ['③床面積<br><span class="m2">m²</span>', '（記載不要）', '代　　理　　人', '令和２年10月16日　申請　Ａ地方法務局']:
    check('申請書の画像（答案用紙の印刷）', n_, mkp, '申請書')
absent('床面積の見出しの古い形', '③床　面　積<br>（m²）', mkp, '申請書')
for name_ in ['R2_dai22mon_toukishinseisho_kansei_toi1', 'R2_dai22mon_toukishinseisho_kansei_toi3', 'R2_dai22mon_toukishinseisho_machigai']:
    h_ = open(os.path.join(ZU, name_ + '.html'), encoding='utf-8').read()
    ok = '③床面積<br><span class="m2">m²</span>' in h_ and '登録免許税' not in h_
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{name_}.html : 床面積の見出しが答案用紙どおり・登録免許税の欄なし')
check('記事：家屋番号は（略）', '家屋番号と申請人は「（略）」と印刷')
check('記事：作成者の印刷', '作成者は「（略）」「（令和2年○月○日作成）」と印刷')
absent('記事：家屋番号を空ける', '空けておくの')
for src_, nm_ in [(text, '記事'), (fig, '解説図'), (form, '申請書'), (fix, '添削'), (drw, '作図'), (mkp, '申請書スクリプト')]:
    for w_ in ['仮のもの', '仮の形', 'リポジトリにない', '手元になかった']:
        absent('仮の文言', w_, src_, nm_)
check('図11の点線', '(0, 4.2)→(0, 6)→(4.1, 6)', fig, '解説図')
check('図11の求積表', '3階／4.10×4.20＝17.2200／7.80×6.00＝46.8000／計　64.0200／床面積　64.02㎡', fig, '解説図')
check('第1欄の画像の注', '不動産登記法第76条の5。令和3年の改正で新設され、出題当時はなかった', form, '申請書')

# ---- 2026-10-08 最新の執筆プロンプトでの照らし直し：わなごとの図、注の仕分け、第4欄を試験の答案用紙の寸法・縮尺で ----
check('注の仕分けの会話', '注は3系統あるの。問題文の注1〜5、〔調査図〕の（注）1〜5、〔平面図〕の（注）1〜9')
check('3階の形の検算', '南の辺は4.10＋7.80＝11.90で北の辺の11.90と、西の辺は4.20＋1.80＝6.00で東の辺の6.00と一致します')
check('各階同型の求積表', '1階・2階は1つの図に『1階・2階（各階同型）』と書けば、求積表も1つでいいわ（床面積は各階71.40平方メートル）')
check('方位は建物図面（規則82条2項）', '方位は建物図面に書くもの（同規則第82条第2項）で、各階平面図には書かない')
check('建物図面の上の大きさ', '図面の上では横24ミリ、縦12.2ミリ')
assert round(12.00 * 1000 / 500, 1) == 24.0 and round(6.10 * 1000 / 500, 1) == 12.2   # 縮尺1/500：1m ＝ 2mm
assert round(11.90 * 4, 1) == 47.6 and round(6.00 * 4, 1) == 24.0                      # 縮尺1/250：1m ＝ 4mm
assert round(4.10 + 7.80, 2) == 11.90 and round(4.20 + 1.80, 2) == 6.00 and round(4.30 + 1.80, 2) == 6.10 and round(4.10 + 7.90, 2) == 12.00
assert round(1.50 + 10.50, 2) == 12.00 and round(2.60 + 3.50, 2) == 6.10                # 1階の〔平面図〕の寸法の合計
# わな（藍子の誤答とトリ先生の訂正）→ その会話の直後の図
TRAPS = [('今の住所は42番地2', 'R2_dai22mon_toukishinseisho_machigai_shinseinin'),
         ('住民票の……住所証明書ですか？', 'R2_dai22mon_toukishinseisho_machigai_tenpu'),
         ('先に住所を直す登記（登記名義人住所変更登記）をしないといけないんじゃ', 'R2_dai22mon_zu03_jyuusho_zentei'),
         ('滅失登記の前に住所変更の登記をしないといけないんですか？', 'R2_dai22mon_zu04_jyuusho_gimuka'),
         ('一番上の行を写して', 'R2_dai22mon_toukishinseisho_machigai_hyouji'),
         ('建物表題部変更登記の申請義務が『有』です！', 'R2_dai22mon_zu05_eikou_iten'),
         ('建物図面にも、南の距離として『3.2』を書けば', 'R2_dai22mon_zu06_shikichi_ichi'),
         ('12.00かける6.10で、73.20平方メートルです！', 'R2_dai22mon_zu08_1kai2kai_kyuuseki'),
         ('全部の寸法から0.10を引けばいいので', 'R2_dai22mon_zu09_3kai_ayamari_hikaku'),
         ('番号の順に『A市B区T町三丁目42番地1、42番地2』です！', 'R2_dai22mon_zu12_shozai_junjo'),
         ('『店舗・共同住宅・居宅』です！', 'R2_dai22mon_zu13_shurui'),
         ('『令和2年9月18日新築』だけです！', 'R2_dai22mon_zu14_zouchiku_heiki')]
order = {n: i for i, (n, _) in enumerate(PNGS)}
for phrase, png in TRAPS:
    pos = text.find(phrase)
    nxt = [m.start() for m in re.finditer(r'^> 【画像挿入】', text, re.M) if m.start() > pos]
    k = len([m for m in re.finditer(r'^> 【画像挿入】', text, re.M) if m.start() < pos])
    ok = pos >= 0 and bool(nxt) and order.get(png) is not None and order[png] >= k and order[png] <= k + 2
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'わなの直後の図 : {phrase[:20]}… → {png}')
print('NG件数:', ng)
