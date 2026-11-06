#!/usr/bin/env python3
"""択一の総論（②）図解プロンプトの見出しを、3行・実測寸法の HEADER LOCK に直す（2026-11-06）。
対象：各年度・答練・予想模試・毎日ドリル以外の note-articles/*-mondai 等の q*.md にあるコードブロックのうち、
GLANCEABLE-POSTER REQUIREMENT と --- HEADER --- を含む総論のプロンプト。何度実行しても同じ結果（冪等）。
  1. Title を「1行目＝問いのタイトル／2行目＝論点」に、Subtitle を「年度 第N問」だけにする（午後の部・午前の部は書かない）。
  2. HEADER LOCK の段落を GLANCEABLE の直前に入れ、最後の確認に1文足す。
使い方： python3 tools/apply_header_lock.py [--dry]
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NA = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(os.path.dirname(NA), 'note-unei', 'instagram'))
from header_lock_text import HEADER_LOCK_PARA, FINAL_SENTENCE  # noqa: E402

DIRS = [d for d in sorted(os.listdir(NA)) if re.match(r'(r\d|h\d\d)-mondai$|jissen-tanren|chokuzen-yosou-moshi|zissen-ansatsu', d)]
TOK = re.compile(r'((?:令和|平成)(?:元|\d+)年度)[ \u3000]*(?:午前の部|午後の部|午前|午後)?[ \u3000]*第(\d+)問'
                 r'|(直前予想模試)[ \u3000]*第(\d+)問'
                 r'|(実践答練)[ \u3000]*(第\d+回)[ \u3000]*(?:択一式)?[ \u3000]*第(\d+)問')
HDR = re.compile(r'--- HEADER ---\n\s*Title \(large, bold, \d行\):\n(.+?)\n\s*Subtitle \(smaller, centered, \d行\):\n(.+?)(\n\n+（|\n\n+---|\n---)', re.S)


def label(t):
    if t.group(1):
        return f'{t.group(1)} 第{t.group(2)}問'
    if t.group(3):
        return f'{t.group(3)} 第{t.group(4)}問'
    return f'{t.group(5)} {t.group(6)} 第{t.group(7)}問'


def fix_header(b):
    m = HDR.search(b)
    if not m:
        return b, 'nomatch'
    titles = [x.strip() for x in m.group(1).split('\n') if x.strip()]
    sub = ' '.join(x.strip() for x in m.group(2).split('\n') if x.strip())
    t = TOK.search(sub)
    if not t:
        return b, 'notoken'
    year = label(t)
    rest = (sub[:t.start()] + sub[t.end():]).strip()
    rest = re.sub(r'[（(]\s*[）)]', '', rest)
    rest = re.sub(r'^[－\-—／/（(\s\u3000]+|[）)－\-—／/\s\u3000]+$', '', rest).strip()
    lines = list(titles)
    if len(lines) == 1 and rest:
        lines.append(rest)
    new = ('--- HEADER ---\nTitle (large, bold, %d行):\n%s\n\nSubtitle (smaller, centered, 1行):\n%s%s'
           % (len(lines), '\n'.join(lines), year, m.group(3)))
    return b[:m.start()] + new + b[m.end():], 'ok'


def process(s):
    out, pos, stat = [], 0, []
    for m in re.finditer(r'```\n(.*?)```', s, re.S):
        b = m.group(1)
        if 'GLANCEABLE-POSTER REQUIREMENT' not in b or '--- HEADER ---' not in b or 'HEADER LOCK (critical)' in b:
            continue
        b2, st = fix_header(b)
        stat.append(st)
        if st != 'ok':
            continue
        b2 = b2.replace('GLANCEABLE-POSTER REQUIREMENT', HEADER_LOCK_PARA + '\n\nGLANCEABLE-POSTER REQUIREMENT', 1)
        j = b2.rfind('Confirm the entire canvas')
        b2 = b2[:j] + FINAL_SENTENCE + ' ' + b2[j:] if j != -1 else b2.rstrip('\n') + '\n' + FINAL_SENTENCE + '\n'
        out.append((m.start(1), m.end(1), b2))
    for a, e, b2 in reversed(out):
        s = s[:a] + b2 + s[e:]
    return s, stat


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    tot = {}
    for d in DIRS:
        for f in sorted(glob.glob(os.path.join(NA, d, 'q*.md'))):
            s = open(f, encoding='utf-8').read()
            s2, stat = process(s)
            for x in stat:
                tot[x] = tot.get(x, 0) + 1
                if x != 'ok':
                    print(x, os.path.relpath(f, NA))
            if s2 != s and not dry:
                open(f, 'w', encoding='utf-8').write(s2)
    print(tot)
