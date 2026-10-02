"""平成25年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と一致することも確認する。
アガルートの過去問集は日付を平成30年に置き換えている（6月21日→8月21日、8月19日→10月19日、8月23日→10月23日。
2か月後ろにずらした改題）。記事は試験問題の本文と答案用紙の印刷どおり平成25年の日付で書き、ここでは日付を戻して照合する。
実行: python3 note-articles-Kijyutsu/H25/Q21/verify_H25_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import (P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num,  # noqa: E402
                          kousa_kou2)

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H25_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H25_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H25_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H25_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H25_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H25_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（問題文の〔A市基準点成果表〕と〔測量によって得られた座標及び距離〕） ----
A100, A101, A102 = P(137.06, 159.96), P(153.30, 159.78), P(153.81, 182.84)
A, D, G = P(151.43, 162.08), P(139.19, 181.35), P(139.19, 162.08)

# ---- 問1 B点（A101から放射。観測角は時計回り＝足す） ----
check('arg(A100−A101)', to_dms(cmath.phase(A100 - A101)))
check('足した方向角', to_dms(cmath.phase(A100 - A101) + dms(278, 47, 58)))
check('1周分を引いた方向角', to_dms(cmath.phase(A100 - A101) + dms(278, 47, 58) - 2 * math.pi))
Bx = radial(A101, A100, 11.76, dms(278, 47, 58))
check('B 表示', '表示：' + disp(Bx))
B = r2(Bx)
check('B 答え', '**▶ B点（151.63, 171.42）**')
Bw = r2(radial(A101, A100, 11.76, -dms(278, 47, 58)))
check('反時計回りの誤りのB', f'（{Bw.real:.2f}, {Bw.imag:.2f}）')
judge('反時計回りのBは西の道路の先（A101より11m以上西）', Bw.imag < A101.imag - 11)
check('BがAより北', f'B点のほうが{B.real - A.real:.2f}m北')
Cx = A + (B - A) / abs(B - A) * 19.22
check('C 表示', '表示：' + disp(Cx))
C = r2(Cx)
check('C 座標', '（151.84, 181.30）')
check('A102C 表示', '表示：' + fmt_num(abs(C - A102)))
judge('A102C 2.50', f'{abs(C - A102):.2f}' == '2.50')

# ---- 問1 F点（三角形G・D・Fの正弦定理） ----
angG = math.pi - dms(5, 46, 21) - dms(166, 36, 4)
judge('∠G＝7°37′35″', to_dms(angG) == '7°37′35.00″')
check('∠Gの式', '180° − 5°46′21″ − 166°36′04″ ＝ 7°37′35″')
check('GD', f'181.35 − 162.08 ＝ {D.imag - G.imag:.2f}')
GF = abs(D - G) * math.sin(dms(5, 46, 21)) / math.sin(dms(166, 36, 4))
check('GF 表示', '表示：' + fmt_num(GF))
GFw = abs(D - G) * math.sin(angG) / math.sin(dms(166, 36, 4))
check('G点の角で計算した誤り', f'{GFw:.2f}m')
check('正弦定理のもう一つの辺', fmt_num(GFw))
Fx = G + (D - G) * math.sin(dms(5, 46, 21)) / math.sin(dms(166, 36, 4)) * cmath.rect(1, dms(7, 37, 35))
check('F 表示', '表示：' + disp(Fx))
F = r2(Fx)
check('F 答え', '**▶ F点（138.08, 170.37）**')
Fw = r2(G + (D - G) / abs(D - G) * GFw * cmath.rect(1, angG))
check('誤りのF', f'（{Fw.real:.2f}, {Fw.imag:.2f}）')
check('誤りのFのずれ', f'{Fw.imag - F.imag:.1f}m')
judge('誤りのFは本当のFより東（E点〈Y＝174.55〉の手前）', F.imag < Fw.imag < 174.55)
Fccw = r2(G + (D - G) * math.sin(dms(5, 46, 21)) / math.sin(dms(166, 36, 4)) * cmath.rect(1, -dms(7, 37, 35)))
check('反時計回りの誤りのF', f'（{Fccw.real:.2f}, {Fccw.imag:.2f}）')
judge('反時計回りのFは点線GDより北', Fccw.real > G.real)
check('DF 表示', '表示：' + fmt_num(abs(D - F)))
Ex = G + (F - G) / abs(F - G) * 12.58
check('E 表示', '表示：' + disp(Ex))
E = r2(Ex)
check('E 座標', '（137.52, 174.55）')
check('A100E 表示', '表示：' + fmt_num(abs(E - A100)))
judge('A100E 14.60', f'{abs(E - A100):.2f}' == '14.60')
check('DE 表示', '表示：' + fmt_num(abs(D - E)))

# ---- 問2 ----
for s in ['- **第2欄**：地目は、土地の主な用途による分類であり', '一筆の土地には一つの地目しか登記することができない',
          '一筆の土地の一部が別の地目になっている', '土地一部地目変更・分筆登記を申請する必要がある',
          '不動産登記法第2条第18号', '不動産登記規則第99条', '不動産登記法第39条第2項', '同法第1条', '同法第34条第1項第3号',
          '不動産登記規則第35条第7号', '同法第37条第1項', '同法第39条第1項', '同法第164条', '10万円以下の過料']:
    check('問2', s)
check('問2の誤答', '『土地地目変更登記』')

# ---- 問3 面積と申請書 ----
RO, I_ = [A, B, F, G], [B, C, D, E, F]
check('（ロ）表示', '表示：' + disp(double_area_sum(RO)))
check('（ロ）対角線 表示', '表示：' + disp((A - F).conjugate() * (B - G)))
check('（ロ）面積', f'{area(RO):.4f}㎡')
judge('（ロ）地積 113.90', chiseki(area(RO)) == 113.90)
check('（イ）表示', '表示：' + disp(double_area_sum(I_)))
check('（イ）面積', f'{area(I_):.4f}㎡')
judge('（イ）が注4の141.69730と一致', abs(area(I_) - 141.69730) < 1e-6)
judge('（イ）地積 141（雑種地）', chiseki(area(I_), takuchi=False) == 141)
check('引き算の誤り', f'255 − 141.69730 ＝ {255 - 141.69730:.2f}㎡')
tot = area([A, B, C, D, E, F, G])
check('全体の実測', f'{area(RO):.4f} ＋ {area(I_):.4f} ＝ {tot:.4f}㎡')
check('全体と登記記録の差', f'差は{tot - 255:.4f}㎡')
check('分筆後の合計', f'113.90 ＋ 141 ＝ {113.90 + 141:.2f}㎡')
check('参考の公差（甲2）', f'約{kousa_kou2(255):.2f}㎡')
judge('差が参考の公差の範囲内', tot - 255 < kousa_kou2(255))
for s in ['- **登記の目的**：土地一部地目変更・分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **申請人**：A市B町三丁目4番5号　海川二郎', '- **登録免許税**：金2,000円（分筆後の土地1個につき1,000円 × 2個）',
          '- **所在**：A市B町二丁目', '①5番、②雑種地、③255（登記記録の地積）',
          '①（イ）5番1、②空欄、③141、登記原因「平成25年6月21日一部地目変更　①③5番1、5番2に分筆」',
          '①（ロ）5番2、②宅地、③113.90、登記原因「5番から分筆」']:
    check('問3', s)
for s in ['A市B町二丁目20番1号の山川一郎さん', '『平成25年6月21日一部地目変更　③5番1、5番2に分筆』', '金1,000円']:
    check('問3の誤答', s)
for s in ['不動産登記事務取扱手続準則第67条第1項第4号', '同準則第73条', '登録免許税法別表第一の一の（十三）イ',
          '不動産登記令別表8の項', '不動産登記法第40条', '不動産登記規則第100条']:
    check('問3の条文', s)

# ---- 問4 辺長 ----
SIDES = {'AB': (A, B), 'BC': (B, C), 'CD': (C, D), 'DE': (D, E), 'EF': (E, F), 'FG': (F, G), 'GA': (G, A),
         'BF（分筆線）': (B, F)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
    if n != 'GA':
        check(f'辺長{n} 表示', '表示：' + fmt_num(abs(p - q)))
judge('AB＋BC＝19.22、EF＋FG＝12.58', f'{round(abs(B - A), 2) + round(abs(C - B), 2):.2f}' == '19.22'
      and f'{round(abs(F - E), 2) + round(abs(G - F), 2):.2f}' == '12.58')
check('答案用紙の大きさ', f'横約{round((D.imag - G.imag) * 4):d}mm・縦約{round((C.real - E.real) * 4):d}mm')
for s in ['測量年月日（平成25年8月19日）', '（イ）5－1、（ロ）5－2', 'A・C・Gはコンクリート杭、D・Eは石杭、B・Fは金属標',
          '不動産登記規則第78条', '不動産登記規則第77条第1項']:
    check('問4', s)

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記。日付は平成25年に戻した） ----
AGAROOT = ['（151.63, 171.42）', '（138.08, 170.37）', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書',
           'A市B町三丁目4番5号　海川二郎', '金2,000円', '③255', '（イ）5番1', '③141', '平成25年6月21日一部地目変更',
           '①③5番1、5番2に分筆', '（ロ）5番2', '②宅地', '③113.90', '5番から分筆',
           '**AB**：9.34', '**BC**：9.88', '**CD**：12.65', '**DE**：7.00', '**EF**：4.22', '**FG**：8.36',
           '**GA**：12.24', '**BF（分筆線）**：13.59', '（イ）5－1、（ロ）5－2', '測量年月日（平成25年8月19日）',
           '一筆の土地には一つの地目しか登記することができない', '分筆してその部分の地目を宅地に変更する']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)
judge('過去問集の置き換えた日付（平成30年）・改題の説明が記事にない（2026-09-30、ユーザー指示）', '平成30年' not in text and '過去問集' not in text)

# ---- 真数表の別解・本番で解く順番・作図範囲（2026-10-02追加） ----
T_SIN8, T_COS8, T_SIN7, T_COS7, T_SIN5, T_SIN13 = 0.14201, 0.98986, 0.13271, 0.99115, 0.10057, 0.23172
judge('tan 0°38′06″＝0.18÷16.24＝0.01108', f'{0.18 / 16.24:.5f}' == '0.01108')
dXB, dYB = 11.76 * T_SIN8, 11.76 * T_COS8
GF_T = 19.27 * T_SIN5 / T_SIN13
dXF, dYF = GF_T * T_SIN7, GF_T * T_COS7
for lab, v in [('南へ（B）', dXB), ('東へ（B）', dYB), ('GF（真数表）', GF_T), ('南へ（F）', dXF), ('東へ（F）', dYF),
               ('B X', 153.30 - dXB), ('B Y', 159.78 + dYB), ('F X', 139.19 - dXF), ('F Y', 162.08 + dYF)]:
    check(f'真数表の別解 {lab}', fmt_num(v))
judge('真数表の別解のB・Fが答えと同じ', r2(P(153.30 - dXB, 159.78 + dYB)) == B and r2(P(139.19 - dXF, 162.08 + dYF)) == F)
for s_ in ['180° − 0°38′06″ ＝ 179°21′54″', '98°09′52″で、東から南へ8°09′52″', 'sin 166°36′04″ ＝ sin 13°23′56″ ＝ 0.23172',
           '- **①**：問を先に読み、注を仕分ける', '- **②**：問2の文章（第2欄）を書き切る', '- **③**：問3の申請書の（ロ）の地積以外の欄を埋める',
           '- **⑤**：F点の正弦定理', '（イ）の141も、調査素図の注4の141.69730を1㎡未満で切り捨てれば出ます',
           '座標が要るのは（ロ）の113.90と地積測量図だけです', '横約92mm', '縦約67mm', '第4欄の枠は横約29cm・縦約21cm']:
    check('2026-10-02の追加', s_)
judge('基準点まで入れた大きさ 23.06m・16.75m', f'{(A102.imag - A101.imag) * 4:.0f}' == '92' and f'{(A102.real - A100.real) * 4:.0f}' == '67')

# ---- 第1欄・第2欄の完成形（申請書でない解答欄。2026-10-02追加） ----
html_1 = open(os.path.join(HERE, 'zu', 'H25_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
html_2 = open(os.path.join(HERE, 'zu', 'H25_dai21mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['第１欄　Ｂ点及びＦ点の座標値', 'Ｘ座標（m）', 'Ｙ座標（m）', '<td>B点</td><td><span class="ink">151.63</span></td><td><span class="ink">171.42</span></td>',
           '<td>F点</td><td><span class="ink">138.08</span></td><td><span class="ink">170.37</span></td>']:
    check('第1欄の画像（HTML）', s_, html_1, '第1欄画像')
dai2_text = re.search(r'^- \*\*第2欄\*\*：(.+)$', text, re.M).group(1)
check('第2欄の画像（HTML）見出し', '第２欄　山川一郎及び海川二郎に対して説明すべき内容', html_2, '第2欄画像')
check('第2欄の画像（HTML）が記事の文章と一字一句同じ', dai2_text, html_2, '第2欄画像')
for s_ in ['H25_dai21mon_dai1ran_kansei.png', 'H25_dai21mon_dai2ran_kansei.png', '151.63」「171.42', '138.08」「170.37',
           '山川一郎及び海川二郎に対して説明すべき内容']:
    check('完成形プロンプトの第1欄・第2欄', s_, form, '登記申請書')

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（10枚）', n_fig == 10)
for i in range(1, 11):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H25_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|fixed_figure\(|fig\.suptitle\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から10まで（{sorted(nums)}）', sorted(nums) == list(range(1, 11)))
judge('作図スクリプトの fit がすべて pad_aspect=True', all('pad_aspect=True' in l for l in draw.splitlines()
                                                         if re.match(r'\s*fit\(', l)))
for s in ['（151.63, 171.42）', '（138.08, 170.37）', '（151.84, 181.30）', '（137.52, 174.55）', '（151.37, 148.18）',
          '（137.73, 173.02）', '179°21′53.91″', '278°47′58″', '98°09′51.91″', '7°37′35″', '5°46′21″', '166°36′04″',
          '8.3638…', '113.90㎡', '141㎡', '113.30', '255.6056', '254.90', '横約77mm・縦約57mm', '平成25年8月19日',
          '横約92mm・縦約67mm', '横約29cm・縦約21cm', '0.01108', '1.6700…', '11.6407…', '8.3634…', '1.1099…', '8.2894…',
          '151.6299…', '171.4207…', '138.0800…', '170.3694…']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
    check('記事の数値', s.replace('㎡', ''), text)
# 画像挿入の位置の文言が記事にあるか
for s in ['GDが真東向きなのが、F点の計算を楽にしてくれるわ', '座標を出す前から（イ）の地積が分かるのよ',
          '2.50m！ 観測データの平面距離とぴったりです。',
          '塀がほぼ南北に通っているのも調査素図どおりです', 'どちらの解き方でも同じ点に着く、と知っておくことが大事よ',
          '距離が合えば十分よ', '登記記録と現況の違いも、図で並べておきます',
          '（ロ）の行は最初から宅地で書けるわ', '基準点まで縮尺どおりに十分入るわ',
          'F点で詰まっても、①〜④で第2欄と申請書の大部分とB点が先に点になるんですね']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成25年８月23日　申請　Ａ地方法務局', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書',
          'Ａ市Ｂ町三丁目４番５号　海川二郎', '金2,000円', 'Ａ市Ｂ町二丁目', '「255｜」', '「（イ）5番１」', '「141｜」',
          '「平成25年６月21日一部地目変更」「①③5番１、5番２に分筆」', '「（ロ）5番２」', '「113｜90」', '「5番から分筆」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['Ａ市Ｂ町二丁目20番１号　山川一郎', 'Ａ市Ｂ町三丁目４番５号　海川二郎', '「113｜30」', '「113｜90」',
          '「③5番１、5番２に分筆」', '「①③5番１、5番２に分筆」', '建物の登記記録の新築の日付で確かめられます']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '建物の登記記録の新築の日付で確かめられます')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H25_dai21mon_toukishinseisho_kansei', 'H25_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    ok = os.path.exists(png)
    if ok:
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H25_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H25_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成25年８月23日　申請　Ａ地方法務局', '土地一部地目変更・分筆登記', '地積測量図　代理権限証書',
          'Ａ市Ｂ町三丁目４番５号　海川二郎', '金2,000円', 'Ａ市Ｂ町二丁目', '>5番<', '>雑種地<', '>255<', '（イ）5番１',
          '>141<', '平成25年６月21日一部地目変更<br>①③5番１、5番２に分筆', '（ロ）5番２', '>宅地<', '>113<', '>90<',
          '5番から分筆', '（略）', '平成25年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
for s in ['①誤答', '②添削（赤ペン）', '③正解', 'Ａ市Ｂ町二丁目20番１号　山川一郎', 'Ａ市Ｂ町三丁目４番５号　海川二郎',
          '>30<', '>90<', '>①<', '申請人は所有権の登記名義人（土地の所有者）。借主・建物の所有者ではない！',
          '（イ）は分筆で変わる事項だけ。地目は変わらないので空欄、地番が変わるので①も付ける',
          '（ロ）は座標法で求積（113.9083）。255から引き算しない',
          '平成25年度 第21問｜申請人は土地の所有者、（イ）の原因は①③、（ロ）は座標法で求積']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
    if s[0] in '申（平':
        check('添削の画像とプロンプトの文言', s, fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '石くい', 'へい（', 'わく', '罠']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', '石杭')
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
        while j < len(lines) and (not lines[j].strip() or lines[j].startswith('> 【画像挿入】')):
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続（画像挿入マーカーをはさむものも含む）: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図10＋第1欄・第2欄2＋添削1＋完成形1＝計14か所の想定）', n_marker == 14)
# マーカーの順とPNGの対応（2026-10-02追加）。マーカーの文言の頭で、記事の順にPNGと1対1に対応させる
ORDER = [('北を上にして座標どおりに描き直した全体図', 'zu01_zentaizu'), ('注の仕分けの整理図', 'zu02_chu_shiwake'),
         ('A101からの放射でB点を求める図', 'zu03_B_housha'), ('三角形G・D・Fの正弦定理でF点を求める図', 'zu04_F_seigen'),
         ('三角関数真数表の値で解く別解の図', 'zu05_shinsuuhyou_betsukai'), ('第1欄の完成形', 'dai1ran_kansei'),
         ('C点とE点を延長で求め', 'zu06_C_E_uradzuke'), ('第2欄の完成形', 'dai2ran_kansei'),
         ('一筆に地目は一つの図', 'zu07_ippitsu_ichimoku'), ('分筆後の区画と地番・地目・地積の図', 'zu08_bunpitsu_chiban'),
         ('登記申請書「申請人」欄と土地の表示', 'toukishinseisho_machigai'), ('登記申請書（問3）の完成形', 'toukishinseisho_kansei'),
         ('地積測量図（5番1・5番2）の完成見本', 'zu09_chiseki_sokuryouzu'), ('本番で解く順番の図', 'zu10_toku_junban')]
markers = [l[len('> 【画像挿入】'):] for l in lines if l.startswith('> 【画像挿入】')]
judge('マーカーの順がPNGの対応表どおり', len(markers) == len(ORDER) and all(m.startswith(k) for m, (k, _) in zip(markers, ORDER)))
pngs = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
judge(f'zu/ のPNGがマーカーと1対1（{len(pngs)}枚）', sorted(f'H25_dai21mon_{v}.png' for _, v in ORDER) == pngs)
for _, v in ORDER:
    png = os.path.join(HERE, 'zu', f'H25_dai21mon_{v}.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        want = (w == 1600 and h == 1200) if v.startswith('zu') else (w == 1200 and (h > w or 'ran' in v))
        judge(f'{v}.png の大きさ（{w}×{h}px）', want)
# 注の書き分け（問題文の注・調査素図の注。2026-10-02追加）
bare = [m.start() for m in re.finditer(r'注\d', text) if not (text[max(0, m.start() - 4):m.start()] == '問題文の'
        or text[max(0, m.start() - 5):m.start()] == '調査素図の')]
judge(f'注の番号の前に「問題文の」「調査素図の」がある（なし: {[text[p - 8:p + 2] for p in bare]}）', not bare)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成25年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成25年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
absent('見出し画像に他年度の文言', '令和6年度', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')

print('NG件数:', ng)
