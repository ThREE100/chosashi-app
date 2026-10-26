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
judge(f'解説図プロンプトの図の数 {n_fig}枚（32枚）', n_fig == 32)
ZU = os.path.join(HERE, 'zu')
lines = text.splitlines()
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
# 画像挿入マーカー（記事の順）と PNG の対応。kind: fig=解説図（横1200px以上）、wide=解答欄（横長）、tall=申請書・添削（縦長）
PNGS = [('R4_dai21mon_zu01_jikeiretsu', '時系列の図', 'fig'),
        ('R4_dai21mon_zu02_chuu_shiwake', '注の仕分けの図', 'fig'),
        ('R4_dai21mon_zu03_zentaizu', '北を上にして座標どおりに描き直した全体図', 'fig'),
        ('R4_dai21mon_zu04_zahyouhou_ab_efg', '座標法の計算過程の図', 'fig'),
        ('R4_dai21mon_zu05_nishigawa_hbg', '西側の部分E・A・H・Fと△HBGの面積の図', 'fig'),
        ('R4_dai21mon_zu06_hikkai_hikaku', 'AB線とE→F→Gの比較図', 'fig'),
        ('R4_dai21mon_zu07_gouseizu', '合成図の辺長で筆界を裏付ける図', 'fig'),
        ('R4_dai21mon_zu08_shoyuukenkai_hikkai', '筆界は合意では動かないことの図', 'fig'),
        ('R4_dai21mon_zu09_P_housha', 'T1からの放射でP点を求める図', 'fig'),
        ('R4_dai21mon_zu10_J_ten', 'J点の求め方の図', 'fig'),
        ('R4_dai21mon_zu11_I_ten', 'I点の求め方の図', 'fig'),
        ('R4_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R4_dai21mon_zu12_hikkai_tokutei', '筆界特定の穴埋めの図', 'fig'),
        ('R4_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R4_dai21mon_zu13_chimoku_3bubun', 'どの部分の地目が変わったかの図', 'fig'),
        ('R4_dai21mon_zu14_mokuteki', '登記の目的の図', 'fig'),
        ('R4_dai21mon_toukishinseisho_machigai_mokuteki', '登記申請書「登記の目的」欄の誤答→添削→正解の3コマ', 'tall'),
        ('R4_dai21mon_zu15_chiban_chuu7', '分筆後の地番の図', 'fig'),
        ('R4_dai21mon_zu16_i_menseki_4kou', '（イ）184番1の面積の計算過程の図', 'fig'),
        ('R4_dai21mon_zu17_taikakusen', '（イ）の面積を対角線で出す別解の図', 'fig'),
        ('R4_dai21mon_zu18_ro_menseki_5kou', '（ロ）184番3の面積の計算過程の図', 'fig'),
        ('R4_dai21mon_zu19_hasuu', '地積の端数処理の図', 'fig'),
        ('R4_dai21mon_zu20_seido_kubun', '精度区分は地域で決まることの図', 'fig'),
        ('R4_dai21mon_zu21_kousa', '地積更正が要るかの判定図', 'fig'),
        ('R4_dai21mon_zu22_bunpitsumae_chiseki', '分筆前の行の地積の図', 'fig'),
        ('R4_dai21mon_toukishinseisho_machigai_chiseki1', '登記申請書「土地の表示」の1行目の誤答→添削→正解の3コマ', 'tall'),
        ('R4_dai21mon_zu23_i_gyou_genin', '（イ）の行の原因の図', 'fig'),
        ('R4_dai21mon_toukishinseisho_machigai_i_genin', '登記申請書「土地の表示」（イ）の行の原因の誤答→添削→正解の3コマ', 'tall'),
        ('R4_dai21mon_zu24_ro_gyou_chimoku', '（ロ）の行の地目の図', 'fig'),
        ('R4_dai21mon_toukishinseisho_machigai_ro', '登記申請書「土地の表示」（ロ）の行の地目の誤答→添削→正解の3コマ', 'tall'),
        ('R4_dai21mon_zu25_tourokumenkyozei', '登録免許税の図', 'fig'),
        ('R4_dai21mon_toukishinseisho_machigai_tax', '登記申請書「登録免許税」欄の誤答→添削→正解の3コマ', 'tall'),
        ('R4_dai21mon_zu26_tenpu_shorui', '添付書類の図', 'fig'),
        ('R4_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R4_dai21mon_zu27_hencho_hasuu', '辺長の端数処理の図', 'fig'),
        ('R4_dai21mon_zu28_bunpitsusen_AH', '分筆線はA点からH点までの図', 'fig'),
        ('R4_dai21mon_zu29_kaku_kakanai', '地積測量図に書くもの・書かないものの図', 'fig'),
        ('R4_dai21mon_zu30_chiseki_sokuryouzu', '地積測量図（184番1・184番3・184番4）の完成見本', 'fig'),
        ('R4_dai21mon_zu31_honnin_kakunin', '本人確認情報の穴埋めの図', 'fig'),
        ('R4_dai21mon_dai5ran_kansei', '第5欄（問5）の完成形', 'wide'),
        ('R4_dai21mon_zu32_kaku_junban', '本番で解く順番の図', 'fig')]
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
nums = [int(re.search(r'_zu(\d+)_', n).group(1)) for n, _, _ in PNGS if '_zu' in n]
judge(f'解説図のPNG名の番号が記事の挿入順に1〜{len(nums)}の連番', nums == list(range(1, len(nums) + 1)))

