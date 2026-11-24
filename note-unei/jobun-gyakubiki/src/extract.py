"""年度別の択一記事（H17〜R8）を肢ごとに分け、肢の解説で法令名つきで引いている条文を拾う。
一問一答バンク（tools/drill/data/items.json）と、出典（年度・問・肢）で突き合わせる。
法令名のない「法第○条」「第○条」は、どの法令か機械的に決められないので拾わない（控えめな拾い方）。
出力：note-unei/jobun-gyakubiki/data/shi.json（肢ごと）、jobun.json（条文ごと）。
"""
import re, glob, json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BASE))
sys.path.insert(0, os.path.join(ROOT, 'note-unei', 'hitogara', 'src'))
from count_articles import LAWS, NAME, PAT, Z, YEARS, body  # 数え方を「条文ベスト10」とそろえる

LABELS = 'アイウエオ'
SEC = re.compile(r'^###\s*(?:空欄)?([アイウエオカキクケコ1-5①-⑩])[：:]\s*(.*)$', re.M)
QUOTE = re.compile(r'^>\s*([アイウエオカキクケコ1-5])[ 　]+(.+?)\s*$', re.M)
TITLE = re.compile(r'^##\s*(【.*)$', re.M)
YEAR_JA = {**{f'h{n}': f'平成{n}年度' for n in range(17, 31)}, 'r1': '令和元年度',
           **{f'r{n}': f'令和{n}年度' for n in range(2, 9)}}


def cites(text):
    found = []
    for m in PAT.finditer(text):
        law = NAME[dict(LAWS)[m.group(1)]]
        art = m.group(2).translate(Z) + ('の' + m.group(3).translate(Z) if m.group(3) else '')
        if (law, art) not in found:
            found.append((law, art))
    return found


def main():
    bank = json.load(open(os.path.join(ROOT, 'tools/drill/data/items.json'), encoding='utf-8'))['items']
    by_src = {}
    for it in bank:
        for s in it['sources']:
            by_src[(s['q'], s['label'])] = it
    shi = []
    miss = 0
    for y in YEARS:
        for f in sorted(glob.glob(f'{ROOT}/note-articles/{y}-mondai/q[0-9][0-9]-*.md')):
            text = open(f, encoding='utf-8').read()
            t = TITLE.search(text)
            title = t.group(1).strip() if t else ''
            qn = int(os.path.basename(f)[1:3])
            yc = y.upper() if y[0] == 'h' else f'R{int(y[1:]):02d}'
            qid = f'{yc}-Q{qn:02d}'
            quoted = dict(QUOTE.findall(text))
            b = body(text)
            secs = list(SEC.finditer(b))
            for i, m in enumerate(secs):
                end = secs[i + 1].start() if i + 1 < len(secs) else len(b)
                end2 = b.find('\n### まとめ', m.start())
                if 0 < end2 < end:
                    end = end2
                sec = b[m.start():end]
                lab = m.group(1)
                kuuran = m.group(0).lstrip('#').strip().startswith('空欄')
                it = by_src.get((qid, lab))
                if it is None:
                    miss += 1
                shi.append({
                    'id': f'{qid}-{lab}', 'kuuran': kuuran, 'year': y, 'year_ja': YEAR_JA[y], 'q': qn, 'label': lab,
                    'heading': m.group(2).strip(), 'title': title,
                    'path': os.path.relpath(f, ROOT),
                    'statement': it['statement'] if it else quoted.get(lab, ''), 'from_bank': bool(it), 'truth': it['truth'] if it else None,
                    'subject': it['subject'] if it else '', 'topic': it['topic'] if it else '',
                    'bank_id': it['id'] if it else '',
                    'cites': [list(c) for c in cites(sec)],
                })
    ID2Y = {s['id']: s['year'] for s in shi}
    jobun = collections.defaultdict(list)
    for s in shi:
        for law, art in s['cites']:
            jobun[(law, art)].append(s['id'])
    rows = []
    for (law, art), ids in jobun.items():
        ys = sorted({ID2Y[i] for i in ids}, key=YEARS.index)
        rows.append({'law': law, 'article': art, 'years': len(ys), 'shi': len(ids),
                     'year_list': ys, 'shi_ids': ids})
    rows.sort(key=lambda r: (-r['years'], -r['shi'], r['law'], r['article']))
    os.makedirs(os.path.join(BASE, 'data'), exist_ok=True)
    json.dump(shi, open(os.path.join(BASE, 'data', 'shi.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    json.dump(rows, open(os.path.join(BASE, 'data', 'jobun.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    n_c = sum(1 for s in shi if s['cites'])
    print(f'肢 {len(shi)}（バンクと対応しない {miss}）、条文を拾えた肢 {n_c}（{n_c*100//max(len(shi),1)}％）、条文 {len(rows)}')
    for r in rows[:15]:
        print(f"{r['law']}第{r['article']}条 {r['years']}年度/{r['shi']}肢")


if __name__ == '__main__':
    main()
