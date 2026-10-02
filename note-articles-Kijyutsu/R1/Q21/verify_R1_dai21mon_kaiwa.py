"""令和元年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集の解答例ページで照合。下の AGAROOT に転記）と一致することも確認する。
実行: python3 note-articles-Kijyutsu/R1/Q21/verify_R1_dai21mon_kaiwa.py"""
import cmath
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_R1_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_R1_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R1_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R1_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R1_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_R1_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（問題文の〔A市基準点成果表〕と〔測量によって得られた座標値〕） ----
T1, T2 = P(285.36, 297.00), P(285.50, 312.00)
A, B, C = P(300.00, 300.00), P(302.00, 318.00), P(289.22, 318.00)
E, F, H = P(301.18, 310.62), P(290.00, 300.00), P(290.30, 318.00)
judge('E点はAB上（△ABEの倍面積のiの係数が0）', abs(((B - A).conjugate() * (E - A)).imag) < 1e-9)

# ---- 問1 D点（T1から放射。観測角は時計回り＝足す） ----
check('arg(T2−T1)', to_dms(cmath.phase(T2 - T1)))
check('足した方向角', '399°29′39.92″')
check('360°を引いた方向角', '39°29′39.92″')
Dx = radial(T1, T2, 4.72, dms(310, 1, 45))
check('D 表示', '表示：' + disp(Dx))
D = r2(Dx)
check('D 答え', '**▶ D点（289.00, 300.00）**')
Dw = r2(radial(T1, T2, 4.72, -dms(310, 1, 45)))
check('反時計回りの誤りのD', f'（{Dw.real:.2f}, {Dw.imag:.2f}）')
check('誤りのDとT1の差', f'{T1.real - Dw.real:.2f}m')
judge('誤りのDはT1より南', Dw.real < T1.real)
judge('DはFの真南1.00m', D == F - 1)
check('CD', f'DからCまでは{abs(C - D):.2f}')

# ---- 問1 G点（EからFHへの垂線の足） ----
w = (E - F) / (H - F)
check('w 表示', '表示：' + disp(w))
Gx = F + (H - F) * (w + w.conjugate()) / 2
check('G 表示', '表示：' + disp(Gx))
G = r2(Gx)
check('G 答え', '**▶ G点（290.18, 310.80）**')
check('H−F 表示（軸に平行でない）', '表示：' + disp(H - F))
judge('FHは真東向きではない（実部0.30）', abs((H - F).real - 0.30) < 1e-9)
num = (E - F).conjugate() * (H - F) * 1j
den = (H - F).conjugate() * (H - F) * 1j
check('別解の分子 表示', '表示：' + disp(num))
check('別解の分母 表示', f'表示：{den.imag:.2f}i')
judge('別解の分母は純虚数', abs(den.real) < 1e-9)
check('別解のt', f'194.514 ÷ 324.09 ＝ {fmt_num(194.514 / 324.09)}')
judge('別解のtはwの実部と同じ', abs(194.514 / 324.09 - w.real) < 1e-12)
check('別解のG 表示', '表示：' + disp(F + (H - F) * 194.514 / 324.09))
check('直角の検算 表示', '表示：' + disp((H - F).conjugate() * (G - E)))
Gw = P(290.18, 310.62)
judge('真南に下ろした誤りの点もFH上（丸めるとX＝290.18）', f'{(F + (H - F) * (Gw.imag - F.imag) / (H.imag - F.imag)).real:.2f}' == '290.18')
check('誤りのG', '（290.18, 310.62）')
check('誤りのGの直角の検算（実部）', f'実部は{fmt_num(((H - F).conjugate() * (Gw - E)).real, 2)}')
judge('誤りのGは正しいGより0.18m西', f'{G.imag - Gw.imag:.2f}' == '0.18' and Gw.imag < G.imag)
check('誤りのGの0.18', '0.18m東')
check('誤りのGの甲区画', f'甲区画は{chiseki(area([A, E, Gw, F])):.2f}㎡')
check('誤りのGの丙区画', f'丙区画は{chiseki(area([B, H, Gw, E])):.2f}㎡')

