#!/usr/bin/env python3
"""note-articles/*-mondai の引用ブロックから、420問の問題文・肢・選択肢行を取り出す。
出力: tools/drill/work/questions_raw.json  (年度×問番号で takuitsu.json の正答番号とも突き合わせる)"""
import json, re, glob, os, sys
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
OUT = os.path.join(os.path.dirname(__file__), 'work')
os.makedirs(OUT, exist_ok=True)

def ycode(path):
    s = path.split('/')[-2].replace('-mondai', '').upper()
    return 'R0' + s[1] if re.fullmatch(r'R\d', s) else s

def parse_quote(text):
    lines = []
    for ln in text.split('\n'):
        if ln.startswith('>'):
            lines.append(ln[1:].strip().replace('　', ' ').strip())
        elif lines:
            break
    return [l for l in lines if l.strip()]

def main():
    tk = {x['id']: x for x in json.load(open(os.path.join(ROOT, 'src/data/takuitsu.json'), encoding='utf-8'))['questions']}
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'note-articles/*-mondai/q*.md'))):
        t = open(f, encoding='utf-8').read()
        y = ycode(f); n = int(re.search(r'/q(\d+)-', f).group(1))
        q = parse_quote(t)
        title = t.split('\n', 1)[0].lstrip('# ').strip()
        qid = f'chosashi_{y}_q{n:02d}'
        k = tk.get(qid, {})
        out.append({
            'id': qid, 'yearCode': y, 'questionNo': n,
            'note_path': os.path.relpath(f, ROOT), 'title': title,
            'quote': q,
            'takuitsu_correctAnswer': k.get('correctAnswer'),
            'takuitsu_combos': {c['no']: c['text'] for c in k.get('combos', [])},
            'takuitsu_alts': k.get('alts', []),
            'subject': k.get('subject'),
        })
    json.dump(out, open(os.path.join(OUT, 'questions_raw.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), 'questions')
main()
