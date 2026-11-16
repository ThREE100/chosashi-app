"""法令の原文（note-articles/laws/）を条ごとに読み出す。引用の実在と、文言の確認に使う。"""
import os
import re

LAWS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'laws')
KAN = {'〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}


def kan2int(s):
    if re.fullmatch(r'[0-9]+', s):
        return int(s)
    s = s.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
    if re.fullmatch(r'[0-9]+', s):
        return int(s)
    total, cur = 0, 0
    for ch in s:
        if ch == '百':
            total += (cur or 1) * 100
            cur = 0
        elif ch == '十':
            total += (cur or 1) * 10
            cur = 0
        else:
            cur = cur * 10 + KAN[ch]
    return total + cur


HEAD = re.compile(r'^#{2,6}\s*第([0-9０-９一二三四五六七八九十百〇]+)条((?:の[0-9０-９一二三四五六七八九十百〇]+)*)[\s　（(]', re.M)

FILES = {
    '不動産登記法': ['fudousan-touki-hou.md'],
    '不動産登記令': ['fudousan-touki-rei.md'],
    '不動産登記規則': ['fudousan-touki-kisoku-1.md', 'fudousan-touki-kisoku-2.md'],
    '準則': ['fudousan-touki-jimu-junsoku.md'],
    '区分所有法': ['kubunshoyuu-hou.md'],
    '民法': ['minpou-1-soukyoku-bukken.md', 'minpou-2-saiken.md', 'minpou-3-shinzoku-souzoku.md'],
    '土地家屋調査士法': ['chousashi-hou.md'],
    '土地家屋調査士法施行規則': ['chousashi-hou-sekourule.md'],
    '登録免許税法': ['touroku-menkyozei-hou.md'],
    '筆界特定': [],
}
_cache = {}


def _stop(text, law):
    """附則以降を除く（本則だけを対象にする）。"""
    for pat in (r'^#{1,3}\s*附\s*則', r'^#{1,3}\s*附則'):
        m = re.search(pat, text, re.M)
        if m:
            return text[:m.start()]
    return text


def articles(law):
    if law in _cache:
        return _cache[law]
    arts = {}
    for fn in FILES[law]:
        t = open(os.path.join(LAWS, fn), encoding='utf-8').read()
        if law not in ('不動産登記規則',):
            t = _stop(t, law)
        ms = list(HEAD.finditer(t))
        for i, m in enumerate(ms):
            key = str(kan2int(m.group(1)))
            for sub in re.findall(r'の([0-9０-９一二三四五六七八九十百〇]+)', m.group(2)):
                key += 'の' + str(kan2int(sub))
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            arts.setdefault(key, t[m.start():end])
    _cache[law] = arts
    return arts


def has(law, key):
    return key in articles(law)


def text(law, key):
    return articles(law).get(key, '')


NAMES = ['不動産登記事務取扱手続準則', '土地家屋調査士法施行規則', '不動産登記法', '不動産登記令', '不動産登記規則', '区分所有法', '土地家屋調査士法', '登録免許税法', '準則', '民法', '規則', '令', '法']
ALIAS = {'規則': '不動産登記規則', '令': '不動産登記令', '法': None, '準則': '準則', '不動産登記事務取扱手続準則': '準則'}
CITE = re.compile(r'(?<![一-龥ぁ-んァ-ヶ])(' + '|'.join(NAMES) + r')第([0-9]+)条((?:の[0-9]+)*)')
BARE = re.compile(r'(?<![一-龥ぁ-んァ-ヶ法令則])第([0-9]+)条((?:の[0-9]+)*)')


def citations(text_, default_law):
    """文中の「法令名第N条」を (law, key) の一覧にする。法令名のない「第N条」は default_law として扱う。"""
    out = []
    spans = []
    for m in CITE.finditer(text_):
        nm = m.group(1)
        law = ALIAS[nm] if nm in ALIAS else nm
        if law is None:
            law = default_law
        key = m.group(2) + m.group(3)
        out.append((law, key, m.group(0)))
        spans.append((m.start(), m.end()))
    for m in BARE.finditer(text_):
        if any(s <= m.start() < e for s, e in spans):
            continue
        out.append((default_law, m.group(1) + m.group(2), m.group(0)))
    return out


if __name__ == '__main__':
    for law in FILES:
        if FILES[law]:
            a = articles(law)
            print(law, len(a), 'articles; e.g.', list(a)[:3], list(a)[-3:])
