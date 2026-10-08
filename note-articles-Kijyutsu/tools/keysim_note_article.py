"""記述式（土地）会話形式の記事の「電卓操作」を、F-789SG の複素数モード（角度は度）のキー列としてそのまま実行し、
直後の「表示：」の値と一致するかを確かめる（2026-10-07追加、R7/Q21の照らし直しで作成）。

- 記事の中のキー列（[ALPHA] [X]、[SHIFT] [STO] [X]、[Apps] [3]＝arg(、[Apps] [4]＝Conjg(、[∠]、[°′″]、[i]、[√]、四則・かっこ・[=]）
  を順に式に直して実行する。変数（A〜F、X、Y）は記事の順に記憶・使い回すので、変数の取り違えや使い回しの時期の誤りも見つかる
- 執筆指示書の「電卓操作の要点」にないキー（[Ans]、実部・虚部の取り出しなど）が出てきたら止める
- √ は正の実数にだけ使う（複素数の√は止める）
- 「表示：（実部）− 1119.7006i」の形は、iの係数（符号を含む）だけを照らす

- 未対応（2026-10-07時点）：記事の中で変数の状態を巻き戻して別解を始める書き方（H29/Q21の「Y＝Gから始める」）、
  ∠ の後にかっこのない書き方（H23〜H25/Q21）、整数の表示（H22/Q21の「1」）。純虚数の表示（実部が丸めの誤差だけ）は2026-10-08に対応（R2/Q21）。年度の照合スクリプトで使うのは、全部の表示が一致した年度だけにする

使い方: python3 note-articles-Kijyutsu/tools/keysim_note_article.py 記事.md
       （照合スクリプトからは simulate(記事のパス) を呼ぶ。戻り値は [(行番号, 記事の表示, 再現した表示, 一致)]）
"""
import cmath
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calc_helpers import disp, fmt_num  # noqa: E402


def _arg(z):
    return math.degrees(cmath.phase(z))


def _conj(z):
    return complex(z).conjugate()


def _polar(r, a):
    return cmath.rect(r, math.radians(complex(a).real))


def _sqrt(x):
    x = complex(x)
    if abs(x.imag) > 1e-12 or x.real < 0:
        raise ValueError('√ は正の実数にだけ使う')
    return math.sqrt(x.real)


def _sin(a):
    return math.sin(math.radians(complex(a).real))


def _cos(a):
    return math.cos(math.radians(complex(a).real))


ENV = {'arg': _arg, 'conj': _conj, 'polar': _polar, 'sqrt': _sqrt, 'absf': lambda z: abs(z), 'sinf': _sin, 'cosf': _cos}
ALLOWED = {'[ALPHA]', '[SHIFT]', '[STO]', '[Apps]', '[3]', '[4]', '[∠]', '[°′″]', '[i]', '[√]', '[+]', '[−]', '[×]', '[÷]',
           '[(]', '[)]', '[=]', '[Abs]', '[sin]', '[cos]'}
FUNCS = {'[Abs]': 'absf(', '[sin]': 'sinf(', '[cos]': 'cosf('}   # 関数のキーは開きかっこを兼ねる


def _tokens(seq):
    return re.findall(r'\[[^\]]+\]|[0-9]+(?:\.[0-9]+)?', seq)


