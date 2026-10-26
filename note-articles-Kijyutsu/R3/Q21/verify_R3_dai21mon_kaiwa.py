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
          '「金3,000円ですね。所在は『K市D町二丁目』。次は土地の表示です。','分筆後は10番1・10番8・10番9',
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
judge(f'解説図プロンプトの図の数 {n_fig}枚（26枚）', n_fig == 26)
pngs = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
for i in range(1, 27):
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
          '令和３年８月１日遺産分割の所有権移転登記請求権', '金3,000円']:
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
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図26＋添削4＋完成形1＋第1欄・第2欄2＝計33か所の想定）', n_marker == 33)
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
for name in ['R3_dai21mon_toukishinseisho_kansei', 'R3_dai21mon_toukishinseisho_machigai_shinseinin',
             'R3_dai21mon_toukishinseisho_machigai_tenpu', 'R3_dai21mon_toukishinseisho_machigai_menkyozei',
             'R3_dai21mon_toukishinseisho_machigai_genin']:
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
MG = {n: open(os.path.join(ZU, f'R3_dai21mon_toukishinseisho_machigai_{n}.html'), encoding='utf-8').read()
      for n in ['shinseinin', 'tenpu', 'menkyozei', 'genin']}
for n_, needles in [('shinseinin', ['申請人兼代位者', '二郎1人なら一郎・三郎の分は代位', '被代位者']),
                    ('tenpu', ['地積測量図　相続証明書<br>代理権限証書', '代位原因証書', '遺産分割協議書']),
                    ('menkyozei', ['金2,000円', '金3,000円', '3個 × 1,000円']),
                    ('genin', ['③10番８、10番９を分筆', '③10番１、10番８、10番９に分筆', '自分の10番1も入れる'])]:
    for s_ in ['①誤答', '②添削', '③正解'] + needles:
        check(f'添削のHTML（{n_}）', s_, MG[n_], '添削HTML')
    judge(f'添削のHTML（{n_}）は①②③の順に縦に積む', MG[n_].index('①誤答') < MG[n_].index('②添削') < MG[n_].index('③正解'))
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
check('図24（作図）', "'問4　今年だけの注（問題文の注5・問題文の注6）と、T1・T2まで入れた作図の範囲'", draw, '作図')
check('図24（プロンプト）', '約22m→約89mm', fig, '解説図')
_pts = [P(500.00, 500.00), P(496.77, 531.50), B, C, D, F, H, I, J, K, L]
judge('作図の範囲 東西約32m・南北約22m（1/250で約126mm×約89mm）',
      round((max(p.imag for p in _pts) - min(p.imag for p in _pts)) * 4) == 126
      and round((max(p.real for p in _pts) - min(p.real for p in _pts)) * 4) == 89)
for q in re.findall(r'\*\*記事の挿入位置\*\*：[^「\n]*「([^」]+)」', fig):
    check('解説図の挿入位置の引用', q, None, '記事（図の挿入位置）')

