"""平成29年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と一致することも確認する。
実行: python3 note-articles-Kijyutsu/H29/Q21/verify_H29_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import (P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num,  # noqa: E402
                          intersect)

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H29_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H29_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H29_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H29_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H29_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H29_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


def area_disp(pts):
    s = double_area_sum(pts)
    return '表示：（実部）' + ('− ' if s.imag < 0 else '＋ ') + fmt_num(abs(s.imag)) + 'i'


# ---- 座標（問題文の〔A市基準点成果表〕と〔測量によって得られた座標値〕） ----
A201, A202 = P(365.21, 287.28), P(361.26, 307.92)
A, B, D, E, F, G = P(383.28, 289.54), P(380.12, 303.80), P(364.94, 307.17), P(368.61, 287.12), P(378.40, 300.41), \
    P(372.41, 299.32)

# ---- 問1 C点（放射。観測角は時計回り＝足す） ----
b = cmath.phase(A201 - A202)
check('arg(A201−A202)', to_dms(b))
check('arg(A201−A202)＋360°', to_dms(b + 2 * math.pi))
check('方向角＋観測角', to_dms(b + dms(85, 53, 40)))
Cx = radial(A202, A201, 17.92, dms(85, 53, 40))
check('C 表示', '表示：' + disp(Cx))
C = r2(Cx)
check('C 答え', '**▶ C点（379.06, 310.02）**')
judge('C の丸め（379.06, 310.02）', C == P(379.06, 310.02))
Cw = r2(radial(A202, A201, 17.92, -dms(85, 53, 40)))
check('反時計回りの誤りのC', f'（{Cw.real:.2f}, {Cw.imag:.2f}）')
judge(f'誤りのCはD点より約21m南（{D.real - Cw.real:.2f}m）', round(D.real - Cw.real) == 21)
check('真数表の検算 X', f'X ＝ 361.26 ＋ 17.92 × 0.99311 ＝ {361.26 + 17.92 * 0.99311:.7f}')
check('真数表の検算 Y', f'Y ＝ 307.92 ＋ 17.92 × 0.11716 ＝ {307.92 + 17.92 * 0.11716:.7f}')
judge('真数表の6°43′43″は方向角＋観測角と一致', to_dms(b + dms(85, 53, 40)).startswith('6°43′42.5'))

# ---- 問1 H点・I点（F′を通りFGに平行な直線との交点） ----
g = cmath.phase(G - F)
check('arg(G−F)', to_dms(g))
check('arg(G−F)＋360°', to_dms(g + 2 * math.pi))
check('arg(G−F)＋90°', to_dms(g + math.pi / 2))
check('arg(G−F)＋90°＋360°', to_dms(g + math.pi / 2 + 2 * math.pi))
judge('真数表の10°18′48″はFGの傾き', to_dms(g + 2 * math.pi).startswith('190°18′47.7'))
Fp = F + cmath.rect(1.0, g + math.pi / 2)
check("F′ 表示", '表示：' + disp(Fp))
Hx, tH, nH, dH = intersect(A, B, Fp, Fp + (G - F))
Ix, tI, nI, dI = intersect(E, D, Fp, Fp + (G - F))
check('H 分子 表示', '表示：' + disp(nH))
check('H 分母 表示', '表示：' + disp(dH))
check('I 分子 表示', '表示：' + disp(nI))
check('I 分母 表示', '表示：' + disp(dI))
check('H 表示（打ち込んだ比）', '表示：' + disp(A + (B - A) * 64.3421 / 88.8618))
check('I 表示（打ち込んだ比）', '表示：' + disp(E + (D - E) * 62.8476 / 124.0998))
judge('打ち込んだ比の値が表示のiの係数と一致', fmt_num(nH.imag).startswith('64.3421') and fmt_num(dH.imag) == '88.8618'
      and fmt_num(nI.imag).startswith('62.8476') and fmt_num(dI.imag) == '124.0998')
judge(f'Hは AとBの間（t＝{tH:.4f}）、Iは EとDの間（t＝{tI:.4f}）', 0 < tH < 1 and 0 < tI < 1)
H, I = r2(Hx), r2(Ix)
check('H 答え', '**▶ H点（380.99, 299.87）**')
check('I 答え', '**▶ I点（366.75, 297.27）**')
judge('H・Iの丸め', H == P(380.99, 299.87) and I == P(366.75, 297.27))
# 離れの検算
for n, p, typed in [('H', H, '6.0577'), ('I', I, '6.1101')]:
    z = (G - F).conjugate() * (p - F)
    check(f'{n}の離れの積 表示', '表示：' + disp(z))
    judge(f'{n}の離れのiの係数を{typed}と打ち込む', fmt_num(z.imag) == typed)
    check(f'{n}の離れ 表示', '表示：' + fmt_num(float(typed) / abs(G - F)))
# 真西に1.00mずらした誤り
Hn = r2(intersect(A, B, F - 1j, G - 1j)[0])
In = r2(intersect(E, D, F - 1j, G - 1j)[0])
check('誤りのH', f'H点は（{Hn.real:.2f}, {Hn.imag:.2f}）')
check('誤りのI', f'I点は（{In.real:.2f}, {In.imag:.2f}）')
judge('誤りのH・Iのずれ（Hは0.01、Iは0.02）', round(Hn.imag - H.imag, 2) == 0.01 and round(In.imag - I.imag, 2) == 0.02)
dw = abs(((G - F).conjugate() * (-1j)).imag) / abs(G - F)
check('誤りの線の離れ', f'{dw:.5f}')
judge('0.98384 は cos 10°18′48″', abs(dw - 0.98384) < 5e-6)
check('足りない長さ', f'約{round((1 - dw) * 100, 1)}cm足りない')

# ---- 問2 面積と公差 ----
ZEN, IP, RO = [A, B, C, D, E], [H, B, C, D, I], [A, H, I, E]
for n, pts in [('対象土地', ZEN), ('（イ）', IP), ('（ロ）', RO)]:
    check(f'{n} 表示', area_disp(pts))
check('対象土地 面積', f'{area(ZEN):.5f}')
check('対象土地 地積', f'{chiseki(area(ZEN)):.2f}㎡')
check('（イ）面積', f'{area(IP):.5f}で{chiseki(area(IP)):.2f}㎡')
check('（ロ）面積', f'{area(RO):.5f}で{chiseki(area(RO)):.2f}㎡')
tot = round(chiseki(area(IP)) + chiseki(area(RO)), 2)
check('分筆後の合計', f'足すと{tot:.2f}㎡')
check('合筆後の地積', f'115.70 ＋ 132.23 ＋ 49.59 ＝ {115.70 + 132.23 + 49.59:.2f}')
check('差', f'{tot:.2f} − 297.52 ＝ {tot - 297.52:.2f}㎡')
check('全体で比べた差', f'{chiseki(area(ZEN)):.2f} − 297.52 ＝ {chiseki(area(ZEN)) - 297.52:.2f}㎡')
judge('差2.32は甲2の1.57を超え、乙1の4.59は超えない', 1.57 < round(tot - 297.52, 2) < 4.59)
check('H・Iの直線からの外れ（1〜2mm）', '1〜2mm')
judge('Hの直線ABからの外れ・Iの直線EDからの外れが1〜2mm程度',
      0.0005 < abs(((B - A).conjugate() * (H - A)).imag) / abs(B - A) < 0.0025 and
      0.0005 < abs(((D - E).conjugate() * (I - E)).imag) / abs(D - E) < 0.0025)
for s in ['- **地積の更正の登記を申請することの要否**：地積の更正の登記を申請する必要がある',
          '合筆後の分筆前の地積297.52㎡を基準にした公差は1.57㎡であり、分筆後の地積の合計299.84㎡との差2.32㎡は、この公差を超えるため',
          '不動産登記事務取扱手続準則第72条第1項', '第77条第5項で準用', '297.52㎡の甲2は1.57㎡', '乙1なら4.59㎡']:
    check('問2', s)

# ---- 問3 申請書 ----
for s in ['- **登記の目的**：土地地積更正・分筆登記', '- **添付書類**：地積測量図　相続証明書　代理権限証書',
          '- **登録免許税**：金2,000円',
          '- **申請人**：（被相続人　甲野一郎）　相続人　A市B町100番地　甲野太郎　A市D町210番地　甲野次郎',
          '- **所在**：A市B町字C', '①100番、②宅地、③297.52（合筆後の登記記録の地積）、登記原因は空欄',
          '①（イ）100番1、②空欄、③146.62、登記原因「③錯誤」「①③100番1、100番2に分筆」',
          '①（ロ）100番2、②宅地、③153.22、登記原因「100番から分筆」']:
    check('問3', s)
for s in ['不動産登記規則第35条第7号', '不動産登記法第39条第1項', '不動産登記法第30条', '不動産登記令第7条第1項第4号',
          '登録免許税法別表第一の一の（十三）イ', '不動産登記事務取扱手続準則第74条第1項']:
    check('条文', s)
check('申請人の誤答', 'A市B町100番地　甲野太郎、A市D町210番地　甲野次郎と書きます')
check('分筆前の地積の誤答', '100番、宅地、115.70です！')
check('原因の誤答', '『③100番1、100番2に分筆』です')
check('登録免許税の誤答', '3,000円です')
check('添付書類の誤答', '登記識別情報と印鑑証明書も')

# ---- 問4 辺長 ----
SIDES = {'AH': (A, H), 'HB': (H, B), 'BC': (B, C), 'CD': (C, D), 'DI': (D, I), 'IE': (I, E), 'EA': (E, A),
         'HI（分筆線）': (H, I)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
check('HBの四捨五入', f'HBは{fmt_num(abs(B - H))}で、小数第3位がちょうど5だから4.03')
check('HIの四捨五入', f'HIは{fmt_num(abs(I - H))}で14.48')
check('CDの四捨五入', f'CDは{fmt_num(abs(D - C))}で14.40')
check('答案用紙の大きさ', f'横約{round((C.imag - E.imag) * 4):d}mm・縦約{round((A.real - D.real) * 4):d}mm')
check('地積測量図の地番欄', '地番の欄は『100番1、100番2』、土地の所在は『A市B町字C』')

# ---- 追加作業（2026-09-29）：別解・注の書き分け・時間配分など ----
for n, p in [('A', A), ('B', B), ('E', E), ('D', D)]:
    z = (G - F).conjugate() * (p - F)
    check(f'{n}の離れの積 表示', '表示：' + disp(z))
    check(f'{n}の離れ 表示', '表示：' + fmt_num(z.imag / abs(G - F)))
check('別解のH 表示', '表示：' + disp(A + (B - A) * (11.5680 - 1) / (11.5680 + 3.0272)))
check('別解のI 表示', '表示：' + disp(E + (D - E) * (11.3225 - 1) / (11.3225 + 9.0605)))
judge('別解のH・Iの丸めが本文と一致', r2(A + (B - A) * (11.5680 - 1) / (11.5680 + 3.0272)) == H
      and r2(E + (D - E) * (11.3225 - 1) / (11.3225 + 9.0605)) == I)
check('別解の打ち込む値（離れのiの係数）', '70.4305 [÷] [Abs]')
check('別解の打ち込む値（Bの離れ）', '0 [−] 18.4313 [÷] [Abs]')
dz = (I - A).conjugate() * (E - H)
check('（ロ）の対角線 表示', '表示：' + disp(dz))
judge('対角線の倍面積と4点の倍面積のiの係数が一致', abs(abs(dz.imag) - abs(double_area_sum(RO).imag)) < 1e-9)
check('図6のtの値（H・切り捨て）', fmt_num((11.5680 - 1) / (11.5680 + 3.0272)), draw.replace('{fmt_num(tH2)}', fmt_num((11.5680 - 1) / (11.5680 + 3.0272))), '作図')
check('図6のtの値（プロンプト）', 'H：t ＝ ' + fmt_num((11.5680 - 1) / (11.5680 + 3.0272)), fig, '解説図')
check('図6のtの値（I・プロンプト）', 'I：t ＝ ' + fmt_num((11.3225 - 1) / (11.3225 + 9.0605)), fig, '解説図')
for s in ['問題文の注3', '問題文の注4', '問題文の注5', '問題文の注6', '観測値の表の注1', '調査図素図の注',
          '毎年ほぼ同じ', '今年の答えに効く']:
    check('注の書き分け', s)
for bad in ['「注3で', '（注5）', '（注6）', '下の注1']:
    absent('どの注かわからない書き方', bad)
for s in ['3筆の間の筆界の境界標は、掘り起こしても見つからなかったのよ', '合筆の制限（不動産登記法第41条）のどれにも当たらない',
          '地積の更正が要るかどうかは、H点とI点がなくても、C点さえ出せば全体の面積だけで決まる',
          '①地域（市街地地域）→ ②精度区分（甲2）→ ③比べる2つの数字', '一郎さんの相続の登記はまだされていないので、申請日の8月18日の時点でも登記名義人は亡くなった一郎さん',
          '縦約88mm', '単位：m', 'いちばん時間を食うのは、F′を作ってH点・I点を出し',
          'H点・I点がないと書けないのは、（イ）（ロ）の地積と、AH・HB・DI・IE・HIの5本の辺長と、分筆線の位置だけです',
          '全体の面積299.83を出し、合筆後の297.52の行の甲2（1.57）と比べて、問2を書き上げる']:
    check('追加作業の内容', s)
judge('A201・A202まで入れた南北の範囲が約22m（縦約88mm）', round((A.real - A202.real) * 4) == 88)
for s in ['毎年同じ注は読み流して、今年だけの注に印を付けておけばいいんですね', 'どちらでも、最後に離れが1.00になるかの検算は忘れないこと',
          '順番を取り違えて辺どうしを掛けると、面積にならないから気をつけなさい', '次の年度も、この調子でいくわよ！']:
    check('新しい図の挿入位置の文言', s)
    check('新しい図の挿入位置の文言（プロンプト側）', s, fig, '解説図')

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記。日付は試験の答案用紙どおり平成29年8月18日） ----
AGAROOT = ['（379.06, 310.02）', '（380.99, 299.87）', '（366.75, 297.27）', '地積の更正の登記を申請する必要がある',
           '土地地積更正・分筆登記', '地積測量図　相続証明書　代理権限証書', '金2,000円', '（被相続人　甲野一郎）',
           'A市B町100番地　甲野太郎', 'A市D町210番地　甲野次郎', 'A市B町字C', '③297.52', '③146.62', '③153.22',
           '「③錯誤」「①③100番1、100番2に分筆」', '100番から分筆', '『100番1、100番2』',
           '：10.58', '：4.03', '：6.31', '：14.40', '：10.06', '：10.32', '：14.87', '：14.48',
           'A・B・C・D・Eはコンクリート杭、H・Iは金属標']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
bb = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:bb].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
N_FIG = 20
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（{N_FIG}枚）', n_fig == N_FIG)
zu_png = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.startswith('H29_dai21mon_zu') and f.endswith('.png'))
for i in range(1, N_FIG + 1):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H29_dai21mon_zu{i:02d}_') for f in zu_png))
judge(f'解説図のPNGの数 {len(zu_png)}枚（{N_FIG}枚）', len(zu_png) == N_FIG)
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\(|fixed_figure\()'図(\d+)　", draw)]
nums += [int(m) for m in re.findall(r"kouten_zu\((\d+),", draw)]
# 2026-10-08：作成済みの10枚は画像の中の文字（作成時の図番）を変えない。新しい9枚と描き直した地積測量図（作成時の図10）には図番を入れない
judge(f'作図スクリプトの作成時の図番（変えていない）が1〜9・11（{sorted(nums)}）', sorted(nums) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
new_titles = re.findall(r"board\('([^']+)'", draw)
judge(f'新しい図のタイトル（{len(new_titles)}枚）に図番がない', len(new_titles) == 9 and not any(re.search(r'図\d', t) for t in new_titles))
for s_ in ["ftext(195, 113, '第4欄'", "'地　積　測　量　図'", "'100番1、100番2'", "'Ａ市Ｂ町字Ｃ'", "'（平成29年○月○日作成）'",
           "'1／250'", "'作 成 者'", "'申 請 人'"]:
    judge(f'地積測量図を答案用紙の第4欄の書式で : {s_}', s_ in draw)
judge('地積測量図の見本のタイトルに図番がない', '図10　問4' not in draw)
for s in ['（379.06, 310.02）', '（380.99, 299.87）', '（366.75, 297.27）', '（343.95, 303.30）', '（380.99, 299.88）',
          '（366.75, 297.29）', '280°50′02.54″', '−79°09′57.46″', '6°43′42.54″', '280°18′47.75″', '85°53′40″',
          '379.0565… ＋ 310.0195…i', '380.9919… ＋ 299.8652…i', '366.7514… ＋ 297.2738…i', '64.3421 ÷ 88.8618',
          '62.8476 ÷ 124.0998', '0.98384', '297.52㎡', '299.83㎡', '146.62㎡', '153.22㎡', '299.84㎡', '±1.57', '±4.59',
          '0.9949…', '1.0035…', '横約92mm・縦約73mm', '11.5680…', '−3.0272…', '11.3225…', '−9.0605…', '306.4549',
          '153.22745㎡', '縦約88mm']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s.replace('±', '').replace('㎡', ''), draw, '作図')
# 画像挿入の位置の文言が記事にあるか
for s in ['出題者が『直角に測れ』と、こっそり教えてくれているの', 'どちらが正しいかは一目でわかるわね',
          'Gはもう使わないからYはI点に使い回すわ', '本番ではここが効いてくるわ',
          'A201は西寄り、A202は東寄りで、どちらも道路の南に描きなさい']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成29年８月18日　申請　Ａ地方法務局', '土地地積更正・分筆登記', '地積測量図　相続証明書　代理権限証書', '金2,000円',
          '（被相続人　甲野一郎）', '相続人　Ａ市Ｂ町100番地　甲野太郎', 'Ａ市Ｄ町210番地　甲野次郎', 'Ａ市Ｂ町字Ｃ',
          '③地積：「297｜52」', '③地積：「146｜62」', '③地積：「153｜22」', '「③錯誤」、2行目「①③100番１、100番２に分筆」',
          '①地番：「（イ）100番１」', '①地番：「（ロ）100番２」', '「100番から分筆」', '土地家屋調査士　法　務　民　子']:
    check('登記申請書', s, form, '登記申請書')
for s in ['Ａ市Ｂ町100番地　甲野太郎', 'Ａ市Ｄ町210番地　甲野次郎', '③「115｜70」', '③「297｜52」', '（被相続人　甲野一郎）',
          'あっ……299.84でも115.70でもなく、297.52ですね', '平成29年８月18日　申請　Ａ地方法務局']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', 'あっ……299.84でも115.70でもなく、297.52ですね')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H29_dai21mon_toukishinseisho_kansei', 'H29_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H29_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H29_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成29年８月18日　申請　Ａ地方法務局', '土地地積更正・分筆登記', '地積測量図　相続証明書　代理権限証書', '金2,000円',
          '（被相続人　甲野一郎）', '相続人　Ａ市Ｂ町100番地　甲野太郎', 'Ａ市Ｄ町210番地　甲野次郎', 'Ａ市Ｂ町字Ｃ', '>100番<',
          '（イ）100番１', '（ロ）100番２', '③錯誤', '①③100番１、100番２に分筆', '100番から分筆', '>297<', '>52<', '>146<',
          '>62<', '>153<', '>22<', '（略）', '法 務　民 子', '平成29年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
for s in ['①誤答', '②添削（赤ペン）', '③正解', 'Ａ市Ｂ町100番地　甲野太郎', 'Ａ市Ｄ町210番地　甲野次郎', '>115<', '>70<',
          '>297<', '>52<', '（被相続人　甲野一郎）', '登記名義人は亡くなった甲野一郎。相続人が法第30条で申請する！',
          '分筆するのは合筆した後の100番。地積は3筆の合計297.52',
          '平成29年度 第21問｜申請人は被相続人と相続人2人、分筆前の地積は合筆後の297.52']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
    if s.startswith('登記名義人') or s.startswith('分筆') or s.startswith('平成29年度 第21問'):
        check('添削の画像とプロンプトの文言', s, fix, '添削')

# ---- 日付（アガルートの過去問集の再掲は平成30年10月18日。試験の答案用紙どおり平成29年8月18日） ----
check('申請日', '申請は平成29年8月18日')
for src, name in [(text, '記事'), (form, '登記申請書'), (fix, '添削'), (html_k, '完成形画像'), (html_m, '添削画像')]:
    absent('過去問集の再掲の日付', '平成30年', src, name)

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '代位者']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')

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
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋第1欄・第2欄の完成形2＋添削1＋申請書の完成形1）', n_marker == N_FIG + 4)
all_png = [f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png')]
judge(f'画像挿入マーカーの数とzu/のPNGの数が一致（{n_marker}・{len(all_png)}）', n_marker == len(all_png))
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成29年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成29年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('見出し画像の半角英字の例外', 'the Latin\nletter "m" (meters)', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')

PNGS = [('H29_dai21mon_zu01_zentaizu', '全体図', 'fig'),
        ('H29_dai21mon_zu02_gappitsu_riyuu', '先に合筆してから分筆する理由の図', 'fig'),
        ('H29_dai21mon_zu03_chuu_shiwake', '注の仕分けの図', 'fig'),
        ('H29_dai21mon_zu04_C_housha', 'C点を求める図', 'fig'),
        ('H29_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('H29_dai21mon_zu05_H_kouten', 'H点の求め方の図', 'fig'),
        ('H29_dai21mon_zu06_I_kouten', 'I点の求め方の図', 'fig'),
        ('H29_dai21mon_zu07_HI_betsukai', 'H点・I点の別解の図', 'fig'),
        ('H29_dai21mon_zu08_ro_taikakusen', '対角線で出す図', 'fig'),
        ('H29_dai21mon_zu09_kousa_hyou_gyou', '公差の表の行の図', 'fig'),
        ('H29_dai21mon_zu10_kousa', '公差の判定図', 'fig'),
        ('H29_dai21mon_dai2ran_kansei', '第2欄（問2）の完成形', 'wide'),
        ('H29_dai21mon_zu11_ikkatsu_shinsei', '一の申請情報の図', 'fig'),
        ('H29_dai21mon_zu12_shinseinin', '申請人の図', 'fig'),
        ('H29_dai21mon_zu13_bunpitsumae_chiseki', '土地の表示の1行目の図', 'fig'),
        ('H29_dai21mon_toukishinseisho_machigai', '誤答→添削→正解', 'tall'),
        ('H29_dai21mon_zu14_genin_13', '（イ）の行の登記原因の図', 'fig'),
        ('H29_dai21mon_zu15_tenpu_shorui', '添付書類の図', 'fig'),
        ('H29_dai21mon_zu16_tourokumenkyozei', '登録免許税の図', 'fig'),
        ('H29_dai21mon_zu17_bunpitsu_chiban', '分筆後の区画と地番の図', 'fig'),
        ('H29_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('H29_dai21mon_zu18_chiban_ran', '地積測量図の地番の欄の図', 'fig'),
        ('H29_dai21mon_zu19_chiseki_sokuryouzu', '地積測量図（100番1、100番2）の完成見本', 'fig'),
        ('H29_dai21mon_zu20_toku_junban', '本番で解く順番の図', 'fig')]
# ---- まとめのわな → 図（2026-10-08追加。執筆指示書「記事で藍子が誤答する論点（わな）にも、図を1枚ずつ」） ----
TRAPS = [('C点は時計回りに足す', 'A202からの放射でC点を求める図'),
         ('1.00m離れた線は直角に測る', 'H点の求め方の図'),
         ('交点はConjgの積のiの係数の比', 'H点・I点の別解の図'),
         ('合筆してから分筆する理由', '先に合筆してから分筆する理由の図'),
         ('公差は合筆後の297.52で比べる', '公差の表の行の図'),
         ('精度区分は地域で決まる', '公差の判定図'),
         ('登記の目的は土地地積更正・分筆登記', '一の申請情報の図'),
         ('申請人は被相続人と相続人2人', '申請人の図'),
         ('分筆前の行は297.52', '土地の表示の1行目の図'),
         ('（イ）の原因は「③錯誤」「①③100番1、100番2に分筆」', '（イ）の行の登記原因の図'),
         ('添付書類は3つ', '添付書類の図'),
         ('登録免許税は2,000円', '登録免許税の図'),
         ('地積測量図の地番は「100番1、100番2」', '地積測量図の地番の欄の図')]
matome_ = text[text.index('## 第7章'):]
traps_ = re.findall(r'^- \*\*(.+?)\*\*：', matome_, re.M)
judge(f'まとめのわなの数と対応表の数（{len(traps_)}・{len(TRAPS)}）', len(traps_) == len(TRAPS))
for t_, m_ in TRAPS:
    judge(f'わな「{t_}」がまとめにあり、図「{m_}」が記事にある', t_ in traps_ and any(m_ in l_ for l_ in text.splitlines() if l_.startswith('> 【画像挿入】')))
# ---- 電卓のキー列を順に実行して表示と比べる（2026-10-08追加。別解でYにI点が入っているのにGとして使っていた誤りを見つけた） ----
import subprocess  # noqa: E402
ks_ = subprocess.run([sys.executable, os.path.join(HERE, '..', '..', 'tools', 'keysim_note_article.py'),
                      os.path.join(HERE, 'note_H29_dai21mon_tochi_kaiwa_kaisetsu.md')], capture_output=True, text=True).stdout
judge('電卓のキー列の再現（keysim_note_article.py）がNG 0件', 'NG件数: 0' in ks_)
absent('別解でYをGとして使う誤り', '電卓はF′を作る前（Y＝G）から始めるわ')
check('別解のG − Fの打ち込み', '[Apps] [4] 0 [−] 5.99 [−] 1.09 [i] [)] [×] [(] [ALPHA] [A] [−] [ALPHA] [F] [)] [=]')
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


after_('第1欄（問1）の完成形', '**▶ I点（366.75, 297.27）**')
after_('第2欄（問2）の完成形', '根拠の条文（準則第72条第1項）も最後に添えておきます')
html_1 = open(os.path.join(ZU, 'H29_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
html_2 = open(os.path.join(ZU, 'H29_dai21mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['第１欄　Ｃ点，Ｈ点及びＩ点の座標値', 'Ｘ座標（m）', 'Ｙ座標（m）', '>379.06<', '>310.02<', '>380.99<', '>299.87<',
           '>366.75<', '>297.27<', '第1欄（問1）解答例']:
    check('第1欄の画像（HTML）', s_, html_1, '第1欄画像')
for s_ in ['第２欄　地積の更正の登記を申請することの要否及びその理由について', '地積の更正の登記を申請することの要否',
           '>地積の更正の登記を申請する必要がある<', '要否の理由',
           '合筆後の分筆前の地積297.52㎡を基準にした公差は1.57㎡であり、分筆後の地積の合計299.84㎡との差2.32㎡は、この公差を超えるため',
           '第2欄（問2）解答例']:
    check('第2欄の画像（HTML）', s_, html_2, '第2欄画像')
for s_ in ['Ｃ点「379.06」「310.02」、Ｈ点「380.99」「299.87」、Ｉ点「366.75」「297.27」', '「地積の更正の登記を申請する必要がある」',
           'public/kijutsu/H29-tochi/a1.webp']:
    check('第1欄・第2欄の画像のプロンプト', s_, form, '登記申請書')
# 法改正（3-0：法定相続情報番号）：答えは「相続証明書」のまま、今の法令の注を記事・プロンプト・画像にそろえる
NOTE_ = ('相続証明書は、今は法定相続情報一覧図の写し又は法定相続情報番号の提供で代えることもできる'
         '（不動産登記規則第37条の3第1項）。出題当時は法定相続情報番号の制度がなかった')
check('法定相続情報番号の注（記事）', '今は、法定相続情報一覧図の写し又は法定相続情報番号を提供して、相続証明書に代えることもできる（不動産登記規則第37条の3第1項。出題当時は法定相続情報番号の制度がなかった）')
check('法定相続情報番号の注（プロンプト）', NOTE_, form, '登記申請書')
check('法定相続情報番号の注（完成形の画像）', NOTE_, html_k, '完成形画像')
check('問題文の注6の書き分け', '問題文の注6でA201・A202も描くから')
absent('どの注か分からない書き方（解説図プロンプトの差し替えデータ）', '（注3）', fig[fig.index('## 差し替えデータ'):], '解説図')
absent('どの注か分からない書き方（登記申請書プロンプト）', '不要（注9）', form, '登記申請書')

print('NG件数:', ng)
