"""夜の計算ドリルの解答に付ける「電卓操作」（キヤノン F-789SG・複素数モード）を作る。
キー列は note-articles-Kijyutsu/tools/keysim_note_article.py でそのまま実行し、表示を再現する（変数の使い回しも記事の順に再現）。
使う変数は A〜F・X・Y（点名とぶつかるので、各問の最初に割り当てを書く）。
使い方: python3 daily-drill/evening/calc_keys.py   （PM-01・04・07 の json に 'keys' を書き足す）"""
import json
import math
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'note-articles-Kijyutsu', 'tools'))
from keysim_note_article import simulate  # noqa: E402

PROB = os.path.join(HERE, 'problems')


def num(v):
    s = f'{v:.4f}'.rstrip('0').rstrip('.')
    return s


def sn(v):
    """符号つきの数の入力：負の数は「(0 − x)」と引き算で入れる（符号のキーは使わない）"""
    return num(v) if v >= 0 else f'[(] 0 [−] {num(-v)} [)]'


def cx(x, y):
    """複素数の入力キー： 541.02 [+] 400.35 [i]（Yが負のときは [−]）"""
    return f'{num(x)} [+] {num(y)} [i]' if y >= 0 else f'{num(x)} [−] {num(-y)} [i]'


def ang_s(a):
    return f'{a[0]}°{a[1]:02d}′{a[2]:02d}″'


def dms_keys(a):
    return f'{a[0]} [°′″] {a[1]} [°′″] {a[2]} [°′″]'


class Doc:
    """手順を並べ、キー列を実行して表示を得る。steps: {title, formula, keys, ans?}"""
    def __init__(self):
        self.steps = []

    def add(self, title, formula, keys, show=True, note=''):
        self.steps.append({'title': title, 'formula': formula, 'keys': keys, 'show': show, 'note': note})

    def md(self):
        out = []
        for s in self.steps:
            out.append('```\n' + s['keys'] + '\n```\n')
            if s['show']:
                out.append('表示：（再現）\n')
        return '\n'.join(out)

    def run(self):
        fd, tmp = tempfile.mkstemp(suffix='.md', prefix='keys_')   # 同時に動いても衝突しないよう、毎回別のファイル
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(self.md())
        try:
            res = simulate(tmp)
        finally:
            os.remove(tmp)
        it = iter(res)
        for s in self.steps:
            if s['show']:
                _, _, got, _ = next(it)
                s['display'] = got
        return self.steps


def val(s, k=0):
    """表示文字列から k 番目の数（実部=0 / 虚部の係数=1）を取り出す"""
    t = s['display'].replace('（実部）', '0').replace('…', '').replace('−', '-').replace('＋', '+').replace(' ', '')
    m = re.match(r'^(-?[0-9.]+)?([+-][0-9.]+)i$', t)
    if m:
        return float(m.group(2)) if k else float(m.group(1) or 0)
    m = re.match(r'^(-?[0-9.]+)i$', t)
    if m:
        return float(m.group(1)) if k else 0.0
    return float(t)


def r2(v):
    return round(v + 1e-9, 2)


