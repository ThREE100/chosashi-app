"""平成28年度 第21問（土地）会話形式note記事：記事・付属プロンプトの数値・体裁の照合スクリプト。
記事の答えが、アガルートの解答例（2026-09-29に添付の過去問集で照合。下の AGAROOT に転記）と一致することも確認する。
食い違いの記録：アガルートの解説は戊土地の（ニ）部分を畑とする（記事は、丙土地と一体の雑種地と見るのが素直、畑と見る解説もある、
どちらでも（ハ）部分の宅地とは地目が違う、と書く。問2の答え〈2筆・一の申請情報でできる〉は同じ）。
実行: python3 note-articles-Kijyutsu/H28/Q21/verify_H28_dai21mon_kaiwa.py"""
import cmath
import math
import os
import re
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
from calc_helpers import (P, r2, radial, dms, to_dms, area, double_area_sum, chiseki, disp, fmt_num,  # noqa: E402
                          intersect, kousa_kou2)

rd = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()  # noqa: E731
text = rd('note_H28_dai21mon_tochi_kaiwa_kaisetsu.md')
fig = rd('prompt_H28_dai21mon_kaiwa_kaisetsuzu.md')
base = open(os.path.join(HERE, '..', '..', 'prompt_kaisetsuzu-gazou_kihon-form_tochi.md'), encoding='utf-8').read()
form = rd('prompt_H28_dai21mon_toukishinseisho_gazou.md')
fix = rd('prompt_H28_dai21mon_toukishinseisho_machigai.md')
thumb = rd('prompt_H28_dai21mon_miidashi_gazou.md')
draw = open(os.path.join(HERE, 'zu', 'draw_H28_dai21mon_kaisetsuzu.py'), encoding='utf-8').read()
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


# ---- 座標（問題文のA市基準点成果表・I点、32番1と40番1の地積測量図の抜粋） ----
A101, A102 = P(325.32, 272.32), P(333.27, 301.99)
A, B = P(348.50, 265.15), P(352.91, 284.25)                 # 32番1のK5・K4
K1, K2, K3 = P(366.00, 262.58), P(366.80, 266.81), P(369.86, 283.49)
G, F, E, H = P(350.47, 284.32), P(350.40, 293.88), P(334.85, 303.80), P(333.88, 280.15)   # 40番1の①②③④
I = P(332.29, 268.34)
for s in ['K5（348.50, 265.15）', 'K4（352.91, 284.25）', '①（350.47, 284.32）', '④（333.88, 280.15）',
          '②（350.40, 293.88）', '③（334.85, 303.80）']:
    check('地積測量図の点と調査素図の点', s)
judge('32番1の地積測量図の辺長 K4K5 19.60・K2K3 16.96・K3K4 16.97・K5K1 17.69',
      [f'{abs(q - p):.2f}' for p, q in [(B, A), (K2, K3), (K3, B), (A, K1)]] == ['19.60', '16.96', '16.97', '17.69'])
judge('40番1の地積測量図の辺長 ①② 9.56・②③ 18.44・③④ 23.67・④① 17.11',
      [f'{abs(q - p):.2f}' for p, q in [(G, F), (F, E), (E, H), (H, G)]] == ['9.56', '18.44', '23.67', '17.11'])
judge('32番1の面積 351.67100・40番1の面積 268.13610（地積測量図の座標求積表と一致）',
      f'{area([K1, K2, K3, B, A]):.5f}' == '351.67100' and f'{area([G, F, E, H]):.5f}' == '268.13610')

