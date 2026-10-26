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
check('建物図面の距離', '『2.0』『2.0』『2.9』と書くの')
check('藍子の誤答（距離の桁）', '『2.00』『2.00』『2.90』と書き写します')

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
    ('図16・図19 1階', [(0, 0), (6.4, 0), (6.4, 2.8), (7.3, 2.8), (7.3, 11.8), (0, 11.8)], 83.62),
    ('図17・図19 2階', [(0, 0), (7.3, 0), (7.3, 12.7), (4.6, 12.7), (4.6, 11.8), (0, 11.8)], 88.57),
    ('図21 2階(工事前)', [(0, 0), (7.3, 0), (7.3, 7.3), (4.6, 7.3), (4.6, 11.8), (0, 11.8)], 73.99),
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
check('2階の張り出しの向き', '東側の部分だけが、1階の11.80メートルより南へ0.90メートル張り出している')
for bad in ['右上の玄関前', '下に長くなってる', '南東の0.90']:
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
check('〔調査図〕の（注）3（両側被覆）', '〔調査図〕の（注）3を読みなさい。鉄骨は両側が被覆されている')
check('問題文の注4（各階平面図）', '小数点第2位までね（問題文の注4）')
check('問題文の注4（建物図面）', '建物図面に記載する距離は、小数点第1位までと書いてある')
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
check('種類：居宅と共同住宅', '二世帯住宅でふた家族が住んでいるから……『共同住宅』ですか？')
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

