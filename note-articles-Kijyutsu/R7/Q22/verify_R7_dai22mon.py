"""令和7年度 第22問（建物）：記事の数値・計算の照合スクリプト。
アガルートの解答例（第22問 答案用紙・解答例）と一致することを確認済み。
実行: python3 note-articles-Kijyutsu/R7/Q22/verify_R7_dai22mon.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))

ART = os.path.join(os.path.dirname(__file__), 'note_R7_dai22mon_tatemono_kaisetsu.md')
text = open(ART, encoding='utf-8').read()
ng = 0


def check(label, s):
    global ng
    ok = s in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label + ' : ' + s)


# 符号2（1階）：138.50 - 5.00×3.00（撤去された張り出し部分15.00） = 123.50（2階と一致）
old_1f = 19.00 * 6.50 + 5.00 * 3.00
assert round(old_1f, 2) == 138.50
notch = 5.00 * 3.00
assert round(notch, 2) == 15.00
new_1f = old_1f - notch
assert round(new_1f, 2) == 123.50 == 19.00 * 6.50
check('符号2 1階（工事前）', '合計138.50平方メートルです')
check('符号2 2階（工事前）', '123.50平方メートルでした')
check('符号2 1階（工事後）', '123.50平方メートル！ あれ、2階と同じ数字になりました')

# 問1：主である建物（旧）
check('主(旧) 床面積', '1階130.00平方メートル、2階130.00平方メートル')

# 問1：主である建物（新＝旧符号2が昇格）
check('主(新) 床面積', '1階123.50平方メートル、2階123.50平方メートル')

# 問1：符号2（消滅時の記載）
check('符号2 床面積(消滅時)', '1階138.50平方メートル、2階123.50平方メートル')

def poly_area(pts):
    n = len(pts)
    return abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2


# 解説図プロンプトの頂点座標（Y=東, X=南）が求積表と一致すること
assert round(poly_area([(0, 0), (19, 0), (19, 6.5), (5, 6.5), (5, 9.5), (0, 9.5)]), 2) == 138.50
assert round(poly_area([(0, 0), (25.5, 0), (25.5, 9), (15.5, 9), (15.5, 6.5), (0, 6.5)]), 2) == 190.75
assert round(poly_area([(0, 0), (25.5, 0), (25.5, 9), (23.5, 9), (23.5, 6.5), (7, 6.5), (7, 4.5), (0, 4.5)]), 2) == 156.75

# 新築倉庫（符号5）1階：壁心＝柱芯寸法の両端に0.30ずつ足す
assert round(7.20 + 5.50 + 2.30 + 4.90 + 0.30 + 4.70, 2) == 24.90
assert round(24.90 + 0.60, 2) == 25.50 == 15.50 + 10.00
assert round(0.30 + 1.50 + 4.40 + 0.30, 2) == 6.50
check('柱芯→壁心', '24.90＋0.60＝25.50m')
check('西側の縦', '0.30＋1.50＋4.40＋0.30＝6.50m')

# 新築倉庫（符号5）1階：10.00×9.00 + 15.50×6.50 = 190.75
a1, a2 = 10.00 * 9.00, 15.50 * 6.50
assert round(a1 + a2, 2) == 190.75
check('符号5 1階 求積', '10.00×9.00＝90.0000、15.50×6.50＝100.7500、合計190.7500')
check('符号5 1階 床面積', '1階の床面積は190.75平方メートル')

# 新築倉庫（符号5）2階：2.00×9.00 + 16.50×6.50 + 7.00×4.50 = 156.75
b1, b2, b3 = 2.00 * 9.00, 16.50 * 6.50, 7.00 * 4.50
assert round(b1 + b2 + b3, 2) == 156.75
check('符号5 2階 求積', '2.00×9.00＝18.0000、16.50×6.50＝107.2500、7.00×4.50＝31.5000、合計156.7500')
check('符号5 2階 床面積', '2階の床面積は156.75平方メートル')

# 1階と2階の差＝南西の吹き抜け(0.30+6.70)×(1.70+0.30) + 南東の吹き抜け＋階段(0.30+2.00+5.70)×(2.20+0.30)
sw = (0.30 + 6.70) * (1.70 + 0.30)
se = (0.30 + 2.00 + 5.70) * (2.20 + 0.30)
assert round(sw, 2) == 14.00 and round(se, 2) == 20.00
assert round((a1 + a2) - (b1 + b2 + b3), 2) == round(sw + se, 2) == 34.00
check('南西の吹き抜け', '横が0.30＋6.70＝7.00m、縦が1.70＋0.30＝2.00m')
check('南東の吹き抜け＋階段', '横8.00m、縦2.50m')
check('検算', '190.75−34.00＝156.75')

# 符号6（守衛所再築）：元と同じ4.00×2.50=10.00
assert round(4.00 * 2.50, 2) == 10.00
check('符号6 床面積', '4.00m×2.50mの単純な長方形、床面積10.00平方メートル')

# 問2：符号5・符号6の登記原因の日付（工事完了順で符号を付ける）
check('符号5 新築日', '令和7年10月7日')
check('符号6 新築日', '令和7年10月17日')
check('符号4 取壊し日', '令和7年9月25日')

# 問4（第4欄）：ア物理 イ報告 ウ1月 エ10万円以下の過料
check('第4欄 ア', 'ア＝物理')
check('第4欄 イ', 'イ＝報告')
check('第4欄 ウ', 'ウ＝1月')
check('第4欄 エ', 'エ＝10万円以下の過料')

# 穴埋めの答えの語を会話でそのまま言っているか（2026-10-02、R5/Q22で見つかった確認。上の4つ）と、根拠の条文（原典で確認）
check('第4欄 ウの条文', '不動産登記法第51条第1項')
check('第4欄 エの条文', '第164条第1項よ')
check('今の法令の用語（拘禁刑）', '今の法律の罰則は『懲役』ではなく『拘禁刑』と書く')
check('問3 各階平面図の記録事項', '不動産登記規則第83条第1項')
check('問3 1階の位置の点線', '不動産登記事務取扱手続準則第53条')
check('問3 縮尺の注', '250分の1の縮尺（問題文の注3）')
check('第4欄 イの対比', '権利を新しく作る『形成的登記』じゃなくて、事実をありのまま報告する『報告的登記』')

# 誤った対比が残っていないこと（報告的登記の対になるのは形成的登記。2026-09-28ユーザー指摘）
for bad in ['創設的登記']:
    ok = bad not in text
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '禁止語なし : ' + bad)

# タイトルの基本形：【土地家屋調査士受験生向け】{年度}問題22（建物）〜見出し（25文字以内）〜
title = text.splitlines()[0]
prefix = '# 【土地家屋調査士受験生向け】令和7年度問題22（建物）〜'
ok = title.startswith(prefix) and title.endswith('〜') and len(title[len(prefix):-1]) <= 25
ng += (not ok)
print(('OK ' if ok else 'NG ') + 'タイトル形式 : ' + title)

# アガルートの解説（2026-09-29）と照らし合わせて追記した観点
from datetime import date
assert date(2025, 1, 21) < date(2025, 2, 6) <= date(2025, 2, 21)  # 取壊しから1月以内に申請
check('2件に分ける理由', '取壊しの分は2月21日が期限')
check('時系列メモ', '- 符号4（守衛所）：9月25日 取壊し')
check('葺の転写', '登記記録に書いてあるとおり『スレート葺』のまま写す')
check('欄番号を付けない', '欄番号を付ける必要がない')
check('会社法人等番号の括弧書き', '『（会社法人等番号　Z）』と括弧書き')
check('符号1・3を使い回さない', '一度使った符号は、その建物がなくなっても使い回さない')
check('各階平面図の所在欄', '建物の所在の欄は左右で1つだけだから、『Y市K区A町三丁目425番地6、425番地5』と1回書けばいい')

# 画像（2026-09-29生成、2026-10-02に第4欄・各階平面図の完成形を追加）：
# 記事の画像挿入マーカー11か所に、zu/ のPNGが記事の順に1枚ずつ対応しているか（マーカーの文言の鍵で確かめる）
from PIL import Image
ZU = os.path.join(os.path.dirname(__file__), 'zu')
markers = [l for l in text.splitlines() if l.startswith('> 【画像挿入】')]
PNGS = [('R7_dai22mon_dai4ran_kansei', '第4欄（問4）の完成形', 'wide'),
        ('R7_dai22mon_zu01_hensen', '建物の変遷図', None),
        ('R7_dai22mon_zu02_fugou2_ichibu_torikowashi', '符号2の1階について、工事前', None),
        ('R7_dai22mon_toukishinseisho_kansei_toi1', '問1（本件工事1）の完成した登記申請書', 'tall'),
        ('R7_dai22mon_toukishinseisho_machigai', '3コマ添削画像', 'tall'),
        ('R7_dai22mon_zu03_hashirashin_ayamari', '新築倉庫1階の誤り比較図', None),
        ('R7_dai22mon_zu04_souko_1kai_kyuuseki', '新築倉庫1階の床面積求積図', None),
        ('R7_dai22mon_zu05_souko_2kai_kyuuseki', '新築倉庫2階の床面積求積図', None),
        ('R7_dai22mon_toukishinseisho_kansei_toi2', '問2（本件工事2）の完成した登記申請書', 'tall'),
        ('R7_dai22mon_zu06_kakukai_heimenzu', '各階平面図の完成形（答案用紙の第3欄の枠の中。左右とも各階平面図）', None),
        ('R7_dai22mon_zu07_toku_junban', '本番で解く順番の図', None)]
ok = len(markers) == len(PNGS) == 11
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}（解説図7・申請書の完成形2・添削1・第4欄1）')
for (name, key, shape), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok and shape:
        w, h = Image.open(path).size
        ok = w == 1200 and (h > w if shape == 'tall' else True)   # 申請書・添削は横1200pxの縦長、第4欄は横1200px
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'マーカーとPNG（記事の順） : {name} ← {key}')
extra = sorted(set(f[:-4] for f in os.listdir(ZU) if f.endswith('.png')) - {n for n, _, _ in PNGS})
ok = not extra
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'zu/ に記事で使わないPNGがない : {extra}')
check('記事：柱の中心で測った誤りの面積', '1階は170.41平方メートル。正解より20.34平方メートルも小さくなる')
assert round(15.50 * 5.90 + 9.40 * 8.40, 2) == 170.41 and round(190.75 - 170.41, 2) == 20.34


def html_has(name, *needles):
    global ng
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        ok = n in h
        ng += (not ok)
        print(('OK ' if ok else 'NG ') + f'{name}.html : {n}')


html_has('R7_dai22mon_toukishinseisho_kansei_toi1', '建物表題部変更登記', '建物図面　各階平面図　会社法人等番号　代理権限証書',
         '（会社法人等番号　Ｚ）', 'Ｙ市Ｋ区Ａ町三丁目425番地６、425番地５', '令和7年1月21日主である建物取壊しにより変更',
         '鉄骨造スレート葺２階建', '令和7年1月21日符号2の附属建物を主である建物に変更', '令和7年1月31日種類変更、一部取壊し',
         '令和7年1月21日主である建物に変更')
html_has('R7_dai22mon_toukishinseisho_kansei_toi2', '所有権証明書', '鉄骨造合金メッキ鋼板ぶき２階建', '令和7年9月25日取壊し',
         '令和7年10月7日新築', '令和7年10月17日新築', '1階190', '2階156', '>75<')
html_has('R7_dai22mon_toukishinseisho_machigai', '令和7年10月17日新築', '令和7年9月25日取壊し', '符号6')
html_has('R7_dai22mon_dai4ran_kansei', '第4欄', '>物理<', '>報告<', '>1月<', '>10万円以下の過料<')
for bad in ['所有権証明書']:   # 問1には所有権証明書を付けない
    h = open(os.path.join(ZU, 'R7_dai22mon_toukishinseisho_kansei_toi1.html'), encoding='utf-8').read()
    ok = bad not in h
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '問1に所有権証明書がない')


# ---- 付属プロンプトとの整合（2026-09-29追加。最新の年度〈H25等〉と同じ確認）----
import re
HERE = os.path.dirname(__file__)
fig = open(os.path.join(HERE, 'prompt_R7_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_R7_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_R7_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_R7_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
draw = open(os.path.join(ZU, 'draw_R7_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()


def check_in(label, s_, src, name):
    global ng
    ok = s_ in src
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[{name}] {label} : {s_}')


def absent(label, s_, src=None, name='記事'):
    global ng
    ok = s_ not in (text if src is None else src)
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + f'[{name}] {label}（含まない） : {s_}')


for s_ in ['**登記の目的**：建物表題部変更登記', '**添付書類**：建物図面　各階平面図　会社法人等番号　代理権限証書',
           '**添付書類**：建物図面　各階平面図　所有権証明書　会社法人等番号　代理権限証書',
           'Ｙ市Ｋ区Ａ町三丁目５番６号　株式会社甲一物流（会社法人等番号　Ｚ）　代表取締役　甲山一郎',
           '変更後：Ｙ市Ｋ区Ａ町三丁目425番地６、425番地５　（原因：令和7年1月21日主である建物取壊しにより変更）',
           '「令和7年1月21日符号2の附属建物を主である建物に変更」「令和7年1月31日種類変更、一部取壊し」',
           '登記原因及びその日付「令和7年1月21日主である建物に変更」', '登記原因及びその日付「令和7年9月25日取壊し」',
           '③床面積「1階　190｜75」「2階　156｜75」', '登記原因及びその日付「令和7年10月7日新築」',
           '登記原因及びその日付「令和7年10月17日新築」', '年・月・日の数字だけを記入（青）',
           '`zu/R7_dai22mon_toukishinseisho_kansei_toi1.png`', '`zu/R7_dai22mon_toukishinseisho_kansei_toi2.png`']:
    check_in('申請書の記入', s_, form, '申請書プロンプト')
absent('登録免許税の記入', '**登録免許税**：', form, '申請書プロンプト')
for s_ in ['## 全体のレイアウト（縦に3コマ積む）', '「令和7年10月17日新築」を赤の取り消し線で消し', '「令和7年9月25日取壊し」',
           '「取り壊した時点で符号4は終わり！」「建て直した守衛所は、新しい符号6の新築として別の行に書く」',
           '`zu/R7_dai22mon_toukishinseisho_machigai.png`']:
    check_in('添削', s_, fix, '添削プロンプト')
for bad in ['✓', '✕', '横に3コマ', '横1800px']:
    absent('添削の旧版・記号', bad, fix, '添削プロンプト')

# 解説図プロンプトの頂点座標：面積を計算して求積表と一致させる
want = {138.50, 123.50, 190.75, 156.75}
got = []
for line in fig.splitlines():
    if '(Y, X) =' in line:
        pts = [tuple(map(float, m)) for m in re.findall(r'\(([\d.]+), ([\d.]+)\)', line.split('=', 1)[1])][:-1]
        got.append(round(poly_area(pts), 2))
ok = set(got) == want and len(got) == 4
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[解説図プロンプト] 頂点座標の面積 : {got}')
check_in('図3 柱の中心の形', '(0.3, 0.3) → (25.2, 0.3) → (25.2, 8.7) → (15.8, 8.7) → (15.8, 6.2) → (0.3, 6.2)', fig, '解説図プロンプト')
assert round(poly_area([(0.3, 0.3), (25.2, 0.3), (25.2, 8.7), (15.8, 8.7), (15.8, 6.2), (0.3, 6.2)]), 2) == 170.41
check_in('図3 柱の中心の面積', '170.41㎡', fig, '解説図プロンプト')
check_in('図5 除く部分', '南東の吹き抜け＋階段：Y：15.50〜23.50、X：6.50〜9.00（横8.00m×縦2.50m、面積20.00）', fig, '解説図プロンプト')
check_in('標準セットで作らない図の理由', '敷地の辺長確認図と建物図面の完成形は作らない', fig, '解説図プロンプト')
for i in range(1, 8):
    check_in(f'図{i}の見出し', f'## 図{i}：', fig, '解説図プロンプト')
for name, _, _ in PNGS:   # 生成したPNGのファイル名がプロンプトに書いてあるか
    src, nm = (fig, '解説図プロンプト') if '_zu0' in name else (form if 'kansei' in name else fix, '申請書・添削プロンプト')
    check_in('PNGのファイル名', f'zu/{name}.png', src, nm)
# 図6（各階平面図の完成形）：答案用紙の第3欄の枠の中、符号5・符号6、求積と床面積、1階の位置の点線
for s_ in ["'建物の所在'", "'Y市K区A町三丁目425番地６、425番地５'", "'家屋番号'", "'作　成　者'", "'申　請　人'",
           "'（令和7年○月○日作成）'", "'250'", "'建　物　図　面'", "'各　階　平　面　図'", "'符号5　1階'", "'符号5　2階'",
           "'符号6'", '床面積　190.75㎡', '床面積　156.75㎡', '床面積　10.00㎡', "ls='--')   # 1階の位置", 'same_scale(A6']:
    check_in('図6 各階平面図の完成形', s_, draw, '作図スクリプト')

# ---- 試験の答案用紙（touan_youshi/。2026-10-02にユーザーから受け取った実物）と欄の形の照合 ----
import pymupdf
TY = os.path.join(HERE, 'touan_youshi', 'R7_dai22mon_touan_youshi.pdf')
doc = pymupdf.open(TY)
t1 = doc[0].get_text().replace(' ', '')
t2 = doc[1].get_text().replace(' ', '')
# 1ページ目（第1欄・第2欄・第4欄）：印刷された欄名・文字
for s_ in ['第1欄', '第2欄', '第4欄', '登記の目的', '添付書類', '申請　Ｙ地方法務局', '令　和', '申　請　人', '代　理　人',
           '主である\n建物又は\n附属建物', '①種　類', '②構　造', '③床　面　積', '登記原因及び\nその日付', '所　　在',
           '家屋番号', 'ア\nイ\nウ\nエ']:
    ok = s_.replace(' ', '') in t1
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '[答案用紙1ページ] 印刷 : ' + s_.replace('\n', '／'))
for bad in ['登録免許税', '添付情報', '主たる']:
    ok = bad not in t1
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '[答案用紙1ページ] 印刷にない : ' + bad)
n_ryaku = t1.count('（略）')   # 第1欄：代理人・家屋番号の右／第2欄：申請人・代理人・家屋番号・①種類の列 ＝ 6
ok = n_ryaku == 6
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[答案用紙1ページ] （略）の数 : {n_ryaku}（6）')
# 2ページ目（第3欄）：左右とも各階平面図、家屋番号・作成者・申請人は（略）、作成年月日・縮尺の印刷
for s_ in ['第3欄', '各　階　平　面　図', '建　物　図　面', '家屋番号', '建物の所在', '作成者', '申請人', '縮尺',
           '（令和7年○月○日作成）', '250']:
    ok = s_.replace(' ', '') in t2
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '[答案用紙2ページ] 印刷 : ' + s_)
ok = t2.count('（略）') == 3 and t2.count('縮尺') == 2
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[答案用紙2ページ] （略）3つ・縮尺2つ : {t2.count("（略）")}・{t2.count("縮尺")}')
strike = [d for d in doc[1].get_drawings() if d['rect'].y0 < 60 and d['rect'].x0 > 850 and d['rect'].height < 1]
ok = len(strike) == 2   # 「建物図面」を消す二重線
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[答案用紙2ページ] 「建物図面」を消す二重線 : {len(strike)}本')

# 画像（HTML・作図スクリプト）が答案用紙の形どおりか
h1 = open(os.path.join(ZU, 'R7_dai22mon_toukishinseisho_kansei_toi1.html'), encoding='utf-8').read()
h2 = open(os.path.join(ZU, 'R7_dai22mon_toukishinseisho_kansei_toi2.html'), encoding='utf-8').read()
h4 = open(os.path.join(ZU, 'R7_dai22mon_dai4ran_kansei.html'), encoding='utf-8').read()
hm = open(os.path.join(ZU, 'R7_dai22mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for label, ok in [
        ('第1欄の見出し', '<div class="ranlab">第1欄</div>' in h1),
        ('第2欄の見出し', '<div class="ranlab">第2欄</div>' in h2),
        ('第1欄 家屋番号の記入欄＋（略）', '425番５</span></td><td class="val center" colspan="3">（略）' in h1),
        ('第2欄 家屋番号は仕切りのない（略）1つ', '家屋番号</td><td class="val" colspan="5">（略）</td>' in h2),
        ('第2欄 ①種類の列は4行で（略）1つ', h2.count('rowspan="4">（略）') == 1),
        ('第2欄 （略）の数（申請人・代理人・家屋番号・①種類）', h2.count('（略）') == 4),
        ('第1欄 （略）の数（代理人・家屋番号の右）', h1.count('（略）') == 2),
        ('見出し「③床　面　積」「主である」', all('③床　面　積' in h and '主である' in h for h in (h1, h2, hm))),
        ('登録免許税の欄がない', all('登録免許税' not in h for h in (h1, h2))),
        ('第4欄は2行2列', h4.count('<tr>') == 2 and h4.count('class="lab2"') == 4),
        ('添削③の①種類は2行で（略）1つ', 'rowspan="2">（略）' in hm),
        ('図6 家屋番号は（略）', "'家屋番号', fs=15)\n    cell(fig, 0.601, FT, 0.720, FT + 0.045, '（略）'" in draw),
        ('図6 申請人（略）', "'申　請　人', fs=14)\n    cell(fig, 0.584, BB, 0.859, FB, '（略）'" in draw),
        ('図6 左右の境は目印の線だけ', '左右の境の目印' in draw)]:
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '[画像の欄の形] ' + label)
absent('図6の家屋番号の記入', "'425番５'", draw, '作図スクリプト')
check_in('図6 答案用紙で確かめた形', '試験の答案用紙で確かめた形', fig, '解説図プロンプト')
check_in('第4欄 答案用紙で確かめた形', '2行2列の表', form, '申請書プロンプト')
check_in('申請書 答案用紙と照らした記録', '試験の答案用紙（`touan_youshi/R7_dai22mon_touan_youshi.pdf` の1ページ目。', form, '申請書プロンプト')
check('記事 第3欄の（略）', '家屋番号・作成者・申請人の欄は『（略）』と印刷済み')
for src, name in [(text, '記事'), (fig, '解説図プロンプト'), (form, '申請書プロンプト'), (fix, '添削プロンプト'), (draw, '作図スクリプト'),
                  (open(os.path.join(ZU, 'make_R7_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read(), '申請書スクリプト')]:
    for bad in ['仮の形', '仮のもの', 'リポジトリにない', '写しが手元にない']:
        absent('仮の文言', bad, src, name)
check_in('図3 柱の四角を重なり検査に登録', 'z2.markers.append(xy(P(e, s)))', draw, '作図スクリプト')
check_in('図3の注の書き分け', '〔調査・測量〕の（注）3', draw, '作図スクリプト')
fits = re.findall(r'\bfit\((.*)\)', draw)
ok = bool(fits) and all('pad_aspect=True' in f for f in fits)
ng += (not ok)
print(('OK ' if ok else 'NG ') + f'[作図スクリプト] fit はすべて pad_aspect=True（{len(fits)}か所）')

# 記事：禁止語・向き・注の書き分け
for bad in ['PDF', '創設的登記', '名変', '✕', '✓', '右上', '左下', '右側', '左側', '奥側', '手前側', '注3を読み', 'は注4の']:
    absent('禁止語・向き・注', bad)
check('注の書き分け（調査・測量）', '〔調査・測量〕の図の（注）3')
check('注の書き分け（問題文）', '問題文の注4のとおり')
check('向き（符号2の張り出しは南西）', '南西の角から南へ横5.00m×縦3.00mの張り出し部分')
check('時間配分（具体的）', '問4 → 時系列メモ → 問1 → 問2（符号5の床面積だけ空けておく）→ 倉庫の1階・2階の求積 → 問3の作図')
check('建物図面を描かない理由', '問3に『記載することを要しない』とあるから答案には描かない')

# note向けの体裁：話者名の行末に半角スペース2つ・名前の次の行がセリフ、記事の最後は区切り線
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
ng += bool(bad_speaker)
print(('OK ' if not bad_speaker else 'NG ') + f'話者名の行（ハードブレーク）: 不備 {bad_speaker}')
ok = lines[-1] == '---'
ng += (not ok)
print(('OK ' if ok else 'NG ') + '記事の最後が区切り線')

# タイトルが付属プロンプトにも引用され、見出し画像の文字とそろっているか
title_body = lines[0][2:]
for src, name in [(fig, '解説図プロンプト'), (form, '申請書プロンプト'), (fix, '添削プロンプト'), (thumb, '見出し画像プロンプト')]:
    check_in('記事タイトルの引用', title_body, src, name)
check_in('見出し画像のタイトル', '令和7年度問題22（建物）', thumb, '見出し画像プロンプト')
check_in('見出し画像のサブタイトル', '〜「主」が消えても滅失登記じゃない〜', thumb, '見出し画像プロンプト')
check_in('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像プロンプト')

# 【登場人物】の説明文が執筆プロンプトの2行と一字一句同じか（2026-09-30の統一ルール）
for s_ in ['**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。',
           '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。']:
    ok = s_ in lines
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + '登場人物の説明文 : ' + s_[:12])
absent('会社法人等番号の根拠の書き方', '問題文のただし書きに')

# 同じ話者のセリフが続いていないか（章の頭は除く）
prev = None
for i, line in enumerate(text.splitlines()):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        ok = line != prev
        ng += (not ok)
        if not ok:
            print('NG 同じ話者の連続 :', i + 1)
        prev = line

print('NG件数:', ng)
