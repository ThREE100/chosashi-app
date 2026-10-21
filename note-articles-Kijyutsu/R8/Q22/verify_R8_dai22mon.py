"""令和8年度 第22問（建物）の記事・付属プロンプト・生成画像の照合スクリプト。

2026-10-18に自力で解き、2026-10-20にアガルートの解答例（答案用紙の再現つき）と照合した。次を確かめる。
- 解答例の答え（KAITOUREI。欄・空欄ごと）が記事・申請書のHTML・付属プロンプトにあること
- 自分の計算（敷地の辺長・面積、DタイプとEタイプの内法の床面積、登記記録76.16との検算、建物図面の距離、敷地権の割合）
- 記事に書いた計算式の値と答え
- 画像挿入マーカー26か所と zu/ のPNG26枚の対応（順番）、まとめのわな→図の対応表（TRAPS）
- 付属プロンプト・HTML の記入データが記事と同じか
- タイトル形式と note 向けの体裁（話者名の行末の半角スペース2つ、同じ話者の連続、区切り線、禁止記号、画像の中の図番）
実行: python3 note-articles-Kijyutsu/R8/Q22/verify_R8_dai22mon.py
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ZU = os.path.join(HERE, 'zu')
ART = open(os.path.join(HERE, 'note_R8_dai22mon_tatemono_kaisetsu.md'), encoding='utf-8').read()
NG = []


def ok(cond, msg):
    print(('OK  ' if cond else 'NG  ') + msg)
    if not cond:
        NG.append(msg)


def has(text, s, where='記事'):
    ok(s in text, f'{where}に「{s}」')


def trunc2(x):
    return int(round(x * 10000)) // 100 / 100


# ---- 1. 自分の計算 ----
A, B, C, D = complex(13.75, 0), complex(13.75, 17), complex(0, 17), complex(0, 0)
ok(round(abs(B - A), 4) == 17.00 and round(abs(C - B), 4) == 13.75, '辺長 AB＝17.00、BC＝13.75（複素数）')
ok(round(abs(B - A) * abs(C - B), 2) == 233.75, '敷地の面積 233.75 が登記記録の地積と一致')
d = (5.30 - 0.12) * (10.00 - 0.12 - 1.00) + (5.30 - 0.12 - 1.00 - 0.95) * 1.00
e = (2.85 - 0.12) * (10.00 - 0.12 - 1.00) + (1.75 - 0.06 - 0.06) * 1.00
wall = 0.12 * (10.00 - 0.12 - 1.00)
ok(round(d, 4) == 49.2284 and trunc2(d) == 49.22, f'Dタイプ 49.2284 → 49.22（{d:.4f}）')
ok(round(e, 4) == 25.8724 and trunc2(e) == 25.87, f'Eタイプ 25.8724 → 25.87（{e:.4f}）')
ok(round(wall, 4) == 1.0656 and trunc2(d + e + wall) == 76.16, '49.2284＋25.8724＋1.0656＝76.1664 → 76.16（登記記録と一致）')
wrong_ps = (5.30 - 0.12) * (10.00 - 0.12) - 0.88 * 0.88 - 0.83 * 0.88
ok(trunc2(wrong_ps) == 49.67, 'PSの中だけ引く誤り 49.67')
ok(round(76.16 - 49.22, 2) == 26.94, '引き算の誤り 26.94')
ok(round(0.6 + 1.0, 1) == 1.6, '北の距離 0.6＋1.0＝1.6')
ok(round(5 * 49.22 / (49.22 + 25.87), 2) == 3.28 and round(5 * 25.87 / (49.22 + 25.87), 2) == 1.72,
   '床面積の割合なら約70分の3.28・約70分の1.72')
ok(3 + 2 == 5, '規約の70分の3＋70分の2＝区分前の70分の5')

# ---- 2. 記事の数値・答え ----
for s in ['5.18×9.88＝51.1784', '51.1784－0.7744－0.7304＝49.6736', '5.18×8.88＝45.9984', '3.23×1.00＝3.2300',
          '2.73×8.88＝24.2424', '1.63×1.00＝1.6300', '49.2284＋25.8724＝75.1008', '0.12×8.88＝1.0656',
          '75.1008＋1.0656＝76.1664', '76.16－49.22＝26.94', '17.00×13.75＝233.75', '0.6＋1.0＝1.6',
          '区分建物区分登記', '建物図面、各階平面図、規約証明書、抵当権消滅承諾書、代理権限証書の5つ', '金2,000円',
          '『③6番3の702を区分』', '『6番3の701から区分』', '『③令和8年10月18日変更』', '平成12年6月17日敷地権', '70分の3', '70分の2',
          'ア＝床面積、イ＝議事録、ウ＝合意書', '建物の存する部分　7階', 'WKマンション', '①に『利用上』、②に『構造上』',
          'A市B町四丁目6番3-701号', '構造上の独立性', '利用上の独立性', '約70分の3.28', '約70分の1.72']:
    has(ART, s)
for s, v in [('51.1784', (5.30 - 0.12) * (10.00 - 0.12)), ('45.9984', 5.18 * 8.88), ('24.2424', 2.73 * 8.88),
             ('49.6736', wrong_ps)]:
    ok(abs(float(s) - v) < 0.00005, f'計算 {s}')
# 電卓のキー列（文中）の表示
ok('[Abs] [ALPHA] [B] [－] [ALPHA] [A] [)] [＝] で表示17' in ART and abs(B - A) == 17, '電卓 Abs(B−A) 表示17')
ok('[Abs] [ALPHA] [C] [－] [ALPHA] [B] [)] [＝] で表示13.75' in ART and abs(C - B) == 13.75, '電卓 Abs(C−B) 表示13.75')

# ---- 2-2. アガルートの解答例（答案用紙の再現つき、2ページ）の答え ----
KAITOUREI = {
    '第1欄①': '利用上', '第1欄②': '構造上',
    '登記の目的': '区分建物区分登記',
    '添付書類': ['規約証明書', '建物図面', '各階平面図', '抵当権消滅承諾書', '代理権限証書'],
    '申請人': 'A市B町四丁目6番3－701号　白石恵', '登録免許税': '金2,000円', '一棟の建物の名称': 'WKマンション',
    '（イ）床面積': '49.22', '（イ）原因': '③6番3の702を区分',
    '（ロ）家屋番号': 'B町四丁目6番3の702', '（ロ）種類': '居宅', '（ロ）構造': '鉄筋コンクリート造1階建',
    '（ロ）床面積': '25.87', '（ロ）原因': '6番3の701から区分',
    '敷地権（イ）': ('1', '所有権', '70分の3', '③令和8年10月18日変更'),
    '敷地権（ロ）': ('1', '所有権', '70分の2', '平成12年6月17日敷地権'),
    '第4欄': ('床面積', '議事録', '合意書'),
    '各階平面図': ['5.18', '8.88', '0.95', '1.00', '3.23', '49.2284', '49.22'],
    '建物図面': '建物の存する部分　7階',
}
HT0 = open(os.path.join(ZU, 'R8_dai22mon_toukishinseisho_kansei.html'), encoding='utf-8').read().replace('<br>', '')
HT0 = re.sub(r'<[^>]+>', '', HT0).replace('7階部分', '').replace('（略）', '')
HT0 = HT0.replace('4922', '49.22').replace('2587', '25.87')
for key, v in KAITOUREI.items():
    vals = v if isinstance(v, (list, tuple)) else [v]
    for x in vals:
        if key.startswith('第1欄'):
            src = open(os.path.join(ZU, 'R8_dai22mon_dai1ran_kansei.html'), encoding='utf-8').read()
        elif key == '第4欄':
            src = open(os.path.join(ZU, 'R8_dai22mon_dai4ran_kansei.html'), encoding='utf-8').read()
        elif key in ('各階平面図', '建物図面'):
            src = ART
        else:
            src = HT0
        x2 = x.replace('B町四丁目6番3の702', 'B町四丁目6番3の702').replace('鉄筋コンクリート造1階建', '鉄筋コンクリート造1階建')
        ok(x2 in src or x2.replace('.', '') in src.replace('</span><span class="ink">', ''), f'解答例 {key}：{x}')
ok(abs((0.95 * 8.88 + 3.23 * 9.88 + 1.00 * 8.88) - 49.2284) < 1e-9, '解答例の求積（0.95×8.88＋3.23×9.88＋1.00×8.88）も49.2284')

# ---- 3. マーカーとPNG ----
ORDER = ['zu01_kubun_bunkatsu', 'zu02_jikeiretsu', 'zu03_chuu_shiwake', 'zu04_dokuritsusei', 'dai1ran_kansei',
         'zu05_shikichi_henchou', 'zu06_ittensasen', 'zu07_kita_kyori', 'zu08_tatemono_zumen_kisai',
         'zu09_tatemono_zumen_kansei', 'zu10_ps_ayamari',
         'zu11_D_kyuuseki', 'zu12_E_kyuuseki', 'zu13_kensan', 'zu14_kakukai_heimenzu',
         'toukishinseisho_machigai_shinseinin', 'toukishinseisho_machigai_tenpu', 'zu15_teitouken',
         'toukishinseisho_machigai_menkyo', 'toukishinseisho_machigai_genin', 'toukishinseisho_machigai_shikichiken',
         'zu16_wariai', 'toukishinseisho_kansei', 'zu17_kiyaku_shoumei', 'dai4ran_kansei', 'zu18_toku_junban']
KEY = ['区分と分割', '時系列メモ', '注の仕分け', '二つの独立性', '第1欄（問1）', '本件土地（6番3）の辺長確認図', '一点鎖線の比較', '北の距離の図',
       '建物図面に書くもの・書かないものの説明図', '建物図面の記入の完成形', 'PSの欠けの誤り', 'Dタイプ（701）7階部分の求積図', 'Eタイプ（702）7階部分の求積図', '合計の検算',
       '各階平面図の完成形', '申請人の欄の添削', '添付書類の欄の添削', '抵当権の行方', '登録免許税の欄の添削',
       '区分した建物の表示の原因の添削', '敷地権の表示の原因の添削', '敷地権の割合の図', '登記申請書の完成形', '規約証明書の図',
       '第4欄（問4）', '本番で解く順番']
marks = re.findall(r'^> 【画像挿入】(.+)$', ART, flags=re.M)
pngs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ZU, 'R8_dai22mon_*.png')))
ok(len(marks) == len(ORDER) == len(KEY) == len(pngs) == 26, f'マーカー{len(marks)}か所・PNG{len(pngs)}枚・一覧26')
for i, (m, k, o) in enumerate(zip(marks, KEY, ORDER)):
    ok(m.startswith(k), f'マーカー{i + 1}「{k}」→ {o}')
    ok(f'R8_dai22mon_{o}.png' in pngs, f'PNG R8_dai22mon_{o}.png がある')
# まとめのわな → 図（1項目1わな、図の重複なし）
TRAPS = [('建物分割登記ではなく、区分建物区分登記', 'zu01_kubun_bunkatsu'),
         ('行き来できないことは構造上の独立性の話', 'zu04_dokuritsusei'),
         ('一棟の7階を一点鎖線で描く', 'zu06_ittensasen'),
         ('0.6＋1.0＝1.6', 'zu07_kita_kyori'),
         ('囲む壁ごと除く', 'zu10_ps_ayamari'),
         ('引き算で出さず、自分で測る', 'zu13_kensan'),
         ('安田結さんはまだ名義人ではない', 'toukishinseisho_machigai_shinseinin'),
         ('登記識別情報・印鑑証明書は要らない', 'toukishinseisho_machigai_tenpu'),
         ('抵当権消滅承諾書を付ける', 'zu15_teitouken'),
         ('「不要」ではない', 'toukishinseisho_machigai_menkyo'),
         ('702の行だけが', 'toukishinseisho_machigai_genin'),
         ('『③令和8年10月18日変更』', 'toukishinseisho_machigai_shikichiken'),
         ('規約で定めた70分の3・70分の2', 'zu16_wariai'),
         ('公正証書は分譲前の分譲業者のもの', 'zu17_kiyaku_shoumei')]
matome = ART[ART.index('「最後にまとめます！'):]
items = re.findall(r'^- (.+)$', matome, flags=re.M)
ok(len(items) == len(TRAPS), f'まとめのわな{len(items)}項目＝対応表{len(TRAPS)}')
ok(len({t for _, t in TRAPS}) == len(TRAPS), 'わな→図に重複なし')
for s, fig in TRAPS:
    ok(any(s in it for it in items) and fig in ORDER, f'わな「{s}」→ {fig}')

# ---- 4. 付属プロンプト・HTML ----
P = {n: open(os.path.join(HERE, f'prompt_R8_dai22mon_{n}.md'), encoding='utf-8').read()
     for n in ['kaisetsuzu', 'toukishinseisho_gazou', 'toukishinseisho_machigai', 'miidashi_gazou']}
for s in ['区分建物区分登記', '金2,000円', '7階部分　49.22', '7階部分　25.87', '7階部分　76.16', '③6番3の702を区分',
          '6番3の701から区分', '③令和8年10月18日変更', '平成12年6月17日敷地権', '70分の3', '70分の2', '床面積', '議事録', '合意書',
          '（略）', '利用上', '構造上']:
    has(P['toukishinseisho_gazou'], s, '申請書プロンプト')
for s in ['49.2284', '25.8724', '1.0656', '76.1664', '北1.6', '西0.8', '書き足さない', '図番を書かない']:
    has(P['kaisetsuzu'], s, '解説図プロンプト')
for s in ['安田結', '抵当権消滅承諾書', '金2,000円', '③6番3の702を区分', '③令和8年10月18日変更', '平成12年6月17日敷地権']:
    has(P['toukishinseisho_machigai'], s, '添削プロンプト')
HT = open(os.path.join(ZU, 'R8_dai22mon_toukishinseisho_kansei.html'), encoding='utf-8').read()
for s in ['区分建物区分登記', '抵当権消滅承諾書', '金2,000円', 'WKマンション', '233', '49', '22', '25', '87',
          '③6番3の<br>702を区分', '6番3の701<br>から区分', '③令和8年10月18日変更', '平成12年6月17日敷地権', '70分の3', '70分の2', '白石恵',
          '〇〇地方法務局〇〇支局', '（略）', '70分の5']:
    has(HT, s, '申請書HTML')
for n in ['dai1ran_kansei', 'dai4ran_kansei']:
    h = open(os.path.join(ZU, f'R8_dai22mon_{n}.html'), encoding='utf-8').read()
    ok('第1欄' in h or '第4欄' in h, f'{n} の見出し')
has(open(os.path.join(ZU, 'R8_dai22mon_dai4ran_kansei.html'), encoding='utf-8').read(), '合意書', '第4欄HTML')

# ---- 5. タイトル・体裁 ----
title = ART.splitlines()[0]
m = re.match(r'^# 【土地家屋調査士受験生向け】令和8年度問題22（建物）〜(.+)〜$', title)
ok(bool(m) and len(m.group(1)) <= 25, 'タイトル形式・見出し25字以内')
has(P['miidashi_gazou'], m.group(1) if m else '???', '見出し画像プロンプト')
lines = ART.splitlines()
spk = [ln for ln in lines if re.match(r'^\*\*(トリ先生|藍子)\*\*\s*$', ln)]
ok(all(ln.endswith('  ') and ln.rstrip() in ('**トリ先生**', '**藍子**') for ln in spk), '話者名の行末に半角スペース2つ')
seq = [ln.strip() for ln in spk]
ok(all(a != b for a, b in zip(seq, seq[1:])), '同じ話者のセリフが続かない（マーカー・箇条書きをはさんでも）')
ok(lines[-1].strip() == '---', '記事の最後に区切り線')
ok(not re.search('[✕✓×]{0}'.format('') + '[✕✓]', ART), '記号（✕・✓）を使っていない')
ok(ART.splitlines()[2] == '※本記事の数値は、アガルートアカデミーの解答例と照合済みです。', '冒頭の照合済みの一文')
ok('書面による合意です' not in ART and '702に区分』' not in ART.split('添削画像')[0][-1] , '古い答えが残っていない')
ok('図の（注）' in ART and '問題文の注' in ART, '注を「問題文の注」「図の（注）」と書き分け')
src = open(os.path.join(ZU, 'draw_R8_dai22mon_kaisetsuzu.py'), encoding='utf-8').read()
titles = re.findall(r"(?:fixed_figure|new_figure|frame_fig)\('([^']+)'", src) + re.findall(r"suptitle\('([^']+)'", src)
ok(titles and not any(re.search(r'図\s*\d', t) for t in titles), f'画像のタイトルに図番がない（{len(titles)}枚）')

print('\nNG', len(NG), '件')
