"""平成24年度 第21問（土地）会話形式note記事：記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-30に添付の過去問集〈全26ページ〉で照合。下の AGAROOT に転記）と一致することも確認する。
過去問集の問題の再掲・解説は日付が平成30年に置き換わっていた（依頼 平成30年2月、分筆の申請 平成30年2月9日など）ので、
記事は試験問題本文（午後の部21〜30ページ）と答案用紙（平成何年何月何日申請と印刷）どおりに書き、その日付で照合する。
実行: python3 note-articles-Kijyutsu/H24/Q21/verify_H24_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num, intersect  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H24_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H24_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H24_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H24_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H24_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H24_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（別紙4・別紙5） ----
A, B, C = P(-8030.50, -2530.30), P(-8041.69, -2518.63), P(-8034.17, -2510.92)
D, E, F = P(-8025.02, -2504.71), P(-8019.28, -2510.26), P(-8015.81, -2516.60)
G, H = P(-8031.92, -2528.82), P(-8024.15, -2521.37)
I, J = P(-8032.59, -2528.12), P(-8024.82, -2520.67)
K611, K612 = P(-8044.07, -2519.78), P(-8031.34, -2532.58)
OTHERS = {'4-613': P(-8017.59, -2556.97), 'A3-5': P(-8066.06, -2497.11), 'A3-6': P(-8018.01, -2468.93),
          'B3-20': P(-8002.88, -2582.05), 'B3-21': P(-8069.25, -2624.64)}
for s in ['0 [−] 8032.59 [−] 2528.12 [i] [SHIFT] [STO] [X]', '0 [−] 8024.82 [−] 2520.67 [i] [SHIFT] [STO] [Y]',
          '0 [−] 8031.92 [−] 2528.82 [i] [SHIFT] [STO] [A]', '0 [−] 8024.15 [−] 2521.37 [i] [SHIFT] [STO] [B]',
          '0 [−] 8034.17 [−] 2510.92 [i] [SHIFT] [STO] [C]', '0 [−] 8025.02 [−] 2504.71 [i] [SHIFT] [STO] [D]',
          '0 [−] 8041.69 [−] 2518.63 [i] [SHIFT] [STO] [D]']:
    check('座標の入力', s)
judge('Iは直線AB上でAから3.02m（別紙図面の注2）', abs((B - A).conjugate() * (I - A)).real > 0
      and abs(((B - A).conjugate() * (I - A)).imag) / abs(B - A) < 0.01 and round(abs(I - A), 2) == 3.02)
check('入口の幅 AG 2.05 → AI 3.02', 'AGは2.05mしかないけど、Iまで広げればAIは別紙図面の注2の3.02m')
judge('AGは2.05', f'{abs(G - A):.2f}' == '2.05')

# ---- 問1 K点 ----
KX = J + (J - I) / abs(J - I) * 0.65
check('K 表示', '表示：' + disp(KX))
K = r2(KX)
check('K 答え', '**▶ K点（−8024.35, −2520.22）**')
judge('Kの丸め', K == P(-8024.35, -2520.22))
check('K 記憶', '0 [−] 8024.35 [−] 2520.22 [i] [SHIFT] [STO] [E]')
check('I→Jの方向角', to_dms(cmath.phase(J - I)))
check('真数表 43°47′44″', '真数表の43°47′44″の行')
KW = r2(J - (J - I) / abs(J - I) * 0.65)
check('誤りのK（Iの向きへ戻る）', f'（{KW.real:.2f}, {KW.imag:.2f}）'.replace('-', '−'))
judge('誤りのKとKはHCの線をはさんで反対側（誤りのKは南）', ((C - H).conjugate() * (KW - H)).imag * ((C - H).conjugate() * (K - H)).imag < 0
      and KW.real < K.real)
pc = (C - H).conjugate() * (J - I)
check('直角の確認 表示', '表示：' + disp(pc))
check('H→Cの方向角', to_dms(cmath.phase(C - H)))
check('真数表 133°47′48″', '真数表の133°47′48″の行')

# ---- 問1の準備 イの面積 ----
di = (J - G).conjugate() * (I - H)
check('イ 表示', '表示：' + disp(di))
SI = abs(di.imag) / 2
judge('イの対角線の式と多角形の式が一致', abs(SI - area([G, H, J, I])) < 1e-6)
check('イ 面積', f'20.861 ÷ 2 ＝ {SI:.4f}㎡')
TGT = 10.4305 * 1.087
check('アの目標', f'10.4305 × 1.087 ＝ {TGT:.7f}')

# ---- 問1 L点 ----
a1 = (J - K).conjugate() * (C - K)
a2 = (C - K).conjugate() * (D - K)
check('△KJC 表示', '表示：' + disp(a1))
check('△KCD 表示', '表示：' + disp(a2))
judge('△KJC 4.395・△KCD 73.0386', f'{abs(a1.imag) / 2:.3f}' == '4.395' and f'{abs(a2.imag) / 2:.4f}' == '73.0386')
check('△の面積', '△KJCは 8.79 ÷ 2 ＝ 4.395㎡、△KCDは 146.0772 ÷ 2 ＝ 73.0386㎡')
check('△KCLに要る面積', f'11.3379535 − 4.395 ＝ {TGT - 4.395:.7f}㎡')
t = (TGT - 4.395) / 73.0386
check('t', f't ＝ (11.3379535 − 4.395) ÷ 73.0386 ＝ 6.9429535 ÷ 73.0386 ＝ {fmt_num(t)}')
LX = C + (D - C) * t
check('L 表示', '表示：' + disp(LX))
L = r2(LX)
check('L 答え', '**▶ L点（−8033.30, −2510.33）**')
judge('Lの丸め', L == P(-8033.30, -2510.33))
check('L 記憶', '0 [−] 8033.30 [−] 2510.33 [i] [SHIFT] [STO] [F]')
KU = KX   # 丸める前のK
a1u = abs(((J - KU).conjugate() * (C - KU)).imag) / 2
a2u = abs(((C - KU).conjugate() * (D - KU)).imag) / 2
LU = r2(C + (D - C) * (TGT - a1u) / a2u)
judge(f'丸める前のKでもLは同じ（△KJC {a1u:.4f}）', LU == L and fmt_num(a1u) == '4.3903…')
check('丸める前のKの△KJC', '△KJCが4.3903…になるけど')
da = (L - J).conjugate() * (K - C)
check('ア 表示', '表示：' + disp(da))
SA = abs(da.imag) / 2
judge('アの対角線の式と多角形の式が一致', abs(SA - area([J, C, L, K])) < 1e-6)
check('ア 面積と比', f'22.6748 ÷ 2 ＝ {SA:.4f}㎡。11.3374 ÷ 10.4305 ＝ {fmt_num(SA / 10.4305)}')
judge('比は四捨五入で1.087', round(SA / 10.4305, 3) == 1.087)
LE = r2(C + (D - C) * (10.4305 - 4.395) / 73.0386)
check('同じ面積にした誤りのL', f'Lは（{LE.real:.2f}, {LE.imag:.2f}）'.replace('-', '−'))
judge('誤りのLは0.1m以上Cの側', abs(LE - C) < abs(L - C) and abs(L - LE) > 0.1)

# ---- L点の別解 ----
check('KC 表示', '表示：' + fmt_num(abs(C - K)))
check('K→Cの方向角', to_dms(cmath.phase(C - K)))
h = 2 * 6.9429535 / abs(C - K)
check('高さ', f'2 × 6.9429535 ÷ 13.5248… ＝ {fmt_num(h)}')
M = C + h * cmath.rect(1, dms(46, 33, 28))
check('M 表示', '表示：' + disp(M))
LA, tA, num, den = intersect(C, D, M, M + (C - K))
judge('別解の分子は実部ほぼ0', abs(num.real) < 1e-4)
check('別解の分子のiの係数', fmt_num(num.imag))
check('別解の分母のiの係数', f'iの係数は{fmt_num(den.imag)}')
judge('別解のLも同じ', r2(LA) == L)
check('別解のt', f'13.8859… ÷ 146.0772 ＝ {fmt_num(tA)}')
for s in ['136°33′28″', '46°33′28″']:
    check('真数表の行（別解）', s)

# ---- 問3 地積 ----
d0 = (C - G).conjugate() * (H - B)
check('5番2（平成23年）表示', '表示：' + disp(d0))
check('5番2（平成23年）面積', f'307.801 ÷ 2 ＝ {abs(d0.imag) / 2:.4f}で、153.90㎡')
d1 = (C - I).conjugate() * (J - B)
check('5番2（イ分筆後）表示', '表示：' + disp(d1))
S52 = abs(d1.imag) / 2
judge('5番2の対角線の式と多角形の式が一致', abs(S52 - area([I, B, C, J])) < 1e-6)
check('5番2 面積', f'286.9408 ÷ 2 ＝ {S52:.4f}で、宅地なので小数第2位未満を切り捨てて{chiseki(S52):.2f}㎡')
check('153.90 − 10.43', '153.90 − 10.43（5番4）＝ 143.47')
judge('153.90 − 10.43 ＝ 143.47', abs(153.90 - 10.43 - 143.47) < 1e-9 and chiseki(SI) == 10.43)
mp = (B - I) * (C - I).conjugate() + (C - I) * (L - I).conjugate() + (L - I) * (K - I).conjugate()
check('5点で回した 表示', '表示：' + disp(mp))
judge('5点の式と多角形の式が一致', abs(abs(mp.imag) / 2 - area([I, B, C, L, K])) < 1e-6)
check('5点で回した面積', f'309.6206 ÷ 2 ＝ {abs(mp.imag) / 2:.4f}で、154.81㎡')
check('合筆後', f'{S52 + SA:.4f}で、154.80㎡')
judge('合筆後 154.80・5点 154.81', chiseki(S52 + SA) == 154.80 and chiseki(abs(mp.imag) / 2) == 154.81)
judge('I・J・Kの三角形 0.0025', f'{area([I, J, K]):.4f}' == '0.0025')
check('三角形の0.0025', '小さな三角形の0.0025㎡')
judge('登記記録どうしの合計も154.80', abs(143.47 + 11.33 - 154.80) < 1e-9)

# ---- 問3 申請書 ----
for s in ['- **1行目**：①5番2、②宅地、③143.47、登記原因及びその日付は空欄',
          '- **2行目**：①5番3、②宅地、③11.33、登記原因及びその日付「5番2に合筆」',
          '- **3行目**：①5番2、②宅地、③154.80、登記原因及びその日付「③5番3を合筆」',
          '- **登記の目的**：土地合筆登記', '- **添付書類**：登記識別情報　印鑑証明書　代理権限証書',
          '- **登録免許税**：金1,000円（合筆後の土地1個 × 1,000円）', '- **申請人**：A市C町六丁目4番9号　海川二郎',
          '- **所在**：D市E町六丁目']:
    check('問3', s)
for s in ['不動産登記法第41条', '同条第3号', '不動産登記規則第106条', '登録免許税法別表第一の一の（十三）ロ',
          '不動産登記令第8条第1項第1号', '同条第2項第1号', '不動産登記規則第47条第3号イ（6）',
          '不動産登記令第18条第1項・第2項、不動産登記規則第49条', '合筆だから地積測量図は要らない']:
    check('問3の根拠', s)

# ---- 問2 地積測量図 ----
SIDES = {'AG': (A, G), 'GH': (G, H), 'HJ': (H, J), 'JK': (J, K), 'KL': (K, L), 'LD': (L, D), 'DE': (D, E),
         'EF': (E, F), 'FA': (F, A), 'JC': (J, C), 'CL': (C, L)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
check('HJ・JKの丸め', f'HJは{fmt_num(abs(J - H))}で0.97、JKは{fmt_num(abs(K - J))}で0.65')
for s in ['不動産登記規則第78条', '- **地番欄**：（略）と印刷済み。書かない', '- **土地の所在**：D市E町六丁目',
          '- **分筆後の土地**：5－1（イ）、5－3（ロ）', 'GHJCの南は5－2', 'コンクリート杭はC・D・E・G・H・J・K・L（J・K・Lは新設）、金属標はA・F',
          'D市4級基準点4-611（X −8044.07、Y −2519.78）', 'D市4級基準点4-612（X −8031.34、Y −2532.58）',
          '- **申請人**：山川一郎。縮尺は250分の1と印刷済み', 'I点とB点（5番1の筆界点ではない）']:
    check('問2', s)
check('4-612はAから', f'4-612はAから{abs(K612 - A):.2f}m')
check('4-611はCから', f'4-611はCから{abs(K611 - C):.2f}m')
pts51 = [A, G, H, J, K, L, D, E, F, C]
judge('最も近い2点は4-611・4-612（他は20m以上）',
      all(min(abs(o - p) for p in pts51) > 20 for o in OTHERS.values())
      and max(min(abs(k - p) for p in pts51) for k in (K611, K612)) < 20)
xs = [p.real for p in pts51]
ys = [p.imag for p in pts51]
check('5番1の大きさ', f'東西が約{round(max(ys) - min(ys)):d}m、南北が約{round(max(xs) - min(xs)):d}mで、横約{round((max(ys) - min(ys)) * 4):d}mm・縦約{round((max(xs) - min(xs)) * 4):d}mm')
xs2 = xs + [K611.real, K612.real]
ys2 = ys + [K611.imag, K612.imag]
check('基準点まで入れた大きさ', f'横約{round((max(ys2) - min(ys2)) * 4):d}mm・縦約{round((max(xs2) - min(xs2)) * 4):d}mm')
check('答案用紙の枠', '枠は横約30cm・縦約22cm')

# ---- 問4 ----
for s in ['- **結論**：お互いの土地の地積を更正する方法による登記の手続をすることはできない。',
          '- **理由**：地積の更正の登記は、登記記録の地積が筆界に囲まれた土地の実際の面積と相違する場合に、これを正すための登記であり、筆界を変更する登記ではない。5番1の土地と5番2の土地の筆界は、G点、H点及びC点を順次直線で結んだ線であり、公法上の境界である筆界は所有者間の合意によって変更することができないから、地積の更正の登記によってI点、K点及びL点を順次直線で結んだ線を筆界とすることはできない。',
          '不動産登記法第38条', '不動産登記法第123条第1号', '報告的な登記', '形成的な登記', '別紙図面の注7']:
    check('問4', s)

# ---- アガルートの解答例（2026-09-30、過去問集の解答例ページから転記。欄・空欄ごとに全部照らす） ----
AGAROOT = {
    '第1欄 K点X':            ('−8024.35', '**▶ K点（−8024.35, −2520.22）**'),
    '第1欄 K点Y':            ('−2520.22', '**▶ K点（−8024.35, −2520.22）**'),
    '第1欄 L点X':            ('−8033.30', '**▶ L点（−8033.30, −2510.33）**'),
    '第1欄 L点Y':            ('−2510.33', '**▶ L点（−8033.30, −2510.33）**'),
    '第2欄 登記の目的':      ('土地合筆登記', '- **登記の目的**：土地合筆登記'),
    '第2欄 添付書類':        ('登記識別情報 印鑑証明書 代理権限証書', '- **添付書類**：登記識別情報　印鑑証明書　代理権限証書'),
    '第2欄 登録免許税':      ('金1,000円', '- **登録免許税**：金1,000円'),
    '第2欄 申請人':          ('A市C町六丁目4番9号 海川二郎', '- **申請人**：A市C町六丁目4番9号　海川二郎'),
    '第2欄 所在':            ('D市E町六丁目', '- **所在**：D市E町六丁目'),
    '第2欄 1行目 地番':      ('5番2', '- **1行目**：①5番2'),
    '第2欄 1行目 地目':      ('宅地', '- **1行目**：①5番2、②宅地'),
    '第2欄 1行目 地積':      ('143.47', '③143.47、登記原因及びその日付は空欄'),
    '第2欄 1行目 原因':      ('空欄', '③143.47、登記原因及びその日付は空欄'),
    '第2欄 2行目 地番':      ('5番3', '- **2行目**：①5番3'),
    '第2欄 2行目 地目':      ('宅地', '- **2行目**：①5番3、②宅地'),
    '第2欄 2行目 地積':      ('11.33', '③11.33、登記原因及びその日付「5番2に合筆」'),
    '第2欄 2行目 原因':      ('5番2に合筆', '登記原因及びその日付「5番2に合筆」'),
    '第2欄 3行目 地番':      ('5番2', '- **3行目**：①5番2'),
    '第2欄 3行目 地目':      ('宅地', '- **3行目**：①5番2、②宅地'),
    '第2欄 3行目 地積':      ('154.80', '③154.80、登記原因及びその日付「③5番3を合筆」'),
    '第2欄 3行目 原因':      ('③5番3を合筆', '登記原因及びその日付「③5番3を合筆」'),
    '第3欄 結論':            ('お互いの土地の地積を更正する方法による登記の手続をすることはできない。',
                              '- **結論**：お互いの土地の地積を更正する方法による登記の手続をすることはできない。'),
    '第3欄 理由（地積更正の意義）': ('地積更正登記は、登記記録上の地積が土地の現況と相違する場合に現況に合致させるための登記',
                              '登記記録の地積が筆界に囲まれた土地の実際の面積と相違する場合に、これを正すための登記'),
    '第3欄 理由（筆界）':    ('G点、H点及びC点を順次直線で結んだ線は公法上の境界である筆界',
                              'G点、H点及びC点を順次直線で結んだ線であり、公法上の境界である筆界'),
    '第3欄 理由（結論）':    ('地積更正登記によってI点、K点及びL点を順次直線で結んだ線に移動することはできない',
                              '地積の更正の登記によってI点、K点及びL点を順次直線で結んだ線を筆界とすることはできない'),
    'その2 地番':            ('（略）（印刷）', '- **地番欄**：（略）と印刷済み。書かない'),
    'その2 土地の所在':      ('D市E町六丁目', '- **土地の所在**：D市E町六丁目'),
    'その2 申請人':          ('山川一郎', '- **申請人**：山川一郎'),
    'その2 分筆後の符号':    ('5－1（イ）、5－3（ロ）', '- **分筆後の土地**：5－1（イ）、5－3（ロ）'),
    'その2 辺長AG':          ('2.05', '- **AG**：2.05'),
    'その2 辺長GH':          ('10.76', '- **GH**：10.76'),
    'その2 辺長HJ':          ('0.97', '- **HJ**：0.97'),
    'その2 辺長JK':          ('0.65', '- **JK**：0.65'),
    'その2 辺長KL':          ('13.34', '- **KL**：13.34'),
    'その2 辺長LD':          ('10.01', '- **LD**：10.01'),
    'その2 辺長DE':          ('7.98', '- **DE**：7.98'),
    'その2 辺長EF':          ('7.23', '- **EF**：7.23'),
    'その2 辺長FA':          ('20.09', '- **FA**：20.09'),
    'その2 辺長JC':          ('13.51', '- **JC**：13.51'),
    'その2 辺長CL':          ('1.05', '- **CL**：1.05'),
    'その2 隣接地':          ('9・8・6・4－2・5－2・道路', 'AFの西は4－2、Fの北の角は9、FEDの北は8、LDとCLの東は6、GHJCの南は5－2、AGの南西は道路'),
    'その2 境界標':          ('C・D・E・G・H・J・K・L コンクリート杭、A・F 金属標', 'コンクリート杭はC・D・E・G・H・J・K・L（J・K・Lは新設）、金属標はA・F'),
    'その2 基準点':          ('4-611・4-612（名称と座標値）', 'D市4級基準点4-611（X −8044.07、Y −2519.78）'),
    'その2 単位':            ('（単位：m）', '（単位：ｍ）'),
    '解説 イの面積':         ('10.4305、ア 11.3379535', '10.4305 × 1.087 ＝ 11.3379535'),
    '解説 5番2・5番3':       ('143.4704、11.3374、合筆後 154.8078', '154.8078で、154.80㎡'),
}
for k, (ag, s) in AGAROOT.items():
    src = draw if k == 'その2 単位' else None
    check(f'アガルートの解答例と一致（{k}：{ag}）', s, src, '作図' if src else '記事')
judge(f'解答例の欄の数 {len(AGAROOT)}（第1欄〜第3欄・その2の全欄）', len(AGAROOT) == 46)

# ---- 最新の執筆ルールで足した内容 ----
for s in ['座標は問題文の注1で', '問題文の注5の三角関数真数表', '別紙図面の注4', '別紙図面の注5', '別紙図面の注6',
          '辺の長さを言いなさい。問題文の注3で', '（問題文の注3）', '別紙図面の注7']:
    check('注の書き分け', s)
for bad in ['座標は注1で', '（注3）', '（注5）', '（注6）']:
    absent('書き分けていない注', bad)
for s in ['今年いちばん時間を食うのは、イの面積からL点までの計算と、辺長11本の地積測量図', '- **1**：問4（第3欄）',
          '- **2**：問3の申請書のうち計算なしで書ける欄', '- **3**：5番2の143.47', '- **4**：K点 → イの面積 → L点（問1）',
          '- **5**：5番3の11.33と、合筆後の154.80', '- **6**：地積測量図（問2）']:
    check('具体的な時間配分と解く順番', s)
for s in ['図11　本番で解く順番', '図7　L点の別解', '図3　注は2系統', '図2　覚書3の登記の順序']:
    check('作図スクリプトの図', s, draw, '作図')
n_fit = len(re.findall(r'\bfit\(', draw))
n_pad = len(re.findall(r'pad_aspect=True', draw))
judge(f'作図のfitがすべてpad_aspect=True（fit {n_fit}か所・pad_aspect {n_pad}か所）', n_fit == n_pad and n_fit > 0)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（11枚）', n_fig == 11)
for i in range(1, 12):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H24_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|fixed_figure\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から11まで（{sorted(nums)}）', sorted(nums) == list(range(1, 12)))
for s in ['（−8024.35, −2520.22）', '（−8025.29, −2521.12）', '43°47′43.93″', '10.4305', '11.3379535', '4.395', '73.0386',
          '0.0950…', '（−8033.30, −2510.33）', '（−8033.41, −2510.41）', '13.5248…', '1.0266…', '136°33′28″', '46°33′28″',
          '6.9429535', '143.4704', '11.3374', '154.8078', '154.8103', '153.90', '4-611', '4-612', '横約111mm・縦約113mm']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
INSERT = {1: '形は普通よ', 2: '問2の地積測量図は①、問3の申請書は⑤です', 4: 'IJはHCに直角です', 5: 'CD上にLを置くのよ',
          6: '0.1m以上、Cの側にずれてしまいます', 7: 'この高さの解き方は検算に使えばいいわ', 8: '縮尺どおりに余裕で入ります',
          9: '合筆後の地積は2筆の合計で決まるの', 10: '報告的な登記と形成的な登記の違いも、図で整理しておきます',
          11: 'L点で詰まっても、第3欄と申請書の大部分は先に点になるんですね'}
for k, s in INSERT.items():
    check(f'図{k}の挿入位置の文言', s)
    check(f'図{k}の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成何年何月何日申請　　Ａ地方法務局', '**登記の目的**：土地合筆登記', '**添付書類**：登記識別情報　印鑑証明書　代理権限証書',
          '**登録免許税**：金「1,000」円', '**申請人**：Ａ市Ｃ町六丁目４番９号　海川二郎', '**所在**：Ｄ市Ｅ町六丁目',
          '①「5番２」、②「宅地」、③「143｜47」、登記原因：空欄', '①「5番３」、②「宅地」、③「11｜33」、登記原因「5番２に合筆」',
          '①「5番２」、②「宅地」、③「154｜80」、登記原因「③5番３を合筆」',
          '「登記の目的 → 添付書類 → 登録免許税 → 申請の日付と提出先 → 申請人 → 代理人（略） → 土地の表示」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['③「153｜90」', '③「154｜81」', '「5番２に合筆」', '143.4704＋11.3374＝154.8078 → 154.80',
          '平成24年度 第21問｜5番2は143.47、合筆後は154.80', '3行目の地番・地目も、合筆後の土地の表示として書くの']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '3行目の地番・地目も、合筆後の土地の表示として書くの')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H24_dai21mon_toukishinseisho_kansei', 'H24_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h_ = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h_}px）', h_ > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H24_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H24_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成何年何月何日申請　　Ａ地方法務局', '土地合筆登記', '登記識別情報　印鑑証明書　代理権限証書', '>1,000<',
          'Ａ市Ｃ町六丁目４番９号　海川二郎', 'Ｄ市Ｅ町六丁目', '5番２', '5番３', '>143<', '>47<', '>11<', '>33<', '>154<', '>80<',
          '5番２に合筆', '③5番３を合筆', '添　付　書　類', '（略）', '①　地　番', '②　地　目', '③　地　積　㎡',
          '平成24年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
judge('完成形の画像：記入行は5行＋最下欄（答案用紙どおり）', html_k.count('<td class="chimoku">') == 5 and html_k.count('class="saika"') == 1)
judge('完成形の画像：登録免許税が申請日と申請人より上（答案用紙の順）',
      html_k.index('登録免許税') < html_k.index('平成何年何月何日申請') < html_k.index('申　　請　　人'))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '>153<', '>90<', '>81<', '143.4704＋11.3374＝154.8078 → 154.80',
          '平成24年度 第21問｜5番2は143.47、合筆後は154.80']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', '令和', '平成30年', '添付情報', '地積更正登記']:
    absent('誤記・混入・過去問集の日付・答案用紙にない項目名', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('問題文どおりの用語', '金属標')
check('問題文どおりの用語', '分割地ア')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
same = []
for i, l in enumerate(lines):
    if l.rstrip() in ('**トリ先生**', '**藍子**'):
        j = i + 2
        while j < len(lines) and (not lines[j].strip() or lines[j].startswith('> 【画像挿入】')):
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続（画像挿入マーカーをはさむものも含む）: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図11＋第1欄・第3欄2＋添削1＋完成形1＝計15か所の想定）', n_marker == 15)
n_png = len([f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png')])
judge(f'zu/ のPNGがマーカーの数だけある（{n_png}枚）', n_png == n_marker)
# マーカーの順とPNGの対応（2026-10-02追加）。マーカーの文言の頭で、記事の順にPNGと1対1に対応させる
ORDER = [('北を上にして座標どおりに描き直した全体図', 'zu01_zentaizu'), ('覚書3の登記の順序の整理図', 'zu02_touki_junjo'),
         ('注の仕分けの整理図', 'zu03_chu_shiwake'), ('K点の図', 'zu04_K_encho'), ('分割地イの面積の図', 'zu05_I_menseki'),
         ('L点の図', 'zu06_L_hirei'), ('第1欄の完成形', 'dai1ran_kansei'), ('L点の別解の図', 'zu07_L_betsukai'),
         ('地積測量図（5番1の分筆）の完成見本', 'zu08_chiseki_sokuryouzu'), ('合筆の地積の図', 'zu09_gappitsu_chiseki'),
         ('登記申請書の土地の表示の誤答', 'toukishinseisho_machigai'), ('登記申請書（問3）の完成形', 'toukishinseisho_kansei'),
         ('第3欄の完成形', 'dai3ran_kansei'), ('問4の整理図', 'zu10_chiseki_kousei'), ('本番で解く順番の図', 'zu11_toku_junban')]
markers = [l[len('> 【画像挿入】'):] for l in lines if l.startswith('> 【画像挿入】')]
judge('マーカーの順がPNGの対応表どおり', len(markers) == len(ORDER) and all(m.startswith(k) for m, (k, _) in zip(markers, ORDER)))
pngs = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
judge(f'zu/ のPNGがマーカーと1対1（{len(pngs)}枚）', sorted(f'H24_dai21mon_{v}.png' for _, v in ORDER) == pngs)
for _, v in ORDER:
    png = os.path.join(HERE, 'zu', f'H24_dai21mon_{v}.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        want = (w == 1600 and h == 1200) if v.startswith('zu') else (w == 1200 and (h > w or 'ran' in v))
        judge(f'{v}.png の大きさ（{w}×{h}px）', want)
# 第1欄・第3欄の完成形（申請書でない解答欄。2026-10-02追加）
html_1 = open(os.path.join(HERE, 'zu', 'H24_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
html_3 = open(os.path.join(HERE, 'zu', 'H24_dai21mon_dai3ran_kansei.html'), encoding='utf-8').read()
for s_ in ['第１欄', 'Ｘ座標（m）', 'Ｙ座標（m）', '<td>K点</td><td><span class="ink">−8024.35</span></td><td><span class="ink">−2520.22</span></td>',
           '<td>L点</td><td><span class="ink">−8033.30</span></td><td><span class="ink">−2510.33</span></td>']:
    check('第1欄の画像（HTML）', s_, html_1, '第1欄画像')
for lab in ['結論', '理由']:
    t_ = re.search(r'^- \*\*' + lab + r'\*\*：(.+)$', text, re.M).group(1)
    check(f'第3欄の画像（HTML）の{lab}が記事と一字一句同じ', t_, html_3, '第3欄画像')
judge('第3欄の画像：結論が理由より先（答案用紙どおり）', html_3.index('>結論<') < html_3.index('>理由<'))
for s_ in ['H24_dai21mon_dai1ran_kansei.png', 'H24_dai21mon_dai3ran_kansei.png', '「−8024.35」「−2520.22」', '「−8033.30」「−2510.33」']:
    check('完成形プロンプトの第1欄・第3欄', s_, form, '登記申請書')
for s_ in ['これで問1のK点とL点がそろったわ。第1欄に書くと、こうなるの', '第3欄に書くと、こうなるわ']:
    check('2026-10-02の画像の挿入位置の文言', s_)
# 注の書き分け（問題文の注・別紙図面の注。2026-10-02追加）
bare = [m.start() for m in re.finditer(r'注\d', text)
        if not (text[:m.start()].endswith(('問題文の', '別紙図面の', '別紙図面の下の', '『')))]  # 『注3』は番号そのものの話
judge(f'注の番号の前に「問題文の」「別紙図面の」がある（なし: {[text[p - 8:p + 2] for p in bare]}）', not bare)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成24年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成24年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
for bad in ['平成26年度', '地役権', '254', '100番5']:
    absent('見出し画像に前の年度の文言', bad, thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '登記申請書')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')

print('NG件数:', ng)
