"""令和8年度 第21問（土地）会話形式note記事：記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト。

答えは問題文の座標から計算し直した値と照らし、さらにアガルートの解答例（2026-10-20受領。答案用紙を再現したもの）と
欄ごと・空欄ごとに照らす（ANSWER_KEY）。
実行: python3 note-articles-Kijyutsu/R8/Q21/verify_R8_dai21mon_kaiwa.py"""
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
from calc_helpers import P, r2, area, double_area_sum, chiseki, disp, fmt_num, radial, dms, intersect, to_dms  # noqa: E402
from keysim_note_article import simulate  # noqa: E402
import lint_note_article  # noqa: E402

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
ART = 'note_R8_dai21mon_tochi_kaiwa_kaisetsu.md'
text = rd(ART)
fig = rd('prompt_R8_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_R8_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_R8_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_R8_dai21mon_miidashi_gazou.md')
draw = rd('zu/draw_R8_dai21mon_kaisetsuzu.py')
ng = 0


def judge(label, ok):
    global ng
    ng += (not ok)
    print(('OK ' if ok else 'NG ') + label)


def check(label, s, src=None, name='記事'):
    judge(f'[{name}] {label} : {s}', s in (text if src is None else src))


def absent(label, s, src=None, name='記事'):
    judge(f'[{name}] 禁止語なし（{label}） : {s}', s not in (text if src is None else src))


# ---- 座標と答えを問題文から計算し直す ----
T1, T2 = P(481.86, 471.43), P(481.75, 506.66)
B, D, E, F = P(486.05, 505.19), P(510.78, 490.69), P(509.94, 475.79), P(486.05, 474.32)
H, I, J, M = P(486.05, 488.12), P(498.53, 494.70), P(510.78, 492.46), P(486.05, 491.31)
Craw = radial(T2, T1, 29.03, dms(90, 4, 40))
C = r2(Craw)
Cw = r2(radial(T2, T1, 29.03, -dms(90, 4, 40)))
Lraw = H + (I - H) * 6.05 / 12.48
L = r2(Lraw)
Lw = r2(H + (I - H) / abs(I - H) * 6.05)
Kraw, t, num, den = intersect(J, L, D, I)
K = r2(Kraw)
Kw = r2(D + (I - D) * (492.46 - D.imag) / (I - D).imag)
judge('C点 (510.78, 506.79)', C == P(510.78, 506.79))
judge('C点の誤り（反時計回り）(452.72, 506.61)', Cw == P(452.72, 506.61))
judge('L点 (492.10, 491.31)、Mの真北', L == P(492.10, 491.31) and L.imag == M.imag)
judge('L点の誤り (491.40, 490.94)', Lw == P(491.40, 490.94))
judge('K点 (506.23, 492.18)', K == P(506.23, 492.18))
judge('K点の誤り（Jの真南）(505.37, 492.46)', Kw == P(505.37, 492.46))
judge('C・J・DのX座標が同じ510.78', C.real == J.real == D.real)
judge('arg(T1 − T2) ＝ −89°49′15.97″', to_dms(__import__('cmath').phase(T1 - T2)) == '−89°49′15.97″')
judge('KはDI上（Conjg(K − D) × (I − D) のiの係数 0.007）', abs(((K - D).conjugate() * (I - D)).imag - 0.007) < 1e-9)
for got, want in [(disp(Lraw), '492.10 ＋ 491.3098…i'), (disp(num), '−7.0977 − 21.6825i'), (disp(den), '224.2185 − 88.9943i'),
                  (disp(Craw), '510.7797… ＋ 506.7900…i')]:
    judge(f'表示 {want}', got == want)
    check('表示', '表示：' + want)
KOU, OTSU, RO = [E, D, I, H, F], [D, C, B, H, I], [I, K, L]
KOU1, OTSU1 = [E, D, K, L, H, F], [D, C, B, M, H, L, K]
URI, S58, S59 = [J, C, B, M, L, K], [H, L, M], [D, J, K]
AREAS = [('甲土地', KOU, 413.325, None), ('乙土地', OTSU, None, None), ('（ロ）', RO, 21.1533, 21.15), ('（イ）', KOU1, 392.1763, 392.17),
         ('2番42', URI, None, 352.29), ('2番58', S58, None, 9.64), ('2番59', S59, None, 4.02)]