# ---- 問1 D点（放射。観測角は右回り＝足す。後視A101の読み0°01′00″を引く） ----
check('arg(A101−A102)', to_dms(cmath.phase(A101 - A102)))
check('arg(A101−A102)＋360°', to_dms(cmath.phase(A101 - A102) + 2 * math.pi))
Dx = A102 + cmath.rect(5.18, cmath.phase(A101 - A102) + dms(168, 9, 0) - dms(0, 1, 0))
check('D 表示', '表示：' + disp(Dx))
D = r2(Dx)
check('D 答え', '**▶ D点（335.61, 306.61）**')
Dw = radial(A102, A101, 5.18, dms(168, 9, 0))
check('引き忘れた誤りの表示', disp(Dw))
judge('引き忘れても丸めると同じ（偶然）', r2(Dw) == D)
check('1′のずれ（5.18m先で約1.5mm）', f'たった{abs(Dx - Dw) * 1000:.1f}mm')
check('50mなら1.5cm', f'距離が50mなら{50 * math.radians(1 / 60) * 100:.1f}cm')
judge('方向角 A102→D ≒ 63°08′（三角関数真数表の63°08′00″）', to_dms(cmath.phase(Dx - A102)).startswith('63°08′'))
check('方向角の足し算', '255°00′ ＋ 168°08′ − 360° ＝ 63°08′')
check('DとEの位置', f'{(D - E).real:.2f}m北、{(D - E).imag:.2f}m東')

# ---- 問1 J点（Gを通るABの平行線と直線AIの交点） ----
Jx, t, num, den = intersect(A, I, G, G + (B - A))
check('交点の分子 表示', '表示：' + disp(num))
check('交点の分母 表示', '表示：' + disp(den))
check('t', f't ＝ 46.9127 ÷ 323.6789 ＝ {math.floor(t * 1e6) / 1e6:.6f}…')
check('J 表示', '表示：' + disp(A + (I - A) * 46.9127 / 323.6789))
J = r2(Jx)
check('J 答え', '**▶ J点（346.15, 265.61）**')
JW = r2(A + (G - B))
check('平行四辺形の誤りのJ', f'（{JW.real:.2f}, {JW.imag:.2f}）')
tw = (JW.real - A.real) / (I.real - A.real)
check('同じX座標での直線AIのY座標', f'Y＝{(A + (I - A) * tw).imag:.2f}')
judge('誤りのJは直線AIより西（41番の側）', JW.imag < (A + (I - A) * tw).imag)
check('誤りのJの離れ（約0.4m）', f'約{abs(((JW - A) * ((I - A) / abs(I - A)).conjugate()).imag):.1f}m西')
check('AIの方向角', f'{to_dms(cmath.phase(I - A))[:7]}')
check('BGの方向角', f'{to_dms(cmath.phase(G - B))[:7]}')
check('△AJI 表示', '表示：' + disp((J - A).conjugate() * (I - A)))
check('平行の確認 表示', '表示：' + disp((B - A).conjugate() * (G - J)))
check('△AJIの面積', f'0.0399 ÷ 2 ＝ {abs(((J - A).conjugate() * (I - A)).imag) / 2:.2f}㎡')
check('JAとBG', f'JAは{abs(A - J):.2f}で、BGの{abs(G - B):.2f}より短い')

# ---- 問3の準備 面積 ----
check('AB 表示', '表示：' + fmt_num(abs(B - A)))
check('GH 表示', '表示：' + fmt_num(abs(H - G)))
s_tei = double_area_sum([A, B, G, H, I])
check('丁土地 表示', '表示：' + disp(s_tei))
a_tei = area([A, B, G, H, I])
check('丁土地 面積', f'{a_tei:.5f}')
judge('丁土地の地積 276（登記記録と一致）', chiseki(a_tei, False) == 276)
check('参考公差', f'約{kousa_kou2(276):.2f}㎡')
check('差', f'差の{a_tei - 276:.2f}㎡')
check('（イ）対角線 表示', '表示：' + disp((J - H).conjugate() * (G - I)))
check('（ロ）対角線 表示', '表示：' + disp((A - G).conjugate() * (B - J)))
a_i, a_ro = area([J, G, H, I]), area([A, B, G, J])
judge('対角線の式と多角形の式の面積が一致', abs(abs(((J - H).conjugate() * (G - I)).imag) / 2 - a_i) < 1e-9
      and abs(abs(((A - G).conjugate() * (B - J)).imag) / 2 - a_ro) < 1e-9)
check('（イ）面積', f'{a_i:.4f}')
check('（ロ）面積', f'{a_ro:.4f}')
check('切り捨て前の合計', f'230.2059 ＋ 46.4342 ＝ {a_i + a_ro:.4f}')
judge('（イ）230・（ロ）46', chiseki(a_i, False) == 230 and chiseki(a_ro, False) == 46)