# ---- 問2 筆界特定 ----
for s in ['- **（1）対象土地の地番**：6番、5番', '- **（2）関係土地の地番**：2番32、3番3、100番',
          '- **（3）関係人の氏名又は名称**：北冬子、山川一郎、東春男、東春子、西秋男、A市',
          '不動産登記法第123条第3号', '同条第4号', '同法第133条第1項', '第133条第1項第1号']:
    check('問2', s)
check('問2の誤答（分筆後の地番）', '5番と6番1です！')
check('問2の誤答（関係土地の取り過ぎ）', '1番25、2番32、3番2、3番3、4番1、4番2、7番、100番！')
check('問2の誤答（申請人を関係人に）', '6番の北冬男さんと北冬子さん')

# ---- 問3 面積 ----
for name, pts, want_im, want_area, want_ch in [
        ('本件土地', [A, B, C, D, F], '428.04', '214.02', '214.02'),
        ('甲区画', [A, E, G, F], '225.0324', '112.5162', '112.51'),
        ('乙区画', [C, D, F, G, H], '37.44', '18.72', '18.72'),
        ('丙区画', [B, H, G, E], '165.5676', '82.7838', '82.78')]:
    s = double_area_sum(pts)
    judge(f'{name} 倍面積のiの係数 {fmt_num(abs(s.imag))}', fmt_num(abs(s.imag)) == want_im)
    check(f'{name} 表示', f'表示：（実部）− {want_im}i')
    judge(f'{name} 面積 {fmt_num(area(pts))}', fmt_num(area(pts)) == want_area)
    judge(f'{name} 地積 {chiseki(area(pts)):.2f}', f'{chiseki(area(pts)):.2f}' == want_ch)
dk = (A - G).conjugate() * (E - F)
dh = (E - H).conjugate() * (B - G)
check('甲区画の対角線 表示', '表示：' + disp(dk))
check('丙区画の対角線 表示', '表示：' + disp(dh))
judge('対角線のiの係数が4点の式と一致', fmt_num(abs(dk.imag)) == '225.0324' and fmt_num(abs(dh.imag)) == '165.5676')
tot = sum(chiseki(area(p)) for p in ([A, E, G, F], [C, D, F, G, H], [B, H, G, E]))
check('3筆の合計', f'112.51 ＋ 18.72 ＋ 82.78 ＝ {tot:.2f}㎡')
check('公差の差（分筆後の合計）', f'{tot:.2f} − 212.70 ＝ {tot - 212.70:.2f}㎡')
check('公差の差（本件土地全体）', f'差は{chiseki(area([A, B, C, D, F])) - 212.70:.2f}㎡')
judge('差1.31は甲2の1.28を超え、甲3の2.57の範囲内（誤答）', 1.28 < tot - 212.70 < 2.57)
check('超えている量', f'たった{tot - 212.70 - 1.28:.2f}㎡')
for s in ['不動産登記事務取扱手続準則第72条第1項', '不動産登記規則第10条第2項第1号', '同条第4項第1号', '不動産登記規則第35条第7号',
          '準則第68条', '同条第3号', '準則第67条第1項第4号', '登録免許税法別表第一の一の（十三）', '不動産登記令別表6の項・8の項']:
    check('条文', s)

# ---- 問3 申請書 ----
for s in ['- **登記の目的**：土地地積更正・分筆登記', '- **添付書類**：地積測量図　代理権限証書',
          '- **登録免許税**：金3,000円（分筆後の土地1個につき1,000円 × 3個）', '- **申請人**：A市B町一丁目5番1号　山川一郎',
          '- **所在**：A市B町一丁目', '①5番、②宅地、③212.70（登記記録の地積）、登記原因は空欄',
          '①（イ）5番1、②空欄、③112.51、登記原因「③錯誤　①③5番1ないし5番3に分筆」',
          '①（ロ）5番2、②宅地、③18.72、登記原因「5番から分筆」', '①（ハ）5番3、②宅地、③82.78、登記原因「5番から分筆」']:
    check('問3', s)
