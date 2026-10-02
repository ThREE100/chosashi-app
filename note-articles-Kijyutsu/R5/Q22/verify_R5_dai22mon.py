"""令和5年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第3欄 各階平面図・求積表）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R5/Q22/verify_R5_dai22mon.py"""
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P

ART = os.path.join(os.path.dirname(__file__), 'note_R5_dai22mon_tatemono_kaisetsu.md')
text = open(ART, encoding='utf-8').read()
ng = 0


def check(label, s):
    global ng
    ok = s in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label + ' : ' + s)


# 敷地（本件土地）の辺長：〔座標値一覧表〕A〜D（複素数モードでの検算）
A, B, C, D = P(50.00, 75.00), P(68.00, 75.00), P(68.00, 89.50), P(52.00, 88.00)
assert abs(B - A) == 18.0 and abs(C - B) == 14.5 and round(abs(A - D), 1) == 13.2
cd = abs(D - C)
assert round(cd, 1) == 16.1
cd_trunc = math.floor(cd * 1e4) / 1e4  # 表示値の「…」は切り捨て（qa-checklist-kijutsu.md 5章）
check('AB・BC・DA', 'ABは18.0メートル、BCは14.5メートル、DAは13.2メートル')
check('CD（丸め前）', f'{cd_trunc:.4f}… なので、四捨五入して 16.1メートル')

# 敷地は長方形ではない（A・DのX座標、C・DのY座標が異なる。アガルート解答例の注意点）
assert A.real != D.real and C.imag != D.imag
check('敷地の斜辺（A・D）', 'A点のXは50.00、D点は52.00')
check('敷地の斜辺（C・D）', 'C点のYは89.50、D点は88.00')
# 縮尺1/500：18.0m → 3.6cm
assert round(18.0 * 100 / 500, 1) == 3.6
check('縮尺換算', '18.0メートルなら図面上は3.6センチ')
# 建物図面の距離は小数点第1位（注4）。解答例の建物図面は 2.0・2.0・2.9
check('建物図面の距離', '『2.0』『2.0』『2.9』')

# 1階の求積（壁心）：東側0.90×9.00 ＋ 西側6.40×11.80（アガルート解答例・求積表と同じ分割）
a1, a2 = 0.90 * 9.00, 6.40 * 11.80
assert round(a1 + a2, 2) == 83.62
check('1階 東側', '0.90 × 9.00 ＝ 8.1000')
check('1階 西側', '6.40 × 11.80 ＝ 75.5200')
check('1階 合計', '合計：83.6200 （床面積：83.62平方メートル）')

# 2階の求積（壁心）：東側2.70×12.70 ＋ 西側4.60×11.80
b1, b2 = 2.70 * 12.70, 4.60 * 11.80
assert round(b1 + b2, 2) == 88.57
check('2階 東側', '2.70 × 12.70 ＝ 34.2900')
check('2階 西側', '4.60 × 11.80 ＝ 54.2800')
check('2階 合計', '合計：88.5700 （床面積：88.57平方メートル）')

# 一棟の建物の表示（工事前）の床面積：2階＝7.30×7.30＋4.60×4.50＝73.99（アガルート解答例と一致）
c1, c2 = 7.30 * 7.30, 4.60 * 4.50
assert round(c1 + c2, 2) == 73.99
check('一棟(工事前)2階 上側', '7.30かける7.30が53.29')
check('一棟(工事前)2階 下側', '4.60かける4.50が20.70')
check('一棟(工事前)2階 合計', '合計73.99平方メートルです')
check('一棟(工事前) 1階・2階', '1階83.62、2階73.99')

# 藍子の「全体から引く」計算：1階は欠け0.90×2.80（解答例 第3欄）なら結果は合う、2階は工事前の形の面積になる
assert round(7.30 * 11.80 - 0.90 * 2.80, 2) == 83.62
assert round(7.30 * 11.80 - 2.70 * 4.50, 2) == 73.99
check('藍子の1階（欠けの寸法）', '欠けている部分（0.90かける2.80）')