for s_ in ['584.84㎡', '584.82㎡', '15.06㎡', '15.10㎡', '33.19', '33.41', '36.57', '（300.63, 293.12）',
           '（300.13, 293.12）', '（279.30, 293.12）', '（310.66, 292.14）', '264°24′08.42″', '338°29′30″',
           '242°53′38.42″', '212.23㎡', '357㎡', '584.8248㎡', '584.73805㎡', '7.17', 'IP ＝ 0.50']:
    check('図の数値', s_, fig, '解説図')
    check('図の数値（作図スクリプト）', s_, draw, '作図')
check('境界標（解説図プロンプト）', '境界標の記号（A・C・Jは金属標、D・E・F・G・Iはコンクリート杭）', fig, '解説図') if False else None
check('境界標', 'A・C・J＝金属標、D・E・F・G・I＝コンクリート杭', fig, '解説図')
for s_ in ['土地一部地目変更・分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｃ台206番地３　春野朝子', '金3,000円',
           '令和４年10月14日　申請　Ａ地方法務局', 'Ａ市Ｂ字八幡', '令和４年10月５日一部地目変更',
           '③184番１、184番３、184番４に分筆', '（ロ）184番３', '雑種地', '「357｜」', '（ハ）184番４', '「15｜06」',
           '「212｜23」', '「584｜75」', '184番１から分筆']:
    check('登記申請書', s_, form, '登記申請書')
for s_ in ['土地分筆登記', '土地一部地目変更・分筆登記', '令和４年10月５日一部地目変更', '「584｜82」', '「584｜75」', '雑種地', '金2,000円',
           '金3,000円', '5枚それぞれの中身', 'machigai_mokuteki', 'machigai_chiseki1', 'machigai_i_genin', 'machigai_ro', 'machigai_tax']:
    check('添削', s_, fix, '添削')