check('誤答（土地分筆登記のみ）', '土地分筆登記です！')
check('誤答（甲3）', '甲3が2.57㎡')
check('誤答（一部地目変更）', '『平成25年5月1日一部地目変更』')
check('誤答（公衆用道路）', '公衆用道路にしたくなります')
check('誤答（（イ）の地番を空ける）', '原因は『③5番2、5番3を分筆』')
check('誤答（登録免許税4,000円）', '4,000円ですか？')

# ---- 問4 地積測量図 ----
SIDES = {'AE': (A, E), 'EB': (E, B), 'BH': (B, H), 'HC': (H, C), 'CD': (C, D), 'DF': (D, F), 'FA': (F, A),
         'EG（分筆線）': (E, G), 'FG（分筆線）': (F, G), 'GH（分筆線）': (G, H)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
check('EBの四捨五入', f'EBは計算すると{fmt_num(abs(B - E))[:-1]}')
check('AEの四捨五入', f'AEは{fmt_num(abs(E - A))[:-1]}')
check('CDの四捨五入', f'CDは{fmt_num(abs(D - C))[:-1]}')
check('答案用紙の大きさ', f'横約{round((B.imag - A.imag) * 4):d}mm・縦約{round((B.real - D.real) * 4):d}mm')
check('地番欄', '地番欄は『5番1、5番2、5番3』')
check('T1・T2まで入れた作図範囲', f'縦約{round((B.real - T1.real) * 4):d}mm・横約{round((B.imag - T1.imag) * 4):d}mm')
check('単位の表示', '（単位：ｍ）')

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページ〈354・355・357ページ〉から転記）と一致するか ----
AGAROOT = ['（289.00, 300.00）', '（290.18, 310.80）', '6番、5番', '2番32、3番3、100番', '北冬子、山川一郎、東春男、東春子、西秋男、A市',
           '土地地積更正・分筆登記', '地積測量図　代理権限証書', '金3,000円', 'A市B町一丁目5番1号　山川一郎', 'A市B町一丁目',
           '③212.70', '（イ）5番1', '③112.51', '③錯誤　①③5番1ないし5番3に分筆', '（ロ）5番2', '③18.72', '5番から分筆',
           '（ハ）5番3', '③82.78', '：10.69', '：7.43', '：11.70', '：1.08', '：18.00', '：1.00', '：10.00', '：11.00', '：10.80',
           '：7.20', 'A・Bは石杭、C・D・F・G・Hはコンクリート杭、Eは金属標', '『5番1、5番2、5番3』']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d+：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（13枚）', n_fig == 13)
for i in range(1, 14):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'R1_dai21mon_zu{i:02d}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\(|seiri_zu\()'図(\d+)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から13まで（{sorted(nums)}）', sorted(nums) == list(range(1, 14)))
for s in ['（289.00, 300.00）', '（290.18, 310.80）', '（281.77, 300.07）', '（290.18, 310.62）', '89°27′54.92″', '310°01′45″',
          '399°29′39.92″', '39°29′39.92″', '0.6001… − 0.6111…i', '112.51', '18.72', '82.78', '214.01', '214.02', '111.51',
          '83.76', '1.31', '1.28', '2.57', '7.4254', '10.6853', '18.0013', '横約72mm・縦約52mm', '横約84mm・縦約67mm',
          '194.514 ÷ 324.09', '0.30 ＋ 18.00i', '225.0324', '165.5676', '−4.9084 ＋ 225.0324i', '75.4656 ＋ 165.5676i']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['ここが問1のG点で効いてくるから、覚えておきなさい', '求めた点が素図の位置に出るかどうかは、必ず見るのよ',
          'わずか0.18mのずれでも、地積はごまかせないのよ', '（2）は2番32、3番3、100番', '四捨五入して112.52や82.79にしないこと',
          '一の申請情報で申請できる（不動産登記規則第35条第7号）', 'だから登記の目的は『土地地積更正・分筆登記』よ',
          'EGはFHに直角よ', '印の付いた注だけを答案を書くときに見直します', '自分の手になじむほうを1つ決めておきなさい',
          '四角形は対角線、それ以外は順に回る、と使い分けなさい', '最後に落ち着いて関係人を数えます']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['令和元年10月18日　申請　Ａ地方法務局', '土地地積更正・分筆登記', '地積測量図　代理権限証書', '金3,000円',
          'Ａ市Ｂ町一丁目５番１号　山川一郎', 'Ａ市Ｂ町一丁目', '③「212｜70」', '①「（イ）5番１」', '③「112｜51」',
          '「③錯誤」「①③5番１ないし5番３に分筆」', '①「（ロ）5番２」', '③「18｜72」', '①「（ハ）5番３」', '③「82｜78」',
          '登記原因「5番から分筆」', '登記の目的 → 添付書類 → 登録免許税 → 申請人 → 代理人 → 申請日・法務局 → 土地の表示']:
    check('登記申請書', s, form, '登記申請書')
for s in ['土地分筆登記', '土地地積更正・分筆登記', '③5番２、5番３を分筆', '5番１', '「③錯誤」「①③5番１ないし5番３に分筆」',
          '差1.31㎡＞甲2の公差1.28㎡。地積更正も一の申請情報で！', '支号のない5番を分筆すると5番１になる（①）。③錯誤も同じ行に',
          '令和元年10月18日　申請　Ａ地方法務局', '令和元年度 第21問｜地積更正と分筆は一の申請情報で、（イ）は5番１に①③']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', 'それから登記の目的も、さっき直したとおりよ')
check('添削の挿入位置の文言（プロンプト側）', 'それから登記の目的も、さっき直したとおりよ', fix, '添削')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['R1_dai21mon_toukishinseisho_kansei', 'R1_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w_, h_ = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w_}×{h_}px）', h_ > w_)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'R1_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'R1_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['令和元年10月18日　申請　Ａ地方法務局', '土地地積更正・分筆登記', '地積測量図　代理権限証書', 'Ａ市Ｂ町一丁目５番１号　山川一郎',
          '金3,000円', 'Ａ市Ｂ町一丁目', '>5番<', '（イ）5番１', '（ロ）5番２', '（ハ）5番３', '③錯誤<br>①③5番１ないし5番３に分筆',
          '5番から分筆', '>212<', '>70<', '>112<', '>51<', '>18<', '>72<', '>82<', '>78<', '（略）',
          '令和元年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
# 答案用紙の順序（登録免許税・申請人が申請日より上）
order = [html_k.index(k) for k in ['登記の目的', '添　付　書　類', '登録免許税', '申　　請　　人', '代　　理　　人', '令和元年10月18日', '所　在']]
judge('完成形の画像の欄の順序が答案用紙どおり', order == sorted(order))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '土地分筆登記', '③5番２、5番３を分筆', '>5番１<',
          '差1.31㎡＞甲2の公差1.28㎡。地積更正も一の申請情報で！', '支号のない5番を分筆すると5番１になる（①）。③錯誤も同じ行に',
          '令和元年度 第21問｜地積更正と分筆は一の申請情報で、（イ）は5番１に①③']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 注の呼び分け（問題文の注・調査図素図の注・観測値の表の注） ----
for s_ in ['問題文の注3', '問題文の注4', '問題文の注5', '問題文の注6', '観測値の表の注1', '調査図素図の注']:
    check('注の呼び分け', s_)
for s_ in ['（注5）', '（注6）', '」注4', '。注3']:
    absent('どの注か分からない書き方', s_)
for s_ in ['（注5）', '（注6）']:
    absent('どの注か分からない書き方（解説図プロンプトの差し替えデータ）', s_, fig[fig.index('## 差し替えデータ（令和元年度'):], '解説図')
    absent('どの注か分からない書き方（作図）', s_, draw, '作図')
# ---- 時間配分が具体的か ----
for s_ in ['いちばん時間を食うのはG点と、そのあとの3筆の面積よ', 'G点がなくても書ける', '面積を出して公差と比べるまで書いてはだめ',
           '① 問題文を読んで注を仕分ける']:
    check('具体的な時間配分', s_)

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '石くい', 'へい（']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('専門用語は問題文どおりの漢字', '石杭')
check('専門用語は問題文どおりの漢字', 'ブロック塀')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
same = []
# 同じ話者のセリフが、空行・画像挿入マーカー・セリフの続きの段落だけをはさんで続いていないか（2026-10-02、マーカーを読み飛ばす形に直した）。
# 箇条書き・計算（式・電卓操作・表示・答えの行・コードブロック）・区切り線・見出しをはさむものは数えない。
spk_ = [(k_, l_.rstrip()) for k_, l_ in enumerate(lines) if l_.rstrip() in ('**トリ先生**', '**藍子**')]
for (i_, a_), (j_, b_) in zip(spk_, spk_[1:]):
    if a_ != b_:
        continue
    mid_ = [l_ for l_ in lines[i_ + 2:j_] if l_.strip()]
    if not any(l_.startswith(('- ', '```', '表示：', '式（', '電卓操作', '**▶', '---', '#')) or re.match(r'^\d+\. ', l_)
               for l_ in mid_):
        same.append(j_ + 1)
