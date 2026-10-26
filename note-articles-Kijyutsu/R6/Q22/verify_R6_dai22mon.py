"""令和6年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 解答例、第1〜4欄・建物図面・各階平面図・求積表）と一致することを確認済み。
実行: /usr/bin/python3 note-articles-Kijyutsu/R6/Q22/verify_R6_dai22mon.py（pymupdf・Pillow・Playwright の入った Python 3.13）"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, area

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_R6_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_R6_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_R6_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_R6_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_R6_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


def poly_area(pts):
    n = len(pts)
    return abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2


def trunc2(v):
    """床面積の端数処理：1平方メートルの100分の1未満を切り捨て（不動産登記規則115条）。"""
    return math.floor(v * 100 + 1e-9) / 100


# ---- 敷地：〔座標値一覧表〕A〜E（X＝北、Y＝東）。図1は傾いて見えるが座標では長方形 ----
A, B, C, D, E = P(50.00, 15.00), P(50.00, 25.00), P(50.00, 35.00), P(37.00, 35.00), P(37.00, 15.00)
assert A.real == B.real == C.real == 50.00 and D.real == E.real == 37.00
assert A.imag == E.imag == 15.00 and C.imag == D.imag == 35.00
assert abs(B - A) == 10 and abs(C - B) == 10 and abs(D - C) == 13 and abs(E - D) == 20 and abs(A - E) == 13
assert round(area([A, B, C, D, E]), 2) == 260.00  # 登記記録の地積 260.00㎡ と一致
check('A・B・Cが一直線', 'A、B、CのX座標は3つとも50.00、DとEは37.00')
check('CDの表示', '[Abs] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]` で、表示は13')
check('DE', '南側の辺DEは同じように20')
check('AB・BC・EA', '北側はABもBCも10、西側のEAは13')
check('地積との一致', '20かける13で260。登記記録の地積260.00平方メートルとぴったり一致')
assert round(20.0 * 100 / 500, 1) == 4.0
check('縮尺換算', '20メートルなら図面上は4センチ')
check('北側の境の切り替わり', 'AからBまでは隣地の16番11との境、BからCまでは道路（100番9）との境')

# ---- 建物図面：筆界からの距離は小数第1位（問題文の注4）。解答例の建物図面は 1.5・1.5・1.0 ----
check('建物図面の距離', '『1.5』『1.5』『1.0』')
# 建物の位置：和室の北の外壁が辺ABから1.5、ウォークインクローゼットの西の外壁が辺EAから1.0
bx0, bx_n = E.imag + 1.0, A.real - 1.5  # 建物座標の原点（西の壁のY、和室の北の壁のX）
assert (bx0, bx_n) == (16.0, 48.5)

# ---- 1階：母屋のみ（車庫＝周壁なし、出窓＝下端0.90・高さ1.10、ポーチは外）----
F1 = [(0.9, 0), (4.5, 0), (4.5, 0.9), (11.25, 0.9), (11.25, 2.7), (10.8, 2.7), (10.8, 8.1),
      (6.3, 8.1), (6.3, 6.75), (4.5, 6.75), (4.5, 6.3), (0, 6.3), (0, 3.6), (0.9, 3.6)]
s1 = [(0.90, 2.70), (3.60, 6.30), (1.80, 5.85), (4.50, 7.20), (0.45, 1.80)]
a1 = sum(w * h for w, h in s1)
assert round(a1, 4) == 68.85 == round(poly_area(F1), 2)
# 寸法線からの拾い方
assert round(0.90 + 1.80 + 0.90 + 2.70, 2) == 6.30
assert round(1.80 + 0.90 + 2.70 + 0.45, 2) == 5.85
assert round(1.35 + 3.15, 2) == 4.50
assert round(8.1 - 0.9, 2) == 7.20
for w, h in s1:
    check(f'1階 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('1階 合計', '合計：68.8500 （床面積：68.85平方メートル）')
check('和室・洋室の列の縦', '縦6.30メートル（0.90足す1.80足す0.90足す2.70）')
check('ホール・玄関の列の縦', '1.80足す0.90足す2.70足す0.45）')
check('キッチン・LDの列の横', '横4.50メートル（1.35足す3.15）')
check('出窓の高さ', '床から0.90メートル上から始まって、高さは1.10メートル')
check('出窓の算入要件', '高さが1.5メートル以上で、しかも下の端が床面と同じ高さにあるものだけ')
check('車庫の寸法（藍子の誤答）', '車庫3.15かける4.50')
# 藍子の誤り：車庫を足すと 83.025（記事では数値を出さず、比較図で示す）
assert round(a1 + 3.15 * 4.50, 3) == 83.025

# ---- 2階：母屋＋（あ）部分の洋室（屋外廊下・バルコニーは外気と分断されていない）----
F2 = [(0.9, 0), (4.5, 0), (4.5, 0.9), (7.65, 0.9), (7.65, 2.7), (10.8, 2.7), (10.8, 8.1),
      (7.2, 8.1), (7.2, 6.3), (0.9, 6.3)]
AA = [(12.6, -0.9), (15.75, -0.9), (15.75, 3.6), (12.6, 3.6)]
s2 = [(3.60, 6.30), (2.70, 5.40), (0.45, 7.20), (3.15, 5.40), (3.15, 4.50)]
a2 = sum(w * h for w, h in s2)
assert round(a2, 4) == 71.685 == round(poly_area(F2) + poly_area(AA), 3)
assert round(poly_area(F2), 2) == 57.51
assert trunc2(a2) == 71.68 and round(a2 + 1e-9, 2) == 71.69  # 四捨五入なら71.69になる＝わな
for w, h in s2:
    check(f'2階 {w:.2f}×{h:.2f}', f'{w:.2f} × {h:.2f} ＝ {w * h:.4f}')
check('2階 合計', '合計：71.6850')
check('2階 床面積（切り捨て）', '71.685の5は切り捨てて、71.68平方メートルよ')
# 0.45の列：上の寸法線（トイレの東の壁）と下の寸法線（東の洋室の西の壁）の差
top = 3.60 + 1.80 + 1.35
bottom = 2.70 + 1.80 + 0.90 + 0.90
assert round(top, 2) == 6.75 and round(bottom, 2) == 6.30 and round(top - bottom, 2) == 0.45
check('上の寸法線', '3.60足す1.80足す1.35で、6.75')
check('下の寸法線', '2.70足す1.80足す0.90足す0.90で、6.30')
check('0.45のずれ', '6.75と6.30で、0.45ずれてます')
# 藍子の誤り：東の洋室の西の壁（下の寸法線）でそろえ、トイレの東の端 0.45×1.80 を落とす
wrong = 3.60 * 6.30 + 2.70 * 5.40 + 3.60 * 5.40 + 3.15 * 4.50
assert round(wrong, 4) == 70.875 and round(a2 - wrong, 2) == round(0.45 * 1.80, 2) == 0.81
check('藍子の2階（誤答）', '東の洋室の列が3.60かける5.40')
check('藍子の2階 合計（誤答）', '合計70.8750です')
check('落とした部分', '横0.45メートル×縦1.80メートルの部分が抜け落ちるんですね。0.81平方メートルの損です')
check('（あ）の縦', '縦4.50メートル（0.90足す2.70足す0.90）')
assert round(0.90 + 2.70 + 0.90, 2) == 4.50

# ---- 問1（第1欄）・問4（第4欄）----
check('第1欄', 'ア＝確認、イ＝検査、ウ＝建築請負人、エ＝固定資産税')
check('第4欄', 'だから①構造上、②利用上')
check('問1 エの対比', '登録免許税は、登記を受けるときに納める税金よ')
check('問4 の対比', '構造上と利用上を入れ替えて覚えてるわね')

# ---- 問2（第2欄）----
check('登記の目的', '建物表題登記です')
check('添付書類', '表題登記の決まりで5つ。建物図面、各階平面図、所有権を証する情報、表題部所有者になる人の住所を証する情報、そして代理で申請するための代理権限を証する情報')
check('登記識別情報は不要', '登記識別情報は、所有権の登記をしたときに登記名義人に通知されるもの')
check('所在', '『A市B町三丁目16番地13』')
check('種類', '種類は『居宅』')
check('構造', '『木造合金メッキ鋼板ぶき2階建』')
check('床面積', '床面積は1階68.85平方メートル、2階71.68平方メートル')
check('原因及びその日付', '『令和6年9月30日新築』')
check('共有者', '『共有者　A市B町三丁目16番地13　持分5分の3　甲野松雄』『A市B町三丁目16番地13　5分の2　甲野桜子』')
check('申請人と共有者の区別', '申請人は、実際に申請の手続をする人。表題部所有者は、登記記録に建物の持ち主として載る人')

# ---- 付属プロンプトとの整合 ----
check('添付書類', '建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書', form, '申請書')
check('床面積', '「1階　68｜85」「2階　71｜68」', form, '申請書')
check('原因', '「令和６年９月30日新築」', form, '申請書')
check('共有者1', '持分　５分の３　　甲野松雄', form, '申請書')
check('共有者2', '５分の２　　甲野桜子', form, '申請書')
check('正解1', '持分　５分の３　　甲野松雄', fix, '添削')
check('正解2', '５分の２　　甲野桜子', fix, '添削')
absent('登録免許税の記入', '登録免許税**：', form, '申請書')


# ---- 申請の期限（2026-10-26追加。不動産登記法第47条第1項・民法第140条・第143条第2項）----
import datetime
done = datetime.date(2024, 9, 30)                       # 新築（所有権取得）の日
start = done + datetime.timedelta(days=1)               # 初日不算入で10月1日から数える
ouVal = datetime.date(start.year, start.month + 1, start.day)   # 応当日 11月1日
deadline = ouVal - datetime.timedelta(days=1)           # 応当日の前日で満了
assert deadline == datetime.date(2024, 10, 31) and datetime.date(2024, 10, 18) <= deadline
check('申請の期限10月31日', 'この1月の期限は、いつまで？')
check('期限の計算', '最後の月で、数え始めた日の応当日の前日に満了する')
check('10月31日', '10月31日が期限よ')
check('日付の整理', '令和6年9月30日に完成して、同じ日に引渡しも受けています')

# 解説図プロンプトの頂点座標（Y＝東、X＝南、上が北）が求積表と一致すること
BAL = [(0.9, 6.3), (7.2, 6.3), (7.2, 8.1), (10.8, 8.1), (10.8, 9), (6.3, 9), (6.3, 7.2), (0.9, 7.2)]
for label, pts, want in [('図14 1階', F1, 68.85), ('図16 2階（母屋）', F2, 57.51), ('図16 バルコニー', BAL, None), ('図11 建物図面の1階', F1, 68.85)]:
    if want is not None:
        assert round(poly_area(pts), 2) == want, label
    s = ' → '.join(f'({y:g}, {x:g})' for y, x in pts + [pts[0]])
    check(label + ' 頂点座標', s, fig, '解説図')
for s in ['辺AB：「10.0m」', '辺BC：「10.0m」', '辺CD：「13.0m」', '辺DE：「20.0m」', '辺EA：「13.0m」',
          '「1.5」を2か所', '1階 床面積：68.85㎡', '2階 床面積：71.68㎡（合計71.685を切り捨て）',
          'Y：7.2〜7.65、X：0.9〜2.7。横0.45m×縦1.80m、面積0.81', 'Y：12.6〜15.75、X：−0.9〜3.6（横3.15m×縦4.50m、面積14.175）']:
    check('図の数値', s, fig, '解説図')

# ---- 形状・向き（図面の上＝北）----
check('（あ）部分の位置', '屋外廊下で隔てられた東側の（あ）部分')
check('浴室の出っ張り', '浴室の東の出っ張り：横0.45メートル × 縦1.80メートル')
for bad in ['PDF', '創設的登記', '『1.50』『1.50』', '列を丸ごと', 'トイレの北東にある', '北側の線も東側の線も', 'ポーチ', '会社の印鑑証明書', '玄関まわり']:
    absent('誤記・混入', bad)

# ---- タイトルの基本形 ----
title = text.splitlines()[0]
prefix = '# 【土地家屋調査士受験生向け】令和6年度問題22（建物）〜'
sub = title[len(prefix):-1]
ok = title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'タイトル形式（見出し{len(sub)}文字） : ' + title)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和6年度問題22（建物）', thumb, '見出し画像')

# ---- note向けの体裁 ----
import re
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
# 注の列挙（仕分けの会話の「注は5つです」「図面の注は6つ」の段落と、画像挿入マーカーの行）は除く
skip = [(m.start(), m.end()) for m in re.finditer(r'^(?:「問題文の末尾の注は5つ|> 【画像挿入】注の仕分け図).*$', text, re.M)]
bare = [m.start() for m in re.finditer(r'注[0-9]', text) if not text[:m.start()].endswith(('問題文の', '図面の'))
        and not any(a_ <= m.start() < b_ for a_, b_ in skip)]
# 「注1〜5」「注1〜6」のような範囲の言い方は除く（図面の注の注番号の列挙は仕分けの会話で区別している）
bare = [b for b in bare if not text[b - 1:b] == '注']
ok = not bare
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'注の書き分け（「問題文の注N」「図面の注N」） : 書き分けていない箇所 {len(bare)}')
for bad in ['✕', '✓', '名変']:
    absent('記号・略語', bad)
check('解く順番', '問1は、別紙を読まなくても準則の知識だけで埋められるから、問題を開いたら真っ先に片付けなさい')
check('寸法線の累計メモ', '足した累計を図の上下と左右にメモしておけば')

# ---- 画像：記事の画像挿入マーカー31か所と zu/ のPNGの対応（記事の挿入順）----
from PIL import Image
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('R6_dai22mon_zu01_jikeiretsu', '完成日・申請日・申請の期限を、日付で並べた図', (1700, 760)),
        ('R6_dai22mon_zu02_chuu_shiwake', '注の仕分け図', None),
        ('R6_dai22mon_zu03_mochinushi', '土地の持ち主と建物の持ち主の整理図', None),
        ('R6_dai22mon_zu04_shinseinin', '申請人と登記記録に載る所有者の対比図', None),
        ('R6_dai22mon_zu05_a_bubun_keiro', '（あ）部分の2階へ入るための唯一の経路', (1600, 1000)),
        ('R6_dai22mon_zu06_kubun_hantei', '判定の流れ図', None),
        ('R6_dai22mon_dai4ran_kansei', '第4欄（問4）の完成形', 'wide'),
        ('R6_dai22mon_zu07_shikichi_henchou', '作図チェック用の辺長', (1600, 1050)),
        ('R6_dai22mon_zu08_b_ten', '北側の辺をA・B・Cの順に並べ', None),
        ('R6_dai22mon_zu09_kakikata', '建物図面に「書くもの」と「書かないもの」', None),
        ('R6_dai22mon_zu10_keta_shukushaku', '距離の桁数と縮尺の比較図', None),
        ('R6_dai22mon_zu11_tatemono_zumen', '建物図面の完成形（答案用紙の第3欄の建物図面の枠の中', (1075, 1797)),
        ('R6_dai22mon_zu12_shako', '左に「誤り＝母屋に（あ）部分の車庫', None),
        ('R6_dai22mon_zu13_demado', '出窓の断面と算入の条件', None),
        ('R6_dai22mon_zu14_1kai_kyuuseki', '1階の床面積求積図', (1600, 1100)),
        ('R6_dai22mon_zu15_sunpousen', '2階の上の寸法線', None),
        ('R6_dai22mon_zu16_2kai_kyuuseki', '2階の床面積求積図', (1700, 1100)),
        ('R6_dai22mon_zu17_hasuu', '2階の合計71.6850の端数処理の比較図', None),
        ('R6_dai22mon_zu18_marujirushi', '〇印をそろえて2階の図に1階の位置を重ねる図', None),
        ('R6_dai22mon_zu19_kakukai_heimenzu', '各階平面図の完成形（答案用紙の第3欄の各階平面図の枠の中', (1075, 1797)),
        ('R6_dai22mon_zu20_tenpu_shorui', '表題登記の添付書類の図', None),
        ('R6_dai22mon_zu21_zeikin_chigai', '問1のエの対比図', None),
        ('R6_dai22mon_dai1ran_kansei', '第1欄（問1）の完成形', 'wide'),
        ('R6_dai22mon_zu22_inshi_ran', '答案用紙の欄の仕分け図', None),
        ('R6_dai22mon_toukishinseisho_machigai_shozai', '「所在」欄の①誤答', 'tall'),
        ('R6_dai22mon_toukishinseisho_machigai_kouzou', '「構造」欄の①誤答', 'tall'),
        ('R6_dai22mon_toukishinseisho_machigai_genin', '「登記原因及びその日付」欄の①誤答', 'tall'),
        ('R6_dai22mon_toukishinseisho_machigai', '「共有者」欄の①誤答', 'tall'),
        ('R6_dai22mon_zu23_touroku_menkyozei', '登録免許税の整理図', None),
        ('R6_dai22mon_toukishinseisho_kansei', '登記申請書（問2）の完成形', 'tall'),
        ('R6_dai22mon_zu24_toku_junban', '本番で解く順番の整理図', (1600, 800))]
ok = len(markers) == len(PNGS) == 31
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーの数 : {len(markers)}／PNG {len(PNGS)}枚（解説図24・第1欄・第4欄・添削4・申請書の完成形）')
for (name, key, size), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        if size == 'tall':
            ok = w == 1200 and h > w
        elif size == 'wide':
            ok = w == 1200 and h < w
        elif size:
            ok = (w, h) == size
        else:
            ok = w >= 1000 and h >= 500
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'PNG（マーカー順・大きさ） : {name}')
    if 'zu' in name.split('_')[2]:
        check('プロンプトにファイル名', f'zu/{name}.png', fig, '解説図プロンプト')
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
ok = not extra
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'zu/ に記事で使わないPNGがない : {extra}')

# ---- 穴埋め・解答欄の語 ----
check('問1 ア〜エの語', 'ア＝確認、イ＝検査、ウ＝建築請負人、エ＝固定資産税ですね')
check('問1 アとイは順不同', 'アとイは問題文で順不同とされているから')
check('問4 ①②の語', '第4欄には、①構造上、②利用上と書きます')
check('保存行為の条文', '保存行為（民法第252条第5項）')
check('第3欄の上の欄（各階平面図）', '家屋番号も（略）と印刷済みです')
check('解く順番（計算のいる欄）', '申請書で計算がいるのは、1階68.85と2階71.68の2か所だけ')
check('解く順番（いちばん時間を食う）', '寸法線を足して2階の床面積を出すところと、第3欄の作図よ')
check('出窓の条文', '準則第82条第11号')
for n in ['## 図11：建物図面の完成形', '## 図19：各階平面図の完成形', '## 図24：本番で解く順番の整理図', '（令和6年○月○日作成）', '6.75−6.30＝0.45',
          'touan_youshi/R6_dai22mon_touan_youshi.pdf']:
    check('解説図プロンプト（第3欄の枠・完成形・本番で解く順番）', n, fig, '解説図')
ok = len(re.findall(r'^## 図\d+：', fig, re.M)) == 24
ng += (not ok)
print(('OK ' if ok else 'NG ') + '解説図プロンプトは24枚')


def html_has(name, *needles, bad=()):
    global ng
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        ok = n in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : {n}')
    for n in bad:
        ok = n not in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html に無い : {n}')


html_has('R6_dai22mon_toukishinseisho_kansei', '建物表題登記', '建物図面　各階平面図　所有権証明書　住所証明書', '代理権限証書',
         '令和６年10月18日　申請　Ａ地方法務局', 'Ａ市Ｂ町三丁目16番地13　　甲　野　桜　子', 'Ａ市Ｂ町三丁目16番地13',
         '居宅', '木造合金メッキ', '鋼板ぶき２階建', '1階68', '>85<', '2階71', '>68<', '令和６年９月30日新築',
         '持分', '５分の３', '甲野松雄', '５分の２', '甲野桜子', '（略）',
         bad=('登録免許税', '登記識別情報', '印鑑証明書', '71.69'))
html_has('R6_dai22mon_dai1ran_kansei', '第1欄', '>確認<', '>検査<', '>建築請負人<', '>固定資産税<', bad=('登録免許税',))
html_has('R6_dai22mon_dai4ran_kansei', '第4欄', '>構造上<', '>利用上<')
html_has('R6_dai22mon_toukishinseisho_machigai', '所有者', '共有者', '甲野松雄', '５分の３', '５分の２', '申請人（手続をする人）')
html_has('R6_dai22mon_toukishinseisho_machigai_shozai', 'Ａ市Ｂ町三丁目16番13', 'Ａ市Ｂ町三丁目16番地13', '「番」のあとに「地」を入れて')
html_has('R6_dai22mon_toukishinseisho_machigai_kouzou', '木造２階建', '木造合金メッキ', '主な材料・屋根の種類・階数')
html_has('R6_dai22mon_toukishinseisho_machigai_genin', '令和６年10月18日新築', '令和６年９月30日新築', '新築した日')
check('添削：縦に積む', '3コマを縦に積む', fix, '添削')
absent('横1800px', '1800px', fix, '添削')
absent('記号', '✓', fix, '添削')
for n in ['machigai_shozai.png', 'machigai_kouzou.png', 'machigai_genin.png', 'R6_dai22mon_toukishinseisho_machigai.png']:
    check('添削プロンプトにファイル名', n, fix, '添削')
drw = open(os.path.join(ZU, 'draw_R6_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
fits = re.findall(r'\bfit\(ax[^\n]*', drw) + re.findall(r'\bfit\(axes\[[01]\][^\n]*', drw)
ok = fits and all('pad_aspect=True' in f for f in fits)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'作図の fit はすべて pad_aspect=True（{len(fits)}か所）')
for s in ['== 68.85', '== 57.51', '== 14.175', '== 71.685', '== 260', "'Ａ市Ｂ町三丁目16番地13'", '（令和6年○月○日作成）']:
    check('作図スクリプトの確認', s, drw, '作図')

# ---- 6-2：まとめのわな25項目（1項目1わな）と、わな→図の対応表（TRAPS）----
TRAPS = [
    ('期限は10月31日', 'この1月の期限は、いつまで？', 'R6_dai22mon_zu01_jikeiretsu', '期限内'),
    ('問題文の注2と図面の注2は別物', 'どちらにも2番の注があるわ', 'R6_dai22mon_zu02_chuu_shiwake', '図面の注2』と書き分ける'),
    ('土地の持ち主と建物の持ち主は別', '土地の持ち主は誰？', 'R6_dai22mon_zu03_mochinushi', 'ここは混ぜないこと'),
    ('申請人は1人でも', '桜子さん1人で申請していいんですか？', 'R6_dai22mon_zu04_shinseinin', '覚えておきなさい'),
    ('構造上の独立性はあるが利用上の独立性がない', '答えは①利用上、②構造上です！', 'R6_dai22mon_zu05_a_bubun_keiro', '使うことはできないでしょう'),
    ('構造上と利用上の両方がそろったときだけ', '判定の流れを図にするとこうなるわ', 'R6_dai22mon_zu06_kubun_hantei', '準則第78条第2項'),
    ('20×13＝260', 'どんな形に見える？', 'R6_dai22mon_zu07_shikichi_henchou', 'あくまで作図のチェック用'),
    ('B点は飾りではなく', 'B点って要らないんじゃないですか？', 'R6_dai22mon_zu08_b_ten', '境目を示すのよ'),
    ('建物図面に書くもの', '書くのは何で、書かないのは何？', 'R6_dai22mon_zu09_kakikata', '建物図面には描かないわ'),
    ('距離の桁数と縮尺', '『1.50』ではだめですか？', 'R6_dai22mon_zu10_keta_shukushaku', '取り違えないこと'),
    ('車庫は周壁がなく', '第1章で何を聞いてたの！？', 'R6_dai22mon_zu12_shako', '壁がないでしょう'),
    ('出窓は「高さ1.5メートル以上」', '出窓は壁から外に出ているけど', 'R6_dai22mon_zu13_demado', '算入しないの'),
    ('1階は長方形に分割して足す', '長方形に分割して足す', 'R6_dai22mon_zu14_1kai_kyuuseki', '横0.45メートル × 縦1.80メートル'),
    ('2階は上と下の寸法線', '上の寸法線でトイレの東の壁の位置を出しなさい', 'R6_dai22mon_zu15_sunpousen', '初めて出てくる数字よ'),
    ('71.6850は四捨五入せず', '四捨五入して71.69平方メートルです', 'R6_dai22mon_zu17_hasuu', '切り捨てて、71.68平方メートルよ'),
    ('〇印をそろえる', '1階と2階を重ねるとき、何を目印にそろえる？', 'R6_dai22mon_zu18_marujirushi', '4本の柱の真上ね'),
    ('添付書類は5点', '登記識別情報も付けますか？', 'R6_dai22mon_zu20_tenpu_shorui', '入っていないでしょう'),
    ('問1のエは固定資産税', '『登録免許税』です！', 'R6_dai22mon_zu21_zeikin_chigai', '示す資料になるのよ'),
    ('書く欄・印刷済みで書かない欄・空けておく欄', '空けておく欄を、先に仕分けておきなさい', 'R6_dai22mon_zu22_inshi_ran', '附属建物がないからですね'),
    ('番地で書く（16番地13）', 'A市B町三丁目16番13』ですよね', 'R6_dai22mon_toukishinseisho_machigai_shozai', '同じ書き方でしょう'),
    ('「主な材料・屋根の種類・階数」の順', '『木造2階建』。床面積は', 'R6_dai22mon_toukishinseisho_machigai_kouzou', '順なんですね'),
    ('申請の日ではなく新築の日', '『令和6年10月18日新築』です！', 'R6_dai22mon_toukishinseisho_machigai_genin', '原因の日付ではありません'),
    ('共有者欄は全員を持分つき', '『所有者　A市B町三丁目16番地13　甲野桜子』と書きます！', 'R6_dai22mon_toukishinseisho_machigai', 'お金を多く出したのは松雄さん'),
    ('登録免許税がかからず', '登録免許税の欄は、この答案用紙にはそもそもないわね', 'R6_dai22mon_zu23_touroku_menkyozei', '同じ理由です'),
    ('計算のいらない問と欄を先に', '最後に、本番での解く順番よ', 'R6_dai22mon_zu24_toku_junban', '同じ原点でそろえます'),
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

# ---- 6-3：図の画像の決まり ----
mk = open(os.path.join(ZU, 'make_R6_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read()
htmls = {f_[:-5]: open(os.path.join(ZU, f_), encoding='utf-8').read() for f_ in os.listdir(ZU) if f_.endswith('.html')}
ok = 'style="height:' not in mk and not any('style="height:' in h_ for h_ in htmls.values())
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書・添削のHTMLに style="height: がない（min-height）')
ok = all('第1欄' not in h_ and '第2欄' not in h_ for n_, h_ in htmls.items() if 'dai4ran' not in n_ and 'dai1ran' not in n_)
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書・添削のHTMLに「第○欄」の見出しがない（第1欄・第4欄の画像だけ印刷どおり入れる）')
bad_titles = re.findall(r"(?:fixed_figure|new_figure|suptitle|set_title)\(\s*'[^']*図\d", drw)
ok = not bad_titles
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[作図スクリプト] タイトルに図番がない : {bad_titles}')

# 答案用紙の原本PDF（ベクター）から列の幅・文字を測り直す
import pymupdf
TY = os.path.join(HERE, 'touan_youshi', 'R6_dai22mon_touan_youshi.pdf')
doc = pymupdf.open(TY)
pg1 = doc[0]
vx = sorted({round(d['rect'].x0, 1) for d in pg1.get_drawings() if d['rect'].width < 1.5 and 178 < d['rect'].x0 < 640 and d['rect'].height > 20 and d['rect'].y0 > 540})
xs = [177.0] + vx + [649.0]
pct = [100 * (b_ - a_) / (xs[-1] - xs[0]) for a_, b_ in zip(xs, xs[1:])]
got = [float(v_) for v_ in re.search(r'COLS_PCT = \(([^)]*)\)', mk).group(1).split(',')]
ok = len(pct) == len(got) == 7 and all(abs(u_ - v_) < 0.3 for u_, v_ in zip(pct, got))
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'表の列の幅の比：答案用紙の原本PDFから測ると {[round(v_, 1) for v_ in pct]}（HTMLの COLS_PCT {got}）')
def _n(x_):
    return x_.replace('\n', '').replace(' ', '').replace('\u3000', '')


t1 = pg1.get_text()
t2 = doc[1].get_text()
for s_ in ['令和6 年10 月18 日', 'Ａ地方法務局', 'Ａ市Ｂ町三丁目16 番地13', '甲　野　桜　子', '家屋番号', '共有者', '主である']:
    ok = _n(s_) in _n(t1)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'答案用紙の原本（第1〜2・4欄）に印刷されている : {s_}')
ok = all(_n(s_) in _n(t2) for s_ in ['各　階　平　面　図', '建　物　図　面', '（略）', '縮尺', '（令和6 年○月○日作成）'])
ng += (not ok)
print(('OK ' if ok else 'NG ') + '答案用紙の原本（第3欄）に各階平面図・建物図面・（略）・縮尺・作成日の印刷')
# 家屋番号の「（略）」は申請書の原本に印刷されている（アガルートの再現にはない）
ok = '（略）' in t1 and '（略）' in html_text if (html_text := htmls['R6_dai22mon_toukishinseisho_kansei']) else False
ng += (not ok)
print(('OK ' if ok else 'NG ') + '申請書のHTMLにも家屋番号の「（略）」を印刷として入れている')

# 面積・寸法の数字を計算し直す（記事の「a × b ＝ c」）
for a_, b_, c_ in re.findall(r'(\d+\.\d+) × (\d+\.\d+) ＝ (\d+\.\d+)', text):
    ok = abs(float(a_) * float(b_) - float(c_)) < 1e-9
    ng += (not ok)
    if not ok:
        print('NG 求積の式 :', a_, b_, c_)
print('OK 記事の求積の式（a × b ＝ c）をすべて再計算した')

print('NG件数:', ng)