check('添削のプロンプトは縦に積む', '3コマを縦に積んだ縦長', fix, '添削')
check('添削のプロンプトは欄ごとに1枚', '藍子が間違えた欄ごとに1枚（5枚）', fix, '添削')
absent('添削のプロンプトに横並びの旧版の指示がない', '横に3コマ並べる', fix, '添削')
absent('添削のプロンプトに記号「✓」がない', '✓', fix, '添削')
absent('添削のプロンプトに「1枚で見せる」旧版の複数欄の指示がない', '土地の表示の1行目〜3行目（分筆前・（イ）・（ロ））だけ', fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')

# ---- note向けの体裁 ----
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
judge(f'画像挿入マーカー（引用形式）: {len(markers)}個（解説図32＋添削5＋完成形1＋第1欄・第2欄・第5欄3＝計41か所の想定）', len(markers) == 41)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和4年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和4年度問題21（土地）', thumb, '見出し画像')
check('添削画像の記事タイトル', title[2:], fix, '添削')
long_ = [i + 1 for i, l in enumerate(lines) if l.startswith('「') and len(l) > 260]
judge(f'セリフが260字以内 : 超えた行 {long_}', not long_)

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
n_fit = len(re.findall(r'^\s*fit\(', draw, re.M))
judge(f'作図スクリプトの表示範囲はすべて fit(..., pad_aspect=True)（{n_fit}か所）',
      n_fit > 0 and n_fit == len(re.findall(r'^\s*fit\(.*pad_aspect=True\)', draw, re.M)))
for s_ in ['拡幅前の道路の線（位置は模式）', '側溝（位置は模式）']:
    check('座標のないものは模式と書く', s_, draw, '作図')
    check('座標のないものは模式と書く', s_, fig, '解説図')

# ---- 注の番号の書き分け（問題文の注・調査図素図の注・観測値の表の注） ----
bare = [text[max(0, m.start() - 6):m.end()] for m in re.finditer(r'注[0-9]', text)
        if not re.search(r'(問題文の|調査図素図の|観測値の表の)$', text[max(0, m.start() - 8):m.start()])
        and not text[max(0, m.start() - 12):m.end()].endswith(('問題文の注1〜8、調査図素図の注1〜4、観測値の表の注1', '観測値の表の注1・2')) ]
bare = [x for x in bare if '注1〜8' not in x and '注1・2' not in x and '注1〜4' not in x]
judge(f'注の番号はすべて書き分けている（書き分けていないもの: {bare}）', not bare)
bare_fig = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)(?<!観測値の表の)注[1-8]', draw)]
judge(f'作図の説明文の注も「問題文の注N」などと書き分けている（{bare_fig}）', not bare_fig)
bare_p = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)(?<!観測値の表の)注[1-8]', fig.split('## 差し替えデータ')[-1])]
judge(f'解説図プロンプトの差し替えデータの注も書き分けている（{bare_p}）', not bare_p)
bare_f = [m.group(0) for m in re.finditer(r'(?<!問題文の)注[0-9]', form)]
judge(f'申請書のプロンプトの注も書き分けている（{bare_f}）', not bare_f)

# ---- 穴埋めの答えの語を会話で言っているか ----
for s_ in ['だから（ア）は『表題登記』', '（イ）は『隣接』です', '（ウ）は『筆界の現地における（ウ）を特定すること』だから『位置』', '「『範囲』です！」',
           'だから①②③は、日時・場所・その状況です', '「④は『申請の権限』、⑤は『登記名義人』です！」',
           '「第1欄は、I点（300.13, 293.12）、J点（279.30, 293.12）です！」']:
    check('答えの語を会話で言っている', s_)

# ====================================================================
# 2026-10-26：品質チェック（6-2・6-3）。わな→図の対応、図番なし、答案用紙の原本の寸法、キー列の再現
# ====================================================================
def prev_line(mk):
    """マーカーの直前の発言（話者の行からマーカーまで。コードや箇条書きを含む）"""
    k = lines.index(mk)
    j = k - 1
    while j >= 0 and not lines[j].startswith(('**トリ先生**', '**藍子**')):
        j -= 1
    return ' '.join(x for x in lines[j:k] if not x.startswith('> 【画像挿入】'))


def marker_of(head):
    r = [m for m in markers if m.startswith('> 【画像挿入】' + head)]
    return r[0] if len(r) == 1 else None