judge(f'同じ話者のセリフの連続: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図13＋第1欄・第2欄の完成形2＋添削1＋申請書の完成形1）', n_marker == 17)
pngs = [f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png')]
judge(f'画像挿入マーカーの数だけPNGが zu/ にある（{len(pngs)}枚）', len(pngs) == n_marker)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】令和元年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '令和元年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')

PNGS = [('R1_dai21mon_zu01_chuu_shiwake', '注の仕分けの図', 'fig'),
        ('R1_dai21mon_zu02_zentaizu', '全体図', 'fig'),
        ('R1_dai21mon_zu03_D_housha', 'D点を求める図', 'fig'),
        ('R1_dai21mon_dai1ran_kansei', '問1の完成形', 'wide'),
        ('R1_dai21mon_zu04_G_suisen', 'G点の求め方の図', 'fig'),
        ('R1_dai21mon_zu05_G_betsukai', 'G点の別解の図', 'fig'),
        ('R1_dai21mon_zu06_taishou_kankei_tochi', '問2（1）（2）の図', 'fig'),
        ('R1_dai21mon_dai2ran_kansei', '問2の完成形', 'wide'),
        ('R1_dai21mon_zu07_kankeinin', '関係人の整理図', 'fig'),
        ('R1_dai21mon_zu08_bunpitsu_chiseki', '分筆後の区画と地積の図', 'fig'),
        ('R1_dai21mon_zu09_taikakusen', '対角線で出す別解の図', 'fig'),
        ('R1_dai21mon_zu10_kousa', '公差の判定図', 'fig'),
        ('R1_dai21mon_zu11_chimoku', '地目の判断の図', 'fig'),
        ('R1_dai21mon_toukishinseisho_machigai', '誤答→添削→正解', 'tall'),
        ('R1_dai21mon_toukishinseisho_kansei', '登記申請書（問3）の完成形', 'tall'),
        ('R1_dai21mon_zu12_chiseki_sokuryouzu', '地積測量図（5番1・5番2・5番3）の完成見本', 'fig'),
        ('R1_dai21mon_zu13_toku_junban', '解く順番と時間配分の図', 'fig')]
