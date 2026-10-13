import json,re,sys,collections
S='/tmp/sokatsu_work/'
g=sys.argv[1]
ids=[o['id'] for o in json.load(open(S+f'dos/bundle_{g}.json'))]
md=open(S+f'out/{g}.md',encoding='utf-8').read()
tags=json.load(open(S+f'out/{g}_tags.json',encoding='utf-8'))
ok=True
# 肢ごとの判定行: 行頭の "- D0000 〇|×"
lines=[l for l in md.split('\n') if re.match(r'^- D\d{4} [〇×]',l)]
cnt=collections.Counter(re.match(r'^- (D\d{4})',l).group(1) for l in lines)
miss=[i for i in ids if cnt[i]!=1]
extra=[i for i in cnt if i not in ids]
print('items',len(ids),'判定行',len(lines),'欠落/重複',miss,'余計',extra)
if miss or extra: ok=False
truth={o['id']:o['truth'] for o in json.load(open(S+f'dos/bundle_{g}.json'))}
for l in lines:
    i=re.match(r'^- (D\d{4}) ([〇×])',l).groups()
    if i[0] in truth and (i[1]=='〇')!=truth[i[0]]:
        print('正誤不一致',i); ok=False
tm=[i for i in ids if i not in tags]
print('tags欠落',tm, 'タグ値',collections.Counter(v.get('primary') if isinstance(v,dict) else v for v in tags.values()))
if tm: ok=False
print('文字数',len(md))
for pat,name in [(r'^\|.*\|$','表'),(r'最判|最大判|最決|大判|先例|登記研究|民三第|民二第|通達番号','番号系'),(r'[ぁ-んァ-ヶ一-龥]\([ぁ-んァ-ヶ一-龥]','半角括弧'),(r'ドリル','ドリル語')]:
    m=[l[:60] for l in md.split('\n') if re.search(pat,l)]
    if m: print('要確認',name,len(m),m[:3])
print('OK' if ok else 'NG')
