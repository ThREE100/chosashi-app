"""章ごとに：ファイル名の論点番号を2桁化、新しい4コマを NAMES に登録、通し番号を記事の順に振り直し、READMEを更新。
usage: reorder.py <n> '<json: [{"fid":..,"topic":"PB-4","slug":"..","line":"README用の1行"}]>'"""
import re, sys, json, subprocess, pathlib
ROOT=pathlib.Path('/home/user/chosashi-app')
n=int(sys.argv[1]); new=json.loads(sys.argv[2]) if len(sys.argv)>2 else []
CH=ROOT/f'note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch{n}'
def pad(s): return re.sub(r'(P[A-G]\d?)-(\d)(?=[_.])',r'\1-0\2',s)
# 1. rename files
for d in (CH, CH/'src'):
    for f in sorted(d.iterdir()):
        if re.match(r'(prompt_4koma_|spec_4koma_|prompt_infographic_)P[A-G]\d?-\d[_.]',f.name):
            nn=pad(f.name)
            if nn!=f.name:
                subprocess.run(['git','mv',str(f),str(d/nn)],cwd=ROOT,check=True)
# 2. gen_infographic.py file names
gi=CH/'src'/'gen_infographic.py'
s=gi.read_text(encoding='utf-8'); s=re.sub(r'prompt_infographic_(P[A-G]\d?)-(\d)\.md',r'prompt_infographic_\1-0\2.md',s); gi.write_text(s,encoding='utf-8')
# 3. build_4koma.py: NAMES
bp=CH/'src'/'build_4koma.py'
s=bp.read_text(encoding='utf-8').split('\n')
i=next(k for k,l in enumerate(s) if l.startswith('NAMES = {'))
j=next(k for k in range(i,len(s)) if s[k].startswith('}'))
ents=[]
for l in s[i+1:j]:
    m=re.match(r'\s*("[^"]+"): \("([^"]+)", "([^"]+)"\),\s*(#.*)?$',l)
    assert m,l
    ents.append([m.group(1),pad(m.group(2)),m.group(3)])
oldnum={}
for e in ents:
    mm=re.match(r'^(.*_4コマ)(\d+)$',e[2]); oldnum[int(mm.group(2))]=None
prefix=re.match(r'^(.*_4コマ)',ents[0][2]).group(1)
old_map={}  # old number -> fid
for e in ents: old_map[int(re.search(r'(\d+)$',e[2]).group(1))]=e[0]
for t in new:
    slug=t['slug']; tp=re.match(r'(P[A-G]\d?)-(\d+)',t['topic']); tn=int(tp.group(2))
    fn=f"prompt_4koma_{tp.group(1)}-{tn:02d}_01_{slug}.md"
    ents.append([f'"{t["fid"]}"',fn,prefix+'0'])
def key(e):
    m=re.search(r'_(P[A-G]\d?)-(\d+)_(\d+)_',e[1]); return (int(m.group(2)),int(m.group(3)))
ents.sort(key=key)
newnum={}
for k,e in enumerate(ents,1):
    e[2]=f'{prefix}{k}'; newnum[e[0]]=k
lines=[f'    {e[0]}: ("{e[1]}", "{e[2]}"),' for e in ents]
s[i+1:j]=lines
txt='\n'.join(s)
txt=txt.replace('sp["_stem"].split("_")[2] +','re.sub(r"(P[A-G]\\d?)-0(\\d)", r"\\1-\\2", sp["_stem"].split("_")[2]) +') if 'split("_")[2] +' in txt and 're.sub(r"(P[A-G]' not in txt else txt
txt=re.sub(r'4コマ\d+本','4コマ%d本'%len(ents),txt,count=1)
bp.write_text(txt,encoding='utf-8')
# 4. README mapping
rp=CH/'README.md'
r=rp.read_text(encoding='utf-8')
r=re.sub(r'prompt_4koma_(P[A-G]\d?)-(\d)_',r'prompt_4koma_\1-0\2_',r)
r=re.sub(r'prompt_infographic_(P[A-G]\d?)-(\d)\.md',r'prompt_infographic_\1-0\2.md',r)
o2n={o:newnum[f] for o,f in old_map.items()}
r=re.sub(r'4コマ(\d+)(?![0-9本])',lambda m:'4コマ%d'%o2n.get(int(m.group(1)),int(m.group(1))),r)
# 新しい4コマの行
for t in new:
    mm=re.search(r'^### 【'+re.escape(t['topic'])+r'】.*$',r,re.M)
    assert mm,t['topic']
    k=newnum[f'"{t["fid"]}"']
    tp=re.match(r'(P[A-G]\d?)-(\d+)',t['topic']); fn=f"prompt_4koma_{tp.group(1)}-{int(tp.group(2)):02d}_01_{t['slug']}.md"
    entry=f"- `{fn}`：4コマ{k}（{t['ids']}）{t['line']}"
    # replace '4コマ：なし' line within this topic's block if present, else insert after heading
    blk_end=re.search(r'\n### |\n## ',r[mm.end():])
    end=mm.end()+(blk_end.start() if blk_end else len(r)-mm.end())
    blk=r[mm.end():end]
    if re.search(r'^- 4コマ：なし.*$',blk,re.M):
        blk=re.sub(r'^- 4コマ：なし.*$',lambda _:entry,blk,count=1,flags=re.M)
    else:
        blk=blk.rstrip('\n')+'\n'+entry+'\n'
    r=r[:mm.end()]+blk+r[end:]
r=r.rstrip('\n')+f"""

## 2026-10-13 追記：全論点に4コマをそろえた（ユーザー指示）

- 4コマのなかった論点に新しい4コマを足した（上の各論点の欄）。既存の4コマ（再利用）がある論点はそのまま。
- 作成済みの4コマは、設計内容のまま。変えたのは、**記事の順に並べるための番号**だけ（論点番号を2桁にそろえたファイル名〈PB-4 → PB-04〉と、4コマの通し番号を記事の順に振り直した保存名）。4コマの中身（セリフ・図・設計メモ）は変えていない。
- 新しい4コマの挿入位置は、各論点の「肢ごとの判定」の直後（記事の順）。
- 肢IDのタグ（結論帯の問題番号、カードや表の小タグ「肢D…」、チェック欄の「（肢D…は〇／×）」）は、作成済みの4コマと同じ形。
"""
rp.write_text(r,encoding='utf-8')
print('ok ch',n,'4koma',len(ents),'new',len(new))