# ---- 画像（2026-10-02追加）：記事の画像挿入マーカーと zu/ のPNGが、記事の順に対応しているか ----
# 解説図の番号を記事の挿入順に振り直し、申請書でない解答欄（第1欄・第2欄）の完成形を足した。
from PIL import Image  # noqa: E402
ZU = os.path.join(HERE, 'zu')
markers = [l for l in text.splitlines() if l.startswith('> 【画像挿入】')]
judge(f'画像挿入マーカーの数とPNGの数 : {len(markers)}／{len(PNGS)}', len(markers) == len(PNGS))
for (name_, key_, kind_), m_ in zip(PNGS, markers):
    path_ = os.path.join(ZU, name_ + '.png')
    ok_ = os.path.exists(path_) and key_ in m_
    if ok_:
        w_, h_ = Image.open(path_).size
        ok_ = {'tall': w_ == 1200 and h_ > w_, 'wide': w_ == 1200 and h_ < w_, 'fig': w_ == 1600}[kind_]
    judge(f'PNG（マーカー順・大きさ） : {name_}（{key_}）', ok_)
    src_ = fig if '_zu' in name_ else (fix if 'machigai' in name_ else form)
    judge(f'プロンプトにファイル名 : zu/{name_}.png', f'zu/{name_}.png' in src_)