# (まとめの項目の語, マーカーの文言の頭, 図の直前の会話にある決め手の語)
TRAPS = [('**AB線は所有権界、筆界はE→F→G**', 'AB線とE→F→Gの比較図', '筆界の決め手にならない年度もあるのよ'),
         ('**合成図の33.19・33.41がF点とG点を測っていた**', '合成図の辺長で筆界を裏付ける図', '昔の測量は、F点とG点を測っていたんですね'),
         ('**筆界は合意では動かない**', '筆界は合意では動かないことの図', '交換の所有権の移転の登記をするしかないの'),
         ('**観測角は時計回りに足す**', 'T1からの放射でP点を求める図', '242°は南西の向き'),
         ('**J点はP点の真南**', 'J点の求め方の図', '回転も交点の公式も要らない'),
         ('**I点はP点ではない**', 'I点の求め方の図', '筆界を50cmも道路の中に'),
         ('**筆界特定の（ア）は表題登記**', '筆界特定の穴埋めの図', 'だから（ア）は『表題登記』'),
         ('**地目が変わったのは中央部分だけ**', 'どの部分の地目が変わったかの図', '地目が変わったのは、10月5日の中央部分だけよ'),
         ('**登記の目的は土地一部地目変更・分筆登記**', '登記の目的の図', '（不動産登記規則第35条第7号）'),
         ('**分筆後の地番は問題文の注7**', '分筆後の地番の図', '新しい地番が184番3からなのはそのためよ'),
         ('**雑種地の地積は1㎡未満切り捨て**', '地積の端数処理の図', '（不動産登記規則第100条）'),
         ('**精度区分は地域で決まる**', '精度区分は地域で決まることの図', '乙1を拾って、7.17㎡よ'),
         ('**地積更正は要らない**', '地積更正が要るかの判定図', '地積更正は要りません'),
         ('**分筆前の行の地積は登記記録のまま**', '分筆前の行の地積の図', '登記記録のとおりに写すだけよ'),
         ('**一部地目変更は（イ）の行に日付付き、分筆は日付なし**', '（イ）の行の原因の図', '建物の区分の登記と同じよ'),
         ('**（ロ）の行は最初から雑種地**', '（ロ）の行の地目の図', '日付も一部地目変更も書かないの'),
         ('**登録免許税は分筆後の個数**', '登録免許税の図', '一部地目変更には登録免許税はかからないわ'),
         ('**添付書類は2つだけ**', '添付書類の図', '相続証明書や代位原因証書も要らないの'),
         ('**辺長は小数第3位を四捨五入**', '辺長の端数処理の図', '19.32と書きそうになりました'),
         ('**分筆線はA点からH点まで**', '分筆線はA点からH点までの図', '境界標を設置しないと立会いで確認しているわ'),
         ('**地積測量図に書かないもの**', '地積測量図に書くもの・書かないものの図', '方位記号は答案用紙に印刷されていないから'),
         ('**本人確認情報は面識がないと第3号**', '本人確認情報の穴埋めの図', '今回は運転免許証の提示を受けているわね'),
         ]
matome = text[text.index('## 第9章'):]
trap_items = [l for l in matome.splitlines() if l.startswith('- **') and '：' in l and not re.match(r'- \*\*[1-4]番目', l)]
judge(f'まとめのワナの数 {len(trap_items)} ＝ 対応表 {len(TRAPS)}', len(trap_items) == len(TRAPS))
heads = [t[1] for t in TRAPS]
judge('対応表のマーカーの頭に重複がない', len(set(heads)) == len(heads))
for t, hd, key in TRAPS:
    check('まとめのわな', '- ' + t)
    mk = marker_of(hd)
    judge(f'ワナの図がある : {t} → {hd}', mk is not None)
    if mk:
        judge(f'図の直前の会話に決め手の語「{key}」 : {hd}', key in prev_line(mk))
pos = [markers.index(marker_of(h)) for h in heads if marker_of(h)]
judge('ワナの図が記事の挿入順（まとめの順）に並ぶ', pos == sorted(pos))
# 計算過程の図（ワナの図とは別）が、その計算の表示の後にあるか
for hd, key in [('座標法の計算過程の図', '584.8248㎡。こっちも登記記録とほとんど同じ'), ('西側の部分E・A・H・Fと△HBGの面積の図', '15.10875㎡'),
                ('（イ）184番1の面積の計算過程の図', '212.2335㎡'), ('（ロ）184番3の面積の計算過程の図', '357.44415㎡')]:
    mk = marker_of(hd)
    judge(f'計算過程の図は計算結果を言った直後 : {hd}', mk is not None and key in prev_line(mk))
