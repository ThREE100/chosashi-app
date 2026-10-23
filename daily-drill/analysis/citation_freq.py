"""過去問（平成17年度〜令和8年度）の択一式解説記事で、各条文が何問で引用されたかを数える。
不動産登記法（「法第○条」）・土地家屋調査士法・民法（「民法第○条」）。削除条は除く。
出力: analysis/citations.json（優先度の目安。引用の書き方の違いで、実際より少なく出ることがある）
使い方: python3 daily-drill/analysis/citation_freq.py"""
import re,glob,os,json,collections
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','note-articles')
L=os.path.join(ROOT,'laws')+'/'
def arts(files,pat):
    out=[];seen=set()
    for fn in files:
        t=open(L+fn,encoding='utf-8').read()
        ms=list(re.finditer(pat,t,re.M))
        for i,m in enumerate(ms):
            h=m.group(1)
            if h in seen: return out
            seen.add(h)
            end=ms[i+1].start() if i+1<len(ms) else len(t)
            body=t[m.end():end]
            body=re.sub(r'（[^）]{1,30}）\s*$','',body.strip())
            out.append((h,body.strip()=='削除' or body.strip().startswith('削除')))
    return out
P=r'^#{3,6} (第\d+条(?:の\d+)*)'
H=arts(['fudousan-touki-hou.md'],P); C=arts(['chousashi-hou.md'],P)
M=arts(['minpou-1-soukyoku-bukken.md','minpou-2-saiken.md','minpou-3-shinzoku-souzoku.md'],P)
for n,a in (('不動産登記法',H),('調査士法',C),('民法',M)):
    print(n,'見出し数',len(a),'うち削除',sum(d for _,d in a),'現行',len([1 for _,d in a if not d]))
valid={'H':{h for h,d in H if not d},'C':{h for h,d in C if not d},'M':{h for h,d in M if not d}}
def norm(n,s): return '第%s条%s'%(n,s or '')
cit={'H':collections.defaultdict(set),'C':collections.defaultdict(set),'M':collections.defaultdict(set)}
EXC=('調査士','区分所有','民事執行','会社','農地','登録免許税','土地区画整理','破産','借地借家','信託','仮登記担保','施行','行政')
for d in sorted(os.path.basename(x) for x in glob.glob(os.path.join(ROOT,'*-mondai'))):
    if not re.match(r'^[rh]\d+-mondai$',d): continue
    for f in sorted(glob.glob(os.path.join(ROOT,d,'q*.md'))):
        q=re.match(r'q(\d+)',os.path.basename(f)).group(1)
        t=open(f,encoding='utf-8').read()
        key=d.split('-')[0]+'Q'+q
        for m in re.finditer(r'民法(?:第)?(\d+)条(の\d+)?',t): cit['M'][norm(m.group(1),m.group(2))].add(key)
        for m in re.finditer(r'土地家屋調査士法(?:第)?(\d+)条(の\d+)?|調査士法(?:第)?(\d+)条(の\d+)?',t):
            n=m.group(1) or m.group(3); s=m.group(2) or m.group(4); cit['C'][norm(n,s)].add(key)
        for m in re.finditer(r'(.{0,8}?)法(?:第)?(\d+)条(の\d+)?',t):
            pre=m.group(1)
            if any(pre.endswith(x) or x in pre[-6:] for x in EXC): continue
            if pre.endswith('民'): continue
            cit['H'][norm(m.group(2),m.group(3))].add(key)
res={}
for k,name,vv in (('H','不動産登記法',valid['H']),('C','調査士法',valid['C']),('M','民法',valid['M'])):
    ok={a:len(s) for a,s in cit[k].items() if a in vv}
    print(name,'過去問の解説で引用された条:',len(ok),'/ 現行',len(vv))
    top=sorted(ok.items(),key=lambda x:-x[1])[:12]
    print('  上位',top)
    res[name]={'total_current':len(vv),'cited':ok}
json.dump(res,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'citations.json'),'w',encoding='utf-8'),ensure_ascii=False)
