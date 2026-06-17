# -*- coding: utf-8 -*-
# 択一データ正本 takuitsu.json を生成する。
#  - kakomon_data.json（H27〜R06の193問）
#  - kakomon_extra/H24.json, H26.json（構造化済みの旧年度40問）
#  - official_answers.json（法務省公式正答）で correctAnswer を検証
import json, os, glob, collections

BASE = r"C:\Users\m2100\OneDrive\Desktop\Claude cowork\chosashi_app"
SRC = json.load(open(os.path.join(BASE, 'kakomon_data.json'), encoding='utf-8'))
OFF = json.load(open(os.path.join(BASE, 'official_answers.json'), encoding='utf-8'))

def year_label(code):
    era = code[0]; n = int(code[1:])
    if era == 'H': return ('平成元年' if n == 1 else f'平成{n}年')
    if era == 'R': return ('令和元年' if n == 1 else f'令和{n}年')
    return code

def year_int(code):
    # 西暦化（H=1988+n, R=2018+n）
    era = code[0]; n = int(code[1:])
    if era == 'H': return 1988 + n
    if era == 'R': return 2018 + n
    return 0

def subject_by_no(qno):
    if qno <= 3: return '民法'
    if qno >= 19: return '土地家屋調査士法'
    return '不動産登記法'

def subject_by_genre(genre):
    g = genre or ''
    if g.startswith('民法'): return '民法'
    if '調査士法' in g: return '土地家屋調査士法'
    if g.startswith('不動産登記法') or '登記' in g: return '不動産登記法'
    return None

def official(yc, qno):
    if yc in OFF and isinstance(OFF[yc], list) and len(OFF[yc]) >= qno:
        return OFF[yc][qno - 1]
    return None

def clean(s):
    return (s or '').strip()

out = []
mismatch = []
no_alts = []

# --- 1) kakomon_data.json（193問） ---
for q in SRC['questions']:
    yc = q['yearCode']; qno = q['questionNo']
    off = official(yc, qno)
    src_ans = q.get('correctAnswer')
    ans = off if off is not None else src_ans
    if off is not None and src_ans is not None and off != src_ans:
        mismatch.append(f"{yc} 問{qno}: 元={src_ans}/公式={off}→公式採用")
    alts = q.get('alts') or []
    if not alts:
        no_alts.append(f"{yc} 問{qno}")
    out.append({
        "id": q['id'],
        "yearCode": yc,
        "yearLabel": year_label(yc),
        "year": q.get('year') or year_int(yc),
        "questionNo": qno,
        "subject": subject_by_no(qno),
        "genre": None,
        "stem": clean(q.get('stem') or q.get('fullText')),
        "alts": [{"label": a.get('label'), "text": clean(a.get('text'))} for a in alts],
        "combos": [{"no": c.get('no'), "text": c.get('text')} for c in (q.get('combos') or [])],
        "correctAnswer": ans,
        "explanation": clean(q.get('explanation')),
    })

# --- 2) kakomon_extra（H24, H26 など構造化済み旧年度） ---
extra_mismatch = []
for p in sorted(glob.glob(os.path.join(BASE, 'kakomon_extra', '*.json'))):
    d = json.load(open(p, encoding='utf-8'))
    yc = d.get('yearCode')
    if not yc:
        continue
    for q in d['questions']:
        qno = q['questionNo']
        off = official(yc, qno)
        src_ans = q.get('correctAnswer')
        ans = off if off is not None else src_ans
        if off is not None and src_ans is not None and off != src_ans:
            extra_mismatch.append(f"{yc} 問{qno}: 元={src_ans}/公式={off}")
        genre = q.get('genre')
        alts = q.get('alts') or []
        if not alts:
            no_alts.append(f"{yc} 問{qno}")
        out.append({
            "id": f"chosashi_{yc}_q{qno:02d}",
            "yearCode": yc,
            "yearLabel": year_label(yc),
            "year": d.get('year') or year_int(yc),
            "questionNo": qno,
            "subject": subject_by_genre(genre) or subject_by_no(qno),
            "genre": genre,
            "stem": clean(q.get('stem')),
            "alts": [{"label": a.get('label'), "text": clean(a.get('text'))} for a in alts],
            "combos": [{"no": c.get('no'), "text": c.get('text')} for c in (q.get('combos') or [])],
            "correctAnswer": ans,
            "explanation": clean(q.get('explanation')),
        })

# 年度→新しい順、問番号昇順
out.sort(key=lambda r: (-year_int(r['yearCode']), r['questionNo']))

dst_dir = r"C:\Users\m2100\OneDrive\Desktop\Claude cowork\chosashi-app-new\src\data"
os.makedirs(dst_dir, exist_ok=True)
payload = {
    "meta": {
        "title": "土地家屋調査士 択一過去問",
        "source": "kakomon_data.json + kakomon_extra + official_answers.json(法務省公式正答)",
        "count": len(out),
        "years": sorted({r['yearCode'] for r in out}, key=year_int),
    },
    "questions": out,
}
json.dump(payload, open(os.path.join(dst_dir, 'takuitsu.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

# レポート
print(f"生成: {len(out)}問")
print(f"correctAnswer欠損: {sum(1 for r in out if r['correctAnswer'] is None)}")
print(f"explanation欠損: {sum(1 for r in out if not r['explanation'])}")
print(f"選択肢(alts)無し: {len(no_alts)}件")
print(f"年度別: {dict(sorted(collections.Counter(r['yearCode'] for r in out).items(), key=lambda x: year_int(x[0])))}")
print(f"分野別: {dict(collections.Counter(r['subject'] for r in out))}")
print(f"kakomon_data 公式不一致: {len(mismatch)} / kakomon_extra 公式不一致: {len(extra_mismatch)} {extra_mismatch[:10]}")
