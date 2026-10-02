"""平成30年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
2026-09-29、出題当初の試験問題の本文（リポジトリの public/kijutsu/H30-tochi/q25〜q30 と、ユーザー添付の過去問集の再掲。
この年の訂正表は第22問だけ）と答案用紙（a1・a2）から作り直した版。同日、別のセッションに添付されていたアガルートの過去問集
（全22ページ。解答例は第1欄・第2欄・第3欄・第4欄）と、欄ごと・空欄ごとに直接照合した（下の AGAROOT）。
答えはすべて、下の計算で座標から出し直して確かめる。
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
          '基準点T2・T4の位置と点名（問題文の注6）', '単位の表示「（単位：m）」', '境界標の種類の凡例', 'E・Iの西は10－1', 'E・K・D・Cの北は10－3', 'Eの北西の角は10－2', '1m ＝ 4mm']:
    check('問4', s)

# ---- アガルートの解答例との直接の照合（2026-09-29、過去問集の解答例ページ〈第1欄〜第4欄〉から欄ごと・空欄ごとに転記） ----
AGAROOT = {
    '第1欄 D点': '**▶ D点（−50720.53, −14868.88）**',
    '第1欄 I点': '**▶ I点（−50731.24, −14880.46）**',
    '第2欄 ア': '- **ア**：表題登記', '第2欄 イ': '- **イ**：隣接する', '第2欄 ウ': '- **ウ**：登記された', '第2欄 エ': '- **エ**：意思',
    '第3欄 登記の目的': '- **登記の目的**：土地一部地目変更・分筆登記',
    '第3欄 添付書類': '- **添付書類**：地積測量図　代理権限証書',
    '第3欄 登録免許税': '- **登録免許税**：金2,000円',
    '第3欄 申請人': '- **申請人**：A市B町三丁目13番1号　丙山次郎',
    '第3欄 所在': '- **所在**：A市B町三丁目',
    '第3欄 1行目': '- **1行目（分筆前）**：①11番、②雑種地、③253',
    '第3欄 （イ）の行': '- **2行目（イ）**：①（イ）11番1、③244、登記原因「平成30年10月1日一部地目変更　①③11番1、11番2に分筆」',
    '第3欄 （ロ）の行': '- **3行目（ロ）**：①（ロ）11番2、②宅地、③9.03、登記原因「11番から分筆」',
    '第4欄 地番・所在': '地番欄は『11番1、11番2』。土地の所在は『A市B町三丁目』',
    '第4欄 地番の符号': '（イ）11－1と（ロ）11－2',
    '第4欄 EK': '- **EK**：0.80', '第4欄 KD': '- **KD**：10.00', '第4欄 DC': '- **DC**：11.00', '第4欄 CB': '- **CB**：11.91',
    '第4欄 BJ': '- **BJ**：20.54', '第4欄 JI': '- **JI**：0.81', '第4欄 IE': '- **IE**：11.24', '第4欄 KJ': '- **KJ（分筆線）**：11.29',
    '第4欄 境界標': 'B・D・J・Kはコンクリート杭、C・E・Iは金属標',
    '第4欄 隣接地': 'E・Iの西は10－1、E・K・D・Cの北は10－3、Eの北西の角は10－2',
    '第4欄 基準点': '基準点T2・T4の位置と点名',
    '解説の求積（イ）': '244.561', '解説の求積（ロ）': '9.03935', '解説の合計': '253.60035', '解説の公差': '1.43㎡',
}
for k_, s_ in AGAROOT.items():
    check(f'アガルートの解答例と一致（{k_}）', s_)
check('照合済みの一文', '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')
check('解説と見比べて足した別解（対角線2本）', '帯の倍面積 ＝ Conjg(E′ − J′) × (K′ − I′)')
check('対角線の式の表示', '表示：' + disp((E - J).conjugate() * (K - I)))
judge('対角線の式のiの係数が4点の式と同じ', abs(((E - J).conjugate() * (K - I)).imag - 18.0787) < 1e-9)
for s_ in ['いちばん時間を食うのは、乙土地の7点と、帯と残りの駐車場の面積', 'D点とI点がなくても書ける欄はどこですか？',
           '①問2を埋める、②申請書の計算の要らない欄を書く、③原点をずらす、④D点、⑤I点と甲土地の面積の裏付け、⑥乙土地・帯・残りの面積と公差の判定、⑦地積測量図の辺長と作図',
           '不動産登記法第51条第1項', '調査図素図の注で、K点は', '調査図素図の注に『I点は', '座標は問題文の注3で', '辺の長さは問題文の注4']:
    check('最新の依頼文との照らし合わせで足した内容', s_)
absent('旧版の実測面積の誤記', '253.61')
for bad in ['座標は注3', '検算よ。注で', '次はI点。注に', '（注5）', '（注6）']:
    absent('どちらの注か書き分けていない', bad)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（11枚）', n_fig == 11)
for i in range(1, 12):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H30_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から11まで（{sorted(nums)}）', sorted(nums) == list(range(1, 12)))
for s in ['271°16′26.04″', '−88°43′33.96″', '116°50′31″', '4°00′58.26″', '848.5619 ÷ 399.4435', '2.1243…',
          '（−50744.12, −14869.40）', '（−50731.33, −14879.67）', '0.79', '187.18645', '191.65', '4.47',
          '253.60035', '1.43', '4.13', '253.03', '244.561', '9.03935', '0.8050…', '約90mm', '約54mm', '約94mm', '約67mm',
          '−50720.00, −14880.00']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['暗算でずらせますね', 'K点はちゃんとED線の上です！', 'わなにはまるところでした……', 'これが鉄則よ',
          '乙土地の申請書には入らないわ', 'こちらも範囲内です', '（イ）の行の原因には①も付けるのよ', '少し離して書きなさい',
          '対角線が交わる四角形なら、この式1本で済むんですね', '問2は先に取れています']:
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
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', 'ブロックへい', '≒']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', 'ブロック塀')
absent('照合していない旨の古い一文', '予備校の解答例との照合はしていません')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
same = []
# 同じ話者のセリフが、空行・画像挿入マーカー・セリフの続きの段落だけをはさんで続いていないか（2026-10-02、マーカーを読み飛ばす形に直した）。
# 箇条書き・計算（式・電卓操作・表示・答えの行・コードブロック）・区切り線・見出しをはさむものは数えない。
spk_ = [(k_, l_.rstrip()) for k_, l_ in enumerate(lines) if l_.rstrip() in ('**トリ先生**', '**藍子**')]
for (i_, a_), (j_, b_) in zip(spk_, spk_[1:]):
    if a_ != b_:
        continue
    mid_ = [l_ for l_ in lines[i_ + 2:j_] if l_.strip()]
    if not any(l_.startswith(('- ', '```', '表示：', '式（', '電卓操作', '**▶', '---', '#')) or re.match(r'^\d+\. ', l_)
               for l_ in mid_):
        same.append(j_ + 1)
judge(f'同じ話者のセリフの連続: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図11＋第1欄・第2欄の完成形2＋添削1＋申請書の完成形1）', n_marker == 15)
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

PNGS = [('H30_dai21mon_zu01_zentaizu', '全体図', 'fig'),
        ('H30_dai21mon_zu02_D_housha', 'D点を求める図', 'fig'),
        ('H30_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('H30_dai21mon_zu03_I_kouten', 'I点の求め方の図', 'fig'),
        ('H30_dai21mon_zu04_kou_menseki', '甲土地の面積による裏付けの図', 'fig'),
        ('H30_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('H30_dai21mon_zu05_hikkai_teigi', '筆界の定義の整理図', 'fig'),
        ('H30_dai21mon_zu06_hitsuyou_touki', '必要な登記の図', 'fig'),
        ('H30_dai21mon_zu07_kousa', '公差の判定図', 'fig'),
        ('H30_dai21mon_zu08_obi_taikakusen', '対角線2本で出す別解の図', 'fig'),
        ('H30_dai21mon_zu09_bunpitsu_chiban', '分筆後の区画と地番の図', 'fig'),
        ('H30_dai21mon_toukishinseisho_machigai', '誤答→添削→正解', 'tall'),
        ('H30_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('H30_dai21mon_zu10_chiseki_sokuryouzu', '地積測量図（11番1・11番2）の完成見本', 'fig'),
        ('H30_dai21mon_zu11_toku_junban', '本番の解く順番の流れ図', 'fig')]
# ---- 画像（2026-10-02追加）：記事の画像挿入マーカーと zu/ のPNGが、記事の順に対応しているか ----
# 解説図の番号を記事の挿入順に振り直し、申請書でない解答欄（第1欄・第2欄）の完成形を足した。
from PIL import Image  # noqa: E402
ZU = os.path.join(HERE, 'zu')
markers = [l for l in text.splitlines() if l.startswith('> 【画像挿入】')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
for (name_, key_, kind_), m_ in zip(PNGS, markers):
    path_ = os.path.join(ZU, name_ + '.png')
    ok_ = os.path.exists(path_) and key_ in m_
    if ok_:
        w_, h_ = Image.open(path_).size
        ok_ = {'tall': w_ == 1200 and h_ > w_, 'wide': w_ == 1200 and h_ < w_, 'fig': w_ == 1600}[kind_]
    judge(f'PNG（マーカー順・大きさ） : {name_}（{key_}）', ok_)
    src_ = fig if '_zu' in name_ else (fix if 'machigai' in name_ else form)
    judge(f'プロンプトにファイル名 : zu/{name_}.png', f'zu/{name_}.png' in src_)
extra_ = sorted(set(f_[:-4] for f_ in os.listdir(ZU) if f_.endswith('.png')) - {n_ for n_, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない {extra_}', not extra_)
fig_order = [int(x_) for x_ in re.findall(r'^- \*\*図(\d+)：', fig, re.M)]
judge(f'解説図プロンプトの図の一覧が番号順（{fig_order}）', fig_order == sorted(fig_order))
zu_order = [int(n_.split('_zu')[1][:2]) for n_, _, _ in PNGS if '_zu' in n_]
judge(f'解説図の番号が記事の挿入順（{zu_order}）', zu_order == list(range(1, len(zu_order) + 1)))
lines_ = text.splitlines()


def after_(key, prev):
    """マーカー（key を含む）の直前の空行でない行に prev があるか（その問の答えの直後に置いたか）"""
    i_ = [k_ for k_, l_ in enumerate(lines_) if l_.startswith('> 【画像挿入】') and key in l_]
    j_ = i_[0] - 1 if i_ else -1
    while j_ >= 0 and not lines_[j_].strip():
        j_ -= 1
    judge(f'「{key}」のマーカーが答えの直後（直前の行に「{prev}」）', j_ >= 0 and prev in lines_[j_])


after_('第1欄（問1）の完成形', '**▶ I点（−50731.24, −14880.46）**')
after_('第2欄（問2）の完成形', '- **エ**：意思')
# 穴埋めの答えの語を、会話の中で語として言っているか（2026-10-02、R5/Q22の照らし直しから）
for s_ in ['（ア）は表題登記', '（イ）は『これに隣接する』', '（ウ）は登記された', '（エ）は意思']:
    check('穴埋めの答えの語を会話で明示', s_)
html_1 = open(os.path.join(ZU, 'H30_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
html_2 = open(os.path.join(ZU, 'H30_dai21mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['>第１欄<', 'Ｘ座標（m）', 'Ｙ座標（m）', '>−50720.53<', '>−14868.88<', '>−50731.24<', '>−14880.46<', '第1欄（問1）解答例']:
    check('第1欄の画像（HTML）', s_, html_1, '第1欄画像')
for s_ in ['>第２欄<', '>ア<', '>表題登記<', '>イ<', '>隣接する<', '>ウ<', '>登記された<', '>エ<', '>意思<', '第2欄（問2）解答例']:
    check('第2欄の画像（HTML）', s_, html_2, '第2欄画像')
absent('第2欄の画像に「合意」がない', '合意', html_2, '第2欄画像')
for s_ in ['Ｄ点「−50720.53」「−14868.88」、Ｉ点「−50731.24」「−14880.46」', 'ア「表題登記」、イ「隣接する」、ウ「登記された」、エ「意思」',
           'public/kijutsu/H30-tochi/a1.webp']:
    check('第1欄・第2欄の画像のプロンプト', s_, form, '登記申請書')
# 冒頭は照合済みの一文だけ（2026-09-30のルール）
judge('冒頭は「照合済みです。」の一文だけ', text.splitlines()[2] == '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')

print('NG件数:', ng)
