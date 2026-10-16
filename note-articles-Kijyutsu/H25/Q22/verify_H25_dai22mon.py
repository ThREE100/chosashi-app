"""平成25年度 第22問（建物）：記事の数値・計算・付属プロンプト・生成画像・体裁の照合スクリプト。
アガルートの解答例の第1欄・第2欄・第3欄・第4欄（各階平面図の求積・建物図面の距離と所在）と一致することを確認済み
（解答例の日付は、作業の中でだけ本試験の問題文・答案用紙の日付に対応させて照合した。記事・プロンプト・画像は本試験の日付）。
2026-10-02：最新の執筆ルールとの照らし直しで、注の書き分け、建物図面の申請人欄、各階平面図の完成形、本番で解く順番、
画像挿入マーカー14か所と zu/ のPNG14枚の対応、生成したHTMLの記入内容の確認を加えた。
同日、試験の答案用紙の原本（touan_youshi/）を受け取り、欄の名前・順序・印刷（不動産番号の行、添付情報、登録免許税の欄なし、
第4欄の作成者（略）・申請人の欄・縮尺）との照合と、解答例（第1欄・第2欄・第3欄。年だけ読み替え）との項目ごとの照合を加えた。
2026-10-05、記事の本文に対して図が足りないというユーザーの指摘を受け、本文で説明しているのに図がなかった7か所の図
（図2 注の仕分け、図3 解体移転とえい行移転、図4 主である建物の滅失と附属建物、図6 建物の位置の計算、図9 鉄骨柱の測り方、
図15 12番の分筆と所在の変更、図16 形成的登記と報告的登記）を加え、解説図の番号を記事の挿入順に振り直した
（マーカー21か所とPNG21枚。解説図17＋完成形3＋添削1）。
2026-10-16、最新の執筆ルール・チェックリストでの照らし直し（ユーザー指示「記事本文にたいして、必要図がいくつか足りません」）で、
所在の順序の誤り比較図（図8）、第1欄・第2欄の添付情報の当てはめ表（図17・図18）と、欄ごとの添削画像（第2欄の所在・申請人を分け、
第1欄の取り壊した主である建物の床面積・新しい主である建物の原因の欄番号を足して4枚）を加え、解説図の番号を記事の挿入順に振り直した
（マーカー27か所とPNG27枚。解説図20＋完成形3＋添削4）。図9（建物図面）・図14（各階平面図）は答案用紙の第4欄の1枚の枠の寸法と
実際の縮尺で描き直した。まとめのわな→図の対応表（TRAPS）、わなの図の位置、電卓のキー列の実行、画像の題に図番がないこと、
申請書・添削のHTMLに style="height: がないこと、建物の表示の表の列の幅と第4欄の枠の寸法を答案用紙の画像から測って比べる検査を加えた。
実行: python3 note-articles-Kijyutsu/H25/Q22/verify_H25_dai22mon.py"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, area, fmt_num

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_H25_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_H25_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_H25_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_H25_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_H25_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


def clip(poly, a, b):
    """多角形 poly（(Y, X) のリスト）のうち、有向直線 a→b の左側（外積が正）の部分を返す。"""
    def side(p):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    out = []
    for i in range(len(poly)):
        cur, nxt = poly[i], poly[(i + 1) % len(poly)]
        sc, sn = side(cur), side(nxt)
        if sc >= 0:
            out.append(cur)
        if (sc >= 0) != (sn >= 0):
            t = sc / (sc - sn)
            out.append((cur[0] + (nxt[0] - cur[0]) * t, cur[1] + (nxt[1] - cur[1]) * t))
    return out


# ---- 日付（解答例は平成30年に置き換えた版。本試験の日付に戻す）----
for v in ['7月26日に、主である建物と本件取壊建物の解体が完了', '8月5日に、12番の土地が道路拡幅予定線（G-H）で12番1と12番2に分筆',
          '8月18日に、附属建物の増改築が完了', '8月22日に、本件新建物の再築が完了', '答案用紙に印刷されているとおり8月23日']:
    check('本試験の日付（時系列）', v)
for src, name in [(text, '記事'), (fig, '解説図'), (form, '申請書'), (fix, '添削'), (thumb, '見出し画像')]:
    for bad in ['平成30年', '改題', '過去問集']:
        absent('改題の要素・説明を書いていない', bad, src, name)
absent('解答例の誤植（平成26年8月22日新築）を写していない', '平成26年')

# ---- 第1章：解体移転・主である建物の滅失 ----
check('誤答（えい行移転と同じ扱い）', '本件旧建物の所在を変える建物表題部変更登記です！')
check('解体移転（準則第85条第1項）', '解体移転は、既存の建物が滅失して新たな建物が建築されたものとして扱う（同条第1項）')
check('えい行移転（同条第2項）', '所在の変更として扱うのは、えい行移転だけ（同条第2項）')
check('誤答（滅失登記）', '12番の1は建物滅失登記です！')
check('主である建物の滅失（準則第102条）', '登記記録への書き方まで、準則第102条に載っているわ')
check('3種類の登記', '問1は建物表題部変更登記、問2は建物表題登記、問3は建物滅失登記')

# ---- 第2章：敷地（座標成果）・辺長（F-789SGの複素数モード）----
A, B, C, D = P(39.24, 73.39), P(39.24, 93.96), P(21.64, 94.91), P(27.15, 74.86)
E, F, G, H = P(17.07, 95.16), P(17.07, 76.09), P(39.24, 66.57), P(17.07, 66.57)
for lab, z in [('BC', C - B), ('CD', D - C), ('DA', A - D), ('CE', E - C), ('FD', D - F)]:
    q_, p_ = {'BC': 'CB', 'CD': 'DC', 'DA': 'AD', 'CE': 'EC', 'FD': 'DF'}[lab]
    s = f'- {lab}：`[Abs] [ALPHA] [{q_}] [−] [ALPHA] [{p_}] [)] [=]` で、表示 {fmt_num(abs(z))}（{abs(z) + 1e-12:.2f}）'
    check('辺長（表示・丸め）', s)
assert round(abs(B - A), 2) == 20.57 and round(abs(F - E), 2) == 19.07
check('A点の記憶', '`39.24 [+] 73.39 [i] [SHIFT] [STO] [A]`')
check('辺長は作図用', 'この辺長は作図のチェック用。建物図面には書かないのよ')
check('斜めの辺', '西の辺A-D-Fも東の辺B-C-Eも、南へ行くほど東へずれる斜めの線です')
assert A.imag < D.imag < F.imag and B.imag < C.imag < E.imag       # 南へ行くほど東（Yが大きい）

# ---- 第2章：本件新建物の位置と所在（10番にかかる）----
nX_ext = round(39.24 - 2.60, 2)            # 北の外壁（注4：距離は外壁まで）
nX = round(nX_ext - 0.10, 2)               # 壁の中心線（注5・注6：柱の中心からの測定値、壁厚20cm）
sX = round(nX - 10.92, 2)                  # 1階の西側の南の壁の中心線
assert (nX_ext, nX, sX) == (36.64, 36.54, 25.62) and round(D.real - sX, 2) == 1.53
sX_ext = round(sX - 0.10, 2)
dfY = 74.86 + (27.15 - sX_ext) * 1.23 / 10.08      # 南西の角の高さ（外壁 X＝25.52）でのD-F線のY
wY_ext, wY = dfY + 2.56, dfY + 2.56 + 0.10
assert round(dfY, 2) == 75.06 and round(wY_ext, 2) == 77.62 and round(wY, 2) == 77.72
dcX_at_w = 27.15 - (round(wY, 2) - 74.86) * 5.51 / 20.05
dcY_at_s = 74.86 + (27.15 - sX) * 20.05 / 5.51
assert round(dcX_at_w, 2) == 26.36 and round(dcX_at_w - sX, 2) == 0.74
assert round(dcY_at_s, 2) == 80.43 and round(dcY_at_s - round(wY, 2), 2) == 2.71
# 1階の多角形（壁の中心線、敷地の座標 (Y, X)）を D-C で切って、10番側・11番側の面積を出す
local1 = [(0, 0), (8.19, 0), (8.19, 0.91), (10.92, 0.91), (10.92, 0), (14.56, 0), (14.56, 9.1), (10.01, 9.1), (10.01, 10.92), (0, 10.92)]
site1 = [(round(round(wY, 2) + y, 2), round(nX - x, 2)) for y, x in local1]
Dyx, Cyx = (74.86, 27.15), (94.91, 21.64)
on11 = poly_area(clip(site1, Dyx, Cyx))                                # (Y, X) の順なので D→C の「左側」が北（11番）
on10 = poly_area(clip(site1, Cyx, Dyx))                                # C→D の「左側」が南（10番）
assert round(on10, 1) == 1.0 and round(on11, 1) == 147.2 and on11 > on10, (on10, on11)
local2 = [(3.64, 0), (14.56, 0), (14.56, 10.92), (3.64, 10.92)]
site2 = [(round(round(wY, 2) + y, 2), round(nX - x, 2)) for y, x in local2]
assert poly_area(clip(site2, Cyx, Dyx)) == 0                         # 2階は全部11番の上
check('誤答（11番地だけ）', 'だから所在は『C市D町一丁目11番地』です！')
check('概略図の注1', '『概略図は、現地調査を行った際に、簡易に作成したもの』')
check('D-Cの線は描かれていない', '10番と11番の境のD-Cの線は、概略図のどこにも描かれていないの')
check('距離（外壁まで）', '北の道路との境から北西の角と北東の角まで2.60、西の12番1との境から南西の角まで2.56です。別紙1の（注）4で、全部外壁までの距離です')
check('柱の両面被覆・壁厚', '見取図の寸法は壁の中心線の寸法で、外壁は壁の中心線から0.10外側ですね')
check('北の外壁と南の壁', '39.24−2.60＝36.64。壁の中心線は、その0.10内側で36.54。1階の西側の部分は南北10.92だから、南の壁の中心線は36.54−10.92＝25.62です')
check('D点との差', 'D点のX座標は27.15。南の壁は、D点より1.53メートルも南にあります！')
check('西の壁', '南西の角の高さで、D-Fの線はY＝約75.06。西の外壁は約77.62、壁の中心線は約77.72です')
check('D-C線の高さ', 'X＝27.15−（77.72−74.86）×5.51÷20.05＝27.15−0.785…で、約26.36')
assert fmt_num((77.72 - 74.86) * 5.51 / 20.05, 3) == '0.785…'
check('南西の角が10番', '南の壁の中心線は25.62だから、D-Cの線より約0.74南です。建物の南西の角が、10番の土地に入っています！')
check('D-Cと南の壁の交点', 'Y＝74.86＋（27.15−25.62）×20.05÷5.51＝74.86＋5.567…で約80.43。西の壁の中心線から約2.71東です')
assert fmt_num((27.15 - 25.62) * 20.05 / 5.51, 3) == '5.567…'
check('10番にかかる面積', '東西約2.71、南北約0.74の直角三角形で、約1.0平方メートル。残りの約147.2平方メートルは11番の上です')
check('2階は11番', '西の端が1階より3.64東にあるので、全部11番の上です')
check('所在の順序の誤答（地番の順）', 'じゃあ所在は、地番の順に『C市D町一丁目10番地、11番地』です！')
check('所在の順序（準則第88条第2項）', '2筆以上の土地にまたがる建物は、床面積の多い部分がある土地の地番を先に書くの（不動産登記事務取扱手続準則第88条第2項）')
check('所在の順序（正答）', '11番の上が約147.2平方メートル、10番の上は約1.0平方メートルです。所在は『C市D町一丁目11番地、10番地』です')
check('建物図面の記載事項', '方位、縮尺、敷地の地番と形、隣接地の地番です（不動産登記規則第82条第2項）。縮尺は問題文の注3で500分の1')
check('隣接地の地番', '北が道路の51、東が9-1、南が16-1、南西の角の先が15-1、西が12-1です')
check('分筆後の地番', '西隣は『12』じゃなく『12-1』')
check('家屋番号は空欄', '家屋番号の欄は、登記官が付けるので空欄です')

# ---- 第3章：各階平面図・床面積 ----
check('柱の外面の誤答', '鉄骨造だから、柱の外面で測るんですよね')
check('両面被覆＝中心線', '両面なら、柱の中心線が壁の中心線です。床面積は壁その他の区画の中心線で囲まれた部分で測る（不動産登記規則第115条）')
check('天井の高さ', '別紙1の（注）7の天井の高さも2.5メートル以上だから、床面積から除く部分もないわ')
assert round(8.19 + 2.73 + 3.64, 2) == 14.56 == round(10.01 + 4.55, 2) and round(9.10 + 1.82, 2) == 10.92
check('1階の閉合', '北は8.19＋2.73＋3.64＝14.56、南は10.01＋4.55＝14.56で一致。東は9.10＋1.82＝10.92で、西の10.92と一致です')
assert round(10.01 - 8.19, 2) == 1.82 and round(10.92 - 0.91, 2) == 10.01 and round(10.92 - 10.01, 2) == 0.91 and round(9.10 - 0.91, 2) == 8.19
rects1 = [(8.19, 10.92), (1.82, 10.01), (0.91, 8.19), (3.64, 9.10)]
parts = [round(a * b, 4) for a, b in rects1]
a1 = round(sum(parts), 4)
assert parts == [89.4348, 18.2182, 7.4529, 33.124] and a1 == 148.2299 == round(poly_area(local1), 4) == round(poly_area(site1), 4)
assert trunc2(a1) == 148.22
check('1階 求積表', '- 8.19 × 10.92 ＝ 89.4348\n- 1.82 × 10.01 ＝ 18.2182\n- 0.91 × 8.19 ＝ 7.4529\n- 3.64 × 9.10 ＝ 33.1240\n- 合計：148.2299 （床面積：148.22平方メートル）')
assert round(14.56 * 10.92 - 2.73 * 0.91 - 4.55 * 1.82, 4) == 148.2299
check('1階の検算（全体から引く）', '14.56×10.92＝158.9952から、北の欠け2.73×0.91＝2.4843と、南東の欠け4.55×1.82＝8.2810を引いて、148.2299')
a2 = round(10.92 * 10.92, 4)
assert a2 == 119.2464 == round(poly_area(local2), 4) and trunc2(a2) == 119.24
check('2階 求積表', '- 10.92 × 10.92 ＝ 119.2464\n- 合計：119.2464 （床面積：119.24平方メートル）')
check('2階の誤答（北西の角）', '北西の角を1階の北西の角に合わせて描きます！')
check('丸印（注9）', '2階も、北東の角と、東の辺を北から9.10下りた点に丸印があります')
check('2階の西の端', '2階の西の端は、1階の西の端から14.56−10.92＝3.64東')
check('張り出しも床面積', '張り出した部分も、壁と床と天井で囲まれた2階の部屋よ')
check('1階の位置の点線', '（不動産登記規則第83条第1項、不動産登記事務取扱手続準則第53条）')
check('切り捨て', '148.2299は148.22、119.2464は119.24です（不動産登記規則第115条）')

# ---- 第4章：問1（第1欄）----
assert round(22.50 / 4.50, 2) == 5.00 and round(8.50 - 5.00, 2) == 3.50 and round(4.50 * 8.50, 4) == 38.25
check('附属建物の増築', '22.50÷4.50＝5.00だから、元は南北5.00で、概略図の斜線の部分のとおり南へ3.50延ばしたんですね')
check('種類（店舗）', '不動産登記規則第113条第1項の区分の『店舗』に当たります')
check('所在の変更', '変更後の所在は『C市D町一丁目12番地1』。原因は『平成25年8月5日分筆により変更』です')
check('所在の変更の申請義務', '（不動産登記法第51条第1項）')
check('一の申請情報', '（不動産登記規則第35条第6号）')
check('家屋番号は登記官', '（不動産登記事務取扱手続準則第79条第10号）。申請書には今の家屋番号『12番の1』を書けばいいわ')
check('登記記録に床面積がない', '別紙2の登記記録の抜粋に、主である建物の床面積が載っていません')
check('1行目', '1階148.22平方メートル、2階119.24平方メートル。原因は『平成25年7月26日取壊し』です')
check('2行目', '種類は店舗、構造は鉄骨造陸屋根平家建、床面積38.25平方メートル。原因は『平成25年7月26日主である建物に変更、平成25年8月18日種類変更、増築』です')
check('主である建物に変わった日', '主である建物の取壊しが完了して、主である建物がいなくなった日だからです')
check('欄番号を付けない理由', '前の行の値のうちどの欄だけが変わったかを示す行じゃないから、欄番号は付けないの')
check('3行目', '物置、鉄骨造陸屋根平家建、22.50平方メートル。原因は『平成25年7月26日主である建物に変更』')
check('問1 登記の目的', '登記の目的は『建物表題部変更登記』')
check('持分は書かない', '表題部の変更の登記に持分は書かないわ')
check('持分の根拠', '（不動産登記令第3条第9号）')
check('問1 添付情報', '添付情報は、建物図面、各階平面図、所有権証明情報、代理権限証明情報です')
check('問1 添付情報の根拠', '不動産登記令別表14の項です。所在を変えるときは変更後の建物図面（添付情報欄イ）。床面積を変えるときは変更後の建物図面と各階平面図（同欄ロ（1））')
check('増築部分の所有権証明', '（同欄ロ（2））')
check('代理権限証明情報', '代理権限証明情報（同令第7条第1項第2号）')
check('登録免許税（非課税）', '（登録免許税法別表第一の一（十三））')

# ---- 第5章：問2（第2欄）----
check('問2 建物の表示', '家屋番号は、表題登記では申請情報にしないので空欄です（不動産登記令第3条第8号ロ）')
check('問2 種類・構造・床面積', '種類は倉庫、構造は軽量鉄骨造亜鉛メッキ鋼板ぶき2階建、床面積は1階148.22平方メートル、2階119.24平方メートルです')
check('問2 原因', '『平成25年8月22日新築』。解体が完了した7月26日でも、申請した8月23日でもありません')
check('表題登記の申請義務', '（不動産登記法第47条第1項）')
check('問2 申請人の誤答（持分なし）', '申請人は、第1欄と同じく『C市D町一丁目3番2号　甲野春男』『C市D町一丁目3番2号　甲野冬子』です！')
check('問2 申請人', '『C市D町一丁目3番2号　持分2分の1　甲野春男』『C市D町一丁目3番2号　2分の1　甲野冬子』')
check('問2 添付情報', '不動産登記令別表12の項の添付情報欄のイからニで、建物図面、各階平面図、所有権証明情報、住所証明情報。それと代理権限証明情報です')
check('所有権証明情報（準則第87条第1項）', '（不動産登記事務取扱手続準則第87条第1項）')

# ---- 第6章：問3（第3欄）----
check('滅失登記の申請義務', '滅失の日から1月以内に申請しなければなりません（不動産登記法第57条）')
check('誤答（共有者全員）', '共有者全員の2人で申請しないといけないと思います')
check('報告的登記⇔形成的登記', '『形成的登記』の考え方よ')
check('報告的登記', '『報告的登記』です！')
check('保存行為', '共有物の保存行為として、共有者の1人が単独でできるの。今の条文でいうと民法第252条第5項よ')
check('過料', '10万円以下の過料（不動産登記法第164条第1項）')
setsumei = '本件取壊建物については、建物滅失登記を申請する必要がある。建物滅失登記は、建物が滅失した事実を登記記録に反映させる報告的登記であり、その申請は共有物の保存行為に当たるから、甲野冬子が関与しなくても、共有者の1人である甲野春男が単独で申請することができる（民法第252条第5項、不動産登記法第57条）。'
check('第3欄の説明文', setsumei)
check('第3欄の説明文', setsumei, form, '申請書')

# ---- 付属プロンプトとの整合（登記申請書等）----
for s in ['**登記の目的**：建物表題部変更登記', '**添付情報**：建物図面　各階平面図　所有権証明情報　代理権限証明情報',
          'Ｃ市Ｄ町一丁目３番２号　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　甲野冬子', '上の段：Ｃ市Ｄ町一丁目12番地',
          '下の段の左：Ｃ市Ｄ町一丁目12番地１', '下の段の右：平成25年８月５日分筆により変更', '左のセル「12番の１」',
          '①種類：「倉庫」', '②構造：「軽量鉄骨造亜鉛メッキ鋼板ぶき２階建」', '③床面積：「1階　148｜22」「2階　119｜24」',
          '登記原因及びその日付：「平成25年７月26日取壊し」', '①種類：「店舗」', '②構造：「鉄骨造陸屋根平家建」', '③床面積：「38｜25」',
          '「平成25年７月26日主である建物に変更、平成25年８月18日種類変更、増築」', '主である建物又は附属建物：「符号１」',
          '①種類：「物置」', '③床面積：「22｜50」', '登記原因及びその日付：「平成25年７月26日主である建物に変更」',
          '**登記の目的**：建物表題登記', '**添付情報**：建物図面　各階平面図　所有権証明情報　住所証明情報　代理権限証明情報',
          'Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　　　２分の１　甲野冬子',
          '上の段：Ｃ市Ｄ町一丁目11番地、10番地', '登記原因及びその日付：「平成25年８月22日新築」',
          '「平成25年8月23日申請　C地方法務局」', '項目名「添　付　情　報」']:
    check('申請書の記入', s, form, '申請書')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')
for s in ['①誤答：所在「Ｃ市Ｄ町一丁目11番地」', '（持分なし）', '③正解：所在「Ｃ市Ｄ町一丁目11番地、10番地」',
          '「Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男」', '令3条9号', '準則88条2項', '準則102条',
          '③床面積に赤字で「1階　148｜22」「2階　119｜24」', '頭の「①③」に赤の取り消し線', '欄ごとに1枚']:
    check('添削', s, fix, '添削')

# ---- 解説図プロンプトの頂点座標（面積を計算して求積表・地積と一致させる）----
lot11 = [(73.39, 39.24), (93.96, 39.24), (94.91, 21.64), (74.86, 27.15)]
lot10 = [(74.86, 27.15), (94.91, 21.64), (95.16, 17.07), (76.09, 17.07)]
lot12_1 = [(66.57, 39.24), (73.39, 39.24), (74.86, 27.15), (76.09, 17.07), (66.57, 17.07)]
assert round(poly_area(lot11), 4) == round(area([A, B, C, D]), 4) == 298.1684
assert round(poly_area(lot10), 4) == round(area([D, C, E, F]), 4) == 141.2383
tri10 = [(77.72, 26.36), (77.72, 25.62), (80.43, 25.62)]
assert round(poly_area(tri10), 1) == 1.0
F2_wrong = [(0, 0), (10.92, 0), (10.92, 10.92), (0, 10.92)]
AN0 = [(0, 0), (4.5, 0), (4.5, 5), (0, 5)]
AN1 = [(0, 0), (4.5, 0), (4.5, 8.5), (0, 8.5)]
lot12 = [(58.57, 39.24), (73.39, 39.24), (74.86, 27.15), (76.09, 17.07), (58.57, 17.07)]      # 図16：西の辺 Y＝58.57 は模式
lot12_2 = [(58.57, 39.24), (66.57, 39.24), (66.57, 17.07), (58.57, 17.07)]
assert abs(poly_area(lot12) - poly_area(lot12_1) - poly_area(lot12_2)) < 1e-9          # 12番＝12番1＋12番2（G-Hで分筆）
figs = [('図5 11番', lot11, 298.1684), ('図5 10番', lot10, 141.2383), ('図5・図16 12番1', lot12_1, poly_area(lot12_1)),
        ('図16 12番（分筆の前）', lot12, poly_area(lot12)), ('図16 12番2', lot12_2, poly_area(lot12_2)),
        ('図6・図7・図9 1階（敷地の座標）', site1, 148.2299), ('図6・図7 10番に入る三角形', tri10, poly_area(tri10)),
        ('図11 1階', local1, 148.2299), ('図12左 誤り', F2_wrong, 119.2464), ('図12右・図13 2階', local2, 119.2464),
        ('図15 工事前', AN0, 22.5), ('図15 工事後', AN1, 38.25)]
for label, pts, want in figs:
    assert round(poly_area(pts), 4) == round(want, 4), label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    if '10番に入る三角形' in label:
        s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts)
    check(label + ' 頂点座標', s, fig, '解説図')
for s in ['AB「20.57」、BC「17.63」、CD「20.79」、DA「12.18」、CE「4.58」、EF「19.07」、FD「10.15」',
          '「2.60」「2.60」「2.56」', '建物の所在」「C市D町一丁目11番地、10番地」', '「3.64」', '「1.53」',
          '1階 床面積：148.22㎡（8.19×10.92＋1.82×10.01＋0.91×8.19＋3.64×9.10＝148.2299）',
          '2階 床面積：119.24㎡（10.92×10.92＝119.2464）', '物置　4.50×5.00＝22.50㎡', '店舗　4.50×8.50＝38.25㎡',
          '増築部分　4.50×3.50＝15.75㎡', '約1.0㎡が10番', '約147.2㎡が11番', '8月5日「12番を12番1・12番2に分筆」']:
    check('図の数値', s, fig, '解説図')
check('向き（北の欠け・南東の欠け）', '北の辺の真ん中に欠け（Y：8.19〜10.92、X：0〜0.91）、南東の角に欠け（Y：10.01〜14.56、X：9.10〜10.92）', fig, '解説図')
check('向き（2階は東にそろう）', 'Y：3.64〜14.56、X：0〜10.92 の正方形（1階の東の辺にそろう）', fig, '解説図')
check('向き（増築は南）', '南の増築部分（Y：0〜4.5、X：5〜8.5）', fig, '解説図')
check('本文の向き（増築は南）', '南へ3.50延ばした')
for bad in ['PDF', '創設的登記', '名変', '✕', '✓', '右上', '左下', '右側', '左側', '四捨五入して']:
    absent('誤記・混入', bad)
# 「10番地、11番地」は藍子の誤答・まとめの対比と図の説明だけに出る（正しい答えとして書いていない）
ok = text.count('10番地、11番地') == 2 and '地番の順に『C市D町一丁目10番地、11番地』です！' in text
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'「10番地、11番地」は誤答・誤りの図の説明にだけある（{text.count("10番地、11番地")}か所）')

# ---- note向けの体裁：話者名の行末に半角スペース2つ、名前とセリフの間に空行なし ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
prev = None
same_speaker = []
for i, line in enumerate(lines):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        if line == prev:
            same_speaker.append(i + 1)
        prev = line
ng += bool(same_speaker)
print(('OK ' if not same_speaker else 'NG ') + f'同じ話者の連続（画像挿入マーカー・箇条書きをはさむ場合も）: {same_speaker}')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# ---- 画像（2026-10-02追加）：記事の画像挿入マーカー（2026-10-05に21か所）と zu/ のPNGが、記事の順に対応しているか ----
from PIL import Image
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('H25_dai22mon_zu01_jikeiretsu', '時系列と、3つの建物それぞれの行き先', (1600, 1050)),
        ('H25_dai22mon_zu02_chuu_shiwake', '注の仕分け図', (1600, 1250)),
        ('H25_dai22mon_zu03_kaitai_eikou_hikaku', '解体移転とえい行移転の誤り比較図', (1600, 1050)),
        ('H25_dai22mon_zu04_shu_messhitsu_fuzoku', '主である建物の滅失と附属建物の誤り比較図', (1800, 1050)),
        ('H25_dai22mon_zu05_shikichi_henchou', '敷地の辺長確認図', (1600, 1250)),
        ('H25_dai22mon_zu06_tatemono_ichi_keisan', '本件新建物の位置を出す計算の手順の図', (1800, 1200)),
        ('H25_dai22mon_zu07_shozai_ayamari_hikaku', '概略図の見た目', (1800, 1050)),
        ('H25_dai22mon_zu08_shozai_junjo', '所在の順序の誤り比較図', (1600, 1000)),
        ('H25_dai22mon_toukishinseisho_machigai_shozai', '第2欄の「所在」の①誤答', 'tall'),
        ('H25_dai22mon_zu09_tatemono_zumen', '建物図面の完成形（答案用紙の第4欄の建物図面の枠の中）', 'sheet'),
        ('H25_dai22mon_zu10_hashira_hikaku', '鉄骨柱の測り方の誤り比較図', (1600, 1050)),
        ('H25_dai22mon_zu11_1kai_kyuuseki', '本件新建物1階の求積図', (1600, 1200)),
        ('H25_dai22mon_zu12_2kai_ayamari_hikaku', '北西の角で1階に合わせた2階（誤り）', (1600, 1000)),
        ('H25_dai22mon_zu13_2kai_kyuuseki', '本件新建物2階の求積図', (1600, 1200)),
        ('H25_dai22mon_zu14_kakukai_heimenzu', '各階平面図の完成形（答案用紙の第4欄の各階平面図の枠の中', 'sheet'),
        ('H25_dai22mon_zu15_fuzoku_zoukaichiku', '附属建物の増改築の前後比較図', (1600, 1000)),
        ('H25_dai22mon_zu16_bunpitsu_shozai', '12番の分筆と所在の変更の図', (1600, 1100)),
        ('H25_dai22mon_toukishinseisho_machigai_yukamenseki', '取り壊した主である建物の行の③床面積の①誤答', 'tall'),
        ('H25_dai22mon_toukishinseisho_machigai_genin', '新しい主である建物（店舗）の行の「登記原因及びその日付」の①誤答', 'tall'),
        ('H25_dai22mon_zu17_tenpu_dai1ran', '第1欄の添付情報の当てはめ表', (1600, 1200)),
        ('H25_dai22mon_dai1ran_kansei', '問1（第1欄）の完成した登記申請書', 'tall'),
        ('H25_dai22mon_toukishinseisho_machigai_shinseinin', '第2欄の「申請人」の①誤答', 'tall'),
        ('H25_dai22mon_zu18_tenpu_dai2ran', '第2欄の添付情報の当てはめ表', (1600, 1200)),
        ('H25_dai22mon_dai2ran_kansei', '問2（第2欄）の完成した登記申請書', 'tall'),
        ('H25_dai22mon_zu19_keiseiteki_houkokuteki', '形成的登記と報告的登記の比較図', (1600, 1050)),
        ('H25_dai22mon_dai3ran_kansei', '問3（第3欄）の完成した説明文', 'wide'),
        ('H25_dai22mon_zu20_toku_junban', '本番で解く順番', (1600, 800))]
ok = len(markers) == len(PNGS) == 27
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}（解説図20＋添削4＋完成形3）')
for (name, key, size), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        if size == 'sheet':     # 第4欄の枠の画像：用紙の範囲（横38〜367mm・縦14〜282mm）と同じ縦横比（横2200px）
            ok = w == 2200 and abs(h / w - (282.0 - 14.0) / (367.0 - 38.0)) < 0.01
        else:
            ok = (w == 1200 and h > w) if size == 'tall' else (w == 1200 and h < w) if size == 'wide' else (w, h) == size
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'PNG（マーカー順・大きさ） : {name}')
    src = fig if '_zu' in name else (form if 'kansei' in name else fix)
    ok = f'zu/{name}.png' in src
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'プロンプトにファイル名 : zu/{name}.png')
# 2026-10-05に加えた図（図2・図3・図4・図6・図10・図16・図19。番号は2026-10-16の振り直し後）：記事の会話・プロンプト・作図スクリプトの文言と数値が一致するか
check('注の仕分けの受け答え（同じ話者を続けない）', '問題文の注は答案を作るときの前提と決まり、別紙1の（注）は概略図と見取図の読み方なんですね')
check('注の仕分けの後の問い', 'そう。じゃあ最初の関門。主である建物は、同じ建材で、同じ形のまま、隣の土地に建て直したのよね')
draw_ = open(os.path.join(ZU, 'draw_H25_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
NEW_FIGS = {
    '図2': ['建物図面は500分の1、各階平面図は250分の1', '概略図は、現地調査のときに簡易に作成したもの', '概略図の敷地境界からの距離は、全部外壁まで',
           '鉄骨柱の両面は被覆、測定値は柱の中心から', '壁厚は全て20センチ', '天井までの高さは全て2.5メートル以上', '見取図1の丸印は、各階の重なる部分',
           '同じ「3」でも別の注', '数値の単位は全てメートル'],
    '図3': ['誤り：本問をえい行移転と同じに扱う', '正しい：解体移転（本問）', '所在の変更として扱う（準則第85条第2項）',
           '既存の建物の滅失と、新たな建物の建築（準則第85条第1項）', '本件新建物は新築 → 建物表題登記（問2）', '解体した上でその建材を用いて隣地に再築'],
    '図4': ['家屋番号12番の1（本件旧建物）', '家屋番号12番の2（本件取壊建物）', '7月26日取壊し', '附属建物を主である建物に変更',
           '「主である建物に変更」（準則第102条）', '建物滅失登記（不動産登記法第57条）'],
    '図6': ['①2.60', '②10.92', '②1.53', '③2.56', '④約0.74', '④約2.71', '北の道路境界 X＝39.24', '北の外壁 X＝36.64', '壁の中心線 X＝36.54',
           '南の壁の中心線 X＝25.62', 'D点 X＝27.15', 'D-Fの線 Y＝約75.06', '西の外壁 Y＝約77.62', '壁の中心線 Y＝約77.72', 'D-Cの線 X＝約26.36',
           '交点 Y＝約80.43', '約1.0㎡が10番', '残り約147.2㎡が11番'],
    '図10': ['誤り：外側だけ被覆と思い、柱の外面で測る', '正しい：両面被覆なので、柱の中心線で測る', '柱の中心線＝壁の中心線', '（測定値8.19・10.92はここから）',
           '外壁（中心線から0.10外側）', '壁厚0.20', '柱の中心から（別紙1の（注）5）', '（不動産登記規則第115条）'],
    '図16': ['道路拡幅予定線（G-H）', '分筆線（G-H）', '本件旧建物の所在：C市D町一丁目12番地', '本件旧建物の所在：C市D町一丁目12番地1',
            '平成25年8月5日分筆により変更', '（不動産登記事務取扱手続準則第79条第10号）', '12番2の西の端と附属建物の位置は模式'],
    '図19': ['誤り：共有物の登記だから共有者全員で', '正しい：滅失登記は報告的登記', '形成的登記の考え方', '合併・分割のように',
            '共有物の保存行為（民法第252条第5項）', '共有者の1人（甲野春男）が単独で申請できる', '（同法第164条第1項）'],
}
for zu_, words in NEW_FIGS.items():
    for w_ in words:
        w2 = w_.replace('「', '『').replace('」', '』')
        ok = (w_ in draw_) and (w_ in fig or w2 in fig)
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'追加した図（作図スクリプトとプロンプト）[{zu_}] : {w_}')
# 図6の数値は本文の会話と同じか
for w_ in ['39.24−2.60＝36.64', '36.54−10.92＝25.62', '1.53メートルも南', '約75.06', '約77.62', '約77.72', '約26.36', '約0.74南', '約80.43',
           '約2.71東', '約1.0平方メートル', '約147.2平方メートル']:
    check('図6の数値が本文にある', w_)
# 図16の所在・原因・家屋番号は本文の会話と同じか
for w_ in ['『C市D町一丁目12番地1』', '『平成25年8月5日分筆により変更』', '（不動産登記事務取扱手続準則第79条第10号）', '今の家屋番号『12番の1』']:
    check('図16の内容が本文にある', w_)
# 固定配置の図も機械で重なりを調べている
for w_ in ['def check_fixed(', "check_fixed(fig, 'H25_dai22mon_zu01_jikeiretsu')", "check_fixed(fig, 'H25_dai22mon_zu20_toku_junban')",
           "save_fixed(fig, 'H25_dai22mon_zu02_chuu_shiwake')", "save_fixed(fig, 'H25_dai22mon_zu19_keiseiteki_houkokuteki')",
           "save_fixed(fig, 'H25_dai22mon_zu08_shozai_junjo')", 'save_fixed(fig, name)', "'H25_dai22mon_zu17_tenpu_dai1ran'",
           "'H25_dai22mon_zu18_tenpu_dai2ran'"]:
    check('固定配置の図の重なり検査', w_, draw_, '作図')
# 作図スクリプトの書き出し順が記事の挿入順（図1〜図20）
order = re.findall(r"^    (zu\d\d)\(\)$", draw_.split("if __name__ == '__main__':")[1], re.M)
ok = order == [f'zu{i:02d}' for i in range(1, 21)]
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図スクリプトの書き出し順（図1〜図20） : {order}')
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
ok = not extra
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'zu/ に記事で使わないPNGがない : {extra}')


def html_has(name, *needles):
    global ng
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        ok = n in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : {n}')


html_has('H25_dai22mon_dai1ran_kansei', '本件旧建物に関する登記の申請書', '建物表題部変更登記',
         '建物図面　各階平面図　所有権証明情報　代理権限証明情報', '平成25年８月23日申請　　Ｃ地方法務局',
         'Ｃ市Ｄ町一丁目３番２号　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　甲野冬子', 'Ｃ市Ｄ町一丁目12番地<', 'Ｃ市Ｄ町一丁目12番地１',
         '平成25年８月５日分筆により変更', '12番の１', '>主<', '>倉庫<', '1階　148', '2階　119', '>22<', '>24<',
         '平成25年７月26日取壊し', '>店舗<', '>38<', '>25<', GENIN_SHU := '平成25年７月26日主である建物に変更、平成25年８月18日種類変更、増築',
         '符号１', '>物置<', '>50<', '平成25年７月26日主である建物に変更</span>', '（略）')
html_has('H25_dai22mon_dai2ran_kansei', '本件新建物に関する登記の申請書', '>建物表題登記<', '所有権証明情報　住所証明情報',
         'Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　　　２分の１　甲野冬子',
         'Ｃ市Ｄ町一丁目11番地、10番地', '平成25年８月22日新築', '1階　148', '2階　119')
html_has('H25_dai22mon_dai3ran_kansei', '第3欄　土地家屋調査士民事花子の説明', setsumei)
for nm_, words_ in [('shozai', ['、10番地', '準則88条2項', 'Ｃ市Ｄ町一丁目11番地、10番地', '所　　在']),
                    ('shinseinin', ['持分２分の１', '令3条9号', 'Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男', '申　請　人']),
                    ('yukamenseki', ['148', '119', '平成25年７月26日取壊し', '事実関係1', '③床面積']),
                    ('genin', ['①③平成25年７月26日主である建物に変更', 'class="red strike">①③', '準則102条', '>店舗<'])]:
    html_has('H25_dai22mon_toukishinseisho_machigai_' + nm_, '①誤答', '②添削（赤ペン）', '③正解', *words_)
for name in ['H25_dai22mon_dai1ran_kansei', 'H25_dai22mon_dai2ran_kansei']:
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    ok = '登録免許税' not in h and '添付書類' not in h
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{name}.html : 登録免許税の欄を描き足していない・欄名は「添付情報」')
h1 = open(os.path.join(ZU, 'H25_dai22mon_dai1ran_kansei.html'), encoding='utf-8').read()
ok = '持分' not in h1
ng += (not ok)
print(('OK ' if ok else 'NG ') + '第1欄（表題部変更登記）の申請人に持分を書いていない')
draw = open(os.path.join(ZU, 'draw_H25_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
for n in ['甲野春男　甲野冬子', "'250'", "'500'", '（平成何年何月何日作成）', 'C市D町一丁目11番地、10番地', 'pad_aspect=True']:
    check('作図スクリプト（第4欄の枠）', n, draw, '作図')

# ---- 最新ルールとの照らし直しで足した会話（2026-10-02）----
check('注の仕分け', '問題文の最後の注1から注4と、別紙1の最後、各階平面見取図2の下にある（注）1から9です')
check('注の仕分け（言い分け）', '番号がかぶるから、『問題文の注3』『別紙1の（注）4』と、どちらの注かを必ず言い分けるのよ')
check('建物図面の申請人欄', '申請人の欄には（略）と印刷されていないので、空けずに『甲野春男　甲野冬子』と2人の氏名を書きます。図面には申請人が記名することになっています（不動産登記規則第74条第2項）')
check('各階平面図の完成形', '縮尺は問題文の注3で250分の1。1メートルが4ミリだから、1階の東西14.56は約58ミリ、南北10.92は約44ミリです。『1階』『2階』と書き分けて、外まわりの辺に壁の中心線の寸法を書きます')
check('解く順番（時間を食うところ）', '座標から建物の位置を出してD-Cの線との関係を確かめるところと、第4欄の作図です')
check('解く順番（所在は空けておく）', '第2欄の所在は、手順3では空けておくんですね')
for n in ['1. 問1から問4・別紙・注を読み', '2. 第3欄の説明文を書く（計算なし）', '3. 第1欄・第2欄のうち、床面積と第2欄の所在以外の欄を埋める',
          '4. 1階・2階を求積し（148.22・119.24）', '5. 座標で建物の位置を出し、D-Cの線を引いて所在を決め', '6. 第4欄の建物図面と各階平面図を描いて、見直す']:
    check('解く順番（手順）', n)
# 注の書き分け：「注N」は「問題文の注N」、「（注）N」は「別紙1の（注）N」（続けて並べる「と（注）6」「・（注）7」は可）
bare = []
SHIWAKE = '問題文の最後の注1から注4と、別紙1の最後、各階平面見取図2の下にある（注）1から9です'   # 2つの注を並べて紹介する文は除く
body_ = text.replace(SHIWAKE, '')
for m in re.finditer(r'（注）\d|注\d', body_):
    i = m.start()
    if m.group().startswith('（'):
        ok_note = body_[max(0, i - 4):i] == '別紙1の' or body_[i - 1] in 'と・'
    else:
        ok_note = body_[max(0, i - 4):i] == '問題文の'
    if not ok_note:
        bare.append(body_[max(0, i - 8):i + 5])
ok = not bare
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'注の書き分け（問題文の注／別紙1の（注））: 書き分けていない箇所 {bare}')

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成25年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成25年度問題22（建物）', thumb, '見出し画像')
for src, name in [(fig, '解説図'), (form, '申請書'), (fix, '添削')]:
    check('記事タイトルの引用', title[2:], src, name)

# ---- 試験の答案用紙の原本（touan_youshi/、2026-10-02受領）との照合 ----
# 原本はテキスト層のない画像PDF（A3横2ページ。1ページ目はPDF上で180°回転）。印刷文字は目で読んで下の表に書き出し、
# 画像（第1欄・第2欄・第3欄・添削・第4欄の枠）の欄の名前・順序・印刷と照らす。これまで欄の形を確かめていた
# public/kijutsu/H25-tatemono/a1.webp・a2.webp が原本と同じものであることも、縮小画像の差で確かめる。
import unicodedata
TY = os.path.join(HERE, 'touan_youshi')
try:
    import pymupdf
    doc = pymupdf.open(os.path.join(TY, 'H25_dai22mon_touan_youshi.pdf'))
    ok = len(doc) == 2 and all(round(pg.rect.width) == 1191 and round(pg.rect.height) == 842 for pg in doc)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '答案用紙の原本：A3横2ページ')
except ImportError:
    print('-- pymupdf がないので原本PDFのページ数の確認は省略')
from PIL import ImageChops, ImageStat
for n in (1, 2):
    a = Image.open(os.path.join(TY, f'H25_dai22mon_touan_youshi_p{n}.png')).convert('L').resize((350, 247))
    b = Image.open(os.path.join(HERE, '..', '..', '..', 'public', 'kijutsu', 'H25-tatemono', f'a{n}.webp')).convert('L').resize((350, 247))
    d = ImageStat.Stat(ImageChops.difference(a, b)).mean[0]
    ok = d < 2.0
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'答案用紙の原本 p{n} と a{n}.webp が同じ用紙（縮小画像の平均差 {d:.2f}）')
# 原本1ページ目（第1欄・第2欄・第3欄）の印刷：見出し・項目の順序
GENPON_P1 = {
    '第1欄': ['本件旧建物に関する登記の申請書', '登記の目的', '添　付　情　報', '平成25年８月23日申請　　Ｃ地方法務局', '申　　請　　人', '代　　理　　人', '（略）',
             '不動産番号', '所　　在', '家屋番号', '主である建物', '又は附属建物', '①種類', '②構造', '③床面積', '登記原因及びその日付'],
    '第2欄': ['本件新建物に関する登記の申請書', '登記の目的', '添　付　情　報', '平成25年８月23日申請　　Ｃ地方法務局', '申　　請　　人', '代　　理　　人', '（略）',
             '不動産番号', '所　　在', '家屋番号', '主である建物', '又は附属建物', '①種類', '②構造', '③床面積', '登記原因及びその日付'],
    '第3欄': ['土地家屋調査士民事花子の説明'],
}
GENPON_NAI = ['登録免許税', '添付書類', '課税価格']        # 原本の第1欄・第2欄にない欄


def strip_tags(h):
    return re.sub(r'<[^>]+>', '', h)


for ran, name in [('第1欄', 'H25_dai22mon_dai1ran_kansei'), ('第2欄', 'H25_dai22mon_dai2ran_kansei'), ('第3欄', 'H25_dai22mon_dai3ran_kansei')]:
    h = strip_tags(open(os.path.join(ZU, name + '.html'), encoding='utf-8').read())
    norm = lambda t: re.sub(r'[\s　]', '', unicodedata.normalize('NFKC', t))
    pos, order_ok = -1, True
    for lab in GENPON_P1[ran]:
        i = norm(h).find(norm(lab), pos + 1)
        if i < 0 or i < pos:
            order_ok = False
            print(f'   NG 欄名がない・順序が違う：{lab}')
        pos = max(pos, i)
    ng += (not order_ok)
    print(('OK ' if order_ok else 'NG ') + f'{name}.html : 原本の{ran}の印刷（見出し・項目名）が原本の順に並ぶ')
    if ran != '第3欄':
        ok = not any(norm(x) in norm(h) for x in GENPON_NAI)
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : 原本にない欄（登録免許税・添付書類・課税価格）を描いていない')
# 記入行が3行（原本の表の記入行は3行）
mk = open(os.path.join(ZU, 'make_H25_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
check('原本の表の形（記入行3行）', '記入行3行', mk, '申請書スクリプト')
check('原本の確かめ（申請書スクリプト）', 'touan_youshi/H25_dai22mon_touan_youshi.pdf', mk, '申請書スクリプト')
check('不動産番号は原本に印刷された行', '不動産番号（試験の答案用紙に印刷されている行。記入は空欄）', mk, '申請書スクリプト')
check('原本の確かめ（申請書プロンプト）', '`touan_youshi/H25_dai22mon_touan_youshi.pdf` の1ページ目', form, '申請書')
check('原本の確かめ（解説図プロンプト）', '`touan_youshi/H25_dai22mon_touan_youshi.pdf` の2ページ目', fig, '解説図')
check('原本の確かめ（作図スクリプト）', 'touan_youshi/H25_dai22mon_touan_youshi.pdf', draw, '作図')
check('原本の確かめ（添削プロンプト）', 'touan_youshi/H25_dai22mon_touan_youshi.pdf', fix, '添削')
h_fix = ''.join(strip_tags(open(os.path.join(ZU, f'H25_dai22mon_toukishinseisho_machigai_{k}.html'), encoding='utf-8').read())
                for k in ('shozai', 'shinseinin', 'yukamenseki', 'genin'))
for lab in ['申　請　人', '所　　在', '（抜粋）']:
    ok = re.sub(r'[\s　]', '', lab) in re.sub(r'[\s　]', '', h_fix)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'添削画像の項目名（原本の第2欄の印刷どおり）: {lab}')
# 原本2ページ目（第4欄）の印刷：家屋番号・建物の所在は1組、作成者は（略）と作成日の印刷あり・縮尺1/250、
# 申請人は（略）の印刷なし・縮尺1/500、「（単位：m）」。図8・図13の枠の印刷と照らす。
for n in ["'家 屋 番 号'", "'建物の所在'", "'申　請　人'", "'作　成　者'", "'（略）'", "'（平成何年何月何日作成）'", "'250'", "'500'", '（単位：m）',
          '甲野春男　甲野冬子', "'第4欄　建物図面及び各階平面図'", "'建　　物　　図　　面'", "'各　階　平　面　図'"]:
    check('原本の第4欄の印刷・記入', n, draw, '作図')
m = re.search(r"ax\.text\([^\n]*'甲野春男　甲野冬子'", draw)
ok = m is not None and '（略）' not in m.group()
ng += (not ok)
print(('OK ' if ok else 'NG ') + '第4欄：申請人の欄は原本に（略）の印刷がないので氏名を記入（不動産登記規則第74条第2項）')
for src, name in [(text, '記事'), (fig, '解説図'), (form, '申請書'), (fix, '添削'), (draw, '作図'), (mk, '申請書スクリプト')]:
    for bad in ['仮の形', '（仮）', '答案用紙がリポジトリにない', 'ならった仮']:
        absent('「仮」の欄の形の文言が残っていない', bad, src, name)

# ---- アガルートの解答例（照合用。第1欄・第2欄・第3欄）との一致 ----
# 解答例は年を平成30年に置き換えた版（月日は同じ）。作業の中だけで「平成30年」→「平成25年」と読み替える。
# 解答例の欄名「添付書類」（書・証書）は試験の答案用紙の欄名「添付情報」に合わせて「〜情報」に読み替える（中身の項目は同じ）。
# 第4欄（建物図面・各階平面図）は今回の解答例の画像に含まれていないので、ここでは照らさない。
NENDO = {'平成30年': '平成25年'}
TENPU = {'所有権証明書': '所有権証明情報', '住所証明書': '住所証明情報', '代理権限証書': '代理権限証明情報'}
KAITOUREI = {
    'H25_dai22mon_dai1ran_kansei': {
        '登記の目的': ['建物表題部変更登記'],
        '添付': ['建物図面', '各階平面図', '所有権証明書', '代理権限証書'],
        '申請人': ['Ｃ市Ｄ町一丁目３番２号　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　甲野冬子'],
        '所在': ['Ｃ市Ｄ町一丁目12番地', 'Ｃ市Ｄ町一丁目12番地１', '平成30年８月５日分筆により変更'],
        '家屋番号': ['12番の１'],
        '表': ['主', '倉庫', '軽量鉄骨造亜鉛メッキ鋼板ぶき２階建', '148', '22', '119', '24', '平成30年７月26日取壊し',
              '店舗', '鉄骨造陸屋根平家建', '38', '25', '平成30年７月26日主である建物に変更、平成30年８月18日種類変更、増築',
              '符号１', '物置', '22', '50', '平成30年７月26日主である建物に変更'],
    },
    'H25_dai22mon_dai2ran_kansei': {
        '登記の目的': ['建物表題登記'],
        '添付': ['建物図面', '各階平面図', '所有権証明書', '住所証明書', '代理権限証書'],
        '申請人': ['Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　２分の１　甲野冬子'],
        '所在': ['Ｃ市Ｄ町一丁目11番地、10番地'],
        '表': ['倉庫', '軽量鉄骨造亜鉛メッキ鋼板ぶき２階建', '148', '22', '119', '24', '平成30年８月22日新築'],
    },
}


def nk(t):
    return re.sub(r'[\s　]', '', unicodedata.normalize('NFKC', t))


for name, items in KAITOUREI.items():
    h = nk(strip_tags(open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()))
    for ran, vals in items.items():
        for v in vals:
            w = v
            for a_, b_ in list(NENDO.items()) + list(TENPU.items()):
                w = w.replace(a_, b_)
            ok = nk(w) in h
            ng += (not ok)
            print(('OK ' if ok else 'NG ') + f'解答例と一致 [{name}・{ran}] : {v}' + (f' → {w}' if w != v else ''))
h1n = nk(strip_tags(open(os.path.join(ZU, 'H25_dai22mon_dai1ran_kansei.html'), encoding='utf-8').read()))
h2n = nk(strip_tags(open(os.path.join(ZU, 'H25_dai22mon_dai2ran_kansei.html'), encoding='utf-8').read()))
ok = '住所証明' not in h1n and '持分' not in h1n and '12番の1' not in h2n
ng += (not ok)
print(('OK ' if ok else 'NG ') + '解答例と一致：第1欄は住所証明・持分なし、第2欄は家屋番号空欄（12番の1を書かない）')
ok = '不動産番号' in h1n and '不動産番号' in h2n and not re.search(r'不動産番号\d', h1n + h2n)
ng += (not ok)
print(('OK ' if ok else 'NG ') + '解答例と一致：不動産番号の行は空欄（原本に印刷された行）')
# 第3欄：解答例の要旨（必要な登記・可否・根拠）を、自分の言葉の説明文が全部含んでいるか（文言は流用しない）
h3 = nk(strip_tags(open(os.path.join(ZU, 'H25_dai22mon_dai3ran_kansei.html'), encoding='utf-8').read()))
for v in ['建物滅失登記を申請する必要がある', '甲野春男が単独で申請することができる', '報告的登記', '保存行為']:
    ok = nk(v) in h3
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'解答例と一致 [第3欄の要旨] : {v}')
for v in ['甲野春男から申請することは可能である', '理由としては', '法的な性質は報告的登記であり']:
    absent('解答例の文言を流用していない', v, setsumei, '第3欄')


# ======================================================================
# 2026-10-16：最新の執筆ルール・チェックリストでの照らし直しで足した検査
# ======================================================================
# ---- まとめのわな → 図（1項目に1つのわな。図は重複しない）と、わなの図の位置 ----
TRAPS = [  # (まとめの項目の決め手の語, 藍子の誤答の語, 図のPNG, 図のマーカーの直前の行にある決め手の語)
    ('解体移転は所在の変更（えい行移転）ではなく', '本件旧建物の所在を変える建物表題部変更登記です！', 'H25_dai22mon_zu03_kaitai_eikou_hikaku',
     'だから本件新建物は建物表題登記です'),
    ('附属建物が残っていれば滅失登記ではなく', '12番の1は建物滅失登記です！', 'H25_dai22mon_zu04_shu_messhitsu_fuzoku', '3つの建物に3種類の登記よ'),
    ('概略図の見た目ではなく座標で決める', 'だから所在は『C市D町一丁目11番地』です！', 'H25_dai22mon_zu07_shozai_ayamari_hikaku',
     '座標で描いた実際を並べてごらんなさい'),
    ('地番の順ではなく、床面積の多い11番地が先', '地番の順に『C市D町一丁目10番地、11番地』です！', 'H25_dai22mon_zu08_shozai_junjo',
     '11番の上が約147.2平方メートル、10番の上は約1.0平方メートル'),
    ('柱の外面ではなく柱の中心線で測る', '鉄骨造だから、柱の外面で測るんですよね', 'H25_dai22mon_zu10_hashira_hikaku', '柱の中心からの測定値をそのまま使えばいい'),
    ('丸印で1階の東の辺にそろえて重ねる', '北西の角を1階の北西の角に合わせて描きます！', 'H25_dai22mon_zu12_2kai_ayamari_hikaku', '1階の位置を点線で示して確かめる'),
    ('本件旧建物の所在は12番地1に変わる', '『C市D町一丁目12番地』を1段目に写します', 'H25_dai22mon_zu16_bunpitsu_shozai', '今の家屋番号『12番の1』を書けばいい'),
    ('空欄にせず本件新建物の求積値', '空欄でいいですか？', 'H25_dai22mon_toukishinseisho_machigai_yukamenseki', '原因は『平成25年7月26日取壊し』です'),
    ('原因の頭に欄番号（①③）を付けない', '頭に欄番号を付けて', 'H25_dai22mon_toukishinseisho_machigai_genin', '番号なしの'),
    ('材料を出した乙川建設ではなく、代金を払い終えた2人が所有者', '乙川建設の建物になりませんか？', 'H25_dai22mon_zu18_tenpu_dai2ran',
     '建築請負人の証明情報などが所有権証明情報になるの'),
    ('表題部変更登記の申請人には持分を書かず、表題登記の申請人には持分を書く', '申請人は、第1欄と同じく', 'H25_dai22mon_toukishinseisho_machigai_shinseinin',
     '第2欄で2つも間違えるところでした'),
    ('共有の建物の滅失登記は報告的登記なので', '共有者全員の2人で申請しないといけないと思います', 'H25_dai22mon_zu19_keiseiteki_houkokuteki',
     '申請人の欄には春男さんだけを書けばいいわ'),
]
matome = text.split('今日のまとめよ。わなを1つずつ並べるわ」')[1].split('**藍子**')[0]
items = [l[2:] for l in matome.splitlines() if l.startswith('- ')]
ok = len(items) == len(TRAPS) == len({p for _, _, p, _ in TRAPS}) and all(k in it for (k, _, _, _), it in zip(TRAPS, items))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'まとめのわな{len(items)}項目と、わな→図の対応表{len(TRAPS)}組（図の重複なし・同じ順）')
ok = all(it.count('。') <= 1 for it in items)
ng += (not ok)
print(('OK ' if ok else 'NG ') + 'まとめの1項目に1つのわな（1項目に文を2つ以上書いていない）')
mk_pos = [(m.start(), l) for m in re.finditer(r'^> 【画像挿入】.*$', text, re.M) for l in [m.group()]]
order_png = [n for n, _, _ in PNGS]
for key, phrase, png, word in TRAPS:
    pos = text.find(phrase)
    after = [k for k, (p, _) in enumerate(mk_pos) if p > pos][:2]
    k_png = order_png.index(png)
    ok = pos >= 0 and k_png in after and '\n## ' not in text[pos:mk_pos[k_png][0]]
    prev = [l for l in text[:mk_pos[k_png][0]].splitlines() if l.strip()][-1]
    ok2 = word in prev
    ng += (not ok) + (not ok2)
    print(('OK ' if ok else 'NG ') + f'わなの誤答のあとの2つ以内のマーカーに図がある : {phrase[:18]}… → {png}')
    print(('OK ' if ok2 else 'NG ') + f'わなの図のマーカーの直前の行に決め手の語 : {word}')

# ---- 電卓のキー列（F-789SG。[Abs] は開きかっこを兼ねる）を記事の順に実行して、文中の表示と比べる ----
mem = {}


def run_keys(seq):
    toks = re.findall(r'\[[^\]]+\]|[0-9]+(?:\.[0-9]+)?', seq)
    out, i, last = [], 0, None
    keymap = {'[÷]': '/', '[×]': '*', '[−]': '-', '[+]': '+', '[Abs]': 'abs(', '[(]': '(', '[)]': ')'}
    while i < len(toks):
        tk = toks[i]
        if tk == '[ALPHA]':
            out.append(f"mem['{toks[i + 1][1:-1]}']")
            i += 2
            continue
        if tk == '[SHIFT]' and toks[i + 1] == '[STO]':      # 入力中の式（なければ直前の結果）を記憶する
            mem[toks[i + 2][1:-1]] = eval(''.join(out), {'mem': mem}) if out else last
            out = []
            i += 3
            continue
        if tk == '[i]':
            out[-1] = f'({out[-1]}*1j)'
        elif tk == '[=]':
            last = eval(''.join(out), {'mem': mem})
            out = []
        else:
            if tk.startswith('[') and tk not in keymap:
                raise ValueError('要点にないキー ' + tk)
            out.append(keymap.get(tk, tk))
        i += 1
    return last


check('複素数モード', 'モードの2番でCPLXにして')
seq_a = re.search(r'A点なら `([^`]*)`', text).group(1)
assert seq_a == '39.24 [+] 73.39 [i] [SHIFT] [STO] [A]'
run_keys(seq_a)
for nm_, z_ in [('B', B), ('C', C), ('D', D), ('E', E), ('F', F)]:            # 「同じようにB〜Fも記憶」を座標成果どおりに
    run_keys(f'{z_.real:.2f} [+] {z_.imag:.2f} [i] [SHIFT] [STO] [{nm_}]')
ok = abs(mem['A'] - A) < 1e-9
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'電卓のキー列 {seq_a} → A に {mem["A"]}')
pairs = re.findall(r'`([^`]*\[Abs\][^`]*)` で、表示 ([0-9.]+…?)', text)
ok = len(pairs) == 5
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'記事のキー列と表示の組 : {len(pairs)}組')
for seq, disp_ in pairs:
    v = run_keys(seq)
    got = fmt_num(abs(v))
    ok = got == disp_
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'電卓のキー列 {seq} → 表示 {got}（記事 {disp_}）')

# ---- 画像の中に図の番号を書かない（題・パネルの題・説明文・申請書と添削のHTML） ----
titles = re.findall(r"(?:new_figure|fixed_figure|sheet_figure|tekiyou_table|suptitle|set_title)\(\s*(?:'[^']*',\s*)?'([^']*)'", draw)
bad_t = [x for x in titles if re.search(r'図\s*[0-9０-９]', x)]
ok = not bad_t and len(titles) >= 20
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像の題に図の番号がない（{len(titles)}件） : {bad_t}')
htmls = sorted(f for f in os.listdir(ZU) if f.endswith('.html'))
bad_h = [f for f in htmls if re.search(r'図\s*[0-9０-９]', strip_tags(open(os.path.join(ZU, f), encoding='utf-8').read()))
         or 'style="height:' in open(os.path.join(ZU, f), encoding='utf-8').read()]
ok = not bad_h and len(htmls) == 7
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'申請書・添削のHTML{len(htmls)}枚に図番・style="height:" がない : {bad_h}')
for nm_ in ('dai1ran', 'dai2ran'):
    h_ = strip_tags(open(os.path.join(ZU, f'H25_dai22mon_{nm_}_kansei.html'), encoding='utf-8').read())
    ok = not re.search(r'第[1-4１-４]欄', h_)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{nm_}：登記申請書の画像に「第○欄」を入れていない（キャプションも）')
ok = re.search(r'第[1-4]欄', ''.join(strip_tags(open(os.path.join(ZU, f'H25_dai22mon_toukishinseisho_machigai_{k}.html'), encoding='utf-8').read())
                                      for k in ('shozai', 'shinseinin', 'yukamenseki', 'genin')).replace('第1欄の表題部変更登記', '')) is None
ng += (not ok)
print(('OK ' if ok else 'NG ') + '添削の画像に「第○欄」の欄の名前を入れていない（吹き出しの説明の語を除く）')

# ---- 建物の表示の表の列の幅：答案用紙の原本の画像（1ページ目・第1欄）の罫線から測って、HTMLの比と比べる ----
import numpy as np
g1 = np.array(Image.open(os.path.join(TY, 'H25_dai22mon_touan_youshi_p1.png')).convert('L'))


def vlines(y0, y1, x0=100, x1=1140):
    b = (g1[y0:y1, x0:x1] < 200).sum(axis=0)
    xs = [x0 + i for i, v in enumerate(b) if v > 0.5 * (y1 - y0)]
    out = []
    for x in xs:
        if out and x - out[-1][-1] <= 3:
            out[-1].append(x)
        else:
            out.append([x])
    return [sum(o) / len(o) for o in out]


ent = vlines(860, 930)          # 記入行：縦書き・主附・種類・構造・床面積の整数部・小数部・原因の縦線
sho = vlines(655, 690)          # 所在の下段の仕切り
kao = vlines(705, 735)          # 家屋番号の行の仕切り
x_div_sho = [x for x in sho if 640 < x < 780][0]
x_div_kao = [x for x in kao if 470 < x < 600][0]
L_, R_ = ent[0], ent[-1]
meas = sorted(ent + [x_div_sho, x_div_kao])
meas_w = [round((b - a) / (R_ - L_) * 100, 2) for a, b in zip(meas[:-1], meas[1:])]
COL_W = eval(re.search(r'COL_W = (\([^)]*\))', mk).group(1))
ok = len(meas_w) == len(COL_W) == 9 and all(abs(a - b) < 0.4 for a, b in zip(meas_w, COL_W)) and abs(sum(COL_W) - 100) < 0.05
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'建物の表示の表の列の幅（答案用紙の原本から測った比 {meas_w} と HTML {COL_W}）')

# ---- 第4欄の枠：答案用紙の原本の画像（2ページ目）の罫線から mm を測って、作図スクリプトの寸法と比べる ----
g2 = np.array(Image.open(os.path.join(TY, 'H25_dai22mon_touan_youshi_p2.png')).convert('L')) < 140
PX = 2481 / 420.0
def first_dark(arr):
    idx = np.nonzero(arr)[0]
    return idx[0] if len(idx) else None


ys_ = range(600, 1300, 10)
frame_l = np.mean([200 + first_dark(g2[y, 200:400]) for y in ys_]) / PX                       # 枠の左の縦線（行ごとに最初の黒）
frame_r = np.mean([2150 - first_dark(g2[y, 2150:2050:-1]) for y in ys_]) / PX                  # 枠の右の縦線（右から最初の黒）
xs_ = range(600, 1000, 10)
frame_t = (1754 - np.mean([180 + first_dark(g2[180:260, x]) for x in xs_])) / 5.906            # 枠の上の横線
frame_b = (1754 - np.mean([1450 + first_dark(g2[1450:1530, x]) for x in xs_])) / 5.906         # 枠の下の横線
mid_ = [1150 + first_dark(g2[y, 1150:1250]) for y in range(232, 272, 4)]                        # 中央の上の短い仕切り
SH = eval(re.search(r'FR_L, FR_R, FR_B, FR_T = ([^\n#]*)', draw).group(1))
MID_ = float(re.search(r'^MID = ([0-9.]+)', draw, re.M).group(1))
ok = (abs(frame_l - SH[0]) < 1.0 and abs(frame_r - SH[1]) < 1.0 and abs(frame_b - SH[2]) < 1.0 and abs(frame_t - SH[3]) < 1.0
      and abs(sum(mid_) / len(mid_) / PX - MID_) < 1.0)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'第4欄の枠（原本から測った 左{frame_l:.1f}・右{frame_r:.1f}・下{frame_b:.1f}・上{frame_t:.1f}・中央{sum(mid_) / len(mid_) / PX:.1f}mm と作図 {SH}・{MID_}）')
# 縮尺どおり：建物図面 1m ＝ 2mm（S500）、各階平面図 1m ＝ 4mm（S250）。方位は建物図面の側だけ
check('建物図面の縮尺（1m＝2mm）', 'M(ZUMEN_X0 + 2 * (p.imag - ZUMEN_E0), ZUMEN_Y0 + 2 * (p.real - ZUMEN_N0))', draw, '作図')
check('各階平面図の縮尺（1m＝4mm）', 'return M(x0 + 4 * e, y0 - 4 * s)', draw, '作図')
heimen_src = draw.split('def heimen_content(z):')[1].split('\ndef ')[0]
zumen_src = draw.split('def zumen_content(z):')[1].split('\ndef ')[0]
ok = 'north_arrow' not in heimen_src and 'north_arrow' in zumen_src
ng += (not ok)
print(('OK ' if ok else 'NG ') + '方位記号は建物図面の側だけ（不動産登記規則第82条第2項。各階平面図の第83条第1項にはない）')
for w_ in ['1メートルが2ミリだから、1階の東西14.56は約29ミリ、敷地の11番と10番を合わせても約44ミリ四方です',
           '枠の右半分は横が約156ミリあるので', '1メートルが4ミリだから、1階の東西14.56は約58ミリ、南北10.92は約44ミリです',
           '方位は建物図面に書くもの（不動産登記規則第82条第2項）で、各階平面図の記録事項（同規則第83条第1項）には入っていないので書きません',
           '第4欄は1枚の枠で、真ん中の上下に短い仕切りの線があるだけ']:
    check('第4欄の大きさ・方位（会話）', w_)
assert round(14.56 * 2, 2) == 29.12 and round(14.56 * 4, 2) == 58.24 and round(10.92 * 4, 2) == 43.68
assert round((39.24 - 17.07) * 2, 1) == 44.3 and round((95.16 - 73.39) * 2, 1) == 43.5 and round(SH[1] - MID_, 1) == 156.4

# ---- 追加した図（図8・図17・図18）と、添削画像の決まり ----
ok = round(on11, 1) == 147.2 and round(on10, 1) == 1.0 and 'on11, on10 = 147.2, 1.0' in draw
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'図8の約147.2㎡・約1.0㎡は、1階の多角形をD-Cの線で切った面積（{on11:.4f}・{on10:.4f}）')
check('図8の面積の検算（プロンプト）', '（147.2226…・1.0072…）', fig, '解説図')
assert fmt_num(on11, 4) == '147.2226…' and fmt_num(on10, 4) == '1.0072…'
NEW16 = {
    '図8': ['誤り：地番の順に書く', '正しい：床面積の多い部分の地番が先', 'C市D町一丁目10番地、11番地', 'C市D町一丁目11番地、10番地',
           '（不動産登記事務取扱手続準則第88条第2項）'],
    '図17': ['イ　所在を変更するとき', 'ロ（1）　床面積を変更するとき', 'ロ（2）　床面積が増加するとき', 'ハ　附属建物を新築したとき',
            'ニ　共用部分である旨の登記', '令第7条第1項第2号　代理人', '所有権証明情報', '代理権限証明情報', '入れない'],
    '図18': ['イ　建物図面', 'ロ　各階平面図', 'ハ　所有権を有することを証する情報', 'ニ　住所を証する情報', 'ホ・ヘ　区分建物・敷地権',
            'ト　法第47条第2項（一般承継人）', '住所証明情報', '準則第87条第1項'],
}
for zu_, words in NEW16.items():
    for w_ in words:
        w2 = w_.replace('\n', '')
        ok = w_ in draw and w2 in fig
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'追加した図（作図スクリプトとプロンプト）[{zu_}] : {w_}')
# 当てはめ表の各号は原典の文言どおり（note-articles/laws/）
LAWS = os.path.join(HERE, '..', '..', '..', 'note-articles', 'laws')
bt = open(os.path.join(LAWS, 'fudousan-touki-rei-betsuhyou.md'), encoding='utf-8').read()
b14 = bt.split('#### 十四')[1].split('#### 十五')[0]
b12 = bt.split('#### 十二')[1].split('#### 十三')[0]
for w_ in ['イ　建物の所在する市、区、郡、町、村、字及び土地の地番を変更し', 'ロ　床面積を変更し', '（２）　床面積が増加するときは',
           'ハ　附属建物を新築したときは', 'ニ　共用部分である旨の登記又は団地共用部分である旨の登記がある建物']:
    check('令別表14の項の原典', w_, b14, '法令')
for w_ in ['イ　建物図面', 'ロ　各階平面図', 'ハ　表題部所有者となる者が所有権を有することを証する情報', 'ニ　表題部所有者となる者の住所を証する',
           'ト　法第四十七条第二項の規定による申請にあっては']:
    check('令別表12の項の原典', w_, b12, '法令')
check('令第7条第1項第2号の原典', '二　代理人によって登記を申請するとき（法務省令で定める場合を除く。）は、当該代理人の権限を証する情報',
      open(os.path.join(LAWS, 'fudousan-touki-rei.md'), encoding='utf-8').read(), '法令')
jun = open(os.path.join(LAWS, 'fudousan-touki-jimu-junsoku.md'), encoding='utf-8').read()
check('準則第88条第2項の原典', '床面積の多い部分又は主たる建物の所在する土地の地番を先に記録し', jun, '法令')
check('準則第87条第1項の原典', '建築請負人又は敷地所有者の証明情報', jun, '法令')
check('準則第102条の原典', '当該原因及びその日付欄に「令和何年何月何日主たる建物に変更」のように記録する', jun, '法令')
kis = open(os.path.join(LAWS, 'fudousan-touki-kisoku-1.md'), encoding='utf-8').read()
check('規則第82条第2項の原典（方位）', '建物図面には、方位、縮尺、敷地の地番及びその形状', kis, '法令')
check('規則第83条第1項の原典（方位なし）', '各階平面図には、縮尺、各階の別、各階の平面の形状、一階の位置', kis, '法令')
# 会話：当てはめ表・添削の前の受け答え
for w_ in ['じゃあ、この行の原因を答案に書く形で言ってごらんなさい', '変わったのは①種類と③床面積だから、頭に欄番号を付けて',
           '全部を書き起こす行だから、番号なしの『平成25年7月26日主である建物に変更、平成25年8月18日種類変更、増築』ですね',
           '材料を出したのが乙川建設でも、建物は代金を払い終えた2人のもの', '第2欄の所在の欄に書いた最初の答えを、赤ペンで直しておきなさい']:
    check('照らし直しで足した会話', w_)

print('NG件数:', ng)
