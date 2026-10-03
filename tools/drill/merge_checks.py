#!/usr/bin/env python3
"""work/article_check_{年度}.json（年度ごとの条文照合の結果）を data/article_checks.json にまとめる。
ドリルは、この結果をもとに、出題中は指摘のある肢だけ追加表示する（毎回の条文確認をしない）。"""
import glob, hashlib, json, os, re, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); WORK = os.path.join(HERE, 'work'); OUT = os.path.join(HERE, 'data', 'article_checks.json')
KEEP = ('error', 'warn', 'unverified')
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


def article_sha(note_path):
    """照合した記事の版を origin/main の内容のハッシュで記録する（あとで記事が更新されたかを判定するため）。"""
    r = subprocess.run(['git', 'show', f'origin/main:{note_path}'], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        return None
    return hashlib.sha256(r.stdout.decode('utf-8').encode('utf-8')).hexdigest()[:16]

def key(label):
    return re.sub(r'[正誤]$', '', label or '')

def main():
    checked, findings, years = {}, [], []
    for f in sorted(glob.glob(os.path.join(WORK, 'article_check_*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        years.append(d.get('year'))
        for path, v in d.get('articles', {}).items():
            checked[path] = {'labels_checked': [key(x) for x in v.get('labels_checked', [])], 'sha': article_sha(path)}
        for x in d.get('findings', []):
            if x.get('severity') not in KEEP:
                continue
            findings.append({'note_path': x['note_path'], 'label': key(x.get('label', '')), 'severity': x['severity'],
                             'problem': x.get('problem', ''), 'law_ref': x.get('law_ref', ''), 'proposal': x.get('proposal', ''),
                             'confidence': x.get('confidence', '')})
    na = subprocess.run(['git', 'log', '-1', '--format=%H', 'origin/main', '--', 'note-articles'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    meta = {'note_articles_commit': na, 'checked_at': dt.date.today().isoformat(), 'law_db': 'note-articles/laws/（e-Gov取得 2026-08-04）',
            'years': years, 'articles': len(checked),
            'findings': {s: sum(1 for x in findings if x['severity'] == s) for s in KEEP}}
    json.dump({'meta': meta, 'checked': checked, 'findings': findings}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))

main()
