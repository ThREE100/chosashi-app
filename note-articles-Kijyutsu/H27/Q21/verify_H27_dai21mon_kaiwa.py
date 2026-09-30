"""平成27年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と一致することも確認する。
アガルートの過去問集は、問題文の日付を平成30年に置き換え、会社法人等番号（1234-56-789012）を聴取記録に書き足した改題版だったので、
日付は試験問題の本文（平成27年7月20日など）に戻して照合し、会社法人等番号の番号は申請人欄に書かない（試験問題に番号がない）。
実行: python3 note-articles-Kijyutsu/H27/Q21/verify_H27_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num, kousa_kou2  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H27_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H27_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H27_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H27_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H27_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H27_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（問題文の〔B市基準点成果表〕と〔測量によって得られた座標〕） ----
T1, T2 = P(527.57, 483.20), P(512.57, 521.95)
B, C, D, E, F, G = P(475.50, 427.50), P(430.00, 427.50), P(430.00, 493.00), P(445.75, 493.00), P(500.00, 493.00), \
    P(500.00, 500.00)
I, J, L, M, N = P(442.25, 500.00), P(430.00, 500.00), P(500.00, 530.00), P(500.00, 537.00), P(470.00, 537.00)

# ---- 問1 A点（T1に据えてT2を後視、右回り） ----
check('arg(T2−T1)', to_dms(cmath.phase(T2 - T1)))
brgA = cmath.phase(T2 - T1) + dms(136, 26, 37)
check('T1→Aの方向角', to_dms(brgA))
Ax = radial(T1, T2, 18.82, dms(136, 26, 37))
check('A 表示', '表示：' + disp(Ax))
A = r2(Ax)
check('A 答え', '**▶ A点（520.40, 465.80）**')
Aw = r2(radial(T2, T1, 18.82, dms(136, 26, 37)))
check('器械点と後視点を入れ替えた誤りのA', f'（{Aw.real:.2f}, {Aw.imag:.2f}）')
check('誤りのAのずれ（約74m）', f'約{round(abs(Aw - A)):d}m')
judge('誤りのAは東（Yが大きい）', Aw.imag > A.imag + 70)
judge('真数表の67°36′17″の行（cos 0.3809・sin 0.9245）と方向角−180°の差が1秒未満',
      abs(math.degrees(brgA) - 180 - (67 + 36 / 60 + 17 / 3600)) < 1 / 3600)
for s in [f'18.82 × 0.3809 ＝ {18.82 * 0.3809:.6f}', f'527.57 − 7.168538 ＝ {527.57 - 7.168538:.6f}',
          f'18.82 × 0.9245 ＝ {18.82 * 0.9245:.5f}', f'483.20 − 17.39909 ＝ {483.20 - 17.39909:.5f}']:
    check('真数表の検算', s)
judge('真数表の検算を丸めても（520.40, 465.80）', r2(P(527.57 - 18.82 * 0.3809, 483.20 - 18.82 * 0.9245)) == A)
for n, (p, q, want) in {'T1・T2': (T1, T2, (68, 50, 20)), 'A・B': (A, B, (40, 27, 51)), 'A・F': (A, F, (53, 7, 48)),
                        'N・I': (N, I, (53, 7, 48)), 'B・F': (B, F, (69, 29, 30)), 'C・E': (C, E, (76, 28, 46))}.items():
    br = math.degrees(cmath.phase(q - p)) % 180
    ang = min(br, 180 - br)
    judge(f'真数表の角 {n}：南北の線となす角 {ang:.4f}°', abs(ang - (want[0] + want[1] / 60 + want[2] / 3600)) < 1 / 3600)

# ---- 問1 K点（EはN・Iから7.00m、K ＝ E ＋ (N − I)） ----
wE = (I - N).conjugate() * (E - N)
check('△NIE 表示', '表示：' + disp(wE))
check('NI 表示', '表示：' + fmt_num(abs(I - N)))
check('Eの幅', f'{abs(wE.imag):.2f} ÷ {abs(I - N):.2f} ＝ {abs(wE.imag) / abs(I - N):.2f}')
Kx = E + (N - I) * (530 - 493) / (537 - 500)
check('K 表示', '表示：' + disp(Kx))
K = r2(Kx)
check('K 答え', '**▶ K点（473.50, 530.00）**')
wK = (I - N).conjugate() * (K - N)
check('△NIK 表示', '表示：' + disp(wK))
judge('Kの幅も7.00（iの係数がEと同じ）', abs(wK.imag - wE.imag) < 1e-9)
Kw = P(470.00, 530.00)
check('Nの真西の誤りのK', '（470.00, 530.00）')
check('誤りのKの幅', f'{abs(((I - N).conjugate() * (Kw - N)).imag) / abs(I - N):.2f}m')
judge('Lを通る岸はY＝530（L・Mの幅7.00）', L.imag == 530 and abs(M - L) == 7)

# ---- 問1 H点（直線EKとY＝500の交点） ----
Hx = E + (K - E) * (500 - 493) / (530 - 493)
check('H 表示', '表示：' + disp(Hx))
H = r2(Hx)
check('H 答え', '**▶ H点（451.00, 500.00）**')
Hw = I + 7.00
check('Iの真北7.00mの誤りのH', f'（{Hw.real:.2f}, {Hw.imag:.2f}）')
check('誤りのHの幅', f'{abs(((I - N).conjugate() * (Hw - N)).imag) / abs(I - N):.2f}m')
check('HI', f'451.00 − 442.25 ＝ {H.real - I.real:.2f}')
check('横切る長さ', f'7.00 ÷ 0.7999 ＝ {math.floor(7 / 0.7999 * 1000) / 1000:.3f}…')
judge('EH＝8.75（5.25と7の斜辺）', abs(abs(H - E) - 8.75) < 1e-9 and abs(H.real - E.real - 5.25) < 1e-9)

# ---- 問2 ----
for s in ['- **結論**：依然として登記の対象となる土地である',
          '- **理由**：株式会社山川製菓が所有する甲土地の一部を水路としたもので、公有水面となったわけではなく、引き続き私権の客体となる土地だから。水路となったことは地目（用悪水路）の変更にすぎない（不動産登記規則第99条）',
          '不動産登記法第36条', '不動産登記法第42条']:
    check('問2', s)

# ---- 問3 ----
s_i = double_area_sum([A, B, C, D, E, F])
check('（イ） 表示', '表示：' + disp(s_i))
a_i, a_ro = area([A, B, C, D, E, F]), area([F, E, H, G])
check('（イ）面積', f'{abs(s_i.imag):.2f} ÷ 2 ＝ {a_i:.3f}')
check('（イ）地積', f'{chiseki(a_i):.2f}㎡です')
check('（イ）四捨五入の誤答', f'{round(a_i + 1e-9, 2):.2f}㎡です！')
check('（ロ）台形', f'(54.25 ＋ 49.00) × 7 ÷ 2 ＝ {(54.25 + 49.00) * 7 / 2:.3f}')
judge('（ロ）台形 ＝ 座標法', abs((54.25 + 49) * 7 / 2 - a_ro) < 1e-9)
check('（ロ）宅地の癖の誤答', f'{math.floor(a_ro * 100) / 100:.2f}㎡！')
check('（ロ）地積', f'{chiseki(a_ro, takuchi=False)}㎡です')
sum_after = chiseki(a_i) + chiseki(a_ro, takuchi=False)
check('分筆後の地積の合計（準則第72条第1項）', f'{chiseki(a_i):.2f} ＋ {chiseki(a_ro, takuchi=False)} ＝ {sum_after:.2f}')
check('登記記録との差', f'差は{sum_after - 5144.50:.2f}です')
check('準則第72条第1項', '不動産登記事務取扱手続準則第72条第1項')
check('別紙2の公差の記述', '今回測量した甲土地の地積及び筆界点間距離は、公差の範囲内')
check('参考の甲2の公差', f'約{kousa_kou2(5144.50):.2f}㎡')
judge('差は参考の甲2の公差より小さい', sum_after - 5144.50 < kousa_kou2(5144.50))
absent('切り捨て前の合計で比べる旧版', '差は0.80')
# （ロ）の対角線の別解
dg = (E - G).conjugate() * (F - H)
check('（ロ）対角線 表示', '表示：' + disp(dg))
check('（ロ）対角線 面積', f'{dg.imag:.2f} ÷ 2 ＝ {dg.imag / 2:.3f}。台形と同じです')
judge('（ロ）対角線 ＝ 座標法', abs(dg.imag / 2 - a_ro) < 1e-9)
# K点・H点の別解（交点の式）
nk, dk = (N - M).conjugate() * (L - E), (N - M).conjugate() * (N - I)
check('Kの別解 分子 表示', '表示：' + disp(nk))
check('Kの別解 分母 表示', '表示：' + disp(dk))
judge('Kの別解 t ＝ 1', abs(nk.imag / dk.imag - 1) < 1e-12 and r2(E + (N - I) * nk.imag / dk.imag) == K)
nh, dh = (G - I).conjugate() * (I - E), (G - I).conjugate() * (K - E)
check('Hの別解 分子 表示', '表示：' + disp(nh))
check('Hの別解 分母 表示', '表示：' + disp(dh))
check('Hの別解 t', f't ＝ {fmt_num(nh.imag)} ÷ {fmt_num(dh.imag)} ＝ {fmt_num(nh.imag / dh.imag)}')
check('Hの別解 表示', '表示：' + disp(E + (K - E) * nh.imag / dh.imag))
judge('Hの別解 t ＝ 7 ÷ 37', abs(nh.imag / dh.imag - 7 / 37) < 1e-12)
check('Hの別解 電卓の割り算', f'[×] {fmt_num(nh.imag)} [÷] {fmt_num(dh.imag)} [=]')
# 「表示：」の行がすべて照合済みか（上で照合した値の一覧と突き合わせる）
judge('甲土地全体の座標の面積 ＝（イ）＋（ロ）', abs(area([A, B, C, D, E, H, G, F]) - (a_i + a_ro)) < 1e-6)
for s in ['- **登記の目的**：土地一部地目変更・分筆登記', '- **添付情報**：地積測量図　会社法人等番号　代理権限証明情報',
          '- **申請人**：E県F市G町二丁目3番4号　株式会社山川製菓　代表取締役　山川一郎',
          '- **登録免許税**：金2,000円（分筆後の土地1個につき1,000円 × 2個）', '- **所在**：B市C町一丁目',
          '①100番1、②宅地、③5144.50（登記記録の地積）、登記原因は空欄',
          '①（イ）、③4783.92、登記原因「平成27年7月20日一部地目変更　③100番1、100番3に分筆」',
          '①（ロ）100番3、②用悪水路、③361、登記原因「100番1から分筆」']:
    check('問3', s)
check('申請人の誤答（旧本店）', 'B市C町一丁目1番2号　株式会社山川製菓')
check('（ロ）の誤答', '100番3、用悪水路、361.37、100番1から分筆')
for s in ['不動産登記法第39条第2項', '不動産登記規則第35条第7号', '同準則第67条第1項第4号', '（同項第3号）',
          '不動産登記事務取扱手続準則第68条第16号', '不動産登記規則第100条', '不動産登記令別表8の項',
          '同令第7条第1項第1号イ', '（同項第2号）', '登録免許税法別表第一の一の（十三）イ', '不動産登記令第3条第2号',
          '別表5の項', '平成27年11月の施行']:
    check('条文', s)

# ---- 問4 ----
s_o = double_area_sum([L, K, H, I, N, M])
check('乙土地 表示', '表示：' + disp(s_o))
check('乙土地 面積', f'{abs(s_o.imag):.2f} ÷ 2 ＝ {area([L, K, H, I, N, M]):.3f}')
check('乙土地 地積', f'切り捨てて{chiseki(area([L, K, H, I, N, M]), takuchi=False)}㎡')
check('KH 表示', '表示：' + fmt_num(abs(H - K)))
SIDES = {'LK': (L, K), 'KH': (K, H), 'HI': (H, I), 'IN': (I, N), 'NM': (N, M), 'ML': (M, L)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', f'{n} {v}', fig, '解説図')
    judge(f'辺長{n}は四捨五入の境目でない', abs(abs(p - q) * 100 - round(abs(p - q) * 100)) < 1e-9)
check('縮尺', '1m ＝ 2mm')
check('南北の長さ', f'約{round((T1.real - I.real) * 2):d}mm')
check('東西の長さ', f'約{round((M.imag - T1.imag) * 2):d}mm')
check('乙土地だけの南北', f'南北{M.real - I.real:.2f}mで約{round((M.real - I.real) * 2):d}mm')
for s in ['『平成27年8月5日公有水面埋立』', '不動産登記令別表4の項', 'L・H・I・Mは石杭、K・Nはコンクリート杭',
          'Hの北西は100－1', 'だから100－1', '100－3です', 'L・K・Hの西は100－2', 'I・Nの南東は101',
          'L・Mの北とH・Iの西は水路']:
    check('問4', s)

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記。日付は試験問題の本文に戻した） ----
AGAROOT = ['（520.40, 465.80）', '（451.00, 500.00）', '（473.50, 530.00）', '依然として登記の対象となる土地である',
           '土地一部地目変更・分筆登記', '地積測量図　会社法人等番号　代理権限', 'E県F市G町二丁目3番4号　株式会社山川製菓',
           '代表取締役　山川一郎', '金2,000円', 'B市C町一丁目', '③5144.50', '③4783.92',
           '一部地目変更　③100番1、100番3に分筆', '（ロ）100番3、②用悪水路、③361', '100番1から分筆',
           '：7.00', '：26.50', '：30.00', '：37.50', '：46.25', '：8.75', '100－1', '100－2', '101', '水路',
           '申請地', 'L・H・I・Mは石杭、K・Nはコンクリート杭']
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
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H27_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\(|seiri_zu\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, 12)))
fits = re.findall(r'^\s*fit\(.*$', draw, re.M)
judge(f'作図のfit {len(fits)}か所がすべて pad_aspect=True', fits and all('pad_aspect=True' in f or 'pad_aspect' in draw[draw.index(f):draw.index(f) + 200] for f in fits))
for s in ['（520.40, 465.80）', '（473.50, 530.00）', '（451.00, 500.00）', '（519.74, 539.35）', '（470.00, 530.00）',
          '（449.25, 500.00）', '111°09′40.54″', '247°36′17.54″', '136°26′37″', '67°36′17″', '323.75 ÷ NI 46.25',
          '4.20', '5.60', '8.75', '4783.925', '4783.92', '4783.93', '361.375', '361', '5144.92', '5144.50', '0.42',
          '−2609.25 ＋ 722.75i', '404.25 ÷ 2136.75', '−1110.00 ÷ −1110.00',
          '54.25', '49.00', '約171mm', '約108mm', '100－1', '100－3', 'B市C町一丁目']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
# 画像挿入の位置の文言が記事にあるか
for s in ['そこから北東へ斜めに走っていた古い水路が乙土地、というわけ', '表は、放射を三角関数で解く人のための道具よ',
          '岸は平行です！', '同じ水路の形になっています', '0.42は、はるかに小さいわ', 'H・Iは真南向きの短い辺よ',
          '迷ったら交点の式に戻りなさい', '台形と同じです', '次の年度も、この調子でいくわよ！']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成27年○月○日　申請　○○法務局', '土地一部地目変更・分筆登記', '地積測量図　会社法人等番号　代理権限証明情報',
          'Ｅ県Ｆ市Ｇ町二丁目３番４号／株式会社山川製菓／代表取締役　山川一郎', '金2,000円', 'Ｂ市Ｃ町一丁目',
          '③「5144｜50」', '③「4783｜92」', '登記原因「平成27年７月20日一部地目変更　③100番１、100番３に分筆」',
          '①「（ロ）100番３」', '②「用悪水路」', '③「361」', '登記原因「100番１から分筆」', '「添　付　情　報」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['Ｂ市Ｃ町一丁目１番２号／株式会社山川製菓', '③「361｜37」', 'Ｅ県Ｆ市Ｇ町二丁目３番４号', '代表取締役　山川一郎',
          '（ロ）の地積は361です', '平成27年○月○日　申請　○○法務局']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '（ロ）の地積は361です」')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H27_dai21mon_toukishinseisho_kansei', 'H27_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    ok = os.path.exists(png)
    if ok:
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H27_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H27_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成27年○月○日　申請　○○法務局', '土地一部地目変更・分筆登記', '地積測量図　会社法人等番号　代理権限証明情報',
          'Ｅ県Ｆ市Ｇ町二丁目３番４号', '株式会社山川製菓', '代表取締役　山川一郎', '金2,000円', 'Ｂ市Ｃ町一丁目', '100番１',
          '（ロ）100番３', '用悪水路', '平成27年７月20日一部地目変更', '③100番１、100番３に分筆', '100番１から分筆',
          '>5144<', '>50<', '>4783<', '>92<', '>361<', '添　付　情　報', '（略）', '※添付情報は今の法令による。出題当時は会社法人等番号の制度（平成27年11月施行）がなく、会社法人等番号の代わりに代表者の資格を証する情報（資格証明情報）を付けた', '平成27年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
    if s.startswith('※添付情報は今の法令による'):
        check('完成形の画像とプロンプトの注', s, open(os.path.join(HERE, 'prompt_H27_dai21mon_toukishinseisho_gazou.md'), encoding='utf-8').read(), '申請書')
for s in ['①誤答', '②添削（赤ペン）', '③正解', 'Ｂ市Ｃ町一丁目１番２号', 'Ｅ県Ｆ市Ｇ町二丁目３番４号', '代表取締役　山川一郎',
          '>37<', '下線は抹消の印。本店移転は付記1号で登記済み！', '用悪水路は1㎡未満を切り捨て。361だけ',
          '平成27年度 第21問｜申請人は今の本店と代表者、用悪水路の地積は1㎡未満を切り捨て']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
    if s.startswith(('下線', '用悪水路', '平成27年度 第21問')):
        check('添削の画像とプロンプトの文言', s, fix, '添削')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', '石くい', 'くいが', '令和6年度問題21']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', '石杭')

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
# ---- 注の書き分け（問題文の注・A点の観測データの表の注・調査素図の注） ----
QUAL = ('問題文の注', '調査素図の注', '観測データの表の注')
bad_chu = []
for k, l in enumerate(lines):
    for m in re.finditer(r'注(\d)', l):
        if not any(q in l[:m.start() + 1] for q in QUAL):
            bad_chu.append((k + 1, l[max(0, m.start() - 12):m.end()]))
judge(f'注の番号の前に、どこの注かが書いてある: 不備 {bad_chu}', not bad_chu)
for s in ['- **問題文の注3**：乙土地における近傍類似の地図の縮尺は500分の1', '- **調査素図の注3**：H点は',
          '- **調査素図の注4**：埋め立てた水路の幅は7.00m', 'A点の観測データの表の注1', '問題文の注8は',
          '不動産登記規則第77条第4項', '同規則第76条第2項', '不動産登記事務取扱手続準則第51条第4項',
          'X 440〜530・Y 480〜540（90m × 60m、答案用紙の上で180mm × 120mm）']:
    check('注の仕分けと縮尺の根拠', s)
judge('作図範囲の計画がT1・I・M・Nを含む', 440 <= I.real and T1.real <= 530 and 480 <= T1.imag and M.imag <= 540)
# ---- 解く順番と時間配分（一般論でなく具体的に） ----
for s in ['いちばん時間を食うのは、問4の作図', '計算でいちばん重いのは、（イ）の6点の面積',
          '座標が要るのは（イ）（ロ）の地積と、問4の図面だけです', '1. 問を先に読み、注を仕分ける',
          '5. 問4：使う範囲を決めてから作図', '『E県』も落とさないこと']:
    check('解く順番', s)
absent('一般論の時間配分', '15分で片付けて')
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成27年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成27年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
absent('見出し画像に前の年度の文言', '令和6年度', thumb, '見出し画像')
absent('見出し画像に前の年度の文言', '塀', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
# 変数の割り当て（第1章）と電卓操作の見出し
for s in ['- **X**：T1（A点を求めた後は、K点に使い回す）', '- **Y**：T2（A点を求めた後は、H点に使い回す）',
          '変数XはK点に使い回すわ', '変数YはH点に使い回すわ']:
    check('変数の割り当て', s)
judge('式（点名）と電卓操作の数', text.count('式（点名）') <= len(re.findall(r'^電卓操作', text, re.M)))

print('NG件数:', ng)
