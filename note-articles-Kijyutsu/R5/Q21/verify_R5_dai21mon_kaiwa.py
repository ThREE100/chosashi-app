"""令和5年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
アガルートの解答例（第1欄・第2欄・第3欄の地積測量図・第4欄の登記申請書・第5欄）の値と一致することも確認する。
実行: python3 note-articles-Kijyutsu/R5/Q21/verify_R5_dai21mon_kaiwa.py"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, area, double_area_sum, chiseki, disp, fmt_num, kousa_kou2  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R5_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_R5_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R5_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R5_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R5_dai21mon_miidashi_gazou.md')
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


d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731

# ---- 座標（問題文の〔測量によって得られた座標値〕） ----
A, C, D, E = P(701.48, 692.76), P(702.79, 703.62), P(704.50, 717.76), P(679.68, 717.76)
F, G, I, J = P(680.14, 703.62), P(680.64, 703.62), P(680.64, 692.76), P(680.49, 692.76)
for n, p in {'A': A, 'C': C, 'F': F, 'J': J}.items():
    check(f'{n}の打ち込み', f'{p.real:.2f} [+] {p.imag:.2f} [i] [SHIFT] [STO] [{"X" if n == "J" else n}]')

# ---- 問1 ----
for s in ['C→G ＝ 702.79 − 680.64 ＝ 22.15', 'C→F ＝ 702.79 − 680.14 ＝ 22.65', 'A→I ＝ 701.48 − 680.64 ＝ 20.84',
          'A→J ＝ 701.48 − 680.49 ＝ 20.99', '11.64 ＋ 11.01 ＝ 22.65', '10.33 ＋ 10.66 ＝ 20.99']:
    check('問1 距離', s)
judge('C→F・A→J が地積測量図の合計と一致、C→G・A→I は不一致',
      d2(C, F) == f'{11.64 + 11.01:.2f}' and d2(A, J) == f'{10.33 + 10.66:.2f}' and d2(C, G) != d2(C, F)
      and d2(A, I) != d2(A, J))
check('FJ 表示', '表示：' + fmt_num(abs(F - J)))
judge('FJ ＝ 10.87（地積測量図の1番3の南の辺）、GI ＝ 10.86', d2(F, J) == '10.87' and d2(G, I) == '10.86')
judge('AC ＝ 10.94・EF ＝ 14.15（地積測量図の北・南の辺と一致）', d2(A, C) == '10.94' and d2(E, F) == '14.15')
for s in ['- **ア**：一筆', '- **イ**：測量', '- **ウ**：F点', '- **エ**：J点']:
    check('問1', s)

# ---- 問2 ----
Braw = A + (C - A) * 9.86 / 10.86
check('B 表示', '表示：' + disp(Braw))
B = r2(Braw)
check('B 答え', '**▶ B点（702.67, 702.62）**')
judge('9.86・10.86 はY座標の差', abs((702.62 - A.imag) - 9.86) < 1e-9 and abs((C.imag - A.imag) - 10.86) < 1e-9)
Bw = C + (A - C) / abs(A - C) * 1.00
check('ACに沿って1.00mの誤り', f'（{r2(Bw).real:.2f}, {r2(Bw).imag:.2f}）')
check('誤りの点とCGの距離', f'{C.imag - Bw.imag:.2f}m')
H = P(G.real, 702.62)
check('H 答え', f'**▶ H点（{H.real:.2f}, {H.imag:.2f}）**')
judge('H は直線GI上（X＝680.64）', H.real == I.real == G.real)
check('IH', f'702.62 − 692.76 ＝ {H.imag - I.imag:.2f}')

# ---- 問3の前提：分筆の区画と地積 ----
OTSU, N2, N4, SHA, HOSO = [A, C, F, J], [A, B, H, I], [B, C, F, J, I, H], [B, C, G, H], [I, H, G, F, J]
s4 = double_area_sum(OTSU)
check('乙土地 表示', f'表示：（実部）− {fmt_num(abs(s4.imag))}i')
check('乙土地 面積', f'{area(OTSU):.4f}㎡')
check('乙土地 台形', f'21.82 × 10.86 ＝ {area(OTSU):.4f}')
check('差', f'差は{area(OTSU) - 236.81:.4f}㎡')
check('公差（参考）', f'≒ {kousa_kou2(236.81):.2f}')
judge('差 ＜ 甲2の公差 → 地積更正不要', area(OTSU) - 236.81 < kousa_kou2(236.81))
check('1番2', f'(20.84 ＋ 22.03) ÷ 2 × 9.86 ＝ {area(N2):.4f}')
check('BH', f'702.67 − 680.64 ＝ {B.real - H.real:.2f}')
check('1番2 地積', f'1番2は{chiseki(area(N2)):.2f}㎡')
check('斜線部分', f'(22.03 ＋ 22.15) ÷ 2 × 1.00 ＝ {area(SHA):.2f}')
check('細長い部分', f'(0.15 ＋ 0.50) ÷ 2 × 10.86 ＝ {area(HOSO):.4f}')
check('1番4', f'22.09 ＋ 3.5295 ＝ {area(N4):.4f}')
check('1番4 地積', f'1番4は{chiseki(area(N4)):.2f}㎡')
check('合計のずれ', f'211.3491 ＋ 25.6195 ＝ {area(N2) + area(N4):.4f}')
check('ずれ', f'{area(N2) + area(N4) - area(OTSU):.4f}だけずれる')

# ---- 問3 地積測量図の辺長 ----
check('AB 表示', '表示：' + fmt_num(abs(B - A)))
check('BC 表示', '表示：' + fmt_num(abs(C - B)))
SIDES = {'AB': (A, B), 'BC': (B, C), 'CF': (C, F), 'FJ': (F, J), 'JI': (J, I), 'IA': (I, A)}
for n, (p, q) in SIDES.items():
    check(f'辺長{n}', f'- **{n}**：{d2(p, q)}')
check('辺長BH', f'- **BH（分筆線）**：{d2(B, H)}')
check('辺長HI', f'- **HI（分筆線）**：{d2(H, I)}')
check('地番欄', '地番欄は『1番2、1番4』、土地の所在は『A市B町二丁目』')
check('境界標', '境界標（A・B・H・Jはコンクリート杭、C・F・Iは金属標）')

# ---- 問4 ----
check('分合筆後の1番1', f'335.5096500 ＋ 22.09 ＝ {335.5096500 + 22.09:.5f}')
check('1番1 地積', f'{chiseki(335.5096500 + 22.09):.2f}㎡です！')
check('誤り（登記記録の335に足す）', f'{335 + 22.09:.2f}㎡！')
BIG = [B, C, D, E, F, G, H]
check('誤り（座標で計算）', f'{chiseki(area(BIG)):.2f}㎡ですか')
check('細長い部分の地積', f'3.5295だから、{chiseki(area(HOSO)):.2f}')
judge('（イ）3.52 ＋（ロ）22.09 ＝ 1番4の25.61', abs(chiseki(area(HOSO)) + 22.09 - 25.61) < 1e-9)
check('地積の検算', '3.52 ＋ 22.09 ＝ 25.61')
for s in ['- **登記の目的**：土地地目変更・分合筆登記', '- **添付書類**：地積測量図　登記識別情報　印鑑証明書　代理権限証書',
          '- **申請人**：A市B町二丁目2番地1　河野桂子', '- **登録免許税**：金2,000円', '- **所在**：A市B町二丁目',
          '①1番4、②宅地、③25.61、登記原因は空欄', '①（イ）1番4、②宅地、③3.52、登記原因「③1番1に一部合併」',
          '①（ロ）、③22.09、登記原因「1番4から分筆して1番1に合併する部分」', '①1番1、②雑種地、③335、登記原因は空欄',
          '①1番1、②宅地、③357.59、登記原因「②③令和5年9月20日地目変更　③1番4から一部合併」']:
    check('問4', s)
check('登録免許税の誤答', '1,000円 × 2個 ＝ 2,000円')

# ---- 問5 ----
for s in ['- **①**：表題部所有者', '- **②**：所有権', '- **③**：異議', '- **④**：職権']:
    check('問5', s)

# ---- アガルートの解答例（照合済み）と同じ答えか ----
KAITO = ['一筆', '測量', 'F点', 'J点', '（702.67, 702.62）', '（680.64, 702.62）', '表題部所有者', '所有権', '異議', '職権',
         '土地地目変更・分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', 'A市B町二丁目2番地1　河野桂子',
         '金2,000円', '③1番1に一部合併', '1番4から分筆して1番1に合併する部分', '②③令和5年9月20日地目変更',
         '③1番4から一部合併', '25.61', '3.52', '22.09', '335', '357.59', '『1番2、1番4』', '9.93', '1.01', '22.65',
         '10.87', '0.15', '20.84', '22.03', '9.86']
for s in KAITO:
    check('解答例と共通の答え', s)

# ---- 電卓操作の変数（割り当て表と一致） ----
for m in re.finditer(r'^電卓操作（(.+?)）', text, re.M):
    pairs = m.group(1).split('、')
    judge(f'電卓操作の見出し（{m.group(1)}）が割り当て表どおり',
          all(p in ('A＝A点', 'B＝B点', 'C＝C点', 'F＝F点', 'X＝J点') for p in pairs))
for s in ['- **A**：A点', '- **C**：C点', '- **F**：F点', '- **X**：J点', '- **B**：B点']:
    check('変数の割り当て', s)

# ---- 条文（原典で確認済みのものだけ） ----
for s in ['不動産登記令第2条第3号', '不動産登記規則第77条第1項第6号', '規則第77条第1項第9号', '不動産登記規則第35条第1号',
          '規則第35条第7号', '不動産登記法第41条第2号', '法第41条第6号', '準則第68条第3号', '法第37条第1項', '規則第100条',
          '不動産登記令第8条第1項第1号', '同条第2項第1号', '不動産登記規則第47条第3号イ（6）', '不動産登記令第18条第1項・第2項',
          '準則第76条', '準則第72条第1項', '不動産登記法第39条第3項', '不動産登記規則第10条第2項第1号', '同条第4項第1号']:
    check('条文', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
N_FIG = 10
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（{N_FIG}枚）', n_fig == N_FIG)
for i in range(1, N_FIG + 1):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R5_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
for s in ['(702.67, 702.62)', '(680.64, 702.62)', '(702.67, 702.63)', '236.9652', '211.3491', '25.6195', '22.09', '3.5295',
          '335.5096500 ＋ 22.09 ＝ 357.59965', '357.59', 'AB 9.93', 'BC 1.01', 'FJ 10.87', 'JI 0.15', 'BH 22.03', 'HI 9.86',
          'CG 22.15', 'AJ 20.99', '0.1552', '約1.37']:
    check('解説図の数値', s, fig, '解説図')
for s in ['土地地目変更・分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', 'Ａ市Ｂ町二丁目２番地１　河野桂子',
          '金2,000円', '令和５年10月16日　申請　Ａ地方法務局', '「25｜61」', '「3｜52」', '「22｜09」', '「335｜」', '「357｜59」',
          '③１番１に一部合併', '１番４から分筆して１番１に合併する部分', '②③令和５年９月20日地目変更', '③１番４から一部合併']:
    check('登記申請書', s, form, '登記申請書')
for s in ['地積測量図　登記識別情報　代理権限証書', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', '「357｜09」', '「357｜59」',
          '335.5096500＋22.09＝357.59965', '②令和５年９月20日地目変更', '②③令和５年９月20日地目変更']:
    check('添削', s, fix, '添削')

# ---- 追加作業（最新の指示書との照らし合わせ） ----
# 誤った筆界（G・I）の面積が合わないこと、甲土地の裏付け
check('G・Iを通した乙土地', f'(20.84 ＋ 22.15) ÷ 2 × 10.86 ＝ {area([A, C, G, I]):.4f}（差 {236.81 - area([A, C, G, I]):.4f}）')
judge('G・Iだと差が公差を超え、F・Jだと範囲内',
      236.81 - area([A, C, G, I]) > kousa_kou2(236.81) > area(OTSU) - 236.81)
check('甲土地（F点を角に）', f'(22.65 ＋ 24.82) ÷ 2 × 14.14 ＝ {area([C, D, E, F]):.4f}')
judge('甲土地と地積測量図の差 0.10', f'{area([C, D, E, F]) - 335.5096500:.2f}' == '0.10')
check('甲土地の差', '335.5096500 との差 0.10')
# 分筆後の地積の合計と公差
s_after = chiseki(area(N2)) + chiseki(area(N4))
check('分筆後の合計', f'211.34 ＋ 25.61 ＝ {s_after:.2f}（登記記録 236.81 との差 {s_after - 236.81:.2f}）')
# 別解（CGから1.00m西の点と交点）
M = C - 1j
check('別解の点', f'C − 1i ＝（{M.real:.2f}, {M.imag:.2f}）')
judge('別解の交点がBと同じ', r2(A + (C - A) * (M.imag - A.imag) / (C.imag - A.imag)) == B)
# 作図の範囲（1/250で何mmか）
check('作図の範囲', '93mm × 51mm')
judge('作図の範囲 93mm × 51mm', round((703.30 - 680.04) * 4) == 93 and round((703.62 - 690.97) * 4) == 51)
check('単位の表示', '辺長の単位の表示（単位：m）')
# 時間配分（具体的に）
for s in ['いちばん時間を食うのは問3の地積測量図の作図', '地積測量図が描けていなくても全部書ける', '最後に問3の作図']:
    check('時間配分', s)
# 注の番号の書き分け（問題文の注と調査図素図の注）
bare = [m.group(0) for m in re.finditer(r'(.{0,6})注[0-9]', text) if not re.search(r'(問題文の|調査図素図の|、)$', m.group(1))]
judge(f'注の番号に「問題文の」「調査図素図の」が付いている（例外：直前の注に続く「、注3」）: {bare}', not bare)
check('調査図素図の注', '調査図素図の注2でHはGとIを結ぶ直線上')
# 作図の表示範囲は pad_aspect
draw = open(os.path.join(HERE, 'zu', 'draw_R5_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
fits = re.findall(r'^\s*fit\(.*$', draw, re.M)
judge(f'作図の fit はすべて pad_aspect=True（{len(fits)}か所）', fits and all('pad_aspect=True' in f for f in fits))
# 申請書の完成形・添削画像（PNGが縦長・横1200px、HTMLの記入データ）
import struct
def png_size(path):
    with open(path, 'rb') as f:
        f.read(16)
        return struct.unpack('>II', f.read(8))
for name in ['R5_dai21mon_toukishinseisho_kansei', 'R5_dai21mon_toukishinseisho_machigai']:
    w, h = png_size(os.path.join(HERE, 'zu', name + '.png'))
    judge(f'{name}.png が縦長・横1200px（{w}×{h}）', w == 1200 and h > w)
kh = open(os.path.join(HERE, 'zu', 'R5_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
for s in ['土地地目変更・分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', 'Ａ市Ｂ町二丁目２番地１　河野桂子', '金2,000円',
          '令和５年10月16日　申請　Ａ地方法務局', '（イ）１番４', '③１番１に一部合併', '１番４から分筆して１番１に合併する部分',
          '雑種地', '>335<', '>357<', '>59<', '②③令和５年９月20日地目変更<br>③１番４から一部合併']:
    check('完成形のHTML', s, kh, '完成形HTML')
mh = open(os.path.join(HERE, 'zu', 'R5_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['①誤答', '②添削（赤ペン）', '③正解', '地積測量図　登記識別情報　代理権限証書', '>09<', '>59<', '印鑑証明書',
          '335.5096500＋22.09＝357.59965', '②令和５年９月20日地目変更']:
    check('添削のHTML', s, mh, '添削HTML')
check('添削プロンプトは縦に積む版', '縦に3コマ積む', fix, '添削')
absent('添削プロンプトに横並びの旧指示', '横1800px', fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいを', 'くいが', '合筆登記」です！」']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
speakers = [(i + 1, l.rstrip()) for i, l in enumerate(lines) if l.rstrip() in ('**トリ先生**', '**藍子**')]
same = []
for (i1, s1), (i2, s2) in zip(speakers, speakers[1:]):
    between = lines[i1:i2 - 1]
    if s1 == s2 and not any(x.startswith(('```', '- ', '#', '表示：', '式', '電卓', '**▶')) for x in between):
        same.append(i2)
judge(f'同じ話者のセリフの連続（画像挿入マーカーをはさむものも）: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋添削1＋完成形1＋第1欄・第2欄・第5欄3＝計{N_FIG + 5}か所の想定）',
      n_marker == N_FIG + 5)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和5年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和5年度問題21（土地）', thumb, '見出し画像')
check('見出し画像の半角英字の例外', 'Latin capital letters "G" and\n"I"', thumb, '見出し画像')

check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')

# ---- 2026-10-02の照らし直し：画像挿入マーカーと zu/ のPNGが記事の順に対応しているか ----
from PIL import Image  # noqa: E402
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R5_dai21mon_zu01_zentaizu', '全体図', 'fig'),
        ('R5_dai21mon_zu02_hikkaiten_FJ', '筆界点の判断の比較図', 'fig'),
        ('R5_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R5_dai21mon_zu03_B_heikou', 'B点の求め方の図', 'fig'),
        ('R5_dai21mon_zu09_B_betsukai', 'B点の別解の図', 'fig'),
        ('R5_dai21mon_zu04_H_kousa', 'H点の求め方の図', 'fig'),
        ('R5_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('R5_dai21mon_zu05_bunpitsu_kukaku', '8月の分筆の区画の比較図', 'fig'),
        ('R5_dai21mon_zu06_chiseki_sokuryouzu', '地積測量図（1番2・1番4）の完成見本', 'fig'),
        ('R5_dai21mon_zu07_bungouhitsu', '10月16日の分合筆の図', 'fig'),
        ('R5_dai21mon_toukishinseisho_machigai', '誤答→添削→正解の3コマ', 'tall'),
        ('R5_dai21mon_toukishinseisho_kansei', '登記申請書（問4）の完成形', 'tall'),
        ('R5_dai21mon_zu08_shokken_bungouhitsu', '問5の図', 'fig'),
        ('R5_dai21mon_dai5ran_kansei', '第5欄（問5）の完成形', 'wide'),
        ('R5_dai21mon_zu10_toku_junban', '本番で解く順番の図', 'fig')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
for (name, key, kind), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        ok = (w == 1200 and h > w) if kind == 'tall' else (w == 1200 and h < w) if kind == 'wide' else w >= 1200
    judge(f'PNG（マーカー順・大きさ） : {name}', ok)
    src, sname = (fig, '解説図') if '_zu' in name else (fix, '添削') if 'machigai' in name else (form, '登記申請書')
    check('プロンプトにファイル名', f'zu/{name}.png', src, sname)
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない : {extra}', not extra)

# ---- 穴埋めの答えの語を会話の中で言っているか（2026-10-02追加）----
check('問1 ア・イ（会話）', '（ア）は『一筆』、（イ）は『測量』です！')
check('問1 ア〜エ（会話）', '答案の第1欄は、アが『一筆』、イが『測量』、ウが『F点』、エが『J点』。')
check('問5 ①〜④（会話）', '答案の第5欄は、①表題部所有者、②所有権、③異議、④職権。')
check('問5 ③の対（会話）', '『承諾があるとき』じゃなくて、『異議がないとき』よ')
check('問2 座標の欄（会話）', '答案の第2欄は、B点が（702.67, 702.62）、H点が（680.64, 702.62）。')
for name, needles in [('R5_dai21mon_dai2ran_kansei', ['第2欄', 'Ｘ座標（m）', 'Ｂ点', '>702.67<', '>702.62<', 'Ｈ点', '>680.64<']),
                      ('R5_dai21mon_dai1ran_kansei', ['第1欄', '>ア<', '一筆', '測量', 'Ｆ点', 'Ｊ点']),
                      ('R5_dai21mon_dai5ran_kansei', ['第5欄', '>①<', '表題部所有者', '所有権', '異議', '職権'])]:
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        check(f'{name}.html', n, h, '欄の完成形HTML')
for s_ in ['ア「一筆」、イ「測量」／ウ「Ｆ点」、エ「Ｊ点」', '①「表題部所有者」、②「所有権」／③「異議」、④「職権」', '仮の形']:
    check('欄の完成形プロンプト', s_, form, '登記申請書')

# ---- 図9（B点の別解）・図10（解く順番）の文言（2026-10-02追加）----
for s_ in ['C − 1i ＝（702.79, 702.62）', '本番で解く順番（問3の作図は最後に回す）', '地積測量図がなくても書ける']:
    check('図9・図10のプロンプト', s_, fig, '解説図')
draw_src = open(os.path.join(ZU, 'draw_R5_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
for s_ in ["'C − 1i ＝（702.79, 702.62）\\nCGから西へ直角に1.00m'", "'図10　本番で解く順番　問3の作図は最後に回す'"]:
    check('作図スクリプト', s_, draw_src, '作図')

print('NG件数:', ng)
