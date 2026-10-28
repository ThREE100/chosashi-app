"""朝の択一の解答ページは、肢の根拠の引用の先頭に「法令名＋条」を付けず、ページ上部の題（theme）にまとめて載せる（2026-10-28。day004 の形）。
そのため、肢の根拠（basis）に出てくる法令の条は、すべて theme に「法第39条」「規則第131条」のように載っている必要がある。
このモジュールは、その載っているかの判定（check_am.py が使う）と、足りない条を theme の末尾のかっこに足す修正（--fix）を行う。
使い方: python3 daily-drill/theme_refs.py          （足りない条の一覧を表示）
        python3 daily-drill/theme_refs.py --fix    （足りない条を theme に足して morning/problems/*.json を書き直す）"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ABBR = {'不動産登記法': '不動産登記法', '法': '不動産登記法', '不動産登記令': '不動産登記令', '令': '不動産登記令',
        '不動産登記規則': '不動産登記規則', '規則': '不動産登記規則', '不動産登記事務取扱手続準則': '不動産登記事務取扱手続準則',
        '準則': '不動産登記事務取扱手続準則', '土地家屋調査士法施行規則': '土地家屋調査士法施行規則', '調査士法施行規則': '土地家屋調査士法施行規則', '施行規則': '土地家屋調査士法施行規則',
        '土地家屋調査士法': '土地家屋調査士法', '調査士法': '土地家屋調査士法', '民法': '民法', '区分所有法': '区分所有法', '登録免許税法': '登録免許税法'}
SHORT = {'不動産登記法': '法', '不動産登記令': '令', '不動産登記規則': '規則', '不動産登記事務取扱手続準則': '準則',
         '土地家屋調査士法': '調査士法', '土地家屋調査士法施行規則': '調査士法施行規則', '民法': '民法', '区分所有法': '区分所有法',
         '登録免許税法': '登録免許税法'}
_NAMES = '|'.join(sorted(ABBR, key=len, reverse=True))
TOK = re.compile(rf'(?P<abbr>{_NAMES})?第(?P<a>\d+)条(?P<an>の\d+)?(?:〜第(?P<b>\d+)条(?P<bn>の\d+)?)?')


def primary_law(p):
    """その問題の根拠で一番多い法令。theme の「法第39条」の「法」は、この法令のこと（調査士法の問題なら調査士法）。"""
    from collections import Counter
    c = Counter(b['law'] for s in p['statements'] for b in s['basis'] if 'doc' not in b and b['law'] in ('不動産登記法', '土地家屋調査士法'))
    return c.most_common(1)[0][0] if c else '不動産登記法'


def covered_set(theme, primary='不動産登記法'):
    """theme に載っている (法令名, 条番号, 枝番) の集合。「法第47条〜第49条、令第8条」のように、略称は次の略称が出るまで引き継ぐ。"""
    out, cur = set(), None
    for m in TOK.finditer(theme):
        if m.group('abbr'):
            cur = primary if m.group('abbr') == '法' else ABBR[m.group('abbr')]
        if not cur:
            continue
        a = int(m.group('a'))
        b = int(m.group('b')) if m.group('b') else a
        out.add((cur, a, m.group('an') or ''))
        for n in range(a, b + 1):
            out.add((cur, n, ''))
    return out


def ref_of(b):
    """basis 1件の (法令名, 表示用の条) 。条番号の取れないもの（令別表など）は (法令名, 条の文字列, None)。"""
    m = re.match(r'第(\d+)条(の\d+)?', b['article'])
    if m:
        return b['law'], int(m.group(1)), m.group(2) or ''
    return b['law'], None, b['article']


def missing_refs(p):
    """theme に載っていない根拠の条を、出てくる順に（重複なしで）返す。先例型（doc）は対象外。"""
    cs = covered_set(p['theme'], primary_law(p))
    miss = []
    for s in p['statements']:
        for b in s['basis']:
            if 'doc' in b:
                continue
            law, n, extra = ref_of(b)
            if n is not None:
                if (law, n, extra) in cs or (law, n, '') in cs:
                    continue
                key = (law, n, extra)
            else:
                art = extra
                if art in p['theme'] or (law == '不動産登記令別表' and f'別表{art}' in p['theme']):
                    continue
                key = (law, None, art)
            if key not in miss:
                miss.append(key)
    return miss


def format_refs(miss):
    """足りない条を「規則第78条・第131条、令別表十三の項」の形に。"""
    groups = []
    for law, n, extra in miss:
        if n is None:
            groups.append(('令別表' if law == '不動産登記令別表' else SHORT.get(law, law), [f'{extra}の項' if not extra.startswith(('第', '別表')) else extra], True))
            continue
        short = SHORT.get(law, law)
        label = f'第{n}条{extra}'
        for g in groups:
            if g[0] == short and not g[2]:
                g[1].append(label)
                break
        else:
            groups.append((short, [label], False))
    out = []
    for short, labels, raw in groups:
        out.append(short + ('・'.join(labels) if raw else labels[0] + ''.join('・' + x for x in labels[1:])))
    return '、'.join(out)


def fixed_theme(p):
    miss = missing_refs(p)
    if not miss:
        return p['theme']
    # 条番号順に並べる（法令は出てくる順）
    order = {}
    for law, _, _ in miss:
        order.setdefault(law, len(order))
    miss = sorted(miss, key=lambda k: (order[k[0]], k[1] if k[1] is not None else 0, k[2]))
    add = format_refs(miss)
    t = p['theme']
    pl = primary_law(p)
    if add.startswith(SHORT[pl] + '第') and not add.startswith('調査士法施行'):   # 本法の条は、すでに載っている本法の並びに続ける
        first, _, rest = add.partition('、')
        mm = re.search(r'(?<![規施])' + re.escape(SHORT[pl]) + r'第\d+条[^、）]*', t)
        if mm:
            t = t[:mm.end()] + '・' + first[len(SHORT[pl]):] + t[mm.end():]
            if not rest:
                return t
            add = rest
    m = re.search(r'（([^（）]*)）$', t)
    if m and re.search(r'第\d+条', m.group(1)):      # 末尾のかっこが条文の一覧なら、そこに足す
        return t[:-1] + '、' + add + '）'
    return t + '（' + add + '）'                      # 条文の一覧がなければ、かっこを足す


if __name__ == '__main__':
    fix = '--fix' in sys.argv
    n = 0
    for fp in sorted(glob.glob(os.path.join(HERE, 'morning', 'problems', '*.json'))):
        p = json.load(open(fp, encoding='utf-8'))
        if not missing_refs(p):
            continue
        n += 1
        new = fixed_theme(p)
        print(p['id'], p['theme'], '\n   →', new)
        if fix:
            p['theme'] = new
            json.dump(p, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{n}問で theme に足りない条があります' + ('（直しました）' if fix and n else ''))
