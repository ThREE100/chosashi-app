"""平成22年度 第21問（土地）会話形式note記事：記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-30に添付の過去問集〈全24ページ、画面の撮影画像〉で照合。下の AGAROOT に転記）と一致することも確認する。
アガルートの過去問集は改題で、申請の日付（平成30年10月22日）、道路拡幅の立会いの日付（平成29年5月10日）、測量の年月日（平成30年10月1日）、
平面直角座標系の番号（II系）を書き足していた。改題で加えられた要素は照合にも記事にも使わない（下の KAIDAI で、記事などにないことを確かめる）。
実行: python3 note-articles-Kijyutsu/H22/Q21/verify_H22_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H22_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H22_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H22_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H22_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H22_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H22_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
make = open(os.path.join(HERE, 'zu', 'make_H22_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
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


def judge(label, ok):
    global ng
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label)


def trunc4(v):
    return f'{math.floor(v * 1e4) / 1e4:.4f}…'


# ---- 座標（問題文のA市基準点成果表・測量によって得られた座標・地積測量図のメモ） ----
T1, T2, T3 = P(510.94, 507.05), P(510.98, 464.24), P(510.51, 482.27)
A, B, E, H, I = P(513.27, 465.77), P(533.99, 466.99), P(531.51, 504.65), P(532.42, 503.38), P(514.61, 502.57)
A1, A2, A3, A4, A6, A8, A10 = (P(212.45, 161.82), P(193.23, 183.97), P(211.47, 184.61), P(214.63, 180.20),
                               P(213.95, 146.95), P(193.23, 145.73), P(193.23, 164.12))

# ---- 放射 G・L・F・J（観測角の向きの注はない → 時計回りとして扱い、見取図の位置で確かめる） ----
b32 = cmath.phase(T2 - T3)
b13 = cmath.phase(T3 - T1)
check('arg(T2−T3)', to_dms(b32))
check('arg(T2−T3)＋360°', to_dms(b32 + 2 * math.pi))
check('arg(T3−T1)', to_dms(b13))
check('arg(T3−T1)＋360°', to_dms(b13 + 2 * math.pi))
PTS = {}
for n, st, bs, d, ang, want in [('G', T3, T2, 3.345, dms(122, 54, 34), '（513.27, 484.16）'),
                                ('L', T3, T2, 12.323, dms(165, 33, 52), '（513.27, 494.28）'),
                                ('F', T1, T3, 3.830, dms(38, 27, 45), '（513.27, 504.01）'),
                                ('J', T1, T3, 6.511, dms(21, 57, 44), '（513.27, 500.97）')]:
    z = radial(st, bs, d, ang)
    check(f'{n} 表示', '表示：' + disp(z))
    PTS[n] = r2(z)
    check(f'{n} 答え', f'**▶ {n}点{want}')
    w = r2(st + cmath.rect(d, cmath.phase(bs - st) - ang))
    check(f'{n}の反時計回りの誤り', f'（{w.real:.2f}, {w.imag:.2f}）')
    judge(f'{n}の反時計回りの誤りは基準点より南（道路の向こう）', w.real < min(T2.real, T3.real, T1.real))
G, L, F, J = PTS['G'], PTS['L'], PTS['F'], PTS['J']
judge('G・L・F・Jと点Aは X＝513.27', all(abs(p.real - 513.27) < 1e-9 for p in (A, G, L, F, J)))
check('G 方向角（360°超）', to_dms(b32 + 2 * math.pi + dms(122, 54, 34)))
check('G 方向角', to_dms(b32 + dms(122, 54, 34)))
check('L 方向角（360°超）', to_dms(b32 + 2 * math.pi + dms(165, 33, 52)))
check('L 方向角', to_dms(b32 + dms(165, 33, 52)))
check('F 方向角', to_dms(b13 + 2 * math.pi + dms(38, 27, 45)))
check('J 方向角', to_dms(b13 + 2 * math.pi + dms(21, 57, 44)))
judge('真数表の34°24′10″・77°03′28″（G・Lの方向角）', to_dms(b32 + dms(122, 54, 34)).startswith('34°24′09.6')
      and to_dms(b32 + dms(165, 33, 52)).startswith('77°03′27.6'))
judge('真数表の127°28′06″・110°58′05″・89°00′21″は180°逆',
      to_dms(b13 + dms(38, 27, 45) + math.pi).startswith('127°28′06') and to_dms(b13 + dms(21, 57, 44) + math.pi).startswith('110°58′05')
      and to_dms(b13 + math.pi).startswith('89°00′21'))
for s in ['34°24′10″', '77°03′28″', '127°28′06″', '110°58′05″', '89°00′21″']:
    check('真数表の角', s)

# ---- 問2 C・D（地積測量図のメモを平行移動）、K ----
ratio = (E - A) / (A3 - A8)
judge('比 (E − A) ÷ (A3 − A8) は1（表示：1）', abs(ratio - 1) < 1e-12)
check('比の表示', '表示：1\n')
check('E − A と A3 − A8', disp(E - A) + ' で、同じベクトル')
judge('A3 − A8 ＝ E − A', abs((A3 - A8) - (E - A)) < 1e-9)
SHIFT = A - A8
check('ずれ 表示', '表示：' + disp(SHIFT))
C = r2(A1 + SHIFT)
D = r2(A4 + SHIFT)
check('C 表示', '表示：' + disp(A1 + SHIFT))
check('D 表示', '表示：' + disp(A4 + SHIFT))
check('C 答え', '**▶ C点（532.49, 481.86）**')
check('D 答え', '**▶ D点（534.67, 500.24）**')
judge('A10・A2・A6をずらすとG・F・B', r2(A10 + SHIFT) == G and r2(A2 + SHIFT) == F and r2(A6 + SHIFT) == B)
check('A10＋ずれ', 'A10 ＋ 320.04 ＋ 320.04i ＝ ' + disp(A10 + SHIFT))
check('A2＋ずれ', 'A2 ＋ 320.04 ＋ 320.04i ＝ ' + disp(A2 + SHIFT))
check('D − C 表示', '表示：' + disp(D - C))
Kx = C + (D - C) / abs(D - C) * 10.18
check('K 表示', '表示：' + disp(Kx))
K = r2(Kx)
check('K 答え', '**▶ K点（533.69, 491.97）**')
check('CDの長さ', 'CDの長さは' + fmt_num(abs(D - C)))
v = (D - C).conjugate() * (K - C)
check('△CDK 表示', '表示：' + disp(v))
check('△CDKの面積', f'三角形CDKの面積は{abs(v.imag) / 2:.4f}㎡')
judge('実部 ÷ CD ＝ 10.18', f'{v.real / abs(D - C):.2f}' == '10.18')
KW = C + 10.18j
check('Yだけ足した誤りのK', f'K（{KW.real:.2f}, {KW.imag:.2f}）')
dist_kw = abs(((D - C).conjugate() * (KW - C)).imag) / abs(D - C)
check('誤りのKと直線CDの距離', f'直線CDより{dist_kw:.2f}mも南')
t_kw = (KW.imag - C.imag) / (D - C).imag
judge('誤りのKは直線CDより南', KW.real < (C + (D - C) * t_kw).real)
check('C→Dの方向角', to_dms(cmath.phase(D - C)), fig, '解説図')

# ---- 問3 面積と地積更正の要否 ----
vb = (L - C).conjugate() * (G - K)
check('(B) 表示', '表示：' + disp(vb))
judge('(B)の対角線の式と多角形の式が一致', abs(abs(vb.imag) / 2 - area([C, K, L, G])) < 1e-6)
check('(B) 面積', f'{abs(vb.imag):.4f} ÷ 2 ＝ {abs(vb.imag) / 2:.4f}')
check('(B) 答え', '**▶ (B)部分　201.86㎡（201.8623）**')
vc = (K - L) * (D - L).conjugate() + (D - L) * (E - L).conjugate() + (E - L) * (F - L).conjugate()
check('(C) 表示', '表示：' + disp(vc))
judge('(C)のLを原点にした式と多角形の式が一致', abs(abs(vc.imag) / 2 - area([K, D, E, F, L])) < 1e-6)
check('(C) 答え', '**▶ (C)部分　230.91㎡（230.91）**')
vw = (C - G) * (D - G).conjugate() + (D - G) * (E - G).conjugate() + (E - G) * (F - G).conjugate()
check('6番2 表示', '表示：' + disp(vw))
judge('6番2（今回の座標）とメモの面積が同じ', abs(area([C, D, E, F, G]) - area([A1, A4, A3, A2, A10])) < 1e-6)
check('6番2 面積', f'{abs(vw.imag):.4f} ÷ 2 ＝ {abs(vw.imag) / 2:.4f}')
judge('登記記録の地積は432.76', chiseki(area([A1, A4, A3, A2, A10])) == 432.76)
sb, sc = chiseki(area([C, K, L, G])), chiseki(area([K, D, E, F, L]))
check('分筆後の合計', f'{sb:.2f} ＋ {sc:.2f} ＝ {sb + sc:.2f}')
check('差', f'{sb + sc:.2f} − 432.76 ＝ {sb + sc - 432.76:.2f}')
judge('差0.01は誤差の限度2.01の範囲内', abs(sb + sc - 432.76) <= 2.01)
for n, p, q, want in [('HE', H, E, '1.56'), ('HI', H, I, '17.83'), ('IJ', I, J, '2.09')]:
    check(f'{n} 表示', '表示：' + fmt_num(abs(q - p)))
    judge(f'{n} は道路管理図の{want}', f'{round(abs(p - q) + 1e-9, 2):.2f}' == want)
vcity = (C - G) * (D - G).conjugate() + (D - G) * (H - G).conjugate() + (H - G) * (I - G).conjugate() + (I - G) * (J - G).conjugate()
check('道路管理図の線 表示', '表示：' + disp(vcity))
acity = abs(vcity.imag) / 2
check('道路管理図の線 面積', f'{abs(vcity.imag):.4f} ÷ 2 ＝ {acity:.5f}')
check('道路管理図の線 地積', f'{chiseki(acity):.2f}㎡')
check('道路管理図の線との差', f'{432.76 - chiseki(acity):.2f}㎡も違って')
check('帯の面積', f'{area([C, D, E, F, G]) - acity:.5f}', fig, '解説図')

# ---- 問4 辺長 ----
SIDES = {'CK': (C, K), 'KD': (K, D), 'DE': (D, E), 'EF': (E, F), 'FL': (F, L), 'LG': (L, G), 'GC': (G, C), 'KL': (K, L)}
for n, (p, q) in SIDES.items():
    val = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{val}')
    check(f'図の辺長{n}', val, fig, '解説図')
    if n not in ('FL', 'LG'):
        check(f'辺長{n} 表示', '表示：' + fmt_num(abs(q - p)))
check('FL', f'FL ＝ 504.01 − 494.28 ＝ {F.imag - L.imag:.2f}')
check('LG', f'LG ＝ 494.28 − 484.16 ＝ {L.imag - G.imag:.2f}')
check('DEの四捨五入', f'DEは{trunc4(abs(E - D))}')
check('答案用紙の大きさ 縦', f'縦約{round((D.real - T3.real) * 4)}mm')
check('答案用紙の大きさ 横', f'横約{round((T1.imag - C.imag) * 4)}mm')

# ---- 問1・問3・問4 の文言 ----
for s in ['- **問1の結論**：登記所に提出されている地積測量図（平成8年の分筆のときのもの）に記録された道路境界線（D点・E点・F点を結ぶ線）を採用すべきである',
          '- **問1の理由**：筆界は、土地が登記された時にその境を構成するものとされた線であり、所有者とA市の協議や道路境界承諾書によって動くものではない',
          '分筆も所有権の移転もされていないので、登記によって公示された筆界ではない', '現地の境界標と平成8年の地積測量図の座標は整合している',
          '- **登記の目的**：土地分筆登記',
          '- **申請人**：（被相続人　杉山太郎）　相続人　C市D町二丁目5番6号　杉山良子　上記成年後見人　E市G町四丁目2番1号　木村光江　相続人　C市D町三丁目4番6号　杉山健二',
          '- **1行目**：6番2、宅地、432.76、登記原因は空欄', '- **2行目**：(B)、地番と地目は空欄、201.86、「③6番2、6番4に分筆」',
          '- **3行目**：(C)、6番4、宅地、230.91、「6番2から分筆」', '- **4行目**：空欄',
          '- **地番の欄**：6番2、6番4', '- **土地の所在の欄**：A市B町二丁目', 'C・D・E・Gはコンクリート杭、K・Lは金属標、Fは鉄鋲',
          'A市基準点T1　X 510.94　Y 507.05、A市基準点T3　X 510.51　Y 482.27', '一部地目変更も要らないわ']:
    check('答え', s)
for s in ['不動産登記法第123条第1号', '不動産登記事務取扱手続準則第72条第1項', '不動産登記事務取扱手続準則第67条第1項第4号ただし書',
          '不動産登記法第39条第1項', '同法第30条', '民法第909条', '民法第859条第1項', '不動産登記令第3条第3号',
          '不動産登記令第7条第1項第4号', '同項第2号', '登録免許税法別表第一の一の（十三）イ']:
    check('条文', s)

# ---- アガルートの解答例（2026-09-30、過去問集の解答例ページ〈問1・問2・問3・問4〉から転記）と一致するか ----
AGAROOT = ['地積測量図（平成8年の分筆のときのもの）に記録された道路境界線（D点・E点・F点を結ぶ線）を採用すべきである', '（532.49, 481.86）', '（534.67, 500.24）', '（533.69, 491.97）', '土地分筆登記',
           '（被相続人　杉山太郎）', '杉山良子', '上記成年後見人　E市G町四丁目2番1号　木村光江', 'C市D町三丁目4番6号　杉山健二',
           '6番2、宅地、432.76', '(B)、地番と地目は空欄、201.86、「③6番2、6番4に分筆」', '(C)、6番4、宅地、230.91、「6番2から分筆」',
           '- **CK**：10.18', '- **KD**：8.33', '- **DE**：5.43', '- **EF**：18.25', '- **FL**：9.73', '- **LG**：10.12', '- **GC**：19.36',
           '- **KL**：20.55', '6番2、6番4', 'C・D・E・Gはコンクリート杭、K・Lは金属標、Fは鉄鋲', '7－1', '7－2', '6－1',
           'A市基準点T1　X 510.94　Y 507.05', 'A市基準点T3　X 510.51　Y 482.27']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)
# 改題で加えられた要素（アガルート独自の教材）：記事・付属プロンプト・作図・画像生成に入れない
KAIDAI = ['平成29年', '平成30年', 'II系', 'Ⅱ系', '改題', '平成30年10月22日', '測量の年月日：']
for src, name in [(text, '記事'), (fig, '解説図'), (form, '登記申請書'), (fix, '添削'), (thumb, '見出し画像'), (draw, '作図'), (make, '画像生成')]:
    for w in KAIDAI:
        absent('改題で加えられた要素', w, src, name)
check('照合済みの一文', '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')

# ---- 付属プロンプトとの整合 ----
a0 = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b0 = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a0:b0].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body.rstrip('\n') in fig)
N_FIG = 23
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（{N_FIG}枚）', n_fig == N_FIG)
for i in range(1, N_FIG + 1):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H22_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = sorted(set(int(m) for m in re.findall(r"'図(\d+)　", draw)))
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, N_FIG + 1)))
fits = re.findall(r'^\s*fit\((.*)', draw, re.M)
judge(f'作図スクリプトのfitはすべて pad_aspect=True（{len(fits)}か所）', fits and all('pad_aspect=True' in f for f in fits))
for s in ['（513.27, 484.16）', '（513.27, 494.28）', '（513.27, 504.01）', '（513.27, 500.97）', '（532.49, 481.86）', '（534.67, 500.24）',
          '（533.69, 491.97）', '（507.66, 484.01）', '（507.13, 494.12）', '（508.51, 504.09）', '（508.40, 501.05）', '（532.49, 492.04）',
          '271°29′35.62″', '269°00′21.11″', '394°24′09.62″', '437°03′27.62″', '307°28′06.11″', '290°58′05.11″', '83°14′09.27″',
          '320.04 ＋ 320.04i', '18.24 ＋ 38.88i', '19.22 ＋ 16.09i', '21.40 ＋ 34.47i', '295.4722 ＋ 403.7246i', '976.2617 − 461.82i',
          '201.8623', '432.7642', '405.48785', '27.27635', '1.20m', '18.5088…', '5.4252…', '8.3278…', '430.75', '434.77']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    if s not in ('（532.49, 481.86）', '（534.67, 500.24）', '（508.40, 501.05）'):   # この3つは作図では f 文字列で書き出すので assert で確かめている
        check('作図スクリプトの数値', s, draw, '作図')
judge('19.22 ＋ 16.09i ＝ A1 − A8', disp(A1 - A8) == '19.22 ＋ 16.09i')
judge('21.40 ＋ 34.47i ＝ A4 − A8', abs((A4 - A8) - P(21.40, 34.47)) < 1e-9)
for s in ['北を上にして描き直すと、こうなるわ', '数字の裏付けは、面積を出してから第6章で見せるわ', '丸めた値を変数Bに記憶しなさい',
          'GもLもX座標が513.27。南の辺の上に並びました', 'Fも南の辺のX＝513.27に乗ったので、足す方で合っています', '真数表の110°58′05″はその180°逆よ',
          'Cは、7－1と7－2の境の南の端で、6番1と6番2の境の北の端よ', 'メモの形をそのまま今の座標に移せると言い切れるわ',
          '平成8年の地積測量図の線が今も筆界だという、数字の裏付けよ', '(B)が6番2のまま、(C)が新しい6番4ですね',
          '申請人の欄は、被相続人の杉山太郎さんを書いて、良子さん、その下に成年後見人の木村さん、それから健二さんの順ですね',
          '基準点まで入れても楽に収まります', '次の年度も、この調子でいくわよ！',
          # 2026-10-05 追加（藍子の誤答のわなごとに図をそろえた）
          '道路として使われるようになるのは、工事に着工して、完成してからの話なんですね。今の帯は、杉山太郎さんの家の敷地の一部のまま',
          '北へも東へも320.04。これをA1に足せばCです', '865.5284 ÷ 2 ＝ 432.7642。登記記録の6番2の地積は、切り捨てて432.76㎡です',
          '合計が432.77で1つ多いのは、Kを丸めた分とそれぞれの切り捨ての分よ。問題ないわ',
          '6番3の次で、6番4」', '分筆を申請するのは、この2人よ」', '3行目は元の地番から『6番2から分筆』よ」',
          'Hは直線DEの途中、JはX＝513.27の南の辺の途中に乗っている杭なんですね。Iは6番2の中。どれも6番2の筆界を折り曲げる点じゃない']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成22年8月22日申請　Ａ地方法務局', '土地分筆登記', '申請人（被相続人　杉山太郎）', '相続人　Ｃ市Ｄ町二丁目５番６号　杉山良子',
          '上記成年後見人　Ｅ市Ｇ町四丁目２番１号　木村光江', '相続人　Ｃ市Ｄ町三丁目４番６号　杉山健二', 'Ａ市Ｂ町二丁目',
          '①「６番２」、②「宅地」、③「432｜76」、登記原因は空欄', '①「（Ｂ）」（地番は空欄）、②空欄、③「201｜86」、登記原因「③６番２、６番４に分筆」',
          '①「（Ｃ）６番４」、②「宅地」、③「230｜91」、登記原因「６番２から分筆」', '**記入行4**：空欄', '土地家屋調査士　北野一郎　職印',
          '「①地番」「②地目」「③地積　m²」「登記原因及びその日付」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['杉山敏夫', '田中文子', '「６番３」', '「６番４」', '申請人は6番2を取得した良子と健二。良子は成年後見人が代表する',
          '最終の支号6番3の次は6番4（6番3は使用済み）', '平成22年度 第21問｜申請人は6番2を取得した良子（成年後見人）と健二、新しい地番は6番4']:
    check('添削', s, fix, '添削')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H22_dai21mon_toukishinseisho_kansei', 'H22_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px、横1200px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H22_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H22_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成22年8月22日申請　Ａ地方法務局', '土地分筆登記', '申請人（被相続人　杉山太郎）', '相続人　Ｃ市Ｄ町二丁目５番６号　杉山良子',
          '上記成年後見人　Ｅ市Ｇ町四丁目２番１号　木村光江', '相続人　Ｃ市Ｄ町三丁目４番６号　杉山健二', 'Ａ市Ｂ町二丁目', '>６番２<', '>宅地<',
          '>432<', '>76<', '>（Ｂ）<', '>201<', '>86<', '>③６番２、６番４に分筆<', '>（Ｃ）６番４<', '>230<', '>91<', '>６番２から分筆<',
          '登録免許税　　略', '添　付　書　類　　略', '代　理　人　　略', '土地家屋調査士　北野一郎', '①地番', '②地目', '③地積　　m²',
          '平成22年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
judge('完成形の画像：記入行は4行（答案用紙どおり）', html_k.count('<td class="chimoku">') == 4)
judge('完成形の画像：申請の日付が添付書類の下・申請人の上（答案用紙の順）',
      html_k.index('添　付　書　類') < html_k.index('平成22年8月22日申請') < html_k.index('申請人（被相続人'))
judge('完成形の画像：登録免許税が添付書類より上（答案用紙の順）', html_k.index('登録免許税') < html_k.index('添　付　書　類'))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '杉山敏夫', '田中文子', '６番３', '６番４', '上記成年後見人　Ｅ市Ｇ町四丁目２番１号　木村光江',
          '申請人は6番2を取得した良子と健二。良子は成年後見人が代表する', '最終の支号6番3の次は6番4（6番3は使用済み）',
          '平成22年度 第21問｜申請人は6番2を取得した良子（成年後見人）と健二、新しい地番は6番4']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 問1・問2の欄の画像（2026-10-02 追加。申請書でない解答欄も答えの直後に置く） ----
for name in ['H22_dai21mon_toukishinseisho_kansei_toi1', 'H22_dai21mon_toukishinseisho_kansei_toi2']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が横1200px（{w}×{h}px）', w == 1200 and 300 < h < 900)
    else:
        judge(f'{name}.png がある', False)
html_t1 = open(os.path.join(HERE, 'zu', 'H22_dai21mon_toukishinseisho_kansei_toi1.html'), encoding='utf-8').read()
html_t2 = open(os.path.join(HERE, 'zu', 'H22_dai21mon_toukishinseisho_kansei_toi2.html'), encoding='utf-8').read()
KETSURON = ('登記所に提出されている地積測量図（平成8年の分筆のときのもの）に記録された道路境界線（D点・E点・F点を結ぶ線）を採用すべきである')
RIYUU = ('筆界は、土地が登記された時にその境を構成するものとされた線であり、所有者とA市の協議や道路境界承諾書によって動くものではない。'
         '道路管理図の線（H点・I点・J点を結ぶ線）は、道路拡幅のための用地の予定線であり、その部分の分筆も所有権の移転もされていないので、'
         '登記によって公示された筆界ではない。現地の境界標と平成8年の地積測量図の座標は整合している')
check('問1の結論（記事）', '- **問1の結論**：' + KETSURON)
check('問1の理由（記事）', '- **問1の理由**：' + RIYUU)
for s in ['第二十一問答案用紙（その一）', '>問1<', '【結論】', '【理由】', KETSURON + '。', RIYUU + '。', '答案用紙（その一） 問1 解答例']:
    check('問1の欄の画像（HTML）', s, html_t1, '問1の欄')
    check('問1の欄のプロンプト', s if not s.startswith('>') else '【結論】', form, '登記申請書')
judge('問1の欄：【結論】が【理由】より上（答案用紙どおり）', html_t1.index('【結論】') < html_t1.index('【理由】'))
for s in ['>問2<', 'C点のX座標', 'C点のY座標', 'D点のX座標', 'K点のY座標', '>532.49m<', '>481.86m<', '>534.67m<', '>500.24m<', '>533.69m<',
          '>491.97m<', '答案用紙（その一） 問2 解答例']:
    check('問2の欄の画像（HTML）', s, html_t2, '問2の欄')
judge('問2の欄はC→D→Kの順（答案用紙どおり）', html_t2.index('C点のX座標') < html_t2.index('D点のX座標') < html_t2.index('K点のX座標'))
for s in ['C点　X座標「532.49m」、Y座標「481.86m」', 'D点　X座標「534.67m」、Y座標「500.24m」', 'K点　X座標「533.69m」、Y座標「491.97m」',
          '答案用紙の問1の欄は、【結論】と【理由】が印刷された大きな枠です', 'これで問2のC点・D点・K点がそろったわ']:
    check('問1・問2の欄のプロンプト', s, form, '登記申請書')
for s in ['答案用紙の問1の欄は、【結論】と【理由】が印刷された大きな枠です', 'これで問2のC点・D点・K点がそろったわ']:
    check('問1・問2の欄の挿入位置の文言', s)

# ---- 注の書き分け（今年は見取図の（注）と問題文の注1〜6の2系統。裸の「注N」を残さない） ----
fig_data = fig[fig.index('## 差し替えデータ'):]
for src, name in [(text, '記事'), (fig_data, '解説図（差し替えデータ）')]:
    bare = [m.group(0) for m in re.finditer(r'(.{0,6})注([1-9])', src)
            if not re.search(r'(問題文の|問題文の注[1-9]〜)$', m.group(1))]
    judge(f'{name}の注の書き分け（裸の「注N」: {bare[:5]}）', not bare)
for s in ['問題文の注3', '問題文の注4', '問題文の注5', '問題文の注1〜6', '見取図の（注）']:
    check('注の書き分け', s)
for s in ['①問1を書き切る', '②問3の申請書の(B)(C)の地積以外の欄を埋める', '③G点・L点・F点の放射', '④C点・D点の平行移動', '⑤(B)(C)の面積と誤差の限度',
          '⑥辺長8本と地積測量図', 'N点とJ点の放射は答えに要らない']:
    check('本番で解く順番', s)

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', '鉄びょう', '令和']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
for s in ['コンクリート杭', '鉄鋲', '金属標', '成年被後見人', '成年後見人', '道路境界承諾書', '道路管理図']:
    check('問題文どおりの用語', s)

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
same = []
for i, l in enumerate(lines):
    if l.rstrip() in ('**トリ先生**', '**藍子**'):
        j = i + 2
        while j < len(lines) and (not lines[j].strip() or lines[j].startswith('> 【画像挿入】')):
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続（画像挿入マーカーをはさむものも）: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋添削1＋申請書の完成形1＋問1・問2の欄2＝計{N_FIG + 4}か所の想定）',
      n_marker == N_FIG + 4)
# 記事の画像挿入マーカーの順と zu/ のPNGの対応（マーカーの文言 → PNG）。2026-10-02 追加
ORDER = [('北を上にして座標どおりに描き直した全体図', 'H22_dai21mon_zu01_zentaizu.png'),
         ('帯H→E→F→J→Iの地目の図', 'H22_dai21mon_zu02_obi_chimoku.png'),
         ('問1の整理図', 'H22_dai21mon_zu03_mon1_seiri.png'),
         ('答案用紙（その一）の問1の欄の完成形', 'H22_dai21mon_toukishinseisho_kansei_toi1.png'),
         ('T3からの放射でG点を求める図', 'H22_dai21mon_zu04_G_housha.png'),
         ('T3からの放射でL点を求める図', 'H22_dai21mon_zu05_L_housha.png'),
         ('T1からの放射でF点を求める図', 'H22_dai21mon_zu06_F_housha.png'),
         ('T1からの放射でJ点を求める図', 'H22_dai21mon_zu07_J_housha.png'),
         ('座標変換の確かめの図', 'H22_dai21mon_zu08_zahyou_henkan.png'),
         ('C点の求め方の図', 'H22_dai21mon_zu09_C_heikou.png'),
         ('D点の求め方の図', 'H22_dai21mon_zu10_D_heikou.png'),
         ('K点の求め方の図', 'H22_dai21mon_zu11_K_ten.png'),
         ('答案用紙（その一）の問2の欄の完成形', 'H22_dai21mon_toukishinseisho_kansei_toi2.png'),
         ('(B)(C)の面積の求め方の図', 'H22_dai21mon_zu12_menseki.png'),
         ('伏せてある6番2の地積を出す図', 'H22_dai21mon_zu13_bunpitsumae_chiseki.png'),
         ('誤差の限度の判定図', 'H22_dai21mon_zu14_kousa.png'),
         ('東の道路境界の比較図', 'H22_dai21mon_zu15_kyoukai_hikaku.png'),
         ('新しい地番の図', 'H22_dai21mon_zu16_chiban_6ban4.png'),
         ('分筆後の区画と地番の図', 'H22_dai21mon_zu17_bunpitsu_chiban.png'),
         ('申請人の整理図', 'H22_dai21mon_zu18_souzokunin.png'),
         ('成年後見人の図', 'H22_dai21mon_zu19_kouken.png'),
         ('誤答→添削→正解の3コマ', 'H22_dai21mon_toukishinseisho_machigai.png'),
         ('土地の表示の行ごとの書き方の図', 'H22_dai21mon_zu20_genin.png'),
         ('登記申請書（問3）の完成形', 'H22_dai21mon_toukishinseisho_kansei.png'),
         ('H・Jは筆界点ではない図', 'H22_dai21mon_zu21_HJ.png'),
         ('地積測量図の完成見本', 'H22_dai21mon_zu22_sokuryouzu.png'),
         ('本番で解く順番の図', 'H22_dai21mon_zu23_toku_junban.png')]
mk = [l for l in lines if l.startswith('> 【画像挿入】')]
judge(f'マーカーの数とPNGの対応表の数が同じ（{len(mk)}・{len(ORDER)}）', len(mk) == len(ORDER))
for n_, ((key, png_), m_) in enumerate(zip(ORDER, mk), 1):
    judge(f'マーカー{n_}「{key}」→ {png_}（記事の順）', key in m_ and os.path.exists(os.path.join(HERE, 'zu', png_)))
zu_png = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
judge(f'zu/ のPNGが対応表と過不足なし（{len(zu_png)}枚）', zu_png == sorted(p_ for _, p_ in ORDER))
# まとめの「わな」の一覧の各項目に、記事の中で図があるか（2026-10-05 追加。藍子の誤答のわなに図がなかった6か所を足したときの再発防止）
TRAPS = [('東の道路境界は地積測量図の線', ['問1の整理図', '東の道路境界の比較図']),
         ('帯H→E→F→J→Iは宅地のまま', ['帯H→E→F→J→Iの地目の図']),
         ('向きの注がない放射は時計回りで', ['T3からの放射でG点を求める図', 'T3からの放射でL点を求める図', 'T1からの放射でF点を求める図']),
         ('任意座標は2点で確かめてから平行移動', ['座標変換の確かめの図']),
         ('K点はCが出発点', ['K点の求め方の図']),
         ('伏せてある登記記録の地積は', ['伏せてある6番2の地積を出す図', '誤差の限度の判定図']),
         ('新しい地番は6番4', ['新しい地番の図']),
         ('申請人は6番2を取得した相続人', ['申請人の整理図', '成年後見人の図']),
         ('原因は「③6番2、6番4に分筆」と「6番2から分筆」', ['土地の表示の行ごとの書き方の図']),
         ('地積測量図にH・Jは描かない', ['H・Jは筆界点ではない図'])]
matome = text[text.index('## 第9章'):]
trap_lines = [l for l in matome.splitlines() if l.startswith('- **')]
judge(f'まとめのわなの数と対応表の数が同じ（{len(trap_lines)}・{len(TRAPS)}）', len(trap_lines) == len(TRAPS))
for (head, keys), l in zip(TRAPS, trap_lines):
    judge(f'わな「{head}」に図がある（{"・".join(keys)}）',
          l.startswith('- **' + head) and all(any(k in m_ for m_ in mk) for k in keys))
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成22年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成22年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '登記申請書')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
print('NG件数:', ng)
