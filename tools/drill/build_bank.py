#!/usr/bin/env python3
"""work/ 配下の中間データから 一問一答バンク data/items.json を作る。

入力:  work/derived_ok.json      機械的に導いた標準形式の問題（313問）
       work/batch_out_*.json     LLM が肢ごとの正誤を確定した問題（対話・個数・空欄補充など）。
                                 batch_out_fix.json は公式正答と解説記事が食い違う問題を、解説記事（現行法令）基準で再確定した分で、他を上書きする
       work/topics.json          問題ごとの論点ラベル
出力:  data/items.json           バンク（重複を統合済み）
       work/dedup_report.json    統合した肢と、似ているが結論が逆の肢（対比ペア）の一覧
重複の扱い: 正規化した文の文字2-gram類似度が 0.85 以上で正誤が同じ → 1肢に統合し、出典を束ねる（出題回数=freq）。
            類似度 0.55 以上で正誤が逆 → 統合せず、互いを pair として結び付ける（引っかけの対比用）。
"""
import glob, json, os, re, unicodedata, collections, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WORK = os.path.join(HERE, 'work'); OUT = os.path.join(HERE, 'data')
os.makedirs(OUT, exist_ok=True)
MERGE_T = 0.85; PAIR_T = 0.55


def subject_of(qno):
    return '民法' if qno <= 3 else ('不動産登記法' if qno <= 19 else '土地家屋調査士法')


def qlabel(qid):  # chosashi_R07_q01 -> R07-Q01
    m = re.match(r'chosashi_(\w+)_q(\d+)', qid)
    return f'{m.group(1)}-Q{int(m.group(2)):02d}'


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = re.sub(r'^【[^】]*】', '', s)
    s = re.sub(r'[\s、。,.，．「」『』（）()\[\]・:：;；ー−\-]', '', s)
    return s


def grams(s):
    return {s[i:i + 2] for i in range(len(s) - 1)} or {s}


def context_of(stem):
    """設問のテーマ（「◯◯に関する次のアからオまで…」の◯◯）を肢の頭に補う"""
    s = re.sub(r'\s+', ' ', stem)
    m = re.match(r'^(.{2,40}?)(?:に関する|についての|について述べた|における|に係る)', s)
    if m and not re.search(r'次の|アから|対話', m.group(1)):
        return m.group(1)
    return None


def premise_of(stem):
    tags = []
    if re.search(r'判例の趣旨', stem): tags.append('判例')
    return ''.join(f'【{t}】' for t in tags)


