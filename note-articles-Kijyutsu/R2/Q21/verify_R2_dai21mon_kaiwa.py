"""令和2年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（第1欄〜第4欄）と同じになることも確認する。
実行: python3 note-articles-Kijyutsu/R2/Q21/verify_R2_dai21mon_kaiwa.py"""
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R2_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_R2_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R2_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R2_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R2_dai21mon_miidashi_gazou.md')
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


def poly_disp(pts):
    return f'表示：（実部）− {fmt_num(abs(double_area_sum(pts).imag))}i'


# ---- 座標（問題文の〔調査及び測量によって得られた座標値〕と〔道路境界確認図の任意座標〕） ----
A, C, D, E, F = P(16.78, -2.92), P(34.00, 10.35), P(24.45, 19.50), P(16.18, 14.48), P(8.93, 7.23)
A_, B_, C_ = P(109.23, 133.26), P(117.63, 141.66), P(126.45, 146.53)

# ---- 問1 B点（2点による座標変換） ----
ratio = (C - A) / (C_ - A_)
judge('回転と縮尺 (C − A) ÷ (C′ − A′) ＝ 1（虚部0）', abs(ratio - 1) < 1e-12)
check('比の表示', '表示：' + fmt_num(ratio.real))
judge('A′→A と C′→C の移動量が同じ（−92.45, −136.18）', abs((A - A_) - P(-92.45, -136.18)) < 1e-9
      and abs((C - C_) - P(-92.45, -136.18)) < 1e-9)
check('移動量', '〈−92.45, −136.18〉')
Bc = A + (B_ - A_) * ratio
check('B 表示', '表示：' + disp(Bc))
B = r2(Bc)
check('B 答え', '**▶ B点（25.18, 5.48）**')
check('B′ − A′', 'B′ − A′ は 8.40 ＋ 8.40i')

# ---- 問1 G点・H点 ----
S4 = area([B, C, D, E])
check('32番4 表示', poly_disp([B, C, D, E]))
check('32番4 面積', f'{S4:.5f}㎡')
need = 156.53 - S4
check('持ってくる面積', f'{need:.5f}㎡です')
check('登記記録で引いた誤り', f'{156.53 - 123.00:.2f}㎡')
dot1 = (E - B).conjugate() * (A - B)
dot2 = (F - E).conjugate() * (A - B)
judge('Conjg(E − B) × (A − B) の実部0（直角）', abs(dot1.real) < 1e-9)
judge('Conjg(F − E) × (A − B) の虚部0（平行）', abs(dot2.imag) < 1e-9)
check('直角の表示', f'表示：{fmt_num(dot1.imag)}i')
check('平行の表示', f'表示：{fmt_num(dot2.real)}\n')
BH = need / abs(E - B)
check('BH 表示', '表示：' + fmt_num(BH))
Hc = B + (A - B) / abs(A - B) * BH
Gc = E + (F - E) / abs(F - E) * BH
check('H 表示', '表示：' + disp(Hc))
check('G 表示', '表示：' + disp(Gc))
H, G = r2(Hc), r2(Gc)
check('H 答え', '**▶ H点（23.34, 3.64）**')
check('G 答え', '**▶ G点（14.34, 12.64）**')
judge('H・G は丸めると（23.34, 3.64）（14.34, 12.64）', H == P(23.34, 3.64) and G == P(14.34, 12.64))
check('別解 d', f'd ＝ 33.11925 ÷ 18 ＝ {fmt_num(need / 18)}')
judge('BE ＝ 9√2', abs(abs(E - B) - 9 * math.sqrt(2)) < 1e-9)
Bw = (156.53 - 123.00) / abs(E - B)
Hw, Gw = r2(B + (A - B) / abs(A - B) * Bw), r2(E + (F - E) / abs(F - E) * Bw)
check('誤りのH', f'H点は（{Hw.real:.2f}, {Hw.imag:.2f}）')
check('誤りのG', f'G点は（{Gw.real:.2f}, {Gw.imag:.2f}）')
check('誤りの甲区画', f'甲区画は{chiseki(area([B, C, D, E, Gw, Hw])):.2f}㎡')
KOU = [B, C, D, E, G, H]
check('甲区画 表示', poly_disp(KOU))
check('甲区画 面積', f'{area(KOU):.5f}㎡')
judge('甲区画の地積 156.53（依頼どおり）', chiseki(area(KOU)) == 156.53)
judge('長方形 BEGH ＝ 18 × 1.84 ＝ 33.12', abs(area([B, E, G, H]) - 33.12) < 1e-9 and abs(18 * 1.84 - 33.12) < 1e-9)

