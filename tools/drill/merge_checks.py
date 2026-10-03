#!/usr/bin/env python3
"""work/article_check_{年度}.json（年度ごとの条文照合の結果）を data/article_checks.json にまとめる。
ドリルは、この結果をもとに、出題中は指摘のある肢だけ追加表示する（毎回の条文確認をしない）。"""
import glob, json, os, re, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); WORK = os.path.join(HERE, 'work'); OUT = os.path.join(HERE, 'data', 'article_checks.json')
KEEP = ('error', 'warn', 'unverified')

def key(label):
    return re.sub(r'[正誤]$', '', label or '')

def main():
    checked, findings, years = {}, [], []
    for f in sorted(glob.glob(os.path.join(WORK, 'article_check_*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        years.append(d.get('year'))
        for path, v in d.get('articles', {}).items():
            checked[path] = {'labels_checked': [key(x) for x in v.get('labels_checked', [])]}
        for x in d.get('findings', []):
            if x.get('severity') not in KEEP:
                continue
            findings.append({'note_path': x['note_path'], 'label': key(x.get('label', '')), 'severity': x['severity'],
                             'problem': x.get('problem', ''), 'law_ref': x.get('law_ref', ''), 'proposal': x.get('proposal', ''),
                             'confidence': x.get('confidence', '')})
    meta = {'checked_at': dt.date.today().isoformat(), 'law_db': 'note-articles/laws/（e-Gov取得 2026-08-04）',
            'years': years, 'articles': len(checked),
            'findings': {s: sum(1 for x in findings if x['severity'] == s) for s in KEEP}}
    json.dump({'meta': meta, 'checked': checked, 'findings': findings}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))

main()
