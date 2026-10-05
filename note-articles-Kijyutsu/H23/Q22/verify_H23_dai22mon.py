"""平成23年度 第22問（建物）：記事の数値・計算・付属プロンプト・生成画像の照合スクリプト。
アガルートの解答例（第22問 解答例：第1欄・第2欄・各階平面図・建物図面）と一致することを確認済み。
アガルートの過去問集の再掲は日付を平成30年に置き換えた改題版（下の対応表）なので、日付は試験問題の本文と答案用紙に合わせている。
実行: python3 note-articles-Kijyutsu/H23/Q22/verify_H23_dai22mon.py"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
from calc_helpers import P, disp, double_area_sum  # noqa: E402

HERE = os.path.dirname(__file__)
text = open(os.path.join(HERE, 'note_H23_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_H23_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_H23_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_H23_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_H23_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


def truth(label, cond):
    global ng
    ng += (not cond)
    print(('OK ' if cond else 'NG ') + f'[計算] {label}')


def trunc2(v):
    """床面積の端数処理：1平方メートルの100分の1未満を切り捨て。"""
    return math.floor(v * 100 + 1e-9) / 100


def poly_area(pts):
    n = len(pts)
    return abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2


# ---- 日付の対応表（アガルートの改題版 → 試験問題の本文・答案用紙）----
DATES = {'平成30年10月2日': '平成23年8月2日', '平成30年10月4日': '平成23年8月4日',
         '平成30年10月12日': '平成23年8月12日', '平成30年10月21日': '平成23年8月21日'}
for old, new in DATES.items():
    absent('改題版の日付', old)
    absent('改題版の日付', old, form, '申請書')
    check('本試験の日付', new)
check('照合済みの一文（改題の説明は書かない。2026-09-30、ユーザー指示）', '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')
absent('改題の説明', '改題')

# ---- 敷地（座標リスト）：F-789SGの表示と辺長 ----
A, B, C, D, E = P(254.43, 187.17), P(241.25, 187.17), P(239.25, 185.17), P(239.25, 163.79), P(254.43, 163.79)
F, G, H, I, J = P(233.25, 193.63), P(207.84, 190.15), P(209.39, 175.36), P(211.13, 158.65), P(233.25, 158.65)
assert disp(abs(B - C)).startswith('2.8284…') and disp(abs(F - G)).startswith('25.6471…')
check('BCの表示', '- 表示：2.8284…')
check('BCの電卓操作', '`[Abs] [ALPHA] [B] [−] [ALPHA] [C] [)] [=]`')
check('FGの表示', 'で表示が 25.6471…、25.65mです')
sides = {'EA': (E, A, '23.38'), 'AB': (A, B, '13.18'), 'CD': (C, D, '21.38'), 'DE': (D, E, '15.18'), 'JF': (J, F, '34.98'),
         'GH': (G, H, '14.87'), 'HI': (H, I, '16.80'), 'IJ': (I, J, '22.12'), 'BC': (B, C, '2.83'), 'FG': (F, G, '25.65')}
for k, (p, q, s) in sides.items():
    truth(f'辺長 {k} {s}', f'{abs(p - q):.2f}' == s)
    check(f'辺長 {k}', f'{k} {s}', fig, '解説図')
a52 = abs(double_area_sum([E, A, B, C, D]).imag) / 2
a101 = abs(double_area_sum([J, F, G, H, I]).imag) / 2
truth('5番2の面積 352.9084', round(a52, 4) == 352.9084 and trunc2(a52) == 352.90)
truth('10番1の面積 792.72795', round(a101, 5) == 792.72795 and trunc2(a101) == 792.72)
check('面積と登記記録', '10番1は792.72平方メートルで、登記記録の792.95平方メートルとほぼ合います。5番2は352.90平方メートルで、登記記録の357.70平方メートルより4.8平方メートルくらい少ないです')
check('辺長は建物図面に書かない', 'この辺長も面積も作図のチェック用で、建物図面には書かない')
truth('道路の幅 6.00', round(C.real - F.real, 2) == 6.00)
check('道路の幅', '間の道路の幅は6.00mです')

# ---- 建物図面：距離と所在 ----
WN, WE_OLD = 254.43 - 1.0 - 0.06, 187.17 - 7.0 - 0.06
WW, WE_NEW = WE_OLD - 10.01, WE_OLD + 2.50
truth('東の距離 7.0 − 2.5 ＝ 4.5', round(187.17 - (WE_NEW + 0.06), 2) == 4.50)
check('東の距離', '7.0 − 2.5 ＝ 4.5')
truth('西の距離 約6.3', round(WW - 0.06 - 163.79, 2) == 6.25)
truth('南の距離 約5.0', round((WN - 9.10 - 0.06) - 239.25, 2) == 4.96)
check('所在の確認（5番2）', '西の外壁は西の筆界から約6.3、南の張り出しの外壁は南の筆界から約5.0。5番2の中に収まっています')
GN = 233.25 - 1.0
Y_FG = F.imag - (F.real - GN) * (F.imag - G.imag) / (F.real - G.real)
GE_OUT = Y_FG - 5.0
GS_OUT = GN - 5.50 - 0.06
Y_FG_S = F.imag - (F.real - GS_OUT) * (F.imag - G.imag) / (F.real - G.real)
truth('北東の角でFGのY 193.49…', f'{Y_FG:.4f}'.startswith('193.49'))
truth('南東の角では約4.2', round(Y_FG_S - GE_OUT, 1) == 4.2)
check('北東の角から5.0', 'でのFGのY座標は193.49…だから、そこから5.0西が外壁。南東の角のあたりではFGが西に寄ってくるので、約4.2しかありません')
GW_OUT = GE_OUT - 0.06 - 9.00 - 0.06   # 東の外壁 → 東の壁の中心 → 西の壁の中心 → 西の外壁
truth('一棟の西の外壁から西の筆界 約20.7', round(GW_OUT - J.imag, 1) == 20.7)
truth('一棟の南の外壁から南の筆界 17m以上', GS_OUT - max(G.real, H.real) > 17)
check('所在の確認（一棟）', '西の外壁が10番1の西の筆界から約20.7、南の外壁も南の筆界から17m以上離れているので、10番1の中だけです')
check('建物図面の建物の所在', '『A市B町二丁目5番地2、A市B町五丁目10番地1』')
check('実線・点線', '畑山さんの部分（専有部分）を実線、それが属する一棟の建物の1階を点線で描くの（準則第52条第2項）')
check('行政界', '建物図面にもその一点鎖線を描いて、『A市B町二丁目』『A市B町五丁目』と書き添えるの')
check('建物図面の申請人', '『畑山邦彦』と書きます')

# ---- 床面積 ----
f1 = 10.01 * 7.28 + 5.46 * 1.82 + 2.50 * 6.37
truth('1階 98.7350 → 98.73（四捨五入は98.74）', round(f1, 4) == 98.735 and trunc2(f1) == 98.73 and round(f1 + 1e-9, 2) == 98.74)
truth('82.81 ＋ 15.925 ＝ 98.735', round(82.81 + 2.50 * 6.37, 3) == 98.735)
truth('2階 66.2480 → 66.24', round(9.10 * 7.28, 4) == 66.248 and trunc2(9.10 * 7.28) == 66.24)
truth('東の辺 9.10 − 6.37 ＝ 2.73', round(9.10 - 6.37, 2) == 2.73)
truth('北の辺 10.01 ＋ 2.50 ＝ 12.51', round(10.01 + 2.50, 2) == 12.51)
check('四捨五入の誤答', '小数第3位が5だから四捨五入して、98.74平方メートルです！')
check('切り捨て', '98.735は切り捨てて98.73よ')
check('1階求積表', '- 10.01 × 7.28 ＝ 72.8728\n- 5.46 × 1.82 ＝ 9.9372\n- 2.50 × 6.37 ＝ 15.9250\n- 合計：98.7350 （床面積：98.73平方メートル）')
check('2階求積表', '- 9.10 × 7.28 ＝ 66.2480\n- 合計：66.2480 （床面積：66.24平方メートル）')
check('構造変更なし（問題文の注8）', '構造は変更なしです')
s_ng1, s_ng2, s_ok = 4.50 * 5.50, (4.50 - 0.12) * (5.50 - 0.12), (4.50 - 0.12) * (5.50 - 0.06)
truth('壁心 24.75', round(s_ng1, 2) == 24.75)
truth('4辺とも引く 23.5644 → 23.56', round(s_ng2, 4) == 23.5644 and trunc2(s_ng2) == 23.56)
truth('内法 23.8272 → 23.82', round(s_ok, 4) == 23.8272 and trunc2(s_ok) == 23.82)
check('壁心の誤答', '4.50 × 5.50 ＝ 24.75平方メートル！')
check('4辺とも引く誤答', '4.38 × 5.38 ＝ 23.5644、23.56平方メートルです！')
check('符号1求積表', '- 4.38 × 5.44 ＝ 23.8272\n- 合計：23.8272 （床面積：23.82平方メートル）')
check('シャッター', '『シャッターの厚さは考慮しないものとする』')
truth('一棟 9.00×5.50 ＝ 49.50', round(9.00 * 5.50, 2) == 49.50)
check('一棟の床面積', '9.00 × 5.50 ＝ 49.50平方メートル')

# ---- 問1（第1欄）----
check('登記の目的', '登記の目的は『建物表題部変更登記』')
check('申請人', '『A市B町二丁目5番地2　畑山邦彦』')
check('所在は5番地2のまま', '建物の表示の一番上の所在の欄は、主である建物の『A市B町二丁目5番地2』のまま')
check('所在の根拠', '（不動産登記法第44条第1項第5号のかっこ書き）')
check('所在の根拠（別表二）', '（不動産登記規則別表二）')
check('主の2行', '原因は『③平成23年8月2日増築』です')
check('符号1の行', '構造の欄は『A市B町五丁目10番地1　コンクリートブロック造陸屋根平家建　床面積49.50㎡』と一棟の建物を書いて、続けて専有部分の『コンクリートブロック造陸屋根平家建』')
check('原因2つ', '『平成23年8月2日新築』『平成23年8月4日敷地権』')
check('敷地権の表示', '『敷地権の表示　A市B町五丁目10番1　宅地　792.95㎡の土地の所有権6分の2』')
check('敷地権（区分所有法22条1項本文）', '（同法第22条第1項本文）')
check('敷地権（法44条1項9号）', '（不動産登記法第44条第1項第9号）')
check('6分の2のまま', 'そのまま『6分の2』よ')
check('縦割りは屋根まで', '建物を階層的に区分したとき（準則第81条第3項）')
check('添付書類', '添付書類は、建物図面、各階平面図、所有権証明書、代理権限証書の4つです')
check('添付の根拠', '（不動産登記令別表14の項添付情報欄ロ（1）（2））')
check('登録免許税', '表題部変更登記は非課税です')
check('区分の登記ではない', '附属建物が区分建物だからといって、建物の区分の登記をしたわけじゃない')

# ---- 問2・問3 ----
check('問2のなお書き', '『各階平面図については、求積及びその方法並びに床面積の表示の記載を省略して差し支えない』')
check('寸法の累計', '東西は、0（西の外壁）、0.91（2階の西の外壁）、4.55（南の張り出しの西）、10.01（元の東の外壁＝2階の東）、12.51（増築部分の東）')
check('問3の誤答（場所）', '道路の向こうの別の町にあるときです！')
check('問3の要件', '主である建物と効用上一体として利用される状態にあること（準則第78条第1項）')
DAI2 = ('車庫が、家屋番号5番2の建物（居宅）の効用を補うために利用されていない場合は、附属建物と認められない。')
check('第2欄の結論', DAI2)
check('第2欄の結論', DAI2, form, '申請書')

# ---- 登記の目的の判定（第1章）----
check('増築の誤答', '10番1の建物の表題部変更登記で、5番2の申請書には関係ないと思います！')
check('区分所有法1条', '（建物の区分所有等に関する法律第1条）')
check('準則78条2項', '（不動産登記事務取扱手続準則第78条第2項）')
check('法2条23号', '（不動産登記法第2条第23号）')
check('10番1の登記は問われていない', '本問では聞かれていないわ')
check('時系列メモ', '- 平成23年8月4日：畑山さんが、10番1の土地の共有者の海野洋子さんから持分の一部を取得（調査の結果4）')
check('1月以内', '8月2日から1月以内（不動産登記法第51条第1項）')

# ---- 付属プロンプトの記入データ ----
for s_ in ['**登記の目的**：建物表題部変更登記', '**添付書類**：建物図面　各階平面図　所有権証明書　代理権限証書',
           '**申請人**：Ａ市Ｂ町二丁目５番地２　畑山邦彦', '平成23年8月21日申請　Ａ地方法務局', '1段目「Ａ市Ｂ町二丁目５番地２」',
           '**家屋番号**：５番２', '②構造「木造かわらぶき２階建」／③床面積「1階　82｜81」「2階　66｜24」',
           '③床面積「1階　98｜73」「2階　66｜24」／登記原因及びその日付「③平成23年8月2日増築」',
           '②構造「Ａ市Ｂ町五丁目10番地１　コンクリートブロック造陸屋根平家建　床面積49.50㎡」', '③床面積「23｜82」',
           '「平成23年8月2日新築」と改行して「平成23年8月4日敷地権」',
           '「敷地権の表示　Ａ市Ｂ町五丁目10番１　宅地　792.95㎡の土地の所有権6分の2」', '**登録免許税**：欄がないので書かない']:
    check('申請書の記入データ', s_, form, '申請書')
check('誤答', '③床面積：「24｜75」', fix, '添削')
check('正解', '「平成23年8月2日新築」と改行して「平成23年8月4日敷地権」', fix, '添削')
check('縦に積む', '横1200pxの縦長の1枚の画像に、上から「①誤答」「②添削（赤ペン）」「③正解」の3コマ', fix, '添削')

# ---- 解説図プロンプトの頂点座標（面積が求積表と一致すること）----
RECTS = [('図9 1階', [(0, 0), (12.51, 0), (12.51, 6.37), (10.01, 6.37), (10.01, 9.1), (4.55, 9.1), (4.55, 7.28), (0, 7.28)], 98.735),
         ('図9 2階', [(0.91, 0), (10.01, 0), (10.01, 7.28), (0.91, 7.28)], 66.248),
         ('図10 誤り1', [(0, 0), (4.5, 0), (4.5, 5.5), (0, 5.5)], 24.75),
         ('図10 誤り2', [(0.06, 0.06), (4.44, 0.06), (4.44, 5.44), (0.06, 5.44)], 23.5644),
         ('図10 正解', [(0.06, 0), (4.44, 0), (4.44, 5.44), (0.06, 5.44)], 23.8272)]
for label, pts, want in RECTS:
    truth(f'{label} の面積 {want}', round(poly_area(pts), 4) == want)
    check(label + ' 頂点座標', ' → '.join(f'({a:g}, {b:g})' for a, b in pts + [pts[0]]), fig, '解説図')
check('標準セットを作る理由', '執筆プロンプトの「想定する画像の標準セット」（敷地の辺長確認図・建物図面の完成形・誤り比較図・各階の求積図）はすべて作る', fig, '解説図')
check('建物図面の距離', '5番2の北1.0（北西の角と増築部分の北東の角）、東4.5（増築部分の東の外壁から）', fig, '解説図')

# ---- 誤記・禁止語 ----
for bad in ['PDF', '右上', '左下', '右側', '左側', '✕', '✓', '名変', '創設的登記', '98.74平方メートル。', '登録免許税は1,000円']:
    absent('誤記・混入', bad)
for bad in ['✕', '✓']:
    absent('記号', bad, fig, '解説図')
    absent('記号', bad, fix, '添削')
absent('所在の欄に10番地1', '所在**：Ａ市Ｂ町二丁目５番地２、', form, '申請書')

# ---- 注の書き分け：問題文の注は「問題文の注N」 ----
bare = [m.start() for m in re.finditer(r'注[0-9]', text) if not text[:m.start()].endswith('問題文の')]
truth(f'注の書き分け（「問題文の」のない「注N」 {len(bare)}か所）', not bare)
for s_ in ['〔見取図〕の（注）', '〔コンクリートブロック造の車庫の詳細図〕の（注）', '問題文の注9', '問題文の注3', '問題文の注4',
           '問題文の注5', '問題文の注8', '問題文の注10']:
    check('注の書き分け', s_)

# ---- 条文（note-articles/laws/ の原典で確認したもの）----
for s_ in ['（不動産登記規則第115条）', '（不動産登記規則第82条第1項）', '（規則第82条第2項）', '（不動産登記規則第83条第1項）',
           '（不動産登記規則第74条第2項）', '（同令第7条第1項第2号）', '（登録免許税法別表第一の一（十三））', '（同法第2条第5項）',
           '（準則第78条第1項）', '（同法第22条第2項）']:
    check('条文', s_)

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
truth(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
prev = None
for i, line in enumerate(lines):
    if line.startswith('## '):
        prev = None
    elif line in ('**トリ先生**  ', '**藍子**  '):
        if line == prev:
            truth(f'同じ話者の連続（{i + 1}行目）', False)
        prev = line
truth('記事の最後が区切り線', lines[-1] == '---')
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成23年度問題22（建物）〜'
sub = title[len(prefix):-1]
truth(f'タイトル形式（見出し{len(sub)}文字）: {title}', title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成23年度問題22（建物）', thumb, '見出し画像')

# ---- 画像：画像挿入マーカー21か所と zu/ のPNGの対応（2026-10-05、本文に対して足りなかった図10枚と所在の欄の添削を足し、図の番号を記事の挿入順に振り直した）----
from PIL import Image  # noqa: E402
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('H23_dai22mon_zu01_hantei_nagare', '判定の流れ'),
        ('H23_dai22mon_zu02_ittou_kankei', 'コンクリートブロック造の車庫の平面図'),
        ('H23_dai22mon_zu03_jikeiretsu', '時系列メモの図'),
        ('H23_dai22mon_zu04_chuu_shiwake', '注の仕分けの図'),
        ('H23_dai22mon_zu05_shikichi_kakunin', '敷地確認図'),
        ('H23_dai22mon_zu06_higashi_kyori', '東の距離の比較図'),
        ('H23_dai22mon_zu07_shozai_kakunin', '筆の中に収まるかの確認図'),
        ('H23_dai22mon_zu08_tatemono_zumen', '建物図面の完成形'),
        ('H23_dai22mon_zu09_omoya_kyuuseki', '主である建物の求積図'),
        ('H23_dai22mon_zu10_shako_ayamari_hikaku', '誤り比較図'),
        ('H23_dai22mon_zu11_uchinori_kabeshin', '壁心と内法が混ざる'),
        ('H23_dai22mon_zu12_touki_kiroku', '登記記録のどこに載るか'),
        ('H23_dai22mon_toukishinseisho_machigai_shozai', '所在の欄の①誤答'),
        ('H23_dai22mon_zu13_shikichiken', '敷地権が生じるまで'),
        ('H23_dai22mon_toukishinseisho_machigai', '符号1の行の①誤答'),
        ('H23_dai22mon_zu14_tenpu_shorui', '添付書類の要否の表'),
        ('H23_dai22mon_toukishinseisho_kansei', '問1の完成した登記申請書'),
        ('H23_dai22mon_zu15_kakai_heimenzu', '各階平面図の完成形'),
        ('H23_dai22mon_zu16_fuzoku_hantei', '使い方で決まる'),
        ('H23_dai22mon_toukishinseisho_kansei_dai2ran', '答案用紙第2欄の完成形'),
        ('H23_dai22mon_zu17_toku_junban', '本番で解く順番の図')]
truth(f'画像挿入マーカーの数 {len(markers)}（解説図17・添削2・完成形2）', len(markers) == len(PNGS) == 21)
truth('解説図の番号が記事の挿入順', [int(re.search(r'_zu(\d\d)_', n).group(1)) for n, _ in PNGS if '_zu' in n] == list(range(1, 18)))
zu_files = sorted(f for f in os.listdir(ZU) if f.endswith('.png'))
truth(f'zu/ のPNGはマーカーと1対1（{len(zu_files)}枚）', zu_files == sorted(n + '.png' for n, _ in PNGS))
for (name, key), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        if name.endswith('dai2ran'):
            ok = w == 1200
        elif 'toukishinseisho' in name:
            ok = w == 1200 and h > w
        else:
            ok = w >= 1600 and h >= 800
    truth(f'PNG（マーカー順） : {name}', ok)
    check('生成済みファイル名', name.replace('H23_dai22mon_', ''), fig if re.search(r'_zu\d\d_', name) else (fix if 'machigai' in name else form),
          '付属プロンプト')


def html_has(name, *needles, bad=()):
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    if name.endswith('dai2ran'):   # 第2欄は罫線の行ごとに文字列が切れているので、タグを外してつなげて調べる
        h = re.sub(r'<[^>]+>', '', h)
    for n in needles:
        truth(f'{name}.html : {n}', n in h)
    for n in bad:
        truth(f'{name}.html に無い : {n}', n not in h)


html_has('H23_dai22mon_toukishinseisho_kansei', '建物表題部変更登記', '建物図面　各階平面図　所有権証明書　代理権限証書',
         '平成23年8月21日申請', 'Ａ地方法務局', 'Ａ市Ｂ町二丁目５番地２　畑山邦彦', '５番２', '木造かわらぶき２階建', '居宅',
         '1階　82', '2階　66', '1階　98', '>73<', '③平成23年8月2日増築', '符号1', '車庫',
         'Ａ市Ｂ町五丁目10番地１　コンクリートブロック造陸屋根平家建　床面積49.50㎡', '>23<', '>82<', '平成23年8月2日新築',
         '平成23年8月4日敷地権', '敷地権の表示　Ａ市Ｂ町五丁目10番１　宅地　792.95㎡の土地の所有権6分の2', '（略）',
         bad=('登録免許税', '平成30年', '>74<', '>75<', '会社法人等番号', '住所証明書', '規約証明書'))
html_has('H23_dai22mon_toukishinseisho_kansei_dai2ran', '附属建物と認められない', '不動産登記法第2条第23号',
         '準則第78条第1項', '第三者に賃貸')
html_has('H23_dai22mon_toukishinseisho_machigai_shozai', '①誤答', '②添削（赤ペン）', '③正解', 'Ａ市Ｂ町二丁目５番地２',
         'Ａ市Ｂ町二丁目５番地２、Ａ市Ｂ町五丁目10番地１', '平成23年8月2日変更', '法第44条第1項第5号かっこ書き', '規則別表二',
         '2段目も原因も空欄')
html_has('H23_dai22mon_toukishinseisho_machigai', '①誤答', '②添削（赤ペン）', '③正解', '>24<', '>75<',
         '平成23年8月4日敷地権', '一棟の建物の所在・構造・床面積と敷地権も書く')
drw = open(os.path.join(ZU, 'draw_H23_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
fits = []
for m in re.finditer(r'\bfit\(', drw):
    depth, j = 0, m.end() - 1
    for j in range(m.end() - 1, len(drw)):
        depth += {'(': 1, ')': -1}.get(drw[j], 0)
        if depth == 0:
            break
    fits.append(drw[m.start():j + 1])
truth(f'作図の fit はすべて pad_aspect=True（{len(fits)}か所）', fits and all('pad_aspect=True' in f for f in fits))
# 図面の完成形は答案用紙（その2）の欄の枠の中に描く（2026-09-30のH27/Q22の作り直しで入ったルール）
for s_ in ["'家屋番号'", "'建物の所在'", "KAOKU = '5番2'", "SHOZAI = 'A市B町二丁目5番地2、A市B町五丁目10番地1'",
           "SHINSEININ = '畑山邦彦'", "'申　請　人'", "'作　成　者'", "'（略）'", "'（平成23年8月21日作成）'", "'1/500'", "'1/250'",
           "'建　物　図　面'", "'各　階　平　面　図'", "答案用紙（その2）の欄・縮尺1/500で描く内容",
           "答案用紙（その2）の欄・縮尺1/250で描く内容", "fit(ax, F1 + Q(F1, O2) + Q(g, O3)"]:
    check('図面の欄の枠', s_, drw, '作図')
check('記事の家屋番号', '家屋番号は『5番2』')
check('記事の建物の所在', '『A市B町二丁目5番地2、A市B町五丁目10番地1』')
check('記事の図面の申請人', '『畑山邦彦』と書きます')
for key in ['答案用紙（その2）の建物図面の欄の枠', '答案用紙（その2）の各階平面図の欄の枠']:
    check('マーカーに欄の枠', key)
for s_ in ['答案用紙（その2）の建物図面の欄の枠', '答案用紙（その2）の各階平面図の欄の枠', '同じ縮尺（1/250）',
           'public/kijutsu/H23-tatemono/a2.webp']:
    check('図のプロンプトに欄の枠', s_, fig, '解説図')
# fit は文字より先（2026-09-30、H21/Q22）：各関数の中で fit が最初の文字の配置より前にあるか
for fn in re.findall(r'def (zu02|zu05|zu06|zu07|zu08|zu09|zu15|garage_panel)\(.*?\):(.*?)(?=\ndef )', drw, re.S):
    body = fn[1]
    i_fit = body.find('fit(')
    i_txt = min([body.find(k) for k in ['free_text(', 'edge_label(', 'callout(', 'dims(', 'point_label('] if body.find(k) >= 0]
                or [10 ** 9])
    if 'garage_panel(' in body and i_fit < 0:      # 図10は garage_panel の中で fit する
        continue
    truth(f'作図 {fn[0]}：fit が文字の配置より先', 0 <= i_fit < i_txt)
for s_ in ['== 98.735', '== 66.24', '== 49.50', '== 23.8272', '== 23.5644', '== 24.75', '== 4.50', '== 352.9084', '== 792.72795']:
    check('作図スクリプトの assert', s_, drw, '作図')

# ---- 2026-10-05追加の図：記事の会話の事実・数値と作図スクリプト・プロンプトの一致 ----
check('所在の欄の誤答', '1段目の『A市B町二丁目5番地2』の下の2段目に『A市B町二丁目5番地2、A市B町五丁目10番地1』、所在が増えたので右の枠に原因『平成23年8月2日変更』も書くんですよね？')
for s_ in ["'H23_dai22mon_zu01_hantei_nagare'", "'問い1　既存の車庫と構造上・利用上の\\n独立性があるか（問題文の注9）'",
           "'5番2の符号1の附属建物\\n（不動産登記法第2条第23号、\\n準則第78条第1項）",
           "'H23_dai22mon_zu03_jikeiretsu'", "主：③平成23年8月2日増築\\n符号1：平成23年8月2日新築", "'符号1：平成23年8月4日敷地権'",
           "'H23_dai22mon_zu04_chuu_shiwake'", "'H23_dai22mon_zu06_higashi_kyori'", "'7.0'", "'4.5'",
           "'H23_dai22mon_zu07_shozai_kakunin'", "'約6.3'", "'約5.0'", "'約20.7'", "'約4.2'", "'約18.7'",
           "== 6.25", "== 4.96", "== 20.7", "== 4.2", "== 18.7",
           "'H23_dai22mon_zu11_uchinori_kabeshin'", "'9.00×5.50＝49.50㎡\\n（構造の欄に書く）'", "'4.38×5.44＝23.82㎡\\n（床面積の欄に書く）'",
           "'H23_dai22mon_zu12_touki_kiroku'", "'所在　A市B町二丁目5番地2　　（ここは変わらない）'",
           "'H23_dai22mon_zu13_shikichiken'", "第22条第1項本文", "（区分所有法第2条第5項）",
           "'原因：平成23年8月2日新築　平成23年8月4日敷地権　／　敷地権の表示：所有権6分の2'",
           "'H23_dai22mon_zu14_tenpu_shorui'", "床面積の変更（不動産登記令別表14の項添付情報欄ロ（1））", "'代理人による申請（同令第7条第1項第2号）'",
           "'H23_dai22mon_zu16_fuzoku_hantei'", "'藍子の誤答：「道路の向こうの別の町にあるときは、附属建物にできない」'"]:
    check('追加の図（作図スクリプト）', s_, drw, '作図')
# 記事の本文の数値が図にもある（本文にだけある数値を残さない）
for s_ in ['約6.3', '約5.0', '約20.7', '約4.2', '7.0 − 2.5 ＝ 4.5', '6分の2', '8月4日']:
    check('本文の数値', s_)
for s_ in ['## 図1：車庫の「増築」はどの登記になるかの判定の流れ', '## 図6：東の距離の比較図', '## 図7：建物が自分の筆の中に収まるかの確認図',
           '## 図12：一棟の建物の所在が登記記録のどこに載るかの図', '## 図13：敷地権が生じるまでの図', '## 図14：添付書類の要否の表',
           '## 図16：附属建物と認められるかの図', '西約6.3（170.10 − 0.06 − 163.79 ＝ 6.25）', '南約18.7（226.69 − 208.01）']:
    check('解説図プロンプト', s_, fig, '解説図')
check('添削2', '# 添削2：「所在」欄の誤答→添削→正解（2026-10-05追加）', fix, '添削')
check('添削2の誤答', '所在の2段目の右の枠（原因）：「平成23年8月2日変更」', fix, '添削')

print('NG件数:', ng)