for n, pts, exact, ch in AREAS:
    a = area(pts)
    if exact is not None:
        judge(f'{n}の面積 {exact}', abs(a - exact) < 1e-6)
    if ch is not None:
        judge(f'{n}の地積 {ch}', chiseki(a) == ch)
judge('乙土地の実測 344.8221…', fmt_num(area(OTSU)) == '344.8221…')
judge('合筆後の区画の座標 365.97（書かない値）', chiseki(area(OTSU1)) == 365.97)
judge('合筆後の2番42 ＝ 344.84 ＋ 21.15 ＝ 365.99', round(344.84 + 21.15, 2) == 365.99)
judge('引き算の誤り 413.30 − 21.15 ＝ 392.15', round(413.30 - 21.15, 2) == 392.15)
judge('分筆後の合計 365.95、差0.04', round(352.29 + 9.64 + 4.02, 2) == 365.95)
for s in ['（実部）− 826.65i', '−40.9682 − 42.3066i', '（実部）− 784.3526i', '（実部）− 704.5887i', '10.1761 ＋ 19.2995i',
          '2.6373 ＋ 8.0535i']:
    check('表示', '表示：' + s)
for pts, s in [(KOU, '826.65'), (KOU1, '784.3526'), (URI, '704.5887')]:
    judge(f'倍面積のiの係数 {s}', fmt_num(abs(double_area_sum(pts).imag)) == s)
SIDES = {'DJ': (D, J, '1.77'), 'JC': (J, C, '14.33'), 'CB': (C, B, '24.78'), 'BM': (B, M, '13.88'), 'MH': (M, H, '3.19'),
         'HL': (H, L, '6.84'), 'LK': (L, K, '14.16'), 'KD': (K, D, '4.79'), 'JK': (J, K, '4.56'), 'LM': (L, M, '6.05')}
for n, (p, q, want) in SIDES.items():
    judge(f'辺長 {n} {want}', f'{round(abs(p - q) + 1e-9, 2):.2f}' == want)
    check('辺長の一覧', f'- **{n}' + ('（分筆線）' if n in ('JK', 'LM') else '') + '**：', name='記事')
for v in ['24.7817…', '14.1567…', '4.5586…', '6.8394…', '4.7877…']:
    check('辺長の表示', '表示：' + v)

# ---- 答え（欄・空欄ごと） ----
ANS = ['- **ア**：登記名義人', '- **イ**：運転免許証', '- **ウ**：個人番号カード', '- **エ**：旅券等',
       '**▶ K点（506.23, 492.18）**', '**▶ C点（510.78, 506.79）**',
       '- **登記の目的**：土地分合筆登記', '- **添付書類**：地積測量図　登記識別情報　印鑑証明書　代理権限証書',
       '- **記号**：イ、エ', '- **申請人**：M市A町二丁目2番19号　佐藤佑介', '- **登録免許税**：金2,000円', '- **所在**：M市A町二丁目',
       '①2番19、②宅地、③413.30、登記原因は空欄', '①（イ）2番19、②宅地、③392.17、登記原因「③2番42に一部合併」',
       '①（ロ）、③21.15、登記原因「2番19から分割して2番42に合併する部分」', '①2番42、②宅地、③344.84、登記原因は空欄',
       '①2番42、②宅地、③365.99、登記原因「③2番19から一部合併」',
       '地番（2番42、2番58、2番59）', '（イ）2－42、（ロ）2－58、（ハ）2－59', '書かない**：各筆界点の座標値']
for s in ANS:
    check('答え', s)
# 誤答の数値
for s in ['（491.40, 490.94）', '（505.37, 492.46）', '（452.72, 506.61）', '392.15', '365.97', 'M市N町一丁目25番3号']:
    check('誤答の数値', s)