# ---- 画像（2026-10-26更新）：記事の画像挿入マーカー32か所と zu/ のPNGが、記事の順に対応しているか ----
from PIL import Image
ZU = os.path.join(os.path.dirname(__file__), 'zu')
fig_src = open(os.path.join(os.path.dirname(__file__), 'prompt_R5_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form_src = open(os.path.join(os.path.dirname(__file__), 'prompt_R5_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R5_dai22mon_zu01_gattai_gappei', '「合体」と「合併」の比較図', (1700, 640)),
        ('R5_dai22mon_zu02_gappei_seigen', '合併の制限3つの確認図', (1700, 600)),
        ('R5_dai22mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R5_dai22mon_zu03_yaneura_fusanyuu', '屋根裏部屋の判定図', (1700, 820)),
        ('R5_dai22mon_zu04_kouji_shiwake', '工事(1)〜(5)の仕分け表', (1700, 860)),
        ('R5_dai22mon_zu05_chuu_shiwake', '問題文の注と〔調査図〕の（注）の仕分け図', (1700, 900)),
        ('R5_dai22mon_zu06_toku_junban', '本番で解く順番の図', (1600, 800)),
        ('R5_dai22mon_zu07_shikichi_henchou', '作図チェック用に計算した4辺の長さ', (1600, 1100)),
        ('R5_dai22mon_zu08_kyori_keta', '距離の桁の比較図', (1700, 640)),
        ('R5_dai22mon_zu09_shozai_kakunin', '建物の位置の確認図', (1600, 1100)),
        ('R5_dai22mon_zu10_kakumono_kakanaimono', '建物図面に書くもの・書かないものの整理図', (1700, 620)),
        ('R5_dai22mon_zu11_tatemono_zumen', '建物図面の完成形（答案用紙の第3欄の建物図面の枠の中）', (1200, 2100)),
        ('R5_dai22mon_zu12_uchinori_kabeshin', '床面積の測り方の比較図', (1700, 880)),
        ('R5_dai22mon_zu13_ryougawa_hifuku', '両側被覆の説明図', (1700, 880)),
        ('R5_dai22mon_zu14_ayamari_hikaku', '左に「誤り＝全体7.30×11.80から2.70×4.50を引く', (1600, 950)),
        ('R5_dai22mon_zu15_2kai_sunpou_tashizan', '2階の4辺の寸法を足し算で検算する図', (1600, 1100)),
        ('R5_dai22mon_zu16_1kai_kyuuseki', '1階の床面積求積図', (1600, 1100)),
        ('R5_dai22mon_zu17_2kai_kyuuseki', '2階の床面積求積図', (1600, 1100)),
        ('R5_dai22mon_zu18_1kai_no_ichi', '2階の図に重ねる1階の位置の説明図', (1600, 1100)),
        ('R5_dai22mon_zu19_kakukai_heimenzu', '各階平面図の完成形（答案用紙の第3欄の各階平面図の枠の中）', (1200, 2100)),
        ('R5_dai22mon_zu20_ittou_hyouji', '一棟の建物の表示の整理図', (1700, 880)),
        ('R5_dai22mon_zu21_2kai_kouji_zengo', '工事前と工事完了後で左右に並べた比較図', (1600, 950)),
        ('R5_dai22mon_zu22_tenpu_shorui', '添付書類6点の一覧表', (1700, 960)),
        ('R5_dai22mon_zu23_toukishikibetsu', '登記識別情報の説明図', (1700, 620)),
        ('R5_dai22mon_zu24_touroku_menkyozei', '登録免許税の説明図', (1700, 640)),
        ('R5_dai22mon_zu25_kubun_3gyou', '区分した建物の表示3行の整理図', (1700, 840)),
        ('R5_dai22mon_zu26_shurui_kyotaku', '種類の判断図', (1700, 660)),
        ('R5_dai22mon_toukishinseisho_machigai', '①誤答', 'tall'),
        ('R5_dai22mon_zu27_shikichiken_fuyou', '敷地権の欄の説明図', (1700, 680)),
        ('R5_dai22mon_toukishinseisho_kansei', '第2欄（問2）の登記申請書の完成形', 'tall'),
        ('R5_dai22mon_zu28_kiyaku_shoumeisho', '問4の説明図', (1700, 680)),
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
check('問1 ア〜オ', 'エは『権利』、オは『接続』です。アは『合併』、イは『構造上の独立性』、ウは『合体』')
check('問1 エの条文', '所有権等の登記以外の権利に関する登記がある建物は同条第5号')
check('問1 所有者の条文', '不動産登記法第56条第2号')
check('問1 オの条文', '不動産登記事務取扱手続準則第86条第2号')
check('問4 ①〜⑤', '穴埋めは①規約証明書、②敷地権、③敷地利用権、④分離、⑤処分')
check('第3欄の上の欄', '家屋番号は空欄よ！')
check('第3欄の所在', '建物の所在は『A市B町一丁目3番地9』')
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
         '所有権証明書　代理権限証書', '令和5年10月12日　申請　Ａ地方法務局', 'Ａ市Ｂ町一丁目３番地９　甲田栄一', '金1,000円',
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
for n in ['R5_dai22mon_zu07_shikichi_henchou', 'R5_dai22mon_zu21_2kai_kouji_zengo', '1階の位置を点線で重ねる',
          'X＝54.05の高さで辺CDはY＝88＋（54.05−52）×1.5÷16＝88.1921…']:
    ok = n in fig
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '解説図プロンプト : ' + n)

# ---- 試験の答案用紙（touan_youshi/。2026-10-02受領）の欄の形・印刷文字と、画像・作図スクリプトの一致 ----
import pymupdf
HERE = os.path.dirname(__file__)
pdf = pymupdf.open(os.path.join(HERE, 'touan_youshi', 'R5_dai22mon_touan_youshi.pdf'))
p1, p2 = (pg.get_text() for pg in pdf)
flat1 = p1.replace('\n', '')
for n in ['第1 欄', '第2 欄', '第4 欄', '登記の目的', '添付書類', '令和5 年10 月12 日', '申請　Ａ地方法務局', '登録免許税',
          '①構　造', '②床　　面　　積', '建物の名称', '所在　（省略）', '（省略）', '②所在及び地番', '③地目', '①種類',
          '②敷地権の種類', '③敷地権の割合', '主たる', '建物又', 'は附属']:
    ok = n in p1 or n in flat1
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '答案用紙1ページ目の印刷 : ' + n)
ok = '主である' not in p1
ng += (not ok)
print(('OK ' if ok else 'NG ') + '答案用紙の見出しは「主たる建物又は附属建物」（「主である」ではない）')
for n in ['第3 欄', '各　 階　 平　 面　 図', '建　 物　 図　 面', '家屋番号', '建物の所在', '作成者', '申請人', '縮尺',
          '（略）', '（令和5 年〇月〇日作成）', '250', '500']:
    ok = n in p2
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '答案用紙2ページ目の印刷 : ' + n)
ok = p2.count('（略）') == 2 and p2.count('家屋番号') == 1 and p2.count('建物の所在') == 1
ng += (not ok)
print(('OK ' if ok else 'NG ') + '第3欄：（略）は作成者・申請人の2か所、家屋番号・建物の所在の欄は1つずつ（建物図面の側、各階平面図と兼用）')
# 作図スクリプト（第3欄の枠）が答案用紙どおりか
draw = open(os.path.join(ZU, 'draw_R5_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
for n in ["PRINT_SAKUSEI = ('（略）', '（令和5年〇月〇日作成）', '250')", "PRINT_SHINSEI = ('（略）', '500')",
          "'家屋番号'", "'建物の所在'", "'作　成　者'", "'申　請　人'", "'各　階　平　面　図'", "'建　物　図　面'",
          "sheet_frame(m, 'right')", "sheet_frame(m, 'left')", "../touan_youshi/"]:
    ok = n in draw
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '作図スクリプトの第3欄の枠 : ' + n)
for n, cnt in [("'家屋番号'", 1), ("'建物の所在'", 1)]:
    ok = draw.count(n) == cnt
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'作図スクリプト：{n} の欄は1か所（建物図面の側だけ）')
# 申請書・第1欄・第4欄のHTMLの欄の形
html_has('R5_dai22mon_toukishinseisho_kansei', '主たる<br>建物又<br>は附属<br>建　物', 'class="omitbox">所在　　（省略）</div>（省略）',
         '家屋<br>番号', '建物の<br>名　称', '①土　地<br>の符号', '④地　積<br>m²', '②床　面　積', '>（略）<', '登録免許税',
         '>①土地の符号<', '>②敷地権の種類<', '>③敷地権の割合<')
