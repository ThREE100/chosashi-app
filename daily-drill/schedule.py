"""毎日ドリル（朝）の出題スケジュール（優先度順）を schedule/ に作る。
前提（変えるときは下の定数と引数）:
- 朝のドリルは毎日（土日も）。第1日 = START（既定 2026-10-26 月）。第1〜7日は作成済み。
- 模試の前日 = END（既定 2027-06-12）。
- 民法は、過去問の解説で引用された条文だけ。不動産登記法・調査士法は本則全部（引用ありを先に、引用なしは後）。
- 空欄補充は新しい条文のまとまり（ユニット）を毎日1つ。択一は、前日の空欄補充のユニット（同じ日に同じ分野を出さない）。
- 土曜：択一式の小テスト（20問20分。民法3・不動産登記法16・調査士法1）、日曜：復習記事。
- 夜は 放射→交点→申請書→垂線の足→平行線→面積→申請書 の7日周期（型は進度に応じて増やす）。
出力: schedule/schedule.md, schedule/schedule.csv, schedule/units.json
使い方: python3 daily-drill/schedule.py [開始日 YYYY-MM-DD] [終了日 YYYY-MM-DD]"""
import csv
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lawtext import article  # noqa: E402

START = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.date(2026, 10, 26)
END = datetime.date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else datetime.date(2027, 6, 12)
WD = '月火水木金土日'
HO, CH, MI = '不動産登記法', '土地家屋調査士法', '民法'
MAXN, GAP = 4, 3     # 1ユニットの最大条数、条番号の飛びの許容

cit = json.load(open(os.path.join(HERE, 'analysis', 'citations.json'), encoding='utf-8'))
# 第1〜7日に作成済みのユニット（法令, 条）
DONE = [
    (HO, ['第41条']), (HO, ['第37条', '第38条', '第42条']), (CH, ['第3条']), (HO, ['第2条']), (HO, ['第39条']),
    (CH, ['第22条', '第22条の2', '第23条', '第24条の2', '第25条']), (HO, ['第34条', '第35条', '第36条']),
    (HO, ['第14条']), (HO, ['第40条']), (HO, ['第27条']),
]


def num(a):
    m = re.match(r'第(\d+)条(?:の(\d+))?', a)
    return int(m.group(1)) + (int(m.group(2)) / 100 if m.group(2) else 0)


def all_articles(law):
    p = {'不動産登記法': r'^#{3,6} (第\d+条(?:の\d+)*)', '土地家屋調査士法': r'^#{3,6} (第\d+条(?:の\d+)*)'}
    return None


def chunks(arts, weight):
    """条番号順に並べ、飛びが大きい所・最大条数で区切ってユニットにする。"""
    arts = sorted(arts, key=num)
    out, cur = [], []
    for a in arts:
        if cur and (len(cur) >= MAXN or num(a) - num(cur[-1]) > GAP):
            out.append(cur)
            cur = []
        cur.append(a)
    if cur:
        out.append(cur)
    return [{'arts': c, 'w': sum(weight.get(a, 0) for a in c)} for c in out]


done_set = {(l, a) for l, arts in DONE for a in arts}
units = {}
for law, key in ((HO, '不動産登記法'), (CH, '調査士法'), (MI, '民法')):
    c = cit[key]['cited']
    cited = [a for a in c if (law, a) not in done_set]
    units[law + '_引用あり'] = chunks(cited, c)
    if law != MI:
        # 引用なし（後回し）：本則の全条のうち、引用なし・未作成
        total = cit[key]['total_current']
        import glob
        pat = r'^#{3,6} (第\d+条(?:の\d+)*)'
        fn = {'不動産登記法': 'fudousan-touki-hou.md', '調査士法': 'chousashi-hou.md'}[key]
        t = open(os.path.join(HERE, '..', 'note-articles', 'laws', fn), encoding='utf-8').read()
        names, seen = [], set()
        for m in re.finditer(pat, t, re.M):
            if m.group(1) in seen:
                break
            seen.add(m.group(1))
            names.append(m.group(1))
        rest = [a for a in names if a not in c and (law, a) not in done_set]
        units[law + '_引用なし'] = chunks(rest, {})
for k in units:   # 引用の多い順（同点は条番号順）に並べる
    units[k].sort(key=lambda u: (-u['w'], num(u['arts'][0])))

# 先に「引用あり」、全部終わってから「引用なし」。法令の比率は本番の配点（不動産登記法16：民法3：調査士法1）に合わせ、
# 21日あたり 不動産登記法17：民法3：調査士法1（2026-10-24 改訂。以前の 4：2：1 は民法・調査士法に偏っていた）
queues = {HO: units[HO + '_引用あり'] + units[HO + '_引用なし'], CH: units[CH + '_引用あり'] + units[CH + '_引用なし'], MI: units[MI + '_引用あり']}
pattern = [HO, HO, HO, MI, HO, HO, HO, HO, HO, HO, MI, HO, HO, HO, HO, HO, HO, MI, HO, HO, CH]
order = []
i = 0
while any(queues.values()):
    law = pattern[i % len(pattern)]
    i += 1
    if not queues[law]:
        alt = [l for l in (HO, MI, CH) if queues[l]]
        if not alt:
            break
        law = alt[0]
    u = queues[law].pop(0)
    order.append((law, u))

