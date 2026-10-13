import json,re,collections
d=json.load(open('all.json'))
def grp(o):
    s=o['subject']; t=o['topic']; st=o['statement']
    if s=='民法':
        if t in ('共有・所有権・占有',): return 'M2_bukken_kyoyu'
        if t in ('物権変動・対抗要件','用益権・担保物権','相続・親族'): return 'M2_bukken_kyoyu' if False else 'M3_taikou_tanpo'
        return 'M1_sosoku'   # 意思表示, 代理, 時効
    if s=='土地家屋調査士法': return 'C1_chousashi'
    if t.startswith('申請総論'):
        if re.search(r'識別情報|電子|添付|証明書|還付|法定相続|住所を証|会社法人等|資格を証|原本|作成後|不動産番号|電子署名|印鑑|権限を証する|所有権を有することを証|情報を提供|情報の提供',st): return 'P_B_tenpu'
        return 'P_A_shinsei'
    if t.startswith('表題部所有者'): return 'P_A_shinsei'
    if t.startswith('登記制度') or t.startswith('登録免許税'): return 'P_B_tenpu'
    if t.startswith('筆界特定') or t.startswith('土地の表題') or t.startswith('土地の滅失'): return 'P_C_tochi'
    if t.startswith('土地の分筆'): return 'P_D_bunpitsu'
    if t.startswith('建物の認定') or t.startswith('建物図面'): return 'P_E_nintei'
    if t.startswith('建物の分割'):
        if '合体' in st: return 'P_F2_gattai'
        if re.search(r'合併|分割|分棟',st): return 'P_F1_bunkatsu_gappei'
        return 'P_E_nintei'
    if t.startswith('区分建物'):
        if re.search(r'敷地権|敷地利用権|規約敷地|分離処分',st): return 'P_G1_shikichiken'
        return 'P_G2_kubun'
    return 'UNK'
for o in d: o['group']=grp(o)
c=collections.Counter(o['group'] for o in d); print(c)
json.dump(d,open('all.json','w'),ensure_ascii=False,indent=1)
for g in c:
    json.dump([o for o in d if o['group']==g],open(f'bundle_{g}.json','w'),ensure_ascii=False,indent=1)
