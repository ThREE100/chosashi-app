"""令和4年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
答えはアガルートの解答例（第1欄・第2欄・第3欄・第4欄・第5欄）と照合済み。その答えをここで固定して確かめる。
実行: python3 note-articles-Kijyutsu/R4/Q21/verify_R4_dai21mon_kaiwa.py"""
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
judge(f'解説図プロンプトの図の数 {n_fig}枚（12枚）', n_fig == 12)
pngs = os.listdir(os.path.join(HERE, 'zu'))
for i in range(1, 13):
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
# 画像挿入マーカーをはさんで同じ話者が続くのも1つの連続とみなす（2026-10-02追加）
same_m = []
for (i1, s1_), (i2, s2_) in zip(speakers, speakers[1:]):
    j = i1
    while j < len(lines) and not lines[j].rstrip().endswith('」'):
        j += 1
    rest = [x for x in lines[j + 1:i2 - 1] if x.strip()]
    if s1_ == s2_ and rest and all(x.startswith('> 【画像挿入】') for x in rest):
        same_m.append(i2)
judge(f'同じ話者のセリフが画像挿入マーカーだけをはさんで続いていない: {same_m}', not same_m)
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図12＋添削1＋完成形1＋第1欄・第2欄・第5欄3＝計17か所の想定）', n_marker == 17)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和4年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和4年度問題21（土地）', thumb, '見出し画像')
check('添削画像の記事タイトル', title[2:], fix, '添削')

# ---- 追加作業（2026-09-29）：予備校の解説と見比べて足した観点 ----
check('（イ）を対角線どうしで（別解）', '（イ）の倍面積 ＝ Conjg(I − C) × (D − J)')
check('（イ）の対角線の式の表示', '表示：' + disp((I - C).conjugate() * (D - J)))
judge('対角線の式と4点の式のiの係数が同じ', abs(((I - C).conjugate() * (D - J)).imag - s1.imag) < 1e-9)
check('問2・問5を先に埋める', '本番では問題を開いたら、先にこの2つを埋めておくのよ')
for s_ in ['306.89 − 279.30 ＝ 27.59m', '305.35 − 272.19 ＝ 33.16m', '縦約11cm、横約13cm']:
    check('地積測量図の大きさ', s_)
judge('T1〜南の筆界 27.59m・T2〜T1 33.16m', abs(T1.real - C.real - 27.59) < 1e-9 and abs(T1.imag - T2.imag - 33.16) < 1e-9)
for s_ in ['- **1番目（計算なし）**', '- **2番目（読解）**', '- **3番目（計算）**', '- **4番目（作図）**',
           'いちばん時間を食うのは、（ロ）の5点の面積と、11本の辺長と、筆界の裏付け']:
    check('時間配分と解く順番', s_)

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['R4_dai21mon_toukishinseisho_kansei', 'R4_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長・横1200px（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'R4_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'R4_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s_ in ['土地一部地目変更・分筆登記', '地積測量図　代理権限証書', '令和４年10月14日　申請　Ａ地方法務局', 'Ａ市Ｃ台206番地３　春野朝子',
           '金3,000円', 'Ａ市Ｂ字八幡', '184番１', '584', '75', '（イ）', '212', '23', '令和４年10月５日一部地目変更',
           '③184番１、184番３、184番４に分筆', '（ロ）184番３', '雑種地', '357', '（ハ）184番４', '15', '06', '184番１から分筆']:
    check('完成形の画像（HTML）', s_, html_k, '完成形画像')
    check('完成形の画像の記入データがプロンプトにある', s_, form, '登記申請書')
absent('完成形の画像に「（略）」の結合セルがない（R4の答案用紙は5行とも地積を書く）', 'class="ryaku" colspan', html_k, '完成形画像')
for s_ in ['①誤答', '②添削（赤ペン）', '③正解', '土地分筆登記', '土地一部地目変更・分筆登記', '令和４年10月５日一部地目変更',
           '中央部分は10月5日から月極駐車場＝雑種地。一部地目変更も一緒に申請', '一部地目変更は（イ）の行に日付付きで。雑種地は1㎡未満切捨て']:
    check('添削の画像（HTML）', s_, html_m, '添削画像')
    check('添削の画像の文言がプロンプトにある', s_, fix, '添削')
check('添削のプロンプトは縦に積む', '3コマを縦に積んだ縦長', fix, '添削')
absent('添削のプロンプトに横並びの旧版の指示がない', '横に3コマ並べる', fix, '添削')
absent('添削のプロンプトに記号「✓」がない', '✓', fix, '添削')
n_fit = len(re.findall(r'^\s*fit\(', draw, re.M))
judge(f'作図スクリプトの表示範囲はすべて fit(..., pad_aspect=True)（{n_fit}か所）',
      n_fit > 0 and n_fit == len(re.findall(r'^\s*fit\(.*pad_aspect=True\)', draw, re.M)))
for s_ in ['拡幅前の道路の線（位置は模式）', '側溝（位置は模式）']:
    check('座標のないものは模式と書く', s_, draw, '作図')
    check('座標のないものは模式と書く', s_, fig, '解説図')

# ---- 注の番号の書き分け（問題文の注・調査図素図の注・観測値の表の注） ----
bare = [text[max(0, m.start() - 6):m.end()] for m in re.finditer(r'注[0-9]', text)
        if not re.search(r'(問題文の|調査図素図の|観測値〕の)$', text[max(0, m.start() - 8):m.start()])]