# 原因及びその日付（解答例 第2欄の2行目）
check('原因及びその日付', '『②③令和5年10月6日構造変更、増築、3番9の2を合併』')


def poly_area(pts):
    n = len(pts)
    return abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2


# 解説図プロンプト（図3・図4・図6）の頂点座標（Y＝東、X＝南、上が北）が求積表と一致すること
FIG = os.path.join(os.path.dirname(__file__), 'prompt_R5_dai22mon_kaisetsuzu.md')
fig = open(FIG, encoding='utf-8').read()
for label, pts, area in [
    ('図3 1階', [(0, 0), (6.4, 0), (6.4, 2.8), (7.3, 2.8), (7.3, 11.8), (0, 11.8)], 83.62),
    ('図4 2階', [(0, 0), (7.3, 0), (7.3, 12.7), (4.6, 12.7), (4.6, 11.8), (0, 11.8)], 88.57),
    ('図6 2階(工事前)', [(0, 0), (7.3, 0), (7.3, 7.3), (4.6, 7.3), (4.6, 11.8), (0, 11.8)], 73.99),
]:
    assert round(poly_area(pts), 2) == area, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    ok = s in fig
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label + ' 頂点座標（面積' + f'{area}） : ' + s)
# 増築で増えた部分（2.70×5.40）＝88.57−73.99
assert round(2.70 * (12.70 - 7.30), 2) == round(88.57 - 73.99, 2) == 14.58

# 形状は東西南北で説明する（図面の上＝北。問題の図1・解答例の建物図面の方位記号で確認）
check('1階の欠けの位置', '1階は北東の角（玄関前）が少し欠けている')
check('2階の張り出しの向き', '1階の11.80メートルより南へ0.90メートル張り出している')
for bad in ['右上の玄関前', '下に長くなってる', '南東の0.90', '2.00』『2.00']:
    ok = bad not in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '禁止語なし : ' + bad)

# タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜
title = text.splitlines()[0]
prefix = '# 【土地家屋調査士受験生向け】令和5年度問題22（建物）〜'
ok = title.startswith(prefix) and title.endswith('〜') and len(title[len(prefix):-1]) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + 'タイトル形式 : ' + title)

