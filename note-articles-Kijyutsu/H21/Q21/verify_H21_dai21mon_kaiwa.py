"""平成21年度 第21問（土地）会話形式note記事：記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-30に添付の過去問集〈全24ページ〉で照合。下の AGAROOT に転記）と一致することも確認する。
過去問集の問題の再掲・解答例は日付を平成30年に置き換え（建物の新築 平成30年10月3日、測量 平成30年10月20日など）、
測量成果の表に「平面直角座標系のⅡ系」の注を加えた改題版だったので、改題の要素は照合にも記事にも使わず、
日付は試験問題本文（午後の部21〜26ページ）と試験の答案用紙（平成21年8月23日作成と印刷）どおりに書いて照合する。
実行: python3 note-articles-Kijyutsu/H21/Q21/verify_H21_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, to_dms, area, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H21_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H21_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H21_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H21_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H21_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H21_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
make = open(os.path.join(HERE, 'zu', 'make_H21_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
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


# ---- 座標（測量成果） ----
T1, T2 = P(498.10, 483.60), P(500.00, 500.00)
A, B, C, D = P(500.27, 484.69), P(506.89, 484.69), P(510.27, 495.26), P(500.27, 497.76)
E, F, G = P(500.27, 482.76), P(514.91, 482.76), P(518.27, 493.26)
S1, S2 = P(500.27, 481.00), P(500.27, 501.88)
for s in ['500.27 [+] 484.69 [i] [SHIFT] [STO] [A]', '506.89 [+] 484.69 [i] [SHIFT] [STO] [B]',
          '510.27 [+] 495.26 [i] [SHIFT] [STO] [C]', '500.27 [+] 497.76 [i] [SHIFT] [STO] [D]']:
    check('座標の入力', s)
judge('道路境界 S1・E・A・D・S2 のX座標がすべて500.27', len({p.real for p in (S1, E, A, D, S2)}) == 1)
judge('EFは真北向き（Y座標が同じ）', E.imag == F.imag)
judge('CはG→D上の点', abs(((D - G).conjugate() * (C - G)).imag) < 1e-9)

# ---- 第2章 筆界点の裏付け ----
check('GC 表示', '表示：' + fmt_num(abs(C - G)))
check('CD 表示', '表示：' + fmt_num(abs(C - D)))
judge('確認書 8.25・10.31', f'{abs(C - G):.2f}' == '8.25' and f'{abs(C - D):.2f}' == '10.31')
check('Gの打ち込み', '[Abs] [ALPHA] [C] [−] [(] 518.27 [+] 493.26 [i] [)] [)] [=]')
dS = (C - A).conjugate() * (D - B)
check('乙土地 表示', '表示：' + disp(dS))
S_OTSU = abs(dS.imag) / 2
judge('乙土地の対角線の式と多角形の式が一致', abs(S_OTSU - area([A, B, C, D])) < 1e-6)
check('乙土地の面積', f'200.6734 ÷ 2 ＝ {S_OTSU:.4f}㎡。登記記録は100㎡なので、差は0.3367㎡')
judge('差0.3367は甲2の0.82の範囲、甲1 0.35でも範囲', S_OTSU - 100 < 0.82)
for s in ['精度区分は甲2で0.82㎡', '乙1の2.26㎡', '不動産登記規則第10条第4項第1号、第77条第5項']:
    check('精度区分', s)

# ---- 第3章 H点 ----
H = E + 2.50j
check('H 表示', '表示：' + disp(H))
judge('H ＝（500.27, 485.26）', H == P(500.27, 485.26))
HW = A + 2.50j
check('誤りのH', f'Hが（{HW.real:.2f}, {HW.imag:.2f}）')
check('誤りのHの通路', f'487.19 − 482.76 ＝ {HW.imag - E.imag:.2f}m')
check('今の通路', f'484.69 − 482.76 ＝ {A.imag - E.imag:.2f}m')
check('Hの電卓操作', '500.27 [+] 482.76 [i] [+] 2.50 [i] [=]')

# ---- 第4章 I点 ----
IX = B + (C - B) * 0.57 / 10.57
check('I 表示', '表示：' + disp(IX))
I = r2(IX)
judge('I の丸め', I == P(507.07, 485.26))
check('I 答え', '**▶ I点（507.07, 485.26）**')
check('I 記憶', '507.07 [+] 485.26 [i] [SHIFT] [STO] [X]')
check('B→Cの方向角', to_dms(cmath.phase(C - B)))
judge('B→Cは真数表の72°16′2″（tan 3.12724）', to_dms(cmath.phase(C - B)) == '72°16′01.67″'
      and abs(math.tan(math.radians(72 + 16 / 60 + 2 / 3600)) - 3.12724) < 1e-5)
check('0.57と10.57', '495.26 − 484.69 ＝ 10.57、BからHJまでは 485.26 − 484.69 ＝ 0.57')

# ---- 第5章 J点 ----
PX = D + (C - D) * 12.50 / 2.50
check('P 表示', '表示：' + disp(PX))
judge('P ＝ Hの真北50m', PX == H + 50)
dT = (PX - H).conjugate() * (D - H)
check('△PHD 表示', '表示：' + disp(dT))
judge('△PHD ＝ 312.5', abs(dT.imag) / 2 == 312.5 and dT.real == 0)
check('C→Dの方向角', to_dms(cmath.phase(D - C)))
judge('C→Dは真数表の165°57′50″（tan −0.25）', to_dms(cmath.phase(D - C)) == '165°57′49.52″')
k = math.sqrt((312.5 - 100.3367) / 312.5)
check('k 表示', '表示：' + fmt_num(k))
check('△PJL', f'312.5 − 100.3367 ＝ {312.5 - 100.3367:.4f}㎡')
JX = PX + (H - PX) * k
LX = PX + (D - PX) * k
check('J 表示', '表示：' + disp(JX))
J = r2(JX)
judge('J の丸め', J == P(509.07, 485.26))
check('J 答え', '**▶ J点（509.07, 485.26）**')
kw = math.sqrt((312.5 - 100) / 312.5)
JW = r2(PX + (H - PX) * kw)
check('100で出した誤りのk', f'k ＝ √((312.5 − 100) ÷ 312.5) ＝ {fmt_num(kw)}')
check('100で出した誤りのJ', f'Jは（{JW.real:.2f}, {JW.imag:.2f}）。0.03m南')
judge('誤りのJは0.03m南（X座標が小さい）', JW.real < J.real and round(J.real - JW.real, 2) == 0.03)

# ---- 第6章 L点 ----
check('L 表示', '表示：' + disp(LX))
L = r2(LX)
judge('L の丸め', L == P(509.07, 495.56))
check('L 答え', '**▶ L点（509.07, 495.56）**')
judge('LはDC上', abs(((C - D).conjugate() * (LX - D)).imag) < 1e-9)
check('L・J 記憶', '509.07 [+] 495.56 [i] [SHIFT] [STO] [F]\n509.07 [+] 485.26 [i] [SHIFT] [STO] [Y]')
check('JとLのX座標', f'X座標がどちらも{fmt_num(JX.real)}')
dq = (L - H).conjugate() * (D - J)
check('交換後の乙土地 表示', '表示：' + disp(dq))
S_AFTER = abs(dq.imag) / 2
judge('交換後の乙土地の対角線の式と多角形の式が一致（100.32）', abs(S_AFTER - area([H, J, L, D])) < 1e-6 and f'{S_AFTER:.2f}' == '100.32')
check('交換後の乙土地の面積', '200.64 ÷ 2 ＝ 100.32㎡。100.3367と0.0167')
check('台形の検算', 'HD 12.50と JL 495.56 − 485.26 ＝ 10.30 の平均に、高さ 509.07 − 500.27 ＝ 8.80 を掛けて 11.40 × 8.80 ＝ 100.32')
judge('台形 11.40 × 8.80 ＝ 100.32', abs((12.50 + 10.30) / 2 * 8.80 - 100.32) < 1e-9)

# ---- 第7章 問2 ----
KX = B + (C - B) * 2.18 / 3.38
check('K 表示', '表示：' + disp(KX))
K = r2(KX)
judge('K の丸め', K == P(509.07, 491.51))
check('K 記憶', '509.07 [+] 491.51 [i] [SHIFT] [STO] [Y]')
judge('KのX座標がJと同じ', K.real == J.real)
dR = (C - K).conjugate() * (L - K)
check('（ロ） 表示', '表示：' + disp(dR))
S_RO = abs(dR.imag) / 2
judge('（ロ） 2.43', f'{S_RO:.2f}' == '2.43' and abs(S_RO - area([K, C, L])) < 1e-6)
check('問2 答え', '**▶ 問2（ロ）部分の面積　2.43㎡**')
check('（ロ）の検算', 'KLが 495.56 − 491.51 ＝ 4.05、KLからCまでの高さが 510.27 − 509.07 ＝ 1.20 で、4.05 × 1.20 ÷ 2 ＝ 2.43')

# ---- 第8章 問3 ----
dH = (I - A).conjugate() * (H - B)
check('（ハ） 表示', '表示：' + disp(dH))
S_HA = abs(dH.imag) / 2
judge('（ハ） 3.8247 → 3.82', f'{S_HA:.4f}' == '3.8247' and chiseki(S_HA) == 3.82 and abs(S_HA - area([A, B, I, H])) < 1e-6)
check('問3 答え', '**▶ 問3（ハ）部分の面積　3.82㎡**')
check('（ハ）の台形', 'AB 6.62とHI 6.80の平均に、幅0.57を掛けて 6.71 × 0.57 ＝ 3.8247')
S_I = area([J, I, K])
judge('（イ） 6.25', f'{S_I:.2f}' == '6.25')
check('（イ）', '（イ） ＝ 2.00 × 6.25 ÷ 2 ＝ 6.25')
check('（ロ）＋（ハ）', f'（ロ）＋（ハ） ＝ 2.43 ＋ 3.8247 ＝ {2.43 + 3.8247:.4f}')
check('差0.0047', '差は0.0047㎡')

# ---- 第9章 別解 ----
QB, QC = 3.20 * 3.12724, 3.20 * 3.20 * 3.12724 / 2 - 3.8247
judge('係数 10.007168・12.1867688', f'{QB:.6f}' == '10.007168' and f'{QC:.7f}' == '12.1867688')
check('2次方程式', '0.125h² ＋ 10.007168h − 12.1867688 ＝ 0')
judge('h²の係数 (3.37724 − 3.12724) ÷ 2 ＝ 0.125', abs((3.37724 - 3.12724) / 2 - 0.125) < 1e-12)
hh = (-QB + math.sqrt(QB * QB + 4 * 0.125 * QC)) / (2 * 0.125)
check('h 表示', '表示：' + fmt_num(hh))
check('別解のJのX座標', f'510.27 − 1.1998… ＝ {fmt_num(510.27 - hh)} で、509.07')
judge('別解のJも509.07', round(510.27 - hh, 2) == 509.07)
check('√の電卓操作', '[√] [(] 10.007168 [×] 10.007168 [+] 4 [×] 0.125 [×] 12.1867688 [)] [)]')


def xj_ro_only():
    """（ハ）を足し忘れて（イ）＝（ロ）としたときのJのX座標（二分法）。"""
    lo, hi = 507.1, 510.2
    for _ in range(100):
        x = (lo + hi) / 2
        k_ = B + (C - B) * (x - B.real) / (C.real - B.real)
        l_ = D + (C - D) * (x - D.real) / (C.real - D.real)
        if area([P(x, 485.26), I, k_]) - area([k_, C, l_]) > 0:
            hi = x
        else:
            lo = x
    return lo


XW = xj_ro_only()
check('（イ）＝（ロ）の誤り', f'JのX座標は{XW:.2f}で、{J.real - XW:.2f}m南')
check('Iの丸めの差', f'Iを丸めたぶん（{fmt_num(IX.real - I.real)}m）')
for s in ['82°21′13″', '336°33′53″', '本問のどの2点の方向角とも一致しない']:
    check('使わない真数表の行', s)
# 使わない行が、本当にどの2点の方向角（逆向きも）とも合わないか
PTS_ALL = [T1, T2, A, B, C, D, E, F, G, S1, S2, H, I, J, K, L, PX]
dirs_all = [math.degrees(cmath.phase(q - p)) % 360 for p in PTS_ALL for q in PTS_ALL if p != q]
judge('82°21′13″・336°33′53″はどの2点の方向角とも一致しない',
      all(min(abs(d - t), 360 - abs(d - t)) > 0.05 for d in dirs_all
          for t in (82 + 21 / 60 + 13 / 3600, 262 + 21 / 60 + 13 / 3600, 336 + 33 / 60 + 53 / 3600, 156 + 33 / 60 + 53 / 3600)))

# ---- 第10章 問4 ----
pent = (I - H) * (K - H).conjugate() + (K - H) * (L - H).conjugate() + (L - H) * (D - H).conjugate()
check('100番1 表示', '表示：' + disp(pent))
S_REM = abs(pent.imag) / 2
judge('100番1 94.07', f'{S_REM:.2f}' == '94.07' and abs(S_REM - area([H, I, K, L, D])) < 1e-6)
check('分筆後の合計', '94.07 ＋ 2.43 ＋ 3.82 ＝ 100.32㎡。登記記録の100㎡との差は0.32㎡')
judge('分筆後の合計 100.32、差0.32 ＜ 0.82', abs(chiseki(S_REM) + chiseki(S_RO) + chiseki(S_HA) - 100.32) < 1e-9)
judge('交換後100.32 − （イ）6.25 ＝ 94.07', abs(100.32 - 6.25 - 94.07) < 1e-9)
for s in ['- **1　登記の目的**：土地地目変更登記', '- **1　登記の原因及び日付**：②③平成21年8月3日地目変更',
          '- **1　添付情報**：代理権限証明情報', '- **2　登記の目的**：土地分筆登記',
          '- **2　登記の原因及び日付**：③100番1、100番3、100番4に分筆（100番1の行）／100番1から分筆（100番3の行）／100番1から分筆（100番4の行）',
          '- **2　添付情報**：地積測量図　抵当権消滅承諾証明情報　代理権限証明情報']:
    check('問4', s)
for s in ['不動産登記事務取扱手続準則第68条第3号', '不動産登記法第37条第1項', '同準則第68条の柱書', '不動産登記規則第35条第7号',
          '不動産登記規則第100条', '準則第73条', '不動産登記令別表5の項', '同令第7条第1項第2号', '準則第72条第1項',
          '不動産登記法第41条第1号', '準則第67条第1項第4号ただし書', '不動産登記令別表8の項', '不動産登記法第40条、不動産登記規則第104条第1項第1号',
          '不動産登記令第19条', '不動産登記法第41条第6号', '登録免許税法別表第一の一の（十三）イ', '3筆で3,000円']:
    check('問4の根拠', s)
check('相続を証する情報は要らない', '相続を証する情報はいらないわよ')

# ---- 第11章 問5 地積測量図 ----
SIDES = {'AB': (A, B), 'BI': (B, I), 'IK': (I, K), 'KC': (K, C), 'CL': (C, L), 'LD': (L, D), 'DH': (D, H),
         'HA': (H, A), 'HI': (H, I), 'KL': (K, L)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
check('四捨五入の境目', f'BIは{fmt_num(abs(B - I))}で0.60、CLは{fmt_num(abs(C - L))}で1.24、KCは{fmt_num(abs(C - K))}で3.94')
for s in ['不動産登記規則第78条', '- **地番欄**：100番1、100番3、100番4', '- **土地の所在**：C市D町四丁目',
          '- **分筆後の土地**：100－1（イ）、100－3（ロ）、100－4（ハ）', '- **隣接地**：ABの西とBCの北は100－2、CDの東は99、ADの南は道路',
          'コンクリート杭はA・B・C・H（Hは新設）、金属標はD・L（Lは新設）。I・Kは計算点なので記号を書かない',
          '「C市基準点T1（X 498.10、Y 483.60）」「C市基準点T2（X 500.00、Y 500.00）」',
          '- **測量の年月日**：平成21年8月20日', '- **書かない**：各筆界点の座標値、求積及びその方法、地積（問題文の注3）',
          '系の番号がありません']:
    check('問5', s)
pts = [A, B, C, D]
xs, ys = [p.real for p in pts], [p.imag for p in pts]
check('100番1の大きさ', f'東西が約{round(max(ys) - min(ys)):d}m、南北が約{round(max(xs) - min(xs)):d}mで、横約{round((max(ys) - min(ys)) * 4):d}mm・縦約{round((max(xs) - min(xs)) * 4):d}mm')
xs2, ys2 = xs + [T1.real, T2.real], ys + [T1.imag, T2.imag]
check('基準点まで入れた大きさ', f'東西{max(ys2) - min(ys2):.2f}m・南北{max(xs2) - min(xs2):.2f}mで、横約{round((max(ys2) - min(ys2)) * 4):d}mm・縦約{round((max(xs2) - min(xs2)) * 4):d}mm')
check('答案用紙の枠', '写し（A4横）で測っても横約23cm・縦約14cm')

# ---- アガルートの解答例（2026-09-30、過去問集の解答例ページ〈108・110・111ページ〉から転記。欄・空欄ごとに全部照らす） ----
# 改題で置き換わった日付（平成30年10月3日 → 本試験 平成21年8月3日、測量 平成30年10月20日 → 平成21年8月20日）は本試験の日付に戻して照らす。
# 改題で加えられた「平面直角座標系：Ⅱ系」は照合の対象から外す。添付情報の「〜書」は答案用紙の欄の名前（添付情報）に合わせて「〜情報」と書いた。
AGAROOT = {
    '問1 I点X':             ('507.07m', '**▶ I点（507.07, 485.26）**'),
    '問1 I点Y':             ('485.26m', '**▶ I点（507.07, 485.26）**'),
    '問1 J点X':             ('509.07m', '**▶ J点（509.07, 485.26）**'),
    '問1 J点Y':             ('485.26m', '**▶ J点（509.07, 485.26）**'),
    '問1 L点X':             ('509.07m', '**▶ L点（509.07, 495.56）**'),
    '問1 L点Y':             ('495.56m', '**▶ L点（509.07, 495.56）**'),
    '問2 （ロ）部分の面積':  ('2.43㎡', '**▶ 問2（ロ）部分の面積　2.43㎡**'),
    '問3 （ハ）部分の面積':  ('3.82㎡', '**▶ 問3（ハ）部分の面積　3.82㎡**'),
    '問4 1 登記の目的':     ('土地地目変更登記', '- **1　登記の目的**：土地地目変更登記'),
    '問4 1 原因及び日付':   ('②③平成21年8月3日地目変更（改題の平成30年10月3日を本試験に戻す）', '②③平成21年8月3日地目変更'),
    '問4 1 添付情報':       ('代理権限証書', '- **1　添付情報**：代理権限証明情報'),
    '問4 2 登記の目的':     ('土地分筆登記', '- **2　登記の目的**：土地分筆登記'),
    '問4 2 原因（1行目）':  ('③100番1、100番3、100番4に分筆', '③100番1、100番3、100番4に分筆（100番1の行）'),
    '問4 2 原因（2行目）':  ('100番1から分筆', '100番1から分筆（100番3の行）'),
    '問4 2 原因（3行目）':  ('100番1から分筆', '100番1から分筆（100番4の行）'),
    '問4 2 添付（地積測量図）': ('地積測量図', '- **2　添付情報**：地積測量図'),
    '問4 2 添付（承諾）':   ('抵当権消滅承諾書', '抵当権消滅承諾証明情報'),
    '問4 2 添付（代理権限）': ('代理権限証書', '抵当権消滅承諾証明情報　代理権限証明情報'),
    '問5 地番':             ('100番1、100番3、100番4', '- **地番欄**：100番1、100番3、100番4'),
    '問5 土地の所在':       ('C市D町四丁目', '- **土地の所在**：C市D町四丁目'),
    '問5 符号':             ('100－1（イ）・100－3（ロ）・100－4（ハ）', '- **分筆後の土地**：100－1（イ）、100－3（ロ）、100－4（ハ）'),
    '問5 辺長AB':           ('6.62', '- **AB**：6.62'),
    '問5 辺長BI':           ('0.60', '- **BI**：0.60'),
    '問5 辺長IK':           ('6.56', '- **IK**：6.56'),
    '問5 辺長KC':           ('3.94', '- **KC**：3.94'),
    '問5 辺長CL':           ('1.24', '- **CL**：1.24'),
    '問5 辺長LD':           ('9.07', '- **LD**：9.07'),
    '問5 辺長DH':           ('12.50', '- **DH**：12.50'),
    '問5 辺長HA':           ('0.57', '- **HA**：0.57'),
    '問5 辺長HI':           ('6.80', '- **HI**：6.80'),
    '問5 辺長KL':           ('4.05', '- **KL**：4.05'),
    '問5 隣接地':           ('100－2・99・道路', 'ABの西とBCの北は100－2、CDの東は99、ADの南は道路'),
    '問5 境界標':           ('A、B、C、H：コンクリート杭　D、L：金属標', 'コンクリート杭はA・B・C・H（Hは新設）、金属標はD・L（Lは新設）'),
    '問5 基準点':           ('T1 C市基準点T1 498.10 483.60、T2 C市基準点T2 500.00 500.00', '「C市基準点T1（X 498.10、Y 483.60）」「C市基準点T2（X 500.00、Y 500.00）」'),
    '問5 測量の年月日':     ('平成21年8月20日（改題の平成30年10月20日を本試験に戻す）', '- **測量の年月日**：平成21年8月20日'),
    '問5 単位':             ('（単位：m）', '（単位：ｍ）'),
    '解説 乙土地の面積':    ('100.3367', '200.6734 ÷ 2 ＝ 100.3367㎡'),
    '解説 交点P・△PHD・△PJL': ('P（550.27, 485.26）、312.5、212.1633', '312.5 − 100.3367 ＝ 212.1633㎡'),
    '解説 K点':             ('509.07、491.51', 'K点は（509.07, 491.51）'),
    '解説 100番1':          ('94.07', '188.14 ÷ 2 ＝ 94.07㎡'),
    '解説 公差':            ('甲2 0.82、差 0.3247（100.3247）で地積更正不要', '甲2の公差0.82㎡の範囲だから、地積の更正はいりません'),
    '解説 地番の付け方':    ('（ロ）100番3、（ハ）100番4', '（ロ）を100番3、（ハ）を100番4にします'),
}
for k_, (ag, s) in AGAROOT.items():
    src = draw if k_ == '問5 単位' else None
    check(f'アガルートの解答例と一致（{k_}：{ag}）', s, src, '作図' if src else '記事')
naked = [m.start() for m in re.finditer(r'注[1-7]', text)
         if not text[max(0, m.start() - 2):m.start()] == '文の' and not text[m.start() - 1] == '、']
judge(f'注の番号がどの注か書き分けてある（問題文の注の列挙の行を除く）: {len(naked)}か所', not naked)
judge(f'解答例の欄の数 {len(AGAROOT)}（問1〜問5の全欄と解説の要点）', len(AGAROOT) == 42)

# ---- 改題の要素を使っていないこと ----
for src, name in [(text, '記事'), (fig, '解説図'), (form, '完成形'), (fix, '添削'), (thumb, '見出し画像'), (draw, '作図'), (make, '申請書画像')]:
    for bad in ['平成30年', 'Ⅱ系', 'II系', '改題', '10月3日', '10月20日']:
        absent('改題の要素', bad, src, name)

# ---- 最新の執筆ルールで足した内容（注の書き分け・時間配分） ----
for s in ['問題文の注1〜7と、測量成果の表の下の注の2系統', '座標は問題文の注1で', '問題文の注4の三角関数真数表', '問題文の注5の公差の表',
          '問題文の注3で小数第3位を四捨五入', '（問題文の注3）', '問5のただし書き',
          '- **問題文の注1**：座標の丸め', '- **問題文の注5**：乙土地の公差の表（市街地地域）',
          '- **測量成果の表の下の注**：「このX軸は北方向と一致している」']:
    check('注の書き分け', s)
for bad in ['（注3）', '（注5）', '座標は注1で']:
    absent('書き分けていない注', bad)
for s in ['今年いちばん時間を食うのは、J点とL点の計算と、辺長10本の地積測量図', '- **1**：問4（計算なし）',
          '- **2**：第2章の乙土地の面積100.3367㎡', '- **3**：H点とI点（問1のI）', '- **4**：問3の（ハ）3.82㎡',
          '- **5**：P点 → 相似比k → J点・L点（問1）', '- **6**：K点と問2の（ロ）2.43㎡', '- **7**：地積測量図（問5）']:
    check('具体的な時間配分と解く順番', s)
n_fit = len(re.findall(r'\bfit\(', draw))
n_pad = len(re.findall(r'pad_aspect=True', draw))
judge(f'作図のfitがすべてpad_aspect=True（fit {n_fit}か所・pad_aspect {n_pad}か所）', n_fit == n_pad and n_fit > 0)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（14枚）', n_fig == 14)
for i in range(1, 15):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H21_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|fixed_figure\(|fig\.suptitle\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から14まで（{sorted(nums)}）', sorted(nums) == list(range(1, 15)))
for s in ['（500.27, 485.26）', '（500.27, 487.19）', '4.43m', '1.93', '507.0722…', '72°16′01.67″', '（507.07, 485.26）',
          '（550.27, 485.26）', '312.5', '100.3367', '212.1633', '0.8239…', '0.8246…', '（509.07, 485.26）', '（509.04, 485.26）',
          '509.0716… ＋ 495.5595…i', '（509.07, 495.56）', '100.32', '11.40', '8.80', '（509.07, 491.51）', '491.5073…', '2.43', '4.05',
          '1.20', '3.8247', '7.6494', '6.2547', '6.25', '12.1867688', '10.007168', '1.1998…', '509.0701…', '508.70',
          '94.07', '188.14', '0.5977…', '1.2369…', '横約66mm・縦約49mm', '平成21年8月20日', '8.2462…', '10.3077…']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
INSERT = {1: '北を上にして座標どおりに描き直すと、こうなるわ', 2: '第5章でJ点を出すときにも使うから、覚えておきなさい',
          3: 'HJはY ＝ 485.26 の南北の線ですね', 4: '北へ1m進むと東へ3.12724m進む、という傾きよ', 5: '0.03m南にずれてしまいます',
          6: '11.40 × 8.80 ＝ 100.32。一致するわ', 7: '切り捨てでも四捨五入でも同じよ', 8: '面積の変動がない交換になっているわ',
          9: '165°57′50″（C→D）が合うことを確かめれば十分よ', 10: '地積の更正はいりません', 11: '地目の変更の登記はかからないわ',
          12: '分筆した後の区画と地番も、図にしておきます', 13: '縮尺どおりに余裕で入ります',
          14: 'J点で詰まっても、問4と問1のIと問3は先に点になるんですね'}
lines = text.splitlines()
marker_idx = [i for i, l in enumerate(lines) if l.startswith('> 【画像挿入】')]
for k_, s in INSERT.items():
    check(f'図{k_}の挿入位置の文言', s)
    check(f'図{k_}の挿入位置の文言（プロンプト側）', s, fig, '解説図')
    # その文言のすぐ後（空行の次）に画像挿入マーカーがあるか
    hit = [i for i, l in enumerate(lines) if s in l]
    judge(f'図{k_}のマーカーが文言の直後', bool(hit) and any(j in marker_idx for j in (hit[0] + 2, hit[0] + 3)))
for s, where in [('合筆の制限（不動産登記法第41条第6号）に引っかからないんですね', fix),
                 ('これで問1のI点・J点・L点がそろいました', form), ("答案用紙の問2の欄は『見取図(ロ)部分の面積』の1つの枠なので", form),
                 ('問3の欄も同じ形です', form), ('整理しなさい。答案用紙の問4の欄は、登記の順番の1と2の2行よ', form)]:
    check('画像の挿入位置の文言', s)
    check('画像の挿入位置の文言（プロンプト側）', s, where, 'プロンプト')

# ---- 完成形・添削のプロンプトと生成画像 ----
for s in ['I点：X座標「507.07m」、Y座標「485.26m」', 'J点：X座標「509.07m」、Y座標「485.26m」', 'L点：X座標「509.07m」、Y座標「495.56m」',
          '**問2**：「2.43㎡」', '**問3**：「3.82㎡」',
          '記入行1：登記の目的「土地地目変更登記」、登記の原因及び日付「②③平成21年8月3日地目変更」、添付情報「代理権限証明情報」',
          '記入行2：登記の目的「土地分筆登記」、登記の原因及び日付「③100番1、100番3、100番4に分筆」「100番1から分筆」「100番1から分筆」（3行）、添付情報「地積測量図」「抵当権消滅承諾証明情報」「代理権限証明情報」（3行）',
          '登記の順番｜登記の目的｜登記の原因及び日付｜添付情報']:
    check('完成形のプロンプト', s, form, '完成形')
for s in ['「②平成21年8月3日地目変更」', '「③100番1、100番3に分筆」「100番1から分筆」（2行）',
          '地目が宅地になると地積の表し方（1㎡単位→小数第2位まで）も変わるので③も付ける',
          '（ロ）と（ハ）は離れているので1筆にできない。100番1・100番3・100番4の3筆（原因は3行）',
          '分筆後の（ロ）（ハ）の1番抵当権を消す承諾書一式（不動産登記法第40条）を添付',
          '平成21年度 第21問｜地目変更は②③、分筆は3筆、抵当権消滅承諾証明情報']:
    check('添削のプロンプト', s, fix, '添削')
    if s.startswith('「') is False:
        check('添削の生成スクリプト', s, make, '申請書画像')
for name in ['H21_dai21mon_toukishinseisho_kansei_toi1', 'H21_dai21mon_toukishinseisho_kansei_toi2',
             'H21_dai21mon_toukishinseisho_kansei_toi3', 'H21_dai21mon_toukishinseisho_kansei', 'H21_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h_ = struct.unpack('>II', open(png, 'rb').read()[16:24])
        if name.endswith('machigai'):
            judge(f'{name}.png が縦長（{w}×{h_}px）', h_ > w and w == 1200)
        else:   # 1つの問の欄だけの画像（2026-10-02、問ごとに分けた）。横1200px
            judge(f'{name}.png が横1200px（{w}×{h_}px）', w == 1200 and 300 < h_ < 900)
    else:
        judge(f'{name}.png がある', False)
html = {n: open(os.path.join(HERE, 'zu', f'H21_dai21mon_toukishinseisho_{n}.html'), encoding='utf-8').read()
        for n in ['kansei_toi1', 'kansei_toi2', 'kansei_toi3', 'kansei', 'machigai']}
html_k, html_m = html['kansei'], html['machigai']
for n, ss in [('kansei_toi1', ['第21問答案用紙（その1）', '>問1<', 'I点のX座標', 'I点のY座標', 'J点のX座標', 'L点のY座標',
                               '507.07m', '509.07m', '485.26m', '495.56m', '第21問 答案用紙（その1） 問1 解答例']),
              ('kansei_toi2', ['>問2<', '見取図(ロ)部分の面積', '2.43㎡', '答案用紙（その1） 問2 解答例']),
              ('kansei_toi3', ['>問3<', '見取図(ハ)部分の面積', '3.82㎡', '答案用紙（その1） 問3 解答例']),
              ('kansei', ['>問4<', '登記の順番', '登記の原因及び日付', '添付情報', '土地地目変更登記', '②③平成21年8月3日地目変更',
                          '代理権限証明情報', '土地分筆登記', '③100番1、100番3、100番4に分筆', '100番1から分筆<br>100番1から分筆',
                          '地積測量図<br>抵当権消滅承諾証明情報<br>代理権限証明情報', '答案用紙（その1） 問4 解答例'])]:
    for s in ss:
        check(f'完成形の画像（{n}.html）', s, html[n], '完成形画像')
judge('問ごとの画像に、ほかの問の欄が入っていない',
      '見取図' not in html['kansei_toi1'] + html['kansei'] and '点のX座標' not in html['kansei_toi2'] + html['kansei_toi3'] + html['kansei']
      and '登記の順番' not in html['kansei_toi1'] + html['kansei_toi2'] + html['kansei_toi3'])
judge('完成形の画像：問4の記入行は2行', html_k.count('<td class="n">') == 2)
for s in ['①誤答', '②添削（赤ペン）', '③正解', '②平成21年8月3日地目変更', '③100番1、100番3に分筆', '抵当権消滅承諾証明情報',
          '平成21年度 第21問｜地目変更は②③、分筆は3筆、抵当権消滅承諾証明情報']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '右下', '左上', '✓', '✕', 'コンクリートくい', '令和', '添付書類']:
    absent('誤記・混入・答案用紙にない項目名', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('問題文どおりの用語', '金属標')
check('問題文どおりの用語', '物置')

# ---- note向けの体裁 ----
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
n_marker = len(marker_idx)
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図14＋添削1＋答案用紙の問ごとの欄4＝計19か所の想定）', n_marker == 19)
# 記事の画像挿入マーカーの順と zu/ のPNGの対応（マーカーの文言 → PNG）。2026-10-02 追加
ORDER = [('北を上にして座標どおりに描き直した全体図', 'H21_dai21mon_zu01_zentaizu.png'),
         ('筆界点の裏付けの図', 'H21_dai21mon_zu02_hikkai_uradzuke.png'),
         ('H点の図', 'H21_dai21mon_zu03_H_haba.png'),
         ('I点の図', 'H21_dai21mon_zu04_I_kouten.png'),
         ('J点の図', 'H21_dai21mon_zu05_J_souji.png'),
         ('L点の図', 'H21_dai21mon_zu06_L_souji.png'),
         ('答案用紙（その1）の問1の欄の完成形', 'H21_dai21mon_toukishinseisho_kansei_toi1.png'),
         ('問2の図', 'H21_dai21mon_zu07_ro_menseki.png'),
         ('答案用紙（その1）の問2の欄の完成形', 'H21_dai21mon_toukishinseisho_kansei_toi2.png'),
         ('問3と等積の図', 'H21_dai21mon_zu08_ha_toseki.png'),
         ('答案用紙（その1）の問3の欄の完成形', 'H21_dai21mon_toukishinseisho_kansei_toi3.png'),
         ('J点の別解の図', 'H21_dai21mon_zu09_J_betsukai.png'),
         ('公差の判定図', 'H21_dai21mon_zu10_kousa.png'),
         ('問4の答案の誤答→添削→正解の3コマ', 'H21_dai21mon_toukishinseisho_machigai.png'),
         ('答案用紙（その1）の問4の欄の完成形', 'H21_dai21mon_toukishinseisho_kansei.png'),
         ('問4の登記の順番の整理図', 'H21_dai21mon_zu11_touki_junban.png'),
         ('分筆後の区画と地番の図', 'H21_dai21mon_zu12_bunpitsu_chiban.png'),
         ('地積測量図（100番1の分筆）の完成見本', 'H21_dai21mon_zu13_chiseki_sokuryouzu.png'),
         ('本番で解く順番の図', 'H21_dai21mon_zu14_toku_junban.png')]
mk = [lines[i] for i in marker_idx]
judge(f'マーカーの数とPNGの対応表の数が同じ（{len(mk)}・{len(ORDER)}）', len(mk) == len(ORDER))
for n_, ((key, png_), m_) in enumerate(zip(ORDER, mk), 1):
    judge(f'マーカー{n_}「{key}」→ {png_}（記事の順）', key in m_ and os.path.exists(os.path.join(HERE, 'zu', png_)))
zu_png = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
judge(f'zu/ のPNGが対応表と過不足なし（{len(zu_png)}枚）', zu_png == sorted(p_ for _, p_ in ORDER))
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成21年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成21年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
for bad in ['平成24年度', '筆界は地積更正', '消しゴム']:
    absent('見出し画像に前の年度の文言', bad, thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '完成形')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
check('照合済みの一文', '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')

print('NG件数:', ng)
