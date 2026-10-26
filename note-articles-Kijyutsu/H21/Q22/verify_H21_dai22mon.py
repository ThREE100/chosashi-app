"""平成21年度 第22問（建物）：記事の数値・計算・付属プロンプト・生成画像の照合スクリプト。
アガルートの解答例（第22問 解答例：問1の登記申請書・問2・問3の各階平面図と建物図面）と照合した。
アガルートの過去問集の再掲は日付を平成30年に置き換え、答案用紙の見出しを「主である建物」に変えていた（下の対応表）ので、
日付と欄の名前は試験問題の本文と試験の答案用紙に合わせている。
構造は、ユーザーの指示（2026-09-30）で解答例どおり「木造かわらぶき3階建」とした（床面積に算入する部分の屋根面積の
30％未満の種類の屋根は表示しない。昭和63年3月24日民三第1826号。択一式の平成25年度第12問・平成29年度第16問で出題）。
解答例との食い違いはない。
実行: python3 note-articles-Kijyutsu/H21/Q22/verify_H21_dai22mon.py"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(HERE, 'note_H21_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
fig = open(os.path.join(HERE, 'prompt_H21_dai22mon_kaisetsuzu.md'), encoding='utf-8').read()
form = open(os.path.join(HERE, 'prompt_H21_dai22mon_toukishinseisho_gazou.md'), encoding='utf-8').read()
fix = open(os.path.join(HERE, 'prompt_H21_dai22mon_toukishinseisho_machigai.md'), encoding='utf-8').read()
thumb = open(os.path.join(HERE, 'prompt_H21_dai22mon_miidashi_gazou.md'), encoding='utf-8').read()
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


# ---- 日付の対応表（アガルートの過去問集の再掲 → 試験問題の本文・答案用紙）。照合の作業の中だけで使う ----
DATES = {'平成30年10月8日': '平成21年8月8日', '平成30年10月10日': '平成21年8月10日', '平成30年10月23日': '平成21年8月23日'}
for old, new in DATES.items():
    absent('再掲の日付', old)
    absent('再掲の日付', old, form, '申請書')
    check('本試験の日付', new)
check('照合済みの一文（改題の説明は書かない）', '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')
absent('改題の説明', '改題')
absent('再掲の見出し「主である建物又は附属建物」', '主である建物又は附属建物', form, '申請書')
check('答案用紙の見出し', '「主たる建物又は附属建物」', form, '申請書')

# ---- アガルートの解答例の答え（日付は本試験に戻したもの）と記事の一致 ----
AGAROOT = {
    '登記の目的': '登記の目的は『建物表題登記』',
    '添付書類': '添付書類は、建物図面、各階平面図、所有権証明書、住所証明書、代理権限証書の5つです',
    '申請人': '申請人は『A市B町二丁目3番地4　土野一郎』',
    '代理人': '代理人は『A市C町五丁目6番地7　家野二郎』',
    '所在': '所在は『A市B町二丁目3番地4』',
    '家屋番号': '家屋番号は『（記載不要）』と印刷済み',
    '種類・床面積': '種類『居宅』、構造『木造かわらぶき3階建』、床面積は『1階　41.40』『2階　33.12』『3階　8.28』',
    '原因': '『平成21年8月8日新築』です',
    '欄外': '『土地家屋調査士　家野二郎』と書きます',
    '問2 確認済証': '- 建築基準法第6条の確認があったことを証する書面（確認済証）',
    '問2 検査済証': '- 建築基準法第7条の検査があったことを証する書面（検査済証）',
    '問2 工事完了引渡証明書': '- 株式会社建倉工務店が作成した工事完了引渡証明書（同社の印鑑証明書付き）',
    '建物図面 北3.10': '1.10 ＋ 2.00 ＝ 3.10 です',
    '建物図面 西1.00×2': '北の3.10と、西の1.00を2か所',
    '建物図面の所在': '『建物の所在』は『A市B町二丁目3番地4』',
    '1階求積': '- 6.37 × 1.82 ＝ 11.5934\n- 5.46 × 5.46 ＝ 29.8116\n- 合計：41.4050 （床面積：41.40平方メートル）',
    '2階求積': '- 4.55 × 1.82 ＝ 8.2810\n- 5.46 × 4.55 ＝ 24.8430\n- 合計：33.1240 （床面積：33.12平方メートル）',
    '3階求積': '- 4.55 × 1.82 ＝ 8.2810\n- 合計：8.2810 （床面積：8.28平方メートル）',
    '1階の辺': '- 1階：北6.37、東1.82、段差0.91、東5.46、南5.46、西7.28',
    '2階の辺': '- 2階：北4.55、吹抜の段差1.82と0.91、東4.55、南5.46、西6.37',
    '3階の辺': '- 3階：4.55×1.82',
}
for k, s_ in AGAROOT.items():
    check('解答例と一致：' + k, s_)
# 構造：屋根の種類が2種類以上ある建物は、床面積に算入する部分の屋根面積の30％未満の種類の屋根を表示しない
# （昭和63年3月24日民三第1826号。択一式の H25/Q12・H29/Q16 で出題）。玄関の小屋根は約4％なので「木造かわらぶき3階建」（解答例と一致）。
check('構造（解答例と一致）', '構造は『木造かわらぶき3階建』です」')
check('30％の先例', '30％未満の種類の屋根は構造に表示しないの（昭和63年3月24日民三第1826号）')
check('択一式の出題', '平成25年度第12問（基準は10％ではなく30％）と平成29年度第16問（65％と35％なら両方書く）')
check('小屋根の割合（概算と書く）', '1.6562 ÷ 41.405 で概算で約4％')
ratio = 0.91 * 1.82 / (6.37 * 1.82 + 5.46 * 5.46)
truth(f'玄関の小屋根の割合 {ratio:.4f}（約4％、30％未満）', round(ratio * 100) == 4 and ratio < 0.30)
absent('旧版の説明（小さい屋根を省く答え方を否定）', '小さい屋根は構造に書かないで済ませる')
absent('旧版の構造', '大屋根が先で、『木造かわら・合金メッキ鋼板ぶき3階建』です')
check('並べて書く誤答（藍子）', '構造は『木造かわら・合金メッキ鋼板ぶき3階建』です！')
check('区分名（準則81条1項）', '準則第81条第1項の区分にある『合金メッキ鋼板ぶき』ですね')
check('並べて書く規定（準則81条2項）', '（準則第81条第2項）')
truth('「アガルート」は冒頭の照合済みの一文だけ', text.count('アガルート') == 1)
absent('予備校の誤りの断定', '予備校')

# ---- 敷地と建物図面（座標値一覧表なし。〔配置図〕の距離で確かめる） ----
truth('後退線は道路境界線から 2.00 − 0.90 ＝ 1.10', round(2.00 - 1.80 / 2, 2) == 1.10)
check('後退線の位置', '2.00 − 0.90 ＝ 1.10 南の、3番4の土地の中を通る線よ')
check('後退線の誤答', '北に2.00と書きます！')
check('筆界は道路境界線', '筆界は、あくまで道路境界線なんですね')
truth('北の距離 3.10', round(1.10 + 2.00, 2) == 3.10)
ew, ns = 6.37 + 0.18, 7.28 + 0.18
truth('東西の外壁間 6.55・東の余り 2.45', round(ew, 2) == 6.55 and round(10.00 - 1.00 - ew, 2) == 2.45)
truth('南北の外壁間 7.46・南の余り 2.54', round(ns, 2) == 7.46 and round(13.10 - 3.10 - ns, 2) == 2.54)
check('所在の確認（東西）', '外壁から外壁までは 6.37 ＋ 0.18 ＝ 6.55。西の1.00と足して7.55で、東の筆界までは 10.00 − 7.55 ＝ 2.45 あります')
check('所在の確認（南北）', '南の筆界までは 13.10 − 10.56 ＝ 2.54 です')
check('複素数モード不要', 'F-789SGの複素数モードの出番はないわ')
check('辺長は建物図面に書かない', 'この辺長は作図のチェック用で、建物図面には書かないのよ')
check('建物図面の申請人', '『土野一郎』と書きます（不動産登記規則第74条第2項）')
check('建物図面の家屋番号', '上の『家屋番号』は、登記所が付けるものなので空けておきます')
check('隣接地', '隣接地の地番（西の3－3、東の3－5、南の3－11、南西の3－12、南東の3－10）と北の道路')

# ---- 床面積・階数 ----
f1 = 6.37 * 1.82 + 5.46 * 5.46
f2 = 4.55 * 1.82 + 5.46 * 4.55
f3 = 4.55 * 1.82
truth('1階 41.4050 → 41.40（四捨五入は41.41）', round(f1, 4) == 41.405 and trunc2(f1) == 41.40 and round(f1 + 1e-9, 2) == 41.41)
truth('2階 33.1240 → 33.12', round(f2, 4) == 33.124 and trunc2(f2) == 33.12)
truth('3階 8.2810 → 8.28', round(f3, 4) == 8.281 and trunc2(f3) == 8.28)
truth('西の辺 1.82 ＋ 1.82 ＋ 3.64 ＝ 7.28', round(1.82 + 1.82 + 3.64, 2) == 7.28)
truth('2階の南北 1.82 ＋ 4.55 ＋ 0.91 ＝ 7.28', round(1.82 + 4.55 + 0.91, 2) == 7.28)
truth('2階の東の寸法線 1.82＋1.82＋2.73＋0.91 ＝ 7.28', round(1.82 + 1.82 + 2.73 + 0.91, 2) == 7.28)
truth('吹抜を忘れる 34.7802・ベランダまで 39.7488', round(5.46 * 6.37, 4) == 34.7802 and trunc2(5.46 * 7.28) == 39.74)
truth('押入を除く 6.6248 → 6.62', round(3.64 * 1.82, 4) == 6.6248 and trunc2(3.64 * 1.82) == 6.62)
truth('ロフトの幅 0.91 ＋ 3.64 ＝ 4.55', round(0.91 + 3.64, 2) == 4.55)
check('ロフトの誤答', '2階建です！')
check('四捨五入の誤答', '四捨五入して41.41平方メートルです！')
check('切り捨て', '41.405は41.40よ')
check('吹抜の誤答', '吹抜を忘れると 5.46 × 6.37 ＝ 34.7802 で34.78、ベランダまで入れると39.74になってしまうんですね')
check('押入の誤答', '3.64 × 1.82 ＝ 6.6248で6.62平方メートルですか？')
check('特殊階（階数）', '（不動産登記事務取扱手続準則第81条第4項）')
check('特殊階（床面積）', '（準則第82条第1号本文）')
check('1室の一部', '『1室の一部が天井の高さ1.5メートル未満であっても、その部分は、当該1室の面積に算入する』')
check('吹抜（82条8号）', '（準則第82条第8号）')
check('階段室（82条6号）', '（準則第82条第6号）')
check('断面図の高さ', '西の押入の外壁のところが0.80、押入とロフトの境が1.20、屋根のてっぺんが2.00、東の端が1.20です')
# 断面の屋根の勾配（図3）：外壁0.80、0.91で1.20、中央2.73で2.00
slope = 0.40 / 0.91
truth('屋根の勾配で中央が2.00', round(0.80 + slope * 2.73, 2) == 2.00)
truth('東の端（4.55）も1.20', round(2.00 - slope * (4.55 - 2.73), 2) == 1.20)

# ---- 構造・問1 ----
check('通し柱から木造', '平面図に通し柱の記号が並んでいるから、構造は木造と判断できるわ')
check('亜鉛メッキ鋼板との対比', '規則第114条の『亜鉛メッキ鋼板ぶき』……じゃなくて')
check('添付の根拠', '（不動産登記令別表12の項添付情報欄イ〜ニ）')
check('代理権限', '（同令第7条第1項第2号）')
check('登録免許税', '建物の表題登記はそこに載っていないので、納めなくていいんです')
check('登録免許税の根拠', '（登録免許税法別表第一の一（十三））')
check('申請義務', '（不動産登記法第47条第1項）')
check('申請の期限', '8月9日から数え始めて、1月後の応当日の9月9日の前日、9月8日に満了します')
truth('8月9日起算・1月後の応当日の前日は9月8日、8月8日から15日目が8月23日', (23 - 8) == 15)
check('引渡日は書かれていない', '引渡しの日は書かれていませんが、工事完了の8月8日より前ではありません')
check('職印', '（土地家屋調査士法施行規則第26条第1項）')
check('不動産番号', '不動産番号は、まだ登記されていない建物なので空欄')
check('問2の根拠', '準則第87条第1項です')
check('問2のわな（附帯設備）', '丸田電気さんと中山設備さんは附帯設備の工事をしただけで、建物の建築請負人じゃありません')
check('問2のわな（社員）', '現場責任者の建倉進さんも、会社の社員で、請負人は会社そのもの')
check('各階平面図の根拠', '（不動産登記規則第83条第1項）')
check('1階の位置の点線', '（準則第53条）')

# ---- 付属プロンプトの記入データ ----
for s_ in ['**登記の目的**：建物表題登記', '**添付書類**：建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書',
           '**申請人**：Ａ市Ｂ町二丁目３番地４　土野一郎', '**代理人**：Ａ市Ｃ町五丁目６番地７　家野二郎',
           '平成21年8月23日　申請　Ｄ地方法務局Ｂ出張所', '1段目「Ａ市Ｂ町二丁目３番地４」',
           '②構造「木造かわらぶき３階建」', '③床面積「1階　41｜40」「2階　33｜12」「3階　8｜28」',
           '登記原因及びその日付「平成21年8月8日新築」', '**表の下の枠**：土地家屋調査士　家野二郎',
           '**登録免許税**：欄がないので書かない', '3. 株式会社建倉工務店が作成した工事完了引渡証明書（同社の印鑑証明書付き）']:
    check('申請書の記入データ', s_, form, '申請書')
for s_ in ['①構造の欄', '②床面積の欄', '②構造「木造かわら・合金メッキ鋼板ぶき３階建」'.replace('②', ''),
           '「1階　41｜41」', '「3階　6｜62」', '「木造かわらぶき３階建」', '「1階　41｜40」「2階　33｜12」「3階　8｜28」',
           '1枚に複数の欄の誤りを詰め込まない', '上から「①誤答」「②添削（赤ペン）」「③正解」の3コマ', '高さが横幅（1200px）より大きい縦長か',
           '画像の中に「図1」などの図番は入れない', 'zu/H21_dai22mon_toukishinseisho_machigai_kouzou.png',
           'zu/H21_dai22mon_toukishinseisho_machigai_yukamenseki.png']:
    check('添削プロンプト', s_, fix, '添削')
absent('旧版の1枚に詰め込む誤答', '②構造：「木造かわら・合金メッキ鋼板ぶき２階建」', fix, '添削')
check('罫線の比（答案用紙から測った）', '罫線の比は試験の答案用紙（`public/kijutsu/H21-tatemono/a1.webp`、990×1400px）から測った', form, '申請書')

# ---- 解説図プロンプトの頂点座標（面積が求積表と一致すること） ----
SHAPES = [('1階', [(0, 0), (6.37, 0), (6.37, 1.82), (5.46, 1.82), (5.46, 7.28), (0, 7.28)], 41.405),
          ('2階', [(0, 0), (4.55, 0), (4.55, 1.82), (5.46, 1.82), (5.46, 6.37), (0, 6.37)], 33.124),
          ('3階（ロフト）', [(0, 0), (4.55, 0), (4.55, 1.82), (0, 1.82)], 8.281),
          ('北の帯', [(0, 0), (6.37, 0), (6.37, 1.82), (0, 1.82)], 11.5934),
          ('南の本体', [(0, 1.82), (5.46, 1.82), (5.46, 7.28), (0, 7.28)], 29.8116),
          ('3番4', [(0, 0), (10.0, 0), (10.0, 13.1), (0, 13.1)], 131.0)]
for label, pts, want in SHAPES:
    truth(f'{label} の面積 {want}', round(poly_area(pts), 4) == want)
    if label != '3番4':
        check(label + ' 頂点座標', ' → '.join(f'({a:g}, {b:g})' for a, b in pts + [pts[0]]), fig, '解説図')
check('3番4 頂点座標', '(0, 0) → (10.00, 0) → (10.00, 13.10) → (0, 13.10)', fig, '解説図')
check('標準セットを作る理由', '執筆プロンプトの「想定する画像の標準セット」（敷地の辺長確認図・建物図面の完成形・誤り比較図・各階の求積図）はすべて作る', fig, '解説図')
check('建物図面の距離', '距離：北3.10（道路境界線から北の外壁まで）、西1.00（北西の角の近くと南西の角の近くの2か所）', fig, '解説図')
check('壁の中心線の位置', '北の壁の中心は道路境界線から 1.10 ＋ 2.00 ＋ 0.09 ＝ 3.19', fig, '解説図')

# ---- 誤記・禁止語 ----
for bad in ['PDF', '右上', '左下', '右側', '左側', '✕', '✓', '⊠', '名変', '創設的登記', '41.41平方メートル。', '登録免許税は1,000円',
            'ガルバリウム鋼板ぶき']:
    absent('誤記・混入', bad)
for bad in ['✕', '✓']:
    absent('記号', bad, fig, '解説図')
    absent('記号', bad, fix, '添削')

# ---- 注の書き分け：問題文の注は「問題文の注N」。調査結果は「調査結果N」 ----
bare = [m.start() for m in re.finditer(r'注[0-9]', text) if not text[:m.start()].endswith('問題文の')]
truth(f'注の書き分け（「問題文の」のない「注N」 {len(bare)}か所）', not bare)
for s_ in ['問題文の注1', '問題文の注2', '問題文の注5', '問題文の注6', '調査結果11', '調査結果7', '〔ロフト平面図〕の下']:
    check('注の書き分け', s_)
check('番号のついたもの3種類', '番号のついたものが3種類あるから仕分けなさい')
absent('3系統', '3系統')

# ---- 条文（note-articles/laws/ の原典で確認したもの） ----
for s_ in ['（不動産登記規則第115条）', '（不動産登記規則第82条第1項）', '（不動産登記規則第82条第2項）', '（不動産登記規則第114条）',
           '（準則第82条第1号本文）', '（準則第81条第2項）']:
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
prefix = '# 【土地家屋調査士受験生向け】平成21年度問題22（建物）〜'
sub = title[len(prefix):-1]
truth(f'タイトル形式（見出し{len(sub)}文字）: {title}', title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成21年度問題22（建物）', thumb, '見出し画像')
for n_ in ['問1', '問2', '問3']:
    check('設問の網羅', n_)

# ---- 画像：画像挿入マーカー24か所と zu/ のPNGの対応（2026-10-26：記事の本文に対して図が足りているかの見直し） ----
from PIL import Image  # noqa: E402
ZU = os.path.join(HERE, 'zu')
markers = [l for l in lines if l.startswith('> 【画像挿入】')]
PNGS = [('H21_dai22mon_zu01_jikeiretsu', '日付を並べた時系列図'),
        ('H21_dai22mon_zu02_chuu_shiwake', '番号のついたものを3種類に仕分けた図'),
        ('H21_dai22mon_zu03_tooshibashira', '構成材料が書かれていないことの判断図'),
        ('H21_dai22mon_zu04_shikichi_kakunin', '3番4の敷地の形（作図チェック用）'),
        ('H21_dai22mon_zu05_koutai_sen', '道路後退線は筆界ではないことを示す図'),
        ('H21_dai22mon_zu06_shozai_kakunin', '建物が3番4の中に収まるかの確認図（所在の確認）'),
        ('H21_dai22mon_zu07_zumen_kisai', '建物図面に書くもの・書かないものを2つの枠に分けた図'),
        ('H21_dai22mon_zu08_tatemono_zumen', '建物図面の完成形（縮尺500分の1）'),
        ('H21_dai22mon_zu09_loft_ayamari_hikaku', 'ロフトの断面の誤り比較図'),
        ('H21_dai22mon_zu10_1kai_kyuuseki', '1階の求積図'),
        ('H21_dai22mon_zu11_2kai_irenai', '2階の床面積に入れるもの・入れないものの図'),
        ('H21_dai22mon_zu12_2kai_kyuuseki', '2階の求積図'),
        ('H21_dai22mon_zu13_3kai_kyuuseki', '3階（ロフト）の求積図'),
        ('H21_dai22mon_zu14_yane_wariai', '屋根の種類ごとの割合の図'),
        ('H21_dai22mon_toukishinseisho_machigai_kouzou', '構造の欄の添削画像'),
        ('H21_dai22mon_zu15_tenpu_shorui', '添付書類の要否の図'),
        ('H21_dai22mon_zu16_touroku_menkyozei', '登録免許税がかかる表示に関する登記とかからない登記'),
        ('H21_dai22mon_toukishinseisho_machigai_yukamenseki', '床面積の欄の添削画像'),
        ('H21_dai22mon_zu17_kakuran', '答案用紙で「書く欄」と「空ける欄」を色分けした図'),
        ('H21_dai22mon_toukishinseisho_kansei', '問1の完成した登記申請書'),
        ('H21_dai22mon_zu18_shoyuuken_shoumei', '問2：所有権を証する書面を、事実に当てはめて選ぶ図'),
        ('H21_dai22mon_toukishinseisho_kansei_toi2', '問2の解答欄の完成形'),
        ('H21_dai22mon_zu19_kakai_heimenzu', '建物図面と各階平面図の完成形（答案用紙（その2）の問3の欄）'),
        ('H21_dai22mon_zu20_toku_junban', '本番で解く順番の図')]
truth(f'画像挿入マーカーの数 {len(markers)}（解説図20・添削2・完成形2）', len(markers) == len(PNGS) == 24)
for (name, key), m in zip(PNGS, markers):
    path = os.path.join(ZU, name + '.png')
    ok = os.path.exists(path) and key in m
    if ok:
        w, h = Image.open(path).size
        if name.endswith('toi2'):
            ok = w == 1200
        elif 'toukishinseisho' in name:
            ok = w == 1200 and h > w
        elif 'zu08' in name or 'zu19' in name:
            ok = w >= 2000 and h >= 1000        # 答案用紙の寸法で描く
        else:
            ok = w >= 1600 and h >= 800
    truth(f'PNG（マーカー順） : {name}', ok)
    check('生成済みファイル名', name.replace('H21_dai22mon_', ''), fig if 'zu' in name.split('toukishinseisho')[0] else (fix if 'machigai' in name else form),
          '付属プロンプト')

# ---- わな → 図の対応（記事のまとめの1項目1わなと、図が該当する会話の直後にあること） ----
TRAPS = [('ロフトを数えない', 'ロフトは名前で判断せず', 'H21_dai22mon_zu09_loft_ayamari_hikaku', '高さで判断させるため'),
         ('構成材料', '構成材料が書かれていなければ', 'H21_dai22mon_zu03_tooshibashira', '通し柱の記号が並んでいるから'),
         ('四捨五入', '1階の41.405は四捨五入せず', 'H21_dai22mon_zu10_1kai_kyuuseki', '5がちょうど出る年は'),
         ('吹抜とベランダ', '2階は吹抜とベランダを床面積に入れず', 'H21_dai22mon_zu11_2kai_irenai', '準則第82条第6号'),
         ('押入を除く', '3階は押入も含めて', 'H21_dai22mon_zu13_3kai_kyuuseki', '4.55 × 1.82 が3階の床面積'),
         ('屋根30％未満', '屋根が2種類でも', 'H21_dai22mon_zu14_yane_wariai', '概算で約4％'),
         ('後退線', '建物図面の北は、道路後退線ではなく', 'H21_dai22mon_zu05_koutai_sen', '道路は道路境界線で描きます'),
         ('所在', '建物の所在は、外壁と筆界の間', 'H21_dai22mon_zu06_shozai_kakunin', '3番4の中に収まります'),
         ('書かないもの', '建物図面に敷地の辺長・建物の辺長・道路後退線は書かない', 'H21_dai22mon_zu07_zumen_kisai', '家屋番号は登記所が付けるので書きません'),
         ('添付書類', '添付書類に登記識別情報と印鑑証明書は入れない', 'H21_dai22mon_zu15_tenpu_shorui', '令別表12の項の添付情報に載っていない'),
         ('登録免許税', '登録免許税の欄はない', 'H21_dai22mon_zu16_touroku_menkyozei', '納めなくていいんです'),
         ('原因の日付・期限', '原因の日付は、依頼や申請の日ではなく', 'H21_dai22mon_zu01_jikeiretsu', '期限内です'),
         ('所有権の証明', '所有権を証する書面は、建築請負人', 'H21_dai22mon_zu18_shoyuuken_shoumei', 'まだ使えません')]
body_lines = lines
marker_pos = {}
for (name, key), m in zip(PNGS, markers):
    marker_pos[name] = body_lines.index(m)
summary_i = next(i for i, l in enumerate(lines) if l.startswith('「今日のまとめよ') or l.startswith('「今日のまとめよ。'.replace('「', '')))
bullets = [l for l in lines[summary_i:] if l.startswith('- ')]
truth(f'まとめは1項目1わな（箇条書き {len(bullets)}項目＝わな {len(TRAPS)}件より多い）', len(bullets) >= len(TRAPS))
for label, bullet_key, fname, decisive in TRAPS:
    in_summary = any(bullet_key in b for b in bullets)
    pos = marker_pos[fname]
    prev_line = next(l for l in reversed(lines[:pos]) if l.strip())
    truth(f'わな「{label}」：まとめの項目あり／図{fname[-18:]}が会話の直後（直前の行に「{decisive}」）', in_summary and decisive in prev_line)
truth('同じ図が2か所に置かれていない', len({n for n, _ in PNGS}) == len(PNGS))


def html_has(name, *needles, bad=()):
    h = open(os.path.join(ZU, name + '.html'), encoding='utf-8').read()
    for n in needles:
        truth(f'{name}.html : {n}', n in h)
    for n in bad:
        truth(f'{name}.html に無い : {n}', n not in h)


html_has('H21_dai22mon_toukishinseisho_kansei', '建物表題登記', '建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書',
         '平成21年8月23日', 'Ｄ地方法務局Ｂ出張所', 'Ａ市Ｂ町二丁目３番地４　土野一郎', 'Ａ市Ｃ町五丁目６番地７　家野二郎',
         '（連絡先電話番号', '不動産番号', '建物の表示', '（記載不要）', '主たる建物<br>又は附属建物', '居宅',
         '木造かわらぶき３階建', '1階　41', '>40<', '2階　33', '>12<', '3階　8', '>28<', '平成21年8月8日新築',
         '土地家屋調査士　家野二郎', '職印', '問1（登記申請書）', '<col style="width:6.2%">', '<col style="width:23.9%">',
         bad=('登録免許税', '平成30年', '主である建物', '>41<', '会社法人等番号', '（略）', '合金メッキ鋼板', 'style="height:'))
html_has('H21_dai22mon_toukishinseisho_kansei_toi2', '所有権を有することを証する情報として添付する具体的書面（情報）の例',
         '建築基準法第6条の確認があったことを証する書面（確認済証）', '建築基準法第7条の検査があったことを証する書面（検査済証）',
         '株式会社建倉工務店が作成した工事完了引渡証明書（同社の印鑑証明書付き）', '問2', bad=('丸田電気', '中山設備', '建倉進'))
html_has('H21_dai22mon_toukishinseisho_machigai_kouzou', '①誤答', '②添削（赤ペン）', '③正解', '木造かわら・合金メッキ鋼板ぶき３階建',
         '・合金メッキ鋼板</span>', '30％未満の種類の屋根は表示しない', '木造かわらぶき３階建', bad=('41.405は切り捨てて',))
html_has('H21_dai22mon_toukishinseisho_machigai_yukamenseki', '①誤答', '②添削（赤ペン）', '③正解', '3階　6', '>62<',
         '41.405は切り捨てて41.40', '押入を除く6.62ではない', '3階　8', bad=('30％未満の種類の屋根は表示しない',))
drw = open(os.path.join(ZU, 'draw_H21_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
# 画像の中のタイトルに図番（「図1」など）が入っていない（2026-10-07のルール）
title_calls = re.findall(r"(?:new_figure|fixed_fig|sheet_figure|suptitle)\(\s*'([^']*)'", drw)
truth(f'画像のタイトル {len(title_calls)}件に図番なし', len(title_calls) == 20 and not any(re.search(r'図[0-9０-９]', t) for t in title_calls))
fits = []
for m in re.finditer(r'\bfit\(', drw):
    depth, j = 0, m.end() - 1
    for j in range(m.end() - 1, len(drw)):
        depth += {'(': 1, ')': -1}.get(drw[j], 0)
        if depth == 0:
            break
    fits.append(drw[m.start():j + 1])
fits = [f for f in fits if not f.startswith('fit(ax, pts')]
truth(f'作図の fit はすべて pad_aspect=True（{len(fits)}か所）', fits and all('pad_aspect=True' in f for f in fits))
for s_ in ['== 41.405', '== 41.40', '== 41.41', '== 33.124', '== 8.281', '== 6.6248', '== 34.7802', '== 131.00', '== 2.45', '== 2.54',
           '== 2.00', '== 1.5925', '== 1.6562']:
    check('作図スクリプトの assert', s_, drw, '作図')
for s_ in ['PX = 0.3', 'S_X0, S_Y0 = 252.0, 204.0', '1m ＝ 2mm', '1m ＝ 4mm', 'FR_L, FR_T = pxm(80.5, 144.5)']:
    check('答案用紙の寸法と縮尺（実際の大きさ）', s_, drw, '作図')
check('制作スクリプトのブラウザの探し方', "chromium-*/chrome-linux*/chrome", open(os.path.join(ZU, 'make_H21_dai22mon_shinseisho_gazou.py'), encoding='utf-8').read(), '作図')

# ---- 答案用紙の原本（touan_youshi/）を置いてある ----
for n_ in ['H21_dai22mon_touan_youshi_p1.png', 'H21_dai22mon_touan_youshi_p2.png']:
    truth(f'答案用紙の原本 {n_}', os.path.exists(os.path.join(HERE, 'touan_youshi', n_)))

# ---- 図面の完成形は答案用紙（その2）の欄の枠の中（H27/Q22のルール） ----
for s_ in ["'家 屋 番 号'", "'建物の所在'", "'A市B町二丁目3番地4'", "'申 請 人'", "'土野一郎'", "'作 成 者'", "'土地家屋調査士　家野二郎'", "'職印'",
           "'（平成21年8月23日作成）'", "'500'", "'250'", "'建　物　図　面'", "'各　階　平　面　図'"]:
    check('図面の完成形の答案用紙の欄', s_, drw, '作図')
check('建物図面の欄の枠（プロンプト）', '図8・図19が答案用紙（その2）の欄の枠', fig, '解説図')
check('建物図面の欄の枠（マーカー）', '建物図面の完成形（縮尺500分の1）。答案用紙（その2）の右半分の欄の枠')
check('各階平面図の欄の枠（マーカー）', '建物図面と各階平面図の完成形（答案用紙（その2）の問3の欄）')
check('各階平面図に方位を書かない', '各階平面図に方位は書かない')
check('記事の所在', '『建物の所在』は『A市B町二丁目3番地4』')
check('記事の申請人欄', '『土野一郎』と書きます（不動産登記規則第74条第2項）')
truth('画像の中に「第○欄」と書かない（問3など答案用紙の印刷どおり）', '第3欄' not in open(os.path.join(ZU, 'H21_dai22mon_toukishinseisho_kansei.html'), encoding='utf-8').read())

print('NG件数:', ng)