html_has('R5_dai22mon_toukishinseisho_machigai', '主たる<br>建物又<br>は附属<br>建　物', 'class="omitbox">所在　　（省略）</div>（省略）')
for name in ['R5_dai22mon_toukishinseisho_kansei', 'R5_dai22mon_toukishinseisho_machigai']:
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    ok = '主である' not in h
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{name}.html : 「主である」が残っていない')
h = open(os.path.join(ZU, 'R5_dai22mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
order = ['登記の目的', '添 付 書 類', '令和5年10月12日　申請　Ａ地方法務局', '申　請　人', '代　理　人', '登録免許税',
         '一棟の建物の表示', '敷地権の目的である', '区分した建物の表示', '敷地権の表示</td>']
pos = [h.find(n) for n in order]
ok = all(p >= 0 for p in pos) and pos == sorted(pos)
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書の欄の順序（答案用紙の左の列→右の列）: ' + str(pos))
for name, marks in [('R5_dai22mon_dai1ran_kansei', ['ア', 'イ', 'ウ', 'エ', 'オ']), ('R5_dai22mon_dai4ran_kansei', ['①', '②', '③', '④', '⑤'])]:
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    rows = h.count('<tr>')
    ok = rows == 3 and 'class=none colspan=2' in h and all(f'<td class="k">{k}</td>' in h for k in marks)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'{name}.html : 2組ずつ横に並ぶ3段（3段目の右は欄なし）、記号{"".join(marks)}')
# 記事：答案用紙の印刷に触れた会話
check('第3欄は1枚の左右', '第3欄は1枚の用紙で、左半分が各階平面図、右半分が建物図面')
check('申請人の（略）と縮尺', '下の申請人の欄には『（略）』が、縮尺の欄には『1／500』がもう印刷されている')
check('作成者の（略）と縮尺', '作成者の欄には『（略）』と作成の日付、縮尺の欄には『1／250』がもう印刷されている')
check('区分した建物の表示の2行目の印刷', '家屋番号と建物の名称の欄にまたがる点線の枠の『所在　（省略）』と、家屋番号の欄の『（省略）』')
# 「仮」の欄の形・答案用紙がないという記述が残っていないこと
for fn in ['note_R5_dai22mon_tatemono_kaisetsu.md', 'prompt_R5_dai22mon_kaisetsuzu.md', 'prompt_R5_dai22mon_toukishinseisho_gazou.md',
           'prompt_R5_dai22mon_toukishinseisho_machigai.md', 'zu/draw_R5_dai22mon_kaisetsuzu.py', 'zu/make_R5_dai22mon_shinseisho_gazou.py']:
    t = open(os.path.join(HERE, fn), encoding='utf-8').read()
    bad = [w for w in ['仮の', '（仮）', '仮の形', 'リポジトリにない', 'にならった', '令和何年', '確かめたら合わせて直す', '確かめたら、ここと'] if w in t]
    ok = not bad
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'「仮」の記述なし : {fn} {bad}')