# ---- アガルートの解答例（2026-10-20受領）と欄ごと・空欄ごとに照合 ----
ANSWER_KEY = {
    '第1欄 ア': ('登記名義人', '- **ア**：登記名義人'), '第1欄 イ': ('運転免許証', '- **イ**：運転免許証'),
    '第1欄 ウ': ('個人番号カード', '- **ウ**：個人番号カード'), '第1欄 エ': ('旅券等', '- **エ**：旅券等'),
    '第2欄 K点': ('506.23, 492.18', '**▶ K点（506.23, 492.18）**'), '第4欄 C点': ('510.78, 506.79', '**▶ C点（510.78, 506.79）**'),
    '第3欄 登記の目的': ('土地分合筆登記', '- **登記の目的**：土地分合筆登記'),
    '第3欄 添付書類': ('地積測量図 登記識別情報 印鑑証明書 代理権限証書', '- **添付書類**：地積測量図　登記識別情報　印鑑証明書　代理権限証書'),
    '第3欄 記号欄': ('イ，エ', '- **記号**：イ、エ'), '第3欄 申請人': ('Ｍ市Ａ町二丁目２番19号 佐藤佑介', '- **申請人**：M市A町二丁目2番19号　佐藤佑介'),
    '第3欄 登録免許税': ('金2,000円', '- **登録免許税**：金2,000円'), '第3欄 所在': ('Ｍ市Ａ町二丁目', '- **所在**：M市A町二丁目'),
    '第3欄 1行目': ('２番19 宅地 413.30', '①2番19、②宅地、③413.30'),
    '第3欄 2行目': ('(イ)２番19 392.17 ③２番42に一部合併', '①（イ）2番19、②宅地、③392.17、登記原因「③2番42に一部合併」'),
    '第3欄 3行目': ('(ロ) 21.15 ２番19から分割して２番42に合併する部分', '①（ロ）、③21.15、登記原因「2番19から分割して2番42に合併する部分」'),
    '第3欄 4行目': ('２番42 宅地 344.84', '①2番42、②宅地、③344.84'),
    '第3欄 5行目': ('２番42 365.99 ③２番19から一部合併', '①2番42、②宅地、③365.99、登記原因「③2番19から一部合併」'),
    '第5欄 地番': ('２番42、２番58、２番59', '地番（2番42、2番58、2番59）'),
    '第5欄 符号': ('（イ）2-42（ロ）2-58（ハ）2-59', '（イ）2－42、（ロ）2－58、（ハ）2－59'),
    '第5欄 隣接地': ('2-18 2-41 2-43 2-55 2-56 2-57 2-19', '2－41・2－43・2－56・2－57・2－19、点で接する2－18・2－55'),
    '第5欄 境界標': ('C、D、H、K、L、M：コンクリート杭 B、J：金属標', '境界標（D・C・H・K・L・Mはコンクリート杭、B・Jは金属標）'),
}
for k, (ans, art) in ANSWER_KEY.items():
    check(f'解答例 {k}「{ans}」', art)
for n, v in [('DJ', '1.77'), ('JC', '14.33'), ('CB', '24.78'), ('BM', '13.88'), ('MH', '3.19'), ('HL', '6.84'), ('LK', '14.16'),
             ('KD', '4.79'), ('JK', '4.56'), ('LM', '6.05')]:
    judge(f'解答例 第5欄 辺長 {n} {v}', SIDES[n][2] == v)
judge('解答例 第5欄 隣接地 2－18・2－55 を作図スクリプトに描いた', "'2－18'" in draw and "'2－55'" in draw)

# ---- 条文（原典 note-articles/laws/ で確認済みのもの） ----
for s in ['不動産登記規則第72条第1項第3号', '不動産登記法第23条第4項第1号', '第72条第2項第2号', '不動産登記規則第35条第1号',
          '登録免許税法別表第一の一の（十三）', '不動産登記法第41条', '準則第68条第3号', '不動産登記規則第78条',
          '不動産登記規則第10条第2項第1号', '準則第72条第1項', '不動産登記令第8条第1項第1号', '同条第2項第1号',
          '不動産登記規則第47条第3号イ（6）', '不動産登記令第18条第1項・第2項', '準則第76条', '準則第67条第1項第4号ただし書']:
    check('条文', s)
laws = os.path.join(HERE, '..', '..', '..', 'note-articles', 'laws')
k1 = open(os.path.join(laws, 'fudousan-touki-kisoku-1.md'), encoding='utf-8').read()
judge('原典：規則第72条第1項第3号の「申請の権限を有する登記名義人であることを確認するため」', '申請の権限を有する登記名義人であることを確認するため' in k1)
judge('原典：規則第72条第2項第1号の書類の順（運転免許証→個人番号カード→旅券等→在留カード）',
      re.search('運転免許証.*個人番号カード.*旅券等.*在留カード.*特別永住者証明書.*運転経歴証明書', k1) is not None)
