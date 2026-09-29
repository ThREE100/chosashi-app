"""令和7年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の数値は、アガルートの解答例と照合済みのプロース版（note_R7_dai21mon_tochi_kijutsu_kaisetsu.md）と同じ答えになることも確認する。
実行: python3 note-articles-Kijyutsu/R7/Q21/verify_R7_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, tri_conj, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R7_dai21mon_tochi_kaiwa_kaisetsu.md')
prose = rd('note_R7_dai21mon_tochi_kijutsu_kaisetsu.md')
fig = rd('prompt_R7_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R7_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R7_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R7_dai21mon_miidashi_gazou.md')
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


# ---- 座標（問題文の〔測量によって得られた座標値〕と基準点成果表） ----
T1, T2 = P(185.31, 135.37), P(188.60, 92.18)
A, B, C = P(184.31, 99.33), P(219.57, 99.33), P(219.57, 117.56)
E, F, G, H = P(184.31, 114.41), P(184.31, 130.08), P(193.50, 131.88), P(217.00, 131.88)

# ---- 問1 D点（放射。観測角は時計回り＝足す） ----
check('arg(T1−T2)', to_dms(cmath.phase(T1 - T2)))
Dr = radial(T2, T1, 25.81, dms(325, 6, 51))
check('D 表示', '表示：' + disp(Dr))
D = r2(Dr)
check('D 答え', '**▶ D点（201.71, 114.41）**')
Dw = r2(T2 + cmath.rect(25.81, cmath.phase(T1 - T2) - dms(325, 6, 51)))
check('反時計回りの誤り', f'（{Dw.real:.2f}, {Dw.imag:.2f}）')
check('T2→Dの方向角', '59°28′12.94″')
judge('T2→Dの方向角（丸める前のDで） 59°28′12.94″', to_dms(cmath.phase(T1 - T2) + dms(325, 6, 51) - 2 * math.pi) == '59°28′12.94″')

# ---- 筆界点Dの裏付け（甲土地の地積） ----
s5 = double_area_sum([A, B, C, D, E])
check('甲土地 表示', f'表示：（実部）− {fmt_num(abs(s5.imag))}i')
check('甲土地 面積', f'{area([A, B, C, D, E]):.4f}㎡')
judge('甲土地の地積（畑は1㎡未満切捨て）＝ 登記記録 559', chiseki(area([A, B, C, D, E]), takuchi=False) == 559)
check('CE直線の甲土地（小数第2位未満切捨てで表示）', f'{chiseki(area([A, B, C, E])):.2f}㎡')
for v in [area([A, B, C, E]), area([C, H, G, F, E]), area([A, B, C, D, E]), area([C, H, G, F, E, D])]:
    check('図3の面積（小数第2位未満切捨てで表示）', f'{chiseki(v):.2f}㎡', fig, '解説図')

# ---- 問1 K点 ----
s6 = double_area_sum([C, H, G, F, E, D])
check('乙土地 表示', f'表示：（実部）− {fmt_num(abs(s6.imag))}i')
S = area([C, H, G, F, E, D])
check('乙土地 面積', f'{S:.4f}㎡')
check('△DCH 表示', '表示：' + disp(tri_conj(D, C, H)))
check('HK 表示', '表示：' + fmt_num((561.1905 / 2 - 131.92535) * 2 / 17.47))
hkw = (278 - 131.92535) * 2 / 17.47
check('278で割った誤りのHK', f'HKは{round(hkw, 2):.2f}')
check('278で割った誤りのK', f'（{H.real - round(hkw, 2):.2f}, 131.88）')
K = r2(H - round((S / 2 - area([D, C, H])) * 2 / (H.imag - D.imag), 2))
check('K 表示', '表示：' + disp(K))
check('K 答え', '**▶ K点（199.98, 131.88）**')
check('10番1 表示', f'表示：（実部）− {fmt_num(abs(double_area_sum([C, H, K, D]).imag))}i')
check('10番2 面積', f'{area([D, K, G, F, E]):.5f}㎡')
judge('10番1・10番2の地積 280.59', chiseki(area([C, H, K, D])) == 280.59 == chiseki(area([D, K, G, F, E])))

# ---- 問2 ----
for s in ['- **ア**：280.59', '- **イ**：2.32', '- **ウ**：超えています', '- **エ**：錯誤', '- **オ**：土地の地積の更正',
          '- **カ**：必要があります']:
    check('問2', s)
check('差', f'{S - 556.00:.2f}㎡')

# ---- 問3 辺長 ----
SIDES = {'CH': (C, H), 'HK': (H, K), 'KG': (K, G), 'GF': (G, F), 'FE': (F, E), 'ED': (E, D), 'DC': (D, C)}
for n, (p, q) in SIDES.items():
    check(f'辺長{n}', f'- **{n}**：{round(abs(p - q) + 1e-9, 2):.2f}')
check('辺長DK', f'- **DK（分筆線）**：{round(abs(K - D), 2):.2f}')
for n, (p, q) in {**SIDES, 'DK': (D, K)}.items():
    check(f'図の辺長{n}', f'{round(abs(p - q) + 1e-9, 2):.2f}', fig, '解説図')

# ---- 問4 J点・L点（延長線の交点Oで相似） ----
I = B - 3.5
J = C + (D - C) * 3.5 / 17.86
check('J 表示', '表示：' + disp(J))
J = r2(J)
check('J 答え', '**▶ J点（216.07, 116.94）**')
judge('BCJI ＝ 62.72', abs(area([B, C, J, I]) - 62.72) < 1e-9)
O = D + (C - D) * 17.47 / 3.15
check('O 表示', '表示：' + disp(O))
odk = ((O - K) * 17.47 / 2).real
check('△ODK 表示', '表示：' + fmt_num(odk))
k = math.sqrt((880.3318 - 62.72) / 880.3318)   # 記事どおり小数第4位まで打ち込んだ値
check('k 表示', '表示：' + fmt_num(k))
L, M = O + (K - O) * k, O + (D - O) * k
check('L 表示', '表示：' + disp(L))
check('M 表示', '表示：' + disp(M))
L, M = r2(L), r2(M)
check('L 答え', '**▶ L点（203.64, 131.88）**')
check('M', '（205.30, 115.04）')
check('MLKD', f'{area([M, L, K, D]):.4f}㎡')
check('CHLM', f'{area([C, H, L, M]):.4f}㎡')
judge('MLKD の地積 62.72（BCJI と等積）', chiseki(area([M, L, K, D])) == 62.72)
check('ML', f'ML ＝ {abs(L - M):.2f}')
check('KL', f'KL ＝ {abs(L - K):.2f}')

# ---- プロース版（アガルート照合済み）と同じ答えか ----
for s in ['（201.71, 114.41）', '（199.98, 131.88）', '（216.07, 116.94）', '（203.64, 131.88）', '2.32', '錯誤',
          'S市T町一丁目10番1号　甲野一郎', '金2,000円', '③10番1、10番3に分筆', '10番1から分筆']:
    check('プロース版と共通の答え', s, prose, 'プロース版')
    check('プロース版と共通の答え', s)

# ---- 問5 ----
for s in ['- **登記の目的**：土地分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **申請人**：S市T町一丁目10番1号　甲野一郎', '- **登録免許税**：金2,000円', '- **所在**：S市T町一丁目',
          '①10番1、②宅地、③280.59', '①（イ）、登記原因「③10番1、10番3に分筆」',
          '①（ロ）10番3、②宅地、登記原因「10番1から分筆」']:
    check('問5', s)
check('（イ）の地積', f'（イ）{chiseki(area([C, H, L, M])):.2f}㎡')
judge('10月の分筆後の合計と登記記録の差 0.03 ＜ 甲2の公差（約1.52）',
      abs(chiseki(area([C, H, L, M])) + chiseki(area([M, L, K, D])) - 280.59 - 0.03) < 1e-9
      and (0.05 + 0.01 * 280.59 ** 0.25) * math.sqrt(280.59) > 0.03)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（9枚）', n_fig == 9)
for i in range(1, 10):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R7_dai21mon_zu0{i}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
for s in ['Ｓ市Ｔ町一丁目10番１号　甲野一郎', '地積測量図　代理権限証書', '金2,000円', '③10番１、10番３に分筆']:
    check('登記申請書', s, form, '登記申請書')
for s in ['Ｓ市Ｔ町一丁目10番１号　甲野一郎', '地積測量図　代理権限証書', 'Ｓ市Ｍ町二丁目３番５号']:
    check('添削', s, fix, '添削')

# ---- 分筆後の地積の合計でも公差と比べる（準則第72条第1項） ----
check('分筆後の合計', '280.59 ＋ 280.59 ＝ 561.18㎡')
judge('合計561.18と556.00の差5.18 ＞ 甲2の公差2.32', abs(2 * chiseki(area([C, H, K, D])) - 556.00 - 5.18) < 1e-9 and 5.18 > 2.32)
check('合計との差', '差は5.18㎡')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['R7_dai21mon_toukishinseisho_kansei', 'R7_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長・横1200px（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'R7_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'R7_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['土地分筆登記', '地積測量図　代理権限証書', '令和７年10月30日　申請　Ｓ地方法務局', 'Ｓ市Ｔ町一丁目10番１号　甲野一郎',
          '金2,000円', 'Ｓ市Ｔ町一丁目', '10番１', '280', '59', '（イ）', '③10番１、10番３に分筆', '（ロ）10番３', '10番１から分筆',
          '（略）']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
    check('完成形の画像の記入データがプロンプトにある', s, form, '登記申請書')
for s in ['①誤答', '②添削（赤ペン）', '③正解', '住所証明情報', 'Ｓ市Ｍ町二丁目３番５号', 'Ｓ市Ｔ町一丁目10番１号',
          '登記記録の住所と一致するので、住所の証明は要らない', '10月20日に住所変更登記が完了済み！登記記録の住所はもう新住所',
          '令和７年10月30日　申請　Ｓ地方法務局']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
    check('添削の画像の文言がプロンプトにある', s, fix, '添削')
check('添削のプロンプトは縦に積む', '3コマを縦に積んだ縦長', fix, '添削')
absent('添削のプロンプトに横並びの旧版の指示がない', '左から「①誤答」', fix, '添削')
draw = open(os.path.join(HERE, 'zu', 'draw_R7_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
n_fit = len(re.findall(r'^\s*fit\(', draw, re.M))
judge(f'作図スクリプトの表示範囲はすべて fit(..., pad_aspect=True)（{n_fit}か所）',
      n_fit > 0 and n_fit == len(re.findall(r'^\s*fit\(.*pad_aspect=True\)', draw, re.M)))

# ---- 試験問題の本文（2026-09-29にユーザーから受領）と照らした文言 ----
check('観測値の表の注1', '観測値の表の注1を読んだ？『観測角は、時計回りの角度を示す』')
absent('（オ）を略した答え', '- **オ**：地積更正')
for s in ['（201.71, 114.41）', '（199.98, 131.88）', '（216.07, 116.94）', '（203.64, 131.88）', '- **ア**：280.59', '- **イ**：2.32',
          '- **ウ**：超えています', '- **エ**：錯誤', '- **オ**：土地の地積の更正', '- **カ**：必要があります',
          '- **CH**：14.55', '- **HK**：17.02', '- **KG**：6.48', '- **GF**：9.36', '- **FE**：15.67', '- **ED**：17.40', '- **DC**：18.14',
          '- **DK（分筆線）**：17.56']:
    check('アガルートの解答例（第1欄〜第5欄）と同じ答え', s)

# ---- 注の番号の書き分け（問題文の注・観測値の表の注） ----
bare = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!観測値の表の)注[0-9]', text)]
judge(f'注の番号はすべて「問題文の注N」と書き分けている（書き分けていないもの: {bare}）', not bare)

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'D点のくい', 'とくいD', '点にくいが']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
seq = [(i, l.rstrip()) for i, l in enumerate(lines) if l.strip()]
dup = [seq[k][0] + 1 for k in range(1, len(seq)) if seq[k][1] in ('**トリ先生**', '**藍子**')
       and k >= 2 and seq[k - 2][1] == seq[k][1] and seq[k - 1][1].startswith('「')]
judge(f'同じ話者のセリフが間に何も挟まずに続いていない: {dup}', not dup)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図9＋添削1＋完成形1＝計11か所の想定）', n_marker == 11)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和7年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和7年度問題21（土地）', thumb, '見出し画像')

# ---- K点の別解（面積の比）と、アガルートの解説と照らして足した要点（2026-09-29） ----
q_dgfe = area([D, G, F, E])
t_dhk, t_dkg = S / 2 - area([D, C, H]), S / 2 - q_dgfe
check('四角形DGFE', f'{q_dgfe:.5f}㎡')
check('△DKG', f'{t_dkg:.4f}㎡')
check('面積の比', f'{t_dhk:.4f}：{t_dkg:.4f}')
kg = abs(H - G) * t_dkg / (t_dhk + t_dkg)
check('KG（面積の比）', f'KGは{fmt_num(kg)}')
judge('面積の比でも K（199.98, 131.88）', r2(G + (H - G) / abs(H - G) * kg) == K)
check('10月は相続を証する情報が要らない', '相続を証する情報は要りません')
check('所有権に関する登記の完了日', '9月20日に完了')
check('地積測量図の町界', '町界（C点の北とE点の南へ一点鎖線で延ばす）')
check('L点は最後に', '**L点は最後に回す**')

print('NG件数:', ng)
