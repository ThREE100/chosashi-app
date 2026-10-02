"""平成20年度 第21問（土地）会話形式note記事：記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-30に添付の過去問集〈全20ページ、画面の撮影画像〉で照合。下の AGAROOT に転記）と一致することも確認する。
アガルートの再掲・解答例は、日付を平成30年などに置き換えた改題だった（申請の日付・売買の日付・死亡の日付・出生の年など）。
改題で加えられた要素はアガルート独自の教材なので、照合にも記事にも使わない（2026-09-30、ユーザー指示。下の KAIDAI で記事にないことを確かめる）。
実行: python3 note-articles-Kijyutsu/H20/Q21/verify_H20_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H20_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H20_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H20_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H20_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H20_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H20_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
make = open(os.path.join(HERE, 'zu', 'make_H20_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
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


def pt(z):
    return f'（{z.real:.2f}, {z.imag:.2f}）'


# ---- 座標（問題文のK市基準点・測量成果） ----
T1, T2, T3 = P(32.74, 3.31), P(13.73, 1.85), P(3.54, 30.35)
A, C, D = P(31.63, 9.85), P(7.03, 28.98), P(32.26, 31.00)

# ---- 問1 T101（結合トラバース T2→T101→T3、コンパスの法則） ----
b21 = cmath.phase(T1 - T2)
check('arg(T1−T2)（真数表の4°23′30″）', to_dms(b21))
check('T2→T101′の方向角', to_dms(b21 + dms(150, 21, 32)))
judge('180° − 25°14′57.55″ ＝ 154°45′02.45″（真数表の25°14′58″）',
      to_dms(math.pi - (b21 + dms(150, 21, 32))) == '25°14′57.55″')
T101R = radial(T2, T1, 10.71, dms(150, 21, 32))
check('T101′ 表示', '表示：' + disp(T101R))
check('arg(T2−T101′)', to_dms(cmath.phase(T2 - T101R)))
check('T101′→T3′の方向角（真数表の1°10′28″）', to_dms(cmath.phase(T2 - T101R) + dms(116, 25, 26)))
T3R = radial(T101R, T2, 23.91, dms(116, 25, 26))
check('T3′ 表示', '表示：' + disp(T3R))
ERR = T3 - T3R
check('T3 − T3′ 表示', '表示：' + disp(ERR))
check('閉合誤差の長さ', f'Abs で{fmt_num(abs(ERR))}、約3cm')
judge('T3′はT3より北西（補正は南東へ）', ERR.real < 0 and ERR.imag > 0)
T101X = T101R + ERR * 10.71 / (10.71 + 23.91)
check('T101 表示', '表示：' + disp(T101X))
check('T101の補正量', disp(ERR * 10.71 / 34.62))
T101 = r2(T101X)
check('T101 答え', '**▶ T101（4.04, 6.43）**')
judge('T101 ＝（4.04, 6.43）', T101 == P(4.04, 6.43))
WS = r2(T101R - ERR * 10.71 / 34.62)
W23 = r2(T101R + ERR * 23.91 / 34.62)
check('補正量の向きを逆にした誤り', f'T101は{pt(WS)}')
check('23.91で配った誤り', f'23.91のほうを掛けると{pt(W23)}')
judge('向きを逆にした誤りは北西へ約2cm', 0.015 < abs(T101R - ERR * 10.71 / 34.62 - T101X) < 0.025
      and (T101R - ERR * 10.71 / 34.62 - T101X).real > 0 and (T101R - ERR * 10.71 / 34.62 - T101X).imag < 0)
judge('半分ずつ配っても丸めると同じ（だから誤答に使わない）', r2(T101R + ERR / 2) == T101)

# ---- 問2 B点（調整後のT101から後視の向きを取り直す） ----
check('arg(T2−T101) 表示（真数表の25°17′52″）', '表示：' + to_dms(cmath.phase(T2 - T101)))
check('T101→Bの方向角（真数表の0°33′10″）', to_dms(cmath.phase(T2 - T101) + dms(24, 44, 42)))
check('T101→Bの方向角＋360°', to_dms(cmath.phase(T2 - T101) + dms(24, 44, 42) + 2 * math.pi))
BX = radial(T101, T2, 6.22, dms(24, 44, 42))
check('B 表示', '表示：' + disp(BX))
B = r2(BX)
check('B 答え', '**▶ B点（10.26, 6.37）**')
BW = T101 + cmath.rect(6.22, cmath.phase(T2 - T101R) + dms(24, 44, 42))
check('調整前の向きを使った誤り 表示', disp(BW))
check('調整前の向きを使った誤り', f'丸めるとB{pt(r2(BW))}')
check('調整前の向き＋24°44′42″', to_dms(cmath.phase(T2 - T101R) + dms(24, 44, 42)))
check('T101′から放射した誤り', f'放射すると{pt(r2(radial(T101R, T2, 6.22, dms(24, 44, 42))))}')
judge('3分の差で約5mm', abs(abs(BW - BX) * 1000 - 5.3) < 0.3)

# ---- 問2 E点（A→Dを4：5に内分） ----
check('D − A', disp(D - A))
EX = A + (D - A) * 4 / 9
check('E 表示', '表示：' + disp(EX))
E = r2(EX)
check('E 答え', '**▶ E点（31.91, 19.25）**')
check('AE 表示', '表示：' + fmt_num(abs(E - A)))
check('ED 表示', '表示：' + fmt_num(abs(D - E)))
judge('AE ÷ ED ＝ 0.8', abs(abs(E - A) / abs(D - E) - 0.8) < 1e-9)
EW = r2(A + (D - A) * 4 / 5)
check('5分の4の誤り', f'アンタの点は{pt(EW)}')
judge('誤りのEはDの4m少し手前', 4 < abs(D - EW) < 4.5)

# ---- 問2 F点（Eから直線BCへの垂線の足） ----
check('C − B 表示', '表示：' + disp(C - B))
W = (E - B) / (C - B)
check('w 表示', '表示：' + disp(W))
FX = B + (C - B) * (W + W.conjugate()) / 2
check('F 表示', '表示：' + disp(FX))
F = r2(FX)
check('F 答え', '**▶ F点（8.89, 15.96）**')
check('直角の検算 表示', '表示：' + disp((C - B).conjugate() * (F - E)))
check('F − E', disp(F - E))
FW = r2(B + (C - B) * (E.imag - B.imag) / (C.imag - B.imag))
check('Eから真南の誤り', f'真南に下ろした点は{pt(FW)}')
check('誤りのFは東へ3.3m', f'東へ{abs(FW - F):.1f}mも離れる')
num = (E - B).conjugate() * ((C - B) * 1j)
den = (C - B).conjugate() * ((C - B) * 1j)
check('別解の分子 表示', '表示：' + disp(num))
check('別解の分母 表示', f'表示：{fmt_num(den.imag)}i')
judge('別解のt ＝ wの実部', abs(num.imag / den.imag - W.real) < 1e-12)
check('別解の割り算', f'221.2873 ÷ 521.645 ＝ {math.floor(num.imag / den.imag * 1e4) / 1e4:.4f}…')

# ---- 問3の前提 面積・公差 ----
RO, I_ = [A, B, F, E], [E, F, C, D]
vi = (C - E).conjugate() * (D - F)
vr = (F - A).conjugate() * (E - B)
vt = (C - A).conjugate() * (D - B)
check('（イ）表示', '表示：' + disp(vi))
check('（ロ）表示', '表示：' + disp(vr))
check('5番 表示', '表示：' + disp(vt))
judge('対角線の式と多角形の式が一致（（イ）（ロ）5番）',
      abs(abs(vi.imag) / 2 - area(I_)) < 1e-9 and abs(abs(vr.imag) / 2 - area(RO)) < 1e-9
      and abs(abs(vt.imag) / 2 - area([A, B, C, D])) < 1e-9)
check('（イ）面積', f'601.5853 ÷ 2 ＝ {area(I_):.5f}')
check('（ロ）面積', f'425.1727 ÷ 2 ＝ {area(RO):.5f}')
check('5番 面積', f'1026.758 ÷ 2 ＝ {area([A, B, C, D]):.3f}')
ki, kr = chiseki(area(I_)), chiseki(area(RO))
check('地積の答え', f'**▶ （イ）{ki:.2f}㎡、（ロ）{kr:.2f}㎡**')
check('分筆後の合計と差', f'300.79 ＋ 212.58 ＝ {ki + kr:.2f}で、登記記録の512.66より{ki + kr - 512.66:.2f}㎡多い')
check('丸める前の差', f'差{area([A, B, C, D]) - 512.66:.3f}㎡')
judge('差0.71は甲2の2.21の内側', ki + kr - 512.66 < 2.21)
for s in ['準則第72条第1項', '甲2', '2.21㎡']:
    check('公差', s)

# ---- 問4 辺長 ----
SIDES = {'AB': (A, B), 'BF': (B, F), 'FC': (F, C), 'CD': (C, D), 'DE': (D, E), 'EA': (E, A), 'EF': (E, F)}
for n, (p, q) in SIDES.items():
    val = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{val}')
    check(f'辺長{n} 表示', '表示：' + fmt_num(abs(q - p)))
    check(f'図の辺長{n}', val, fig, '解説図')
check('DEの四捨五入', f'DEは{math.floor(abs(D - E) * 1e4) / 1e4:.4f}…で')
check('基準点まで入れた縦', f'縦約{round((T1.real - T3.real) * 4)}mm')
check('基準点まで入れた横', f'横約{round((D.imag - T2.imag) * 4)}mm')

# ---- 相続人と申請書の欄 ----
for s in ['- **西川和子**：配偶者。常に相続人（民法第890条）。C市A町二丁目5番2号',
          '- **西川二郎**：父だけが同じ兄。兄弟姉妹として相続人。B市D町三丁目1番7号',
          '- **西川八郎**：平成15年に死亡した弟の五郎の子。代襲して相続人（民法第889条第2項・第887条第2項）。B市D町四丁目6番1号',
          '- **相続人にならない人**：西川七郎（相続の放棄）、西川六郎（欠格）、西川九郎（兄弟姉妹の相続は再代襲しない）',
          '- **登記の目的**：土地分筆登記', '- **添付書類**：地積測量図　相続証明書　代位原因証書　代理権限証書',
          '- **大きな枠**：被代位者（被相続人　西川四郎）　相続人　C市A町二丁目5番2号　西川和子　B市D町三丁目1番7号　西川二郎　B市D町四丁目6番1号　西川八郎　申請人（代位者）　B市C町二丁目3番4号　南野二郎　代位原因　平成19年5月1日売買の所有権移転登記請求権　登録免許税　金2,000円',
          '- **所在**：K市B町一丁目', '- **1行目**：①5番、②宅地、③512.66、登記原因及びその日付は空欄',
          '- **2行目**：①（イ）5番1、②空欄、③300.79、「①③5番1、5番2に分筆」',
          '- **3行目**：①（ロ）5番2、②宅地、③212.58、「5番から分筆」',
          '- **代位原因**：平成19年5月1日売買の所有権移転登記請求権', '- **申請人（代位者）**：B市C町二丁目3番4号　南野二郎']:
    check('答え', s)
for s in ['不動産登記法第39条第1項', '同法第30条', '民法第939条', '民法第889条第1項第2号', '民法第889条第2項が第887条第2項だけを準用',
          '第887条第3項は準用していない', '民法第900条第4号ただし書', '民法第890条', '民法第423条', '不動産登記令第3条第4号',
          '不動産登記令第7条第1項第3号', '同項第4号', '不動産登記事務取扱手続準則第72条第1項',
          '登録免許税法別表第一の一の（十三）イ', '不動産登記事務取扱手続準則第67条第1項第4号本文', '不動産登記令別表8の項添付情報欄イ']:
    check('条文', s)

# ---- アガルートの解答例（2026-09-30、過去問集の解答例ページから転記）と一致するか ----
AGAROOT = ['T101（4.04, 6.43）', 'B点（10.26, 6.37）', 'E点（31.91, 19.25）', 'F点（8.89, 15.96）', '土地分筆登記',
           '地積測量図　相続証明書　代位原因証書　代理権限証書', '被代位者（被相続人　西川四郎）', 'C市A町二丁目5番2号　西川和子',
           'B市D町三丁目1番7号　西川二郎', 'B市D町四丁目6番1号　西川八郎', '申請人（代位者）　B市C町二丁目3番4号　南野二郎',
           '売買の所有権移転登記請求権', '金2,000円', 'K市B町一丁目', '①5番、②宅地、③512.66', '（イ）5番1', '③300.79',
           '「①③5番1、5番2に分筆」', '（ロ）5番2、②宅地、③212.58', '「5番から分筆」',
           '- **AB**：21.65', '- **BF**：9.69', '- **FC**：13.15', '- **CD**：25.31', '- **DE**：11.76', '- **EA**：9.40', '- **EF**：23.25',
           '地番の欄（5番1、5番2）', 'A・Bは金属標、C・D・Eはコンクリート杭、Fは今回設置した金属鋲', '北は6－2と6－1、西は4、東は7、南は道路',
           '基準点T1・T2・T3と多角点T101の位置と名称']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)
# 改題で加えられた要素（アガルート独自の教材）：記事・付属プロンプト・作図・画像に入れない（2026-09-30、ユーザー指示）
KAIDAI = ['平成30年', '平成6年', '昭和34年', '平成18年', '昭和57年', '改題', '平成○年']
for src, name in [(text, '記事'), (fig, '解説図'), (form, '登記申請書'), (fix, '添削'), (thumb, '見出し画像'), (draw, '作図'),
                  (make, '申請書の画像')]:
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
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H20_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = sorted(set(int(m) for m in re.findall(r"(?:new_figure|fixed_figure)\('図(\d+)　", draw)))
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, N_FIG + 1)))
fits = re.findall(r'^\s*fit\((.*)', draw, re.M)
judge(f'作図スクリプトのfitはすべて pad_aspect=True（{len(fits)}か所）',
      fits and all('pad_aspect=True' in draw[draw.index(f):draw.index(f) + 300] for f in fits))
for s in ['（4.04, 6.43）', '（10.26, 6.37）', '（31.91, 19.25）', '（8.89, 15.96）', '（4.05, 6.41）', '（4.03, 6.44）',
          '（10.26, 6.38）', '（10.26, 6.36）', '（32.13, 26.77）', '（8.42, 19.25）', '4°23′30.45″', '154°45′02.45″',
          '−25°14′57.55″', '91°10′28.45″', '−25°17′52.31″', '−0°33′10.31″', '4.0432… ＋ 6.4184…i', '3.5531… ＋ 30.3234…i',
          '−0.0131… ＋ 0.0265…i', '4.0391… ＋ 6.4266…i', '10.2597… ＋ 6.3699…i', '6.3752…', '0.4242… − 1.0181…i',
          '8.8898 ＋ 15.9614i', '−0.0323 ＋ 531.1089i', '−3.23 ＋ 22.61i', '−23.02 − 3.29i', '−413.6242 − 425.1727i',
          '−435.1064 − 601.5853i', '212.58635', '300.79265', '513.379', '0.719', '9.4041…', '11.7552…']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['そのとおり。北を上にして描き直すと、こうなるわ', '変数XをT101に使い回しなさい', 'そう。配り方だけ正しくやればいいの。図にするとこうよ',
          '真数表に25°17′52″があるのが、正しい向きの合図だったのよ', '9.4041… ÷ 11.7552… ＝ 0.8。4：5になっています',
          'そう。本番は、キーの少ない w の式でいいわ', '1026.758 ÷ 2 ＝ 513.379。（イ）と（ロ）の丸める前の和300.79265 ＋ 212.58635とも一致します',
          '一番厳しい列で比べる必要はないの', 'そこが出題者のねらいよ。まとめなさい', '相続人が申請する立場を証する情報（同項第4号。戸籍など、相続証明書）よ',
          '地積更正をしないんだから、登記記録のまま書くの', '基準点だけ描いてT101を忘れないこと', '次の年度も、この調子でいくわよ！']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成20年８月24日　　申請　　Ｋ地方法務局', '土地分筆登記', '地積測量図　相続証明書　代位原因証書　代理権限証書',
          '被代位者（被相続人　西川四郎）', '相続人　Ｃ市Ａ町二丁目５番２号　西川和子', 'Ｂ市Ｄ町三丁目１番７号　西川二郎',
          'Ｂ市Ｄ町四丁目６番１号　西川八郎', '申請人（代位者）　　　　Ｂ市Ｃ町二丁目３番４号　南野二郎',
          '代位原因　平成19年５月１日売買の所有権移転登記請求権', '登録免許税　金2,000円', 'Ｋ市Ｂ町一丁目',
          '①「５番」、②「宅地」、③「512｜66」', '①「（イ）５番１」、②空欄、③「300｜79」、登記原因及びその日付「①③５番１、５番２に分筆」',
          '①「（ロ）５番２」、②「宅地」、③「212｜58」、登記原因及びその日付「５番から分筆」',
          '「表題 → 登記の目的 → 添付書類 → 申請日・法務局 → 大きな枠 → 代理人 → 土地の表示 → 土地家屋調査士（職印）」',
          '登録免許税の欄はないので、大きな枠の最後の行に書く', '「①地　　番」「②地　　目」「③地　　積　m²」「登記原因及びその日付」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['Ｃ市Ａ町二丁目５番２号　西川七郎', '相続の放棄', 'Ｂ市Ｄ町三丁目１番７号　西川二郎', 'Ｂ市Ｄ町四丁目６番１号　西川八郎',
          '七郎は相続の放棄で初めから相続人でない。父母も死亡 → 兄弟姉妹へ。', '二郎は父だけ同じでも兄弟、八郎は五郎を代襲（九郎は再代襲しない）',
          '平成20年度 第21問｜七郎は放棄、相続人は和子・二郎・八郎の3人', '放棄した人を消して、兄弟姉妹の代まで下りる。赤で直すとこうよ']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '放棄した人を消して、兄弟姉妹の代まで下りる。赤で直すとこうよ')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H20_dai21mon_toukishinseisho_kansei', 'H20_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H20_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H20_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成20年８月24日　　申請　　Ｋ地方法務局', '>土地分筆登記<', '>地積測量図　相続証明書　代位原因証書　代理権限証書<',
          '>被代位者（被相続人　西川四郎）<', '>相続人<', '>Ｃ市Ａ町二丁目５番２号　西川和子<', '>Ｂ市Ｄ町三丁目１番７号　西川二郎<',
          '>Ｂ市Ｄ町四丁目６番１号　西川八郎<', '>申請人（代位者）<', '>Ｂ市Ｃ町二丁目３番４号　南野二郎<',
          '>代位原因　平成19年５月１日売買の所有権移転登記請求権<', '>登録免許税　金2,000円<', '>Ｋ市Ｂ町一丁目<',
          '>５番<', '>宅地<', '>512<', '>66<', '>（イ）５番１<', '>300<', '>79<', '>①③５番１、５番２に分筆<', '>（ロ）５番２<', '>212<', '>58<',
          '>５番から分筆<', 'Ａ市Ｂ町一丁目２番３号', '東田太郎　㊞', '（連絡先　＊＊－＊＊＊＊－＊＊＊＊）', '土地家屋調査士　東田太郎',
          '①地　　番', '②地　　目', '③地　　積　m²', '平成20年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
# 法改正（3-0：法定相続情報番号）：答えは「相続証明書」のまま、今の法令の注を記事・プロンプト・画像にそろえる（2026-10-02）
NOTE_ = '相続証明書は、今は法定相続情報一覧図の写し又は法定相続情報番号の提供で代えることもできる（不動産登記規則第37条の3第1項）。出題当時は法定相続情報番号の制度がなかった'
check('法定相続情報番号の注（記事）', '今は、法定相続情報一覧図の写し又は法定相続情報番号を提供して、相続証明書に代えることもできる（不動産登記規則第37条の3第1項。出題当時は法定相続情報番号の制度がなかった）')
check('法定相続情報番号の注（完成形の画像）', NOTE_, html_k, '完成形画像')
judge('完成形の画像：記入行は3行（答案用紙どおり）', html_k.count('<td class="chimoku">') == 3)
judge('完成形の画像：登録免許税の独立した欄がない（答案用紙どおり、大きな枠の中）', '登録免許税</div>' not in html_k)
judge('完成形の画像：相続人でない人がいない', all(n not in html_k for n in ['西川七郎', '西川六郎', '西川九郎', '西川美子']))
judge('完成形の画像：添付書類 → 申請の日付 → 大きな枠 → 代理人 → 土地の表示（答案用紙の順）',
      html_k.index('添　付　書　類') < html_k.index('平成20年８月24日') < html_k.index('被代位者') < html_k.index('代　　理　　人')
      < html_k.index('土地の表示'))
# ---- 問1・問2の欄の画像（2026-10-02 追加。申請書でない解答欄も答えの直後に置く） ----
for name in ['H20_dai21mon_toukishinseisho_kansei_toi1', 'H20_dai21mon_toukishinseisho_kansei_toi2']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が横1200px（{w}×{h}px）', w == 1200 and 200 < h < 700)
    else:
        judge(f'{name}.png がある', False)
html_t1 = open(os.path.join(HERE, 'zu', 'H20_dai21mon_toukishinseisho_kansei_toi1.html'), encoding='utf-8').read()
html_t2 = open(os.path.join(HERE, 'zu', 'H20_dai21mon_toukishinseisho_kansei_toi2.html'), encoding='utf-8').read()
for s in ['第21問答案用紙（その1）', '>問1<', '>T101<', '>X座標<', '>Y座標<', '>4.04m<', '>6.43m<', '答案用紙（その1） 問1 解答例']:
    check('問1の欄の画像（HTML）', s, html_t1, '問1の欄')
for s in ['>問2<', '>B点<', '>10.26m<', '>6.37m<', '>E点<', '>31.91m<', '>19.25m<', '>F点<', '>8.89m<', '>15.96m<', '答案用紙（その1） 問2 解答例']:
    check('問2の欄の画像（HTML）', s, html_t2, '問2の欄')
judge('問2の欄はB→E→Fの順（答案用紙どおり）', html_t2.index('>B点<') < html_t2.index('>E点<') < html_t2.index('>F点<'))
for s in ['T101　X座標「4.04m」、Y座標「6.43m」', 'B点　X座標「10.26m」、Y座標「6.37m」', 'E点　X座標「31.91m」、Y座標「19.25m」',
          'F点　X座標「8.89m」、Y座標「15.96m」', '答案用紙の問1の欄は、T101のX座標とY座標の枠が横に1行並んでいるだけです',
          'これで問2のB点・E点・F点がそろいました']:
    check('問1・問2の欄のプロンプト', s, form, '登記申請書')
for s in ['答案用紙の問1の欄は、T101のX座標とY座標の枠が横に1行並んでいるだけです', 'これで問2のB点・E点・F点がそろいました']:
    check('問1・問2の欄の挿入位置の文言', s)
for s in ['①誤答', '②添削（赤ペン）', '③正解', 'Ｃ市Ａ町二丁目５番２号　西川七郎', '相続の放棄', 'Ｂ市Ｄ町三丁目１番７号　西川二郎',
          'Ｂ市Ｄ町四丁目６番１号　西川八郎', '七郎は相続の放棄で初めから相続人でない。父母も死亡 → 兄弟姉妹へ。',
          '二郎は父だけ同じでも兄弟、八郎は五郎を代襲（九郎は再代襲しない）', '平成20年度 第21問｜七郎は放棄、相続人は和子・二郎・八郎の3人']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 注の書き分け（今年は、見取図の注・親族関係の注・測量成果の表の下の注1〜3・問題文の注1〜4。裸の「注N」を残さない） ----
fig_data = fig[fig.index('## 差し替えデータ'):]
for src, name in [(text, '記事'), (fig_data, '解説図（差し替えデータ）'), (draw, '作図')]:
    bare = [m.group(0) for m in re.finditer(r'(.{0,9})注([1-9])', src)
            if not re.search(r'(問題文の|測量成果の表の下の)$', m.group(1))]
    judge(f'{name}の注の書き分け（裸の「注N」: {bare[:5]}）', not bare)
for s in ['見取図の注', '親族関係の注', '測量成果の表の下の注2', '問題文の注1', '問題文の注3', '問題文の注4', '調査結果の6', '調査結果の5〜7']:
    check('注の書き分け', s)
for s in ['①親族関係を読んで相続人を確定し、問3の申請書の地積以外の欄を埋める', '②E点（9分の4ですぐ終わる）', '③T101（コンパスの法則）',
          '④B点（後視の向きを取り直す）', '⑤F点（垂線の足）', '⑥（イ）（ロ）の面積と公差', '⑦辺長7本と地積測量図']:
    check('本番で解く順番', s)

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '令和', '金属びょう', '≒']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
for s in ['コンクリート杭', '金属標', '金属鋲', '多角点', '閉合誤差', 'コンパスの法則']:
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
        while j < len(lines) and (not lines[j].strip() or lines[j].startswith('> 【画像挿入】')):
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続（画像挿入マーカーをはさむものも含む）: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図{N_FIG}＋添削1＋申請書の完成形1＋問1・問2の欄2＝計{N_FIG + 4}か所の想定）',
      n_marker == N_FIG + 4)
# 記事の画像挿入マーカーの順と zu/ のPNGの対応（マーカーの文言 → PNG）。2026-10-02 追加
ORDER = [('北を上にして座標どおりに描き直した全体図', 'H20_dai21mon_zu01_zentaizu.png'),
         ('結合トラバースの図', 'H20_dai21mon_zu02_T101_ketsugou.png'),
         ('コンパスの法則の配分の図', 'H20_dai21mon_zu03_compass.png'),
         ('答案用紙（その1）の問1の欄の完成形', 'H20_dai21mon_toukishinseisho_kansei_toi1.png'),
         ('B点の求め方の図', 'H20_dai21mon_zu04_B_housha.png'),
         ('E点の求め方の図', 'H20_dai21mon_zu05_E_naibun.png'),
         ('F点の求め方の図', 'H20_dai21mon_zu06_F_suisen.png'),
         ('答案用紙（その1）の問2の欄の完成形', 'H20_dai21mon_toukishinseisho_kansei_toi2.png'),
         ('（イ）E→F→C→Dと（ロ）A→B→F→Eの面積の図', 'H20_dai21mon_zu07_menseki.png'),
         ('公差の数直線の図', 'H20_dai21mon_zu08_kousa.png'),
         ('西川四郎の相続関係図', 'H20_dai21mon_zu09_souzoku.png'),
         ('代位の関係図', 'H20_dai21mon_zu10_daii.png'),
         ('誤答→添削→正解の3コマ', 'H20_dai21mon_toukishinseisho_machigai.png'),
         ('分筆後の区画と地番の図', 'H20_dai21mon_zu11_bunpitsu_chiban.png'),
         ('登記申請書（問3）の完成形', 'H20_dai21mon_toukishinseisho_kansei.png'),
         ('地積測量図（1／250）の完成見本', 'H20_dai21mon_zu12_chiseki_sokuryouzu.png'),
         ('本番で解く順番の図', 'H20_dai21mon_zu13_toku_junban.png')]
mk = [l for l in lines if l.startswith('> 【画像挿入】')]
judge(f'マーカーの数とPNGの対応表の数が同じ（{len(mk)}・{len(ORDER)}）', len(mk) == len(ORDER))
for n_, ((key, png_), m_) in enumerate(zip(ORDER, mk), 1):
    judge(f'マーカー{n_}「{key}」→ {png_}（記事の順）', key in m_ and os.path.exists(os.path.join(HERE, 'zu', png_)))
zu_png = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
judge(f'zu/ のPNGが対応表と過不足なし（{len(zu_png)}枚）', zu_png == sorted(p_ for _, p_ in ORDER))
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成20年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成20年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '登記申請書')
for k in '買主相続人代位分筆':
    judge(f'見出し画像の字形チェックに「{k}」がある', k in thumb[thumb.index('Final check'):])
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
print('NG件数:', ng)