def _to_expr(tk):
    out, pend, depth, i = [], [], 0, 0
    while i < len(tk):
        x = tk[i]
        if x == '[ALPHA]':
            out.append(f"mem['{tk[i + 1][1:-1]}']")
            i += 2
            continue
        if x == '[Apps]':
            out.append({'[3]': 'arg(', '[4]': 'conj('}[tk[i + 1]])
            depth += 1
            i += 2
            continue
        if x in FUNCS:
            out.append(FUNCS[x])
            depth += 1
            i += 1
            continue
        if x == '[∠]':                       # r∠(θ) → polar(r, (θ))
            r = out.pop()
            out.append(f'polar({r},')
            if tk[i + 1] != '[(]':
                raise ValueError('∠ の後はかっこで角度を囲む')
            out.append('(')
            depth += 1
            pend.append(depth)
            i += 2
            continue
        if re.match(r'^[0-9]', x) and i + 1 < len(tk) and tk[i + 1] == '[°′″]':   # d [°′″] m [°′″] s [°′″]
            out.append(f'({x}+{tk[i + 2]}/60+{tk[i + 4]}/3600)')
            i += 6
            continue
        out.append({'[√]': 'sqrt', '[(]': '(', '[+]': '+', '[−]': '-', '[×]': '*', '[÷]': '/'}.get(x, x))
        if x == '[(]':
            depth += 1
        elif x == '[)]':
            out[-1] = ')'
            if pend and pend[-1] == depth:
                out.append(')')
                pend.pop()
            depth -= 1
        elif x == '[i]':
            out.pop()
            out[-1] = f'({out[-1]}*1j)'
        elif x not in ('[√]', '[+]', '[−]', '[×]', '[÷]', '[(]') and not re.match(r'^[0-9]', x):
            raise ValueError(f'想定外のキー {x}')
        i += 1
    e = ''.join(out)
    return re.sub(r"(\)|\]|[0-9])(?=(mem\[|arg\(|conj\(|absf\(|sinf\(|cosf\(|sqrt|polar\(|\())", r'\1*', e)   # 暗黙の掛け算


def simulate(path):
    lines = open(path, encoding='utf-8').read().splitlines()
    mem, results, inblock, buf, start = {}, [], False, [], 0
    for n, l in enumerate(lines, 1):
        if l.strip().startswith('```'):
            if not inblock:
                inblock, buf, start = True, [], n
                continue
            inblock = False
            if not any(k in b for b in buf for k in ('[ALPHA]', '[SHIFT]', '[=]')):
                continue
            tk = _tokens(' '.join(buf))
            bad = [x for x in tk if x.startswith('[') and x not in ALLOWED and not re.match(r'^\[[A-FXY]\]$', x)]
            if bad:
                raise ValueError(f'{start}行目: 要点にないキー {bad}')
            seg, vals, j = [], [], 0
            while j < len(tk):
                x = tk[j]
                if x == '[=]':
                    vals.append(eval(_to_expr(seg), {'mem': mem, **ENV}))
                    seg = []
                    j += 1
                    continue
                if x == '[SHIFT]' and tk[j + 1] == '[STO]':
                    v = eval(_to_expr(seg), {'mem': mem, **ENV}) if seg else vals[-1]
                    seg = []
                    mem[tk[j + 2][1:-1]] = v
                    j += 3
                    continue
                seg.append(x)
                j += 1
            if vals:
                results.append((start, vals))
            continue
        if inblock:
            buf.append(l)
    out = []
    disp_lines = [(n, l[3:]) for n, l in enumerate(lines, 1) if l.startswith('表示：')]
    for n, want in disp_lines:
        blk = max(s for s, _ in results if s < n)
        vs = [v for s, vv in results if s == blk for v in vv]
        used = sum(1 for m, _ in disp_lines if blk < m < n)
        v = complex(vs[min(used, len(vs) - 1)])
        if '（実部）' in want:
            got = f'（実部）{"−" if v.imag < 0 else "＋"} {fmt_num(abs(v.imag))}i'
        else:
            if abs(v.imag) < 1e-9:
                got = fmt_num(v.real)
            elif abs(v.real) < 1e-9:   # 実部が丸めの誤差だけの純虚数（R2/Q21の Conjg(E − B) × (A − B) ＝ 151.20i。2026-10-08追加）
                got = ('−' if v.imag < 0 else '') + f'{fmt_num(abs(v.imag))}i'
            else:
                got = disp(v)
        out.append((n, want, got, want == got))
    return out


if __name__ == '__main__':
    res = simulate(sys.argv[1])
    for n, want, got, ok in res:
        print(('OK ' if ok else 'NG ') + f'{n}行目: 記事「{want}」／ キー列の再現「{got}」')
    print('NG件数:', sum(not ok for *_, ok in res))