judge('原典：規則第47条第3号イ（6）合筆の登記', '（６） 合筆の登記、合体による登記等又は建物の合併の登記' in k1)
rei = open(os.path.join(laws, 'fudousan-touki-rei.md'), encoding='utf-8').read()
judge('原典：令第8条第2項第1号（いずれか一筆）', '当該合筆に係る土地のうちいずれか一筆の土地の所有権の登記名義人の登記識別情報' in rei)
jun = open(os.path.join(laws, 'fudousan-touki-jimu-junsoku.md'), encoding='utf-8').read()
judge('原典：準則第76条「③何番に一部合併」', '「③何番に一部合併」' in jun and '「③何番から一部合併」' in jun)

# ---- 体裁（タイトル・登場人物・区切り線・注の書き分け） ----
title = text.splitlines()[0]
m = re.match(r'^# 【土地家屋調査士受験生向け】令和8年度問題21（土地）〜(.+)〜$', title)
judge('タイトルの形式', m is not None)
judge(f'見出しは25文字以内（{len(m.group(1))}文字）', m is not None and len(m.group(1)) <= 25)
check('登場人物（トリ先生）', '**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。')
check('登場人物（藍子）', '**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。')
judge('照合済みの一文', text.splitlines()[2] == '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。')
judge('記事に「仮の形」「未発表」が残っていない', '仮の形' not in text and '未発表' not in text)
judge('記事の最後が区切り線', text.rstrip().endswith('---'))
judge('話者名の行末はハードブレーク', all(l.endswith('  ') for l in text.splitlines() if re.match(r'^\*\*(トリ先生|藍子)\*\*\s*$', l)))
bare = re.findall(r'(?<!の)注[1-9１-９]', text)
judge(f'注は「問題文の注」「調査図素図の注」と書き分け（裸の「注N」{len(bare)}件）', not bare)
judge('「アガルート」は冒頭の照合済みの一文だけ', text.count('アガルート') == 1)
for w in ['PDF', '✕', '✓', '名変', 'コンクリートくい', '図1']:
    absent('禁止語', w)

# ---- lint と キー列の再現 ----
res = simulate(os.path.join(HERE, ART))
judge(f'キー列の再現（表示 {len(res)}個）すべて一致', len(res) == 19 and all(ok for *_, ok in res))
import io
import contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    lint_note_article.lint(os.path.join(HERE, ART))
judge('lint：表記ルール違反なし', '表記ルール違反: なし' in buf.getvalue())

# ---- 画像挿入マーカーとPNGの1対1の対応（記事の順） ----
markers = [l for l in text.splitlines() if l.startswith('> 【画像挿入】')]
MAP = [('時系列の図', 'zu01_jikeiretsu'), ('北を上にして', 'zu02_zentaizu'), ('注の仕分け', 'zu03_chuu_shiwake'),
       ('不動産登記規則第72条第1項の整理図', 'zu04_kisoku72_1'), ('本人確認の書類', 'zu05_shorui'), ('第1欄', 'dai1ran_kansei'),
       ('L点の求め方', 'zu06_L_ten'), ('K点の求め方', 'zu07_K_ten'), ('第2欄', 'dai2ran_kansei'),
       ('条件の数え方', 'zu08_K_jouken'), ('補助線で交点の式を作り直す', 'zu09_K_hojosen'), ('5つの型の表', 'zu10_K_pattern'), ('線を延ばして描く図', 'zu11_K_nobasu'),
       ('手が止まったときの手順', 'zu12_K_mayottara'),
       ('申請件数と登録免許税', 'zu13_kensuu'), ('合筆の制限', 'zu14_goppitsu_seigen'), ('本件登記1と本件登記2の地積測量図の範囲', 'zu15_chiseki_hani_8gatsu'),
       ('甲土地の面積の計算', 'zu16_kou_menseki'), ('甲土地の公差', 'zu17_kousa'), ('（ロ）三角形I・K・Lの面積', 'zu18_ro_menseki'), ('（イ）2番19の地積', 'zu19_i_chiseki'), ('合筆後の2番42', 'zu20_gappei_go'),
       ('申請人の住所', 'zu21_juusho'), ('合筆の登記識別情報の図', 'zu22_shikibetsu_1hitsu'), ('甲区の持分', 'zu23_kouku_mochibun'), ('「添付書類」欄の誤答', 'toukishinseisho_machigai'),
       ('（ロ）の原因の書き方', 'zu24_bunkatsu'), ('分合筆で変わる欄', 'zu25_chimoku_ran'),
       ('登記申請書（問3）の完成形', 'toukishinseisho_kansei'), ('C点の求め方', 'zu26_C_housha'), ('第4欄', 'dai4ran_kansei'),
       ('本件登記2の分筆', 'zu27_sanpitsu'), ('新しい地番', 'zu28_chiban'), ('11月の分筆後の合計と公差', 'zu29_kousa_11gatsu'), ('辺長10本の求め方', 'zu30_henchou'), ('地積測量図に描く範囲', 'zu31_I_egakanai'),
       ('隣接地の地番の図', 'zu32_rinsetsu'),
       ('第5欄の地積測量図', 'zu33_chiseki_sokuryouzu'), ('本番で解く順番', 'zu34_kaku_junban')]
