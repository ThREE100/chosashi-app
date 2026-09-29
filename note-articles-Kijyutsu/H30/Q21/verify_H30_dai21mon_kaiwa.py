"""平成30年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と一致することも確認する。
問2（エ）だけは解答例の「意思」ではなく「合意」を採用している（記事では「意思」でも同じ趣旨と説明）。
実行: python3 note-articles-Kijyutsu/H30/Q21/verify_H30_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, tri_conj, chiseki, disp, fmt_num, intersect  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H30_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H30_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H30_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H30_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H30_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H30_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


def m(v):
    """記事の座標の書き方（マイナスは全角の「−」）。"""
    return f'{v:.2f}'.replace('-', '−')


def pt(z):
    return f'（{m(z.real)}, {m(z.imag)}）'


# ---- 座標（問題文の〔基準点成果表〕と〔測量によって得られた座標値〕） ----
T1, T2 = P(-50731.54, -14904.34), P(-50732.19, -14875.11)
T3, T4 = P(-50710.35, -14900.56), P(-50736.86, -14856.95)
A, B, C = P(-50729.15, -14899.00), P(-50733.63, -14859.25), P(-50721.79, -14857.95)
E, F, G = P(-50720.03, -14879.67), P(-50719.93, -14888.41), P(-50719.87, -14897.37)
H, J, K = P(-50710.06, -14878.97), P(-50731.33, -14879.66), P(-50720.07, -14878.87)
for n, z in [('T1', T1), ('T2', T2), ('A', A), ('B', B), ('C', C), ('E', E), ('F', F), ('H', H), ('J', J), ('K', K)]:
    check(f'{n}の入力', f'0 [−] {-z.real:.2f} [−] {-z.imag:.2f} [i]')
check('Gの入力（式の中で直接）', '0 [−] 50719.87 [−] 14897.37 [i]')

# ---- 問1 D点（放射。観測角は時計回り＝足す） ----
check('arg(T1−T2)', to_dms(cmath.phase(T1 - T2)))
check('arg(T1−T2)＋360°', to_dms(cmath.phase(T1 - T2) + 2 * math.pi))
check('方向角＋観測角−360°', to_dms(cmath.phase(T1 - T2) + dms(116, 50, 31)))
Dx = radial(T2, T1, 13.22, dms(116, 50, 31))
check('D 表示', '表示：' + disp(Dx))
D = r2(Dx)
check('D 答え', f'**▶ D点{pt(D)}**')
check('D−T2 表示', '表示：' + disp(D - T2))
Dw = r2(radial(T2, T1, 13.22, -dms(116, 50, 31)))
check('反時計回りの誤りのD', pt(Dw))
check('誤りのDはT2より南', f'T2より{abs(Dw.real - T2.real):.2f}mも南')
judge('反時計回りのDはT2の南（道路の向こう）、正しいDはT2の北東', Dw.real < T2.real < D.real and D.imag > T2.imag)
ekd = tri_conj(E, K, D)
check('△EKD 表示', '表示：' + disp(ekd))
check('△EKD 面積', f'{abs(ekd.imag) / 2:.4f}㎡')
judge('KはDEから3mm程度', round(abs(ekd.imag) / abs(D - E), 3) == 0.003)

# ---- 問1 I点（交点） ----
check('E−H 表示', '表示：' + disp(E - H))
Ix, t, num, den = intersect(H, E, A, B)
check('交点の分子 表示', '表示：' + disp(num))
check('交点の分母 表示', '表示：' + disp(den))
check('t 表示', '表示：' + fmt_num(num.imag / den.imag))
judge('t＞1（延長線上）', t > 1)
check('I 表示', '表示：' + disp(H + (E - H) * 848.5619 / 399.4435))
I = r2(Ix)
check('I 答え', f'**▶ I点{pt(I)}**')
Iw = r2(A + (B - A) * ((E.imag - A.imag) / (B.imag - A.imag)))
check('真南に下ろした誤りのI', pt(Iw))
check('J点の座標', pt(J))
check('誤りのIとJの差', f'たった{abs(Iw - J):.2f}m')
check('誤りのIと正しいIの差', f'正しいIとは{abs(Iw - I):.2f}m')
s_kou = (I - A) * (E - A).conjugate() + (E - A) * (F - A).conjugate() + (F - A) * (G - A).conjugate()
check('甲土地 表示', '表示：' + disp(s_kou))
check('甲土地 面積', f'{abs(s_kou.imag) / 2:.5f}')
judge('甲土地の地積 187.18＝登記記録', chiseki(area([A, I, E, F, G])) == 187.18)
kw = chiseki(area([A, Iw, E, F, G]))
check('誤りのIの甲土地', f'甲土地は{kw:.2f}㎡')
check('誤りのIの甲土地の差', f'{kw - 187.18:.2f}㎡も大きく')
check('187㎡の公差（問題文の表）', '187㎡の公差1.19㎡（甲2）')
for s in ['- **D点**：X座標 −50720.53、Y座標 −14868.88', '- **I点**：X座標 −50731.24、Y座標 −14880.46']:
    check('問1', s)

# ---- 問2 ----
for s in ['- **ア**：表題登記', '- **イ**：隣接する', '- **ウ**：登記された', '- **エ**：合意', '不動産登記法第123条第1号',
          '『意思』と書いても']:
    check('問2', s)

# ---- 問3 必要な登記 ----
for s in ['土地一部地目変更・分筆登記', '不動産登記法第37条第1項', '不動産登記規則第35条第7号', '不動産登記法第39条第2項',
          '準則第68条第3号', '不動産登記法第51条第1項', '平成30年10月1日']:
    check('問3 判断', s)
# ---- 問3 面積・公差 ----
s_otsu = (B - I) * (C - I).conjugate() + (C - I) * (D - I).conjugate() + (D - I) * (E - I).conjugate()
check('乙土地 表示', '表示：' + disp(s_otsu))
a_otsu = abs(s_otsu.imag) / 2
check('乙土地 面積', f'{a_otsu:.4f}㎡')
check('乙土地の差', f'差の{a_otsu - 253:.4f}㎡')
check('公差（甲2・253㎡）', '1.43㎡')
check('乙1の誤り', '乙1の4.13㎡')
check('精度区分の条文', '不動産登記規則第10条第4項第1号')
check('地積更正の条文', '準則第72条第1項')
s_i = (B - J) * (C - J).conjugate() + (C - J) * (D - J).conjugate() + (D - J) * (K - J).conjugate()
s_ro = (J - I) * (K - I).conjugate() + (K - I) * (E - I).conjugate()
check('（イ） 表示', '表示：' + disp(s_i))
check('（ロ） 表示', '表示：' + disp(s_ro))
a_i, a_ro = abs(s_i.imag) / 2, abs(s_ro.imag) / 2
check('（イ） 面積', f'{a_i:.3f}')
check('（イ）の誤答（宅地の切り捨て）', f'{chiseki(a_i):.2f}㎡')
check('（イ） 地積', f'（イ）は{chiseki(a_i, takuchi=False)}㎡')
check('（ロ） 面積', f'{a_ro:.5f}')
check('（ロ） 地積', f'{chiseki(a_ro):.2f}㎡')
check('分筆後の合計', f'244 ＋ 9.03 ＝ {244 + 9.03:.2f}㎡')
judge('分筆前後の差 0.03・実測の差 0.6177 とも 1.43 以内', abs(253.03 - 253) < 1.43 and a_otsu - 253 < 1.43)
check('地積の条文', '不動産登記規則第100条')
# ---- 問3 申請書 ----
for s in ['- **登記の目的**：土地一部地目変更・分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **登録免許税**：金2,000円', '- **申請人**：A市B町三丁目13番1号　丙山次郎', '- **所在**：A市B町三丁目',
          '①11番、②雑種地、③253（登記記録の地積）', '①（イ）11番1、②空欄、③244、登記原因「平成30年10月1日一部地目変更」「①③11番1、11番2に分筆」',
          '①（ロ）11番2、②宅地、③9.03、登記原因「11番から分筆」', '準則第74条第1項', '準則第74条第2項',
          '準則第67条第1項第4号', '不動産登記令別表8の項', '登録免許税法別表第一の一の（十三）イ']:
    check('問3', s)
check('登記の目的の誤答', '登記の目的は『土地分筆登記』')
check('（イ）（ロ）の誤答', '（ロ）は『（ロ）11番2、雑種地、9.03、11番から分筆』')
check('地番の誤答', '元の土地はそのまま11番で地番欄は空欄')
check('登録免許税の誤答', '1,000円？')

# ---- 問4 辺長 ----
SIDES = {'EK': (E, K), 'KD': (K, D), 'DC': (D, C), 'CB': (C, B), 'BJ': (B, J), 'JI': (J, I), 'IE': (I, E),
         'KJ（分筆線）': (K, J)}
for n, (p, q) in SIDES.items():
    check(f'辺長{n}', f'- **{n}**：{round(abs(p - q) + 1e-9, 2):.2f}')
    check(f'辺長{n} 表示', '表示：' + fmt_num(abs(p - q)))
    check(f'図の辺長{n}', f'{round(abs(p - q) + 1e-9, 2):.2f}', fig, '解説図')
check('JIの四捨五入', 'JIは0.8050…よ')
judge('JIは0.805を超える（0.81）', abs(J - I) > 0.805)
check('答案用紙の大きさ（横）', f'横約{round((C.imag - I.imag) * 4):d}mm')
check('答案用紙の大きさ（縦）', f'縦約{round((E.real - B.real) * 4):d}mm')
check('乙土地の東西', f'東西が約{C.imag - I.imag:.1f}m')
check('乙土地の南北', f'南北が約{E.real - B.real:.1f}m')
for s in ['B・D・J・Kはコンクリート杭、C・E・Iは金属標', '基準点T2・T4の位置と点名（注6）', '地番欄「11番1、11番2」']:
    check('問4', s)

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記）と一致するか ----
AGAROOT = ['−50720.53', '−14868.88', '−50731.24', '−14880.46', '表題登記', '隣接する', '登記された',
           '土地一部地目変更・分筆登記', '地積測量図　代理権限証書', '金2,000円', '13番1号　丙山次郎', 'A市B町三丁目',
           '③253', '（イ）11番1', '③244', '平成30年10月1日一部地目変更', '①③11番1、11番2に分筆', '（ロ）11番2', '②宅地',
           '③9.03', '11番から分筆', '：0.80', '：10.00', '：11.00', '：11.91', '：20.54', '：0.81', '：11.24', '：11.29',
           '11番1、11番2']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)
check('アガルートの解答例（エ）の「意思」にも触れる', '『意思』')

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（9枚）', n_fig == 9)
for i in range(1, 10):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H30_dai21mon_zu0{i}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(x) for x in re.findall(r"(?:new_figure\(|frame\(|suptitle\()'図(\d)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, 10)))
for s in ['271°16′26.04″', '−88°43′33.96″', '116°50′31″', '28°06′57.04″', '13.22', '11.93m', '0.0158㎡', '2.1243…',
          '−9.97 − 0.70i', '187.18645', '191.65㎡', '4.47㎡', '1.19㎡', '253.6177', '253.03', '0.6177', '244.561',
          '9.03935', '±1.43㎡', '±4.13㎡', '横約90mm・縦約54mm', '0.8050…', '848.5619 ÷ 399.4435']:
    check('解説図プロンプトの数値', s, fig, '解説図')
for s in ['271°16′26.04″', '−88°43′33.96″', '116°50′31″', '28°06′57.04″', '13.22', '11.93m', '0.0158㎡', '2.1243…',
          '−9.97 − 0.70i', '187.18645', '191.65㎡', '4.47㎡', '1.19㎡', '253.6177', '253.03', '0.6177', '244.561',
          '9.03935', '±1.43㎡', '±4.13㎡', '横約90mm・縦約54mm', '0.8050…']:
    check('作図スクリプトの数値', s, draw, '作図')
for z, n in [(D, 'D'), (I, 'I'), (Dw, '誤りのD'), (Iw, '誤りのI'), (J, 'J')]:
    check(f'解説図プロンプトの座標 {n}', f'({m(z.real)}, {m(z.imag)})', fig, '解説図')
for s in ['北を上にして座標どおりに描き直すと、こうなるわ', 'KはDEの直線から3mmくらいしか離れていないので、Dは合っています！',
          'T2ももう使わないから、変数YにI点を記憶しなさい', '正しいIなら甲土地の面積が合う。これがIの裏付けよ',
          'だから、筆界はそのままにして、売る部分を分筆で切り分けるんですね', '表示に関する登記の申請人は丙山次郎よ',
          '分筆前の253㎡との差は0.03㎡で、これも1.43㎡の範囲です', '元の土地の地番まで変わるんですね。だから（イ）の行にも地番を書く',
          'D点で北の辺が折れているのよ']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成30年10月19日　申請　Ａ地方法務局', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書',
          'Ａ市Ｂ町三丁目13番１号　丙山次郎', '金2,000円', '「Ａ市Ｂ町三丁目」', '①地番：「11番」', '③地積：「253｜」',
          '①地番：「（イ）11番１」', '③地積：「244｜」', '「平成30年10月１日一部地目変更」「①③11番１、11番２に分筆」',
          '①地番：「（ロ）11番２」', '②地目：「宅地」', '③地積：「9｜03」', '「11番から分筆」',
          '登記の目的 → 添付書類 → 登録免許税 → 申請人 → 代理人 → 申請の日付と提出先 → 土地の表示']:
    check('登記申請書', s, form, '登記申請書')
for s in ['登記の目的：「土地分筆登記」', '登記原因「③11番１、11番２に分筆」', '②「雑種地」、③「9｜03」',
          '「平成30年10月１日一部地目変更」「①③11番１、11番２に分筆」', '②「宅地」、③「9｜03」',
          '売った細い部分は10月1日に宅地へ。一部地目変更も一緒に！', '本番の11番は地番も変わるので①③。（ロ）は宅地',
          '（イ）の行は『平成30年10月1日一部地目変更』と『①③11番1、11番2に分筆』の2つ。（ロ）は宅地です']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '（イ）の行は『平成30年10月1日一部地目変更』と『①③11番1、11番2に分筆』の2つ。（ロ）は宅地です')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H30_dai21mon_toukishinseisho_kansei', 'H30_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H30_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H30_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成30年10月19日　申請　Ａ地方法務局', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書',
          'Ａ市Ｂ町三丁目13番１号　丙山次郎', '金2,000円', 'Ａ市Ｂ町三丁目', '>11番<', '>雑種地<', '>253<', '（イ）11番１', '>244<',
          '平成30年10月１日一部地目変更<br>①③11番１、11番２に分筆', '（ロ）11番２', '>宅地<', '>9<', '>03<', '11番から分筆', '（略）',
          '平成30年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
judge('完成形の画像：項目の順序（目的→添付→登録免許税→申請人→代理人→申請日→土地の表示）',
      [html_k.index(s) for s in ['登記の目的', '添　付　書　類', '登録免許税', '申　　請　　人', '代　　理　　人', '平成30年10月19日',
                                 '土地の表示']] == sorted(html_k.index(s) for s in ['登記の目的', '添　付　書　類', '登録免許税',
                                                                                   '申　　請　　人', '代　　理　　人',
                                                                                   '平成30年10月19日', '土地の表示']))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '土地分筆登記', '③11番１、11番２に分筆', '>雑種地</span><br><span class="red">宅地<',
          '売った細い部分は10月1日に宅地へ。一部地目変更も一緒に！', '本番の11番は地番も変わるので①③。（ロ）は宅地',
          '平成30年度 第21問｜細い部分は宅地に変わった。土地一部地目変更・分筆登記、本番の分筆は①③']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
check('添削の画像とプロンプトのキャプション', '平成30年度 第21問｜細い部分は宅地に変わった。土地一部地目変更・分筆登記、本番の分筆は①③', fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', 'へい（', 'ブロックべい']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', 'ブロック塀')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
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
prefix = '# 【土地家屋調査士受験生向け】平成30年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成30年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
absent('見出し画像に他年度の文言', '令和6年度', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
# 電卓操作の見出しに書いた変数の対応と、第1章の割り当て表の整合（変数が A〜F、X、Y だけか）
used = set(re.findall(r'\[ALPHA\] \[([A-Z])\]', text))
judge(f'電卓の変数は A〜F、X、Y だけ（{sorted(used)}）', used <= set('ABCDEFXY'))

print('NG件数:', ng)