# ---- 問2 地積更正の要否（精度区分 甲2） ----
S5 = area([A, B, E, F])
check('32番5 表示', poly_disp([A, B, E, F]))
check('32番5 面積', f'{S5:.2f}㎡')
for s in ['- **32番4**：差 0.41㎡、甲2の公差 0.91㎡ → 範囲内', '- **32番5**：差 0.05㎡、甲2の公差 1.00㎡ → 範囲内',
          '32番4の甲1は0.38㎡']:
    check('公差', s)
judge('32番4 差 0.41 ≦ 甲2 0.91（甲1 0.38 だと超える）', 0.38 < round(S4 - 123.00, 2) <= 0.91)
judge('32番5 差 0.05 ≦ 甲2 1.00', round(S5 - 140.80, 2) == 0.05 <= 1.00)
check('分筆2件＋合筆1件の誤り', '合わせて3,000円')

# ---- 問2 申請書 ----
I_ = [A, H, G, F]
check('（イ） 表示', poly_disp(I_))
check('（イ） 面積', f'{area(I_):.2f}㎡')
judge('（イ）の地積 107.73（引き算の107.68ではない）', chiseki(area(I_)) == 107.73 and round(140.80 - 33.12, 2) == 107.68)
check('引き算の誤り', '140.80 − 33.12 ＝ 107.68')
judge('合筆後の32番4 ＝ 123.00 ＋ 33.12 ＝ 156.12', round(123.00 + 33.12, 2) == 156.12)
check('合筆後の地積の説明', '156.12㎡')
for s in ['- **登記の目的**：土地分合筆登記',
          '- **添付書類**：地積測量図　登記済証　印鑑証明書　相続証明書　代理権限証書',
          '- **登録免許税**：金2,000円',
          '- **申請人**：（被相続人　山川一郎）　相続人　A市B町一丁目32番地4　山川小太郎　A市B町一丁目32番地5　香川浪子',
          '- **所在**：A市B町一丁目',
          '①32番5、②宅地、③140.80（登記記録の地積）、登記原因は空欄',
          '①（イ）32番5、③107.73、登記原因「③32番4に一部合併」',
          '①（ロ）、③33.12、登記原因「32番5から分割して32番4に合併する部分」',
          '①32番4、②宅地、③123.00（登記記録の地積）、登記原因は空欄',
          '①32番4、③156.12、登記原因「③32番5から一部合併」']:
    check('問2', s)

# ---- 問3 ----
for s in ['- **ア**：不動産', '- **イ**：登記名義人', '- **ウ**：書面', '- **エ**：合筆', '- **オ**：合併']:
    check('問3', s)