# ======================================================================
# 2026-10-26：最新の基準（qa-checklist-kijutsu.md の6-2・6-3）で足した確認
# ======================================================================
import re
from decimal import Decimal
# 6-3：作図スクリプトのタイトルに「図N」がない（画像の中に図番を入れない）
bad_titles = re.findall(r"(?:fixed_figure|new_figure|suptitle|set_title)\(\s*'[^']*図\d", draw) + \
    re.findall(r"(?:card_figure|table_figure)\(\s*'[^']*',\s*'[^']*図\d", draw)
ok = not bad_titles
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[作図スクリプト] タイトルに図番がない : {bad_titles}')
# 6-2：まとめ26項目（1項目1わな）と、わな→図の対応表（TRAPS）
TRAPS = [
    ('合体ではなく合併', 'くっつけるから『合体』ですか？', 'R5_dai22mon_zu01_gattai_gappei', '区分建物の合併'),
    ('所有者・権利の登記・接続', '所有者はどちらも甲田栄一さんで同じ', 'R5_dai22mon_zu02_gappei_seigen', '準則第86条第2号'),
    ('問1のウは合体', 'じゃあ問1ですね。', 'R5_dai22mon_dai1ran_kansei', '合体したとみることはできません'),
    ('屋根裏部屋は天井の最高部1.40', '3階建にします！', 'R5_dai22mon_zu03_yaneura_fusanyuu', '同準則第81条第4項'),
    ('原因に書く増築と構造変更', 'じゃあ、工事の(1)から(5)まで', 'R5_dai22mon_zu04_kouji_shiwake', '仕分けを思い出しなさい'),
    ('問題文の注と〔調査図〕の（注）は番号がかぶる', '『〔調査図〕の（注）1〜10』の2種類', 'R5_dai22mon_zu05_chuu_shiwake', '3つよ'),
    ('本番は問を読み', '時間配分も知りたいです', 'R5_dai22mon_zu06_toku_junban', '床面積が間に合わなくても書けるわよ'),
    ('敷地の辺ADと辺CDは斜め', '調査図の図1だと長方形に見えるのに', 'R5_dai22mon_zu07_shikichi_henchou', '建物図面には書かない'),
    ('距離の桁は', '『2.00』『2.00』『2.90』と書き写します', 'R5_dai22mon_zu08_kyori_keta', '同じ距離でも図面ごとに桁が違う'),
    ('建物は座標で確かめて', '所在は『3番地9』だけですね', 'R5_dai22mon_zu09_shozai_kakunin', '所在は3番地9だけ、でいいわ'),
    ('建物図面に敷地の辺長と家屋番号を書かない', '家屋番号は『3番9』と書いて', 'R5_dai22mon_zu10_kakumono_kakanaimono', '縮尺も書かなくていいわ'),
    ('区分建物でなくなると', '足せば1階の床面積になりませんか？', 'R5_dai22mon_zu12_uchinori_kabeshin', '壁心で測り直しなさい'),
    ('鉄骨が両側被覆', '0.075ずつ足したり引いたりしたほうが', 'R5_dai22mon_zu13_ryougawa_hifuku', 'それこそ誤りよ'),
    ('全体から引かず', '私、天才かも', 'R5_dai22mon_zu14_ayamari_hikaku', 'リビング拡張'),
    ('2階の東側は3.71', '東側の縦の寸法が『3.71』', 'R5_dai22mon_zu15_2kai_sunpou_tashizan', '足し算してから拾い直す'),
    ('2階の図に重ねる1階の位置', '点線で描くのは、どこですか？', 'R5_dai22mon_zu18_1kai_no_ichi', '△印（南西の角）'),
    ('一棟の建物の表示は工事前', '床面積は、さっき出した83.62と88.57でいいんですか？', 'R5_dai22mon_zu20_ittou_hyouji', '計算し直すのよ'),
    ('一棟の建物の表示の2階は、工事前の73.99', '合計73.99平方メートルです', 'R5_dai22mon_zu21_2kai_kouji_zengo', '増築前の形なら正しかった'),
    ('添付書類は6点', '添付書類は何を付ければいいですか？', 'R5_dai22mon_zu22_tenpu_shorui', '不動産登記規則第47条第3号イ（6）'),
    ('登記識別情報は', '2つとも出すんですか？', 'R5_dai22mon_zu23_toukishikibetsu', '登記識別情報』だけでいいのよ'),
    ('登録免許税は、不要ではなく', 'どおり『不要』ですか？', 'R5_dai22mon_zu24_touroku_menkyozei', '甲田栄一さんね'),
    ('区分した建物の表示は3行', '合併後の建物で、3行ですか？', 'R5_dai22mon_zu25_kubun_3gyou', '83.62と88.57よ'),
    ('合併後の種類は共同住宅ではなく居宅', '『共同住宅』ですか？', 'R5_dai22mon_zu26_shurui_kyotaku', '居宅のままよ'),
    ('原因は構造変更を落とさず', '工事が終わった日だから', 'R5_dai22mon_toukishinseisho_machigai', '変えるのを忘れないことね'),
    ('敷地権の2つの欄', '全部空欄でいいですか？', 'R5_dai22mon_zu27_shikichiken_fuyou', '『記載不要』と書くの'),
    ('問4は', '追加で何を提供すべき？', 'R5_dai22mon_zu28_kiyaku_shoumeisho', '不動産登記令別表12の項添付情報欄ホ'),
]
matome = text.split('今日のまとめよ。わなを1つずつ並べるわ」')[1].split('**藍子**')[0]
items = [l[2:] for l in matome.splitlines() if l.startswith('- ')]
ok = len(items) == len(TRAPS) == len({p_ for _, _, p_, _ in TRAPS}) and all(k in it for (k, _, _, _), it in zip(TRAPS, items))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'まとめのわな{len(items)}項目と、わな→図の対応表{len(TRAPS)}組（図の重複なし・同じ順）')
ok = all(it.count('。') == 0 and it.count('、') <= 3 for it in items)
ng += (not ok)
print(('OK ' if ok else 'NG ') + 'まとめの1項目に1つのわな')
mk_pos = [m_.start() for m_ in re.finditer(r'^> 【画像挿入】.*$', text, re.M)]
order_png = [n_ for n_, _, _ in PNGS]
for key, phrase, png, word in TRAPS:
    pos = text.find(phrase)
    after = [k_ for k_, p_ in enumerate(mk_pos) if p_ > pos][:3]
    k_png = order_png.index(png)
    ok = pos >= 0 and k_png in after and '\n## ' not in text[pos:mk_pos[k_png]]
    prev = [l_ for l_ in text[:mk_pos[k_png]].splitlines() if l_.strip()][-1]
    ok2 = word in prev
    ng += (not ok) + (not ok2)
    print(('OK ' if ok else 'NG ') + f'わなの会話のあと3つ以内のマーカーに図がある : {phrase[:16]}… → {png}')
    print(('OK ' if ok2 else 'NG ') + f'わなの図のマーカーの直前の段落に決め手の語 : {word[:20]}')