judge(f'マーカーの数 {len(markers)}（{len(MAP)}）', len(markers) == len(MAP))
for mk, (head, png) in zip(markers, MAP):
    judge(f'マーカー「{head}」→ zu/R8_dai21mon_{png}.png', head in mk and os.path.exists(os.path.join(HERE, 'zu', f'R8_dai21mon_{png}.png')))
pngs = sorted(f for f in os.listdir(os.path.join(HERE, 'zu')) if f.endswith('.png'))
judge(f'zu/ に記事で使わないPNGがない（{len(pngs)}枚）', sorted(f'R8_dai21mon_{p}.png' for _, p in MAP) == pngs)

# ---- まとめのワナ → 図（1項目に1ワナ、図の重複なし、図は正す会話の直後） ----
TRAPS = [('本人確認情報の（ア）は「登記名義人」', '不動産登記規則第72条第1項の整理図', '面識が生じた経緯'),
         ('（イ）〜（エ）は第2項第1号の書類', '本人確認の書類', '旅券等は、旅券と乗員手帳'),
         ('L点はMから真北に6.05m', 'L点の求め方', '区画の形が変わってしまう'),
         ('K点はJLとDIの交点', 'K点の求め方', 'KはちゃんとDとIの直線の上'),
         ('問題用紙の図は線が途中で切れている', '線を延ばして描く図', 'どちらも線分の内側の交点よ'),
         ('本件登記1は分合筆の1件', '申請件数と登録免許税', '三角形は地番をもらわないまま'),
         ('家庭菜園でも宅地', '合筆の制限', '合筆の制限には当たりません'),
         ('本件登記1はC点を待たずに申請できる', '本件登記1と本件登記2の地積測量図の範囲', '11月5日なんですね'),
         ('（イ）2番19は座標の392.17', '（イ）2番19の地積', '甲2の範囲内ね'),
         ('合筆後の2番42は365.99', '合筆後の2番42', '365.99㎡ですね'),
         ('申請人は今の住所', '申請人の住所', '住所の変更を証する情報も要りません'),
         ('合筆の登記識別情報は1筆分で足りる', '合筆の登記識別情報の図', '本人確認情報も要らない'),
         ('記号欄はイとエ', '甲区の持分', '今の名義人のものではありません'),
         ('合筆には印鑑証明書', '「添付書類」欄の誤答', '分合筆も合筆だから必要'),
         ('C点は時計回りに足す', 'C点の求め方', '放射の検算になる'),
         ('本件登記2は3筆の分筆', '本件登記2の分筆', '3,000円よ'),
         ('新しい地番は面積の大きい順', '新しい地番', 'D・J・Kが2番59'),
         ('I点は描かない', '地積測量図に描く範囲', 'D→K→L→Hです'),
         ('（ロ）の原因は「分割して」', '（ロ）の原因の書き方', '直して並べます'),
         ('隣接地は角で接する土地も', '隣接地の地番の図', '書き漏らさないようにします')]
summ = text[text.index('今日のわなをおさらい'):text.index('全部の問が')]
items = [l for l in summ.splitlines() if l.startswith('- **')]
judge(f'まとめのワナ {len(items)}項目 ＝ 対応表 {len(TRAPS)}', len(items) == len(TRAPS))
judge('対応表の図に重複がない', len({f for _, f, _ in TRAPS}) == len(TRAPS))
lines = text.splitlines()
for trap, figkey, key in TRAPS:
    judge(f'ワナ「{trap}」がまとめにある', any(trap in l for l in items))
    idx = [i for i, l in enumerate(lines) if l.startswith('> 【画像挿入】') and figkey in l]
    prev = ''
    if idx:
        j = idx[0] - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        prev = lines[j]
    judge(f'  図「{figkey}」は「{key}」の会話の直後', bool(idx) and key in prev)

