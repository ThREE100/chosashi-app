"""毎日ドリルの「誤答を型で記録するログ」。個人の演習結果は問題・解説には入れず、ここ（daily-drill/log/）にだけ残す。

1回解くごとに1行（JSON）を log/YYYYMMDD.jsonl に足す：
  {"date": "2026-10-24", "id": "PM-20", "side": "evening", "result": "×", "traps": ["A2"], "item": "添付情報", "minutes": 18, "note": "…"}
- result は ○（できた）・△（一部まちがい）・×（まちがい）。
- traps は taxonomy.json のひっかけの型（朝 M1〜M10、夜 C1〜C14・A1〜A8・D1〜D5）。△・× のときは1つ以上必須。
  型に当てはまらないときは「他」を使い、--note に中身を書く（3回以上たまったら、新しい型として taxonomy.json に足す）。

使い方（daily-drill で）:
  python3 kiroku.py add PM-20 × A2 --item 添付情報 --min 18      # 問題IDで記録
  python3 kiroku.py add day20-pm × A2 A5                          # 第20日の夜（dayNN-am / dayNN-pm）でもよい
  python3 kiroku.py add AM-003 ○
  python3 kiroku.py report                                        # log/report.md を作り直す（型別の集計・再演習の予定・おすすめ）
  python3 kiroku.py due [--date 2026-10-30]                       # その日に解き直す問題
  python3 kiroku.py list [--days 7]                               # 最近の記録
  python3 kiroku.py check                                         # 記録の形の検査（check_all.py からも呼ぶ）
"""
import argparse
import collections
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.environ.get('KIROKU_LOG') or os.path.join(HERE, 'log')   # 試験用に別の場所を指定できる
TAX = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))
REG = json.load(open(os.path.join(HERE, 'registry.json'), encoding='utf-8'))
RESULTS = {'○': '○', 'ok': '○', 'o': '○', '△': '△', 'part': '△', '×': '×', 'x': '×', 'ng': '×', '✕': '×'}
OTHER = '他'
# 再演習の間隔：最後の ×・△ から、その後の ○ の数に応じて（0回→3日後、1回→7日後、2回→卒業）
INTERVALS = [3, 7]


def trap_names(side):
    return TAX['traps_morning'] if side == 'morning' else TAX['traps_evening']


def problems():
    """問題ID → (side, day, 題)"""
    out = {}
    for side, d in (('morning', 'morning'), ('evening', 'evening')):
        for fp in glob.glob(os.path.join(HERE, d, 'problems', '*.json')):
            p = json.load(open(fp, encoding='utf-8'))
            out[p['id']] = (side, p.get('day'), p.get('title') or p.get('theme', ''))
    return out


def resolve(ref, probs):
    m = re.fullmatch(r'day0*(\d+)-(am|pm)', ref.lower())
    if m:
        day, side = int(m.group(1)), 'morning' if m.group(2) == 'am' else 'evening'
        hit = [k for k, v in probs.items() if v[0] == side and v[1] == day]
        if not hit:
            sys.exit(f'第{day}日の{"朝" if side == "morning" else "夜"}の問題がない')
        return hit[0]
    ref = ref.upper()
    if ref not in probs:
        sys.exit(f'問題 {ref} がない（AM-001 や PM-20、day20-pm の形で指定する）')
    return ref


def validate(r, probs):
    """1件の記録の誤りを文字列のリストで返す"""
    e = []
    for k in ('date', 'id', 'side', 'result', 'traps'):
        if k not in r:
            e.append(f'{k} がない')
    if e:
        return e
    try:
        datetime.date.fromisoformat(r['date'])
    except ValueError:
        e.append(f'日付が不正 {r["date"]}')
    if r['id'] not in probs:
        e.append(f'問題 {r["id"]} がない')
    elif probs[r['id']][0] != r['side']:
        e.append('朝・夜の区別が問題と合わない')
    if r['result'] not in ('○', '△', '×'):
        e.append(f'結果は ○・△・× のどれか（{r["result"]}）')
    names = trap_names(r['side'])
    for t in r['traps']:
        if t != OTHER and t not in names:
            e.append(f'ひっかけの型 {t} は taxonomy.json にない（{"朝は M" if r["side"] == "morning" else "夜は C・A・D"}）')
    if r['result'] in ('△', '×') and not r['traps']:
        e.append('△・× のときは、ひっかけの型を1つ以上書く（当てはまらなければ「他」と --note）')
    if OTHER in r['traps'] and not r.get('note'):
        e.append('「他」のときは --note に中身を書く')
    return e


def load():
    rows = []
    for fp in sorted(glob.glob(os.path.join(LOG, '*.jsonl'))):
        for n, ln in enumerate(open(fp, encoding='utf-8'), 1):
            if ln.strip():
                r = json.loads(ln)
                r['_src'] = f'{os.path.basename(fp)}:{n}'
                rows.append(r)
    rows.sort(key=lambda r: (r['date'], r['_src']))
    return rows