# 図番号が記事の順（PNG名の zuNN が昇順）
nums = [int(m_.group(1)) for n_ in order_png for m_ in [re.search(r'_zu(\d+)_', n_)] if m_]
ok = nums == sorted(nums) == list(range(1, 29))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'図番号（PNG名）が記事の順に1〜28で並ぶ : {nums}')
# 6-3：申請書・添削のHTMLに inline の height がなく（min-height）、「第○欄」の見出しがない（第1欄・第4欄だけ印刷どおり）
mk = open(os.path.join(ZU, 'make_R5_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
htmls = {f_[:-5]: open(os.path.join(ZU, f_), encoding='utf-8').read() for f_ in os.listdir(ZU) if f_.endswith('.html')}
ok = 'style="height:' not in mk and not any('style="height:' in h_ for h_ in htmls.values())
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書・添削のHTMLに style="height: がない（min-height）')
ok = all('第1欄' not in h_ and '第2欄' not in h_ for n_, h_ in htmls.items() if 'dai1ran' not in n_ and 'dai4ran' not in n_)
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書・添削のHTMLに「第○欄」の見出しがない（第1欄・第4欄の画像だけ印刷どおり入れる）')
# 6-3：答案用紙の原本PDFの罫線から測った列の幅の比・行の高さと、HTMLの値の一致
pg = pdf[0]
segs = []
for d_ in pg.get_drawings():
    for it_ in d_['items']:
        if it_[0] == 'l':
            a_, b_ = it_[1], it_[2]
            if abs(a_.x - b_.x) < 0.8 and abs(a_.y - b_.y) > 8:
                segs.append(('v', round((a_.x + b_.x) / 2, 1), min(a_.y, b_.y), max(a_.y, b_.y)))
            elif abs(a_.y - b_.y) < 0.8 and abs(a_.x - b_.x) > 8:
                segs.append(('h', round((a_.y + b_.y) / 2, 1), min(a_.x, b_.x), max(a_.x, b_.x)))
        elif it_[0] == 're':
            r_ = it_[1]
            if r_.width < 1.5 and r_.height > 8:
                segs.append(('v', round(r_.x0 + r_.width / 2, 1), r_.y0, r_.y1))
            elif r_.height < 1.5 and r_.width > 8:
                segs.append(('h', round(r_.y0 + r_.height / 2, 1), r_.x0, r_.x1))
            elif r_.width > 1.5 and r_.height > 8:
                segs += [('v', round(r_.x0, 1), r_.y0, r_.y1), ('v', round(r_.x1, 1), r_.y0, r_.y1),
                         ('h', round(r_.y0, 1), r_.x0, r_.x1), ('h', round(r_.y1, 1), r_.x0, r_.x1)]


def xs_of(y0, y1, x0, x1):
    return sorted({s_[1] for s_ in segs if s_[0] == 'v' and s_[2] <= y1 - 3 and s_[3] >= y0 + 3 and x0 - 1 <= s_[1] <= x1 + 1})


def ys_of(x0, x1, y0, y1):
    return sorted({s_[1] for s_ in segs if s_[0] == 'h' and s_[2] <= x1 - 5 and s_[3] >= x0 + 5 and y0 - 1 <= s_[1] <= y1 + 1})


def pct_of(xs):
    return [100 * (b_ - a_) / (xs[-1] - xs[0]) for a_, b_ in zip(xs, xs[1:])]


def css_cols(table_marker):
    seg_ = mk[mk.index(table_marker):]
    seg_ = seg_[:seg_.index('</colgroup>')]
    return [float(v_) for v_ in re.findall(r'width:([\d.]+)%', seg_)]


for label, xs_, want in [('一棟の建物の表示', xs_of(621, 791, 176, 650), css_cols('ITTOU_COLS = (')),
                         ('敷地権の目的である土地の表示', xs_of(78, 215, 670, 1145), css_cols("'<table class=\"t mokuteki\">")),
                         ('区分した建物の表示', xs_of(227, 482, 670, 1145), css_cols('KUBUN_COLS = (')),
                         ('敷地権の表示', xs_of(485, 624, 670, 1145), css_cols('class="t stack shiki"'))]:
    got_ = pct_of(xs_)
    if label == '敷地権の目的である土地の表示':
        got_ = pct_of([671.5, 698.4, 749.4, 858.6, 923.7, 991.8, 1032.9, 1143.4])   # 地積の点線を含む7区切り
    if label == '一棟の建物の表示':
        got_ = pct_of([177.0, 204.0, 269.2, 321.6, 389.6, 430.7, 449.2, 498.8, 539.9, 649.0])
    if label == '区分した建物の表示':
        got_ = pct_of([671.5, 698.4, 749.4, 800.4, 851.5, 896.8, 964.8, 1025.8, 1054.1, 1143.4])
    ok = len(got_) == len(want) and all(abs(a_ - b_) < 0.35 for a_, b_ in zip(got_, want))
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'列の幅の比（{label}）：原本から測ると {[round(v_, 1) for v_ in got_]}（HTML {want}）')
# 行の高さ（倍率2.288）
SC = 1080 / 472.0
for label, ys_, css_keys in [('一棟の建物の表示', ys_of(177, 649, 615, 795), ['table.ittou td.val {{ height: 65px; }}', 'table.ittou td.nm {{ height: 52px; }}',
                                                                       'table.ittou td.head {{ height: 68px; }}', 'table.ittou td.entry {{ height: 139px; }}']),
                             ('敷地権の目的である土地の表示', ys_of(671, 1144, 75, 216), ['table.mokuteki td.head {{ height: 117px; }}', 'table.mokuteki td.entry {{ height: 195px; }}']),
                             ('区分した建物の表示', ys_of(671, 1144, 225, 483), ['table.kubun td.head {{ height: 123px; }}', 'table.kubun td.entry {{ height: 156px; }}']),
                             ('敷地権の表示', ys_of(671, 1144, 483, 626), ['table.shiki td.head {{ height: 123px; }}', 'table.shiki td.entry {{ height: 195px; }}'])]:
    hs = [b_ - a_ for a_, b_ in zip(ys_, ys_[1:])]
    pxs = [int(re.search(r'height: (\d+)px', k_).group(1)) for k_ in css_keys]
    # 原本の行の高さ(pt)×倍率が、CSSの高さと3px以内（最後のデータ行・見出し行・所在行・名称行）
    cand = [round(h_ * SC) for h_ in hs]
    ok = all(any(abs(c_ - p_) <= 3 for c_ in cand) for p_ in pxs) and all(k_[:k_.index('{{')] in mk or k_.split(' {{')[0] in mk for k_ in css_keys)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'行の高さ（{label}）：原本の行の高さ×{SC:.3f} ＝ {cand}px（HTML {pxs}）')
