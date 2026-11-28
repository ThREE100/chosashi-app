"""毎日ドリル（夜）の学習まんが：計算の途中の数を、問題データから計算し直して確かめる。
台本の calc＝[(式, 漫画に書く文字), …]。式は Python の式で、問題の図の点の名前（K1・S など。X＋Yi の複素数）と
下の関数が使える。漫画に書く文字（「−92.816」「−7.55 ＋ 0.16i」「245°21′56.68″」「1.7490…」）を数に直し、
式の値と、最後の桁の1つ分以内で一致するかを見る。一致した文字の数だけが、漫画に出てよい「途中の数」になる。"""
import cmath
import math
import re


def ang(d, m=0, s=0):
    """度分秒 → 度"""
    return d + m / 60 + s / 3600


def argd(z):
    """複素数の向き（度。電卓の arg と同じく −180〜180）"""
    return math.degrees(cmath.phase(z))


def polar(r, deg):
    """r∠deg"""
    return cmath.rect(r, math.radians(deg))


def cross(a, b):
    """Conjg(a) × b の i の係数 ＝ aX × bY − aY × bX（たすき掛け）"""
    return (a.conjugate() * b).imag


def names(P):
    """問題の図の点 → 複素数（X ＋ Yi）。点P・Q・R は答え（小数第2位）の値"""
    return {k: complex(*v['xy']) for k, v in P['fig']['points'].items()}


NS = dict(ang=ang, argd=argd, polar=polar, cross=cross, abs=abs, conj=lambda z: z.conjugate())
NUM = r'[−-]?\d+(?:\.\d+)?'


def _unit(s):
    """最後の桁の1つ分（「…」は切り捨てなので1つ分、四捨五入でも1つ分以内なら通す）"""
    return 10 ** -len(s.split('.')[1]) if '.' in s else 1


def parse(shown):
    """漫画の文字 → (値, 許す差)。度分秒・複素数・実数"""
    t = shown.replace('…', '').replace(' ', '').replace('　', '').replace('＋', '+').replace('−', '-').replace('（', '(').replace('）', ')')
    t = t.replace('(', '').replace(')', '')
    m = re.fullmatch(r'(-?)(\d+)°(\d+)′(\d+(?:\.\d+)?)″', t)
    if m:
        v = int(m.group(2)) + int(m.group(3)) / 60 + float(m.group(4)) / 3600
        return (-v if m.group(1) else v), _unit(m.group(4)) / 3600
    m = re.fullmatch(r'(-?\d+(?:\.\d+)?)([+-])(\d+(?:\.\d+)?)i', t)
    if m:
        re_, im = float(m.group(1)), float(m.group(3)) * (1 if m.group(2) == '+' else -1)
        return complex(re_, im), max(_unit(m.group(1)), _unit(m.group(3)))
    m = re.fullmatch(r'-?\d+(?:\.\d+)?', t)
    if m:
        return float(t), _unit(t.lstrip('-'))
    raise ValueError(f'読めない：{shown}')


def check(P, calc):
    """[(式, 文字)] を確かめて (NG のリスト, 漫画に出てよい数の集合) を返す"""
    ns = dict(NS, **names(P))
    ng, ok = [], set()
    for expr, shown in calc:
        try:
            v = eval(expr, {'__builtins__': {}}, ns)
            want, tol = parse(shown)
        except Exception as e:  # noqa: BLE001
            ng.append(f'計算「{expr}」→「{shown}」が確かめられない：{e}')
            continue
        d = complex(v) - complex(want)
        if max(abs(d.real), abs(d.imag)) > tol * 1.0001:
            ng.append(f'計算「{expr}」＝{v} が漫画の「{shown}」と合わない')
            continue
        ok.update(re.findall(r'\d+(?:\.\d+)?', shown))
    return ng, ok
