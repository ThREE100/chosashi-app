"""令和3年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えは、アガルートの解答例（第1欄〜第4欄）と照合済み（ANSWER_KEY）。
実行: python3 note-articles-Kijyutsu/R3/Q21/verify_R3_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R3_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_R3_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R3_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R3_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R3_dai21mon_miidashi_gazou.md')
draw = rd(os.path.join('zu', 'draw_R3_dai21mon_kaisetsuzu.py'))
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


def num(x):
    """表示の文字列（「−446.791」など）の絶対値を数にする（記事どおりに打ち込む値）。"""
    return float(fmt_num(abs(x)).rstrip('…'))


def dist_line(p, a, b):
    return abs(((b - a).conjugate() * (p - a)).imag) / abs(b - a)


# ---- 問題文の座標（基準点成果表・測量によって得られた座標値） ----
T1, T2 = P(500.00, 500.00), P(496.77, 531.50)
B, D, E, F = P(498.29, 524.15), P(511.93, 530.00), P(504.63, 500.56), P(518.95, 505.48)
G, I, J, K = P(497.74, 526.20), P(502.14, 509.77), P(516.61, 513.65), P(499.94, 517.99)

# ---- 問1 A点（放射。観測角は時計回り＝足す） ----
check('arg(T2−T1)', to_dms(cmath.phase(T2 - T1)))
check('T1→Aの方向角', '323°34′52.66″')
judge('T1→Aの方向角 323°34′52.66″（電卓の中では −36°25′07.34″）',
      to_dms(cmath.phase(T2 - T1) + dms(227, 43, 36) - 2 * math.pi) == '−36°25′07.34″')
check('電卓の中の角', '−36°25′07.34″')
Ar = radial(T1, T2, 7.37, dms(227, 43, 36))
check('A 表示', '表示：' + disp(Ar))
A = r2(Ar)
check('A 答え', '**▶ A点（505.93, 495.62）**')
Aw = r2(T1 + cmath.rect(7.37, cmath.phase(T2 - T1) - dms(227, 43, 36)))
check('反時計回りの誤り', f'（{Aw.real:.2f}, {Aw.imag:.2f}）')
judge(f'反時計回りの誤りは道路境界の線から10m以上（{dist_line(Aw, I, B):.2f}）', dist_line(Aw, I, B) > 10)
judge(f'反時計回りの誤りはT1の約5m南（{T1.real - Aw.real:.2f}）', 4.5 < T1.real - Aw.real < 5.5)
judge(f'A点は直線IBから0.002m以内（{dist_line(A, I, B):.4f}）', dist_line(A, I, B) < 0.002)

# ---- 問1 C点（隅切り） ----
check('GB 表示', '表示：' + fmt_num(abs(B - G)))
Cr = G + (D - G) / abs(D - G) * abs(B - G)
check('C 表示', '表示：' + disp(Cr))
C = r2(Cr)
check('C 答え', '**▶ C点（499.79, 526.75）**')
check('BCの検算', f'{fmt_num(abs(C - B))}で、四捨五入すると3.00')
Cw = r2(G + (D - G) / abs(D - G) * 3.00)
check('隅切長3.00で進めた誤りのBC', f'Bとの間は{abs(Cw - B):.2f}になって')

# ---- 問1 H点（直線ABと直線FEの延長の交点） ----
n1 = (A - F).conjugate() * (B - A)
n2 = (E - F).conjugate() * (B - A)
check('H 1つ目の表示', '表示：' + disp(n1))
check('H 2つ目の表示', '表示：' + disp(n2))
check('H の比の式', f'H ＝ F ＋ (E − F) × {fmt_num(abs(n1.imag))} ÷ {fmt_num(abs(n2.imag))}')
judge('比は1を少し超える（FからEを通り越す）', 1 < n1.imag / n2.imag < 1.01)
Hr = F + (E - F) * num(n1.imag) / num(n2.imag)
check('H 表示', '表示：' + disp(Hr))
H = r2(Hr)
check('H 答え', '**▶ H点（504.61, 500.55）**')
check('FH 表示', '表示：' + fmt_num(abs(H - F)))
check('FE 表示', '表示：' + fmt_num(abs(E - F)))
judge('FH 15.16 は10番2の地積測量図と一致、FE 15.14 は不一致',
      f'{abs(H - F):.2f}' == '15.16' and f'{abs(E - F):.2f}' == '15.14')
hH = (A - F).conjugate() * (H - F)
check('高さの途中の表示', '表示：' + disp(hH))
check('高さ（H）の表示', '表示：' + fmt_num(num(hH.imag) / abs(A - F)))
hE = (A - F).conjugate() * (E - F)
check('E点のiの係数', f'iの係数が{fmt_num(abs(hE.imag))}')
check('高さ（E）', f'高さは{fmt_num(num(hE.imag) / abs(A - F))}')
judge('高さ H 4.73・E 4.72', f'{dist_line(H, A, F):.2f}' == '4.73' and f'{dist_line(E, A, F):.2f}' == '4.72')
check('AF', f'AFは計算すると{abs(F - A):.2f}')
H1516 = F + 15.16 * (E - F) / abs(E - F)
check('15.16進めた点', f'（{fmt_num(H1516.real)}, {fmt_num(H1516.imag)}）')
judge('15.16進めた点も丸めるとH', r2(H1516) == H)
check('EとHの差', f'わずか{abs(E - H):.2f}m')

# ---- 問1 L点（Kを通るIJの平行線と直線FDの交点） ----
m1 = (K - F).conjugate() * (J - I)
m2 = (D - F).conjugate() * (J - I)
check('L 1つ目の表示', '表示：' + disp(m1))
check('L 2つ目の表示', '表示：' + disp(m2))
check('L の比の式', f'L ＝ F ＋ (D − F) × {fmt_num(abs(m1.imag))} ÷ {fmt_num(abs(m2.imag))}')
Lr = F + (D - F) * num(m1.imag) / num(m2.imag)
check('L 表示', '表示：' + disp(Lr))
L = r2(Lr)
check('L 答え', '**▶ L点（514.27, 521.83）**')
Lw = r2(J + (K - I))
check('平行四辺形の誤り', f'（{Lw.real:.2f}, {Lw.imag:.2f}）')
judge(f'誤りのLは直線FDから0.15m（{dist_line(Lw, F, D):.4f}）、北側',
      f'{dist_line(Lw, F, D):.2f}' == '0.15'
      and Lw.real > F.real + (D.real - F.real) * (Lw.imag - F.imag) / (D.imag - F.imag))
check('誤りは北側', '0.15mも北、隣の10番4の側')
check('IJとKL', f'IJは{abs(J - I):.2f}、KLは{abs(L - K):.2f}')
check('誤りのKL', f'KLも{abs(Lw - K):.2f}になって')

# ---- 問2 ----
for s in ['- **ア**：登記所', '- **イ**：位置', '- **ウ**：形状', '- **エ**：地番', '- **オ**：閉鎖', '- **カ**：永久']:
    check('問2', s)

# ---- 問3 地積と公差 ----
HEI, OTSU, KOU, ZEN = [H, I, J, F], [I, K, L, J], [B, C, D, L, K], [H, B, C, D, F]
for nm, pts in [('丙区画', HEI), ('乙区画', OTSU), ('甲区画', KOU)]:
    s = double_area_sum(pts)
    sign = '＋' if s.imag > 0 else '−'
    check(f'{nm} 表示', f'表示：（実部）{sign} {fmt_num(abs(s.imag))}i')
    check(f'{nm} 面積', f'{fmt_num(abs(s.imag))} ÷ 2 ＝ {area(pts):.4f}㎡')
    check(f'{nm} 地積', f'{chiseki(area(pts)):.2f}㎡')
tot = sum(chiseki(area(p)) for p in (HEI, OTSU, KOU))
check('合計', f'135.84 ＋ 126.84 ＋ 123.21 ＝ {tot:.2f}㎡')
check('差', f'386.30 − 385.89 ＝ {386.30 - tot:.2f}㎡')
check('全体', f'{area(ZEN):.4f}㎡')
judge('差0.41 ≦ 甲2の公差1.85（問題文の表）', 386.30 - tot < 1.85)
check('甲2の公差', '表の甲2は1.85㎡')

# ---- 問3 申請書 ----
for s in ['- **登記の目的**：土地分筆登記', '- **添付書類**：地積測量図　相続証明書　代位原因証書　代理権限証書',
          '- **登録免許税**：金3,000円', '- **所在**：K市D町二丁目',
          '- **1行目**：（被相続人　山田太郎）',
          '- **被代位者**：相続人　M市D町五丁目2番2号　山田一郎、S市D町一丁目3番5号　山田三郎',
          '- **申請人兼代位者**：K市D町二丁目10番1号　山田二郎',
          '- **代位原因**：令和3年8月1日遺産分割の所有権移転登記請求権',
          '①10番1、②宅地、③386.30（登記記録の地積）',
          '①（イ）、③126.84、登記原因「③10番1、10番8、10番9に分筆」',
          '①（ロ）10番8、②宅地、③123.21、登記原因「10番1から分筆」',
          '①（ハ）10番9、②宅地、③135.84、登記原因「10番1から分筆」']:
    check('問3', s)
check('誤答（二郎だけ）', '申請人は『K市D町二丁目10番1号　山田二郎』')
check('誤答（登録免許税）', '2,000円……')
check('誤答（登記原因）', '『③10番8、10番9を分筆』')

# ---- 問4 地積測量図 ----
SIDES = {'HI': (H, I), 'IK': (I, K), 'KB': (K, B), 'BC': (B, C), 'CD': (C, D), 'DL': (D, L), 'LJ': (L, J),
         'JF': (J, F), 'FH': (F, H)}
for n, (p, q) in SIDES.items():
    check(f'辺長{n}', f'- **{n}**：{round(abs(p - q) + 1e-9, 2):.2f}')
    check(f'図の辺長{n}', f'{n} {round(abs(p - q) + 1e-9, 2):.2f}', fig, '解説図')
check('分筆線IJ', f'- **IJ（分筆線）**：{abs(J - I):.2f}')
check('分筆線KL', f'- **KL（分筆線）**：{abs(L - K):.2f}')
check('四捨五入の境目', f'DLとJFは計算すると{fmt_num(abs(D - L))}'.replace('…', '……'))
judge('DL・JFは8.4984…', fmt_num(abs(D - L)) == fmt_num(abs(J - F)) == '8.4984…')
check('地番欄', '地番は分筆後の3筆で『10番1、10番8、10番9』')

# ---- アガルートの解答例（第1欄〜第4欄）との照合 ----
ANSWER_KEY = {
    '第1欄 A点': ((A.real, A.imag), (505.93, 495.62)), '第1欄 C点': ((C.real, C.imag), (499.79, 526.75)),
    '第1欄 H点': ((H.real, H.imag), (504.61, 500.55)), '第1欄 L点': ((L.real, L.imag), (514.27, 521.83)),
    '(イ)10番1': (chiseki(area(OTSU)), 126.84), '(ロ)10番8': (chiseki(area(KOU)), 123.21),
    '(ハ)10番9': (chiseki(area(HEI)), 135.84),
}
for k, (got, want) in ANSWER_KEY.items():
    judge(f'解答例と一致 {k}: {got}', got == want if not isinstance(got, tuple)
          else all(abs(g - w) < 1e-9 for g, w in zip(got, want)))
AGAROOT_SIDES = {'HI': '9.55', 'IK': '8.51', 'KB': '6.38', 'BC': '3.00', 'CD': '12.57', 'DL': '8.50',
                 'LJ': '8.51', 'JF': '8.50', 'FH': '15.16'}
for n, v in AGAROOT_SIDES.items():
    judge(f'解答例の地積測量図の辺長 {n} {v}', f'{round(abs(SIDES[n][0] - SIDES[n][1]) + 1e-9, 2):.2f}' == v)
judge('解答例の分筆線 IJ 14.98・KL 14.84', f'{abs(J - I):.2f}' == '14.98' and f'{abs(L - K):.2f}' == '14.84')

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（12枚）', n_fig == 12)
pngs = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
for i in range(1, 13):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R3_dai21mon_zu{i:02d}_') for f in pngs))
for s in ['（505.93, 495.62）', '(499.79, 526.75)', '(504.61, 500.55)', '(514.27, 521.83)', '(495.08, 494.51)',
          '(500.64, 526.98)', '(514.41, 521.87)', '135.8455', '126.8422', '123.2128', '385.8952', '446.791 ÷ 446.1384',
          '254.7785 ÷ 382.042', '差 0.41㎡ ≦ 公差 1.85㎡', 'FH ＝ 15.16', '高さ 4.73', 'FE ＝ 15.14　高さ 4.72']:
    check('解説図プロンプトの数値', s.replace('（505.93, 495.62）', '(505.93, 495.62)'), fig, '解説図')
for s in ['P(505.93, 495.62)', 'P(499.79, 526.75)', 'P(504.61, 500.55)', 'P(514.27, 521.83)', '135.8455, 135.84',
          '126.8422, 126.84', '123.2128, 123.21', "'IJ': (I, J, '14.98')", "'KL': (K, L, '14.84')"]:
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['土地分筆登記', '地積測量図　相続証明書', '代位原因証書　代理権限証書', '金3,000円',
          '（被相続人　山田太郎）', 'Ｍ市Ｄ町五丁目２番２号　山田一郎', 'Ｓ市Ｄ町一丁目３番５号　山田三郎',
          'Ｋ市Ｄ町二丁目10番１号　山田二郎', '代位原因　令和３年８月１日遺産分割の所有権移転登記請求権',
          '令和３年10月17日　申請　Ａ地方法務局', 'Ｋ市Ｄ町二丁目', '「386｜30」', '「126｜84」', '「123｜21」', '「135｜84」',
          '③10番１、10番８、10番９に分筆', '（ロ）10番８', '（ハ）10番９', '10番１から分筆']:
    check('登記申請書', s, form, '登記申請書')
judge('登記申請書の項目の順序（登録免許税が申請人の枠より前）',
      form.index('**④ 登録免許税**') < form.index('**⑤ 申請人の枠') < form.index('**⑦ 申請の日付と提出先'))
for s in ['地積測量図　相続証明書　代理権限証書', '相続人　Ｋ市Ｄ町二丁目10番１号　山田二郎', '代位原因証書',
          'Ｍ市Ｄ町五丁目２番２号　山田一郎', 'Ｓ市Ｄ町一丁目３番５号　山田三郎', '申請人兼代位者',
          '代位原因　令和３年８月１日遺産分割の所有権移転登記請求権', '金3,000円']:
    check('添削', s, fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいを', 'くいが', 'せんじょ', '予備校', 'アガルートの解説']:
    absent('誤記・混入・専門用語のひらがな書き・解答例の流用', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', '隅切剪除長')
check('問題文どおり', 'ブロック塀')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図12＋添削1＋完成形1＋第1欄・第2欄2＝計16か所の想定）', n_marker == 16)
spk = [(i, l.strip()) for i, l in enumerate(lines) if l.rstrip() in ('**トリ先生**', '**藍子**')]
same = [i1 + 1 for (i1, n1), (i2, n2) in zip(spk, spk[1:]) if n1 == n2 and not any(x.strip() for x in lines[i1 + 2:i2])]
judge(f'同じ話者のセリフが間に何も挟まずに続いていない: {same}', not same)
# 画像挿入マーカーをはさんで同じ話者が続くのも1つの連続とみなす。複数段落のセリフも1つとして読む（2026-10-02追加）
same_m = []
for (i1, n1), (i2, n2) in zip(spk, spk[1:]):
    j = i1 + 1
    while j < len(lines) and not lines[j].rstrip().endswith('」'):
        j += 1
    rest = [x for x in lines[j + 1:i2] if x.strip()]
    if n1 == n2 and (not rest or all(x.startswith('> 【画像挿入】') for x in rest)):
        same_m.append(i2 + 1)
judge(f'同じ話者のセリフが続いていない（画像挿入マーカーだけをはさむものも）: {same_m}', not same_m)
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和3年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和3年度問題21（土地）', thumb, '見出し画像')
absent('見出し画像に別年度の文言', '令和7', thumb, '見出し画像')

# ---- 変数の割り当て（第1章の箇条書き）と電卓操作で使う変数 ----
used = set(re.findall(r'\[ALPHA\] \[([A-FXY])\]', text)) | set(re.findall(r'\[STO\] \[([A-FXY])\]', text))
judge(f'電卓操作で使う変数 {sorted(used)} は、第1章の割り当て表にすべてある',
      all(f'- **{v}**：' in text for v in used))

# ---- 注の書き分け（問題文の注・調査図素図の注・観測値の注） ----
for s_ in ['問題文の注3', '問題文の注4', '問題文の注5', '問題文の注6', '調査図素図の注3', '調査図素図の注2',
           '〔測量によって得られた観測値〕の表の下の注1']:
    check('注の出どころを書き分け', s_)
for bad in ['（注5）', '（注6）', 'は注4で', 'は注3で']:
    absent('出どころのない注の番号', bad)
    absent('出どころのない注の番号', bad, fig, '解説図')
check('相続を証する情報の時系列', 'まだ太郎さんの名義のまま')
check('解く順番（時間配分）', '- **5番目**：L点 → 3区画の面積 → 公差の判定 → 申請書の地積の欄')
check('作図の範囲', '約126mm×約89mm')

# ---- 登記申請書の完成形・添削画像（zu/ の PNG と HTML） ----
import struct


def png_size(path):
    with open(path, 'rb') as f:
        head = f.read(24)
    return struct.unpack('>II', head[16:24])


ZU = os.path.join(HERE, 'zu')
for name in ['R3_dai21mon_toukishinseisho_kansei', 'R3_dai21mon_toukishinseisho_machigai']:
    pp, hp = os.path.join(ZU, name + '.png'), os.path.join(ZU, name + '.html')
    judge(f'{name}.png と .html がある', os.path.exists(pp) and os.path.exists(hp))
    if os.path.exists(pp):
        w, h = png_size(pp)
        judge(f'{name}.png は縦長で横1200px（{w}×{h}）', w == 1200 and h > w)
html_k = open(os.path.join(ZU, 'R3_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
for s_ in ['土地分筆登記', '地積測量図　相続証明書', '代位原因証書　代理権限証書', '金3,000円', '（被相続人　山田太郎）',
           'Ｍ市Ｄ町五丁目２番２号　山田一郎', 'Ｓ市Ｄ町一丁目３番５号　山田三郎', 'Ｋ市Ｄ町二丁目10番１号　山田二郎',
           '代位原因　令和３年８月１日遺産分割の所有権移転登記請求権', '令和３年10月17日　申請　Ａ地方法務局', 'Ｋ市Ｄ町二丁目',
           '>386<', '>30<', '>126<', '>84<', '>123<', '>21<', '>135<', '③10番１、10番８、10番９に分筆', '（ロ）10番８',
           '（ハ）10番９', '10番１から分筆', '申請人兼代位者', '被代位者']:
    check('完成形のHTML', s_, html_k, '完成形HTML')
    check('完成形プロンプトと同じ文言', s_.strip('><'), form, '登記申請書')
judge('完成形HTMLの順序（登録免許税 → 申請人の枠 → 代理人 → 申請の日付 → 土地の表示）',
      html_k.index('金3,000円') < html_k.index('（被相続人') < html_k.index('（略）') < html_k.index('令和３年10月17日')
      < html_k.index('所　在'))
html_m = open(os.path.join(ZU, 'R3_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s_ in ['①誤答', '②添削', '③正解', '地積測量図　相続証明書　代理権限証書', '代位原因証書', '申請人兼代位者',
           '二郎1人なら一郎・三郎の分は代位']:
    check('添削のHTML', s_, html_m, '添削HTML')
judge('添削のHTMLは①②③の順に縦に積む', html_m.index('①誤答') < html_m.index('②添削') < html_m.index('③正解'))
check('添削プロンプトは縦に積む', '3コマを縦に積む', fix, '添削')
absent('添削プロンプトに横並びの旧版の文言', '横に3コマ並べる', fix, '添削')


# ---- 2026-10-02 追加：穴埋めの答えの語を会話で言っているか ----
for s_ in ['（ア）は、地図に準ずる図面を備え付ける場所なので『登記所』', '「（イ）位置、（ウ）形状、（エ）地番ですね。順不同です」',
           '新しい地図を備え付けたら、従前の地図に準ずる図面は『閉鎖』されます', '「（カ）は永久です！」',
           '「第1欄は、A点（505.93, 495.62）、C点（499.79, 526.75）、H点（504.61, 500.55）、L点（514.27, 521.83）です！」']:
    check('答えの語を会話で言っている', s_)
# ---- 2026-10-02 追加：今の法令の注（法定相続情報番号） ----
NOTE_ = ('※相続証明書は、今は法定相続情報一覧図の写しか法定相続情報番号の提供で代えることもできる（不動産登記規則第37条の3第1項）。'
         '出題当時は法定相続情報番号の制度がなかった')
check('法定相続情報番号の注（記事）', '（相続証明書は、今は法定相続情報一覧図の写しか法定相続情報番号の提供で代えることもできる。不動産登記規則第37条の3第1項。出題当時は法定相続情報番号の制度がなかった）')
check('法定相続情報番号の注（完成形の画像）', NOTE_, html_k, '完成形HTML')
check('法定相続情報番号の注（プロンプト）', NOTE_, form, '登記申請書')
# ---- 2026-10-02 追加：記事に足した観点（注の仕分けと作図の範囲）の図 ----
for s_ in ['問題文の注のうち、注1から注4と注7は毎年ほとんど同じ注', '問題文の注5と、基準点は位置と点名だけでいいとした問題文の注6']:
    check('注の仕分け', s_)
check('図10（作図）', "'図10　問4　問題文の注の仕分けと地積測量図の作図の範囲'", draw, '作図')
check('図10（プロンプト）', '約32m　→　1/250〈1m ＝ 4mm〉で約126mm', fig, '解説図')
_pts = [P(500.00, 500.00), P(496.77, 531.50), B, C, D, F, H, I, J, K, L]
judge('作図の範囲 東西約32m・南北約22m（1/250で約126mm×約89mm）',
      round((max(p.imag for p in _pts) - min(p.imag for p in _pts)) * 4) == 126
      and round((max(p.real for p in _pts) - min(p.real for p in _pts)) * 4) == 89)
for q in re.findall(r'\*\*記事の挿入位置\*\*：[^「\n]*「([^」]+)」', fig):
    check('解説図の挿入位置の引用', q, None, '記事（図の挿入位置）')

# ---- 2026-10-02 追加：記事の画像挿入マーカーと zu/ のPNGが記事の順に対応しているか ----
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R3_dai21mon_zu01_zentaizu', '北を上にして座標どおりに描き直した全体図', 'fig'),
        ('R3_dai21mon_zu02_A_housha', 'T1からの放射でA点を求める図', 'fig'),
        ('R3_dai21mon_zu03_C_sumikiri', '隅切りでC点を求める図', 'fig'),
        ('R3_dai21mon_zu04_H_kousa', 'H点の求め方の図', 'fig'),
        ('R3_dai21mon_zu05_L_heikousen', 'L点の求め方の図', 'fig'),
        ('R3_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R3_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R3_dai21mon_zu06_chizu_junzuru', '地図と地図に準ずる図面の比較図', 'fig'),
        ('R3_dai21mon_zu07_kousa', '公差の判定図', 'fig'),
        ('R3_dai21mon_zu08_dai_kankei', '申請人の関係図', 'fig'),
        ('R3_dai21mon_toukishinseisho_machigai', '誤答→添削→正解の3コマ', 'tall'),
        ('R3_dai21mon_zu09_bunpitsu_chiban', '分筆後の区画と地番の図', 'fig'),
        ('R3_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R3_dai21mon_zu10_chuu_shiwake', '問題文の注の仕分けと作図の範囲の図', 'fig'),
        ('R3_dai21mon_zu11_chiseki_sokuryouzu', '地積測量図（10番1・10番8・10番9）の完成見本', 'fig'),
        ('R3_dai21mon_zu12_kaku_junban', '本番の解く順番の図', 'fig')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
for (name, key, kind), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = png_size(path)
        ok = (w == 1200 and h > w) if kind == 'tall' else (w == 1200 and h < w) if kind == 'wide' else w >= 1200
    judge(f'PNG（マーカー順・大きさ） : {name}', ok)
    src = fig if '_zu' in name else (fix if 'machigai' in name else form)
    judge(f'プロンプトにファイル名 : zu/{name}.png', f'zu/{name}.png' in src)
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない : {extra}', not extra)
for name, needles in [('R3_dai21mon_dai1ran_kansei', ['第1欄', 'Ａ点', 'Ｃ点', 'Ｈ点', 'Ｌ点', '505.93', '495.62', '499.79', '526.75',
                                                     '504.61', '500.55', '514.27', '521.83']),
                      ('R3_dai21mon_dai2ran_kansei', ['第2欄', '登記所', '位置', '形状', '地番', '閉鎖', '永久', 'イ〜エは順不同'])]:
    h_ = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n_ in needles:
        check(f'{name}.html', n_, h_, '解答欄の画像')
for s_ in ['「Ａ点」「505.93」「495.62」', '「Ｌ点」「514.27」「521.83」', '「ア」「登記所」「イ」「位置」／「ウ」「形状」「エ」「地番」／「オ」「閉鎖」「カ」「永久」',
           '試験の答案用紙（`touan_youshi/R3_dai21mon_touan_youshi.pdf` の1ページ目の左の列）で確かめた']:
    check('解答欄の画像のプロンプト', s_, form, '登記申請書')

# ---- 2026-10-02 追加：試験の答案用紙（実物、touan_youshi/）の欄の形との照合 ----
TOUAN = os.path.join(HERE, 'touan_youshi', 'R3_dai21mon_touan_youshi.pdf')
judge('試験の答案用紙のPDFがある', os.path.exists(TOUAN))
try:
    import pymupdf
    _d = pymupdf.open(TOUAN)
    tp1, tp2 = _d[0].get_text(), _d[1].get_text()
except Exception as e:  # pymupdf がない環境では印刷文字の照合を飛ばす
    print('（pymupdf で答案用紙を読めないため、印刷文字の照合を省略）', e)
    tp1 = tp2 = None
if tp1 is not None:
    flat1, flat2 = tp1.replace('\n', ''), tp2.replace('\n', '')
    for s_ in ['第1 欄', 'Ｘ座標（m）', 'Ｙ座標（m）', 'Ａ点', 'Ｃ点', 'Ｈ点', 'Ｌ点', '第2 欄', 'ア', 'イ', 'ウ', 'エ', 'オ', 'カ',
               '第3 欄', '登　記　申　請　書', '登記の目的', '添付書類', '登録免許税', '（略）',
               '令和3 年10 月17 日　申請　Ａ地方法務局', '所　在', '①地　　番', '②地　　目', '登記原因及びその日付']:
        judge(f'答案用紙1ページ目の印刷 : {s_}', s_ in tp1 or s_ in flat1)
    judge('答案用紙1ページ目に「添付情報」の欄はない（欄の名前は「添付書類」）', '添付情報' not in tp1)
    judge('答案用紙1ページ目の第1欄は4点（Ａ→Ｃ→Ｈ→Ｌの順）',
          tp1.index('Ａ点') < tp1.index('Ｃ点') < tp1.index('Ｈ点') < tp1.index('Ｌ点'))
    judge('答案用紙1ページ目の左の列の順（登記の目的 → 添付書類 → 登録免許税）',
          tp1.index('登記の目的') < tp1.index('添付書類') < tp1.index('登録免許税'))
    for s_ in ['第4 欄', '地　　　番', '地　積　測　量　図', '土地の所在', '作 成 者', '（令和3 年○月○日作成）', '申 請 人', '縮尺', '250']:
        judge(f'答案用紙2ページ目（第4欄）の印刷 : {s_}', s_ in tp2)
    judge('答案用紙2ページ目の「（略）」は作成者と申請人の2か所', tp2.count('（略）') == 2)
    judge('答案用紙2ページ目に方位記号の文字（N・北）の印刷はない', not re.search(r'(^|\n)(N|Ｎ|北)(\n|$)', tp2))
# 画像・プロンプト・記事を答案用紙の形にそろえたこと
for s_ in ['>第3欄<', '>登記申請書<', '>登記の目的<', '>添　付　書　類<', '>登録免許税<', '>代　　理　　人<', '>（略）<']:
    check('完成形HTMLの印刷文字（答案用紙どおり）', s_, html_k, '完成形HTML')
absent('完成形HTMLに「添付情報」の欄', '添付情報', html_k, '完成形HTML')
judge('完成形HTMLの順序（第3欄 → 登記の目的 → 添付書類 → 登録免許税）',
      html_k.index('第3欄') < html_k.index('登記の目的') < html_k.index('添　付　書　類') < html_k.index('登録免許税'))
h1_ = open(os.path.join(ZU, 'R3_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
h2_ = open(os.path.join(ZU, 'R3_dai21mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['<div class="rt">第1欄</div>', 'Ｘ座標（m）', 'Ｙ座標（m）', 'diag']:
    check('第1欄の画像の形（答案用紙どおり）', s_, h1_, '解答欄の画像')
judge('第1欄の画像の行の順（Ａ→Ｃ→Ｈ→Ｌ）', h1_.index('Ａ点') < h1_.index('Ｃ点') < h1_.index('Ｈ点') < h1_.index('Ｌ点'))
check('第2欄の画像の形（答案用紙どおり）', '<div class="rt">第2欄</div>', h2_, '解答欄の画像')
judge('第2欄の画像は「ア｜イ」「ウ｜エ」「オ｜カ」の3行', h2_.count('<tr>') == 3 and
      h2_.index('>ア<') < h2_.index('>イ<') < h2_.index('>ウ<') < h2_.index('>エ<') < h2_.index('>オ<') < h2_.index('>カ<'))
check('図11の説明文（第4欄の印刷）', '作成者・申請人は「（略）」、縮尺1/250は印刷済み。方位記号は自分で描く（印刷なし）。', draw, '作図')
check('図11の説明文（第4欄の印刷）', '作成者・申請人は「（略）」、縮尺1/250は印刷済み。方位記号は自分で描く（印刷なし）。', fig, '解説図')
check('図10の枠の大きさ', '答案用紙の第4欄の枠（横約30cm・縦約23cm）に収まるので', draw, '作図')
check('記事の第4欄の印刷', "『作成者』と『申請人』は『（略）』、縮尺の1/250も印刷済みよ。方位記号は印刷されていないから、自分で描くの")
check('記事の第4欄の枠の大きさ', '第4欄の枠は横約30cm・縦約23cmあるから、余裕で収まるわ')
mk_ = open(os.path.join(ZU, 'make_R3_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
for nm_, src_ in [('記事', text), ('解説図プロンプト', fig), ('申請書プロンプト', form), ('添削プロンプト', fix), ('見出し画像プロンプト', thumb),
                  ('作図スクリプト', draw), ('申請書の生成スクリプト', mk_)]:
    for w_ in ['仮のもの', '仮の形', 'リポジトリにない', '確かめたら直す']:
        judge(f'{nm_}に「{w_}」が残っていない', w_ not in src_)
bare_p = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)(?<!注1〜)注[0-9]', fig.split('## 差し替えデータ')[-1])]
judge(f'解説図プロンプトの差し替えデータの注も書き分けている（{bare_p}）', not bare_p)
bare_f = [m.group(0) for m in re.finditer(r'(?<!問題文の)注[0-9]', form)]
judge(f'申請書のプロンプトの注も書き分けている（{bare_f}）', not bare_f)

print('NG件数:', ng)
