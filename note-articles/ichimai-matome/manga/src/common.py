"""一枚まとめの学習まんが：共通の読み込み。シートのデータ（../../src/sheets/<ID>.py）は読むだけで書き換えない。"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MANGA = os.path.dirname(HERE)                       # note-articles/ichimai-matome/manga
IM = os.path.dirname(MANGA)                         # note-articles/ichimai-matome
REPO = os.path.abspath(os.path.join(IM, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools', 'gakushu_manga'))
sys.path.insert(0, os.path.join(IM, 'src'))
REL = 'note-articles/ichimai-matome/manga/'


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sheet(cid):
    return _load(os.path.join(IM, 'src', 'sheets', cid + '.py'), 'sheet_' + cid.replace('-', '_')).SHEET


def scripts():
    """台本 src/<ID>.py（ID は A-01 の形）"""
    out = []
    for f in sorted(os.listdir(HERE)):
        if re.fullmatch(r'[A-H]-\d\d\.py', f):
            out.append(_load(os.path.join(HERE, f), 'manga_' + f[:-3].replace('-', '_')).MANGA)
    return out


def bold(lines):
    return [w for s in lines for w in re.findall(r'\*\*(.+?)\*\*', s)]


def plain(s):
    return s.replace('**', '')


def sheet_text(S):
    """シートの全文（照合用）。"""
    parts = [S['articles']] + S['conclusion'] + S['traps'] + S['basis'] + S['example']['lines']
    for b in S['blocks']:
        parts += [b.get('title', ''), b.get('note', '') or '', b.get('text', '') or '']
        for r in b.get('rows', []):
            parts += r
        parts += b.get('head', []) + list(b.get('items', [])) if b['kind'] != 'defs' else [x for kv in b['items'] for x in kv]
        parts += b.get('yes', []) + b.get('no', [])
    return plain('\n'.join(str(x) for x in parts))