# ---- 2026-09-29 追加作業：最新の執筆プロンプト・アガルートの解説と照らし合わせて追記した内容 ----
check('解く順番', 'まず問1から問4までをざっと読んで')
check('一の申請の根拠', '不動産登記規則第35条第7号')
check('〔調査図〕の（注）3（両側被覆）', '〔調査図〕の（注）3で、鉄骨は両側が被覆されているから')
check('問題文の注4（各階平面図）', '小数点第2位までね（問題文の注4）')
check('問題文の注4（建物図面）', '小数点第1位まで（問題文の注4）')
# 注の書き分け：「注」の前に「問題文の」か「〔調査図〕の（」が付いていること
import re as _re
bare = [m.start() for m in _re.finditer(r'注', text) if not (text[max(0, m.start() - 4):m.start()] == '問題文の' or text[max(0, m.start() - 7):m.start()] == '〔調査図〕の（')]
ng += bool(bare)
print(('OK ' if not bare else 'NG ') + f'注の書き分け（問題文の注／〔調査図〕の（注））: 書き分けのない「注」{len(bare)}か所')
# 建物の位置：外壁までの距離と壁の中心線（壁厚0.15の半分）から、建物が3番9の中に収まることを確かめる
n_ext = 68 - 2.0
s_ext = round(n_ext - 11.80 - 0.15, 2)
y_cd = 88 + (s_ext - 52) * 1.5 / 16
e_ext = y_cd - 2.9
w_ext = e_ext - 7.30 - 0.15
assert s_ext == 54.05 and round(y_cd, 2) == 88.19 and round(e_ext, 2) == 85.29 and round(w_ext, 2) == 77.84
assert round(w_ext - 75, 1) == 2.8 and round(s_ext - (50 + 2 * (e_ext - 75) / 13), 1) == 2.5   # 辺ABまで約2.8、辺ADまで南東の角で約2.5（最小）
check('辺ADまでの最小', 'いちばん狭い南東の角で約2.5')
check('所在の確認', '建物は全部3番9の中。所在は3番地9だけ')
check('建物の位置（南の外壁）', 'X＝54.05')
check('各階平面図の1階の位置', '1階の位置を点線で重ねる')
check('家屋番号の欄', '家屋番号の欄は空けておく')
check('添付書類の根拠', '不動産登記令別表14の項添付情報欄ロ、16の項添付情報欄イ')
check('登記識別情報は1個で足りる', '不動産登記令第8条第2項第3号')
check('印鑑証明書の根拠', '同令第16条第2項、不動産登記規則第47条第3号イ（6）')
check('登録免許税の根拠', '登録免許税法別表第一の一（十三）ロ')
check('登録免許税「不要」のわな', '問2のただし書きどおり『不要』ですか？')
check('種類：居宅と共同住宅', '「二世帯住宅で、ふた家族が住んでいるから……『共同住宅』ですか？」')
check('3番9の1の4.61', '1階の北寄りにある階段室と、北側の玄関だけが3番9の1の部分')
check('問4の穴埋め', '①規約証明書、②敷地権、③敷地利用権、④分離、⑤処分')
check('問4の根拠', '不動産登記令別表12の項添付情報欄ホ')
for bad in ['非課税ですか', '階層に入れたり', '✕', '✓', '名変']:
    ok = bad not in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '禁止語なし : ' + bad)

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')
prev = None
for i, line in enumerate(lines):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        ok = line != prev
        ng += (not ok)
        if not ok:
            print('NG 同じ話者の連続 :', i + 1)
        prev = line

# ---- 画像（2026-10-02更新）：記事の画像挿入マーカー12か所と zu/ のPNGが、記事の順に対応しているか ----
from PIL import Image
ZU = os.path.join(os.path.dirname(__file__), 'zu')
fig_src = open(os.path.join(os.path.dirname(__file__), 'prompt_R5_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form_src = open(os.path.join(os.path.dirname(__file__), 'prompt_R5_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R5_dai22mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R5_dai22mon_zu01_toku_junban', '本番で解く順番', (1600, 800)),
        ('R5_dai22mon_zu02_shikichi_henchou', '作図チェック用に計算した4辺の長さ', (1600, 1100)),
        ('R5_dai22mon_zu03_tatemono_zumen', '建物図面の完成形（答案用紙の第3欄の建物図面の枠の中）', (1600, 1400)),
        ('R5_dai22mon_zu04_ayamari_hikaku', '左に「誤り＝全体7.30×11.80から2.70×4.50を引く', (1600, 950)),
        ('R5_dai22mon_zu05_1kai_kyuuseki', '1階の床面積求積図', (1600, 1100)),
        ('R5_dai22mon_zu06_2kai_kyuuseki', '2階の床面積求積図', (1600, 1100)),
        ('R5_dai22mon_zu07_kakukai_heimenzu', '各階平面図の完成形（答案用紙の第3欄の各階平面図の枠の中）', (1800, 1100)),
        ('R5_dai22mon_zu08_2kai_kouji_zengo', '工事前と工事完了後で左右に並べた比較図', (1600, 950)),
        ('R5_dai22mon_toukishinseisho_machigai', '①誤答', 'tall'),
        ('R5_dai22mon_toukishinseisho_kansei', '第2欄（問2）の登記申請書の完成形', 'tall'),
        ('R5_dai22mon_dai4ran_kansei', '第4欄（問4）の完成形', 'wide')]
ok = len(markers) == len(PNGS)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}')
for (name, key, size), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        ok = (w == 1200 and h > w) if size == 'tall' else (w == 1200 and h < w) if size == 'wide' else (w, h) == size
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'PNG（マーカー順・大きさ） : {name}')
    src = fig_src if '_zu' in name else (form_src if 'kansei' in name else None)
    if src is not None:
        ok = f'zu/{name}.png' in src
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'プロンプトにファイル名 : zu/{name}.png')
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
ok = not extra
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'zu/ に記事で使わないPNGがない : {extra}')

