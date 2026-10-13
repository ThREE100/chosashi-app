import sys, json, collections
sys.path.insert(0,'/home/user/chosashi-app/tools/drill')
import drill
S='/tmp/sokatsu_work/dos/'
bank=drill.load_bank(); logs=drill.read_log(); st=drill.item_state(logs)
hist=collections.defaultdict(list)
for r in logs: hist[r['id']].append(r)
tags=collections.defaultdict(list)
import os
if os.path.exists(drill.TAGS):
    for ln in open(drill.TAGS,encoding='utf-8'):
        try:
            t=json.loads(ln); tags[t.get('id')].append(t)
        except: pass
out=[]
for iid,s in st.items():
    if iid not in bank: continue
    c=drill.review_class(s)
    if c not in ('must','check'): continue
    it=bank[iid]
    ex=[]
    for sr in it.get('sources',[])[:3]:
        q=drill.article_quote(sr.get('note_path',''),sr.get('label',''))
        ex.append({'q':sr['q'],'label':sr.get('label',''),'path':sr.get('note_path',''),
                   'section':(q or {}).get('section'),'summary':(q or {}).get('summary')})
    out.append({'id':iid,'class':c,'subject':it['subject'],'topic':it['topic'],'statement':it['statement'],
      'premise':it.get('premise'),'truth':it['truth'],'basis':it.get('basis'),'status':it.get('status'),'pair':it.get('pair'),
      'W':drill.wrong_total(s),'c':s['cons'],'n':s['n'],'miscon':s['miscon'],'unknown':s['unknown'],
      'history':[ (r['t'][5:10], r['ans'], r['res'][0]) for r in hist[iid]],
      'expl':ex,'tags':[t.get('tag') for t in tags[iid]]})
json.dump(out,open(S+'all.json','w'),ensure_ascii=False,indent=1)
print(len(out), collections.Counter((o['class']) for o in out))
print(collections.Counter(o['subject'] for o in out))
tc=collections.Counter((o['subject'],o['topic']) for o in out)
for k,v in sorted(tc.items(), key=lambda x:(x[0][0],-x[1])): print(k,v)
