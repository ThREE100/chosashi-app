"""平成23年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-30に添付の過去問集〈全22ページ、画面の撮影画像〉で照合。下の AGAROOT に転記）と一致することも確認する。
アガルートの再掲は改題で、日付や問題文の注5などを書き換えていた。改題で加えられた要素（書き換えた注5とそれに由来する添付書類の
「登記事項証明書」・会社法人等番号、置き換えた日付など）は、アガルート独自の教材なので照合にも記事にも使わない（2026-09-30、ユーザー指示）。
記事は試験問題の本文の注5どおり、資格証明書を書かない答えとした（下の KAIDAI で、改題の要素が記事にないことを確かめる）。
実行: python3 note-articles-Kijyutsu/H23/Q21/verify_H23_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H23_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H23_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H23_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H23_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H23_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H23_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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
T1, T2, T3 = P(309.14, 292.20), P(300.12, 306.99), P(299.47, 333.78)
D, E, F, G = P(320.31, 309.24), P(326.52, 315.34), P(323.58, 334.66), P(302.56, 332.88)
I, J, L = P(312.05, 313.06), P(303.18, 315.34), P(303.65, 302.14)

# ---- 放射 A・M・K（観測角の向きの注はない → 時計回りとして扱い、見取図の位置で確かめる） ----
b12 = cmath.phase(T2 - T1)
check('arg(T2−T1)', to_dms(b12))
check('T1→T2 ＋ 150°21′44″', to_dms(b12 + dms(150, 21, 44)))
Ax = radial(T1, T2, 15.120, dms(150, 21, 44))
check('A 表示', '表示：' + disp(Ax))
A = r2(Ax)
check('A 答え', '**▶ A点（309.60, 277.09）**')
AW = r2(T1 + cmath.rect(15.120, b12 - dms(150, 21, 44)))
check('Aの反時計回りの誤り', f'（{AW.real:.2f}, {AW.imag:.2f}）')
check('A′はT1から北へ13m', f'T1から北へ{round(AW.real - T1.real)}m')
judge('真数表の1°44′24″（271°44′24″ − 270°）', to_dms(b12 + dms(150, 21, 44) - math.radians(270)).startswith('1°44′24'))
Mx = radial(T1, T2, 6.613, dms(324, 2, 29))
check('M 表示', '表示：' + disp(Mx))
M = r2(Mx)
check('M 答え', '**▶ M点（309.67, 298.79）**')
check('M 方向角（360°超）', to_dms(b12 + dms(324, 2, 29)))
check('M 方向角−360°', to_dms(b12 + dms(324, 2, 29) - 2 * math.pi))
MW = r2(T1 + cmath.rect(6.613, b12 - dms(324, 2, 29)))
check('Mの反時計回りの誤り', f'（{MW.real:.2f}, {MW.imag:.2f}）')
judge('M′はA→Mの線より6m以上南', M.real - MW.real > 6)
check('AM 表示', '表示：' + fmt_num(abs(M - A)))
judge('AM ＝ 21.70（51番3の地積測量図の底辺）', f'{abs(M - A):.2f}' == '21.70')
b23 = cmath.phase(T3 - T2)
check('arg(T3−T2)', to_dms(b23))
Kx = radial(T2, T3, 5.067, dms(319, 7, 54))
check('K 表示', '表示：' + disp(Kx))
K = r2(Kx)
check('K 答え', '**▶ K点（303.34, 310.90）**')
check('K 方向角（360°超）', to_dms(b23 + dms(319, 7, 54)))
check('K 方向角−360°', to_dms(b23 + dms(319, 7, 54) - 2 * math.pi))
KW = r2(T2 + cmath.rect(5.067, b23 - dms(319, 7, 54)))
check('Kの反時計回りの誤り', f'（{KW.real:.2f}, {KW.imag:.2f}）')
judge('K′はT2より南', KW.real < T2.real)
check('KがG→Lの上 表示', '表示：' + disp((L - G).conjugate() * (K - G)))
check('△GLKの面積', f'三角形GLKの面積は{abs(((L - G).conjugate() * (K - G)).imag) / 2:.4f}㎡')

# ---- 問2 C点（51番3の地積測量図の三斜と、ABとEMの平行。面積の比） ----
v = (E - M).conjugate() * (A - M)
check('△AMEの倍面積 表示', '表示：' + disp(v))
judge('157.3309 ＝ 16.27 × 9.67', f'{16.27 * 9.67:.4f}' == '157.3309')
judge('314.867 ＝ 21.70 × 14.51', f'{21.70 * 14.51:.3f}' == '314.867')
Cx = M + (E - M) * 157.3309 / 364.4865
check('C 表示', '表示：' + disp(Cx))
C = r2(Cx)
check('C 答え', '**▶ C点（316.94, 305.93）**')
check('MC 表示', '表示：' + fmt_num(abs(C - M)))
check('MCと塀の差（14cm）', f'10.05mより{round((abs(C - M) - 10.05) * 100)}cm長い')
Bx = A + (E - M) * 314.867 / 364.4865
check('BM 表示', '表示：' + fmt_num(abs(Bx - M)))
judge('BM ＝ 16.27（三斜の対角線）・Bから直線AMまで14.51',
      f'{abs(Bx - M):.2f}' == '16.27' and f'{abs(((M - A).conjugate() * (Bx - A)).imag) / abs(M - A):.2f}' == '14.51')
CW = r2(M + (E - M) / abs(E - M) * 10.05)
check('ブロック塀の10.05mのC′', f'（{CW.real:.2f}, {CW.imag:.2f}）')
check('C′はMに0.14m寄る', f'{abs(C - CW):.2f}mだけMに寄る')
check('方向角 M→E（真数表44°29′07″）', to_dms(cmath.phase(E - M))[:8])
check('方向角 A→M（真数表89°48′55″）', '89°48′55″')
judge('A→Mの方向角は89°48′54.63″（真数表の89°48′55″）', to_dms(cmath.phase(M - A)) == '89°48′54.63″')
judge('M→Eの方向角は44°29′07.37″（真数表の44°29′07″）', to_dms(cmath.phase(E - M)) == '44°29′07.37″')
h_tbl = 21.70 * 0.71116
check('真数表の別解 h', f'h ＝ 21.70 × 0.71116 ＝ {math.floor(h_tbl * 1e4) / 1e4:.4f}…')
check('真数表の別解 MC', f'MC ＝ 157.3309 ÷ 15.4321… ＝ {math.floor(157.3309 / h_tbl * 1e4) / 1e4:.4f}…')
check('Conjgで出したMC（丸める前）', f'{math.floor(abs(Cx - M) * 1e4) / 1e4:.4f}…')
judge('真数表の別解のCも丸めると同じ', r2(M + (E - M) / abs(E - M) * 157.3309 / h_tbl) == C)
y = math.asin(14.51 / 16.27)
ame = math.pi - (cmath.phase(M - A) - cmath.phase(E - M))
x = ame - y
mc_alt = 9.67 / math.sin(x)
check('三斜の角度の別解 ∠AMB 約63°06′', '約63°06′')
judge('∠AMB は約63°06′', to_dms(y).startswith('63°06′'))
judge('∠AME ＝ 180° − 45°19′48″ ＝ 134°40′12″', abs(math.degrees(ame) - (134 + 40 / 60 + 12 / 3600)) < 1 / 3600)
judge('∠BMC は約71°34′', to_dms(x).startswith('71°34′') or to_dms(x).startswith('71°33′'))
check('三斜の角度の別解 MC', f'{math.floor(mc_alt * 1e4) / 1e4:.4f}…')
judge('三斜の角度の別解のCも丸めると同じ', r2(M + (E - M) / abs(E - M) * mc_alt) == C)

# ---- 問2 H点（E→Jは真南、交点から120°の向きに6.836m） ----
check('E − J 表示', '表示：' + fmt_num((E - J).real))
judge('E − J はiの係数0（真南）', abs((E - J).imag) < 1e-9)
PX = E - 9.732
check('交点', f'（{PX.real:.3f}, {PX.imag:.2f}）')
check('arg(交点−D) 表示', '表示：' + to_dms(cmath.phase(PX - D)))
Hx = PX + cmath.rect(6.836, dms(120))
check('H 表示', '表示：' + disp(Hx))
H = r2(Hx)
check('H 答え', '**▶ H点（313.37, 321.26）**')
HW = r2(D + cmath.rect(6.836, dms(120)))
check('Dから6.836mの誤り', f'（{HW.real:.2f}, {HW.imag:.2f}）')
check('誤りの点と交点の距離', f'交点から{abs(HW - PX):.2f}mしか離れていない')
check('真数表の30°で検算', f'6.836 × 0.86602 ＝ {math.floor(6.836 * 0.86602 * 1e4) / 1e4:.4f}…')
check('予備校の解き方の表示（Dから交点への向き）', disp(PX + (PX - D) / abs(PX - D) * 6.836))
judge('予備校の解き方でも丸めると同じH', r2(PX + (PX - D) / abs(PX - D) * 6.836) == H)

# ---- 問3 面積・地積 ----
HONKEN = [C, D, H, J, K, I]
check('本件土地 表示', '表示：' + disp(double_area_sum(HONKEN)))
a = area(HONKEN)
check('本件土地 面積', f'227.75 ÷ 2 ＝ {a:.3f}')
judge('境内地は1㎡未満切捨てで113', chiseki(a, False) == 113)
check('宅地と誤った113.87', f'{chiseki(a, True):.2f}')
aw = area([CW, D, H, J, K, I])
check('C′で囲んだ面積', f'{aw:.3f}㎡')
judge('C′だと114', chiseki(aw, False) == 114)
check('地積の答え', '**▶ 本件土地の地積　113㎡（113.875）**')

# ---- 問4 辺長 ----
SIDES = {'CD': (C, D), 'DH': (D, H), 'HJ': (H, J), 'JK': (J, K), 'KI': (K, I), 'IC': (I, C)}
for n, (p, q) in SIDES.items():
    val = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{val}')
    check(f'辺長{n} 表示', '表示：' + fmt_num(abs(q - p)))
    check(f'図の辺長{n}', val, fig, '解説図')
check('ICの四捨五入', f'ICは{math.floor(abs(C - I) * 1e4) / 1e4:.4f}…だから')
check('答案用紙の大きさ 本件土地の横', f'横約{round((H.imag - C.imag) * 4)}mm')
check('答案用紙の大きさ 本件土地の縦', f'縦約{round((D.real - J.real) * 4)}mm')
check('基準点まで入れた横', f'横約{round((T3.imag - C.imag) * 4)}mm')
check('基準点まで入れた縦', f'縦約{round((D.real - T3.real) * 4)}mm')
check('土地所在図の大きさ', f'横約{round((H.imag - C.imag) * 2)}mm・縦約{round((D.real - J.real) * 2)}mm')

# ---- 問1・問3・問4 の文言 ----
for s in ['- **問1の答え**：本件土地は国有財産であり、宗教法人雨堤天満宮にとって他人の物である。',
          '所有の意思をもって維持、管理し、一般に開放してきた', '平穏かつ公然と占有していた',
          'この占有を昭和26年8月19日から20年間継続し、昭和46年8月19日に取得時効が完成した（民法第162条第1項）',
          '- **登記の目的**：土地表題登記', '- **添付書類**：土地所在図　地積測量図　所有権証明書　会社法人等番号　代理権限証書（出題当時は会社法人等番号の制度がなく、住所証明書を付け、資格証明書は問題文の注5で不要）',
          '- **申請人**：A市B町五丁目50番地1　宗教法人雨堤天満宮　代表役員　荒牧英雄', '- **所在**：A市B町五丁目',
          '- **1行目**：①地番は空欄、②境内地、③113、登記原因及びその日付「不詳」']:
    check('答え', s)
for s in ['民法第162条', '民法第144条', '不動産登記令第7条第1項第1号イ', '不動産登記令第9条、不動産登記規則第36条第4項', '不動産登記法第36条', '同法第74条第1項第1号', '不動産登記事務取扱手続準則第68条第13号',
          '宗教法人法第3条第2号及び第3号', '不動産登記規則第100条', '不動産登記令別表4の項添付情報欄ハ', '不動産登記令別表4の項添付情報欄ニ',
          '登録免許税法第2条',
          '不動産登記令第3条第7号ロ', '同条第2号', '不動産登記規則第76条第2項', '同規則第77条第4項',
          '不動産登記事務取扱手続準則第51条第4項', '準則第51条第3項', '不動産登記規則第76条第1項']:
    check('条文', s)

# ---- アガルートの解答例（2026-09-30、過去問集の解答例ページから転記）と一致するか ----
AGAROOT = ['（316.94, 305.93）', '（313.37, 321.26）', '土地表題登記', '所有権証明書',
           '代理権限証書', 'A市B町五丁目50番地1　宗教法人雨堤天満宮　代表役員　荒牧英雄', '境内地', '③113', '「不詳」',
           '- **CD**：4.72', '- **DH**：13.88', '- **HJ**：11.78', '- **JK**：4.44', '- **KI**：8.97', '- **IC**：8.65',
           '国有財産', '所有の意思', '平穏かつ公然', '20年間', 'C・D・H・Iはコンクリート杭', '50－2', '50－1', '51－3', '51－2',
           '縮尺　1／500', 'T2・T3の位置と名称と座標値']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)
# 改題で加えられた要素（アガルート独自の教材）：記事・付属プロンプト・作図に入れない（2026-09-30、ユーザー指示）
KAIDAI = ['昭和30年10月19日', '平成30年', '登記事項証明書', '商業登記', '改題', '北野一郎', '昭和50年']
for src, name in [(text, '記事'), (fig, '解説図'), (form, '登記申請書'), (fix, '添削'), (thumb, '見出し画像'), (draw, '作図')]:
    for w in KAIDAI:
        absent('改題で加えられた要素', w, src, name)
check('照合済みの一文', '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')

# ---- 付属プロンプトとの整合 ----
a0 = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b0 = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a0:b0].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
N_FIG = 13
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))   # 2桁の図番号も数える
judge(f'解説図プロンプトの図の数 {n_fig}枚（{N_FIG}枚）', n_fig == N_FIG)
for i in range(1, N_FIG + 1):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H23_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|fixed_figure\(|housha_figure\(\n?\s*\d+, '\w+', )'図(\d+)　", draw)]
nums += [int(m) for m in re.findall(r"^\s+\d+, '\w+', '図(\d+)　", draw, re.M)]
nums = sorted(set(nums))
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, N_FIG + 1)))
fits = re.findall(r'^\s*fit\((.*)', draw, re.M)
judge(f'作図スクリプトのfitはすべて pad_aspect=True（{len(fits)}か所）',
      fits and all('pad_aspect=True' in f or 'pad_aspect=True' in draw[draw.index(f):draw.index(f) + 300] for f in fits))
for s in ['（309.60, 277.09）', '（309.67, 298.79）', '（303.34, 310.90）', '（316.94, 305.93）', '（313.37, 321.26）',
          '（322.37, 284.87）', '（303.04, 294.75）', '（296.71, 310.74）', '（316.84, 305.83）', '（316.89, 315.16）',
          '（316.788, 315.34）', '121°22′40.17″', '91°23′23.58″', '150°21′44″', '324°02′29″', '319°07′54″',
          '445°25′09.17″', '410°31′17.58″', '157.3309 ÷ 364.4865', '16.2681…', '113.875', '114.479', '120°00′04.14″',
          '676.5154 ＋ 0.019i', '0.21m', '0.14m', '15.4321…', '10.1949…', '10.1929…', '134°40′12″', '8.6457…']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['北を上にして描き直すと、こうなるわ', 'この図を信じて、あとでC点を出すのよ',
          '問題文の『J点及びK点は、G点とL点を結ぶ直線上の点』のとおりね',
          '51番3の地積測量図は、底辺21.70も対角線16.27も今回の座標と合っています', '塀の長さを優先する理由はないわ',
          '真数表の角度は、自分の方向角が合っているかの答え合わせに使うのよ', 'それを使うのが素直よ', 'これが骨組みよ',
          '無番地だから、地番は書かないわ', '隣の50番1や51番3との位置関係が分かるように描くのよ', '次の年度も、この調子でいくわよ！']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成23年8月21日申請　Ａ地方法務局', '土地表題登記', '土地所在図　地積測量図　所有権証明書　会社法人等番号　代理権限証書',
          'Ａ市Ｂ町五丁目50番地１　宗教法人雨堤天満宮　代表役員　荒牧英雄', 'Ａ市Ｂ町五丁目',
          '①空欄、②「境内地」、③「113｜」（小数部は空欄）、登記原因「不詳」', '**記入行2**：空欄', '**記入行3**：空欄',
          '「登記の目的 → 添付書類 → 申請の日付と提出先 → 申請人 → 代理人 → 土地の表示」',
          '「①地番」「②地目」「③地積　m²」「登記原因及びその日付」', '登録免許税の欄がない']:
    check('登記申請書', s, form, '登記申請書')
for s in ['資格証明書', '「宅地」', '「113｜87」', '「昭和26年8月19日時効取得」', '「境内地」', '「不詳」',
          '今の法令では会社法人等番号（出題当時は住所証明書を付け、資格証明書は注5で不要）', '境内地は1㎡未満切捨て、原因は土地が生じた原因の不詳',
          '平成23年度 第21問｜添付書類は会社法人等番号、境内地113㎡、原因は不詳', '本試験の年の注が、今の法令でも意味を持つのかを確かめてから書きなさい']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '本試験の年の注が、今の法令でも意味を持つのかを確かめてから書きなさい')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H23_dai21mon_toukishinseisho_kansei', 'H23_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H23_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H23_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成23年8月21日申請　Ａ地方法務局', '土地表題登記', '>土地所在図<', '>地積測量図<', '>所有権証明書<', '>会社法人等番号<', '>代理権限証書<',
          'Ａ市Ｂ町五丁目50番地１　宗教法人雨堤天満宮', '代表役員　荒牧英雄', 'Ａ市Ｂ町五丁目', '>境内地<', '>113<', '>不詳<',
          'Ａ市Ｂ町三丁目１番２号　土地家屋調査士　中村　容子', '①地番', '②地目', '③地積　　m²',
          '平成23年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
judge('完成形の画像：記入行は3行（答案用紙どおり）', html_k.count('<td class="chimoku">') == 3)
judge('完成形の画像：登録免許税の欄がない（答案用紙どおり）', '登録免許税' not in html_k)
judge('完成形の画像：添付書類は今の法令（会社法人等番号）で、出題当時の扱いは表の下の注', '>会社法人等番号<' in html_k and '>住所証明書<' not in html_k and '※添付書類は今の法令による。出題当時は会社法人等番号の制度がなく、住所証明書を付け、資格証明書は問題文の注5（登記所が同一）で不要だった' in html_k)
judge('完成形の画像：申請の日付が添付書類の下・申請人の上（答案用紙の順）',
      html_k.index('添　付　書　類') < html_k.index('平成23年8月21日申請') < html_k.index('申　　請　　人'))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '資格証明書', '>宅地<', '>87<', '昭和26年8月19日時効取得', '>境内地<', '>不詳<', '住所証明書', '会社法人等番号',
          '今の法令では会社法人等番号<br>（出題当時は住所証明書を付け、資格証明書は注5で不要）', '境内地は1㎡未満切捨て、原因は土地が生じた原因の不詳',
          '平成23年度 第21問｜添付書類は会社法人等番号、境内地113㎡、原因は不詳']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 注の書き分け（今年は問題文の注1〜7の1系統。裸の「注N」を残さない） ----
fig_data = fig[fig.index('## 差し替えデータ'):]
for src, name in [(text, '記事'), (fig_data, '解説図（差し替えデータ）')]:
    bare = [m.group(0) for m in re.finditer(r'(.{0,6})注([1-9])', src)
            if not re.search(r'(問題文の|問題文の注[1-9]〜)$', m.group(1))]
    judge(f'{name}の注の書き分け（裸の「注N」: {bare[:5]}）', not bare)
for s in ['問題文の注4', '問題文の注5', '問題文の注6', '問題文の注1〜7']:
    check('注の書き分け', s)
for s in ['①問1を書き切る', '②問3の申請書の地積以外の欄を埋める', '③A点・M点・K点の放射', '④H点', '⑤C点', '⑥本件土地の面積と地積の113',
          '⑦辺長6本と、土地所在図・地積測量図']:
    check('本番で解く順番', s)

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '令和', '昭和30年', 'ブロックべい', '北野一郎']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
for s in ['コンクリート杭', 'ブロック塀', '石標', '市金属標', '神楽殿', '参道', '境内地']:
    check('問題文どおりの用語', s)

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
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋添削1＋完成形1＝計{N_FIG + 2}か所の想定）', n_marker == N_FIG + 2)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成23年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成23年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '登記申請書')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')

# ---- 答えは今の法令、出題当時の扱いは「（出題当時は〜）」の注（2026-09-30、ユーザー指示） ----
for s_ in ['（出題当時は会社法人等番号の制度〈平成27年11月施行〉がなく、住所証明書を付け、資格証明書は問題文の注5〈申請を受ける登記所と法人の登記を受けた登記所が同一〉で付けなくてよかった）',
           '- **添付書類は今の法令で会社法人等番号**', '不動産登記令第7条第1項第1号イ']:
    check('出題当時の注', s_)
print('NG件数:', ng)
