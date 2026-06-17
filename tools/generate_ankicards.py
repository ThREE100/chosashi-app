# -*- coding: utf-8 -*-
import json, os, collections
d=json.load(open('textbook_data.json',encoding='utf-8'))
chapters={c['id']:c['title'].strip().rstrip('·').strip() for c in d['chapters']}
chap_order=[{'id':c['id'],'no':c.get('no'),'title':chapters[c['id']]} for c in d['chapters']]

ox=[]; bad=[]
for q in d['questions']:
    exp=(q.get('explanation') or '').strip()
    if exp.startswith('【正】'): correct=True
    elif exp.startswith('【誤】'): correct=False
    else: correct=None; bad.append(q.get('id'))
    ox.append({
        'id': q['id'],
        'chapterId': q.get('chapterId'),
        'chapter': chapters.get(q.get('chapterId'),''),
        'stem': (q.get('stem') or '').strip(),
        'correct': correct,            # True=○(正しい記述), False=×(誤った記述)
        'explanation': exp,
        'tags': q.get('tags') or [],
    })

terms=[]
for t in d['terms']:
    terms.append({
        'id': t['id'],
        'chapterId': t.get('chapterId'),
        'chapter': chapters.get(t.get('chapterId'),''),
        'term': (t.get('term') or '').strip(),
        'yomi': (t.get('yomi') or '').strip(),
        'definition': (t.get('definition') or '').strip(),
        'cautions': (t.get('cautions') or '').strip(),
    })

dst=r"C:\Users\m2100\OneDrive\Desktop\Claude cowork\chosashi-app-new\src\data"
os.makedirs(dst,exist_ok=True)
payload={
    'meta':{'title':'土地家屋調査士 暗記','oxCount':len(ox),'termCount':len(terms),
            'source':'textbook_data.json（正答は解説の【正】【誤】から判定）'},
    'chapters':chap_order,
    'ox':ox,
    'terms':terms,
}
json.dump(payload,open(os.path.join(dst,'ankicards.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)

print(f"ox={len(ox)} (○{sum(1 for o in ox if o['correct'] is True)} / ×{sum(1 for o in ox if o['correct'] is False)} / 不明{len(bad)})")
print(f"terms={len(terms)}")
print(f"章別ox: {dict(collections.Counter(o['chapter'] for o in ox))}")
print(f"判定不明: {bad}")