def main():
    topics = json.load(open(os.path.join(WORK, 'topics.json'), encoding='utf-8')) if os.path.exists(os.path.join(WORK, 'topics.json')) else {}
    raw = {x['id']: x for x in json.load(open(os.path.join(WORK, 'questions_raw.json'), encoding='utf-8'))}
    cands = []   # 統合前の肢
    # 1) 機械導出
    for q in json.load(open(os.path.join(WORK, 'derived_ok.json'), encoding='utf-8')):
        r = raw[q['id']]
        ctx = context_of(q['stem']); pre = premise_of(q['stem'])
        for lab, text in q['alts'].items():
            cands.append({'qid': q['id'], 'label': lab, 'statement': pre + text, 'context': ctx, 'truth': q['truth'][lab],
                          'basis': '', 'status': 'verified', 'note_path': r['note_path']})
    # 2) LLM 確定分
    llm = {}   # 後のファイル（batch_out_fix.json＝現行法で再確定した分）が同じ問題を上書きする
    for f in sorted(glob.glob(os.path.join(WORK, 'batch_out_*.json'))):
        for q in json.load(open(f, encoding='utf-8')):
            llm[q['id']] = q
    if True:
        for q in llm.values():
            r = raw[q['id']]
            conf = q.get('confidence', 'low')
            for it in q['items']:
                if it.get('truth') is None:
                    continue
                st = {'high': 'verified', 'medium': 'provisional'}.get(conf, 'hold')
                cands.append({'qid': q['id'], 'label': it['label'], 'statement': it['statement'], 'context': q.get('stem_short'),
                              'truth': bool(it['truth']), 'basis': it.get('basis', ''), 'status': st, 'note_path': r['note_path'],
                              'note_hint': it.get('note_hint', ''), 'issues': q.get('issues', '')})
    # 2.5) 個別の上書き（現行法の結論に確認が必要な肢を保留にする等）。data/overrides.json
    ov_path = os.path.join(OUT, 'overrides.json')
    if os.path.exists(ov_path):
        ov = {(o['q'], o['label']): o for o in json.load(open(ov_path, encoding='utf-8'))}
        for c in cands:
            o = ov.get((c['qid'], c['label'])) or ov.get((c['qid'], '*'))
            if o:
                if o.get('status'):
                    c['status'] = o['status']
                if o.get('suffix'):
                    c['statement'] += o['suffix']
                if o.get('reason') and o.get('status') == 'hold':
                    c['basis'] = (c['basis'] + ' ／ ' if c['basis'] else '') + '【要確認】' + o['reason']
    # 3) 重複の統合
    for c in cands:
        c['n'] = norm(c['statement']); c['g'] = grams(c['n'])
    inv = collections.defaultdict(list)
    for i, c in enumerate(cands):
        for g in c['g']:
            inv[g].append(i)
    parent = list(range(len(cands)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    pairs = set(); merged_log = []
    for i, c in enumerate(cands):
        cnt = collections.Counter()
        for g in c['g']:
            for j in inv[g]:
                if j > i: cnt[j] += 1
        for j, k in cnt.items():
            d = cands[j]
            sim = k / (len(c['g']) + len(d['g']) - k)
            if sim >= MERGE_T and c['truth'] == d['truth'] and c['qid'] != d['qid']:
                a, b = find(i), find(j)
                if a != b:
                    parent[b] = a; merged_log.append({'sim': round(sim, 2), 'a': c['statement'], 'b': d['statement'], 'q': [c['qid'], d['qid']]})
            elif sim >= PAIR_T and c['truth'] != d['truth']:
                pairs.add((i, j, round(sim, 2)))
    groups = collections.defaultdict(list)
    for i in range(len(cands)):
        groups[find(i)].append(i)
    items = []; gid = {}
    order = sorted(groups.values(), key=lambda g: (cands[g[0]]['qid'], cands[g[0]]['label']))
    for k, g in enumerate(order, 1):
        iid = f'D{k:04d}'
        for i in g: gid[i] = iid
        head = cands[g[0]]
        qno = int(re.search(r'_q(\d+)', head['qid']).group(1))
        sources = [{'q': qlabel(cands[i]['qid']), 'label': cands[i]['label'], 'note_path': cands[i]['note_path'],
                    'hint': cands[i].get('note_hint', '')} for i in g]
        # 出題順の新しい順に並べる
        sources.sort(key=lambda s: s['q'], reverse=True)
        stat = {c: sum(1 for i in g if cands[i]['status'] == c) for c in ('verified', 'provisional', 'hold')}
        status = 'verified' if stat['verified'] else ('provisional' if stat['provisional'] else 'hold')
        basis = next((cands[i]['basis'] for i in g if cands[i]['basis']), '')
        ctx = head['context']
        text = head['statement']
        if ctx and ctx not in text:
            text = f'〔{ctx}〕' + text
        items.append({'id': iid, 'subject': subject_of(qno), 'topic': topics.get(head['qid'], '未分類'),
                      'statement': text, 'truth': head['truth'], 'basis': basis, 'status': status,
                      'freq': len({cands[i]['qid'] for i in g}), 'sources': sources})
    by_id = {it['id']: it for it in items}
    pair_rows = []
    for i, j, sim in pairs:
        a, b = gid[i], gid[j]
        if a == b: continue
        by_id[a].setdefault('pair', [])
        by_id[b].setdefault('pair', [])
        if b not in by_id[a]['pair']: by_id[a]['pair'].append(b)
        if a not in by_id[b]['pair']: by_id[b]['pair'].append(a)
        pair_rows.append({'sim': sim, 'a': a, 'b': b})
    meta = {'title': '土地家屋調査士 択一 一問一答バンク', 'built_from_questions': len(raw), 'raw_items': len(cands), 'items': len(items),
            'merged_away': len(cands) - len(items), 'status_counts': dict(collections.Counter(x['status'] for x in items))}
    json.dump({'meta': meta, 'items': items}, open(os.path.join(OUT, 'items.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'merged': merged_log, 'pairs': pair_rows}, open(os.path.join(WORK, 'dedup_report.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))


main()