# ---- 問3 合筆後の32番1 ----
a_go = area([K1, K2, K3, B, G, J, A])
check('合筆後の32番1', f'合筆後の32番1 ＝ 351.67100 ＋ 46.4342 ＝ {a_go:.4f} → {chiseki(a_go, False)}㎡')
judge('7点の座標法でも398.1052', f'{a_go:.4f}' == '398.1052' and abs(a_go - (351.671 + a_ro)) < 1e-6)
check('誤答 351＋46', '351 ＋ 46 ＝ 397')
check('捨てた端数の合計', f'{0.671 + 0.4342:.4f}')
check('分筆と合筆の2件の誤答', '合わせて3,000円')

# ---- 問2 ----
for s in ['- **必要となる登記**：土地表題登記（（ニ）部分と（ハ）部分を2筆の土地として）',
          '- **一の申請情報によって申請することができるか否か**：一の申請情報によって申請することができる',
          '取得原因は時効取得、（ハ）部分の取得原因は売払いと異なるが', '登記原因及びその日付は不詳で同一である',
          '（ニ）部分が雑種地、（ハ）部分が宅地で地目が異なるため']:
    check('問2', s)
for s in ['不動産登記法第36条', '不動産登記事務取扱手続準則第68条第3号', '準則第69条第3号', '不動産登記令別表4の項添付情報欄ハ',
          '不動産登記令第4条ただし書', '不動産登記規則第76条第2項', '畑と見る解説もある']:
    check('問2の根拠', s)

# ---- 問3 申請書 ----
for s in ['- **登記の目的**：土地分合筆登記', '- **添付書類**：地積測量図　登記識別情報　印鑑証明書　代理権限証書',
          '- **登録免許税**：金2,000円（分合筆後の土地1個につき1,000円 × 2個）', '- **申請人**：A市B町一丁目16番1号　甲野太郎',
          '- **所在**：A市B町一丁目', '①40番2、②畑、③276（登記記録の地積）', '①（イ）40番2、③230、登記原因「③32番1に一部合併」',
          '①（ロ）、③46、登記原因「40番2から分割して32番1に合併する部分」', '①32番1、②畑、③351（登記記録の地積）',
          '①32番1、③398、登記原因「③40番2から一部合併」']:
    check('問3', s)
for s in ['不動産登記規則第35条第1号', '不動産登記法第41条', '不動産登記令別表8の項', '同令第8条第1項第1号',
          '不動産登記規則第47条第3号イ（6）', '不動産登記令第18条第1項・第2項', '準則第76条']:
    check('問3の根拠', s)

# ---- 問4 地積測量図 ----
SIDES = {'AB': (A, B), 'BG': (B, G), 'GH': (G, H), 'HI': (H, I), 'IJ': (I, J), 'JA': (J, A), 'JG（分筆線）': (J, G)}
for n, (p, q) in SIDES.items():
    v = f'{round(abs(p - q) + 1e-9, 2):.2f}'
    check(f'辺長{n}', f'- **{n}**：{v}')
    check(f'図の辺長{n}', v, fig, '解説図')
check('ABの四捨五入', f'ABは{abs(B - A):.4f}だから')
check('JAの四捨五入', f'JAは{math.floor(abs(A - J) * 1e4) / 1e4:.4f}…で')
check('不動産登記規則第78条', '不動産登記規則第78条')
check('答案用紙の大きさ（横）', f'横約{round((G.imag - A.imag) * 4):d}mm')
check('答案用紙の大きさ（縦）', f'縦約{round((B.real - I.real) * 4):d}mm')
check('基準点まで入れた横', f'横は約{round((A102.imag - A.imag) * 4):d}mm')
check('A102はGより東', f'Gより約{round(A102.imag - G.imag):d}m東')

# ---- アガルートの解答例（2026-09-29、過去問集の解答例ページから転記）と一致するか ----
AGAROOT = ['（335.61, 306.61）', '（346.15, 265.61）', '土地表題登記', '一の申請情報によって申請することができる', '不詳',
           '土地分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書', '金2,000円', '16番1号　甲野太郎',
           '③276', '③230', '③32番1に一部合併', '③46', '40番2から分割して32番1に合併する部分', '③351', '③398',
           '③40番2から一部合併', '：19.60', '：2.44', '：17.11', '：11.92', '：14.13', '：2.39', '：19.20']