# ---- 問1（第1欄）・問4（第4欄）の答えを会話で明示しているか（2026-10-02追加）----
check('問1 ア〜オ', 'アは『合併』、イは『構造上の独立性』、ウは『合体』、エは『権利』、オは『接続』です！')
check('問1 エの条文', '不動産登記法第56条第5号')
check('問1 オの条文', '不動産登記事務取扱手続準則第86条第2号')
check('問4 ①〜⑤', '穴埋めは①規約証明書、②敷地権、③敷地利用権、④分離、⑤処分')
check('第3欄の上の欄', '家屋番号は空欄、建物の所在は『A市B町一丁目3番地9』ですね')
check('各階平面図の完成形', '屋根裏部屋は床面積に入らないから、3階として描いたりしません')
check('解く順番', '床面積を出さないと申請書の床面積の欄が埋まらないから、図面が先なんですね')

def html_has(name, *needles):
    global ng
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        ok = n in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : {n}')


html_has('R5_dai22mon_toukishinseisho_kansei', '区分建物表題部変更・合併登記', '建物図面　各階平面図　登記識別情報　印鑑証明書',
         '所有権証明書　代理権限証書', '令和５年10月12日　申請　　Ａ地方法務局', 'Ａ市Ｂ町一丁目３番地９　甲田栄一', '金1,000円',
         '軽量鉄骨造陸屋<br>根２階建', '73</span>', '>99<', '②③令和5年10月6日構造変更、増築、3番9の2を合併',
         '3番9の1に合併', '所在　　（省略）', '記載不要', '1階部分', '>74<', '>72<', '>4<', '>61<', '>70<', '>21<',
         '2階　88', '>57<', '居宅')
html_has('R5_dai22mon_dai1ran_kansei', '第1欄', '>合併<', '>構造上の独立性<', '>合体<', '>権利<', '>接続<')
html_has('R5_dai22mon_dai4ran_kansei', '第4欄', '>規約証明書<', '>敷地権<', '>敷地利用権<', '>分離<', '>処分<')
html_has('R5_dai22mon_toukishinseisho_machigai', '令和5年10月6日増築、3番9の2を合併', '∨②③', '∨構造変更、',
         '②③令和5年10月6日構造変更、増築、3番9の2を合併')
h = open(os.path.join(ZU, 'R5_dai22mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
ok = h.count('記載不要') == 2
ng += (not ok)
print(('OK ' if ok else 'NG ') + '「記載不要」は敷地権の目的である土地の表示と敷地権の表示の2か所')

# ---- 見出し画像のプロンプトの文字がタイトルと同じか ----
thumb = open(os.path.join(os.path.dirname(__file__), 'prompt_R5_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
sub = title[len(prefix):-1]
for n in ['令和5年度問題22（建物）', '〜' + sub + '〜', '土地家屋調査士受験生向け']:
    ok = n in thumb
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '見出し画像の文字 : ' + n)

# ---- 解説図プロンプトの頂点座標とファイル名 ----
for n in ['R5_dai22mon_zu02_shikichi_henchou', 'R5_dai22mon_zu08_2kai_kouji_zengo', '1階の位置を点線で重ねる',
          'X＝54.05の高さで辺CDはY＝88＋（54.05−52）×1.5÷16＝88.1921…']:
    ok = n in fig
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '解説図プロンプト : ' + n)

print('NG件数:', ng)
