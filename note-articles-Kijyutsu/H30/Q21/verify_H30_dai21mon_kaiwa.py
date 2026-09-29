"""平成30年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
2026-09-29、出題当初の試験問題の本文（リポジトリの public/kijutsu/H30-tochi/q25〜q30 と、ユーザー添付の過去問集の再掲。
この年の訂正表は第22問だけ）と答案用紙（a1・a2）から作り直した版。予備校の解答例は添付がなく、照合していない
（記事の冒頭にもそう書いてある）。答えはすべて、下の計算で座標から出し直して確かめる。
実行: python3 note-articles-Kijyutsu/H30/Q21/verify_H30_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, tri_conj, chiseki, disp, intersect  # noqa: E402

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


def ab(p):
    q = p + O
    return f'（{q.real:.2f}, {q.imag:.2f}）'.replace('-', '−')


# ---- 座標（問題文の〔基準点成果表〕〔測量によって得られた座標値〕。原点を（−50720, −14880）にずらす） ----
O = P(-50720.00, -14880.00)
RAW = {'T1': (-50731.54, -14904.34), 'T2': (-50732.19, -14875.11), 'T4': (-50736.86, -14856.95),
       'A': (-50729.15, -14899.00), 'B': (-50733.63, -14859.25), 'C': (-50721.79, -14857.95),
       'E': (-50720.03, -14879.67), 'F': (-50719.93, -14888.41), 'G': (-50719.87, -14897.37),
       'H': (-50710.06, -14878.97), 'J': (-50731.33, -14879.66), 'K': (-50720.07, -14878.87)}
S = {k: r2(P(*v) - O) for k, v in RAW.items()}
for k, v in S.items():
    check(f'ずらした座標 {k}', f'- **{k}′**：' + f'（{v.real:.2f}, {v.imag:.2f}）'.replace('-', '−'))
T1, T2, T4 = S['T1'], S['T2'], S['T4']
A, B, C, E, F, G, H, J, K = (S[k] for k in 'ABCEFGHJK')

# ---- 問1 D点（T2から時計回りの放射） ----
check('arg(T1′−T2′)', to_dms(cmath.phase(T1 - T2)))
check('arg＋360°', to_dms(cmath.phase(T1 - T2) + 2 * math.pi))
Dx = radial(T2, T1, 13.22, dms(116, 50, 31))
check('D′ 表示', '表示：' + disp(Dx))
D = r2(Dx)
check('D 答え', '**▶ D点（−50720.53, −14868.88）**')
check('D 足し戻しX', f'X ＝ −50720.00 ＋ （−0.53） ＝ {(D + O).real:.2f}'.replace('-5', '−5'))
check('D 足し戻しY', f'Y ＝ −14880.00 ＋ 11.12 ＝ {(D + O).imag:.2f}'.replace('-1', '−1'))
Dw = r2(radial(T2, T1, 13.22, -dms(116, 50, 31)))
check('反時計回りの誤りのD', ab(Dw))
check('誤りのDはT2より南', f'T2より{T2.real - Dw.real:.2f}m南')
w = tri_conj(E, D, K)
check('△EDK 表示', '表示：' + disp(w))
check('△EDK 面積', f'{abs(w.imag):.4f} ÷ 2 ＝ {abs(w.imag) / 2:.4f}㎡')
check('ED', f'{abs(D - E):.2f}mくらい')
check('KのED線からの距離', f'約{abs(w.imag) / abs(D - E):.3f}m')

# ---- 問1 I点（H→Eの延長線とA→Bの交点） ----
Ix, t, num, den = intersect(H, E, A, B)
check('交点の分子 表示', '表示：' + disp(num))
check('交点の分母 表示', '表示：' + disp(den))
judge(f't＝{t:.4f}（1を超える＝延長線上）', t > 1 and f'{t:.2f}' == '2.12')
check('I′ 表示', '表示：' + disp(H + (E - H) * 848.5619 / 399.4435))
I = r2(Ix)
check('I 答え', '**▶ I点（−50731.24, −14880.46）**')
check('I 足し戻しX', f'X ＝ −50720.00 ＋ （−11.24） ＝ {(I + O).real:.2f}'.replace('-5', '−5'))
check('I 足し戻しY', f'Y ＝ −14880.00 ＋ （−0.46） ＝ {(I + O).imag:.2f}'.replace('-1', '−1'))
Iw = r2(intersect(E, E + 1, A, B)[0])
check('Eの真南の誤りのI', ab(Iw))
check('J点', ab(J))
check('誤りのIとJ', f'差が{abs(Iw - J):.2f}m')
check('誤りのIのずれ', f'正しいIより{Iw.imag - I.imag:.2f}m東')
judge('誤りのIは正しいIより東', Iw.imag > I.imag)
check('E→Hの傾き', f'北へ{(H - E).real:.2f}m進む間に東へ{(H - E).imag:.2f}m')
check('E→Hの方向角', to_dms(cmath.phase(H - E)))
s_kou = double_area_sum([A, G, F, E, I])
check('甲土地 表示', '表示：' + disp(s_kou))
check('甲土地 面積', f'{abs(s_kou.imag):.4f} ÷ 2 ＝ {area([A, G, F, E, I]):.5f}')
check('甲土地 地積', f'{chiseki(area([A, G, F, E, I])):.2f}㎡。登記記録の187.18㎡とぴったり')
a_w = chiseki(area([A, G, F, E, Iw]))
check('誤りのIの甲土地', f'{a_w:.2f}㎡')
check('誤りのIの差', f'{a_w - 187.18:.2f}㎡も違って')
judge('誤りの差は甲2の187㎡の公差1.19を超える', a_w - 187.18 > 1.19)

# ---- 問2 ----
for s in ['- **ア**：表題登記', '- **イ**：隣接する', '- **ウ**：登記された', '- **エ**：意思',
          '不動産登記法第123条第1号', '『所有者間の合意』なら通る']:
    check('問2', s)

# ---- 問3 ----
s_otsu = double_area_sum([E, K, D, C, B, J, I])
check('乙土地 表示', '表示：' + disp(s_otsu))
a_otsu = area([E, K, D, C, B, J, I])
check('乙土地 面積', f'{abs(s_otsu.imag):.4f} ÷ 2 ＝ {a_otsu:.5f}')
check('乙土地の差', f'差は{a_otsu - 253:.2f}㎡')
s_ro = double_area_sum([E, I, J, K])
check('帯 表示', '表示：' + disp(s_ro))
a_ro = area([E, I, J, K])
check('帯 面積', f'{abs(s_ro.imag):.4f} ÷ 2 ＝ {a_ro:.5f}')
check('帯 地積', f'切り捨てて{chiseki(a_ro):.2f}㎡')
s_i = double_area_sum([K, D, C, B, J])
check('残り 表示', '表示：' + disp(s_i))
a_i = area([K, D, C, B, J])
check('残り 面積', f'{abs(s_i.imag):.3f} ÷ 2 ＝ {a_i:.3f}')
check('残り 地積', f'切り捨てて{chiseki(a_i, takuchi=False)}㎡')
check('切り捨て前の合計', f'{a_i:.3f} ＋ {a_ro:.5f} ＝ {a_i + a_ro:.5f}')
check('分筆後の合計', f'合計{chiseki(a_i, takuchi=False) + chiseki(a_ro):.2f}で差は{chiseki(a_i, takuchi=False) + chiseki(a_ro) - 253:.2f}㎡')
judge('差0.60も0.03も甲2の253㎡の公差1.43の範囲内', a_otsu - 253 < 1.43)
check('誤答の雑種地の端数', f'{math.floor(a_i * 100) / 100:.2f}')
for s in ['- **登記の目的**：土地一部地目変更・分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **登録免許税**：金2,000円（分筆後の土地1個につき1,000円 × 2個）',
          '- **申請人**：A市B町三丁目13番1号　丙山次郎', '- **所在**：A市B町三丁目',
          '①11番、②雑種地、③253（登記記録の地積）、登記原因は空欄',
          '①（イ）11番1、③244、登記原因「平成30年10月1日一部地目変更　①③11番1、11番2に分筆」',
          '①（ロ）11番2、②宅地、③9.03、登記原因「11番から分筆」']:
    check('問3', s)
check('申請人の誤答', 'A市B町三丁目10番1号　山田太郎')
check('（イ）の誤答', '③11番、11番1に分筆')
check('登記の目的の誤答', '『土地分筆登記』！')
for s in ['不動産登記事務取扱手続準則第68条第3号', '不動産登記法第37条第1項', '同法第39条第2項', '不動産登記規則第35条第7号',
          '不動産登記規則第10条第4項第1号', '不動産登記事務取扱手続準則第72条第1項', '不動産登記規則第100条',
          '不動産登記事務取扱手続準則第67条第1項第4号本文', '不動産登記法第39条第1項・第37条第1項', '不動産登記令別表8の項',
          '別表5の項', '登録免許税法別表第一の一の（十三）イ', '不動産登記規則第78条', '不動産登記規則第10条第2項第1号']:
    check('条文', s)

# ---- 問4 ----
SIDES = {'EK': (E, K), 'KD': (K, D), 'DC': (D, C), 'CB': (C, B), 'BJ': (B, J), 'JI': (J, I), 'IE': (I, E),
         'KJ（分筆線）': (K, J)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n[:2]}', f'{n[:2]} {v}', fig, '解説図')
check('JIの四捨五入', f'JIは{math.floor(abs(J - I) * 1e4) / 1e4:.4f}…')
xs = [p.real for p in (E, K, D, C, B, J, I)]
ys = [p.imag for p in (E, K, D, C, B, J, I)]
check('東西の長さ', f'東西が約{max(ys) - min(ys):.1f}mで約{round((max(ys) - min(ys)) * 4)}mm')
check('南北の長さ', f'南北が約{max(xs) - min(xs):.1f}mで約{round((max(xs) - min(xs)) * 4)}mm')
check('T4まで', f'東西約{round((T4.imag - min(ys)) * 4)}mm、南北約{round((max(xs) - T4.real) * 4)}mm')
for s in ['地番欄は『11番1、11番2』', '『A市B町三丁目』', '（イ）11－1と（ロ）11－2', 'B・D・J・Kはコンクリート杭、C・E・Iは金属標',
          '基準点T2・T4の位置と点名（注6）', 'E・Iの西は10－1', 'E・K・D・Cの北は10－3', 'Eの北西の角は10－2', '1m ＝ 4mm']:
    check('問4', s)

# ---- 間接の照合：作り直す前の版（2026-09-29、アガルートの解答例と照合済み）の照合スクリプトに転記されていた答え ----
# 今回は解答例の添付がないので、その転記と一致するかを「間接の照合」として確かめる（記事の冒頭には照合済みと書かない）。
PREV_AGAROOT = ['−50720.53', '−14868.88', '−50731.24', '−14880.46', '表題登記', '隣接する', '登記された', '- **エ**：意思',
                '土地一部地目変更・分筆登記', '地積測量図　代理権限証書', '金2,000円', '13番1号　丙山次郎', 'A市B町三丁目',
                '③253', '（イ）11番1', '③244', '平成30年10月1日一部地目変更', '①③11番1、11番2に分筆', '（ロ）11番2', '②宅地',
                '③9.03', '11番から分筆', '：0.80', '：10.00', '：11.00', '：11.91', '：20.54', '：0.81', '：11.24', '：11.29',
                '11番1、11番2']
for s_ in PREV_AGAROOT:
    check('旧版に転記されたアガルートの解答例と一致（間接）', s_)
absent('旧版の実測面積の誤記', '253.61')

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
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\()'図(\d)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, 10)))
for s in ['271°16′26.04″', '−88°43′33.96″', '116°50′31″', '4°00′58.26″', '848.5619 ÷ 399.4435', '2.1243…',
          '（−50744.12, −14869.40）', '（−50731.33, −14879.67）', '0.79', '187.18645', '191.65', '4.47',
          '253.60035', '1.43', '4.13', '253.03', '244.561', '9.03935', '0.8050…', '約90mm', '約54mm', '約94mm', '約67mm',
          '−50720.00, −14880.00']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['暗算でずらせますね', 'K点はちゃんとED線の上です！', 'わなにはまるところでした……', 'これが鉄則よ',
          'その1月以内ね', 'こちらも範囲内です', '（イ）の行の原因には①も付けるのよ', '少し離して書きなさい']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成30年10月19日　申請　Ａ地方法務局', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書', '金2,000円',
          'Ａ市Ｂ町三丁目13番１号　丙山次郎', 'Ａ市Ｂ町三丁目', '①「11番」、②「雑種地」、③「253」',
          '①「（イ）11番１」、②空欄、③「244」', '「平成30年10月１日一部地目変更」「①③11番１、11番２に分筆」',
          '①「（ロ）11番２」、②「宅地」、③「9｜03」、登記原因「11番から分筆」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['Ａ市Ｂ町三丁目10番１号　山田太郎', '③「244｜56」', '「③11番、11番１に分筆」', '①「（ロ）11番１」',
          '「Ａ市Ｂ町三丁目13番１号　丙山次郎」', '「①③11番１、11番２に分筆」',
          '（ロ）は『（ロ）11番2、宅地、9.03、11番から分筆』です']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '（ロ）は『（ロ）11番2、宅地、9.03、11番から分筆』です」')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H30_dai21mon_toukishinseisho_kansei', 'H30_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w_, h_ = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w_}×{h_}px）', h_ > w_ and w_ == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H30_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H30_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成30年10月19日　申請　Ａ地方法務局', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書', '金2,000円',
          'Ａ市Ｂ町三丁目13番１号　丙山次郎', 'Ａ市Ｂ町三丁目', '11番', '雑種地', '>253<', '（イ）11番１', '>244<',
          '平成30年10月１日一部地目変更', '①③11番１、11番２に分筆', '（ロ）11番２', '宅地', '>9<', '>03<', '11番から分筆',
          '（略）', '平成30年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
for s in ['①誤答', '②添削（赤ペン）', '③正解', 'Ａ市Ｂ町三丁目10番１号　山田太郎', 'Ａ市Ｂ町三丁目13番１号　丙山次郎',
          '>56<', '③11番、11番１に分筆', '①③11番１、11番２に分筆', '11番２',
          '申請人は所有権の登記名義人。移転の登記の前は丙山次郎！', '支号のない11番の分筆は11番１・11番２。雑種地は1㎡未満を切り捨て',
          '平成30年度 第21問｜申請人は登記名義人、支号のない本番の分筆は11番１・11番２']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
    if s.startswith(('申請人は', '支号のない', '平成30年度 第21問')):
        check('添削の画像とプロンプトの文言', s, fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', 'ブロックへい', '照合済みです', '≒']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', 'ブロック塀')
check('照合していないことの明記', '予備校の解答例との照合はしていません')

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
for bad in ['平成27年度', '水路になっても', '塀も残地']:
    absent('見出し画像に別の年度の文言', bad, thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
for s in ['- **X**：T1′（D点を求めた後は、H′に使い回す）', '- **Y**：T2′（D点を求めた後は、I′に使い回す）',
          '変数XはH′に使い回します', '変数YはI′に使い回すわ']:
    check('変数の割り当て', s)

print('NG件数:', ng)