def cmd_add(a):
    probs = problems()
    pid = resolve(a.ref, probs)
    side = probs[pid][0]
    res = RESULTS.get(a.result.lower() if a.result.isascii() else a.result)
    if not res:
        sys.exit('結果は ○・△・×（ok・part・ng でもよい）')
    traps = [t.upper() if t != OTHER else t for t in a.traps]
    r = {'date': a.date or datetime.date.today().isoformat(), 'id': pid, 'side': side, 'result': res, 'traps': traps}
    for k in ('item', 'note'):
        if getattr(a, k):
            r[k] = getattr(a, k)
    if a.min:
        r['minutes'] = a.min
    err = validate(r, probs)
    if err:
        sys.exit('記録できない：' + ' ／ '.join(err))
    expected = set(REG.get(pid, {}).get('traps', []))
    extra = [t for t in traps if t != OTHER and t not in expected]
    os.makedirs(LOG, exist_ok=True)
    fp = os.path.join(LOG, r['date'].replace('-', '') + '.jsonl')
    with open(fp, 'a', encoding='utf-8') as f:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
    names = trap_names(side)
    print(f'記録した：{r["date"]} {pid} {res} ' + '、'.join(f'{t}（{names.get(t, "その他")}）' for t in traps))
    if extra:
        print(f'  ※ {"・".join(extra)} は、この問の想定のひっかけ（{"・".join(sorted(expected)) or "なし"}）にない型。問題の作りの見直しの材料になる')
    write_report()


def status(rows):
    """問題ごとの再演習の状態：{id: (最後の×△の日, その後の○の数, 次の日 or None)}"""
    st = {}
    for r in rows:
        d = datetime.date.fromisoformat(r['date'])
        if r['result'] in ('×', '△'):
            st[r['id']] = [d, 0]
        elif r['id'] in st:            # 解き直して ○：間隔は、この日から数える
            st[r['id']][1] += 1
            st[r['id']][0] = d
    out = {}
    for pid, (d, ok) in st.items():
        out[pid] = (d, ok, d + datetime.timedelta(days=INTERVALS[ok]) if ok < len(INTERVALS) else None)
    return out


def due(rows, day):
    return sorted(((nxt, pid, ok) for pid, (_, ok, nxt) in status(rows).items() if nxt and nxt <= day), key=lambda x: (x[0], x[1]))


def write_report():
    rows, probs = load(), problems()
    today = datetime.date.today()
    md = ['# 誤答の型の記録（自動生成：`python3 daily-drill/kiroku.py report`）', '',
          '個人の演習結果。問題・解説・公開用の記事には転記しない。', '']
    if not rows:
        md += ['まだ記録がない。解答ページの「記録」の欄のコマンドで記録する。']
        _save(md)
        return
    cnt = collections.Counter(r['result'] for r in rows)
    md += [f'## 全体（{rows[0]["date"]}〜{rows[-1]["date"]}）', '',
           f'- 記録 {len(rows)} 件：○ {cnt["○"]}・△ {cnt["△"]}・× {cnt["×"]}（正答率 {cnt["○"] / len(rows):.0%}）']
    for side, lab in (('morning', '朝'), ('evening', '夜')):
        rs = [r for r in rows if r['side'] == side]
        if rs:
            ok = sum(r['result'] == '○' for r in rs)
            md.append(f'- {lab}：{len(rs)} 件、○ {ok}（{ok / len(rs):.0%}）')
    # ひっかけの型別：×・△で引っかかった回数と、その型を含む問に出会った回数
    md += ['', '## ひっかけの型別（引っかかった回数の多い順）', '',
           '「出会った」は、その型が想定に入っている問を解いた回数（registry.json）。引っかかった率 ＝ 引っかかった ÷ 出会った。', '',
           '| 型 | 内容 | 引っかかった | 出会った | 率 |', '|---|---|---|---|---|']
    hit, met = collections.Counter(), collections.Counter()
    for r in rows:
        for t in REG.get(r['id'], {}).get('traps', []):
            met[(r['side'], t)] += 1
        if r['result'] != '○':
            for t in r['traps']:
                hit[(r['side'], t)] += 1
    keys = sorted(set(hit) | {k for k in met if hit[k]}, key=lambda k: (-hit[k], -met[k], k[1]))
    for side, t in keys:
        names = trap_names(side)
        m = met[(side, t)]
        md.append(f'| {t} | {names.get(t, "その他（メモを見る）")} | {hit[(side, t)]} | {m or "－"} | {f"{hit[(side, t)] / m:.0%}" if m else "－"} |')
    # 夜の問題の型（T・B）・朝の分野
    md += ['', '## 問題の型・分野別', '', '| 区分 | 解いた | ○ | 正答率 |', '|---|---|---|---|']
    grp = collections.defaultdict(list)
    for r in rows:
        g = REG.get(r['id'], {})
        if r['side'] == 'evening':
            for t in g.get('types', []):
                grp[f'夜 {t} {TAX["evening_types"].get(t, {}).get("name", "")}'].append(r['result'])
        else:
            grp[f'朝 {g.get("field", "")}・{g.get("style", "")}'].append(r['result'])
    for k in sorted(grp):
        v = grp[k]
        md.append(f'| {k} | {len(v)} | {v.count("○")} | {v.count("○") / len(v):.0%} |')
    # 再演習
    st = status(rows)
    md += ['', '## 再演習の予定（最後の ×・△ から、○ 0回→3日後、1回→7日後、2回続けて ○ で卒業）', '']
    act = sorted(((nxt, pid, ok) for pid, (_, ok, nxt) in st.items() if nxt), key=lambda x: (x[0], x[1]))
    if act:
        md += ['| 予定日 | 問題 | 第何日 | 題 | その後の○ |', '|---|---|---|---|---|']
        for nxt, pid, ok in act:
            s, d, ti = probs.get(pid, ('', '', ''))
            md.append(f'| {nxt}{"（期限切れ）" if nxt < today else ""} | {pid} | 第{d}日{"朝" if s == "morning" else "夜"} | {ti} | {ok} |')
    else:
        md.append('なし')
    # 弱い型の練習におすすめの問題（まだ解いていない、その型を含む問）
    md += ['', '## 弱い型を練習する問題（引っかかった回数の多い型3つ。まだ解いていない問から、日の順に3問ずつ）', '']
    done = {r['id'] for r in rows}
    top = [k for k in keys if hit[k]][:3]
    for side, t in top:
        cand = sorted((probs[p][1], p) for p, g in REG.items() if p in probs and probs[p][0] == side and t in g.get('traps', []) and p not in done)
        md.append(f'- {t}（{trap_names(side).get(t, "その他")}）：' + ('、'.join(f'{p}（第{d}日）' for d, p in cand[:3]) or '該当する未演習の問がない'))
    # 「他」のメモ
    others = [r for r in rows if OTHER in r['traps']]
    if others:
        md += ['', '## 型に当てはまらなかった誤答（3回以上たまったら新しい型を taxonomy.json に足す）', '']
        md += [f'- {r["date"]} {r["id"]}：{r.get("note", "")}' for r in others]
    _save(md)


