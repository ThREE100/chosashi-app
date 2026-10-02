"""平成30年度 第22問（建物）：記事の数値・計算・付属プロンプト・体裁の照合スクリプト。
アガルートの解答例（第22問 解答例、第1欄（その1）（その2）・第2欄・第3欄の各階平面図・求積表・建物図面）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/H30/Q22/verify_H30_dai22mon.py"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, area

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_H30_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_H30_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_H30_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_H30_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_H30_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


# ---- 敷地：〔座標一覧表〕（X＝北、Y＝東）。すべての辺が軸に平行な長方形 ----
A, B, C, D, E, F = P(0, -15), P(29, -15), P(29, 0), P(29, 15), P(0, 15), P(0, 0)
lot301, lot302 = [A, B, C, F], [F, C, D, E]
assert A.imag == B.imag and F.imag == C.imag and E.imag == D.imag
assert B.real == C.real == D.real == 29 and A.real == F.real == E.real == 0
assert round(area(lot301), 2) == round(area(lot302), 2) == 435.00      # 登記記録の地積と一致
check('座標の読み取り（301番）', 'A（0.00、−15.00）、B（29.00、−15.00）、C（29.00、0.00）、F（0.00、0.00）')
check('座標の読み取り（302番）', 'D（29.00、15.00）、E（0.00、15.00）')
check('長方形', '南北29.00メートル、東西15.00メートルの長方形')
check('複素数モード不要', '関数電卓の複素数モードを持ち出すまでもないわ')
check('地積と一致', '29.00かける15.00で435.00平方メートル。登記記録の地積435.00と、301番も302番も一致')
check('辺長は建物図面に書かない', 'その辺長は作図のチェック用よ。建物図面には書かないの')
check('周りの地番', '301番の北が314番、西が300番2、302番の北が315番、東が303番。南は両方とも道路（200）')

# ---- 建物（外壁の座標）：G〜O ----
G, H, I, J, K, L = P(20, -8), P(20, 12), P(11, 12), P(11, -3), P(8, -3), P(8, -8)
M, N, O = P(20, 3), P(11, 3), P(20, -3)
assert O.real == M.real == G.real == H.real and N.real == J.real == I.real  # O・M・Nは外形の角ではない
outer = [G, H, I, J, K, L]
assert area(outer) == 195.00
# 建物図面の距離（外壁の角G・H・Lから筆界まで）
dG, dH, dL = G.imag - A.imag, B.real - H.real, L.real - A.real
assert (dG, dH, dL) == (7, 9, 8)
check('G→AB', '−8.00−（−15.00）＝7.00メートル')
check('H→CD', '29.00−20.00＝9.00メートル')
check('L→AF', 'L点（8.00、−8.00）から南の道路との境AFまでは8.00メートル')
check('建物図面の距離の桁', '『7.00』『9.00』『8.00』')
# 所在の順序：床面積の多い部分（境はY＝0）
on302 = (12 - 0) * 9
on301 = (0 - (-8)) * 9 + 5 * 3
assert (on302, on301) == (108, 87) and on302 > on301
wc302 = round(11.93 * 8.86, 4)
wc301 = round(7.93 * 8.86 + 4.86 * 3.00, 4)
assert wc302 > wc301 and round(wc302 + wc301, 4) == 190.5396  # 壁心でも順序は同じ
check('所在の順序の計算', '302番の上は東西12.00×南北9.00で108.00平方メートル、301番の上は8.00×9.00の72.00平方メートルと南西の張り出しの5.00×3.00で87.00平方メートル')
check('所在の順序', '『302番地、301番地』！')
check('所在の根拠', '不動産登記事務取扱手続準則第88条第2項')

# ---- 1階：外壁から0.07内側（事実関係8）。入り隅に端がある3.00・15.00は変わらない ----
t = 0.07
F1 = [(0, 0), (19.86, 0), (19.86, 8.86), (4.86, 8.86), (4.86, 11.86), (0, 11.86)]   # (Y東, X南)
w_n, h_n = round(20 - 2 * t, 2), round(9 - 2 * t, 2)
w_s, h_s = round(5 - 2 * t, 2), 3.00                                                  # 3.00は両端が同じ向きにずれる
assert (w_n, h_n, w_s) == (19.86, 8.86, 4.86)
a1 = round(w_n * h_n + w_s * h_s, 4)
assert a1 == 190.5396 == round(poly_area(F1), 4) and trunc2(a1) == 190.53 and round(a1, 2) == 190.54
assert round(4.86 + 15.00, 2) == 19.86 and round(8.86 + 3.00, 2) == 11.86 == round(12 - 2 * t, 2)
wrong = round(19.86 * 8.86 + 4.86 * 2.86, 4)
assert wrong == 189.8592 and trunc2(wrong) == 189.85 and round(a1 - wrong, 4) == round(4.86 * 0.14, 4) == 0.6804
check('藍子の誤答1（外壁のまま）', '20.00×9.00＋5.00×3.00で、195.00平方メートル！')
check('壁心の根拠', '壁その他の区画の中心線で囲まれた部分で測るの（不動産登記規則第115条）')
check('藍子の誤答2（一律0.14）', '175.9596＋13.8996で189.8592、189.85平方メートル！')
check('入り隅の3.00', '両方とも北へずれるから、間の長さは3.00のまま！')
check('入り隅の15.00', '外壁で15.00メートルなら、中心線でも15.00メートルのままです！')
check('検算', '4.86＋15.00＝19.86。西の辺も、8.86＋3.00＝11.86')
check('差', '4.86×0.14、0.6804平方メートルも減らしすぎていました')
check('1階 求積表', '- 19.86 × 8.86 ＝ 175.9596\n- 4.86 × 3.00 ＝ 14.5800\n- 合計：190.5396 （床面積：190.53平方メートル）')
check('1階 切り捨て', '190.5396だから、四捨五入して190.54……じゃなくて')

# ---- 2階：Q部分と同型（事実関係9）----
F2 = [(11, 0), (19.86, 0), (19.86, 8.86), (11, 8.86)]
a2 = round(8.86 * 8.86, 4)
assert a2 == 78.4996 == round(poly_area(F2), 4) and trunc2(a2) == 78.49 and round(a2, 2) == 78.50
assert round(19.86 - 8.86, 2) == 11.00  # 2階の西の端は1階の北西の角から東へ11.00
check('2階 求積表', '- 8.86 × 8.86 ＝ 78.4996\n- 合計：78.4996 （床面積：78.49平方メートル）')
check('2階 切り捨て', '78.4996は、四捨五入すると78.50、切り捨てると78.49')
check('1階の位置の点線', '1階の外形を点線で重ねて1階の位置を示すこと。')

# ---- 合体前の建物の床面積（登記記録で省略→計算）----
aP = round(round(12 - 2 * t, 2) * round(5 - 2 * t, 2), 4)
assert aP == 57.6396 and trunc2(aP) == 57.63
ext = round((3 + t) - (-3 - t), 2)
assert ext == 6.14 and round(aP + round(ext * 8.86, 4) + a2, 4) == a1
check('P部分の床面積', '11.86×4.86＝57.6396。切り捨てて57.63平方メートル')
check('Q部分の床面積', '8.86×8.86＝78.4996、1階も2階も78.49平方メートル')
check('合体前後の検算', '6.14×8.86＝54.4004。57.6396＋54.4004＋78.4996＝190.5396')

# ---- 問1 第1欄（その2）ア〜エ ----
check('ア〜エ（正解）', 'ア＝主従、イ＝増築工事、ウ＝隔壁を除去、エ＝構造上1個')
check('エの対比（利用上⇔構造上）', '『利用上1個』です！')
check('間取図の根拠', 'P部分の中に、内寸5.5メートルの部屋は入らない')

# ---- 問1 第1欄（その1）申請書 ----
check('登記の目的の対比（増築⇔合体）', 'Q部分だけ増築があったことにしてほしい')
check('登記の目的の対比（合併⇔合体）', '建物合併登記です！')
check('合併の制限', '不動産登記法第56条第5号')
check('合体の根拠', '合体の日から1月以内の申請義務（同法第49条第1項）')
check('登記の目的', '『合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消』')
check('一の申請情報', '不動産登記令第5条第1項')
check('家屋番号は空欄', '申請情報には書かないの（不動産登記令第3条第8号ロ）')
check('建物の表示（3行の原因）', '1行目が『平成30年10月1日302番と合体』、2行目が『平成30年10月1日301番と合体』、3行目が『平成30年10月1日301番、302番を合体』')
check('欄番号を付けない', '表題部の変更の登記や更正の登記（不動産登記事務取扱手続準則第94条第2項）')
check('合体後の建物', '種類は居宅、構造は木造かわらぶき2階建、床面積は1階190.53平方メートル、2階78.49平方メートル')
check('所有権登記の表示', '301番は順位番号2番、平成29年1月20日第567号、甲山太郎。302番は順位番号1番、昭和60年3月12日第1234号、甲山太郎')
check('存続登記', '301番の乙区1番、抵当権設定、平成29年1月20日第568号、株式会社C銀行')
check('申請人（誤答）', '『A市B町一丁目1番1号　甲山太郎』です！')
check('同一人でないとみなす根拠', '不動産登記令別表13の項申請情報欄ニ')
check('申請人（正解）', '『A市B町一丁目1番1号　持分10分の2　甲山太郎（あ）』と『A市B町一丁目1番1号　10分の8　甲山太郎（い）』')
check('目的となる権利', '存続登記の目的となる権利は『甲山太郎（あ）持分』です！')
check('移記の根拠', '不動産登記規則第120条第4項')
check('添付書類', '建物図面、各階平面図、所有権証明書、住所証明書、登記識別情報、印鑑証明書、承諾書、代理権限証書の8点')
check('登記識別情報の誤答', '事前通知か、資格者代理人の本人確認情報が必要ですね')
check('登記識別情報は1つ', '301番の登記識別情報1つでいいんですね！')
check('登記識別情報の根拠', '令第8条第2項第2号')
check('印鑑証明書の根拠', '不動産登記規則第47条第3号イ（6）')
check('承諾書の根拠', '不動産登記令別表13の項添付情報欄ト')
check('登録免許税', '合体は載っていないからですね')

# ---- 問2 第2欄 ----
check('問2 誤答（合体による登記等）', 'やっぱり合体による登記等です！')
check('問2 登記の目的', 'だから『建物表題部変更登記』よ')
check('問2 原因の誤答（②③）', '『②③平成30年10月1日構造変更、増築、符号1の附属建物合体』です')
check('問2 原因（正解）', '『③平成30年10月1日増築、符号1の附属建物合体』です')
check('問2 根拠', '不動産登記事務取扱手続準則第95条')
check('問2 構造が変わらない理由', 'Q部分は最初から木造かわらぶき2階建で、工事の後も木造かわらぶき2階建')

# ---- 付属プロンプトとの整合（登記申請書）----
check('登記の目的', '**登記の目的**：合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消', form, '申請書')
check('添付書類', '建物図面　各階平面図　所有権証明書　住所証明書　登記識別情報　印鑑証明書　承諾書　代理権限証書', form, '申請書')
app1 = 'Ａ市Ｂ町一丁目１番１号　持分　10分の２　甲山太郎（あ）'
app2 = 'Ａ市Ｂ町一丁目１番１号　　　　10分の８　甲山太郎（い）'
check('申請人1', app1, form, '申請書')
check('申請人2', app2, form, '申請書')
check('申請日・提出先', '平成30年10月19日　申請　Ｄ地方法務局Ｅ出張所', form, '申請書')
check('所在', '**所在**：Ａ市Ｂ町一丁目', form, '申請書')
check('301番の床面積', '「57｜63」', form, '申請書')
check('302番の床面積', '「1階　78｜49」「2階　78｜49」', form, '申請書')
check('合体後の床面積', '「1階　190｜53」「2階　78｜49」', form, '申請書')
check('合体後の地番', '「302番地」「301番地」（2行に分けて、302番地を上に）', form, '申請書')
for s in ['平成30年10月１日302番と合体', '平成30年10月１日301番と合体', '平成30年10月１日301番、302番を合体',
          '平成29年１月20日第567号', '昭和60年３月12日第1234号', '平成29年１月20日第568号', '「甲山太郎（あ）持分」']:
    check('申請書の記入', s, form, '申請書')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')
check('正解（申請人1）', app1, fix, '添削')
check('正解（申請人2）', app2, fix, '添削')
check('誤答（申請人）', '「Ａ市Ｂ町一丁目１番１号　甲山太郎」', fix, '添削')
check('誤答（目的となる権利）', '「甲山太郎の持分」', fix, '添削')
check('正解（目的となる権利）', '「甲山太郎（あ）持分」', fix, '添削')

# ---- 解説図プロンプトの頂点座標（面積を計算して求積表と一致させる）----
BLDG_SITE = [(-7.93, 19.93), (11.93, 19.93), (11.93, 11.07), (-3.07, 11.07), (-3.07, 8.07), (-7.93, 8.07)]
assert round(poly_area(BLDG_SITE), 4) == 190.5396
check('図3 床面積の線 頂点座標', ' → '.join(f'({y:g}, {x:g})' for y, x in BLDG_SITE + [BLDG_SITE[0]]), fig, '解説図')
SITE301 = [(-15, 0), (-15, 29), (0, 29), (0, 0)]
SITE302 = [(0, 0), (0, 29), (15, 29), (15, 0)]
OUTER = [(c.imag, c.real) for c in outer]                       # 敷地の座標系 (Y, X)
P_OUT = [(-8, 20), (-3, 20), (-3, 8), (-8, 8)]
Q_OUT = [(3, 20), (12, 20), (12, 11), (3, 11)]
WRONG = [(0, 0), (19.86, 0), (19.86, 8.86), (4.86, 8.86), (4.86, 11.72), (0, 11.72)]
assert round(poly_area(P_OUT) + 6 * 9 + poly_area(Q_OUT), 2) == 195.00
for label, pts, want in [('図2 301番', SITE301, 435.00), ('図2 302番', SITE302, 435.00), ('図1・図3 1階の外壁', OUTER, 195.00),
                         ('図1 P部分', P_OUT, 60.00), ('図1 Q部分', Q_OUT, 81.00),
                         ('図4右・図5 1階', F1, 190.5396), ('図4左 誤り', WRONG, 189.8592), ('図6 2階', F2, 78.4996)]:
    assert round(poly_area(pts), 4) == want, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
for s in ['「7.00」「9.00」「8.00」', '「29.00m」', '「15.00m」', '301番　435.00㎡', '1階 床面積：190.53㎡',
          '2階 床面積：78.49㎡', '19.86×8.86＋4.86×2.86＝189.85ではなく', '19.86×8.86＋4.86×3.00＝190.53㎡',
          '12.00×9.00＝108.00㎡', '8.00×9.00＋5.00×3.00＝87.00㎡', '「建物の所在」の欄に、濃い青で「A市B町一丁目302番地、301番地」と記入する']:
    check('図の数値', s, fig, '解説図')

# ---- 形状・向き（図面の上＝北。見取図の注4と方位記号で確認）----
check('張り出しの位置', '南西にP部分の南側がK点・L点まで3メートル張り出すL字形')
check('張り出しの位置', '張り出しは西の端（P部分の南側）にある', fig, '解説図')
assert L.imag == G.imag and L.real < I.real                     # 張り出しは西の端で、南へ出ている
check('2階の位置', '2階の西の端は、1階の北西の角から東へ11.00m')
for bad in ['PDF', '創設的登記', '名変', '✕', '✓', '右上', '左下', '右側', '左側', '四捨五入して190.54平方', '78.50平方メートル']:
    absent('誤記・混入', bad)

# ---- note向けの体裁：話者名の行末に半角スペース2つ、名前とセリフの間に空行なし ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
markers = re.findall(r'^> 【画像挿入】(.*)$', text, re.M)
# 記事の順に、マーカーの文言の手がかりと zu/ のPNGを対応させる（解説図8＋第1欄（その2）＋添削＋完成形＋第2欄＝12）
ZU = os.path.join(HERE, 'zu')
PAIRS = [('第1欄（その2）の完成形', 'H30_dai22mon_dai1ran_sono2_kansei.png'),
         ('工事前', 'H30_dai22mon_zu01_kouji_zengo.png'),
         ('座標どおりに301番', 'H30_dai22mon_zu02_shikichi_henchou.png'),
         ('建物図面の完成形', 'H30_dai22mon_zu03_tatemono_zumen.png'),
         ('1階の誤り比較図', 'H30_dai22mon_zu04_1kai_ayamari_hikaku.png'),
         ('1階の床面積求積図', 'H30_dai22mon_zu05_1kai_kyuuseki.png'),
         ('2階の床面積求積図', 'H30_dai22mon_zu06_2kai_kyuuseki.png'),
         ('各階平面図の完成形', 'H30_dai22mon_zu07_kakukai_heimenzu.png'),
         ('3コマ添削画像', 'H30_dai22mon_toukishinseisho_machigai.png'),
         ('登記申請書（問1）の完成形', 'H30_dai22mon_toukishinseisho_kansei.png'),
         ('第2欄の完成形', 'H30_dai22mon_dai2ran_kansei.png'),
         ('本番で解く順番', 'H30_dai22mon_zu08_toku_junban.png')]
ok = len(markers) == len(PAIRS) == 12
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカー（引用形式）: {len(markers)}個（想定12）')
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
# 同じ話者のセリフが続いていないか（章の見出しで区切る）
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
# 注の書き分け（問題文の注・〔見取図〕の（注））
bare = [m.start() for m in re.finditer(r'(?<!問題文の)(?<!（)注\d', text)]
ng += bool(bare)
print(('OK ' if not bare else 'NG ') + f'書き分けのない「注N」: {len(bare)}か所')
check('注の書き分け（見取図）', '〔見取図〕の（注）4で、北はX軸の正方向')
check('注の書き分け（桁）', '問題文の注にも〔見取図〕の（注）にも桁の指定はない')
# 最新の執筆ルールで足した会話
check('第3欄の家屋番号・所在', '建物図面の上の「家屋番号」の欄は（略）と印刷済みだから何も書かないで、「建物の所在」の欄に『A市B町一丁目302番地、301番地』と書くの')
check('求積方法', 'その求積方法（求積表）も書くのよ（どちらも不動産登記規則第83条第1項）')
check('解く順番（問を先に）', 'まず前文と問を先に読むの')
check('時系列メモ', '昭和60年3月12日に302番の所有権の登記、平成29年1月20日に301番の所有権の登記と抵当権の設定、平成30年10月1日に工事完了（合体の日）、10月10日に登記記録の調査、10月19日に申請')
check('累計メモ', '東へ0・4.86・19.86、南へ0・8.86・11.86。2階は東へ11.00から19.86')
check('訂正表（問2・事実関係10）', '試験のときに配られた訂正表でどちらも『３』に直っているわ')
check('問3の下線', '問3の『問1の登記の申請書に添付する』には下線が引いてあるでしょう')
check('第2欄の答え', '第2欄は、登記の目的『建物表題部変更登記』と、主である建物の原因『③平成30年10月1日増築、符号1の附属建物合体』の2つですね')
# 申請書・添削・欄の画像のHTML（記入内容）
H = {n: open(os.path.join(ZU, n + '.html'), encoding='utf-8').read() for n in
     ['H30_dai22mon_toukishinseisho_kansei', 'H30_dai22mon_toukishinseisho_machigai',
      'H30_dai22mon_dai1ran_sono2_kansei', 'H30_dai22mon_dai2ran_kansei']}
k = H['H30_dai22mon_toukishinseisho_kansei']
for s_ in ['合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消', '住所証明書', '登記識別情報', '印鑑証明書', '承諾書',
           '持分　10分の２　甲山太郎（あ）', '10分の８　甲山太郎（い）', '平成30年10月19日　申請　　Ｄ地方法務局Ｅ出張所',
           '>57</span>', '>63</span>', '1階　190', '>53</span>', '302番地<br>301番地', '平成30年10月１日301番、<br>302番を合体',
           '平成29年１月20日第567号', '昭和60年３月12日第1234号', '甲山太郎（あ）<br>持分', '木造スレート<br>ぶき平家建']:
    check('完成形HTML', s_, k, '申請書HTML')
for bad in ['登録免許税', '78</span></td><td class="entry dec"><span class="ink">50', '>54</span>', '>64</span>', '③平成30年10月１日301番']:
    absent('完成形HTML', bad, k, '申請書HTML')
assert k.index('代　　理　　人') < k.index('平成30年10月19日')   # 答案用紙どおり、代理人の行が申請日の行より上
m_ = H['H30_dai22mon_toukishinseisho_machigai']
for s_ in ['Ａ市Ｂ町一丁目１番１号　甲山太郎</span>', '甲山太郎の持分', '令別表13の項ニ', '①誤答', '②添削', '③正解']:
    check('添削HTML', s_, m_, '添削HTML')
for s_ in ['主従', '増築工事', '隔壁を除去', '構造上1個']:
    check('第1欄（その2）HTML', s_, H['H30_dai22mon_dai1ran_sono2_kansei'], '第1欄その2')
for s_ in ['建物表題部変更登記', '③平成30年10月１日増築、符号１の附属建物合体']:
    check('第2欄HTML', s_, H['H30_dai22mon_dai2ran_kansei'], '第2欄')
# 作図スクリプト：fit はすべて pad_aspect=True、面積の assert がある
draw = open(os.path.join(ZU, 'draw_H30_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
n_fit = len(re.findall(r'\bfit\(ax', draw))
n_pad = draw.count('pad_aspect=True')
ok = n_fit == n_pad and n_fit > 0
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit {n_fit}か所がすべて pad_aspect=True（{n_pad}）')
for s_ in ['== 190.5396', '== 189.8592', '== 78.4996', '== 195.00', '105.6998']:
    check('作図スクリプトの検算', s_, draw, '作図')
for f in ['prompt_H30_dai22mon_kaisetsuzu.md', 'prompt_H30_dai22mon_toukishinseisho_gazou.md',
          'prompt_H30_dai22mon_toukishinseisho_machigai.md']:
    src = open(os.path.join(HERE, f), encoding='utf-8').read()
    absent('記号', '✕', src, f)
    absent('記号', '✓', src, f)
check('生成済みのファイル名', 'zu/H30_dai22mon_zu08_toku_junban.png', fig, '解説図')
check('生成済みのファイル名', 'zu/H30_dai22mon_zu07_kakukai_heimenzu.png', fig, '解説図')
# 図面の完成形は答案用紙の第3欄の欄の枠の中（2026-09-30のルール。答案用紙は public/kijutsu/H30-tatemono/a2.webp）
for s_ in ["cell(fig, 0.20, 0.885, 0.46, 0.935, '（略）'", "'A市B町一丁目302番地、301番地', fs=16, ha='left', color=INK",
           "'申　請　人'", "'1/500'", "'作　成　者'", '（平成30年○月○日作成）', "'1/250'",
           "'H30_dai22mon_zu07_kakukai_heimenzu'", '== 190.5396 and round(area([P(*v) for v in F2]), 4) == 78.4996']:
    check('第3欄の枠・各階平面図の完成形', s_, draw, '作図')
check('第3欄の枠（プロンプト）', '答案用紙の第3欄の右半分', fig, '解説図')
check('第3欄の枠（プロンプト）', '答案用紙の第3欄の左半分', fig, '解説図')
# 2026-10-02の照らし直しで足した会話
check('各階平面図の完成形の会話', '答案用紙の第3欄の左半分には、どう並べればいいですか？')
check('各階平面図の完成形の会話', '下の作成者の欄は（略）と印刷済みだから何も書かないし、縮尺の1/250も印刷済みよ')
check('時間配分', 'いちばん時間を食うのは、⑤の求積と⑥の作図よ')
for w_ in ['ア＝主従', 'イ＝増築工事', 'ウ＝隔壁を除去', 'エ＝構造上1個']:
    check('穴埋めの答えの語の明示（問1）', w_)
check('生成済みのファイル名', 'zu/H30_dai22mon_dai2ran_kansei.png', form, '申請書')
check('生成済みのファイル名', 'zu/H30_dai22mon_toukishinseisho_machigai.png', fix, '添削')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# ---- タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜 ----
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成30年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成30年度問題22（建物）', thumb, '見出し画像')
for src, name in [(fig, '解説図'), (form, '申請書'), (fix, '添削')]:
    check('記事タイトルの引用', title[2:], src, name)

print('NG件数:', ng)