def pm01(p):
    v = p['verify']
    T1, T2, K1, K2, S, M = (v[k] for k in ('T1', 'T2', 'K1', 'K2', 'S', 'M'))
    d = Doc()
    d.add('割り当て', 'Y＝T1（器械点）、X＝T2（後視点）', f'{cx(*T1)} [SHIFT] [STO] [Y]\n{cx(*T2)} [SHIFT] [STO] [X]', show=False)
    for nm in 'PQ':
        o = v['obs'][nm]
        d.add(f'点{nm}（放射）', f'{nm} ＝ T1 ＋ {o["dist"]:.2f}∠( arg(T2 − T1) ＋ {o["angle"][0]}°{o["angle"][1]:02d}′{o["angle"][2]:02d}″ )',
              f'[ALPHA] [Y] [+] {num(o["dist"])} [∠] [(] [Apps] [3] [ALPHA] [X] [−] [ALPHA] [Y] [)] [+] {dms_keys(o["angle"])} [)] [=]')
    d.run()
    P_, Q_ = (d.steps[1], d.steps[2])
    Pxy = (r2(val(P_)), r2(val(P_, 1)))
    Qxy = (r2(val(Q_)), r2(val(Q_, 1)))
    # R：直線K1K2と直線SMの交点（A＝K1、B＝K2、C＝S、D＝M）
    d2 = Doc()
    d2.add('割り当て', 'A＝K1、B＝K2、C＝S、D＝M', f'{cx(*K1)} [SHIFT] [STO] [A]\n{cx(*K2)} [SHIFT] [STO] [B]\n{cx(*S)} [SHIFT] [STO] [C]\n{cx(*M)} [SHIFT] [STO] [D]', show=False)
    d2.add('分子（iの係数）', 'Conjg(S − K1) × (M − S)', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
    d2.add('分母（iの係数）', 'Conjg(K2 − K1) × (M − S)', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
    d2.run()
    n_, de_ = val(d2.steps[1], 1), val(d2.steps[2], 1)
    d2.add('点R', 'R ＝ K1 ＋ (K2 − K1) × 分子 ÷ 分母', f'[ALPHA] [A] [+] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {sn(n_)} [÷] {sn(de_)} [=]')
    d2.run()
    R_ = d2.steps[-1]
    Rxy = (r2(val(R_)), r2(val(R_, 1)))
    # 面積：A＝P、B＝Q、C＝R、D＝S（丸めた座標）
    d3 = Doc()
    d3.add('割り当て（丸めた座標）', 'A＝P、B＝Q、C＝R、D＝S', f'{cx(*Pxy)} [SHIFT] [STO] [A]\n{cx(*Qxy)} [SHIFT] [STO] [B]\n{cx(*Rxy)} [SHIFT] [STO] [C]\n{cx(*S)} [SHIFT] [STO] [D]', show=False)
    d3.add('面積（倍面積）', 'Conjg(R − P) × (S − Q)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [B] [)] [=]')
    d3.run()
    area = abs(val(d3.steps[1], 1)) / 2
    return [('点P・点Q（器械点T1から放射）', d.steps), ('点R（2直線の交点）', d2.steps), ('地積（座標法）', d3.steps)], {'P': Pxy, 'Q': Qxy, 'R': Rxy, 'area': math.floor(area * 100 + 1e-9) / 100}


def pm04(p):
    v = p['verify']
    Ap, B, C, D, E, F, K = (v[k] for k in 'ABCDEFK')
    d = Doc()
    d.add('割り当て', 'A＝A、B＝B、C＝C、D＝D、E＝E、F＝F、Y＝K（Xは A′ に使う）',
          '\n'.join(f'{cx(*pt)} [SHIFT] [STO] [{nm}]' for pt, nm in ((Ap, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (K, 'Y'))), show=False)
    d.add('A′（ABを東へ1.20m、直角に）', 'A′ ＝ A ＋ 1.20 × (−i) × (B − A) ÷ Abs(B − A)　（ABはほぼ南北なので、−i倍が東向き）',
          '[ALPHA] [A] [+] 1.2 [×] [(] 0 [−] 1 [i] [)] [×] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [÷] [Abs] [ALPHA] [B] [−] [ALPHA] [A] [)] [=]\n[SHIFT] [STO] [X]')
    d.add('点Hの分子', 'Conjg(C − A′) × (D − C)　のiの係数', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [X] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
    d.add('点Hの分母', 'Conjg(B − A) × (D − C)　のiの係数', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
    d.run()
    s = d.steps
    tn, td = val(s[2], 1), val(s[3], 1)
    d.add('点H', 'H ＝ A′ ＋ (B − A) × 分子 ÷ 分母', f'[ALPHA] [X] [+] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {sn(tn)} [÷] {sn(td)} [=]')
    d.run()
    Hxy = (r2(val(s[-1])), r2(val(s[-1], 1)))
    d.add('Hを記憶（Cに上書き）', '', f'{cx(*Hxy)} [SHIFT] [STO] [C]', show=False)
    d.add('点Iの分子', 'Conjg(E − A′) × (F − E)　のiの係数', '[Apps] [4] [ALPHA] [E] [−] [ALPHA] [X] [)] [×] [(] [ALPHA] [F] [−] [ALPHA] [E] [)] [=]')
    d.add('点Iの分母', 'Conjg(B − A) × (F − E)　のiの係数', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [F] [−] [ALPHA] [E] [)] [=]')
    d.run()
    s = d.steps
    tn2, td2 = val(s[-2], 1), val(s[-1], 1)
    d.add('点I', 'I ＝ A′ ＋ (B − A) × 分子 ÷ 分母', f'[ALPHA] [X] [+] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {sn(tn2)} [÷] {sn(td2)} [=]')
    d.run()
    Ixy = (r2(val(s[-1])), r2(val(s[-1], 1)))
    d.add('Iを記憶（Dに上書き）', '', f'{cx(*Ixy)} [SHIFT] [STO] [D]', show=False)
    d.add('w（Kの、HからIへの割合）', 'w ＝ (K − H) ÷ (I − H)', '[(] [ALPHA] [Y] [−] [ALPHA] [C] [)] [÷] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]\n[SHIFT] [STO] [A]')
    d.add('点J（垂線の足）', 'J ＝ H ＋ (I − H) × (w ＋ Conjg(w)) ÷ 2', '[ALPHA] [C] [+] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [×] [(] [ALPHA] [A] [+] [Apps] [4] [ALPHA] [A] [)] [)] [÷] 2 [=]')
    d.run()
    Jxy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('Jを記憶（Bに上書き）', '', f'{cx(*Jxy)} [SHIFT] [STO] [B]', show=False)
    d.add('KからJまでの距離', 'Abs(K − J)', '[Abs] [ALPHA] [Y] [−] [ALPHA] [B] [)] [=]')
    d.run()
    dist = round(val(d.steps[-1]) + 1e-9, 2)
    return [('点H・点I・点J・距離', d.steps)], {'H': Hxy, 'I': Ixy, 'J': Jxy, 'dist': dist}


def pm07(p):
    v = p['verify']
    A, B, C, D = (v[k] for k in 'ABCD')
    d = Doc()
    d.add('割り当て', 'A＝A、B＝B、C＝C、D＝D', '\n'.join(f'{cx(*pt)} [SHIFT] [STO] [{nm}]' for pt, nm in ((A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'))), show=False)
    d.add('点E（ADの向きにAから9.50m）', 'E ＝ A ＋ (D − A) ÷ Abs(D − A) × 9.50', f'[ALPHA] [A] [+] [(] [ALPHA] [D] [−] [ALPHA] [A] [)] [÷] [Abs] [ALPHA] [D] [−] [ALPHA] [A] [)] [×] {num(v["d_AE"])} [=]')
    d.run()
    Exy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('Eを記憶（Xに）', '', f'{cx(*Exy)} [SHIFT] [STO] [X]', show=False)
    d.add('倍面積 p（t＝0のとき）', 'Conjg(B − A) × (E − B)　のiの係数（四角形ABFEの倍面積はF＝Bのとき）', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [X] [−] [ALPHA] [B] [)] [=]')
    d.add('倍面積の増え方 q', 'Conjg(C − B) × (E − B)　のiの係数（Fが B→C へ t 進むと倍面積は p ＋ t × q）', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [B] [)] [×] [(] [ALPHA] [X] [−] [ALPHA] [B] [)] [=]')
    d.run()
    pc, qc = val(d.steps[-2], 1), val(d.steps[-1], 1)
    sg = 1 if pc > 0 else -1
    tgt = sg * 2 * v['target']
    d.add('t（倍面積が 2×280.00 になる位置）', f't ＝ ({num(tgt)} − p) ÷ q　（pの符号に合わせて ±560.00）', f'[(] {sn(tgt)} [−] {sn(pc)} [)] [÷] {sn(qc)} [=]')
    d.run()
    t = val(d.steps[-1])
    d.add('点F', 'F ＝ B ＋ (C − B) × t', f'[ALPHA] [B] [+] [(] [ALPHA] [C] [−] [ALPHA] [B] [)] [×] {sn(t)} [=]')
    d.run()
    Fxy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('Fを記憶（Yに）', '', f'{cx(*Fxy)} [SHIFT] [STO] [Y]', show=False)
    d.add('検算：四角形ABFEの倍面積', 'Conjg(F − A) × (E − B)　のiの係数 ÷ 2 ≒ 280.00', '[Apps] [4] [ALPHA] [Y] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [X] [−] [ALPHA] [B] [)] [=]')
    d.add('分筆前の倍面積', 'Conjg(C − A) × (D − B)　のiの係数 ÷ 2 ＝ 分筆前の面積', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [B] [)] [=]')
    d.add('分筆線EFの長さ', 'Abs(F − E)', '[Abs] [ALPHA] [Y] [−] [ALPHA] [X] [)] [=]')
    d.run()
    s = d.steps
    tot = abs(val(s[-2], 1)) / 2
    return [('点E・点F・（ロ）の地積・EFの長さ', d.steps)], {'E': Exy, 'F': Fxy, 'ro': round(math.floor(tot * 100 + 1e-9) / 100 - v['target'], 2), 'ef': round(val(s[-1]) + 1e-9, 2), 'tot': tot, 'check': abs(val(s[-3], 1)) / 2}


def pm08(p):
    v = p['verify']
    T1, T2, A, B, K1, K2, S = (v[k] for k in ('T1', 'T2', 'A', 'B', 'K1', 'K2', 'S'))
    o = v['obs']['C']
    reg = v['reg']
    d = Doc()
    d.add('割り当て', 'Y＝T1（器械点）、X＝T2（後視点）', f'{cx(*T1)} [SHIFT] [STO] [Y]\n{cx(*T2)} [SHIFT] [STO] [X]', show=False)
    d.add('点C（放射）', f'C ＝ T1 ＋ {o["dist"]:.2f}∠( arg(T2 − T1) ＋ {o["angle"][0]}°{o["angle"][1]:02d}′{o["angle"][2]:02d}″ )',
          f'[ALPHA] [Y] [+] {num(o["dist"])} [∠] [(] [Apps] [3] [ALPHA] [X] [−] [ALPHA] [Y] [)] [+] {dms_keys(o["angle"])} [)] [=]')
    d.run()
    Cxy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('割り当て（以後）', 'A＝K1、B＝K2、C＝C、D＝S、X＝A点、Y＝B点（Cは丸めた座標）',
          f'{cx(*K1)} [SHIFT] [STO] [A]\n{cx(*K2)} [SHIFT] [STO] [B]\n{cx(*Cxy)} [SHIFT] [STO] [C]\n{cx(*S)} [SHIFT] [STO] [D]\n{cx(*A)} [SHIFT] [STO] [X]\n{cx(*B)} [SHIFT] [STO] [Y]', show=False)
    d.add('点Dの分子', 'Conjg(C − K1) × (S − C)　のiの係数', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
    d.add('点Dの分母', 'Conjg(K2 − K1) × (S − C)　のiの係数', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [C] [)] [=]')
    d.run()
    tn, td = val(d.steps[-2], 1), val(d.steps[-1], 1)
    d.add('点D', 'D ＝ K1 ＋ (K2 − K1) × 分子 ÷ 分母', f'[ALPHA] [A] [+] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {sn(tn)} [÷] {sn(td)} [=]')
    d.run()
    Dxy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('Dを記憶（Eに）', '', f'{cx(*Dxy)} [SHIFT] [STO] [E]', show=False)
    d.add('点E（ABの向きにAから7.60m）', 'E ＝ A ＋ (B − A) ÷ Abs(B − A) × 7.60', f'[ALPHA] [X] [+] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [÷] [Abs] [ALPHA] [Y] [−] [ALPHA] [X] [)] [×] {num(v["d_AE"])} [=]')
    d.run()
    Exy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('点F（DCの向きにDから7.10m）', 'F ＝ D ＋ (C − D) ÷ Abs(C − D) × 7.10', f'[ALPHA] [E] [+] [(] [ALPHA] [C] [−] [ALPHA] [E] [)] [÷] [Abs] [ALPHA] [C] [−] [ALPHA] [E] [)] [×] {num(v["d_DF"])} [=]')
    d.run()
    Fxy = (r2(val(d.steps[-1])), r2(val(d.steps[-1], 1)))
    d.add('E・Fを記憶（A・Bに上書き）', 'A＝E点、B＝F点（以後、Dは E の変数、A点はX、B点はY）', f'{cx(*Exy)} [SHIFT] [STO] [A]\n{cx(*Fxy)} [SHIFT] [STO] [B]', show=False)
    d.add('（イ）の倍面積', '四角形A・E・F・D：Conjg(F − A) × (D − E)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [B] [−] [ALPHA] [X] [)] [×] [(] [ALPHA] [E] [−] [ALPHA] [A] [)] [=]')
    d.add('（ロ）の倍面積', '四角形E・B・C・F：Conjg(C − E) × (F − B)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [B] [−] [ALPHA] [Y] [)] [=]')
    d.run()
    ai = math.floor(abs(val(d.steps[-2], 1)) / 2 * 100 + 1e-9) / 100
    ar = math.floor(abs(val(d.steps[-1], 1)) / 2 * 100 + 1e-9) / 100
    d.add('分筆後の合計と登記記録の差', '（イ）＋（ロ）− 登記記録の地積', f'[(] {num(ai)} [+] {num(ar)} [−] {num(reg)} [)] [=]')
    d.add('誤差の限度（甲2）', '(0.05 ＋ 0.01 × ⁴√F) × √F　（F＝登記記録の地積。表の値は小数第2位未満切捨て）',
          f'[(] 0.05 [+] 0.01 [×] [√] [(] [√] [(] {num(reg)} [)] [)] [)] [×] [√] [(] {num(reg)} [)] [=]')
    d.run()
    diff = round(val(d.steps[-2]) + 1e-9, 2)
    kk = math.floor(val(d.steps[-1]) * 100 + 1e-9) / 100
    return [('点C（放射）', d.steps[:2]), ('点D・E・F・（イ）（ロ）・差と誤差の限度', d.steps[2:])], {'C': Cxy, 'D': Dxy, 'E': Exy, 'F': Fxy, 'ai': ai, 'ar': ar, 'diff': diff, 'kk': kk}


def pm09(p):
    v = p['verify']
    pts = v['pts']
    d = Doc()
    d.add('割り当て', 'A〜F＝点A〜F（変数A〜Fにそのまま入れる）', '\n'.join(f'{cx(*pts[n])} [SHIFT] [STO] [{n}]' for n in 'ABCDEF'), show=False)
    L = {}
    for u, w in (('A', 'B'), ('B', 'F'), ('F', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('E', 'F')):
        d.add(f'辺{u}{w}', f'Abs({u} − {w})', f'[Abs] [ALPHA] [{u}] [−] [ALPHA] [{w}] [)] [=]')
    d.add('12番1の倍面積', '四角形A・B・F・E：Conjg(F − A) × (E − B)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [F] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [E] [−] [ALPHA] [B] [)] [=]')
    d.add('12番2の倍面積', '四角形E・F・C・D：Conjg(C − E) × (D − F)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [E] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [F] [)] [=]')
    d.run()
    st = d.steps
    lens = [round(val(s) + 1e-9, 2) for s in st[1:8]]
    a1 = math.floor(abs(val(st[8], 1)) / 2 * 100 + 1e-9) / 100
    a2 = math.floor(abs(val(st[9], 1)) / 2 * 100 + 1e-9) / 100
    return [('辺長7つと地積2つ', st)], {'lens': lens, 'a1': a1, 'a2': a2}


def pm10(p):
    d = Doc()
    d.add('1階の床面積', '9.10 × 6.37 ＋ 2.73 × 1.82（普通の四則計算）', '9.1 [×] 6.37 [+] 2.73 [×] 1.82 [=]')
    d.add('2階の床面積', '9.10 × 4.55', '9.1 [×] 4.55 [=]')
    d.add('北東の角から北側の筆界まで', '417.00 − (400.00 ＋ 3.50 ＋ 8.19)', '417 [−] [(] 400 [+] 3.5 [+] 8.19 [)] [=]')
    d.add('北東の角から東側の筆界まで', '320.00 − (300.00 ＋ 4.00 ＋ 9.10)', '320 [−] [(] 300 [+] 4 [+] 9.1 [)] [=]')
    d.run()
    st = d.steps
    return [('床面積と距離（普通の四則計算）', st)], {'f1': math.floor(val(st[0]) * 100 + 1e-9) / 100, 'f2': math.floor(val(st[1]) * 100 + 1e-9) / 100, 'dn': round(val(st[2]) + 1e-9, 2), 'de': round(val(st[3]) + 1e-9, 2)}


def cxs(x, y):
    """負の実部にも対応した複素数の入力キー"""
    return f'{sn(x)} [+] {num(y)} [i]' if y >= 0 else f'{sn(x)} [−] {num(-y)} [i]'


def xy(st):
    return (r2(val(st)), r2(val(st, 1)))


def pm82(p):
    v = p['verify']
    d = Doc()
    d.add('割り当て', 'A＝A、D＝D（平面直角座標）、X＝A′、Y＝D′、B＝B′、C＝C′（任意の座標）',
          '\n'.join(f'{cx(*v[k])} [SHIFT] [STO] [{m}]' for k, m in (('A', 'A'), ('D', 'D'), ('Aa', 'X'), ('Da', 'Y'), ('Ba', 'B'), ('Ca', 'C'))), show=False)
    d.add('比 k（Eに記憶）', 'k ＝ (D − A) ÷ (D′ − A′)', '[(] [ALPHA] [D] [−] [ALPHA] [A] [)] [÷] [(] [ALPHA] [Y] [−] [ALPHA] [X] [)] [=] [SHIFT] [STO] [E]')
    d.add('比の大きさ', 'Abs(k)（1に近いことを確かめる）', '[Abs] [ALPHA] [E] [)] [=]')
    d.add('点B', 'B ＝ A ＋ (B′ − A′) × k', '[ALPHA] [A] [+] [(] [ALPHA] [B] [−] [ALPHA] [X] [)] [×] [ALPHA] [E] [=]')
    d.add('点C', 'C ＝ A ＋ (C′ − A′) × k', '[ALPHA] [A] [+] [(] [ALPHA] [C] [−] [ALPHA] [X] [)] [×] [ALPHA] [E] [=]')
    d.run()
    B, C = xy(d.steps[3]), xy(d.steps[4])
    d.add('B・Cを記憶（丸めた座標）', 'B＝点B、C＝点C', f'{cx(*B)} [SHIFT] [STO] [B]\n{cx(*C)} [SHIFT] [STO] [C]', show=False)
    d.add('辺BC', 'Abs(C − B)', '[Abs] [ALPHA] [C] [−] [ALPHA] [B] [)] [=]')
    d.add('地積（倍面積）', '四角形A・B・C・D：Conjg(C − A) × (D − B)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [D] [−] [ALPHA] [B] [)] [=]')
    d.run()
    bc = round(val(d.steps[-2]) + 1e-9, 2)
    area = math.floor(abs(val(d.steps[-1], 1)) / 2 * 100 + 1e-9) / 100
    return [('座標の変換（共通点A・D）', d.steps[:5]), ('辺BCと地積', d.steps[5:])], {'点B': B, '点C': C, '辺BC': bc, '本件土地の地積': area}


def pm83(p):
    v = p['verify']
    o = v['obs']
    T3 = v['T3']
    d = Doc()
    d.add('割り当て', 'X＝T1、Y＝T2、A＝T3', f'{cx(*v["T1"])} [SHIFT] [STO] [X]\n{cx(*v["T2"])} [SHIFT] [STO] [Y]\n{cx(*T3)} [SHIFT] [STO] [A]', show=False)
    a = o['T101']
    d.add('T101′（補正前）', f'T101′ ＝ T2 ＋ {a["dist"]:.2f}∠( arg(T1 − T2) ＋ {ang_s(a["angle"])} )',
          f'[ALPHA] [Y] [+] {num(a["dist"])} [∠] [(] [Apps] [3] [ALPHA] [X] [−] [ALPHA] [Y] [)] [+] {dms_keys(a["angle"])} [)] [=]')
    d.run()
    T1p = xy(d.steps[1])
    b = o['T3']
    d.add('T101′を記憶', 'B＝T101′（丸めた座標）', f'{cx(*T1p)} [SHIFT] [STO] [B]', show=False)
    d.add('T3′', f'T3′ ＝ T101′ ＋ {b["dist"]:.2f}∠( arg(T2 − T101′) ＋ {ang_s(b["angle"])} )',
          f'[ALPHA] [B] [+] {num(b["dist"])} [∠] [(] [Apps] [3] [ALPHA] [Y] [−] [ALPHA] [B] [)] [+] {dms_keys(b["angle"])} [)] [=]')
    d.run()
    T3p = xy(d.steps[3])
    d.add('補正量', 'T3 − T3′', f'[ALPHA] [A] [−] [(] {cx(*T3p)} [)] [=]')
    d.run()
    cr = xy(d.steps[4])
    L = a['dist'] + b['dist']
    d.add('T101（補正後）', f'T101 ＝ T101′ ＋ 補正量 × {a["dist"]:.2f} ÷ ( {a["dist"]:.2f} ＋ {b["dist"]:.2f} )',
          f'[ALPHA] [B] [+] [(] {cxs(*cr)} [)] [×] {num(a["dist"])} [÷] [(] {num(a["dist"])} [+] {num(b["dist"])} [)] [=]')
    d.run()
    T101 = xy(d.steps[5])
    d.add('T101を記憶', 'C＝T101（丸めた座標）', f'{cx(*T101)} [SHIFT] [STO] [C]', show=False)
    got = {'点T3′': T3p, '補正量': cr, '点T101': T101}
    for nm in 'PQ':
        q = o[nm]
        d.add(f'点{nm}（放射）', f'{nm} ＝ T101 ＋ {q["dist"]:.2f}∠( arg(T2 − T101) ＋ {ang_s(q["angle"])} )',
              f'[ALPHA] [C] [+] {num(q["dist"])} [∠] [(] [Apps] [3] [ALPHA] [Y] [−] [ALPHA] [C] [)] [+] {dms_keys(q["angle"])} [)] [=]')
    d.run()
    got['点P'], got['点Q'] = xy(d.steps[-2]), xy(d.steps[-1])
    return [('結合トラバース（T2→T101→T3）とコンパスの法則', d.steps[:7]), ('補正したT101から点P・Q', d.steps[7:])], got


def pm84(p):
    v = p['verify']
    ox, oy = v['off']
    sh = lambda k: (round(v[k][0] - ox, 2), round(v[k][1] - oy, 2))
    o = v['obs']
    d = Doc()
    d.add('割り当て（ずらした座標）', 'Y＝T1、X＝T2（元の座標から −38500.00 ＋ 22700.00i を引いた値）', f'{cx(*sh("T1"))} [SHIFT] [STO] [Y]\n{cx(*sh("T2"))} [SHIFT] [STO] [X]', show=False)
    for nm in 'PQ':
        q = o[nm]
        d.add(f'点{nm}（放射・ずらした座標）', f'{nm} ＝ T1 ＋ {q["dist"]:.2f}∠( arg(T2 − T1) ＋ {ang_s(q["angle"])} )',
              f'[ALPHA] [Y] [+] {num(q["dist"])} [∠] [(] [Apps] [3] [ALPHA] [X] [−] [ALPHA] [Y] [)] [+] {dms_keys(q["angle"])} [)] [=]')
    d.run()
    Ps, Qs = xy(d.steps[1]), xy(d.steps[2])
    d.add('割り当て（以後）', 'A＝K1、B＝K2、C＝Q、D＝S、E＝P（ずらした座標。P・Qは丸めた値）',
          f'{cx(*sh("K1"))} [SHIFT] [STO] [A]\n{cx(*sh("K2"))} [SHIFT] [STO] [B]\n{cx(*Qs)} [SHIFT] [STO] [C]\n{cx(*sh("S"))} [SHIFT] [STO] [D]\n{cx(*Ps)} [SHIFT] [STO] [E]', show=False)
    d.add('点Rの分子', 'Conjg(S − Q) × (Q − K1)　のiの係数', '[Apps] [4] [ALPHA] [D] [−] [ALPHA] [C] [)] [×] [(] [ALPHA] [C] [−] [ALPHA] [A] [)] [=]')
    d.add('点Rの分母', 'Conjg(S − Q) × (K2 − K1)　のiの係数', '[Apps] [4] [ALPHA] [D] [−] [ALPHA] [C] [)] [×] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [=]')
    d.run()
    tn, td = val(d.steps[-2], 1), val(d.steps[-1], 1)
    d.add('点R（ずらした座標）', 'R ＝ K1 ＋ (K2 − K1) × 分子 ÷ 分母', f'[ALPHA] [A] [+] [(] [ALPHA] [B] [−] [ALPHA] [A] [)] [×] {sn(tn)} [÷] {sn(td)} [=]')
    d.run()
    Rs = xy(d.steps[-1])
    d.add('Rを記憶', 'F＝R（丸めた座標）', f'{cx(*Rs)} [SHIFT] [STO] [F]', show=False)
    d.add('地積（倍面積）', '四角形K1・P・Q・R：Conjg(Q − K1) × (R − P)　のiの係数の絶対値 ÷ 2', '[Apps] [4] [ALPHA] [C] [−] [ALPHA] [A] [)] [×] [(] [ALPHA] [F] [−] [ALPHA] [E] [)] [=]')
    off = f'[(] {sn(ox)} [)] [+] {num(oy)} [i]'
    for nm, m in (('P', 'E'), ('Q', 'C'), ('R', 'F')):
        d.add(f'点{nm}を元の座標に戻す', f'{nm} ＝ ずらした{nm} ＋ (−38500.00 ＋ 22700.00i)', f'[ALPHA] [{m}] [+] [(] {off} [)] [=]')
    d.run()
    st = d.steps
    area = math.floor(abs(val(st[-4], 1)) / 2 * 100 + 1e-9) / 100
    got = {'点P': xy(st[-3]), '点Q': xy(st[-2]), '点R': xy(st[-1]), '本件土地の地積': area}
    return [('点P・Q（ずらした座標で放射）', st[:3]), ('点R・地積・元の座標に戻す', st[3:])], got


def main():
    for pid, fn in (('PM-01', pm01), ('PM-04', pm04), ('PM-07', pm07), ('PM-08', pm08), ('PM-09', pm09), ('PM-10', pm10), ('PM-82', pm82), ('PM-83', pm83), ('PM-84', pm84)):
        fp = os.path.join(PROB, pid + '.json')
        p = json.load(open(fp, encoding='utf-8'))
        groups, got = fn(p)
        p['keys'] = [{'title': t, 'steps': [{k: s[k] for k in ('title', 'formula', 'keys', 'display') if k in s} for s in st]} for t, st in groups]
        json.dump(p, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(pid, got)


if __name__ == '__main__':
    main()