# 申請書の記入欄の min-height（答案用紙の枠の高さ 57・79・57・44pt × 2.23）
for cls_, pt_, px_ in [('h-mokuteki', 56.7, 126), ('h-tenpu', 79.4, 177), ('h-shinsei', 56.7, 126), ('h-menkyo', 43.5, 97)]:
    ok = abs(pt_ * 2.23 - px_) <= 3 and f'.box.{cls_} {{{{ min-height: {px_}px; }}}}' in mk
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'申請書の記入欄の min-height（{cls_}）：{pt_}pt × 2.23 ＝ {pt_ * 2.23:.0f}px')
# 第1欄・第4欄の列と行（原本）
ok = 'DAI1_COLS, DAI1_ROWH = (11.9, 38.0, 12.1, 38.0), 91' in mk and 'DAI4_COLS, DAI4_ROWH = (10.8, 39.5, 10.6, 39.1), 102' in mk
ng += (not ok)
print(('OK ' if ok else 'NG ') + '第1欄・第4欄の列の幅と行の高さ（原本の画像から測った値）')
# 記事中の「a×b＝c」の再計算（求積表・本文）
n_calc = 0
for m_ in re.finditer(r'(\d+\.\d+)\s*[×かけ]\s*(\d+\.\d+)\s*＝\s*(\d+\.\d+)', text):
    a_, b_, c_ = Decimal(m_.group(1)), Decimal(m_.group(2)), Decimal(m_.group(3))
    got_ = a_ * b_
    ok = got_ == c_ or got_.quantize(Decimal('0.01')) == c_.quantize(Decimal('0.01'))
    n_calc += 1
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[記事の計算式] {a_}×{b_}＝{c_}')
for m_ in re.finditer(r'(\d+\.\d+)かける(\d+\.\d+)が(\d+\.\d+)', text):
    a_, b_, c_ = Decimal(m_.group(1)), Decimal(m_.group(2)), Decimal(m_.group(3))
    ok = a_ * b_ == c_
    n_calc += 1
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[記事の計算式] {a_}かける{b_}が{c_}')
ok = n_calc >= 6
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[記事の計算式] 計算し直した式の数 : {n_calc}')
for expr, want_ in [(Decimal('4.61') + Decimal('74.72'), Decimal('79.33')),
                    (Decimal('3.64') + Decimal('3.66'), Decimal('7.30')), (Decimal('2.73') + Decimal('1.87') + Decimal('2.70'), Decimal('7.30')),
                    (Decimal('2.80') + Decimal('4.50') + Decimal('4.50'), Decimal('11.80')), (Decimal('3.71') + Decimal('3.59') + Decimal('5.40'), Decimal('12.70')),
                    (Decimal('12.70') - Decimal('11.80'), Decimal('0.90')), (Decimal('2.73') + Decimal('2.30') + Decimal('1.37') + Decimal('0.90'), Decimal('7.30')),
                    (Decimal('0.15') / 2, Decimal('0.075'))]:
    ok = expr == want_
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[新しい図・会話の数値] {expr}＝{want_}')
check('4.61＋74.72の説明', '4.61足す74.72は79.33')
check('図の足し算', '西側は2.80足す4.50足す4.50で11.80メートル')
# 話者の連続（マーカーをはさんでも同じ話者が続かない。章をまたぐ場合も）
spk = [l_.strip() for l_ in lines if l_.strip() in ('**トリ先生**', '**藍子**')]
ok = all(a_ != b_ for a_, b_ in zip(spk, spk[1:]))
ng += (not ok)
print(('OK ' if ok else 'NG ') + '話者が交互に並ぶ（マーカー・章をはさんで同じ話者が連続しない）')
print('NG件数（6-2・6-3追加分を含む）:', ng)