# ---- K点に全く手が出なかった人への節（2026-10-20追加） ----
ksec = text[text.index('### K点に全く手が出なかった人へ'):text.index('## 第4章')]
for s_ in ['調査図素図の注4', '条件の数を数える', '芋づる', 'K ← L ← H・I・M', '補助線', '7.0977 ＋ 21.6825i', '231.3162 − 67.3118i',
           '21.6825 ＋ 67.3118 ＝ 88.9943', '2直線の交点', '直線上で決まった距離', '平行で決まった幅だけ離れた直線', '垂線の足', '面積の条件',
           '令和3年度のH点', '平成30年度のI点', '平成28年度のJ点', '平成24年度のK点', '平成22年度のK点', '令和5年度のB点・H点', '平成29年度のH点・I点',
           '令和元年度のG点', '平成20年度のF点', '平成24年度のL点', '平成21年度のJ点', '令和7年度の2等分', 't ＝ 0.24', '0.37', '3分', '2時間30分', 'メモ']:
    judge(f'K点の節に「{s_}」', s_ in ksec)
_D, _J, _I, _L = P(510.78, 490.69), P(510.78, 492.46), P(498.53, 494.70), P(492.10, 491.31)
judge('高さの比の値（21.6825・−67.3118、和88.9943、K一致）',
      disp((_J - _D).conjugate() * (_I - _D)) == '7.0977 ＋ 21.6825i' and disp((_L - _D).conjugate() * (_I - _D)) == '231.3162 − 67.3118i'
      and disp(_J + (_L - _J) * 21.6825 / (21.6825 + 67.3118)) == '506.2288… ＋ 492.1798…i')

# ---- 藍子の質問の行を全部拾い、思い込みを正す答えなら図・まとめ・TRAPSがそろっているか（チェック指示書6-2の7） ----
# 値が None：情報を聞くだけの質問（答えが「違う／しなくていい」ではない）。値が文字列：訂正の図のマーカーの語（TRAPSにもある）
QUESTIONS = {'電卓の準備はどうしますか': None, '読んではいたんです': None, '交点の式を思い出せなかったら': None,
             '高さはどうやって出すんですか': None, '全然知らない形の問題': None,
             '問題用紙の調査図素図じゃだめなんですか': '線を延ばして描く図', '見当』は、どうやってつけるんですか': None,
             '何を見て決めればいいですか': None, '座標で計算した365.97㎡……': '合筆後の2番42', '地番はどうなりますか': None,
             '本番の時間配分はどうしたらいいですか': None}
_tl = text.split('\n')
_qs = [_tl[i + 1] for i, l_ in enumerate(_tl[:-1]) if l_.startswith('**藍子**') and ('？' in _tl[i + 1] or 'でしょうか' in _tl[i + 1])]
judge(f'藍子の質問の行 {len(_qs)}個がすべて分類済み', len(_qs) == len(QUESTIONS) and all(any(k in q for k in QUESTIONS) for q in _qs))
for k, fk in QUESTIONS.items():
    if fk:
        judge(f'  思い込みを正す質問「{k}」の図がTRAPSにある', any(f == fk for _, f, _ in TRAPS))

# ---- 解説図プロンプト ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + title[2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
judge('解説図プロンプトの図の数 34枚', len(re.findall(r'^- \*\*図\d+：', fig, re.M)) == 34)
nums = [int(p[2:4]) for _, p in MAP if p.startswith('zu')]
judge(f'解説図のPNGの番号が記事の挿入順に1〜{len(nums)}', nums == list(range(1, len(nums) + 1)))
judge('作図スクリプトのタイトルに図番がない', not re.search(r"(new_figure|board|suptitle)\(\s*'図\d", draw))
for s in ['（506.23, 492.18）', '（510.78, 506.79）', '（492.10, 491.31）', '392.1763', '21.1533', '365.99', '352.29', '9.64', '4.02',
          '14.16（14.1567…）', '位置は模式']:
    check('解説図プロンプトの数値', s, fig, '解説図')