extra_ = sorted(set(f_[:-4] for f_ in os.listdir(ZU) if f_.endswith('.png')) - {n_ for n_, _, _ in PNGS})
judge(f'zu/ に記事で使わないPNGがない {extra_}', not extra_)
fig_order = [int(x_) for x_ in re.findall(r'^- \*\*図(\d+)：', fig, re.M)]
judge(f'解説図プロンプトの図の一覧が番号順（{fig_order}）', fig_order == sorted(fig_order))
zu_order = [int(n_.split('_zu')[1][:2]) for n_, _, _ in PNGS if '_zu' in n_]
judge(f'解説図の番号が記事の挿入順（{zu_order}）', zu_order == list(range(1, len(zu_order) + 1)))
lines_ = text.splitlines()


def after_(key, prev):
    """マーカー（key を含む）の直前の空行でない行に prev があるか（その問の答えの直後に置いたか）"""
    i_ = [k_ for k_, l_ in enumerate(lines_) if l_.startswith('> 【画像挿入】') and key in l_]
    j_ = i_[0] - 1 if i_ else -1
    while j_ >= 0 and not lines_[j_].strip():
        j_ -= 1
    judge(f'「{key}」のマーカーが答えの直後（直前の行に「{prev}」）', j_ >= 0 and prev in lines_[j_])


after_('問1の完成形', '**▶ G点（290.18, 310.80）**')
after_('問2の完成形', '- **（3）関係人の氏名又は名称**：北冬子、山川一郎、東春男、東春子、西秋男、A市')
# 問2の答えを、会話の中で語として言っているか（2026-10-02、R5/Q22の照らし直しから）
for s_ in ['だから（1）は5番と6番', '（2）は2番32、3番3、100番', '北冬男さんを外して、北冬子、山川一郎、東春男、東春子、西秋男、A市']:
    check('問2の答えを会話で明示', s_)
html_1 = open(os.path.join(ZU, 'R1_dai21mon_dai1ran_kansei.html'), encoding='utf-8').read()
html_2 = open(os.path.join(ZU, 'R1_dai21mon_dai2ran_kansei.html'), encoding='utf-8').read()
for s_ in ['問１　Ｄ点及びＧ点の座標値', 'Ｘ座標（m）', 'Ｙ座標（m）', '>289.00<', '>300.00<', '>290.18<', '>310.80<', '問1 解答例']:
    check('問1の画像（HTML）', s_, html_1, '問1画像')
for s_ in ['（1）対象土地の地番', '>6番、5番<', '（2）関係土地の地番', '>2番32、3番3、100番<', '（3）関係人の氏名又は名称',
           '>北冬子、山川一郎、東春男、東春子、西秋男、Ａ市<', '問2 解答例']:
    check('問2の画像（HTML）', s_, html_2, '問2画像')
absent('問2の画像に申請人の北冬男がない', '北冬男', html_2, '問2画像')
for s_ in ['Ｄ点「289.00」「300.00」、Ｇ点「290.18」「310.80」', '「（3）関係人の氏名又は名称」に「北冬子、山川一郎、東春男、東春子、西秋男、Ａ市」',
           '**仮のもの**']:
    check('問1・問2の画像のプロンプト', s_, form, '登記申請書')
check('問題文の注の書き分け', '今年だけなのは問題文の注5と注6')
absent('どの注か分からない書き方（解説図プロンプトの差し替えデータ）', '（注3）', fig[fig.index('## 差し替えデータ'):], '解説図')

print('NG件数:', ng)