# 添削画像が、対応する解説図のすぐ次にある
for fz, mh_ in [('登記の目的の図', '登記申請書「登記の目的」欄'), ('分筆前の行の地積の図', '登記申請書「土地の表示」の1行目'),
                ('（イ）の行の原因の図', '登記申請書「土地の表示」（イ）の行の原因'), ('（ロ）の行の地目の図', '登記申請書「土地の表示」（ロ）の行の地目'),
                ('登録免許税の図', '登記申請書「登録免許税」欄')]:
    i1_ = markers.index(marker_of(fz))
    judge(f'添削画像が解説図の次 : {fz}', markers[i1_ + 1].startswith('> 【画像挿入】' + mh_))

# 画像の中に図番がない（作図スクリプトのタイトルの文字列）
titled = re.findall(r"(?:new_figure|suptitle|board|calc_poly_fig)\(\s*(?:\d+(?:\.\d+)?,\s*)?'([^']*)'", draw)
judge(f'作図スクリプトのタイトル {len(titled)}個に図番がない', len(titled) >= 30 and not [x for x in titled if re.match(r'図\d', x)])
absent('作図スクリプトのタイトルに「図N　」が残っていない', "'図1", draw, '作図')
absent('解説図プロンプトに「図番のまま」の注記', '画像の中のタイトルは作成時の', fig, '解説図')
judge('作図スクリプトの管理用の番号は zu01〜zu32 の識別子だけ', '図12　本番で解く順番' not in draw)

# 電卓操作のキー列を実行して直後の「表示：」と一致するか
from keysim_note_article import simulate  # noqa: E402
sim = simulate(os.path.join(HERE, 'note_R4_dai21mon_tochi_kaiwa_kaisetsu.md'))
n_disp = len(re.findall(r'^表示：', text, re.M))
judge(f'キー列を再現した表示の数 {len(sim)}（記事の「表示：」{n_disp}個）', len(sim) == n_disp)
for n_, want, got, ok_ in sim:
    judge(f'キー列の再現 {n_}行目 : 記事「{want}」／ 再現「{got}」', ok_)

# ---- 試験の答案用紙の原本（touan_youshi/）の寸法を測り直し、作図・HTMLの値と比べる ----
import glob as _glob  # noqa: E402
TY = os.path.join(HERE, 'touan_youshi')
judge('試験の答案用紙（PDF）が touan_youshi/ にある', bool(_glob.glob(os.path.join(TY, '*.pdf'))))
import pymupdf  # noqa: E402
_doc = pymupdf.open(_glob.glob(os.path.join(TY, '*.pdf'))[0])
sheet = [''.join(pg.get_text().split()) for pg in _doc]
for s_ in ['第1欄', 'Ｉ点', 'Ｊ点', 'Ｘ座標（m）', 'Ｙ座標（m）', '第2欄', '登記の目的', '添付書類', '登録免許税',
           '令和4年10月14日申請Ａ地方法務局', '代理人（略）', '登記原因及びその日付', '③地積m', '第5欄']:
    judge(f'答案用紙1ページ目の印刷 : {s_}', s_ in sheet[0])
for s_ in ['第4欄', '地積測量図', '地番', '土地の所在', '作成者', '申請人', '（略）', '（令和4年○月○日作成）', '縮尺', '250']:
    judge(f'答案用紙2ページ目の印刷 : {s_}', s_ in sheet[1])
judge('答案用紙2ページ目の「（略）」は作成者・申請人の2か所', sheet[1].count('（略）') == 2)
judge('答案用紙に「添付情報」の欄名はない（添付書類）', '添付情報' not in sheet[0])
judge('第5欄の記号は①〜⑤', all(c in sheet[0] for c in '①②③④⑤'))
MM = 25.4 / 72


def _segs(page):
    out = []
    for dr in page.get_drawings():
        for it in dr['items']:
            if it[0] == 'l':
                out.append((it[1], it[2]))
            elif it[0] in ('re', 'qu'):
                r = it[1].rect if it[0] == 'qu' else it[1]
                P_ = pymupdf.Point
                out += [(P_(r.x0, r.y0), P_(r.x1, r.y0)), (P_(r.x1, r.y0), P_(r.x1, r.y1)),
                        (P_(r.x1, r.y1), P_(r.x0, r.y1)), (P_(r.x0, r.y1), P_(r.x0, r.y0))]
    return out


