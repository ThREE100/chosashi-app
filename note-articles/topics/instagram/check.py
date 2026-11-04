#!/usr/bin/env python3
"""data.json と生成物の機械チェック。python3 note-articles/topics/instagram/check.py"""
import json, os, re, glob
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
D = json.load(open(os.path.join(H, 'data.json'), encoding='utf-8'))
ng = []
ids = sorted(os.path.basename(p)[:5] for p in glob.glob(os.path.join(T, 'K*_*.md')))
for i in ids:
    if i not in D: ng.append(f'{i}: data.jsonにない'); continue
    d = D[i]
    for k in ['l1','l2','emph','band','scene','hook','lead','points','close','tags']:
        if not d.get(k): ng.append(f'{i}: {k} が空')
    if d.get('emph') and d['emph'] not in d.get('l2',''): ng.append(f'{i}: emphがl2に含まれない')
    for k, mx in (('l1',12),('l2',10),('band',18),('sub',20)):
        t = d.get(k,'')
        if len(t) > mx: ng.append(f'{i}: {k}が{mx}字超（{len(t)}）')
        if re.search(r'[A-Za-z0-9０-９Ａ-Ｚａ-ｚ]', t): ng.append(f'{i}: {k}に英数字 {t}')
    if not 3 <= len(d.get('points',[])) <= 4: ng.append(f'{i}: pointsは3〜4個')
    if not 3 <= len(d.get('tags',[])) <= 5: ng.append(f'{i}: tagsは3〜5個')
    if re.search(r'[぀-ヿ一-鿿]', d.get('scene','')): ng.append(f'{i}: sceneは英語で')
    body = '\n'.join([d.get('hook',''), d.get('lead',''), *d.get('points',[]), d.get('close','')])
    for w in ['予備校の解答例', '教材としてまとめた', '合格するまで', '誤答', '解答の回数', '間違えた回数']:
        if w in body: ng.append(f'{i}: 禁止語「{w}」')
    if 'プロフィール' not in d.get('close',''): ng.append(f'{i}: closeにプロフィールのリンク案内がない')
    p = os.path.join(H, f'{i}.md')
    if not os.path.exists(p): ng.append(f'{i}: 生成物がない')
    else:
        s = open(p, encoding='utf-8').read()
        cap = s.split('```')[-2]
        if len(cap) > 2200: ng.append(f'{i}: キャプション2200字超')
for i in D:
    if i not in ids: ng.append(f'{i}: data.jsonにあるが記事がない')
print('NG', len(ng))
for x in ng: print(' ', x)
