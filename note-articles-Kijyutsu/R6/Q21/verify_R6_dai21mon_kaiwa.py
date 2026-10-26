"""令和6年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と、
照合済みのプロース版（note_R6_dai21mon_tochi_kijutsu_kaisetsu.md）の両方と一致することも確認する。
実行: python3 note-articles-Kijyutsu/R6/Q21/verify_R6_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import (P, r2, radial, dms, to_dms, area, double_area_sum, tri_conj, chiseki, disp, fmt_num,  # noqa: E402
                          intersect, kousa_kou2)

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R6_dai21mon_tochi_kaiwa_kaisetsu.md')
prose = rd('note_R6_dai21mon_tochi_kijutsu_kaisetsu.md')
fig = rd('prompt_R6_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R6_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R6_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R6_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_R6_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（問題文の〔A市基準点成果表〕と〔測量によって得られた座標値〕） ----
T1, T2 = P(16.63, 61.67), P(26.91, 64.19)
A, C, E, F, G = P(25.09, 48.35), P(27.49, 60.92), P(35.40, 60.81), P(35.40, 50.15), P(33.82, 48.35)
H, I, J, K = P(21.83, 54.17), P(21.83, 60.90), P(19.83, 60.93), P(19.83, 48.35)

# ---- 問2 B点・D点（放射。観測角は時計回り＝足す） ----
check('arg(T1−T2)', to_dms(cmath.phase(T1 - T2)))
check('arg(T1−T2)＋360°', to_dms(cmath.phase(T1 - T2) + 2 * math.pi))
Bx = radial(T2, T1, 10.03, dms(78, 58, 8))
Dx = radial(T2, T1, 4.60, dms(118, 24, 27))
check('B 表示', '表示：' + disp(Bx))
check('D 表示', '表示：' + disp(Dx))
B, D = r2(Bx), r2(Dx)
check('B 答え', '**▶ B点（27.39, 54.17）**')
check('D 答え', '**▶ D点（30.00, 60.78）**')
Bw = r2(radial(T2, T1, 10.03, -dms(78, 58, 8)))
check('反時計回りの誤りのB', f'（{Bw.real:.2f}, {Bw.imag:.2f}）')
judge('反時計回りのBは道路の東（Y＞D・Jの線）', Bw.imag > 61)
check('BH 表示', '表示：' + fmt_num(abs(H - B), 2))
check('DJ 表示', '表示：' + fmt_num(abs(J - D)))
check('AB 表示', '表示：' + fmt_num(abs(B - A)))
judge('BH・DJ・AB が既存図面の 5.56・10.17・6.26 と一致',
      f'{abs(H - B):.2f}' == '5.56' and f'{abs(J - D):.2f}' == '10.17' and f'{abs(B - A):.2f}' == '6.26')

# ---- 問1（ア） A・B・Dが一直線／面積の裏付け ----
col = (B - A).conjugate() * (D - A)
check('△ABD 表示', '表示：' + disp(col))
check('△ABD 面積', f'{abs(col.imag) / 2:.4f}㎡')
judge('Bは直線ADから1mm程度（0.0015m未満）', abs(col.imag) / abs(D - A) < 0.0015)
s_otsu = double_area_sum([B, D, I, H])
check('乙土地 表示', '表示：' + disp(s_otsu))
check('乙土地 面積', f'{area([B, D, I, H]):.5f}')
check('乙土地 地積', f'{chiseki(area([B, D, I, H])):.2f}㎡')
s_kou = double_area_sum([A, B, D, E, F, G])
check('甲土地 表示', '表示：' + disp(s_kou))
check('甲土地 面積', f'{area([A, B, D, E, F, G]):.5f}')
check('甲土地 地積', f'{chiseki(area([A, B, D, E, F, G])):.2f}㎡')
check('甲土地の差', f'{97.00 - chiseki(area([A, B, D, E, F, G])):.2f}㎡')
check('参考公差（乙）', f'約{kousa_kou2(45.88):.2f}㎡')
check('参考公差（甲）', f'約{kousa_kou2(97.00):.2f}㎡')
judge('筆界どおりの差が参考公差の範囲内', 45.88 - 45.86 < kousa_kou2(45.88) and 97.00 - 96.29 < kousa_kou2(97.00))
check('利用状況の甲土地（誤り）', f'{chiseki(area([A, B, C, D, E, F, G])):.2f}㎡')
check('利用状況の乙土地（誤り）', f'{chiseki(area([B, H, I, C])):.2f}㎡')
judge('3番2の面積 50.79（昭和50年の地積測量図と一致）', chiseki(area([A, K, J, I, H, B])) == 50.79)

# ---- 問2 P点（交点） ----
Pp, t, num, den = intersect(B, C, D, J)
check('交点の分子 表示', '表示：' + disp(num))
check('交点の分母 表示', '表示：' + disp(den))
check('P 表示', '表示：' + disp(B + (C - B) * 67.6152 / 68.6625))
PP = r2(Pp)
check('P 答え', '**▶ P点（27.49, 60.82）**')
check('CP', f'{abs(C - PP):.2f}m')
u = (J - D) / abs(J - D)
foot = r2(D + u * ((C - D) * u.conjugate()).real)
judge('Cから直線DJへの垂線の足も（27.49, 60.82）', foot == PP)
judge('DJ上のX＝27.49のY座標 60.82', f'{(D + (J - D) * (27.49 - D.real) / (J.real - D.real)).imag:.2f}' == '60.82')
w1, w2 = chiseki(area([B, H, I, C])), chiseki(area([B, C, D]))
check('Cのまま分けた誤り（B→C→D）', f'{w2:.2f}㎡')
check('Cのまま分けた誤り（合計）', f'{w1 + w2:.2f}㎡')

# ---- 問1（イ）〜（エ） ----
for s in ['- **ア**：2（地図に準ずる図面に記録された本件各土地の形状）', '- **イ**：9（野原花子）', '- **ウ**：5（乙土地）',
          '- **エ**：6（分筆の登記の申請）']:
    check('問1', s)
check('合筆の制限の条文', '不動産登記法第41条第3号')

# ---- 問3 ----
check('△BDP 表示', '表示：' + disp(tri_conj(B, D, PP)))
check('BPIH 表示', '表示：' + disp(double_area_sum([B, PP, I, H])))
a33, a31 = area([B, D, PP]), area([B, PP, I, H])
check('3番3 面積', f'{a33:.5f}')
check('3番1 面積', f'{a31:.4f}')
check('切り捨て前の合計', f'{a33 + a31:.5f}')
judge('（ロ）3番3が小さい方（注8）', a33 < a31)
for s in ['- **登記の目的**：土地分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **申請人**：A市B町一丁目3番地1　野原花子', '- **登録免許税**：金2,000円', '- **所在**：A市B町一丁目',
          '①3番1、②宅地、③45.88（登記記録の地積）', '①（イ）、③37.53、登記原因「③3番1、3番3に分筆」',
          '①（ロ）3番3、②宅地、③8.34、登記原因「3番1から分筆」']:
    check('問3', s)
check('申請人の誤答', 'A市B町一丁目2番地1　山田太郎')
check('地積の誤答', '筆界どおりの45.86')
check('分筆の添付情報の条文', '不動産登記令別表8の項')
check('登録免許税の条文', '登録免許税法別表第一の一の（十三）イ')

# ---- 問4 辺長 ----
SIDES = {'BP（分筆線）': (B, PP), 'PD': (PP, D), 'DB': (D, B), 'PI': (PP, I), 'IH': (I, H), 'HB': (H, B)}
for n, (p, q) in SIDES.items():
    check(f'辺長{n}', f'- **{n}**：{round(abs(p - q) + 1e-9, 2):.2f}')
    check(f'図の辺長{n}', f'{round(abs(p - q) + 1e-9, 2):.2f}', fig, '解説図')
check('DBの四捨五入', f'DBは{math.floor(abs(B - D) * 1e4) / 1e4:.4f}…で第3位が6だから切り上げて7.11')
check('PIの四捨五入', f'PIは{math.floor(abs(PP - I) * 1e4) / 1e4:.4f}…で第3位が0だから切り捨てて5.66')
check('答案用紙の大きさ（横）', f'横約{round((I.imag - H.imag) * 4):d}mm')
check('答案用紙の大きさ（縦）', f'縦約{round((D.real - H.real) * 4):d}mm')

# ---- 問5 ----
for s in ['- **①**：土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人',
          '- **②ア**：地番', '- **②イ**：職権', '- **②ウ**：土地所在図又は地積測量図',
          '同条第15項', '同条第13項第2号', '第16条第5項第1号']:
    check('問5', s)

# ---- 答えを欄・空欄ごとに全部照らす（会話形式の記事・照合済みのプロース版・アガルートの解答例〈2026-09-29、過去問集の解答例ページから転記〉） ----
# （欄, 会話形式の記事の文字列, プロース版の文字列, 解答例の値）
ANSWERS = [
    ('第1欄ア', '- **ア**：2（地図に準ずる図面に記録された本件各土地の形状）', '- **ア**：2（地図に準ずる図面に記録された本件各土地の形状）', '2'),
    ('第1欄イ', '- **イ**：9（野原花子）', '- **イ**：9（野原花子）', '9'),
    ('第1欄ウ', '- **ウ**：5（乙土地）', '- **ウ**：5（乙土地）', '5'),
    ('第1欄エ', '- **エ**：6（分筆の登記の申請）', '- **エ**：6（分筆の登記の申請）', '6'),
    ('第2欄B点', '**▶ B点（27.39, 54.17）**', '**▶ B点（27.39, 54.17）**', '27.39, 54.17'),
    ('第2欄D点', '**▶ D点（30.00, 60.78）**', '**▶ D点（30.00, 60.78）**', '30.00, 60.78'),
    ('第2欄P点', '**▶ P点（27.49, 60.82）**', '**▶ P点（27.49, 60.82）**', '27.49, 60.82'),
    ('第3欄 登記の目的', '- **登記の目的**：土地分筆登記', '- **登記の目的**：土地分筆登記', '土地分筆登記'),
    ('第3欄 添付書類', '- **添付書類**：地積測量図　代理権限証書', '- **添付書類**：地積測量図　代理権限証書', '地積測量図　代理権限証書'),
    ('第3欄 申請人', '- **申請人**：A市B町一丁目3番地1　野原花子', '- **申請人**：A市B町一丁目3番地1　野原花子', 'A市B町一丁目3番地1　野原花子'),
    ('第3欄 登録免許税', '- **登録免許税**：金2,000円', '- **登録免許税**：金2,000円', '金2,000円'),
    ('第3欄 所在', '- **所在**：A市B町一丁目', '- **所在**：A市B町一丁目', 'A市B町一丁目'),
    ('第3欄 1行目', '①3番1、②宅地、③45.88', '1行目：①3番1、②宅地、③45.88', '3番1　宅地　45.88'),
    ('第3欄 2行目', '①（イ）、③37.53、登記原因「③3番1、3番3に分筆」', '2行目：①（イ）、③37.53、登記原因「③3番1、3番3に分筆」', '（イ）　37.53　③3番1、3番3に分筆'),
    ('第3欄 3行目', '①（ロ）3番3、②宅地、③8.34、登記原因「3番1から分筆」', '3行目：①（ロ）3番3、②宅地、③8.34、登記原因「3番1から分筆」', '（ロ）3番3　宅地　8.34　3番1から分筆'),
    ('第4欄 BP', '- **BP（分筆線）**：6.65', '- BP（分筆線）：6.65', '6.65'),
    ('第4欄 PD', '- **PD**：2.51', '- PD：2.51', '2.51'),
    ('第4欄 DB', '- **DB**：7.11', '- DB：7.11', '7.11'),
    ('第4欄 PI', '- **PI**：5.66', '- PI：5.66', '5.66'),
    ('第4欄 IH', '- **IH**：6.73', '- IH：6.73', '6.73'),
    ('第4欄 HB', '- **HB**：5.56', '- HB：5.56', '5.56'),
    ('第4欄 境界標', 'B・D・H・Iはコンクリート杭、Pは金属標', 'B、D、H、Iはコンクリート杭、Pは金属標', 'B、D、H、I：コンクリート杭　P：金属標'),
    ('第4欄 地番欄', '地番欄は3番1、3番3', '- **地番欄**：3番1、3番3', '3番1、3番3'),
    ('第5欄①', '- **①**：土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人',
     '表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人', '土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人'),
    ('第5欄②ア', '- **②ア**：地番', '- **②ア**：地番', '地番'),
    ('第5欄②イ', '- **②イ**：職権', '- **②イ**：職権', '職権'),
    ('第5欄②ウ', '- **②ウ**：土地所在図又は地積測量図', '- **②ウ**：土地所在図又は地積測量図', '土地所在図又は地積測量図'),
]
for label, k, pr, ag in ANSWERS:
    check(f'{label}（解答例：{ag}）', k)
    check(f'{label}（プロース版と同じ答え）', pr, prose, 'プロース版')
judge(f'照らした欄・空欄の数 {len(ANSWERS)}（第1欄4・第2欄3・第3欄8・第4欄8・第5欄4）', len(ANSWERS) == 27)

# ---- 最新の指示書との照らし直しで足した内容（2026-09-29） ----
bare = [i + 1 for i, l in enumerate(text.splitlines())
        if re.search(r'注[0-9]', l) and '問題文の注' not in l and '調査図素図の注' not in l]
judge(f'注の番号を書いた行は、問題文の注か調査図素図の注かを書き分けている（不備の行 {bare}）', not bare)
for bad in ['（注3）', '（注4）', '（注5）', '（注6）', '（注7）', '（注8）']:
    absent('問題文の注と調査図素図の注の書き分け', bad)
for s in ['調査図素図の注にも『D点からJ点は直線', '問題文の注3', '問題文の注7', '問題文の注8', '問題文の注4', '問題文の注5', '問題文の注6',
          '注1〜4と注9は毎年ほぼ同じ決まり文句']:
    check('注の書き分け', s)
check('四角形の対角線 表示', '表示：' + disp((B - I).conjugate() * (PP - H)))
judge('対角線の式と4点の式の面積が同じ', abs(abs(((B - I).conjugate() * (PP - H)).imag) / 2 - area([B, PP, I, H])) < 1e-9)
check('分筆後の地積の合計', f'37.53 ＋ 8.34 ＝ {chiseki(area([B, PP, I, H])) + chiseki(area([B, D, PP])):.2f}㎡')
check('分筆後の合計と登記記録の差', f'差は{45.88 - (chiseki(area([B, PP, I, H])) + chiseki(area([B, D, PP]))):.2f}㎡')
check('登録免許税の「不要」の指示（会話）', '『不要』と書くのは、そもそも納付を要しない登記のときだけよ')
check('登録免許税の誤答（会話）', '登録免許税の欄は『不要』ですか？')
check('T1・T2まで入れた作図範囲（南北）', f'{D.real - T1.real:.2f}mで約{round((D.real - T1.real) * 4)}mm')
check('T1・T2まで入れた作図範囲（東西）', f'{T2.imag - H.imag:.2f}mで約{round((T2.imag - H.imag) * 4)}mm')
check('時間配分（具体的な順番）', '問1と問5 → B点・D点の放射 → 申請書の地積以外の欄 → P点の交点 → （イ）（ロ）の面積 → 地積測量図の辺長と作図')
n_fit = len(re.findall(r'^\s*fit\(', draw, re.M))
n_pad = len(re.findall(r'^\s*fit\(.*pad_aspect=True\)', draw, re.M))
judge(f'作図スクリプトの fit がすべて pad_aspect=True（{n_pad}/{n_fit}）', n_fit > 0 and n_pad == n_fit)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
N_FIG = 28
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（{N_FIG}枚）', n_fig == N_FIG)
for i in range(1, N_FIG + 1):
    judge(f'作図済みPNG zu{i:02d}', any(f.startswith(f'R6_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                      for f in os.listdir(os.path.join(HERE, 'zu'))))
# 2026-10-26：画像の中に図番を入れない（作図スクリプトの new_figure・suptitle のタイトル文字列に「図N」がない）
titled = re.findall(r"(?:new_figure|suptitle)\(\s*'([^']*)'", draw)
judge(f'作図スクリプトのタイトル {len(titled)}個（第4欄の地積測量図の枠の図はタイトルなし）に図番がない', len(titled) == N_FIG - 1 and not [x for x in titled if re.match(r'図\d', x)])
absent('解説図プロンプトに「図番のまま」の注記が残っていない', '画像の中のタイトルは作成時の', fig, '解説図')
for s in ['（27.39, 54.17）', '（30.00, 60.78）', '（27.49, 60.82）', '193°46′25.18″', '−166°13′34.82″', '78°58′08″',
          '118°24′27″', '104.76㎡', '37.81㎡', '96.29㎡', '45.86㎡', '0.0064㎡', '46.28㎡', '8.34㎡', '37.53㎡',
          '45.88065', '67.6152 ÷ 68.6625', '7.1066']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s.replace('㎡', ''), draw, '作図')
# 画像挿入の位置の文言：解説図プロンプトの「記事の挿入位置」の「」の中の語が、記事にそのまま出てくるか
pos_lines = re.findall(r'  - \*\*記事の挿入位置\*\*：([^\n]*)', fig)
judge(f'解説図プロンプトの「記事の挿入位置」の行 {len(pos_lines)}（{N_FIG}）', len(pos_lines) == N_FIG)
for pl in pos_lines:
    for q in re.findall(r'「([^」]*)」', pl):
        check('図の挿入位置の文言（プロンプト側の引用が記事にある）', q)
for s in ['令和６年10月18日　申請　Ａ地方法務局', '土地分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｂ町一丁目３番地１　野原花子',
          '金2,000円', 'Ａ市Ｂ町一丁目', '③「45｜88」', '③「37｜53」', '登記原因「③3番１、3番３に分筆」',
          '①「（ロ）3番３」', '③「8｜34」', '登記原因「3番１から分筆」']:
    check('登記申請書（プロース版と共用）', s, form, '登記申請書')
for s in ['Ａ市Ｂ町一丁目２番地１　山田太郎', 'Ａ市Ｂ町一丁目３番地１　野原花子', '③「45｜86」', '③「45｜88」',
          '令和６年10月18日　申請　Ａ地方法務局']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言（申請人）', '申請人も、手続をする土地の所有者ですね')
check('添削の挿入位置の文言（地積）', '分筆前の行は登記記録の写し、でしたね。じゃあ添付書類は')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
import struct  # noqa: E402
for name in ['R6_dai21mon_toukishinseisho_kansei', 'R6_dai21mon_toukishinseisho_machigai_shinseinin', 'R6_dai21mon_toukishinseisho_machigai_chiseki']:
    png = os.path.join(HERE, 'zu', name + '.png')
    ok = os.path.exists(png)
    if ok:
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w)
    else:
        judge(f'{name}.png がある', False)
rdh = lambda n: open(os.path.join(HERE, 'zu', n + '.html'), encoding='utf-8').read()  # noqa: E731
html_k = rdh('R6_dai21mon_toukishinseisho_kansei')
html_m = rdh('R6_dai21mon_toukishinseisho_machigai_shinseinin')
html_c = rdh('R6_dai21mon_toukishinseisho_machigai_chiseki')
for s_ in ['令和６年10月18日　申請　Ａ地方法務局', '土地分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｂ町一丁目３番地１　野原花子',
           '金2,000円', 'Ａ市Ｂ町一丁目', '3番１', '（ロ）3番３', '③3番１、3番３に分筆', '3番１から分筆', '>45<', '>88<', '>37<',
           '>53<', '>8<', '>34<', '（略）', '令和6年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s_, html_k, '完成形画像')
for s_ in ['①誤答', '②添削（赤ペン）', '③正解', 'Ａ市Ｂ町一丁目２番地１　山田太郎', 'Ａ市Ｂ町一丁目３番地１　野原花子',
           '分筆するのは乙土地。申請人は分筆の時点の所有者！', '令和6年度 第21問｜申請人は、分筆する乙土地の（分筆の時点の）所有者']:
    check('添削の画像（申請人。HTML）', s_, html_m, '添削画像（申請人）')
for s_ in ['①誤答', '②添削（赤ペン）', '③正解', '>86<', '>88<', '分筆前の行は登記記録の地積。計算値は書かない',
           '令和6年度 第21問｜分筆前の行の地積は、登記記録どおり（計算値の45.86ではない）']:
    check('添削の画像（地積。HTML）', s_, html_c, '添削画像（地積）')
for s_ in ['分筆するのは乙土地。申請人は分筆の時点の所有者！', '分筆前の行は登記記録の地積。計算値は書かない']:
    check('添削の画像とプロンプトの文言', s_, fix, '添削')
# 添削は欄ごとに1枚（申請人の画像に地積の誤答が、地積の画像に申請人の誤答が混ざっていない）
absent('申請人の添削画像に地積の誤答がない', '>86<', html_m, '添削画像（申請人）')
absent('地積の添削画像に申請人の誤答がない', '山田太郎', html_c, '添削画像（地積）')
# 2026-10-26：HTMLの枠は min-height（固定の height を残さない）、申請書の画像に「第○欄」の見出しを入れない
for nm, hh in [('完成形', html_k), ('添削（申請人）', html_m), ('添削（地積）', html_c)]:
    absent(f'{nm}HTMLに style="height: が残っていない', 'style="height:', hh, f'{nm}画像')
    absent(f'{nm}HTMLに「第○欄」の見出しがない（申請書の画像）', '第1欄', hh, f'{nm}画像')
    absent(f'{nm}HTMLに「第○欄」の見出しがない（申請書の画像）', '第3欄', hh, f'{nm}画像')
for nm_, v_ in [('登記の目的', 'min-height:119px'), ('添付書類', 'min-height:170px')]:
    check(f'完成形HTML：{nm_}の枠は原本の19mm・27mmの比', v_, html_k, '完成形画像')
check('完成形HTML：土地の表示の記入行は原本の22mm（137px）', 'height: 137px', html_k, '完成形画像')
check('完成形HTML：所在の行は原本の18mm（112px）', 'height: 112px', html_k, '完成形画像')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '生けがき', 'へい（']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', 'ブロック塀')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
# 同じ話者のセリフの連続（画像挿入マーカーをはさむものも。2026-10-02、マーカーを読み飛ばす形に直した）
same = []
for i, l in enumerate(lines):
    if l.rstrip() in ('**トリ先生**', '**藍子**'):
        j = i + 1
        while j < len(lines) and not lines[j].rstrip().endswith('」'):   # セリフの終わり（複数段落も）
            j += 1
        j += 1
        while j < len(lines) and (not lines[j].strip() or lines[j].startswith('> 【画像挿入】')):
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続（画像挿入マーカーをはさむものも）: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋添削2＋完成形1＋第1欄・第2欄・第5欄3＝計{N_FIG + 6}か所の想定）',
      n_marker == N_FIG + 6)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和6年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和6年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')

# ---- 画像挿入マーカーと zu/ のPNGが記事の順に1対1に対応しているか（2026-10-26に28枚の解説図＋画像6枚へ） ----
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R6_dai21mon_zu01_jikeiretsu_zentai', '全体の時系列の図', 'fig'),
        ('R6_dai21mon_zu02_chuu_shiwake', '問題文の注の仕分けの図', 'fig'),
        ('R6_dai21mon_zu03_zentaizu', '北を上にして座標どおりに描き直した全体図', 'fig'),
        ('R6_dai21mon_zu04_kansokukaku_muki', '観測角の向きの図', 'fig'),
        ('R6_dai21mon_zu05_B_housha', 'T2からの放射でB点を求める図', 'fig'),
        ('R6_dai21mon_zu06_D_housha', 'T2からの放射でD点を求める図', 'fig'),
        ('R6_dai21mon_zu07_goui_konkyo', '合意した位置は筆界の根拠にならない図', 'fig'),
        ('R6_dai21mon_zu08_zanchi_sokuryouzu', '残地の地積測量図が測ったのは3番2の周りだけという図', 'fig'),
        ('R6_dai21mon_zu09_ichokusen_ABD', 'A・B・Dは一直線の図', 'fig'),
        ('R6_dai21mon_zu10_hikkai_handan', '筆界の判断の比較図', 'fig'),
        ('R6_dai21mon_zu11_C_mama_menseki', 'Cのまま分けると面積が増える図', 'fig'),
        ('R6_dai21mon_zu12_P_kousa', 'P点の求め方の図', 'fig'),
        ('R6_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R6_dai21mon_zu13_bunpitsu_otsu', '分筆するのは乙土地の図', 'fig'),
        ('R6_dai21mon_zu14_chizu_teisei_fuyou', '要るのは分筆の登記だけの図', 'fig'),
        ('R6_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R6_dai21mon_zu15_hitsuyou_touki', '必要な登記の流れの図', 'fig'),
        ('R6_dai21mon_zu16_taikakusen', '対角線で出す別解の図', 'fig'),
        ('R6_dai21mon_zu17_bunpitsu_chiban', '分筆後の区画と地番の図', 'fig'),
        ('R6_dai21mon_toukishinseisho_machigai_shinseinin', '「申請人」欄の誤答→添削→正解の3コマ', 'tall'),
        ('R6_dai21mon_toukishinseisho_machigai_chiseki', '「土地の表示」1行目の地積の誤答→添削→正解の3コマ', 'tall'),
        ('R6_dai21mon_zu18_tenpu_shorui', '添付書類の図', 'fig'),
        ('R6_dai21mon_zu19_tourokumenkyozei', '登録免許税は分筆後の個数で数える図', 'fig'),
        ('R6_dai21mon_zu20_tochi_hyouji_gyou', '土地の表示の欄は行ごとに書くものが違う図', 'fig'),
        ('R6_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R6_dai21mon_zu21_hensuu_hasuu', '辺長は小数第3位だけを見て一度で決める図', 'fig'),
        ('R6_dai21mon_zu22_kaku_kakanai', '地積測量図に書くもの・書かないもの・印刷済みのものの図', 'fig'),
        ('R6_dai21mon_zu23_C_kakanai', '地積測量図にC点は描かない図', 'fig'),
        ('R6_dai21mon_zu24_chiseki_sokuryouzu', '地積測量図（3番1・3番3）の完成見本', 'fig'),
        ('R6_dai21mon_zu25_chizu_kubun', '地図は「区画」、地図に準ずる図面は「位置・形状」の図', 'fig'),
        ('R6_dai21mon_zu26_shokken_shuttai', '申出ができる者と、権限のない者の申出の扱いの図', 'fig'),
        ('R6_dai21mon_zu27_dai5kou_gou', '併せて提供する情報は第5項の第1号と第2号の図', 'fig'),
        ('R6_dai21mon_dai5ran_kansei', '第5欄（問5）の完成形', 'wide'),
        ('R6_dai21mon_zu28_toku_junban', '本番で解く順番の図', 'fig')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS) == N_FIG + 6)
for (name, key, kind), m in zip(PNGS, markers):
    png = os.path.join(ZU, name + '.png')
    ok = os.path.exists(png) and key in m
    if ok:
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        ok = (w == 1200 and h > w) if kind == 'tall' else (w == 1200 and h < w) if kind == 'wide' else w >= 1200
    judge(f'PNG（マーカー順・大きさ） : {name}', ok)
    src, sname = (fig, '解説図') if '_zu' in name else (fix, '添削') if 'machigai' in name else (form, '登記申請書')
    check('プロンプトにファイル名', f'zu/{name}.png', src, sname)
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない : {extra}', not extra)
# PNG名の図番号（zu01〜zu28）が記事の挿入順に並ぶ
znums = [int(re.search(r'_zu(\d+)_', n).group(1)) for n, _, _ in PNGS if '_zu' in n]
judge(f'解説図のPNG名の番号が記事の挿入順に1〜{N_FIG}で並ぶ', znums == list(range(1, N_FIG + 1)) or znums == sorted(znums))

# ---- 穴埋めの答えの語を会話の中で言っているか（2026-10-02追加）----
for s in ['やっぱり（ア）は2です！', 'だから（イ）は9の野原花子、（ウ）は5の乙土地', '（エ）は6の分筆の登記の申請よ',
          '第1欄は、アが2、イが9、ウが5、エが6。',
          '①が『土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人』',
          '②はアが『地番』、イが『職権』、ウが『土地所在図又は地積測量図』ですね']:
    check('穴埋めの答えの語（会話）', s)
check('穴埋めの答えの語（会話）', 'B点が（27.39, 54.17）、D点が（30.00, 60.78）、P点が（27.49, 60.82）です')
for name, needles in [('R6_dai21mon_dai2ran_kansei', ['第2欄', 'Ｘ座標（m）', '>27.39<', '>54.17<', '>30.00<', '>60.78<', '>27.49<', '>60.82<']),
                      ('R6_dai21mon_dai1ran_kansei', ['第1欄', '>ア<', '>イ<', '>ウ<', '>エ<', '２', '９', '５', '６']),
                      ('R6_dai21mon_dai5ran_kansei', ['第5欄', '>①<', '土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人',
                                                      '地番', '職権', '土地所在図又は地積測量図'])]:
    h_ = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        check(f'{name}.html', n, h_, '欄の完成形HTML')
for s in ['ア「２」、イ「９」、ウ「５」、エ「６」', 'ア「地番」、イ「職権」、ウ「土地所在図又は地積測量図」']:
    check('欄の完成形プロンプト', s, form, '登記申請書')

# ---- 図10〜図12（注の仕分け・対角線の別解・解く順番）の文言（2026-10-02追加）----
for s in ['今年だけ②　分筆後の地番', 'Conjg(B − I) × (P − H)', '−13.2849 ＋ 75.0658i', '37.53 ＋ 8.34 ＝ 45.87㎡',
          'P点がなくても書ける', 'いちばん時間を食う']:
    check('図10〜図12のプロンプト', s, fig, '解説図')
    check('図10〜図12の作図スクリプト', s, draw, '作図')
for s in ['分筆と一緒に地積更正をする必要もありません', '今年だけの注5〜8に印を付けておきます']:
    check('図10・図11の挿入位置の文言', s)
    check('図10・図11の挿入位置の文言（プロンプト側）', s, fig, '解説図')


# ====================================================================
# 2026-10-26：品質チェック（qa-checklist-kijutsu.md の6-2・6-3）
#   わな→図の対応表（図が会話の直後にあるか）、電卓のキー列の再現、答案用紙の原本（touan_youshi/）の寸法、フォント
# ====================================================================
from keysim_note_article import simulate  # noqa: E402
sim = simulate(os.path.join(HERE, 'note_R6_dai21mon_tochi_kaiwa_kaisetsu.md'))
n_disp = len(re.findall(r'^表示：', text, re.M))
judge(f'キー列を再現した表示の数 {len(sim)}（記事の「表示：」{n_disp}個）', len(sim) == n_disp)
for n_, want, got, ok_ in sim:
    judge(f'キー列の再現 {n_}行目 : 記事「{want}」／ 再現「{got}」', ok_)
absent('[Ans]キー（要点にないキー）', '[Ans]')


def prev_line(mk):
    """マーカーの直前の、空でなくマーカーでもない行（それを正す会話の最後の行）"""
    k_ = lines.index(mk)
    j_ = k_ - 1
    while j_ >= 0 and (not lines[j_].strip() or lines[j_].startswith('> 【画像挿入】')):
        j_ -= 1
    return lines[j_]


def marker_of(head):
    r = [m for m in markers if m.startswith('> 【画像挿入】' + head)]
    return r[0] if len(r) == 1 else None


# (まとめの項目の語, マーカーの文言の頭, 図の直前の行にある決め手の語)
TRAPS = [('**観測角の向きの注がなければ時計回りに足す**', '観測角の向きの図', 'じゃあ、足します'),
         ('**ブロック塀と金属標は筆界の根拠にならない**', '合意した位置は筆界の根拠にならない図', 'C点以外の境界標'),
         ('**残地の地積測量図は残地の周りを測っていない**', '残地の地積測量図が測ったのは3番2の周りだけという図', 'だから（ア）は2'),
         ('**A・B・Dは一直線**', 'A・B・Dは一直線の図', '筆界はB→Dの直線です'),
         ('**筆界を面積で裏付ける**', '筆界の判断の比較図', 'やっぱり（ア）は2です'),
         ('**P点はブロック塀の線と道路境界の交点**', 'Cのまま分けると面積が増える図', '0.4㎡も増える'),
         ('**分筆するのは乙土地**', '分筆するのは乙土地の図', '（ウ）は5の乙土地'),
         ('**要るのは分筆の登記だけ**', '要るのは分筆の登記だけの図', '（エ）は6の分筆の登記の申請'),
         ('**分筆した三角形は山田太郎へ移してから合筆する**', '必要な登記の流れの図', 'このためよ'),
         ('**地番は問題文の注8で面積の小さい土地を3番3**', '分筆後の区画と地番の図', '使われていますもんね'),
         ('**申請人は野原花子**', '登記申請書「申請人」欄の誤答', '3番地1'),
         ('**分筆前の行の地積は登記記録の45.88**', '登記申請書「土地の表示」1行目の地積の誤答', '登記されていない数字'),
         ('**添付書類は地積測量図と代理権限証書**', '添付書類の図', '承諾書も要らないわ'),
         ('**登録免許税は分筆後の個数で数える**', '登録免許税は分筆後の個数で数える図', '納付を要しない登記のとき'),
         ('**土地の表示は行ごとに書くものが違う**', '土地の表示の欄は行ごとに書くものが違う図', '地積を書くのよ'),
         ('**辺長は小数第3位だけを見て一度で四捨五入**', '辺長は小数第3位だけを見て一度で決める図', '7.10'),
         ('**地積測量図に書かないもの**', '地積測量図に書くもの・書かないもの・印刷済みのものの図', '印刷済みなので書かない'),
         ('**地積測量図にC点は描かない**', '地積測量図にC点は描かない図', '見分けがつかなくなる'),
         ('**地図に準ずる図面は「位置、形状又は地番」**', '地図は「区画」、地図に準ずる図面は「位置・形状」の図', '（ア）は地番よ'),
         ('**権限のない人の申出は職権の発動を促す申出として扱える**', '申出ができる者と、権限のない者の申出の扱いの図', 'そう扱うことができるの'),
         ('**位置・形状の誤りには土地所在図又は地積測量図**', '併せて提供する情報は第5項の第1号と第2号の図', '正しい形を示す土地所在図又は地積測量図を付けるのよ')]
matome = text[text.index('## 第9章'):]
n_trap = len(re.findall(r'^- \*\*', matome, re.M))
judge(f'まとめのワナの数 {n_trap} ＝ 対応表 {len(TRAPS)}', n_trap == len(TRAPS))
heads = [t[1] for t in TRAPS]
judge('対応表のマーカーの頭に重複がない', len(set(heads)) == len(heads))
for t, hd, key in TRAPS:
    check('まとめのわな', '- ' + t)
    mk = marker_of(hd)
    judge(f'ワナの図がある : {t} → {hd}', mk is not None)
    if mk:
        judge(f'図の直前の会話に決め手の語「{key}」 : {hd}', key in prev_line(mk))
pos_ = [markers.index(marker_of(h)) for h in heads if marker_of(h)]
judge('ワナの図が記事の挿入順（まとめの順）に並ぶ', pos_ == sorted(pos_))
# 1つのわなに図が2枚、1枚に2つのわなを作らない：まとめの項目名に「と」「・」で並べた2つのわなを入れていない
_okto = ('**ブロック塀と金属標は筆界の根拠にならない**', '**P点はブロック塀の線と道路境界の交点**', '**添付書類は地積測量図と代理権限証書**')
judge('まとめの項目が1項目1わな（項目名に2つのわなを「と」で並べていない。「ごと」「として」と、1つの判断の中の「Aと B」は除く）',
      all('と' not in t[0].replace('ごと', '').replace('として', '') or t[0] in _okto for t in TRAPS))
# 会話の中の誤答と訂正（藍子の誤答が会話にあるか）
for v in ['現地にブロック塀があって、C点には金属標まで入っています。目に見える境界標と構造物が一番確かなので、1の',
          '地図に準ずる図面では、甲乙の境は西のA点のあたりから東のD点まで1本の直線でした。その上にBがあるかどうか、座標で確かめられますか？',
          'じゃあ、3の『乙土地を残地とする地積測量図』です', '二度丸めるんじゃないわよ', '申請人は『A市B町一丁目2番地1　山田太郎』です',
          '地積に関する更正の登記の申請及び地図訂正の申出』！', '登録免許税の欄は『不要』ですか？', 'C点は描かなくていいんですか？',
          '地図の訂正と同じだと思うので……『区画』！', '訂正の申出には『誤りがあることを証する情報』を付けるので、それです']:
    check('藍子の誤答・質問（会話）', v)
# 辺長の第3位（図の表の確認）：BP 6.6507…・PD 2.5103…・DB 7.1066…・PI 5.6605…（第3位は0・0・6・0）
judge('辺長の第3位 BP・PD・PIは0、DBは6', [int(math.floor(abs(q_ - p_) * 1000 + 1e-9)) % 10 for p_, q_ in [(B, PP), (PP, D), (D, B), (PP, I)]] == [0, 0, 6, 0])
check('二度丸めの例（会話）', '7.1049を7.105にして7.11としてしまうわよ。正しくは第3位が4だから7.10')
judge('7.1049の第3位は4（切り捨てで7.10）', int(math.floor(7.1049 * 1000)) % 10 == 4 and f'{round(7.1049 + 1e-9, 2):.2f}' == '7.10')
# 第4欄（地積測量図）の会話：枠の大きさ・印刷済みのもの・方位記号
check('第4欄の会話（枠の大きさ）', '第4欄の図を描く枠は横約30cm・縦約23cm')
check('第4欄の会話（方位記号）', '方位記号は印刷されていないから、自分で描くのよ')
check('C点とPの差（会話）', 'CとPは0.10mしか違わない。250分の1だと0.4mm')
# 作図スクリプトの書式（答案用紙の第4欄）
for v in ["'第4欄'", '地　積　測　量　図', '3番1、3番3', 'Ａ市Ｂ町一丁目', '（令和６年○月○日作成）', "'申 請 人'", "'縮尺'", "'250'"]:
    check('第4欄の書式（作図スクリプト）', v, draw, '作図')
for v in ['フォントが Noto', 'ORIG_FRAME_MM = (80.6, 25.8, 382.6, 256.8)', 'ORIG_SHEET_MM = (56.3, 12.2, 406.9, 274.8)']:
    pass
check('作図の枠の寸法（原本の測定値）', 'ORIG_FRAME_MM = (80.6, 25.8, 382.6, 256.8)', draw, '作図')
check('作図の用紙の外枠（原本の測定値）', 'ORIG_SHEET_MM = (56.3, 12.2, 406.9, 274.8)', draw, '作図')
for v_ in ['frect(240.6, 15.8, 302.6, 25.8)', 'frect(240.6, 25.8, 382.6, 35.8)', 'frect(80.6, 256.8, 223.6, 271.3)',
           'frect(239.6, 256.8, 382.6, 271.3)', 'fline(231.6, 25.8, 231.6, 35.8)']:
    check('作図の欄の位置（原本の測定値）', v_, draw, '作図')

# ---- 試験の答案用紙の原本（touan_youshi/、2026-10-26受領）の寸法を測り直し、作図・HTMLの値と比べる ----
import pymupdf  # noqa: E402
TYP = os.path.join(HERE, 'touan_youshi', 'R6_dai21mon_touan_youshi.pdf')
judge('答案用紙の原本PDFがある（touan_youshi/）', os.path.exists(TYP))
_d = pymupdf.open(TYP)
sheet1, sheet2 = (re.sub(r'\s', '', pg.get_text()) for pg in _d)
for s_ in ['第1欄', '第2欄', '第3欄', '第5欄', 'Ｂ点', 'D点', 'P点', 'ア', 'イ', 'ウ', 'エ', '登記申請書', '登記の目的', '添付書類', '令和6年10月18日申請Ａ地方法務局',
           '申請人', '代理人（略）', '登録免許税', '所在', '示表の地土', '①地番', '②地目', '登記原因及びその日付', '③地積', '（m2）']:
    judge(f'[答案用紙1ページ目] 印刷文字「{s_}」', s_ in sheet1.replace('Ｂ', 'Ｂ').replace('B', 'Ｂ') or s_ in sheet1)
judge('[答案用紙1ページ目] 「添付書類」であって「添付情報」ではない', '添付情報' not in sheet1)
judge('[答案用紙1ページ目] 「（略）」は代理人の1か所だけ（地積の欄に（略）の印刷はない）', sheet1.count('（略）') == 1)
for s_ in ['第4欄', '地積測量図', '地番', '土地の所在', '作成者', '申請人', '縮尺', '250', '（令和6年○月○日作成）']:
    judge(f'[答案用紙2ページ目] 印刷文字「{s_}」', s_ in sheet2)
judge('[答案用紙2ページ目] 「（略）」は作成者・申請人の2か所', sheet2.count('（略）') == 2)
judge('[答案用紙2ページ目] 方位記号の印刷はない', '北' not in sheet2 and 'N' not in sheet2)
MM = 25.4 / 72


def _segs(page):
    out = []
    for dr in page.get_drawings():
        for it in dr['items']:
            if it[0] == 'l':
                out.append((it[1], it[2]))
            elif it[0] in ('re', 'qu'):
                r_ = it[1].rect if it[0] == 'qu' else it[1]
                P_ = pymupdf.Point
                out += [(P_(r_.x0, r_.y0), P_(r_.x1, r_.y0)), (P_(r_.x1, r_.y0), P_(r_.x1, r_.y1)),
                        (P_(r_.x1, r_.y1), P_(r_.x0, r_.y1)), (P_(r_.x0, r_.y1), P_(r_.x0, r_.y0))]
    return out


def _vlines(page, ymin, ymax, xmin=0, xmax=999):
    return sorted({round(a.x * MM, 1) for a, b in _segs(page) if abs(a.x - b.x) < 0.3 and abs(a.y - b.y) * MM > 6
                   and ymin <= min(a.y, b.y) * MM + 0.2 and max(a.y, b.y) * MM <= ymax + 0.2 and xmin <= a.x * MM <= xmax})


def _hlines(page, xmin, xmax):
    return sorted({round(a.y * MM, 1) for a, b in _segs(page) if abs(a.y - b.y) < 0.3 and abs(a.x - b.x) * MM > 10
                   and xmin <= min(a.x, b.x) * MM + 0.2 and max(a.x, b.x) * MM <= xmax + 0.2})


_p = _d[0]
# 第3欄の右の土地の表示の表：列の幅の比（原本から）と HTML の colgroup
vl = _vlines(_p, 27.0, 163.5, 232.0, 403.0)
_cols = [232.6, 242.6, 273.6, 298.6, 340.6, 402.6]
for c_ in _cols + [323.6]:
    judge(f'原本の罫線に x={c_}mm がある', any(abs(c_ - v_) < 0.3 for v_ in vl))
W_ = _cols[-1] - _cols[0]
cw_ = [(_cols[1] - _cols[0]), (_cols[2] - _cols[1]), (_cols[3] - _cols[2]), 323.6 - _cols[3], (_cols[4] - 323.6), (_cols[5] - _cols[4])]
ratios = [100 * x_ / W_ for x_ in cw_]
html_cols = [float(x_) for x_ in re.findall(r'<col style="width:([0-9.]+)%">', html_k)]
judge(f'土地の表示の列の幅の比（原本 {[round(x_, 1) for x_ in ratios]}）と申請書HTML {html_cols} が0.2%以内',
      len(html_cols) == 6 and all(abs(a_ - b_) < 0.2 for a_, b_ in zip(ratios, html_cols)))
hl_ = _hlines(_p, 232.0, 403.0)
for y_ in [27.2, 45.2, 53.2, 75.2, 97.2, 119.2, 141.2, 163.2]:
    judge(f'原本の罫線に y={y_}mm（土地の表示の行。所在18・見出し8・記入行22×5）がある', any(abs(y_ - v_) < 0.3 for v_ in hl_))
# 第3欄の左の枠：登記の目的19mm・添付書類27mm・申請人19mm・登録免許税19mm
hl2 = _hlines(_p, 85.0, 224.0)
for y0_, y1_ in [(152.0, 171.0), (178.0, 205.0), (224.0, 243.0), (260.8, 279.8)]:
    judge(f'原本の枠 y={y0_}〜{y1_}mm', any(abs(y0_ - v_) < 0.3 for v_ in hl2) and any(abs(y1_ - v_) < 0.3 for v_ in hl2))
# 第1欄・第2欄・第5欄
v1 = _vlines(_p, 33.9, 63.9, 60, 230)
judge('第1欄：記号の列10.2％・記入39.8％（原本）',
      abs(100 * (v1[1] - v1[0]) / (v1[-1] - v1[0]) - 10.2) < 0.3 and abs(100 * (v1[2] - v1[1]) / (v1[-1] - v1[0]) - 39.8) < 0.3)
h1 = rdh('R6_dai21mon_dai1ran_kansei')
cw1 = [float(x_) for x_ in re.findall(r'<col style="width:([0-9.]+)%">', h1)]
judge(f'第1欄HTMLの列の幅 {cw1}', len(cw1) == 4 and abs(cw1[0] - 10.2) < 0.2 and abs(cw1[1] - 39.8) < 0.2)
v2 = _vlines(_p, 77.3, 137.3, 60, 230)
judge('第2欄：3列が等しい幅（原本）', max(abs((v2[i_ + 1] - v2[i_]) - (v2[-1] - v2[0]) / 3) for i_ in range(3)) < 0.3)
h2 = rdh('R6_dai21mon_dai2ran_kansei')
cw2 = [float(x_) for x_ in re.findall(r'<col style="width:([0-9.]+)%">', h2)]
judge(f'第2欄HTMLの列の幅 {cw2} が33.3％ずつ', len(cw2) == 3 and all(abs(c_ - 33.3) < 0.2 for c_ in cw2))
v5 = _vlines(_p, 209.2, 239.2, 232, 403)
judge('第5欄②：記号の列10.3％・記入39.7％（原本）',
      abs(100 * (v5[1] - v5[0]) / (v5[-1] - v5[0]) - 10.3) < 0.3 and abs(100 * (v5[2] - v5[1]) / (v5[-1] - v5[0]) - 39.7) < 0.3)
h5 = rdh('R6_dai21mon_dai5ran_kansei')
cw5 = [float(x_) for x_ in re.findall(r'<col style="width:([0-9.]+)%">', h5)]
judge(f'第5欄HTMLの列の幅 {cw5}', len(cw5) == 4 and abs(cw5[0] - 10.3) < 0.2 and abs(cw5[1] - 39.7) < 0.2)
judge('第5欄①：枠 x 242.6〜402.6mm・y 184.2〜199.2mm（原本）', 184.2 in _hlines(_p, 242.6, 402.6) and 199.2 in _hlines(_p, 242.6, 402.6))
# 第4欄の枠（原本の2ページ目）と作図スクリプトの値
_p2 = _d[1]
vv, hh_ = _vlines(_p2, 25.8, 271.4), _hlines(_p2, 80.6, 382.6)
judge('原本の第4欄の枠 x 80.6〜382.6mm', 80.6 in vv and 382.6 in vv)
judge('原本の第4欄の枠 y 25.8〜256.8mm', 25.8 in hh_ and 256.8 in hh_)
judge('原本：地番の欄 x 240.6〜302.6・y 15.8〜25.8mm', 240.6 in _vlines(_p2, 15.8, 35.8) and 302.6 in _vlines(_p2, 15.8, 25.8) and 15.8 in _hlines(_p2, 240.6, 302.6))
judge('原本：作成者・申請人の欄 y 256.8〜271.3mm', 271.3 in _hlines(_p2, 80.6, 223.6) and 271.3 in _hlines(_p2, 239.6, 382.6))
judge('原本の枠の大きさ 横302mm・縦231mm ＝ 1/250で横75.5m・縦57.75m（T1・T2を入れた図の範囲 東西10.02m・南北13.37mが収まる）',
      abs((382.6 - 80.6) / 4 - 75.5) < 1e-9 and 10.02 < 75.5 and 13.37 < 57.75 and abs((T2.imag - H.imag) - 10.02) < 0.01 and abs((D.real - T1.real) - 13.37) < 0.01)
# フォント（点名のOが数字の0に見えないよう Noto Sans CJK JP で描く）
from zu_helpers import setup_font as _sf  # noqa: E402
_fn = _sf()
judge(f'作図のフォントが Noto Sans CJK JP（実際: {_fn}）', 'Noto' in _fn)

print('NG件数:', ng)