def _vl(page, xmin, xmax):
    return sorted({round(a.x * MM, 1) for a, b in _segs(page) if abs(a.x - b.x) < 0.3 and abs(a.y - b.y) * MM > 6
                   and xmin <= a.x * MM <= xmax})


def _hl(page, xmin, xmax):
    return sorted({round(a.y * MM, 1) for a, b in _segs(page) if abs(a.y - b.y) < 0.3 and abs(a.x - b.x) * MM > 10
                   and xmin <= min(a.x, b.x) * MM + 0.2 and max(a.x, b.x) * MM <= xmax + 0.2})


kh = open(os.path.join(ZU, 'R4_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
vl0 = _vl(_doc[0], 230, 404)
for c in [232.6, 242.6, 273.6, 298.6, 323.6, 340.6, 402.6]:
    judge(f'原本の罫線に x={c}mm がある（土地の表示の表）', any(abs(c - v) < 0.3 for v in vl0))
W = 402.6 - 232.6
ratios = [100 * x / W for x in (242.6 - 232.6, 273.6 - 242.6, 298.6 - 273.6, 323.6 - 298.6, 340.6 - 323.6, 402.6 - 340.6)]
html_cols = [float(x) for x in re.findall(r'<col style="width:([0-9.]+)%">', kh)]
judge(f'土地の表示の列の幅の比（原本 {[round(x, 1) for x in ratios]}）と申請書HTML {html_cols} が0.2%以内',
      len(html_cols) == 6 and all(abs(a_ - b_) < 0.2 for a_, b_ in zip(ratios, html_cols)))
hl0 = _hl(_doc[0], 232, 403)
for c in [27.2, 45.2, 53.2, 75.2, 97.2, 119.2, 141.2, 163.2]:
    judge(f'原本の罫線に y={c}mm がある（土地の表示の行。所在18・見出し8・記入行22mm）', any(abs(c - v) < 0.3 for v in hl0))
check('申請書HTML：記入行の高さは原本の22mm ＝ 137px', 'height: 137px', kh, '完成形画像')
check('申請書HTML：見出し行は8mm ＝ 50px、所在の行は18mm ＝ 112px', 'height: 112px', kh, '完成形画像')
for nm, v_ in [('登記の目的・申請人・登録免許税', 'min-height: 125px'), ('添付書類', 'min-height: 178px')]:
    check(f'完成形HTML：{nm}の枠は原本の19mm・27mmの比', v_, kh, '完成形画像')
# 第1欄・第2欄・第5欄の列の幅
for nm, want in [('R4_dai21mon_dai1ran_kansei', [33.4, 33.3, 33.3]), ('R4_dai21mon_dai2ran_kansei', [10.2, 39.8, 10.2, 39.8]),
                 ('R4_dai21mon_dai5ran_kansei', [9.7, 40.3, 9.7, 40.3])]:
    hh_ = open(os.path.join(ZU, nm + '.html'), encoding='utf-8').read()
    cw_ = [float(x) for x in re.findall(r'<col style="width:([0-9.]+)%">', hh_)]
    judge(f'{nm} の列の幅 {cw_} が原本の比 {want}', cw_ == want)
judge('原本の第1欄の縦罫線 x=116.3・170.0mm（3列等幅）', any(abs(116.3 - v) < 0.3 for v in _vl(_doc[0], 60, 225)) and any(abs(170.0 - v) < 0.3 for v in _vl(_doc[0], 60, 225)))
judge('原本の第2欄の縦罫線 x=79.1・143.1・159.6mm', all(any(abs(c - v) < 0.3 for v in _vl(_doc[0], 60, 225)) for c in (79.1, 143.1, 159.6)))
judge('原本の第5欄の縦罫線 x=249.1・317.6・334.1mm', all(any(abs(c - v) < 0.3 for v in _vl(_doc[0], 230, 404)) for c in (249.1, 317.6, 334.1)))
# 高さは min-height（固定の height を残さない）。「第○欄」の見出しを申請書・添削に入れない
import glob as _g2  # noqa: E402
for pth in sorted(_g2.glob(os.path.join(ZU, 'R4_dai21mon_toukishinseisho_*.html'))):
    hh_ = open(pth, encoding='utf-8').read()
    nm = os.path.basename(pth)
    absent(f'{nm} に style="height: が残っていない', 'style="height:', hh_, '画像HTML')
    for t_ in ['第1欄', '第2欄', '第3欄', '第4欄', '第5欄']:
        absent(f'{nm} に「{t_}」の見出しがない', t_, hh_, '画像HTML')
check('完成形の画像の地積の見出しは答案用紙どおり', '③地　　積　m²', kh, '完成形画像')
for nm in ['chiseki1', 'i_genin', 'ro', 'mokuteki', 'tax']:
    hh_ = open(os.path.join(ZU, f'R4_dai21mon_toukishinseisho_machigai_{nm}.html'), encoding='utf-8').read()
    for s_ in ['①誤答', '②添削（赤ペン）', '③正解']:
        check(f'添削HTML（{nm}）', s_, hh_, '添削画像')
    judge(f'添削HTML（{nm}）の3コマ', hh_.count('class="panel"') == 3)
    if nm in ('chiseki1', 'i_genin', 'ro'):
        check(f'添削HTML（{nm}）の列の幅', '<col style="width:5.9%"><col style="width:18.2%">', hh_, '添削画像')
check('添削HTML（登記の目的）の吹き出し', '中央部分は10月5日から月極駐車場＝雑種地。一部地目変更も一緒に申請', open(os.path.join(ZU, 'R4_dai21mon_toukishinseisho_machigai_mokuteki.html'), encoding='utf-8').read(), '添削画像')
check('添削HTML（登録免許税）の正解', '金3,000円', open(os.path.join(ZU, 'R4_dai21mon_toukishinseisho_machigai_tax.html'), encoding='utf-8').read(), '添削画像')
# 解答欄の画像の見出しは印刷どおり「第○欄」だけ
for name, t_ in [('R4_dai21mon_dai1ran_kansei', '第1欄'), ('R4_dai21mon_dai2ran_kansei', '第2欄'), ('R4_dai21mon_dai5ran_kansei', '第5欄')]:
    h_ = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    check(f'{name} の見出しは印刷どおり「{t_}」だけ', f'<div class="ranhead">{t_}</div>', h_, '解答欄の画像')
h5 = open(os.path.join(ZU, 'R4_dai21mon_dai5ran_kansei.html'), encoding='utf-8').read()
judge('第5欄の画像は⑤の行の右2セルを描かない（答案用紙どおり段になる）', h5.count('<td class="none"></td>') == 2)
for name, needles in [('R4_dai21mon_dai1ran_kansei', ['Ｉ点', 'Ｊ点', '300.13', '279.30', '293.12', 'Ｘ座標（m）']),
                      ('R4_dai21mon_dai2ran_kansei', ['表題登記', '隣接', '位置', '範囲']),
                      ('R4_dai21mon_dai5ran_kansei', ['日時', '場所', 'その状況', '申請の権限', '登記名義人', '①〜③は順不同'])]:
    h_ = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n_ in needles:
        check(f'{name}.html', n_, h_, '解答欄の画像')
for s_ in ['「Ｉ点」「300.13」「293.12」', '「Ｊ点」「279.30」「293.12」', '「ア」「表題登記」「イ」「隣接」／「ウ」「位置」「エ」「範囲」',
           '「⑤」「登記名義人」']:
    check('解答欄の画像のプロンプト', s_, form, '登記申請書')
# 第4欄の枠（原本の2ページ目）と作図スクリプトの値
vv, hh2 = _vl(_doc[1], 80, 383), _hl(_doc[1], 80.6, 382.6)
judge('原本の第4欄の枠 x 80.6〜382.6mm', any(abs(80.6 - v) < 0.3 for v in vv) and any(abs(382.6 - v) < 0.3 for v in vv))
judge('原本の第4欄の枠 y 25.8〜256.8mm', any(abs(25.8 - v) < 0.3 for v in hh2) and any(abs(256.8 - v) < 0.3 for v in hh2))
dsrc = re.sub(r'\s', '', draw)
check('作図の枠の寸法（原本の測定値）', 'ORIG_FRAME_MM=(80.6,25.8,382.6,256.8)', dsrc, '作図')
check('作図の用紙の外枠（原本の測定値）', 'ORIG_SHEET_MM=(56.3,12.2,406.9,274.8)', dsrc, '作図')
judge('地番の欄 x 240.6〜302.6mm（264.6で区切る）・土地の所在の欄 y 25.8〜35.8mm',
      all(any(abs(c - v) < 0.3 for v in vv) for c in (240.6, 264.6, 302.6, 231.6)))
judge('枠 横302mm・縦231mm（1/250で横75.5m・縦57.75m）に、T1・T2まで入れた図（東西33.16m・南北27.59m）が収まる',
      abs((382.6 - 80.6) / 4 - 75.5) < 1e-9 and 33.16 < 75.5 and 27.59 < 57.75)
check('図の説明文に答案用紙の印刷', '黒は答案用紙に印刷済みのもの（枠、欄の見出し、作成者・申請人の「（略）」、作成日の欄、縮尺 1／250）', draw, '作図')
check('作図の説明文に方位記号', '方位記号（印刷されていないので必ず描く）', draw, '作図')
for s_ in ['下の段は『作成者』と『申請人』の欄で、どちらも『（略）』と印刷済み', '縮尺の欄にも『1／250』が印刷されている',
           '方位記号は答案用紙に印刷されていないから、自分で描くのよ']:
    check('記事で答案用紙の第4欄の印刷に触れている', s_)
check('整理図は目視確認の対象', '整理図（固定配置）', draw + 'put_board', '作図') if False else None
mk_ = open(os.path.join(ZU, 'make_R4_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
for name_, src_ in [('記事', text), ('解説図', fig), ('登記申請書', form), ('添削', fix), ('見出し画像', thumb), ('作図', draw), ('画像生成', mk_)]:
    left = [w for w in ['仮のもの', '仮の形', '答案用紙そのものはリポジトリにない', '答案用紙がリポジトリにない', 'ならった仮'] if w in src_]
    judge(f'「仮」の文言が残っていない（{name_}）: {left}', not left)
check('図8の（ハ）の対角線の式', 'Conjg(H − E) × (F − A) で 15.0604㎡', fig, '解説図')
judge('（ハ）の対角線の式も15.0604', abs(abs(((H - E).conjugate() * (F - A)).imag) / 2 - 15.0604) < 1e-9)
check('図32（プロンプト）', '①問2・問5（計算なし）', fig, '解説図')
check('図30の作図範囲', 'T1・T2まで入れて縦約11cm・横約13cm', draw + fig, '作図')
for q in re.findall(r'\*\*記事の挿入位置\*\*：[^「\n]*「([^」]+)」', fig):
    check('解説図の挿入位置の引用', q, None, '記事（図の挿入位置）')

# 作図の座標法の各項の値が記事の面積と対応しているか（作図スクリプトの assert の再確認）
def _t(p, q):
    return (p * q.conjugate()).imag


judge('AB線の四角形の各項の合計の絶対値÷2 = 584.84705', abs(abs(sum(_t(x, y) for x, y in zip([A, D, C, B], [D, C, B, A]))) / 2 - 584.84705) < 1e-9)
judge('本件土地の各項の合計の絶対値÷2 = 584.8248', abs(abs(sum(_t(x, y) for x, y in zip([E, D, C, G, F], [D, C, G, F, E]))) / 2 - 584.8248) < 1e-9)
judge('（イ）の各項の合計 424.467', abs(sum(_t(x, y) for x, y in zip([C, D, I, J], [D, I, J, C])) - 424.467) < 1e-9)
judge('（ロ）の各項の合計 −714.8883', abs(sum(_t(x, y) for x, y in zip([A, I, J, G, H], [I, J, G, H, A])) + 714.8883) < 1e-9)
from zu_helpers import setup_font as _sf  # noqa: E402
_fn = _sf()
judge(f'作図のフォントが Noto Sans CJK JP（実際: {_fn}）', 'Noto' in _fn)

print('NG件数:', ng)