# ---- 問4 辺長 ----
SIDES = {'AH': (A, H), 'HB': (H, B), 'BE': (B, E), 'EG': (E, G), 'GF': (G, F), 'FA': (F, A)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', f'{n} {v}', fig, '解説図')
check('辺長HG', f'- **HG（分筆線）**：{round(abs(G - H), 2):.2f}')
for n, p, q in [('HB', H, B), ('AH', A, H), ('GF', G, F)]:
    check(f'四捨五入前の{n}', fmt_num(abs(p - q)))

# ---- アガルートの解答例（第1欄〜第4欄）と同じ答えか ----
AGAROOT = ['（25.18, 5.48）', '（14.34, 12.64）', '（23.34, 3.64）', '土地分合筆登記', '金2,000円',
           '地積測量図　登記済証　印鑑証明書　相続証明書　代理権限証書', '（被相続人　山川一郎）',
           'A市B町一丁目32番地4　山川小太郎', 'A市B町一丁目32番地5　香川浪子', '③32番4に一部合併',
           '32番5から分割して32番4に合併する部分', '③32番5から一部合併', '107.73', '33.12', '156.12',
           '- **ア**：不動産', '- **イ**：登記名義人', '- **ウ**：書面', '- **エ**：合筆', '- **オ**：合併',
           '地番の欄は32番5、土地の所在はA市B町一丁目']
for s in AGAROOT:
    check('解答例と同じ答え', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（18枚）', n_fig == 18)
for i in range(1, 19):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R2_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
for q in re.findall(r'\*\*記事の挿入位置\*\*：[^「\n]*「([^」]+)」', fig):
    check('解説図の挿入位置の引用', q, None, '記事（図の挿入位置）')
for s in ['123.41075', '156.53075', '107.73', '33.12', '156.12', '（23.32, 3.62）', '（14.32, 12.62）', '156.89',
          '（−92.45, −136.18）', '2.6020…', '12.7279…']:
    check('解説図の数値', s, fig, '解説図')
for s in ['土地分合筆登記', '地積測量図　登記済証　印鑑証明書　相続証明書', '代理権限証書', '金2,000円', '（被相続人　山川一郎）',
          '相続人　Ａ市Ｂ町一丁目32番地４　山川小太郎', 'Ａ市Ｂ町一丁目32番地５　香川浪子', '「107｜73」', '「33｜12」',
          '「156｜12」', '「③32番４に一部合併」', '「③32番５から一部合併」', '「32番５から分割して32番４に合併する部分」',
          '令和２年10月18日　申請　Ａ地方法務局']:
    check('登記申請書', s, form, '登記申請書')
for s in ['「107｜68」', '「156｜53」', '「107｜73」', '「156｜12」', '「③32番４に一部合併」', '「③32番５から一部合併」']:
    check('添削', s, fix, '添削')


# ---- 2026-09-29 追加作業：アガルートの解説と照らして足した別解・作図範囲・解く順番 ----
dz = (B - D).conjugate() * (C - E)
check('対角線の別解（32番4） 表示', '表示：' + disp(dz))
judge('対角線の別解のiの係数 ÷ 2 ＝ 32番4の面積', abs(abs(dz.imag) / 2 - S4) < 1e-9)
dz2 = (H - F).conjugate() * (G - A)
check('対角線の別解（（イ）） 表示', '表示：' + disp(dz2))
judge('対角線の別解のiの係数 ÷ 2 ＝ （イ）の面積', abs(abs(dz2.imag) / 2 - 107.73) < 1e-9)
K1_, K2_ = P(3.24, 2.76), P(19.39, 24.16)
xs, ys = [p.real for p in [A, B, E, F, G, H, K1_, K2_]], [p.imag for p in [A, B, E, F, G, H, K1_, K2_]]
judge('作図範囲 X 3.24〜25.18・Y −2.92〜24.16（約88mm × 108mm）', (min(xs), max(xs), min(ys), max(ys)) == (3.24, 25.18, -2.92, 24.16)
      and round((max(xs) - min(xs)) * 4) == 88 and round((max(ys) - min(ys)) * 4) == 108)
for s in ['Xが3.24（A市基準点1）から25.18（B点）まで、Yが−2.92（A点）から24.16（A市基準点2）まで', '約88mm', '約108mm',
          '「（単位：ｍ）」', 'まず問3です。登記識別情報の穴埋めは、別紙を読まなくても答えられます',
          '問3 → 問1のB点 → 申請書の書ける欄 → G点・H点 → 申請書の地積3つ → 地積測量図']:
    check('足した観点', s)
for s in ['70.9112 ＋ 246.8215i', '123.41075㎡', '約88mm × 108mm', '（イ）107.73・（ロ）33.12・合筆後156.12']:
    check('図8・図9の数値', s, fig, '解説図')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['R2_dai21mon_toukishinseisho_kansei', 'R2_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長・横1200px（{w}×{h}px）', h > w and w == 1200)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'R2_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'R2_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['土地分合筆登記', '地積測量図　登記済証　印鑑証明書　相続証明書', '代理権限証書', '金2,000円', '（被相続人　山川一郎）',
          'Ａ市Ｂ町一丁目32番地４　山川小太郎', 'Ａ市Ｂ町一丁目32番地５　香川浪子', '令和２年10月18日　申請　Ａ地方法務局',
          'Ａ市Ｂ町一丁目', '（イ）32番５', '③32番４に一部合併', '32番５から分割して32番４に合併する部分', '③32番５から一部合併']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
k_order = [html_k.index(s) for s in ['登記の目的', '添　付　書　類', '登録免許税', '申　　請　　人', '代　　理　　人', '令和２年10月18日']]
judge('完成形の画像の欄の順序が答案用紙どおり（目的→添付→登録免許税→申請人→代理人→申請日）', k_order == sorted(k_order))
for a_, b_ in [('107', '73'), ('33', '12'), ('123', '00'), ('156', '12'), ('140', '80')]:
    check('完成形の画像の地積', f'{a_}</span></td><td class="dec"><span class="ink">{b_}', html_k, '完成形画像')
for s in ['①誤答', '②添削（赤ペン）', '③正解', '>68<', '>53<', '>73<', '>12<', '（イ）は分筆後の土地。座標で求めた地積（A・H・G・F）を書く',
          '32番4は地積更正をしていない！登記記録の123.00 ＋ 33.12']:
    check('添削の画像（HTML）', s, html_m, '添削画像')
check('添削のプロンプトは縦に積む', '3コマを縦に積んだ縦長', fix, '添削')
absent('添削のプロンプトに横並びの旧版の指示がない', '左から「①誤答」', fix, '添削')
draw = open(os.path.join(HERE, 'zu', 'draw_R2_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
fits = re.findall(r'^\s*fit\(.*$', draw, re.M)
judge(f'作図スクリプトの表示範囲はすべて fit(..., pad_aspect=True)（{len(fits)}か所）', fits and all('pad_aspect=True' in f for f in fits))

# ---- 注の番号の書き分け（問題文の注・調査図素図の注。2026-10-08に調査図素図の注を追加） ----
bare = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)注[0-9]', text)]
judge(f'注の番号はすべて「問題文の注N」「調査図素図の注N」と書き分けている（書き分けていないもの: {bare}）', not bare)

# ---- アガルートの解答例（第1欄〜第4欄）と空欄ごとに全部照らす ----
for s in ['**▶ B点（25.18, 5.48）**', '**▶ G点（14.34, 12.64）**', '**▶ H点（23.34, 3.64）**',
          '- **ア**：不動産', '- **イ**：登記名義人', '- **ウ**：書面', '- **エ**：合筆', '- **オ**：合併',
          '- **登記の目的**：土地分合筆登記', '- **添付書類**：地積測量図　登記済証　印鑑証明書　相続証明書　代理権限証書',
          '- **登録免許税**：金2,000円', '- **所在**：A市B町一丁目',
          '- **AH**：9.28', '- **HB**：2.60', '- **BE**：12.73', '- **EG**：2.60', '- **GF**：7.65', '- **FA**：12.83',
          '- **HG（分筆線）**：12.73']:
    check('アガルートの解答例と空欄ごとに同じ答え', s)
# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '令和7']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
spk = [l.rstrip() for l in lines if l.rstrip() in ('**トリ先生**', '**藍子**')]
seq = [(i, l.rstrip()) for i, l in enumerate(lines) if l.strip()]
dup = [seq[k][0] + 1 for k in range(2, len(seq)) if seq[k][1] in ('**トリ先生**', '**藍子**')
       and seq[k - 2][1] == seq[k][1] and seq[k - 1][1].startswith('「')]
judge(f'同じ話者のセリフが間に何も挟まずに続いていない: {dup}', not dup)
# 画像挿入マーカーをはさんで同じ話者が続くのも1つの連続とみなす。複数段落のセリフも1つとして読む（2026-10-02追加）
speakers = [(i + 1, l.rstrip()) for i, l in enumerate(lines) if l.rstrip() in ('**トリ先生**', '**藍子**')]
same_m = []
for (i1, s1_), (i2, s2_) in zip(speakers, speakers[1:]):
    j = i1
    while j < len(lines) and not lines[j].rstrip().endswith('」'):
        j += 1
    rest = [x for x in lines[j + 1:i2 - 1] if x.strip()]
    if s1_ == s2_ and (not rest or all(x.startswith('> 【画像挿入】') for x in rest)):
        same_m.append(i2)
judge(f'同じ話者のセリフが続いていない（画像挿入マーカーだけをはさむものも）: {same_m}', not same_m)
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図18＋添削1＋完成形1＋第1欄・第3欄2＝計22か所の想定）', n_marker == 22)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和2年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和2年度問題21（土地）', thumb, '見出し画像')
check('添削画像の記事タイトル', title[2:], fix, '添削')


# ---- 2026-10-02 追加：穴埋めの答えの語を会話で言っているか ----
for s_ in ['（ア）不動産及び（イ）登記名義人となった申請人ごとに', '（ウ）は書面です',
           '（エ）は『所有権の登記がある土地の（エ）の登記』だから合筆、（オ）は『所有権の登記がある建物の（オ）の登記』だから合併ですね',
           '「第1欄は、B点（25.18, 5.48）、G点（14.34, 12.64）、H点（23.34, 3.64）です！」']:
    check('答えの語を会話で言っている', s_)
# ---- 2026-10-02 追加：今の法令の注（法定相続情報番号） ----
NOTE_ = ('※相続証明書は、今は法定相続情報一覧図の写しか法定相続情報番号の提供で代えることもできる（不動産登記規則第37条の3第1項）。'
         '出題当時は法定相続情報番号の制度がなかった')
check('法定相続情報番号の注（記事）', '法定相続情報一覧図の写しか法定相続情報番号を提供して、これに代えることもできる（不動産登記規則第37条の3第1項。出題当時は法定相続情報番号の制度がなく、番号での提供はできなかった）')
check('法定相続情報番号の注（完成形の画像）', NOTE_, html_k, '完成形画像')
check('法定相続情報番号の注（プロンプト）', NOTE_, form, '登記申請書')

# ---- 2026-10-02 追加：記事の画像挿入マーカーと zu/ のPNGが記事の順に対応しているか ----
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R2_dai21mon_zu01_jikeiretsu', '時系列と人の関係の図', 'fig'),
        ('R2_dai21mon_zu02_zentaizu', '北を上にして座標どおりに描き直した全体図', 'fig'),
        ('R2_dai21mon_zu03_chuu_shiwake', '注の仕分けの図', 'fig'),
        ('R2_dai21mon_zu04_B_henkan', 'B点の座標変換の図', 'fig'),
        ('R2_dai21mon_zu05_taikakusen', '四角形の面積を対角線で出す別解の図', 'fig'),
        ('R2_dai21mon_zu06_hikizan', '差し引く面積の比較図', 'fig'),
        ('R2_dai21mon_zu07_GH_chouhoukei', 'G点・H点の求め方の図', 'fig'),
        ('R2_dai21mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R2_dai21mon_zu08_kousa', '公差の判定図', 'fig'),
        ('R2_dai21mon_zu09_kensuu', '申請件数と登録免許税の比較図', 'fig'),
        ('R2_dai21mon_zu10_chimoku', '地目の判断の図', 'fig'),
        ('R2_dai21mon_zu11_goppitsu_seigen', '合筆の制限の図', 'fig'),
        ('R2_dai21mon_zu12_shinseinin', '申請人の図', 'fig'),
        ('R2_dai21mon_zu13_i_chiseki', '（イ）の地積の図', 'fig'),
        ('R2_dai21mon_zu14_bungoppitsu', '分合筆の流れの図', 'fig'),
        ('R2_dai21mon_toukishinseisho_machigai', '誤答→添削→正解の3コマ', 'tall'),
        ('R2_dai21mon_toukishinseisho_kansei', '登記申請書（問2）の完成形', 'tall'),
        ('R2_dai21mon_zu15_shikibetsu', '登記識別情報の整理図', 'fig'),
        ('R2_dai21mon_dai3ran_kansei', '第3欄（問3）の完成形', 'wide'),
        ('R2_dai21mon_zu16_chiseki_hani', '地積測量図に描く範囲の図', 'fig'),
        ('R2_dai21mon_zu17_chiseki_sokuryouzu', '第4欄（問4）の地積測量図（32番5）の完成見本', 'fig'),
        ('R2_dai21mon_zu18_kaku_junban', '本番で解く順番の図', 'fig')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
for (name, key, kind), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = struct.unpack('>II', open(path, 'rb').read()[16:24])
        ok = (w == 1200 and h > w) if kind == 'tall' else (w == 1200 and h < w) if kind == 'wide' else w >= 1200
    judge(f'PNG（マーカー順・大きさ） : {name}', ok)
    src = fig if '_zu' in name else (fix if 'machigai' in name else form)
    judge(f'プロンプトにファイル名 : zu/{name}.png', f'zu/{name}.png' in src)
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない : {extra}', not extra)
for name, needles in [('R2_dai21mon_dai1ran_kansei', ['第1欄', 'Ｂ点', 'Ｇ点', 'Ｈ点', '25.18', '5.48', '14.34', '12.64', '23.34', '3.64']),
                      ('R2_dai21mon_dai3ran_kansei', ['第3欄', '不動産', '登記名義人', '書面', '合筆', '合併'])]:
    h_ = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n_ in needles:
        check(f'{name}.html', n_, h_, '解答欄の画像')
for s_ in ['「Ｂ点」「25.18」「5.48」', '「Ｇ点」「14.34」「12.64」', '「Ｈ点」「23.34」「3.64」',
           '上から「ア」「不動産」／「イ」「登記名義人」／「ウ」「書面」／「エ」「合筆」／「オ」「合併」',
           '試験の答案用紙（`touan_youshi/R2_dai21mon_touan_youshi.pdf` の1ページ目）で確かめた形']:
    check('解答欄の画像のプロンプト', s_, form, '登記申請書')
check('作図のタイトル（対角線の別解。図番なし）', "'問1　四角形の面積を対角線で出す別解", draw, '作図')
bare_p = [m.group(0) for m in re.finditer(r'(?<!問題文の)(?<!調査図素図の)注[0-9]', fig.split('## 差し替えデータ')[-1])]
judge(f'解説図プロンプトの差し替えデータの注も書き分けている（{bare_p}）', not bare_p)


# ---- 2026-10-02 追加：試験の答案用紙（実物、touan_youshi/）と欄の形を照らす ----
import pymupdf  # noqa: E402
TY = os.path.join(HERE, 'touan_youshi', 'R2_dai21mon_touan_youshi.pdf')
doc = pymupdf.open(TY)
judge(f'答案用紙は2ページ（{doc.page_count}）', doc.page_count == 2)
nz = lambda t: re.sub(r'[\s　]', '', t)  # noqa: E731
t1, t2 = nz(doc[0].get_text()), nz(doc[1].get_text())
for s_ in ['第1欄', 'Ｘ座標（m）', 'Ｙ座標（m）', 'Ｂ点', 'Ｇ点', 'Ｈ点', '登記申請書', '登記の目的', '添付書類', '登録免許税',
           '申請人', '代理人', '（略）', '令和2年10月18日申請Ａ地方法務局', '第2欄', '所在', '土地の表示', '①地番', '②地目',
           '③地積', '登記原因及びその日付', '第3欄', 'アイウエオ']:
    check('答案用紙1ページ目の印刷', s_, t1, '答案用紙')
for s_ in ['第4欄', '地番', '地積測量図', '土地の所在', '作成者', '（略）（令和2年○月○日作成）', '申請人（略）', '縮尺1250']:
    check('答案用紙2ページ目の印刷', s_, t2, '答案用紙')
# 欄の順序（1ページ目）：目的→添付書類→登録免許税→申請人→代理人→（略）→申請の日付
o1 = [t1.index(x) for x in ['登記の目的', '添付書類', '登録免許税', '申請人', '代理人', '（略）', '令和2年10月18日']]
judge('答案用紙の申請書の欄の順序（目的→添付書類→登録免許税→申請人→代理人（略）→申請日）', o1 == sorted(o1))
judge('答案用紙の第3欄の記号は ア〜オ の5つ（縦に1組ずつ）', 'アイウエオ' in t1 and 'カ' not in t1.split('第3欄')[-1])
judge('答案用紙の欄名は「添付書類」（「添付情報」ではない）', '添付情報' not in t1)
judge('答案用紙の第4欄に方位記号の印刷はない（N・北の文字なし）', 'Ｎ' not in t2 and 'N' not in t2 and '北' not in t2)
# 画像（HTML）が答案用紙の形どおりか
h1 = open(os.path.join(ZU, 'R2_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
h3 = open(os.path.join(ZU, 'R2_dai21mon_dai3ran_kansei.html'), encoding='utf-8').read()
check('第1欄の見出し（答案用紙どおり）', 'Ｘ座標（m）', h1, '解答欄の画像')
check('第1欄の見出し（答案用紙どおり）', 'Ｙ座標（m）', h1, '解答欄の画像')
check('第1欄の左上の斜線のセル', 'class="head diag"', h1, '解答欄の画像')
judge('第1欄の点名の行は Ｂ点→Ｇ点→Ｈ点 の順', h1.index('Ｂ点') < h1.index('Ｇ点') < h1.index('Ｈ点'))
rows3 = re.findall(r'<tr><td>([アイウエオ])</td><td class="ans">', h3)
judge(f'第3欄の画像は答案用紙どおり ア〜オ を1組ずつ縦に5行（{rows3}）', rows3 == list('アイウエオ'))
n_land_k = html_k.count('<td class="cause">')
n_land_m = html_m.count('<td class="cause">')
judge(f'完成形の土地の表示は記入行6行（{n_land_k}）', n_land_k == 6)
judge(f'添削の土地の表示も答案用紙どおり記入行6行×3コマ（{n_land_m}）', n_land_m == 18)
check('完成形の代理人の行の（略）', '<div class="ryaku">（略）</div>', html_k, '完成形画像')
judge('完成形の申請書に「添付情報」の欄名がない', '添付情報' not in html_k)
check('記事：第4欄の印刷済みのもの', '- **答案用紙に印刷済み**：縮尺「1／250」、作成者・申請人の欄の「（略）」。方位記号は印刷されていないので自分で描く')
PRINTED = '印刷済み：「第4欄」「地積測量図」、地番・土地の所在の欄の枠、作成者と申請人の「（略）」、作成日の欄、縮尺 1/250（作成者・申請人・縮尺は書かない）'
check('第4欄の図の説明文：印刷済みのもの', PRINTED, draw, '作図')
check('解説図プロンプト：第4欄の印刷済みのもの', PRINTED, fig, '解説図')
make = open(os.path.join(ZU, 'make_R2_dai21mon_shinseisho_gazou.py'), encoding='utf-8').read()
for name_, src_ in [('記事', text), ('解説図プロンプト', fig), ('申請書プロンプト', form), ('添削プロンプト', fix),
                    ('見出し画像プロンプト', thumb), ('作図スクリプト', draw), ('画像スクリプト', make)]:
    for bad in ['仮のもの', '仮の形', 'リポジトリにない', '試験の答案用紙で確かめたら直す']:
        absent(f'「仮」の記述が残っていない（{name_}）', bad, src_, name_)


# ---- 2026-10-08 追加：最新の執筆指示書との照らし直し ----
# まとめのワナの各項目 → その会話の直後の図（2つのワナを1枚にまとめない）
TRAPS = [('**B点は2点で座標変換**', 'B点の座標変換の図'),
         ('**引くのは実測の123.41**', '差し引く面積の比較図'),
         ('**Conjg(u) × v の実部0は直角、虚部0は平行**', 'G点・H点の求め方の図'),
         ('**精度区分は地域で決まる**', '公差の判定図'),
         ('**分合筆1件、登録免許税2,000円**', '申請件数と登録免許税の比較図'),
         ('**自宅の駐車場は宅地**', '地目の判断の図'),
         ('**抵当権は建物の乙区**', '合筆の制限の図'),
         ('**申請人は相続人**', '申請人の図'),
         ('**（イ）は座標で求めた107.73**', '（イ）の地積の図'),
         ('**合筆後の32番4は156.12**', '分合筆の流れの図'),
         ('**登記識別情報が要るのは合筆**', '登記識別情報の整理図'),
         ('**地積測量図は分筆前の32番5だけ**', '地積測量図に描く範囲の図'),
         ('**G点・H点は後回しでいい**', '本番で解く順番の図')]
n_trap = len(re.findall(r'^- \*\*', text[text.index('## 第8章'):], re.M))
judge(f'まとめのワナの数 {n_trap} ＝ 対応表 {len(TRAPS)}', n_trap == len(TRAPS))
for t, mk in TRAPS:
    check('まとめのワナ', '- ' + t)
    judge(f'ワナの図がある : {t} → {mk}', any(m.startswith('> 【画像挿入】' + mk) for m in markers))
judge('ワナの図が重複していない（1つの図に2つのワナをまとめない）', len({mk for _, mk in TRAPS}) == len(TRAPS))
# ワナの図は、誤答を正す会話の直後にある（直前のセリフの決め手の語）
for mk, before in [('差し引く面積の比較図', '差し引く面積を取り違えただけで'), ('申請件数と登録免許税の比較図', 'それも2件ですね'),
                   ('地目の判断の図', '地目変更は要らないわ'), ('合筆の制限の図', '合筆の制限には当たらないの'),
                   ('申請人の図', '浪子さんは32番地5です'), ('（イ）の地積の図', '第4章で確かめたとおり公差の範囲内です'),
                   ('登記識別情報の整理図', '合筆が入っているから'), ('地積測量図に描く範囲の図', '描かなくていいの')]:
    i_ = next(k for k, l in enumerate(lines) if l.startswith('> 【画像挿入】' + mk))
    prev = [l for l in lines[:i_] if l.strip()][-1]
    judge(f'ワナの図が会話の直後 : {mk}（直前「{before}」）', before in prev)
# 誤答・比較の数値（自分で計算し直す）
BWr = (156.53 - 123.00) / abs(E - B)
Hw2, Gw2 = r2(B + (A - B) / abs(A - B) * BWr), r2(E + (F - E) / abs(F - E) * BWr)
for v in [f'H〈{Hw2.real:.2f}, {Hw2.imag:.2f}〉', f'G〈{Gw2.real:.2f}, {Gw2.imag:.2f}〉', f'甲区画{chiseki(area([B, C, D, E, Gw2, Hw2])):.2f}㎡']:
    check('差し引く面積の比較図（マーカー）', v)
judge('分筆＋合筆の2件・合筆＋分筆の2件はどちらも3,000円、分合筆1件は2,000円', 2000 + 1000 == 1000 + 2000 == 3000 and 2 * 1000 == 2000)
for v in ['不動産登記規則第35条第1号', '準則第68条第3号', '不動産登記法第41条第6号', '不動産登記法第30条']:
    check('条文（原典 note-articles/laws/ で確認済み）', v)
# 注の仕分け（第1章）
for v in ['問題文の注1（全て適法）', '問題文の注7（訂正・加入・削除の仕方）', '調査図素図の注2（G点はEとFを結ぶ直線上）',
          '調査図素図の注3（H点はAとBを結ぶ直線上）', '調査図素図の注4（本件土地1と本件土地2の筆界は聴取の時点で不明',
          'A市基準点成果表の注（北はX軸の正方向）', '任意座標の表の注（A′はA、B′はB、C′はCと同一の点）']:
    check('注の仕分け', v)
# 第4欄の地積測量図（答案用紙の書式で枠ごと描く）
for v in ["'第4欄'", '地　積　測　量　図', "'32番5'", 'Ａ市Ｂ町一丁目', '（令和２年○月○日作成）', "'申 請 人'", "'縮尺'", "'250'"]:
    check('第4欄の書式（作図スクリプト）', v, draw, '作図')
check('第4欄の会話（地番・土地の所在は自分で書く）', '地番の欄と土地の所在の欄も、印刷されていないから自分で書くのよ')
check('第4欄の枠の大きさ', '第4欄の図を描く枠は横約30cm・縦約23cm')
# 画像の中のタイトルに図番がない（全18枚）
titled = re.findall(r"(?:new_figure|suptitle|board\(\d+,)\(?\s*'([^']*)'", draw)
numbered = [x for x in titled if re.match(r'図\d', x)]
judge(f'作図スクリプトのタイトル {len(titled)}個（第4欄の地積測量図はタイトルなし）に図番がない : {numbered}',
      len(titled) == 17 and not numbered)
# 解答欄の画像の見出しは印刷どおり欄の名前だけ（問の内容はキャプション）
judge('第1欄の画像の見出しは「第1欄」だけ', '<div class="rt">第1欄</div>' in h1)
judge('第3欄の画像の見出しは「第3欄」だけ', '<div class="rt">第3欄</div>' in h3)
judge('申請書の画像の枠は min-height（高さを固定しない）', 'style="height:' not in html_k)
check('土地の表示の列幅（答案用紙の比）', '<col style="width:6%"><col style="width:18%"><col style="width:15%"><col style="width:15%"><col style="width:10%"><col style="width:36%">', html_k, '完成形画像')
# 電卓操作のキー列をそのまま実行して、直後の「表示：」と一致するか（tools/keysim_note_article.py）
from keysim_note_article import simulate  # noqa: E402
sim = simulate(os.path.join(HERE, 'note_R2_dai21mon_tochi_kaiwa_kaisetsu.md'))
judge(f'キー列を再現した表示の数 {len(sim)}（記事の「表示：」13個）', len(sim) == 13)
for n_, want, got, ok_ in sim:
    judge(f'キー列の再現 {n_}行目 : 記事「{want}」／ 再現「{got}」', ok_)

print('NG件数:', ng)