judge('作図スクリプトのタイトルに図番がない', not re.search(r"(new_figure|board|suptitle)\(\s*'図\d", draw) and not re.search(r"'図\d+[　 ]", draw))
judge('作図スクリプト：N点は「位置は模式」', '位置は模式' in draw)

# ---- 申請書・添削・見出し画像のプロンプトと生成画像 ----
for s in ['土地分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', '記号欄（項目名「記　号　欄」、小さな枠）：「イ，エ」', 'Ｍ市Ａ町二丁目２番19号　佐藤佑介', '金2,000円',
          '「(イ)２番19」「宅地」「392｜17」「③２番42に一部合併」', '「２番19から分割して２番42に合併する部分」',
          '「２番42」「宅地」「365｜99」「③２番19から一部合併」', '令和８年８月20日　申請　Ａ地方法務局']:
    check('申請書のプロンプト', s, form, '申請書')
for s in ['地積測量図　登記識別情報　代理権限証書', '印鑑証明書', '縦に積んだ縦長']:
    check('添削のプロンプト', s, fix, '添削')
for s in ['土地家屋調査士受験生向け', '令和8年度問題21（土地）', '〜' + m.group(1) + '〜']:
    check('見出し画像の文字', s, thumb, '見出し')
judge('見出し画像のプロンプトに前年度の文言が残っていない', '令和5' not in thumb and 'GとI' not in thumb)


def png_size(p):
    with open(p, 'rb') as f:
        h = f.read(24)
    return struct.unpack('>II', h[16:24])


for n, tall in [('toukishinseisho_kansei', True), ('toukishinseisho_machigai', True), ('dai1ran_kansei', False),
                ('dai2ran_kansei', False), ('dai4ran_kansei', False)]:
    w, h = png_size(os.path.join(HERE, 'zu', f'R8_dai21mon_{n}.png'))
    judge(f'{n}.png 横1200px' + ('・縦長' if tall else ''), w == 1200 and (h > w if tall else True))
    html = open(os.path.join(HERE, 'zu', f'R8_dai21mon_{n}.html'), encoding='utf-8').read()
    judge(f'{n}.html に style="height: がない', 'style="height:' not in html)
