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
check('DBの四捨五入', f'DBは{abs(B - D):.4f}だから7.11')
check('PIの四捨五入', f'PIは{math.floor(abs(PP - I) * 1e4) / 1e4:.4f}')
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
check('登録免許税の「不要」の指示', '『納付を要しない場合は不要と記載』とありますが、この申請は課税されるので『不要』とは書きません')
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
N_FIG = 12
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（{N_FIG}枚）', n_fig == N_FIG)
for i in range(1, N_FIG + 1):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R6_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, N_FIG + 1)))
for s in ['（27.39, 54.17）', '（30.00, 60.78）', '（27.49, 60.82）', '193°46′25.18″', '−166°13′34.82″', '78°58′08″',
          '118°24′27″', '104.76㎡', '37.81㎡', '96.29㎡', '45.86㎡', '0.0064㎡', '46.28㎡', '8.34㎡', '37.53㎡',
          '45.88065', '67.6152 ÷ 68.6625', '7.1066', '横約27mm・縦約33mm']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s.replace('（', '（').replace('㎡', ''), draw, '作図')
# 画像挿入の位置の文言が記事にあるか
for s in ['ここがこの問題のすべての出発点よ', '5.56はX座標の差そのものですね', '道路境界確認図とも合いました！', 'やっぱり（ア）は2です！',
          'BCとDJがほぼ直角に交わっているからよ', '二人がその後の手続にも協力すると合意しているのは、このためよ',
          '3番2は昭和50年の分筆でもう使われていますもんね', 'BDは地図に準ずる図面のA→Dの直線の一部よ']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['令和６年10月18日　申請　Ａ地方法務局', '土地分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｂ町一丁目３番地１　野原花子',
          '金2,000円', 'Ａ市Ｂ町一丁目', '③「45｜88」', '③「37｜53」', '登記原因「③3番１、3番３に分筆」',
          '①「（ロ）3番３」', '③「8｜34」', '登記原因「3番１から分筆」']:
    check('登記申請書（プロース版と共用）', s, form, '登記申請書')
for s in ['Ａ市Ｂ町一丁目２番地１　山田太郎', 'Ａ市Ｂ町一丁目３番地１　野原花子', '③「45｜86」', '③「45｜88」',
          '申請人も、手続をする土地の所有者です', '令和６年10月18日　申請　Ａ地方法務局']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '申請人も、手続をする土地の所有者です')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
import struct  # noqa: E402
for name in ['R6_dai21mon_toukishinseisho_kansei', 'R6_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    ok = os.path.exists(png)
    if ok:
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'R6_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'R6_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['令和６年10月18日　申請　Ａ地方法務局', '土地分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｂ町一丁目３番地１　野原花子',
          '金2,000円', 'Ａ市Ｂ町一丁目', '3番１', '（ロ）3番３', '③3番１、3番３に分筆', '3番１から分筆', '>45<', '>88<', '>37<',
          '>53<', '>8<', '>34<', '（略）', '令和6年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
for s in ['①誤答', '②添削（赤ペン）', '③正解', 'Ａ市Ｂ町一丁目２番地１　山田太郎', 'Ａ市Ｂ町一丁目３番地１　野原花子', '>86<',
          '>88<', '分筆するのは乙土地。申請人は分筆の時点の所有者！', '分筆前の行は登記記録の地積。計算値は書かない',
          '令和6年度 第21問｜申請人は分筆する土地の所有者、分筆前の地積は登記記録どおり']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
    if s.startswith('分筆') or s.startswith('令和6年度 第21問'):
        check('添削の画像とプロンプトの文言', s, fix, '添削')

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
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋添削1＋完成形1＋第1欄・第2欄・第5欄3＝計{N_FIG + 5}か所の想定）',
      n_marker == N_FIG + 5)
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

# ---- 2026-10-02の照らし直し：画像挿入マーカーと zu/ のPNGが記事の順に対応しているか ----
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R6_dai21mon_zu10_chuu_shiwake', '問題文の注の仕分けの図', 'fig'),
        ('R6_dai21mon_zu01_zentaizu', '全体図', 'fig'),
        ('R6_dai21mon_zu02_B_housha', 'B点を求める図', 'fig'),
        ('R6_dai21mon_zu03_D_housha', 'D点を求める図', 'fig'),
        ('R6_dai21mon_zu04_hikkai_handan', '筆界の判断の比較図', 'fig'),
        ('R6_dai21mon_zu05_P_kousa', 'P点の求め方の図', 'fig'),
        ('R6_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R6_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R6_dai21mon_zu06_hitsuyou_touki', '必要な登記の流れの図', 'fig'),
        ('R6_dai21mon_zu11_taikakusen', '対角線で出す別解の図', 'fig'),
        ('R6_dai21mon_zu07_bunpitsu_chiban', '分筆後の区画と地番の図', 'fig'),
        ('R6_dai21mon_toukishinseisho_machigai', '誤答→添削→正解の3コマ', 'tall'),
        ('R6_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R6_dai21mon_zu08_chiseki_sokuryouzu', '地積測量図（3番1・3番3）の完成見本', 'fig'),
        ('R6_dai21mon_zu09_chizu_teisei', '地図に準ずる図面の訂正の申出の整理図', 'fig'),
        ('R6_dai21mon_dai5ran_kansei', '第5欄（問5）の完成形', 'wide'),
        ('R6_dai21mon_zu12_toku_junban', '本番で解く順番の図', 'fig')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
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

print('NG件数:', ng)