def _save(md):
    os.makedirs(LOG, exist_ok=True)
    open(os.path.join(LOG, 'report.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')


def cmd_due(a):
    rows, probs = load(), problems()
    day = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
    lst = due(rows, day)
    if not lst:
        print(f'{day} に解き直す問題はない')
    for nxt, pid, ok in lst:
        s, d, ti = probs.get(pid, ('', '', ''))
        print(f'{pid}（第{d}日{"朝" if s == "morning" else "夜"}）{ti}　予定 {nxt}　その後の○ {ok}回')


def cmd_list(a):
    rows = load()
    since = (datetime.date.today() - datetime.timedelta(days=a.days)).isoformat()
    for r in rows:
        if r['date'] >= since:
            print(f'{r["date"]} {r["id"]} {r["result"]} {"・".join(r["traps"])} {r.get("item", "")} {r.get("note", "")}'.rstrip())


def check():
    """記録の形の検査。誤りの件数を返す"""
    probs, n = problems(), 0
    for fp in sorted(glob.glob(os.path.join(LOG, '*.jsonl'))):
        name = os.path.basename(fp)
        if not re.fullmatch(r'\d{8}\.jsonl', name):
            print(f'NG {name}: ファイル名は YYYYMMDD.jsonl')
            n += 1
        for i, ln in enumerate(open(fp, encoding='utf-8'), 1):
            if not ln.strip():
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                print(f'NG {name}:{i}: JSONでない')
                n += 1
                continue
            e = validate(r, probs)
            if r.get('date', '').replace('-', '') != name[:8]:
                e.append('日付とファイル名が合わない')
            for x in e:
                print(f'NG {name}:{i}: {x}')
            n += len(e)
    print(f'記録の検査：NG {n}件')
    return n


def main():
    ap = argparse.ArgumentParser(description='毎日ドリルの誤答を型で記録する')
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('add')
    s.add_argument('ref')
    s.add_argument('result')
    s.add_argument('traps', nargs='*')
    s.add_argument('--item')
    s.add_argument('--note')
    s.add_argument('--min', type=int)
    s.add_argument('--date')
    sub.add_parser('report')
    s = sub.add_parser('due')
    s.add_argument('--date')
    s = sub.add_parser('list')
    s.add_argument('--days', type=int, default=7)
    sub.add_parser('check')
    a = ap.parse_args()
    if a.cmd == 'add':
        cmd_add(a)
    elif a.cmd == 'report':
        write_report()
        print('log/report.md を書き出し')
    elif a.cmd == 'due':
        cmd_due(a)
    elif a.cmd == 'list':
        cmd_list(a)
    else:
        sys.exit(1 if check() else 0)


if __name__ == '__main__':
    main()