for s in AGAROOT:
    check('アガルートの解答例と一致', s)

# ---- 付属プロンプトとの整合 ----
a = base.index('あなたは土地家屋調査士試験の教材デザイナーです。')
b = base.index('---\n\n## 差し替えデータ（問題ごとにここを埋める）')
body = base[a:b].replace('note記事【記事のタイトル】', 'note記事「' + text.splitlines()[0][2:] + '」', 1)
judge('解説図プロンプトの本文が基本フォームと一致', body in fig)
n_fig = len(re.findall(r'^- \*\*図\d：', fig, re.M))
judge(f'解説図プロンプトの図の数 {n_fig}枚（8枚）', n_fig == 8)
for i in range(1, 9):
    judge(f'作図済みPNG 図{i}', any(f.startswith(f'H28_dai21mon_zu0{i}_') and f.endswith('.png')
                                  for f in os.listdir(os.path.join(HERE, 'zu'))))
nums = [int(m) for m in re.findall(r"(?:new_figure\(|suptitle\()'図(\d)　", draw)]
judge(f'作図スクリプトの図のタイトル番号が1から順（{nums}）', nums == list(range(1, 9)))
for s in ['（335.61, 306.61）', '（346.15, 265.61）', '（346.06, 265.22）', '255°00′00.34″', '−104°59′59.66″', '168°08′00″',
          '46.9127 ÷ 323.6789', '276.62015', '230.2059', '46.4342', '351.67100', '398.1052', '351 ＋ 46 ＝ 397',
          '19m60', '17m11', '横約77mm・縦約82mm', '横約147mm', '19.6025', '2.3945…', '約0.4m西']:
    check('解説図プロンプトの数値', s, fig, '解説図')
    check('作図スクリプトの数値', s, draw, '作図')
for s in ['北を上にして描き直すと、こうなるわ', '位置も合っています', '台形だからよ', 'ここが問3の山場につながるのよ',
          '2筆の土地表題登記になるんですね', '実務ならここで使うの', '書き足すものはないわ', 'JGはABと平行に描くのよ']:
    check('図の挿入位置の文言', s)
    check('図の挿入位置の文言（プロンプト側）', s, fig, '解説図')
for s in ['平成28年○月○日　申請　Ａ地方法務局', '土地分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書',
          'Ａ市Ｂ町一丁目16番１号　甲野太郎', '金2,000円', 'Ａ市Ｂ町一丁目', '①「40番２」、②「畑」、③「276｜」',
          '①「（イ）40番２」、②空欄、③「230｜」、登記原因「③32番１に一部合併」',
          '①「（ロ）」、②空欄、③「46｜」、登記原因「40番２から分割して32番１に合併する部分」', '①「32番１」、②「畑」、③「351｜」',
          '①「32番１」、②空欄、③「398｜」、登記原因「③40番２から一部合併」', '**記入行6**：空欄',
          '「登記の目的 → 添付書類 → 登録免許税 → 申請の日付と提出先 → 申請人 → 代理人 → 土地の表示」',
          '「①地番」「②地目」「③地積　m²」']:
    check('登記申請書', s, form, '登記申請書')
for s in ['金3,000円', '金2,000円', '「397｜」', '「398｜」', '分合筆1件なら、分合筆後の2個で2,000円！',
          '351.67100＋46.4342＝398.1052 → 398', '平成28年度 第21問｜分合筆は1件で2,000円、合筆後の32番1は398㎡',
          '捨てた端数の0.671と0.4342の合計1.1052の分だけ足りなくなるんですね']:
    check('添削', s, fix, '添削')
check('添削の挿入位置の文言', '捨てた端数の0.671と0.4342の合計1.1052の分だけ足りなくなるんですね')

# ---- 生成済みの申請書・添削画像（縦長、記入データがプロンプトどおりか） ----
for name in ['H28_dai21mon_toukishinseisho_kansei', 'H28_dai21mon_toukishinseisho_machigai']:
    png = os.path.join(HERE, 'zu', name + '.png')
    if os.path.exists(png):
        w, h = struct.unpack('>II', open(png, 'rb').read()[16:24])
        judge(f'{name}.png が縦長（{w}×{h}px）', h > w)
    else:
        judge(f'{name}.png がある', False)