# ---- 2026-10-02 追加：記事の画像挿入マーカーと zu/ のPNGが記事の順に対応しているか ----
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R3_dai21mon_zu01_jikeiretsu_zentai', '全体の時系列の図', 'fig'),
        ('R3_dai21mon_zu02_zentaizu', '北を上にして座標どおりに描き直した全体図', 'fig'),
        ('R3_dai21mon_zu03_chuu_shiwake', '注の仕分けの表', 'fig'),
        ('R3_dai21mon_zu04_A_housha', 'T1からの放射でA点を求める図', 'fig'),
        ('R3_dai21mon_zu05_C_sumikiri', '隅切りでC点を求める図', 'fig'),
        ('R3_dai21mon_zu06_H_hantei', 'H点が筆界点と判断される流れの図', 'fig'),
        ('R3_dai21mon_zu07_H_hi', 'H点の交点の比の図', 'fig'),
        ('R3_dai21mon_zu08_H_kousa', 'H点の求め方の図', 'fig'),
        ('R3_dai21mon_zu09_L_hi', 'L点の交点の比の図', 'fig'),
        ('R3_dai21mon_zu10_L_heikousen', 'L点の求め方の図', 'fig'),
        ('R3_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R3_dai21mon_zu11_chizu_kukaku', '地図と地図に準ずる図面の比較図', 'fig'),
        ('R3_dai21mon_zu12_chizu_eikyuu', '閉鎖と保存期間の図', 'fig'),
        ('R3_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R3_dai21mon_zu13_menseki_hei', '丙区画の面積の計算の図', 'fig'),
        ('R3_dai21mon_zu14_menseki_otsu', '乙区画の面積の計算の図', 'fig'),
        ('R3_dai21mon_zu15_menseki_kou', '甲区画の面積の計算の図', 'fig'),
        ('R3_dai21mon_zu16_seido_kubun', '精度区分の図', 'fig'),
        ('R3_dai21mon_zu17_kousa', '公差の判定図', 'fig'),
        ('R3_dai21mon_zu18_dai_kankei', '申請人の関係図', 'fig'),
        ('R3_dai21mon_zu19_sozoku_hantei', '相続を証する情報が要るかの判定の図', 'fig'),
        ('R3_dai21mon_toukishinseisho_machigai_shinseinin', '登記申請書「申請人」欄の誤答→添削→正解', 'tall'),
        ('R3_dai21mon_toukishinseisho_machigai_tenpu', '登記申請書「添付書類」欄の誤答→添削→正解', 'tall'),
        ('R3_dai21mon_toukishinseisho_machigai_menkyozei', '登記申請書「登録免許税」欄の誤答→添削→正解', 'tall'),
        ('R3_dai21mon_zu20_bunpitsu_chiban', '分筆後の区画と地番の図', 'fig'),
        ('R3_dai21mon_zu21_chiseki_zenmae', '分筆前の行の地積の図', 'fig'),
        ('R3_dai21mon_toukishinseisho_machigai_genin', '登記申請書「土地の表示」欄（登記原因）の誤答→添削→正解', 'tall'),
        ('R3_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R3_dai21mon_zu22_hencho', '辺長11本の計算の図', 'fig'),
        ('R3_dai21mon_zu23_kaku_kakanai', '地積測量図に書くもの・書かないもの・描かない点の図', 'fig'),
        ('R3_dai21mon_zu24_sakuzu_hanni', '今年だけの注と作図の範囲の図', 'fig'),
        ('R3_dai21mon_zu25_chiseki_sokuryouzu', '地積測量図（10番1・10番8・10番9）の完成見本', 'fig'),
        ('R3_dai21mon_zu26_kaku_junban', '本番の解く順番の図', 'fig')]
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
absent('完成形HTMLに「第3欄」の見出しがない', '第3欄', html_k, '完成形HTML')
for s_ in ['>登記申請書<', '>登記の目的<', '>添　付　書　類<', '>登録免許税<', '>代　　理　　人<', '>（略）<']:
    check('完成形HTMLの印刷文字（答案用紙どおり）', s_, html_k, '完成形HTML')
absent('完成形HTMLに「添付情報」の欄', '添付情報', html_k, '完成形HTML')
judge('完成形HTMLの順序（登記の目的 → 添付書類 → 登録免許税）',
      html_k.index('登記の目的') < html_k.index('添　付　書　類') < html_k.index('登録免許税'))