html = open(os.path.join(HERE, 'zu', 'R8_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
for s in ['土地分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', '記　号　欄', 'イ，エ', '令和８年８月20日　申請　Ａ地方法務局', 'Ｍ市Ａ町二丁目２番19号　佐藤佑介', '金2,000円',
          '③２番42に一部合併', '２番19から分割して２番42に合併する部分', '③２番19から一部合併', '>392<', '>365<', '>99<',
          'width:15.88%', 'width:41.09%', '③地　　積（㎡）']:
    judge(f'申請書のHTML：{s}', s in html)
# ---- 申請書の土地の表示の表を、解答例のPDF（ベクター）の罫線と比べる（2026-10-26、pymupdf の get_drawings で測定） ----
# 表の外枠 x 684.6〜1140.6pt、縦の罫線 711.4・770.5（所在の欄だけ）・784.0・856.4・921.0（点線）・953.2
_x = [684.6, 711.4, 770.5, 784.0, 856.4, 921.0, 953.2, 1140.6]
_meas = [round((_x[i + 1] - _x[i]) / (_x[-1] - _x[0]) * 100, 2) for i in range(7)]
_cols = [float(v) for v in re.findall(r'<col style="width:([0-9.]+)%">', html)[:7]]
judge(f'土地の表示の列の幅が原本の罫線と0.1%以内（{_cols}）', len(_cols) == 7 and all(abs(a_ - b_) <= 0.1 for a_, b_ in zip(_cols, _meas)))
# 行の高さ：所在 43.1pt・見出し 19.8pt・記入行 56.7pt、表の幅 1060px ÷ 456pt ＝ 2.325px/pt
_mk = rd('zu/make_R8_dai21mon_shinseisho_gazou.py')
judge('土地の表示の行の高さが原本の比（記入行132px・見出し46px・所在100px）',
      all(t in _mk for t in ['height: 132px', 'td.head {{ height: 46px', 'shozai-lab {{ text-align: center; height: 100px']))
judge('申請書のHTMLに「第○欄」がない', not re.search('第[0-9０-９]欄', html))
for n, s in [('dai1ran_kansei', ['第1欄', '登記名義人', '運転免許証', '個人番号カード', '旅券等']),
             ('dai2ran_kansei', ['第2欄', '506.23', '492.18']), ('dai4ran_kansei', ['第4欄', '510.78', '506.79'])]:
    h_ = open(os.path.join(HERE, 'zu', f'R8_dai21mon_{n}.html'), encoding='utf-8').read()
    judge(f'{n}.html の記入：{"・".join(s)}', all(x in h_ for x in s))
judge('地積測量図の枠の書式（第5欄・地番・土地の所在・地積測量図・作成日・縮尺）',
      all(x in draw for x in ["'第5欄'", "'地　　番'", "'土地の所在'", "'地　積　測　量　図'", '（令和８年○月○日作成）', "'縮尺'", "'250'"]))

# ---- 動画化の準備（douga/：計算過程のコマ・絵コンテ・試作の動画） ----
DOUGA = {'D01_C_housha': 7, 'D02_L_ten': 6, 'D03_K_kouten': 8, 'D04_kou_menseki': 8, 'D05_ro_sankaku': 4,
         'D06_i_menseki': 9, 'D07_gappei_go': 4, 'D08_sanpitsu_menseki': 12, 'D09_henchou': 12,
         'D10_K_hojosen': 9}
ddir = os.path.join(HERE, 'douga')
kontei = open(os.path.join(ddir, 'kontei_R8_dai21mon_douga.md'), encoding='utf-8').read()
for d, n in DOUGA.items():
    frames = sorted(x for x in os.listdir(os.path.join(ddir, d)) if x.endswith('.png'))
    judge(f'動画 {d}：コマ{n}枚（1280×720）', frames == [f'step{k:02d}.png' for k in range(1, n + 1)]
          and all(png_size(os.path.join(ddir, d, x)) == (1280, 720) for x in frames))
    judge(f'動画 {d}：絵コンテに{n}ステップ', f'## {d}：' in kontei and f'（{n}コマ）' in kontei.split(f'## {d}：')[1].split('\n## ')[0])
    judge(f'動画 {d}.mp4 がある', os.path.getsize(os.path.join(ddir, d + '.mp4')) > 10000)
for s in ['510.7797… ＋ 506.7900…i', '492.10 ＋ 491.3098…i', '−7.0977 − 21.6825i', '224.2185 − 88.9943i', '506.2288… ＋ 492.1798…i',
          '826.65', '21.1533', '392.17', '344.84 ＋ 21.15', '352.29', '9.64', '4.02', '14.1567…', '（452.72, 506.61）', '（491.40, 490.94）', '（505.37, 492.46）',
          '7.0977 ＋ 21.6825i', '231.3162 − 67.3118i', '21.6825 ÷ (21.6825 ＋ 67.3118)']:
    judge(f'絵コンテに記事と同じ値：{s}', s in kontei)
for s in ['510.7797… ＋ 506.7900…i', '492.10 ＋ 491.3098…i', '506.2288… ＋ 492.1798…i', '392.17', '352.29']:
    judge(f'記事にも同じ値：{s}', s in text)
judge('絵コンテに図番がない', not re.search('図[0-9０-９]', kontei))

# ---- 第5欄の枠を解答例のPDFの罫線（mm）と比べ、図が1/250の実寸かを確かめる（2026-10-26） ----
for t in ['mrect(56.3, 12.2, 406.9, 274.8', 'mrect(81.3, 26.7, 383.3, 257.7', 'mrect(241.3, 16.7, 303.3, 26.7', 'mrect(241.3, 26.7, 383.3, 36.7',
          'mrect(81.3, 257.7, 224.3, 272.2', 'mrect(240.3, 257.7, 383.3, 272.2', 'mline(362.7, 270.2, 379.8, 259.7']:
    judge(f'第5欄の枠が原本の寸法どおり：{t}', t in draw)
judge('第5欄の図が実寸（紙の範囲mmからfigsize、1mm＝0.25m）', all(t in draw for t in [
    'figsize=((PX1 - PX0) / 25.4, (PY1 - PY0) / 25.4)', 'WM, HM = (AX1 - AX0) * 250 / 1000, (AY1 - AY0) * 250 / 1000']))

print('NG件数:', ng)
sys.exit(1 if ng else 0)
