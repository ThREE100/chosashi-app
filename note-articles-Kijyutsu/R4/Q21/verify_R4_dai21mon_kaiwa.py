"""令和4年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
答えはアガルートの解答例（第1欄・第2欄・第3欄・第4欄・第5欄）と照合済み。その答えをここで固定して確かめる。
実行: python3 note-articles-Kijyutsu/R4/Q21/verify_R4_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R4_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_R4_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R4_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R4_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R4_dai21mon_miidashi_gazou.md')
draw = rd(os.path.join('zu', 'draw_R4_dai21mon_kaisetsuzu.py'))
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


def im_disp(s):
    """多角形の倍面積の表示（実部は書かず、iの係数だけ）。"""
    return f'表示：（実部）{"−" if s.imag < 0 else "＋"} {fmt_num(abs(s.imag))}i'


# ---- 座標（問題文の〔測量によって得られた座標値〕と基準点成果表） ----
A, B, C, D = P(298.21, 273.89), P(279.30, 274.90), P(279.30, 303.07), P(301.13, 303.07)
E, F, G, H = P(298.09, 272.68), P(289.14, 272.74), P(279.30, 279.15), P(286.41, 274.52)
T1, T2 = P(306.89, 305.35), P(303.64, 272.19)
judge('B・G・C は X＝279.30、C・D は Y＝303.07（軸に平行）', B.real == G.real == C.real and C.imag == D.imag)
judge('H はAB線とFGの交点（外積がほぼ0）', abs(((B - A).conjugate() * (H - A)).imag) < 0.01
      and abs(((G - F).conjugate() * (H - F)).imag) < 0.02)

# ---- 第2章 筆界（AB線とE→F→G） ----
s_ab = double_area_sum([A, D, C, B])
check('AB線の四角形 表示', im_disp(s_ab))
check('AB線の四角形 面積', f'{area([A, D, C, B]):.5f}㎡')
s_hon = double_area_sum([E, D, C, G, F])
check('本件土地 表示', im_disp(s_hon))
check('本件土地 面積', f'{area([E, D, C, G, F]):.4f}㎡')
check('西側E・A・H・F 表示', im_disp(double_area_sum([E, A, H, F])))
check('西側E・A・H・F 面積', f'{area([E, A, H, F]):.4f}㎡')
check('△HBG 表示', '表示：' + disp((B - H).conjugate() * (G - H)))
check('△HBG 面積', f'{area([H, B, G]):.5f}㎡')
check('交換の面積（切捨て）', f'西側で{chiseki(area([E, A, H, F])):.2f}㎡はみ出して、南西で{chiseki(area([H, B, G])):.2f}㎡へこんで')
Dp = D + 1.49
check('FD′ 表示', '表示：' + fmt_num(abs(Dp - F)))
check('GD′ 表示', '表示：' + fmt_num(abs(Dp - G)))
judge('合成図の33.19・33.41と一致', round(abs(Dp - F), 2) == 33.19 and round(abs(Dp - G), 2) == 33.41)
judge('D′B は36.57（合成図にない）', round(abs(Dp - B), 2) == 36.57)

# ---- 問1 P点・I点・J点 ----
check('arg(T2−T1)', to_dms(cmath.phase(T2 - T1)))
check('arg＋360°', to_dms(cmath.phase(T2 - T1) + 2 * math.pi))
check('方向の合計', to_dms(cmath.phase(T2 - T1) + dms(338, 29, 30)))
Pr = radial(T1, T2, 13.74, dms(338, 29, 30))
check('P 表示', '表示：' + disp(Pr))
Pp = r2(Pr)
check('P の丸め', f'（{Pp.real:.2f}, {Pp.imag:.2f}）')
Pw = r2(T1 + cmath.rect(13.74, cmath.phase(T2 - T1) - dms(338, 29, 30)))
check('反時計回りの誤り', f'（{Pw.real:.2f}, {Pw.imag:.2f}）')
judge('誤りの点はT1より北（道路の向こう側）', Pw.real > T1.real)
check('20.44・30.39', f'{Pp.imag - E.imag:.2f} ÷ {D.imag - E.imag:.2f}')
Ir = E + (D - E) * (Pp.imag - E.imag) / (D.imag - E.imag)
check('I 表示', '表示：' + disp(Ir))
I = r2(Ir)
J = P(C.real, Pp.imag)
check('I 答え', '**▶ I点（300.13, 293.12）**')
check('J 答え', '**▶ J点（279.30, 293.12）**')
judge('I・J は解答例と一致', abs(I - P(300.13, 293.12)) < 1e-9 and abs(J - P(279.30, 293.12)) < 1e-9)
check('IP 表示', '表示：' + fmt_num(abs(Pp - I)))
check('P点を答えにした誤り', f'I点はP点と同じ（{Pp.real:.2f}, {Pp.imag:.2f}）')
judge('IJ は BC に直交（IJは真北向き）', I.imag == J.imag)

# ---- 問2 ----
for s in ['- **ア**：表題登記', '- **イ**：隣接', '- **ウ**：位置', '- **エ**：範囲']:
    check('問2', s)
check('問2の誤答', '（ア）は『所有権の登記』ですか？')

# ---- 問3 ----
s1 = double_area_sum([C, D, I, J])
check('（イ） 表示', im_disp(s1))
check('（イ） 面積', f'{area([C, D, I, J]):.4f}㎡')
s3 = double_area_sum([A, I, J, G, H])
check('（ロ） 表示', im_disp(s3))
check('（ロ） 面積', f'{area([A, I, J, G, H]):.5f}㎡')
tot = area([C, D, I, J]) + area([A, I, J, G, H]) + area([E, A, H, F])
check('3筆の合計', f'{tot:.5f}㎡')
judge('（イ）212.23・（ロ）357（雑種地）・（ハ）15.06', chiseki(area([C, D, I, J])) == 212.23
      and chiseki(area([A, I, J, G, H]), takuchi=False) == 357 and chiseki(area([E, A, H, F])) == 15.06)
check('（ロ）を宅地のまま切り捨てた誤り', f'（ロ）は{chiseki(area([A, I, J, G, H])):.2f}㎡です！')
check('差（1筆）', f'差は{area([E, D, C, G, F]) - 584.75:.2f}㎡')
check('差（3筆）', f'差は{abs(tot - 584.75):.2f}㎡')
judge('公差（乙1 7.17）の範囲内', abs(area([E, D, C, G, F]) - 584.75) < 7.17 and abs(tot - 584.75) < 7.17)
check('精度区分の誤答（甲2）', '市街地地域の甲2、2.39㎡です！')
check('精度区分（乙1）', '7.17㎡')
check('登録免許税の誤答', '金2,000円です！')
for s in ['- **登記の目的**：土地一部地目変更・分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **申請人**：A市C台206番地3　春野朝子', '- **登録免許税**：金3,000円', '- **所在**：A市B字八幡',
          '①184番1、②宅地、③584.75（登記記録の地積）、登記原因は空欄',
          '①（イ）、③212.23、登記原因「令和4年10月5日一部地目変更　③184番1、184番3、184番4に分筆」',
          '①（ロ）184番3、②雑種地、③357、登記原因「184番1から分筆」',
          '①（ハ）184番4、②宅地、③15.06、登記原因「184番1から分筆」']:
    check('問3', s)

# ---- 問4 辺長 ----
SIDES = {'EA': (E, A), 'AI': (A, I), 'ID': (I, D), 'DC': (D, C), 'CJ': (C, J), 'JG': (J, G), 'GH': (G, H),
         'HF': (H, F), 'FE': (F, E), 'IJ（分筆線）': (I, J), 'AH（分筆線）': (A, H)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
for p, q in [(A, E), (I, A), (D, I), (H, G), (F, H), (E, F), (H, A)]:
    check('辺長の表示', '表示：' + fmt_num(abs(p - q)))
for s in ['DC ＝ 301.13 − 279.30 ＝ 21.83', 'CJ ＝ 303.07 − 293.12 ＝ 9.95', 'JG ＝ 293.12 − 279.15 ＝ 13.97',
          'IJ ＝ 300.13 − 279.30 ＝ 20.83']:
    check('軸に平行な辺', s)
check('四捨五入の境目（AI）', 'AIは19.3256')
check('地番欄', '地番欄は184番1、184番3、184番4')
check('境界標', '境界標（A・C・Jは金属標、D・E・F・G・Iはコンクリート杭）')

# ---- 問5 ----
for s in ['- **①**：日時', '- **②**：場所', '- **③**：その状況', '- **④**：申請の権限', '- **⑤**：登記名義人']:
    check('問5', s)

# ---- 変数の割り当て（割り当て表・電卓操作の見出し・キー操作の一致） ----
for s in ['- **B**：B点（第2章の後は、T2に使い回す。さらにP点を出した後は、I点に使い回す）',
          '- **C**：C点（第6章で（イ）の面積を出した後は、H点に使い回す）',
          '- **X**：G点', '- **Y**：H点（第2章の後は、T1に使い回す。さらにP点、J点の順に使い回す）',
          '電卓操作（Y＝T1、B＝T2）', '電卓操作（B＝I、Y＝P）', '電卓操作（B＝I、Y＝J）',
          '電卓操作（B＝I、Y＝J、X＝G、C＝H）', '電卓操作（B＝I、X＝G、C＝H）',
          '303.64 [+] 272.19 [i] [SHIFT] [STO] [B]', '300.13 [+] 293.12 [i] [SHIFT] [STO] [B]',
          '279.30 [+] 293.12 [i] [SHIFT] [STO] [Y]', '286.41 [+] 274.52 [i] [SHIFT] [STO] [C]']:
    check('変数', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（10枚）', n_fig == 10)
pngs = os.listdir(os.path.join(HERE, 'zu'))
for i in range(1, 11):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R4_dai21mon_zu{i:02d}_') and f.endswith('.png') for f in pngs))
for s in ['584.84㎡', '584.82㎡', '15.06㎡', '15.10㎡', '33.19', '33.41', '36.57', '（300.63, 293.12）',
          '（300.13, 293.12）', '（279.30, 293.12）', '（310.66, 292.14）', '264°24′08.42″', '338°29′30″',
          '242°53′38.42″', '212.23㎡', '357㎡', '584.8248㎡', '584.73805㎡', '7.17', 'IP ＝ 0.50']:
    check('図の数値', s, fig, '解説図')
    check('図の数値（作図スクリプト）', s, draw, '作図')
for s in ['土地一部地目変更・分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｃ台206番地３　春野朝子', '金3,000円',
          '令和４年10月14日　申請　Ａ地方法務局', 'Ａ市Ｂ字八幡', '令和４年10月５日一部地目変更',
          '③184番１、184番３、184番４に分筆', '（ロ）184番３', '雑種地', '「357｜」', '（ハ）184番４', '「15｜06」',
          '「212｜23」', '「584｜75」', '184番１から分筆']:
    check('登記申請書', s, form, '登記申請書')
for s in ['土地分筆登記', '土地一部地目変更・分筆登記', '令和４年10月５日一部地目変更', '「357｜44」', '雑種地']:
    check('添削', s, fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
speakers = [(i + 1, l.rstrip()) for i, l in enumerate(lines) if l.rstrip() in ('**トリ先生**', '**藍子**')]
same = []
for (i1, s1_), (i2, s2_) in zip(speakers, speakers[1:]):
    between = lines[i1:i2 - 1]
    if s1_ == s2_ and not any(x.startswith(('## ', '```', '表示：', '- ', '> ')) for x in between):
        same.append(i2)
judge(f'同じ話者のセリフが地の文なしで続いていない: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図10＋添削1＋完成形1＝計12か所の想定）', n_marker == 12)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和4年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和4年度問題21（土地）', thumb, '見出し画像')
check('添削画像の記事タイトル', title[2:], fix, '添削')

print('NG件数:', ng)