judge(f'注の番号はすべて書き分けている（書き分けていないもの: {bare}）', not bare)
bare_fig = [m.group(0) for m in re.finditer(r'(?<!問題文の)注[57]', draw)]
judge(f'作図の説明文の注も「問題文の注N」（{bare_fig}）', not bare_fig)


# ---- 2026-10-02 追加：穴埋めの答えの語を会話で言っているか ----
for s_ in ['だから（ア）は『表題登記』', '（イ）は『隣接』です', '（ウ）は『筆界の現地における（ウ）を特定すること』だから『位置』', '「『範囲』です！」',
           'だから①②③は、日時・場所・その状況です', '「④は『申請の権限』、⑤は『登記名義人』です！」',
           '「第1欄は、I点（300.13, 293.12）、J点（279.30, 293.12）です！」']:
    check('答えの語を会話で言っている', s_)

# ---- 2026-10-02 追加：記事の画像挿入マーカーと zu/ のPNGが記事の順に対応しているか ----
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R4_dai21mon_zu01_zentaizu', '北を上にして座標どおりに描き直した全体図', 'fig'),
        ('R4_dai21mon_zu02_hikkai_hikaku', 'AB線とE→F→Gの比較図', 'fig'),
        ('R4_dai21mon_zu03_gouseizu', '合成図の辺長で筆界を裏付ける図', 'fig'),
        ('R4_dai21mon_zu04_P_housha', 'T1からの放射でP点を求める図', 'fig'),
        ('R4_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R4_dai21mon_zu05_I_J', 'I点とJ点の求め方の図', 'fig'),
        ('R4_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R4_dai21mon_zu06_hikkai_tokutei', '筆界特定の穴埋めの図', 'fig'),
        ('R4_dai21mon_zu07_bunpitsu_chiban', '分筆後の区画と地番・地目の図', 'fig'),
        ('R4_dai21mon_zu08_taikakusen', '（イ）の面積を対角線で出す別解の図', 'fig'),
        ('R4_dai21mon_zu09_kousa', '地積更正が要るかの判定図', 'fig'),
        ('R4_dai21mon_toukishinseisho_machigai', '誤答→添削→正解の3コマ', 'tall'),
        ('R4_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R4_dai21mon_zu10_chiseki_sokuryouzu', '地積測量図（184番1・184番3・184番4）の完成見本', 'fig'),
        ('R4_dai21mon_dai5ran_kansei', '第5欄（問5）の完成形', 'wide'),
        ('R4_dai21mon_zu11_honnin_kakunin', '本人確認情報の穴埋めの図', 'fig'),
        ('R4_dai21mon_zu12_kaku_junban', '本番で解く順番の図', 'fig')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
for (name, key, kind), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = struct.unpack('>II', open(path, 'rb').read()[16:24])
        ok = (w == 1200 and h > w) if kind == 'tall' else (w == 1200 and h < w) if kind == 'wide' else w >= 1200
    judge(f'PNG（マーカー順・大きさ） : {name}', ok)
    src = fig if '_zu' in name else (fix if 'machigai' in name else form)
    judge(f'プロンプトにファイル名 : zu/{name}.png', f'zu/{name}.png' in src)
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない : {extra}', not extra)
for name, needles in [('R4_dai21mon_dai1ran_kansei', ['第1欄', 'Ｉ点', 'Ｊ点', '300.13', '279.30', '293.12', 'Ｘ座標（ｍ）']),
                      ('R4_dai21mon_dai2ran_kansei', ['第2欄', '表題登記', '隣接', '位置', '範囲']),
                      ('R4_dai21mon_dai5ran_kansei', ['第5欄', '日時', '場所', 'その状況', '申請の権限', '登記名義人', '①〜③は順不同'])]:
    h_ = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n_ in needles:
        check(f'{name}.html', n_, h_, '解答欄の画像')
for s_ in ['「Ｉ点」「300.13」「293.12」', '「Ｊ点」「279.30」「293.12」', '「ア」「表題登記」「イ」「隣接」／「ウ」「位置」「エ」「範囲」',
           '「⑤」「登記名義人」', '仮のもの']:
    check('解答欄の画像のプロンプト', s_, form, '登記申請書')
check('図8の説明文', 'Conjg(I − C) × (D − J) ＝ 355.7164 ＋ 424.467i', draw, '作図')
check('図8の説明文（プロンプト）', 'Conjg(I − C) × (D − J) ＝ 355.7164 ＋ 424.467i', fig, '解説図')
judge('図8の（ハ）の対角線の式も15.0604', abs(abs(((H - E).conjugate() * (F - A)).imag) / 2 - 15.0604) < 1e-9)
check('図12（プロンプト）', '①問2・問5（計算なし）', fig, '解説図')
check('図10の作図範囲', 'T1・T2まで入れると南北27.59m・東西33.16m（1/250で縦約11cm・横約13cm）', draw, '作図')
check('作図の図の番号（図12）', "'図12　本番で解く順番", draw, '作図')
bare_p = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)注[0-9]', fig.split('## 差し替えデータ')[-1])]
judge(f'解説図プロンプトの差し替えデータの注も書き分けている（{bare_p}）', not bare_p)
bare_f = [m.group(0) for m in re.finditer(r'(?<!問題文の)注[0-9]', form)]
judge(f'申請書のプロンプトの注も書き分けている（{bare_f}）', not bare_f)

for q in re.findall(r'\*\*記事の挿入位置\*\*：[^「\n]*「([^」]+)」', fig):
    check('解説図の挿入位置の引用', q, None, '記事（図の挿入位置）')

print('NG件数:', ng)
