import json,collections,sys
S='/tmp/sokatsu_work/dos/'
d=json.load(open(S+'all.json'))
ck=json.load(open('/home/user/chosashi-app/tools/drill/data/article_checks.json'))
find=collections.defaultdict(list)
for f in ck['findings']:
    if f.get('resolved'): continue
    find[(f['note_path'],f['label'])].append(f)
RES={'k':'正解','m':'誤解(逆に答えた)','u':'？(わからない)'}
byg=collections.defaultdict(list)
for o in d: byg[o['group']].append(o)
for g,L in byg.items():
    out=[]
    for o in sorted(L,key=lambda x:x['id']):
        h=' → '.join(f"{a}:{ {'o':'〇','x':'×','?':'？'}[b] }({RES[c]})" for a,b,c in o['history'])
        out.append(f"=== {o['id']}｜{o['subject']}／{o['topic']}｜バンクの正解={'〇(正しい記述)' if o['truth'] else '×(誤った記述)'}｜誤答通算W={o['W']}・その後の連続正解c={o['c']}｜区分={'要復習' if o['class']=='must' else 'チェック'}")
        out.append("回答履歴: "+h)
        out.append("出典: "+'、'.join(f"{e['q']}{e['label']}" for e in o['expl']))
        if o.get('premise'): out.append("【前提条件】"+o['premise'])
        out.append("肢: "+o['statement'])
        if o.get('pair'): out.append("対比肢(結論が逆の類似肢): "+', '.join(o['pair']))
        for e in o['expl']:
            out.append(f"【記事の解説 {e['q']}{e['label']}（{e['path']}）】")
            out.append((e['section'] or '(取得できず)')[:1800])
            if e['summary']: out.append("記事のまとめ: "+e['summary'].strip())
            for f in find.get((e['path'],e['label']),[]):
                out.append(f"⚠条文照合の未処理指摘[{f['severity']}]: {f['problem']} ／原文: {f.get('law_ref','')} ／訂正案: {f.get('proposal','')}")
        out.append('')
    open(S+f'bundle_{g}.txt','w').write('\n'.join(out))
    print(g,len(L),len('\n'.join(out)))
