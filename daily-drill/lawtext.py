"""法令の原文（note-articles/laws/）から条文を取り出す共通部品。
本則の条（最初に出てくる見出し）だけを返す。附則は対象外。"""
import os
import re

LAWS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'note-articles', 'laws')
LAW_FILES = {
    '不動産登記法': ['fudousan-touki-hou.md'],
    '不動産登記令': ['fudousan-touki-rei.md'],
    '不動産登記規則': ['fudousan-touki-kisoku-1.md', 'fudousan-touki-kisoku-2.md', 'fudousan-touki-kisoku-3.md'],
    '不動産登記事務取扱手続準則': ['fudousan-touki-jimu-junsoku.md'],
    '土地家屋調査士法': ['chousashi-hou.md'],
    '土地家屋調査士法施行規則': ['chousashi-hou-sekourule.md'],
    '不動産登記令別表': ['fudousan-touki-rei-betsuhyou.md'],
    '登録免許税法': ['touroku-menkyozei-hou.md'],
    '民法': ['minpou-1-soukyoku-bukken.md', 'minpou-2-saiken.md', 'minpou-3-shinzoku-souzoku.md'],
}
_cache = {}


def _lines(fn):
    if fn not in _cache:
        with open(os.path.join(LAWS_DIR, fn), encoding='utf-8') as f:
            _cache[fn] = f.read().split('\n')
    return _cache[fn]


_K = '〇一二三四五六七八九'


def _kan(n):
    """1〜999 を漢数字にする（百五・二十二 など）。"""
    out = ''
    h, t, o = n // 100, n // 10 % 10, n % 10
    if h:
        out += ('' if h == 1 else _K[h]) + '百'
    if t:
        out += ('' if t == 1 else _K[t]) + '十'
    if o:
        out += _K[o]
    return out


def _alt(num):
    """'第105条の2' → '第百五条の二'（規則・令・準則の見出しは漢数字）。"""
    return re.sub(r'\d+', lambda m: _kan(int(m.group())), num)


def article(law, num):
    if num == '別表第一':   # 登録免許税法の別表第一は表（見出しがないので全文を対象にする）
        return '\n'.join(_lines(LAW_FILES[law][0]))
    r = _article(law, num)
    return r if r is not None else _article(law, _alt(num))


def _article(law, num):
    """num は '第41条' や '第41条の2'。見出し行（'##### 第41条（…）'）から次の見出しの手前まで。見つからなければ None。"""
    pat = re.compile(r'^#{3,6} ' + re.escape(num) + r'(（|\s|$)')  # 見出し「第41条（…）」「第百五条 （…）」
    for fn in LAW_FILES[law]:
        lines = _lines(fn)
        for i, ln in enumerate(lines):
            if pat.match(ln):
                out = [ln]
                for j in range(i + 1, len(lines)):
                    if re.match(r'^#{1,6} ', lines[j]):
                        break
                    out.append(lines[j])
                # 次の条の見出しの見出し語（例：（会則の遵守義務））が末尾に付くので除く
                while out and (not out[-1].strip() or re.fullmatch(r'（[^）]{1,30}）', out[-1].strip())):
                    out.pop()
                return '\n'.join(out).strip()
    return None


def normalize(s):
    """引用の突き合わせ用：空白・改行・箇条書き記号・全角半角のゆれを除く。"""
    s = re.sub(r'^\s*- ', '', s, flags=re.M)
    s = re.sub(r'\s+', '', s)
    return s