days = []
d0 = START
cur = d0
n = 8        # 第8日から
# 第1〜7日（作成済み）
done_days = [
    ('不動産登記法 第14条（地図等）', '不動産登記法 第41条（合筆の制限）'),
    ('不動産登記法 第37条・第38条・第42条', '土地家屋調査士法 第3条'),
    ('土地家屋調査士法 第3条', '不動産登記法 第2条（定義）'),
    ('不動産登記法 第2条', '不動産登記法 第39条'),
    ('不動産登記法 第39条・第40条', '土地家屋調査士法 第22条〜第25条'),
    ('土地家屋調査士法 第22条〜第25条', '不動産登記法 第34条〜第36条'),
    ('不動産登記法 第27条・第34条〜第36条', '不動産登記法 第37条・第38条・第42条'),
]
rows = []
for k, (q, c) in enumerate(done_days, 1):
    rows.append({'day': k, 'q': q, 'cloze': c, 'law': '', 'done': True})
prev = '不動産登記法 第37条・第38条・第42条'
for law, u in order:
    label = f'{law} ' + '・'.join(u['arts'])
    rows.append({'day': n, 'q': prev, 'cloze': label, 'law': law, 'done': False, 'arts': u['arts'], 'w': u['w']})
    prev = label
    n += 1
last_first_pass = n - 1
PMCYC = ['筆界点の計算（放射・直線の交点）', '土地の申請書', '建物の申請書', '筆界点の計算（平行線・垂線の足）', '土地の申請書', '建物の申請書', '筆界点の計算（面積の条件）']
for r in rows:
    r['date'] = START + datetime.timedelta(days=r['day'] - 1)
    r['wd'] = WD[r['date'].weekday()]
    r['pm'] = PMCYC[(r['day'] - 1) % 7]
    r['sat'] = '土曜：択一式小テスト（20問20分）' if r['wd'] == '土' else ('日曜：復習記事' if r['wd'] == '日' else '')
total_days = (END - START).days + 1
use = len(rows)
spare = total_days - use
os.makedirs(os.path.join(HERE, 'schedule'), exist_ok=True)
with open(os.path.join(HERE, 'schedule', 'schedule.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['日', '日付', '曜日', '朝・空欄補充（新しい条文）', '朝・択一（前日の空欄補充の条文）', '夜', '土日', '作成状況'])
    for r in rows:
        w.writerow([r['day'], r['date'].isoformat(), r['wd'], r['cloze'], r['q'], r['pm'], r['sat'], '作成済み' if r['done'] else '未作成'])
json.dump({k: v for k, v in units.items()}, open(os.path.join(HERE, 'schedule', 'units.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cnt = {HO: 0, CH: 0, MI: 0}
arts_n = {HO: 0, CH: 0, MI: 0}
for r in rows:
    if not r['done']:
        cnt[r['law']] += 1
        arts_n[r['law']] += len(r['arts'])
md = [f'# 毎日ドリル 出題スケジュール（優先度順）', '',
      f'- 第1日 ＝ {START}（{WD[START.weekday()]}）、模試の前日 ＝ {END}。全 {total_days} 日。朝のドリルは毎日。',
      f'- 第1〜7日は作成済み。第8日以降の新しい条文のまとまり（ユニット）は {len(order)} 個で、第{last_first_pass}日（{START + datetime.timedelta(days=last_first_pass - 1)}）までに1周する。',
      f'- 残りの {max(spare, 0)} 日は、2周目（弱点の復習、条文の組合せ問題）と模試の直前整理に使う。',
      f'- ユニット数：不動産登記法 {cnt[HO]}（{arts_n[HO]}条）、民法 {cnt[MI]}（{arts_n[MI]}条）、土地家屋調査士法 {cnt[CH]}（{arts_n[CH]}条）。',
      '- 民法は、過去問の解説で引用された条文だけ。引用の多いまとまりから順に出す。',
      '- 択一は、前日の空欄補充と同じ条文（同じ日に同じ分野を出さない）。', '',
      '| 日 | 日付 | 朝・空欄補充（新しい条文） | 朝・択一（前日の条文） | 夜 | 土日 |', '|---|---|---|---|---|---|']
for r in rows:
    md.append(f"| {r['day']}{'✓' if r['done'] else ''} | {r['date'].strftime('%m/%d')}({r['wd']}) | {r['cloze']} | {r['q']} | {r['pm']} | {r['sat']} |")
open(os.path.join(HERE, 'schedule', 'schedule.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print(f'全{total_days}日 / 1周に必要 {use}日（第{last_first_pass}日＝{START + datetime.timedelta(days=last_first_pass - 1)}）/ 余り {spare}日')
print('ユニット', cnt, '条', arts_n)
