# -*- coding: utf-8 -*-
# 書式（記述）レビュー用データ kijutsu.json を生成。
#  - kakomon_data.json の descriptive（土地10＋建物10）から問題文・模範解答テキスト
#  - 図面画像があれば problemImages / answerImages に紐付け（public/kijutsu/<id>/ ）
import json, os, collections

BASE = r"C:\Users\m2100\OneDrive\Desktop\Claude cowork\chosashi_app"
SRC = json.load(open(os.path.join(BASE, 'kakomon_data.json'), encoding='utf-8'))

def year_label(code):
    era = code[0]; n = int(code[1:])
    if era == 'H': return ('平成元年' if n == 1 else f'平成{n}年')
    if era == 'R': return ('令和元年' if n == 1 else f'令和{n}年')
    return code

def year_int(code):
    era = code[0]; n = int(code[1:])
    return (1988 + n) if era == 'H' else (2018 + n) if era == 'R' else 0

# 画像が用意できている問題（idごと）。public/kijutsu/<dir>/ に配置済み。
IMAGE_SETS = {
    'R06_建物': {
        'dir': 'kijutsu/R06-tatemono',
        'problem': [f'q{i}.png' for i in range(1, 8)],
        'answer': ['a1.png', 'a2.png'],
    },
}

out = []
for q in SRC.get('descriptive', []):
    yc = q['yearCode']
    cat = q.get('category')  # '土地' or '建物'
    key = f"{yc}_{cat}"
    imgs = IMAGE_SETS.get(key)
    problem_images, answer_images = [], []
    if imgs:
        problem_images = [f"{imgs['dir']}/{f}" for f in imgs['problem']]
        answer_images = [f"{imgs['dir']}/{f}" for f in imgs['answer']]
    out.append({
        'id': q.get('id') or f"kijutsu_{yc}_{cat}",
        'yearCode': yc,
        'yearLabel': year_label(yc),
        'category': cat,
        'questionNo': q.get('questionNo'),
        'problemText': (q.get('fullText') or '').strip(),
        'modelAnswerText': (q.get('explanation') or '').strip(),
        'problemImages': problem_images,
        'answerImages': answer_images,
    })

# 年度新しい順 → 建物→土地
out.sort(key=lambda r: (-year_int(r['yearCode']), 0 if r['category'] == '建物' else 1))

dst_dir = r"C:\Users\m2100\OneDrive\Desktop\Claude cowork\chosashi-app-new\src\data"
payload = {
    'meta': {
        'title': '土地家屋調査士 書式（記述）レビュー',
        'note': '作図は自己採点。模範解答と照合する方式。',
        'count': len(out),
        'withImages': sum(1 for r in out if r['problemImages']),
    },
    'problems': out,
}
json.dump(payload, open(os.path.join(dst_dir, 'kijutsu.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

print(f"書式: {len(out)}問")
print(f"category別: {dict(collections.Counter(r['category'] for r in out))}")
print(f"画像つき: {sum(1 for r in out if r['problemImages'])}問")
print(f"模範解答テキスト欠損: {sum(1 for r in out if not r['modelAnswerText'])}問")
