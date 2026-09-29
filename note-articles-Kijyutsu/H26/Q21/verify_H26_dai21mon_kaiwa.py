"""平成26年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と一致することも確認する。
過去問集の問題の再掲は日付が平成30年に置き換わっていた（現況の調査 平成30年10月3日、申請 平成30年10月22日、甲区・乙区の日付も別）ので、
記事は試験問題本文と答案用紙（平成26年8月3日の現況、平成26年8月22日の申請）どおりに書き、その日付でも照合する。
実行: python3 note-articles-Kijyutsu/H26/Q21/verify_H26_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H26_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H26_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H26_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H26_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H26_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H26_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（問題文のA市基準点成果表・測量によって得られた座標） ----
T1, T2, T3 = P(256.25, 178.56), P(220.89, 168.32), P(220.72, 208.12)
A, B, C = P(223.42, 172.02), P(223.22, 199.64), P(239.65, 198.66)
for s in ['220.89 [+] 168.32 [i] [SHIFT] [STO] [X]', '220.72 [+] 208.12 [i] [SHIFT] [STO] [Y]',
          '223.42 [+] 172.02 [i] [SHIFT] [STO] [A]', '223.22 [+] 199.64 [i] [SHIFT] [STO] [B]',
          '239.65 [+] 198.66 [i] [SHIFT] [STO] [C]']:
    check('問題文の座標の入力', s)

# ---- 問1 P点（T3から放射。観測角は右回り＝足す） ----
bT2 = cmath.phase(T2 - T3)
check('arg(T2−T3)', to_dms(bT2))
check('arg(T2−T3)＋360°', to_dms(bT2 + 2 * math.pi))
check('真数表の行 270°14′41″', '真数表の270°14′41″の行')
Px = T3 + cmath.rect(35.36, bT2 + dms(45, 36, 12))
check('P 表示', '表示：' + disp(Px))
PP = r2(Px)
check('P 答え', '**▶ P点（246.09, 183.49）**')
check('P 記憶', '246.09 [+] 183.49 [i] [SHIFT] [STO] [F]')
Pw = T3 + cmath.rect(35.36, bT2 - dms(45, 36, 12))
check('反時計回りの誤りの表示', disp(Pw))
check('反時計回りの誤りの点', f'（{r2(Pw).real:.2f}, {r2(Pw).imag:.2f}）')
line_x = T2.real + (T3.real - T2.real) * (r2(Pw).imag - T2.imag) / (T3.imag - T2.imag)
check('T2・T3の線より約25m南', f'約{round(line_x - r2(Pw).real):d}m南')
judge('PはT1の南東', PP.real < T1.real and PP.imag > T1.imag)

# ---- 問2 D点・E点（Pから放射。後視はT3、方向角はarg(T3−P)） ----
bT3 = cmath.phase(T3 - PP)
check('arg(T3−P)', to_dms(bT3))
check('真数表の行 135°50′52″', '真数表の135°50′52″の行')
Dx = PP + cmath.rect(12.70, bT3 + dms(340, 52, 49))
Ex = PP + cmath.rect(7.70, bT3 + dms(72, 22, 37))
check('D 表示', '表示：' + disp(Dx))
check('E 表示', '表示：' + disp(Ex))
judge('P→Dの方向角 476°43′41.50″ − 360° ＝ 116°43′41.50″',
      to_dms(bT3 + dms(340, 52, 49) - 2 * math.pi) == '116°43′41.50″' and '116°43′41.50″' in text)
check('P→Eの方向角', to_dms(bT3 + dms(72, 22, 37)))
check('P→Eの arg', to_dms(cmath.phase(Ex - PP)))
check('真数表の行 116°43′41″・208°13′29″', '116°43′41″の行')
check('真数表の行 208°13′29″', '208°13′29″の行')
D, E = r2(Dx), r2(Ex)
check('D 答え', '**▶ D点（240.38, 194.83）**')
check('E 答え', '**▶ E点（239.31, 179.85）**')
judge('EのX座標は小数第3位が5（239.3055…）', fmt_num(Ex.real) == '239.3055…' and E.real == 239.31)
check('D 記憶', '240.38 [+] 194.83 [i] [SHIFT] [STO] [D]')
check('E 記憶', '239.31 [+] 179.85 [i] [SHIFT] [STO] [E]')
bP = bT2 + dms(45, 36, 12)                     # 第2章でT3からPへ進んだ向き（藍子が使い回す誤り）
check('T3→Pの方向角（誤りに使う向き）', to_dms(bP))
DW = r2(PP + cmath.rect(12.70, bP + dms(340, 52, 49)))
EW = r2(PP + cmath.rect(7.70, bP + dms(72, 22, 37)))
check('逆向きのD', f'Dは（{DW.real:.2f}, {DW.imag:.2f}）')
check('逆向きのE', f'Eは（{EW.real:.2f}, {EW.imag:.2f}）')
judge('逆向きのD・EはCより12m以上北', DW.real - C.real > 12 and EW.real - C.real > 12)
# 丸める前のPで回しても、D・Eの丸めた座標は同じ
judge('丸める前のPでも同じD・E', r2(Px + cmath.rect(12.70, cmath.phase(T3 - Px) + dms(340, 52, 49))) == D
      and r2(Px + cmath.rect(7.70, cmath.phase(T3 - Px) + dms(72, 22, 37))) == E)

# ---- 問2 V点・W点 ----
Vx = E + (A - E) / abs(A - E) * 3.30
Wx = C + (B - C) / abs(B - C) * 3.22
check('V 表示', '表示：' + disp(Vx))
check('W 表示', '表示：' + disp(Wx))
V, W = r2(Vx), r2(Wx)
check('V 答え', '**▶ V点（236.35, 178.39）**')
check('W 答え', '**▶ W点（236.44, 198.85）**')
check('V 記憶', '236.35 [+] 178.39 [i] [SHIFT] [STO] [X]')
check('W 記憶', '236.44 [+] 198.85 [i] [SHIFT] [STO] [Y]')
VW_ = r2(A + (E - A) / abs(E - A) * 3.30)
check('Aから測った誤りのV', f'Vは（{VW_.real:.2f}, {VW_.imag:.2f}）')
check('VとWのX座標', f'{V.real:.2f}と{W.real:.2f}')

# ---- 公差 ----
s_all = double_area_sum([A, B, C, D, E])
check('本件土地 表示', '表示：' + disp(s_all))
S = area([A, B, C, D, E])
check('本件土地 面積', f'764.8628 ÷ 2 ＝ {S:.4f}㎡')
check('差', f'差は{S - 380:.4f}㎡')
judge('乙1の5.39の範囲内・甲2の1.83は超える', S - 380 < 5.39 and S - 380 > 1.83)
check('ED 表示', '表示：' + fmt_num(abs(D - E)))
check('DC 表示', '表示：' + fmt_num(abs(C - D)))
judge('ED 15.02（地積測量図15.05と差0.03）・DC 3.90（3.89と差0.01）',
      f'{abs(D - E):.2f}' == '15.02' and f'{abs(C - D):.2f}' == '3.90')
for s in ['EDは15.02で、地積測量図の15.05との差は0.03m', 'DCは3.90で、3.89との差は0.01m', '15mの公差35cm', '3mの公差27cm',
          '不動産登記規則第77条第5項が準用する第10条第4項', '本件土地の周辺地域は、村落地に該当する']:
    check('公差の根拠', s)

# ---- 面積（（イ）（ロ）と合筆後の100番5） ----
dg = (W - A).conjugate() * (V - B)
check('（イ）対角線 表示', '表示：' + disp(dg))
a_i = area([A, B, W, V])
judge('対角線の式と多角形の式の面積が一致', abs(abs(dg.imag) / 2 - a_i) < 1e-9)
check('（イ）面積', f'628.9529 ÷ 2 ＝ {a_i:.5f}')
s_ro = double_area_sum([C, D, E, V, W])
check('（ロ）表示', '表示：' + disp(s_ro))
a_ro = area([C, D, E, V, W])
check('（ロ）面積', f'135.9084 ÷ 2 ＝ {a_ro:.4f}')
judge('（イ）314・（ロ）67', chiseki(a_i, False) == 314 and chiseki(a_ro, False) == 67)
check('切り捨て前の合計', f'314.47645 ＋ 67.9542 ＝ {a_i + a_ro:.5f}')
sk = [18.64 * 8.37 / 2, 19.40 * 9.25 / 2, 10.00 * 3.78 / 2]
check('三斜①', f'① 18.64 × 8.37 ÷ 2 ＝ {sk[0]:.4f}')
check('三斜②', f'② 19.40 × 9.25 ÷ 2 ＝ {sk[1]:.3f}')
check('三斜③', f'③ 10.00 × 3.78 ÷ 2 ＝ {sk[2]:.1f}')
check('三斜の合計', f'合計 78.0084 ＋ 89.725 ＋ 18.9 ＝ {sum(sk):.4f} → 186㎡')
go = sum(sk) + a_ro
check('合筆後の100番5', f'合筆後の100番5 ＝ 186.6334 ＋ 67.9542 ＝ {go:.4f} → {math.floor(go)}㎡')
check('誤答 186＋67', '186 ＋ 67 ＝ 253')
check('捨てた端数の合計', f'0.6334と0.9542の合計{0.6334 + 0.9542:.4f}')

# ---- 問4 申請書 ----
for s in ['- **1行目（分合筆前の100番1）**：①100番1、②雑種地、③380（答案用紙に印刷済み）、登記原因は空欄',
          '- **2行目（イ）**：①（イ）100番1、③314、登記原因「③100番5に一部合併」',
          '- **3行目（ロ）**：①（ロ）、③67、登記原因「100番1から分割して100番5に合併する部分」',
          '- **4行目（分合筆前の100番5）**：①100番5、②雑種地、③186（登記記録の地積）、登記原因は空欄',
          '- **5行目（合筆後の100番5）**：①100番5、③254、登記原因「③100番1から一部合併」',
          '- **最下欄**：地役権設定の範囲　100番5の土地　南側67平方メートル',
          '- **登記の目的**：土地分合筆登記',
          '- **申請人**：B市K町213番地　乙野二郎／B市L三丁目4番5号　甲野明子／K市B町135番地　山川次郎',
          '- **登録免許税**：金2,000円（分合筆後の土地1個につき1,000円 × 2個）',
          '- **所在**：A市B町字C（答案用紙に印刷済み）']:
    check('問4', s)
for s in ['不動産登記法第41条第6号', '不動産登記規則第105条', '承役地についてする地役権の登記', '不動産登記規則第35条第1号',
          '不動産登記令別表9の項申請情報欄ロ', '同じ別表9の項添付情報欄', '準則第76条', '不動産登記令第3条第9号',
          '登録免許税法別表第一の一の（十三）', '分筆後の2個と合筆後の1個で3,000円']:
    check('問4の根拠', s)

# ---- 問3 甲区・乙区 ----
for s in ['- **甲区**：登記の目的「合併による所有権登記」、受付年月日・受付番号「平成26年8月22日第○号」、権利者その他の事項「共有者　B市K町213番地　持分3分の1　乙野二郎　B市L三丁目4番5号　3分の1　甲野明子　K市B町135番地　3分の1　山川次郎」',
          '- **乙区**：100番1の乙区1番の地役権の登記（平成20年10月10日受付第10000号、要役地 A市B町字C102番）が移記され、地役権設定の範囲（南側67平方メートル）と地役権図面番号が記録される',
          '不動産登記規則第107条第1項。分合筆には第108条第3項で準用', '規則第107条第3項。これも第108条第3項で準用',
          '第108条第3項が準用する第104条第5項・第3項']:
    check('問3', s)

# ---- 共有者の追いかけ（試験問題本文の甲区） ----
for s in ['順位5番の『山川一郎持分全部移転』', '平成15年1月26日の相続で山川次郎さん（K市B町135番地）',
          '今の共有者は、乙野二郎さん、甲野明子さん、山川次郎さんの3人', '平成20年10月10日受付第10000号', '平成26年8月3日現在',
          '平成26年8月22日（答案用紙に印刷済み）']:
    check('試験問題本文の事実', s)

# ---- 問5 地積測量図 ----
SIDES = {'AB': (A, B), 'BW': (B, W), 'WC': (W, C), 'CD': (C, D), 'DE': (D, E), 'EV': (E, V), 'VA': (V, A), 'VW（分筆線）': (V, W)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
check('CDの四捨五入', f'CDは{fmt_num(abs(C - D))}だから3.90')
check('WCの四捨五入', f'WCは{fmt_num(abs(C - W))}で、小数第3位が5だから3.22')
check('不動産登記規則第78条', '不動産登記規則第78条')
check('答案用紙の大きさ（横）', f'横約{round((B.imag - A.imag) * 4):d}mm')
check('答案用紙の大きさ（縦）', f'縦約{round((D.real - B.real) * 4):d}mm')
check('基準点まで入れた横・縦', f'横約{round((T3.imag - T2.imag) * 4):d}mm、縦約{round((T1.real - T3.real) * 4):d}mm')
check('T1はDから16mほど北', f'T1はDから{round(T1.real - D.real):d}mほど北')
check('T3はBから9mほど南東', f'T3はBから{round(abs(T3 - B)):d}mほど南東')
check('本件土地の大きさ', f'東西が約{round(B.imag - A.imag):d}m、南北が約{round(D.real - B.real):d}m')

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記。日付は試験問題本文に戻して照合） ----
AGAROOT = ['（246.09, 183.49）', '（240.38, 194.83）', '（239.31, 179.85）', '（236.35, 178.39）', '（236.44, 198.85）',
           '合併による所有権登記', '持分3分の1　乙野二郎', '3分の1　甲野明子', '3分の1　山川次郎', '地役権設定の範囲（南側67平方メートル）と地役権図面番号',
           '土地分合筆登記', 'B市K町213番地　乙野二郎', 'B市L三丁目4番5号　甲野明子', 'K市B町135番地　山川次郎', '金2,000円',
           '③314', '③100番5に一部合併', '③67', '100番1から分割して100番5に合併する部分', '③186', '③254', '③100番1から一部合併',
           '地役権設定の範囲　100番5の土地　南側67平方メートル', '：27.62', '：13.24', '：3.22', '：3.90', '：15.02', '：3.30', '：14.41', '：20.46',
           'A・C・D・Wはコンクリート杭、B・E・Vは金属標', 'T1・T2・T3の位置と名称', '314.47645', '67.9542', '186.6334', '254.5876']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（11枚）', n_fig == 11)
for i in range(1, 12):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H26_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\()'図(\d+)　", draw)]
nums += [int(m) for m in re.findall(r"housha_fig\((\d+), ", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から11まで（{sorted(nums)}）', sorted(nums) == list(range(1, 12)))
for s in ['（246.09, 183.49）', '（195.56, 183.27）', '270°14′41.03″', '−89°45′18.97″', '135°50′52.50″', '116°43′41.50″',
          '476°43′41.50″', '208°13′29.50″', '−151°46′30.50″', '（240.38, 194.83）', '（239.31, 179.85）', '239.3055…',
          '（251.80, 172.15）', '（252.87, 187.13）', '（236.35, 178.39）', '（236.44, 198.85）', '（226.38, 173.48）',
          '382.4314', '2.4314', '15.0181…', '3.8989…', '314.47645', '67.9542', '628.9529', '135.9084', '382.43065',
          '186.6334', '254.5876', '186 ＋ 67 ＝ 253', '南側67平方メートル', '平成26年8月22日第○号', '平成20年10月10日受付第10000号',
          '横約110mm・縦約69mm', '横約159mm・縦約142mm', '3.2156…']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['北を上にして描き直すと、こうなるわ', '調査素図でT1の近くに置いた観測点と合います',
          '調査素図のDとEは本件土地と100番5の境の上なので、合いません', '調査素図の点線VWも、本件土地を北の（ロ）と南の（イ）に分けています',
          'これが次の章の山場につながるのよ', '捨てた端数の0.6334と0.9542の合計1.5876の分だけ足りなくなるんですね',
          '1件でまとめるのよ', '書き漏らさないの', 'WはBとCを結ぶ直線の上に描くのよ']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成26年8月22日　申請　Ａ地方法務局', '**登記の目的**：土地分合筆登記', '**添付情報**：（略）と印刷済み。記入しない',
          'Ｂ市Ｋ町213番地　乙野二郎', 'Ｂ市Ｌ三丁目４番５号　甲野明子', 'Ｋ市Ｂ町135番地　山川次郎', '**登録免許税**：金2,000円',
          '①「100番１」、②「雑種地」、③「380｜」', '①「（イ）100番１」、②空欄、③「314｜」、登記原因「③100番５に一部合併」',
          '①「（ロ）」、②空欄、③「67｜」、登記原因「100番１から分割して100番５に合併する部分」',
          '①「100番５」、②「雑種地」、③「186｜」', '①「100番５」、②空欄、③「254｜」、登記原因「③100番１から一部合併」',
          '**最下欄**：「地役権設定の範囲　100番５の土地　南側67平方メートル」',
          '「登記の目的 → 添付情報（略） → 申請の日付と提出先 → 申請人 → 代理人（略） → 登録免許税 → 土地の表示」',
          '「①地番」「②地目」「③地積」「登記原因及びその日付」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['「253｜」', '「254｜」', '最下欄：空欄', '186.6334＋67.9542＝254.5876 → 254', '範囲が合筆後の一部なら申請情報に書く！',
          '平成26年度 第21問｜合筆後の100番5は254㎡、地役権設定の範囲も書く', '2行目・3行目・5行目の地目の欄は空欄']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '2行目・3行目・5行目の地目の欄は空欄')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H26_dai21mon_toukishinseisho_kansei', 'H26_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H26_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H26_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成26年8月22日　申請　Ａ地方法務局', '土地分合筆登記', 'Ｂ市Ｋ町213番地　乙野二郎', 'Ｂ市Ｌ三丁目４番５号　甲野明子',
          'Ｋ市Ｂ町135番地　山川次郎', '金2,000円', 'Ａ市Ｂ町字Ｃ', '（イ）100番１', '（ロ）', '100番５', '③100番５に一部合併',
          '100番１から分割して100番５に合併する部分', '③100番１から一部合併', '>380<', '>314<', '>67<', '>186<', '>254<', '>雑種地<',
          '地役権設定の範囲　100番５の土地　南側67平方メートル', '添　付　情　報', '（略）', '①地番', '②地目', '③地積',
          '平成26年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
judge('完成形の画像：記入行は5行＋最下欄（答案用紙どおり）', html_k.count('<td class="chimoku">') == 5 and html_k.count('class="saika"') == 1)
judge('完成形の画像：登録免許税が代理人より下（答案用紙の順）', html_k.index('登録免許税') > html_k.index('代　　理　　人'))
judge('完成形の画像：添付情報が申請日より上', html_k.index('添　付　情　報') < html_k.index('平成26年8月22日'))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '>253<', '>254<', '186.6334＋67.9542＝254.5876 → 254',
          '範囲が合筆後の一部なら申請情報に書く！', '平成26年度 第21問｜合筆後の100番5は254㎡、地役権設定の範囲も書く']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', '令和', '平成30年', '添付書類', '昭和54年', '平成19年', '平成24年']:
    absent('誤記・混入・過去問集の日付・答案用紙にない項目名', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('問題文どおりの用語', '金属標')
check('問題文どおりの用語', '観測点P')

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
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図11＋添削1＋完成形1＝計13か所の想定）', n_marker == 13)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成26年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成26年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
absent('見出し画像に前の年度の文言', '平成28年度', thumb, '見出し画像')
absent('見出し画像に前の年度の文言', '取得原因', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '登記申請書')

print('NG件数:', ng)
