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
judge(f'解説図プロンプトの図の数 {n_fig}枚（9枚）', n_fig == 9)
for i in range(1, 10):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R2_dai21mon_zu0{i}_') and f.endswith('.png')
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

# ---- 注の番号の書き分け（問題文の注） ----
bare = [m.group(0) for m in re.finditer(r'(?<!問題文の)注[0-9]', text)]
judge(f'注の番号はすべて「問題文の注N」と書き分けている（書き分けていないもの: {bare}）', not bare)

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
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図9＋添削1＋完成形1＝計11か所の想定）', n_marker == 11)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和2年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和2年度問題21（土地）', thumb, '見出し画像')
check('添削画像の記事タイトル', title[2:], fix, '添削')

print('NG件数:', ng)
