#!/usr/bin/env python3
"""解説文の長い段落を、文の区切り（。）で複数の段落に分ける。

使い方: python split_paragraphs.py <記事.md> [--write] [--limit 125] [--target 90]
- 対象は「問題文の引用の後の区切り線」から「### まとめ」の前の区切り線までの解説文（見出し・引用・箇条書き・区切り線は除く）。
- 段落の長さが --limit 文字（およそ5行）を超えたら、--target 文字前後になるよう、「。」の位置でできるだけ均等に分ける。
- 「」（）の中の「。」では分けない。
"""
import re, sys, argparse

def sentences(p):
    out=[]; cur=''; depth=0
    for ch in p:
        cur+=ch
        if ch in '「（': depth+=1
        elif ch in '」）': depth=max(0,depth-1)
        elif ch=='。' and depth==0:
            out.append(cur); cur=''
    if cur: out.append(cur)
    return out

def split_para(p, limit, target):
    if len(p)<=limit: return [p]
    ss=sentences(p)
    if len(ss)<2: return [p]
    n=max(2,round(len(p)/target))
    n=min(n,len(ss))
    # 動的計画法で、各段落の長さが target に近くなる分割点を選ぶ
    best=None
    import itertools
    L=len(ss); pre=[0]
    for s in ss: pre.append(pre[-1]+len(s))
    from functools import lru_cache
    @lru_cache(None)
    def f(i,k):
        if k==1: return (abs(pre[L]-pre[i]-target)**2,(L,))
        res=None
        for j in range(i+1,L-k+2):
            c,rest=f(j,k-1)
            c+=abs(pre[j]-pre[i]-target)**2
            if res is None or c<res[0]: res=(c,(j,)+rest)
        return res
    _,cuts=f(0,n)
    out=[];i=0
    for j in cuts:
        out.append(''.join(ss[i:j])); i=j
    return [x for x in out if x]

def process(text, limit=125, target=90):
    L=text.split('\n')
    # 解説文の範囲
    q_end=next(i for i,l in enumerate(L) if l.startswith('>'))
    while q_end+1<len(L) and L[q_end+1].startswith('>'): q_end+=1
    s=next(i for i in range(q_end,len(L)) if L[i].strip()=='---')+1
    e=next(i for i,l in enumerate(L) if re.match(r'^### まとめ',l))
    out=L[:s]; changed=0
    for l in L[s:e]:
        plain = l.strip() and not l.startswith(('#','>','-','---','※','|'))
        if plain and len(l)>limit:
            parts=split_para(l,limit,target)
            if len(parts)>1: changed+=1
            out.append(('\n\n').join(parts))
        else: out.append(l)
    out+=L[e:]
    return '\n'.join(out),changed

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--write',action='store_true')
    ap.add_argument('--limit',type=int,default=125); ap.add_argument('--target',type=int,default=90)
    a=ap.parse_args()
    t=open(a.file).read(); new,c=process(t,a.limit,a.target)
    print(f'{c}段落を分割')
    if a.write: open(a.file,'w').write(new)
    else: print(new)