html_k = open(os.path.join(HERE, 'zu', 'H28_dai21mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
html_m = open(os.path.join(HERE, 'zu', 'H28_dai21mon_toukishinseisho_machigai.html'), encoding='utf-8').read()
for s in ['平成28年○月○日　申請　Ａ地方法務局', '土地分合筆登記', '地積測量図　登記識別情報　印鑑証明書　代理権限証書',
          'Ａ市Ｂ町一丁目16番１号　甲野太郎', '金2,000円', 'Ａ市Ｂ町一丁目', '40番２', '（イ）40番２', '（ロ）', '32番１',
          '③32番１に一部合併', '40番２から分割して32番１に合併する部分', '③40番２から一部合併', '>276<', '>230<', '>46<', '>351<',
          '>398<', '>畑<', '（略）', '①地番', '②地目', '③地積　　m²', '平成28年度 土地家屋調査士試験 第21問 登記申請書 解答例']:
    check('完成形の画像（HTML）', s, html_k, '完成形画像')
judge('完成形の画像：記入行は6行（答案用紙どおり）', html_k.count('<td class="chimoku">') == 6)
judge('完成形の画像：登録免許税が申請日より上（答案用紙の順）', html_k.index('登録免許税') < html_k.index('平成28年○月○日'))
for s in ['①誤答', '②添削（赤ペン）', '③正解', '金3,000円', '金2,000円', '>397<', '>398<',
          '分合筆1件なら、分合筆後の2個で2,000円！', '351.67100＋46.4342＝398.1052 → 398',
          '平成28年度 第21問｜分合筆は1件で2,000円、合筆後の32番1は398㎡']:
    check('添削の画像（HTML）', s, html_m, '添削画像')

# ---- 表記 ----
for bad in ['PDF', '名変', '右上', '左下', '✓', '✕', 'コンクリートくい', 'くいが', '令和']:
    absent('誤記・混入・専門用語のひらがな書き', bad)
check('専門用語は問題文どおりの漢字', 'コンクリート杭')
check('問題文どおりの用語', '売払い')
check('問題文どおりの用語', '永続性のない小屋')

# ---- note向けの体裁 ----
lines = text.splitlines()
bad_speaker = [i + 1 for i, l in enumerate(lines)
               if l.rstrip() in ('**トリ先生**', '**藍子**') and (not l.endswith('  ') or not lines[i + 1].startswith('「'))]
judge(f'話者名の行（ハードブレーク）: 不備 {bad_speaker}', not bad_speaker)
same = []
for i, l in enumerate(lines):
    if l.rstrip() in ('**トリ先生**', '**藍子**'):
        j = i + 2
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines) and lines[j].rstrip() == l.rstrip():
            same.append(i + 1)
judge(f'同じ話者のセリフの連続: {same}', not same)
n_marker = len(re.findall(r'^> 【画像挿入】', text, re.M))
judge(f'画像挿入マーカー（引用形式）: {n_marker}個（解説図8＋添削1＋完成形1＝計10か所の想定）', n_marker == 10)
judge('記事の最後が区切り線', lines[-1] == '---')
title = lines[0]
prefix = '# 【土地家屋調査士受験生向け】平成28年度問題21（土地）〜'
sub = title[len(prefix):-1]
judge(f'タイトル形式（見出し{len(sub)}文字） : ' + title, title.startswith(prefix) and title.endswith('〜') and len(sub) <= 25)
check('見出し画像のサブタイトル', '〜' + sub + '〜', thumb, '見出し画像')
check('見出し画像のタイトル', '平成28年度問題21（土地）', thumb, '見出し画像')
check('見出し画像のラベル', '土地家屋調査士受験生向け', thumb, '見出し画像')
check('解説図プロンプトのタイトル', title[2:], fig, '解説図')
check('添削プロンプトのタイトル', title[2:], fix, '添削')
check('完成形プロンプトのタイトル', title[2:], form, '登記申請書')

print('NG件数:', ng)