h1_ = open(os.path.join(ZU, 'R3_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
h2_ = open(os.path.join(ZU, 'R3_dai21mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['<div class="rt">第1欄</div>', 'Ｘ座標（m）', 'Ｙ座標（m）', 'diag']:
    check('第1欄の画像の形（答案用紙どおり）', s_, h1_, '解答欄の画像')
judge('第1欄の画像の行の順（Ａ→Ｃ→Ｈ→Ｌ）', h1_.index('Ａ点') < h1_.index('Ｃ点') < h1_.index('Ｈ点') < h1_.index('Ｌ点'))
check('第2欄の画像の形（答案用紙どおり）', '<div class="rt">第2欄</div>', h2_, '解答欄の画像')
judge('第2欄の画像は「ア｜イ」「ウ｜エ」「オ｜カ」の3行', h2_.count('<tr>') == 3 and
      h2_.index('>ア<') < h2_.index('>イ<') < h2_.index('>ウ<') < h2_.index('>エ<') < h2_.index('>オ<') < h2_.index('>カ<'))
check('図25の説明文（第4欄の印刷）', '作成者・申請人の「（略）」、作成日の欄、縮尺 1／250', draw, '作図')
check('図25の説明文（第4欄の枠の中に実寸）', '第4欄の枠の中に1/250の実寸で描く', fig, '解説図')
check('図10の枠の大きさ', '答案用紙の第4欄の枠（横約30cm・縦約23cm）に収まるので', draw, '作図')
check('記事の第4欄の印刷', "『作成者』と『申請人』は『（略）』、縮尺の1/250も印刷済みよ。方位記号は印刷されていないから、自分で描くの")
check('記事の第4欄の枠の大きさ', '第4欄の枠は横約30cm・縦約23cmあるから、余裕で収まるわ')
mk_ = open(os.path.join(ZU, 'make_R3_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
for nm_, src_ in [('記事', text), ('解説図プロンプト', fig), ('申請書プロンプト', form), ('添削プロンプト', fix), ('見出し画像プロンプト', thumb),
                  ('作図スクリプト', draw), ('申請書の生成スクリプト', mk_)]:
    for w_ in ['仮のもの', '仮の形', 'リポジトリにない', '確かめたら直す']:
        judge(f'{nm_}に「{w_}」が残っていない', w_ not in src_)
bare_p = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)(?<!観測値の表の下の)(?<!注1〜)注[0-9]', fig.split('## 差し替えデータ')[-1])]
judge(f'解説図プロンプトの差し替えデータの注も書き分けている（{bare_p}）', not bare_p)
bare_f = [m.group(0) for m in re.finditer(r'(?<!問題文の)注[0-9]', form)]
judge(f'申請書のプロンプトの注も書き分けている（{bare_f}）', not bare_f)

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


# (まとめの項目の語, マーカーの文言の頭, 図の直前の発言にある決め手の語)
TRAPS = [('**観測角は時計回りに足す**', 'T1からの放射でA点を求める図', '正しい向きで出せた証拠'),
         ('**C点は隅切剪除長で測る**', '隅切りでC点を求める図', '隅切りの角は'),
         ('**H点はE点の杭ではない**', 'H点が筆界点と判断される流れの図', '筆界点は杭の位置じゃなくて'),
         ('**H点は10番2の地積測量図で裏付ける**', 'H点の求め方の図', '定義どおり交点で出して'),
         ('**L点の台形は平行四辺形ではない**', 'L点の求め方の図', '平行四辺形のつもりで出したら'),
         ('**地図は区画・地番、準ずる図面は位置・形状・地番**', '地図と地図に準ずる図面の比較図', '対で覚えなさい'),
         ('**閉鎖しても保存期間は永久**', '閉鎖と保存期間の図', '永久に保存されるの'),
         ('**精度区分は地域で決まる**', '精度区分の図', '市街地地域は甲2まで'),
         ('**地積更正は公差で決める**', '公差の判定図', '土地分筆登記だけです'),
         ('**申請人は二郎が一郎と三郎に代位**', '申請人の関係図', '遺産分割協議書がそれに当たるわ'),
         ('**相続を証する情報は、相続の登記が未了だから要る**', '相続を証する情報が要るかの判定の図', 'この分筆が済んでからよ'),
         ('**添付書類に代位原因証書を足す**', '登記申請書「添付書類」欄の誤答', '代位原因証書'),
         ('**登録免許税は分筆後の個数**', '登記申請書「登録免許税」欄の誤答', '残る10番1も数えるの'),
         ('**分筆前の行の地積は登記記録の386.30**', '分筆前の行の地積の図', '386.30を写すの'),
         ('**分筆元の原因は「③10番1、10番8、10番9に分筆」**', '登記申請書「土地の表示」欄（登記原因）', '自分の10番1も入れるのよ'),
         ('**辺長は小数第3位を四捨五入**', '辺長11本の計算の図', '端数の処理を表にしておくわね'),
         ('**地積測量図に書くもの・書かないもの・描かない点**', '地積測量図に書くもの・書かないもの・描かない点の図', '- **描かない点**'),
         ('**作図の範囲はT1・T2まで入れる**', '今年だけの注と作図の範囲の図', '余裕で収まるわ')]
matome = text[text.index('## 第10章'):]
trap_items = [l for l in matome.splitlines() if l.startswith('- **') and '：' in l and not re.match(r'- \*\*[1-9]番目\*\*', l)]
judge(f'まとめのわなの数 {len(trap_items)} ＝ 対応表 {len(TRAPS)}', len(trap_items) == len(TRAPS))
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
# 計算過程の図（電卓の表示・答えの直後）
for hd, key in [('H点の交点の比の図', '符号が同じだからtは正'), ('L点の交点の比の図', '今度は1より小さいので'),
                ('丙区画の面積の計算の図', '丙区画は135.84㎡です'), ('乙区画の面積の計算の図', '乙区画は126.84㎡です'),
                ('甲区画の面積の計算の図', '甲区画は123.21㎡です'), ('全体の時系列の図', 'ここがあとで効いてくるわ'),
                ('注の仕分けの表', '書き分けるわ')]:
    mk = marker_of(hd)
    judge(f'計算過程・前提の図がある : {hd}', mk is not None and key in prev_line(mk))

# 図番号（PNG名）が記事の挿入順に1〜26で並ぶ
nums = [int(re.match(r'R3_dai21mon_zu(\d+)_', n).group(1)) for n, _, _ in PNGS if '_zu' in n]
judge(f'解説図のPNG番号が記事の挿入順に1〜26で並ぶ : {nums}', nums == list(range(1, 27)))

# 画像の中に図番がない（作図スクリプトの new_figure・suptitle の題）
titled = re.findall(r"(?:new_figure|suptitle)\(\s*f?'([^']*)'", draw)
judge(f'作図スクリプトの題 {len(titled)}個に図番がない', titled and not [x for x in titled if re.match(r'図\d', x)])
absent('解説図プロンプトに旧「図N　」の題', '画像の中のタイトルは作成時の', fig, '解説図')

# セリフは260字以内
long_ = [i + 1 for i, l in enumerate(lines) if l.startswith('「') and len(l) > 260]
judge(f'セリフが260字以内 : 超えた行 {long_}', not long_)

# 電卓操作のキー列を実行して直後の「表示：」と一致するか
from keysim_note_article import simulate  # noqa: E402
sim = simulate(os.path.join(HERE, 'note_R3_dai21mon_tochi_kaiwa_kaisetsu.md'))
judge(f'キー列を再現した表示の数 {len(sim)}（記事の「表示：」16個）', len(sim) == 16)
for n_, want, got, ok_ in sim:
    judge(f'キー列の再現 {n_}行目 : 記事「{want}」／ 再現「{got}」', ok_)

# ---- 試験の答案用紙の原本（touan_youshi/）の寸法を測り直し、作図・HTMLの値と比べる ----
import pymupdf  # noqa: E402
MM = 25.4 / 72
_doc = pymupdf.open(TOUAN)


def _segs(page):
    M_ = page.rotation_matrix           # 原本のページは90度回転している。罫線の座標を回転後の向きにそろえる
    out = []
    for dr in page.get_drawings():
        for it in dr['items']:
            if it[0] == 'l':
                out.append((it[1] * M_, it[2] * M_))
            elif it[0] in ('re', 'qu'):
                r = it[1].rect if it[0] == 'qu' else it[1]
                P_ = pymupdf.Point
                pts_ = [P_(r.x0, r.y0) * M_, P_(r.x1, r.y0) * M_, P_(r.x1, r.y1) * M_, P_(r.x0, r.y1) * M_]
                out += [(pts_[k], pts_[(k + 1) % 4]) for k in range(4)]
    return out


def _vl(page, xmin, xmax, ymin=-1e9, ymax=1e9):
    return sorted({round(a.x * MM, 1) for a, b in _segs(page) if abs(a.x - b.x) < 0.3 and abs(a.y - b.y) * MM > 6
                   and xmin <= a.x * MM <= xmax and ymin <= a.y * MM <= ymax})


def _hl(page, xmin, xmax):
    return sorted({round(a.y * MM, 1) for a, b in _segs(page) if abs(a.y - b.y) < 0.3 and abs(a.x - b.x) * MM > 10
                   and xmin <= min(a.x, b.x) * MM + 0.2 and max(a.x, b.x) * MM <= xmax + 0.2})


vl0 = _vl(_doc[0], 230, 404, 140, 280)
for c in [232.6, 242.6, 273.6, 298.6, 323.6, 340.6, 402.6]:
    judge(f'原本の罫線に x={c}mm がある（土地の表示の表）', any(abs(c - v) < 0.3 for v in vl0))
W = 402.6 - 232.6
ratios = [100 * x / W for x in (242.6 - 232.6, 273.6 - 242.6, 298.6 - 273.6, 323.6 - 298.6, 340.6 - 323.6, 402.6 - 340.6)]
mk_html = open(os.path.join(ZU, 'make_R3_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
html_cols = [float(x) for x in re.findall(r'<col style="width:([0-9.]+)%">', html_k)]
judge(f'土地の表示の列の幅の比（原本 {[round(x, 1) for x in ratios]}）と申請書HTML {html_cols} が0.2%以内',
      len(html_cols) == 6 and all(abs(a_ - b_) < 0.2 for a_, b_ in zip(ratios, html_cols)))
hl0 = _hl(_doc[0], 232, 403)
# 土地の表の行：所在18mm・見出し8mm・記入行22mm×5
for y_ in [143.0, 161.0, 169.0, 191.0, 213.0, 235.0, 257.0, 279.0]:
    judge(f'原本の罫線に y={y_}mm がある（土地の表示の行）', any(abs(y_ - v) < 0.3 for v in hl0))
# 第1欄・第2欄・第3欄の枠の高さ（15mm・53mm・95mm）
hl_left = _hl(_doc[0], 85, 224)
for lo, hi, mm_ in [(188.8, 203.8, 15), (207.8, 260.8, 53), (264.8, 279.8, 15)]:
    judge(f'原本の左の列の枠 y {lo}〜{hi}mm（{mm_}mm）',
          any(abs(lo - v) < 0.3 for v in hl_left) and any(abs(hi - v) < 0.3 for v in hl_left))
judge('原本の申請人の枠 y 27.2〜122.2mm（95mm）', any(abs(27.2 - v) < 0.3 for v in hl0) and any(abs(122.2 - v) < 0.3 for v in hl0))
vv0 = _vl(_doc[0], 232, 403, 20, 125)
judge('原本の申請人の枠 x 232.6〜402.6mm（170mm）', any(abs(232.6 - v) < 0.3 for v in vv0) and any(abs(402.6 - v) < 0.3 for v in vv0))
for nm_, v_ in [('登記の目的・登録免許税', 'H_15, H_53, H_95 = 94, 330, 592')]:
    check(f'申請書の生成スクリプト：枠の高さは原本の15mm・53mm・95mm（×6.235px）', v_, mk_html, '生成スクリプト')
judge('枠の高さの px が原本の mm × 6.235（15mm→94、53mm→330、95mm→592）', round(15 * 6.235) == 94 and round(53 * 6.235) == 330 and round(95 * 6.235) == 592)
# 第1欄（左の列の表）・第2欄
vl1 = _vl(_doc[0], 60, 226, 30, 112)
judge(f'原本の第1欄の列の境 {vl1}（3列が等幅 53.6mm）', all(any(abs(c - v) < 0.4 for v in vl1) for c in (62.7, 116.3, 170.0, 223.7)))
vl2 = _vl(_doc[0], 60, 226, 120, 172)
judge(f'原本の第2欄の列の境 {vl2}（記号10.2%・記入39.8%）', all(any(abs(c - v) < 0.4 for v in vl2) for c in (62.7, 79.2, 143.2, 159.7, 223.7)))
cw1 = [float(x) for x in re.findall(r'<col style="width:([0-9.]+)%">', h1_)]
cw2 = [float(x) for x in re.findall(r'<col style="width:([0-9.]+)%">', h2_)]
judge(f'第1欄HTMLの列の幅 {cw1}（3列が等幅）', len(cw1) == 3 and all(abs(c - 33.3) < 0.2 for c in cw1))
judge(f'第2欄HTMLの列の幅 {cw2}（原本の10.2・39.8の2組）', len(cw2) == 4 and abs(cw2[0] - 10.2) < 0.2 and abs(cw2[1] - 39.8) < 0.2)
for nm_, hh_ in [('完成形', html_k)] + [(f'添削（{k}）', v) for k, v in MG.items()]:
    absent(f'{nm_}HTMLに style="height: が残っていない', 'style="height:', hh_, f'{nm_}画像')
    absent(f'{nm_}HTMLに「第○欄」の見出しがない', '第3欄', hh_, f'{nm_}画像')
check('完成形HTML：枠は min-height', 'min-height:94px', html_k, '完成形画像')
check('完成形HTML：添付書類の枠は原本の53mm', 'min-height:330px', html_k, '完成形画像')
check('完成形HTML：申請人の枠は原本の95mm', 'min-height:592px', html_k, '完成形画像')
# 第4欄の枠（原本の2ページ目）と作図スクリプトの値
vv, hh2 = _vl(_doc[1], 80, 383), _hl(_doc[1], 80.6, 382.6)
judge('原本の第4欄の枠 x 80.6〜382.6mm', any(abs(80.6 - v) < 0.3 for v in vv) and any(abs(382.6 - v) < 0.3 for v in vv))
judge('原本の第4欄の枠 y 25.8〜256.8mm', any(abs(25.8 - v) < 0.3 for v in hh2) and any(abs(256.8 - v) < 0.3 for v in hh2))
dflat = re.sub(r'\s', '', draw)
check('作図の枠の寸法（原本の測定値）', 'ORIG_FRAME_MM=(80.6,25.8,382.6,256.8)', dflat, '作図')
check('作図の用紙の外枠（原本の測定値）', 'ORIG_SHEET_MM=(56.3,12.2,406.9,274.8)', dflat, '作図')
judge('枠 横302mm・縦231mm（1/250で横75.5m・縦57.75m）にT1・T2を入れた図（東西31.5m・南北22.18m）が収まる',
      abs((382.6 - 80.6) / 4 - 75.5) < 1e-9 and 31.5 < 75.5 and 22.18 < 57.75)
# 固定配置の整理図は目視確認の対象（自動検査の対象外）
check('整理図は目視確認の対象', '整理図（固定配置。目視で確認する）', draw, '作図')
# フォント
from zu_helpers import setup_font as _sf  # noqa: E402
_fn = _sf()
judge(f'作図のフォントが Noto Sans CJK JP（実際: {_fn}）', 'Noto' in _fn)

print('NG件数:', ng)
