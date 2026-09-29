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

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記）と一致するか ----
AGAROOT = ['（27.39, 54.17）', '（30.00, 60.78）', '（27.49, 60.82）', '2（地図に準ずる図面', '9（野原花子）', '5（乙土地）',
           '6（分筆の登記の申請）', '土地分筆登記', '地積測量図　代理権限証書', 'A市B町一丁目3番地1　野原花子',
           '金2,000円', '③45.88', '③37.53', '③3番1、3番3に分筆', '（ロ）3番3', '③8.34', '3番1から分筆',
           '：6.65', '：2.51', '：7.11', '：5.66', '：6.73', '：5.56',
           '土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人', '地番', '職権',
           '土地所在図又は地積測量図']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)
# プロース版（照合済み）とも同じ答え
for s in ['（27.39, 54.17）', '（30.00, 60.78）', '（27.49, 60.82）', '金2,000円', '③3番1、3番3に分筆', '3番1から分筆',
          '土地所在図又は地積測量図']:
    check('プロース版と共通の答え', s, prose, 'プロース版')

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（9枚）', n_fig == 9)
for i in range(1, 10):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R6_dai21mon_zu0{i}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\()'図(\d)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, 10)))
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
# 同じ話者のセリフが、間に何も挟まずに続いていないか
same = []
for i, l in enumerate(lines):
    if l.rstrip() in ('**トリ先生**', '**藍子**'):
        j = i + 2
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図9＋添削1＋完成形1＝計11か所の想定）', n_marker == 11)
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

print('NG件数:', ng)
