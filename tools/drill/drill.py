#!/usr/bin/env python3
"""択一式 一問一答ドリル エンジン（標準ライブラリのみ）

学習記録は専用ブランチ `drill-log` の `log.jsonl` に追記する（git worktree: .drill-log/）。
問題バンクは tools/drill/data/items.json（main側）。

使い方（Claude Code のセッションから呼ぶ）:
  drill.py start                       記録ブランチを用意し、現状の要約と今日のおすすめを表示
  drill.py next [-n 10] [--subject 民法|不動産登記法|調査士法] [--topic 論点] [--mode mixed|new|review|weak]
                                       出題する問題を選ぶ（正解は出さない）。選んだ問題は .drill-log/session.json に保存
  drill.py answer <ID> <o|x|?>         回答を記録して、正誤・根拠・出典を表示
  drill.py save                        記録をコミットして drill-log ブランチに push
  drill.py report [--json]             苦手分析（論点別の 未習得／誤解／定着）
  drill.py explain <ID>                その肢の出典と解説記事の場所を表示

回答は 〇(o)・×(x)・？(?) の3択。
  〇/× が正解   → 定着(known)
  〇/× が不正解 → 誤解(miscon)   間違って覚えている（最優先で復習）
  ？            → 未習得(unknown) 知らない（正誤は問わない）
"""
import argparse, collections, datetime as dt, json, math, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BANK = os.path.join(HERE, 'data', 'items.json')
LOGDIR = os.path.join(ROOT, '.drill-log')
LOG = os.path.join(LOGDIR, 'log.jsonl')
SESSION = os.path.join(LOGDIR, 'session.json')
BRANCH = 'drill-log'
SUBJECTS = ['民法', '不動産登記法', '土地家屋調査士法']
SUBJ_ALIAS = {'調査士法': '土地家屋調査士法', '不登法': '不動産登記法'}
# 復習間隔（日）。連続正解数(streak)ごと。誤答・？は streak=0 に戻る。
INTERVALS = [0, 1, 3, 7, 21, 60]
FIRST_TRY_STREAK = 4      # 初見で正解した肢は streak=4（21日後に確認）から始める
RETIRE_STREAK = 6         # これ以上は復習に出さない（定着）
MIN_GAP = 6               # 誤答・？の肢を同じセッションで再出題するまでに挟む最低問数


def sh(*args, check=True, cwd=ROOT):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"git/コマンド失敗: {' '.join(args)}\n{r.stderr.strip()}")
    return r


def now():
    return dt.datetime.now(dt.timezone.utc)


def load_bank():
    d = json.load(open(BANK, encoding='utf-8'))
    return {x['id']: x for x in d['items']}


def ensure_log_branch():
    """.drill-log を drill-log ブランチの worktree として用意する（なければ孤立ブランチで新規作成）。"""
    if os.path.isdir(LOGDIR) and os.path.exists(os.path.join(LOGDIR, '.git')):
        return
    sh('git', 'fetch', 'origin', BRANCH, check=False)
    have_remote = sh('git', 'rev-parse', '--verify', f'origin/{BRANCH}', check=False).returncode == 0
    have_local = sh('git', 'rev-parse', '--verify', BRANCH, check=False).returncode == 0
    if have_local:
        sh('git', 'worktree', 'add', LOGDIR, BRANCH)
        if have_remote:
            sh('git', 'merge', '--ff-only', f'origin/{BRANCH}', check=False, cwd=LOGDIR)
    elif have_remote:
        sh('git', 'worktree', 'add', '-b', BRANCH, LOGDIR, f'origin/{BRANCH}')
    else:
        sh('git', 'worktree', 'add', '--orphan', '-b', BRANCH, LOGDIR)
        open(os.path.join(LOGDIR, 'README.md'), 'w', encoding='utf-8').write(
            '# drill-log\n\n一問一答ドリルの学習記録専用ブランチ。log.jsonl に1回答1行で追記する。コードは置かない。\n')
        open(LOG, 'a').close()
        sh('git', 'add', '.', cwd=LOGDIR)
        sh('git', 'commit', '-m', 'drill-log: 初期化', cwd=LOGDIR)


def read_log():
    if not os.path.exists(LOG):
        return []
    out = []
    for ln in open(LOG, encoding='utf-8'):
        ln = ln.strip()
        if ln:
            out.append(json.loads(ln))
    return out


def item_state(logs):
    """肢ごとの履歴から 現在の状態を出す。"""
    st = {}
    for r in logs:
        s = st.setdefault(r['id'], {'n': 0, 'known': 0, 'miscon': 0, 'unknown': 0, 'streak': 0, 'last': None, 'last_res': None, 'ever_fail': False})
        s['n'] += 1
        s[r['res']] += 1
        t = dt.datetime.fromisoformat(r['t'])
        if r['res'] == 'known':
            if s['n'] == 1:
                s['streak'] = FIRST_TRY_STREAK
            else:
                s['streak'] += 1
        else:
            s['streak'] = 0
            s['ever_fail'] = True
        s['last'] = t
        s['last_res'] = r['res']
    return st


def due_at(s):
    if s['streak'] >= RETIRE_STREAK:
        return None
    days = INTERVALS[min(s['streak'], len(INTERVALS) - 1)]
    return s['last'] + dt.timedelta(days=days)


def topic_stats(bank, st):
    ts = collections.defaultdict(lambda: {'n': 0, 'known': 0, 'miscon': 0, 'unknown': 0})
    for iid, s in st.items():
        it = bank.get(iid)
        if not it:
            continue
        key = (it['subject'], it['topic'])
        t = ts[key]
        t['n'] += s['n']; t['known'] += s['known']; t['miscon'] += s['miscon']; t['unknown'] += s['unknown']
    return ts


def weakness(t):
    """弱さの推定（0〜1）。回答が少ない論点は平均に寄せる（ベイズ補正）。誤解は未習得より重く見る。"""
    prior_n, prior_w = 4, 0.35
    w = (t['miscon'] * 1.0 + t['unknown'] * 0.7)
    return (w + prior_n * prior_w) / (t['n'] + prior_n)


def cmd_start(a):
    ensure_log_branch()
    bank = load_bank(); logs = read_log(); st = item_state(logs)
    total = len(bank)
    seen = len(st)
    due = [i for i, s in st.items() if due_at(s) and due_at(s) <= now() and i in bank]
    print(f'問題バンク {total}肢 / 解答済み {seen}肢 / 復習の期限が来ている {len(due)}肢 / 記録 {len(logs)}件')
    by = collections.Counter(bank[i]['subject'] for i in st if i in bank)
    for s in SUBJECTS:
        n = sum(1 for x in bank.values() if x['subject'] == s)
        print(f'  {s}: {by.get(s, 0)}/{n}')
    if logs:
        print('直近の記録: ' + logs[-1]['t'][:16])


def pick(bank, st, n, subject, topic, mode):
    nowt = now()
    last_session = []
    if os.path.exists(SESSION):
        try:
            last_session = json.load(open(SESSION, encoding='utf-8')).get('recent', [])
        except Exception:
            pass
    pool = {i: x for i, x in bank.items()
            if x.get('status', 'verified') == 'verified'
            and (not subject or x['subject'] == subject)
            and (not topic or x['topic'] == topic)}
    ts = topic_stats(bank, st)
    answered_topics = collections.Counter()
    for iid, s in st.items():
        if iid in bank:
            answered_topics[(bank[iid]['subject'], bank[iid]['topic'])] += s['n']

    def prio_review(i):
        s = st[i]; d = due_at(s)
        over = (nowt - d).total_seconds() / 86400
        base = {'miscon': 3.0, 'unknown': 2.0, 'known': 1.0}[s['last_res']]
        return base + min(over, 10) * 0.1 + s['miscon'] * 0.2

    due = [i for i in pool if i in st and due_at(st[i]) and due_at(st[i]) <= nowt and i not in last_session]
    due.sort(key=prio_review, reverse=True)
    new = [i for i in pool if i not in st]

    def prio_new(i):
        it = pool[i]; key = (it['subject'], it['topic'])
        covered = answered_topics.get(key, 0)
        explore = 1.0 / (1 + covered / 3)            # まだ解いていない論点を先に（診断）
        weak = weakness(ts[key]) if key in ts else 0.35
        return explore * 1.5 + weak * 1.5 + 0.15 * min(it.get('freq', 1), 5) + random.random() * 0.6

    new.sort(key=prio_new, reverse=True)
    if mode == 'review':
        chosen = due[:n]
    elif mode == 'new':
        chosen = new[:n]
    elif mode == 'weak':
        # 弱い論点の肢（未出題＋復習が近いもの）を弱さ順に
        cand = [i for i in pool if i not in last_session and (i not in st or (st[i]['streak'] < RETIRE_STREAK))]
        cand.sort(key=lambda i: -(weakness(ts[(pool[i]['subject'], pool[i]['topic'])]) if (pool[i]['subject'], pool[i]['topic']) in ts else 0.35) - random.random() * 0.3)
        chosen = cand[:n]
    else:  # mixed: 復習期限が来たものを最大半分、残りは新規
        k = min(len(due), max(1, n // 2) if due else 0)
        chosen = due[:k] + new[:n - k]
        if len(chosen) < n:
            chosen += [i for i in due[k:]][:n - len(chosen)]
    # 同じ論点が連続しないよう軽く散らす
    random.shuffle(chosen)
    return chosen


def cmd_next(a):
    ensure_log_branch()
    bank = load_bank(); st = item_state(read_log())
    subj = SUBJ_ALIAS.get(a.subject, a.subject)
    ids = pick(bank, st, a.n, subj, a.topic, a.mode)
    if not ids:
        print('出題できる問題がありません（期限の来た復習なし／新規なし）。--mode new か別の科目を試してください。')
        return
    sess = {'started': now().isoformat(), 'ids': ids, 'recent': ids}
    json.dump(sess, open(SESSION, 'w', encoding='utf-8'), ensure_ascii=False)
    for k, i in enumerate(ids, 1):
        it = bank[i]
        tag = '復習' if i in st else '新規'
        print(f'[{k}/{len(ids)}] ({i}) {tag}・{it["subject"]}／{it["topic"]}')
        print(f'  {it["statement"]}')
        print()


def cmd_answer(a):
    ensure_log_branch()
    bank = load_bank()
    if a.id not in bank:
        raise SystemExit(f'ID不明: {a.id}')
    it = bank[a.id]
    ans = {'o': 'o', '〇': 'o', '○': 'o', 'x': 'x', '×': 'x', '✕': 'x', '?': '?', '？': '?'}.get(a.ans)
    if ans is None:
        raise SystemExit('回答は o / x / ? （〇 × ？）')
    truth = bool(it['truth'])
    if ans == '?':
        res = 'unknown'
    elif (ans == 'o') == truth:
        res = 'known'
    else:
        res = 'miscon'
    rec = {'t': now().isoformat(timespec='seconds'), 'id': a.id, 'ans': ans, 'truth': truth, 'res': res}
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    mark = {'known': '✅ 定着（正解）', 'miscon': '❌ 誤解（逆に覚えている）', 'unknown': '❔ 未習得（？）'}[res]
    print(mark)
    print(f'正解: {"〇（正しい記述）" if truth else "×（誤った記述）"}')
    if it.get('basis'):
        print(f'根拠: {it["basis"]}')
    srcs = '、'.join(f'{s["q"]}{s.get("label", "")}' for s in it.get('sources', [])[:4])
    print(f'出典: {srcs}' + (f'（ほか {len(it["sources"]) - 4}）' if len(it.get('sources', [])) > 4 else ''))
    if it.get('pair'):
        print(f'対比: {", ".join(it["pair"][:2])}（逆の結論になる類似肢）')
    # 履歴
    st = item_state(read_log())[a.id]
    print(f'この肢: {st["n"]}回目（定着{st["known"]}／誤解{st["miscon"]}／未習得{st["unknown"]}）')
    if res != 'known':
        print('→ 同じセッション内でも間隔を空けて再出題されます。')


def cmd_save(a):
    ensure_log_branch()
    sh('git', 'add', 'log.jsonl', cwd=LOGDIR)
    r = sh('git', 'diff', '--cached', '--quiet', check=False, cwd=LOGDIR)
    if r.returncode == 0:
        print('変更なし（保存済み）')
        return
    n = len(read_log())
    sh('git', 'commit', '-m', f'drill-log: {now().strftime("%Y-%m-%d %H:%M")} 累計{n}件', cwd=LOGDIR)
    sh('git', 'fetch', 'origin', BRANCH, check=False, cwd=LOGDIR)
    if sh('git', 'rev-parse', '--verify', f'origin/{BRANCH}', check=False, cwd=LOGDIR).returncode == 0:
        m = sh('git', 'merge', '--no-edit', f'origin/{BRANCH}', check=False, cwd=LOGDIR)
        if m.returncode != 0:
            # 別セッションの記録とぶつかったら、行単位の和集合でlog.jsonlを統合する
            ours = sh('git', 'show', f':2:log.jsonl', check=False, cwd=LOGDIR).stdout.splitlines()
            theirs = sh('git', 'show', f':3:log.jsonl', check=False, cwd=LOGDIR).stdout.splitlines()
            lines = sorted(set(l for l in ours + theirs if l.strip()), key=lambda l: json.loads(l)['t'])
            open(LOG, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
            sh('git', 'add', 'log.jsonl', cwd=LOGDIR)
            sh('git', 'commit', '--no-edit', cwd=LOGDIR)
    for wait in (0, 2, 4, 8, 16):
        if wait:
            import time; time.sleep(wait)
        p = sh('git', 'push', '-u', 'origin', BRANCH, check=False, cwd=LOGDIR)
        if p.returncode == 0:
            print(f'保存しました（{BRANCH}、累計{n}件）')
            return
    raise SystemExit('push失敗: ' + p.stderr.strip())


def cmd_explain(a):
    bank = load_bank(); it = bank.get(a.id)
    if not it:
        raise SystemExit('ID不明')
    print(json.dumps({k: it.get(k) for k in ('id', 'subject', 'topic', 'statement', 'truth', 'basis', 'sources', 'pair')}, ensure_ascii=False, indent=1))


def cmd_report(a):
    ensure_log_branch()
    bank = load_bank(); logs = read_log(); st = item_state(logs)
    ts = topic_stats(bank, st)
    rows = []
    for (subj, topic), t in ts.items():
        n = t['n']
        rows.append({'subject': subj, 'topic': topic, 'n': n, 'known': t['known'], 'miscon': t['miscon'], 'unknown': t['unknown'],
                     'known_rate': t['known'] / n, 'miscon_rate': t['miscon'] / n, 'unknown_rate': t['unknown'] / n, 'weak': weakness(t)})
    rows.sort(key=lambda r: -r['weak'])
    # 繰り返し誤解している肢
    chronic = sorted([(i, s) for i, s in st.items() if s['miscon'] >= 2 and i in bank], key=lambda x: -x[1]['miscon'])[:10]
    # 〇×の癖: 正しい記述を×にする／誤り記述を〇にする
    biasT = sum(1 for r in logs if r['truth'] and r['res'] == 'miscon'); nT = sum(1 for r in logs if r['truth'] and r['ans'] != '?')
    biasF = sum(1 for r in logs if (not r['truth']) and r['res'] == 'miscon'); nF = sum(1 for r in logs if (not r['truth']) and r['ans'] != '?')
    # 対比ペアの混同: 同じ pair に属する肢を両方間違えた
    out = {'total_answers': len(logs), 'items_seen': len(st), 'items_total': len(bank),
           'topics': rows, 'chronic': [{'id': i, 'miscon': s['miscon'], 'statement': bank[i]['statement']} for i, s in chronic],
           'bias': {'true_as_x': (biasT, nT), 'false_as_o': (biasF, nF)}}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    print(f'解答 {len(logs)}件 / 解答済み {len(st)}・{len(bank)}肢')
    if not rows:
        print('まだ記録がありません。'); return
    print('\n■ 論点別（弱い順。未習得＝？、誤解＝逆に覚えている）')
    for r in rows[:25]:
        print(f'  {r["subject"][:3]}／{r["topic"]}: {r["n"]}問 定着{r["known_rate"]:.0%} 誤解{r["miscon_rate"]:.0%} 未習得{r["unknown_rate"]:.0%}')
    if chronic:
        print('\n■ 何度も誤解している肢')
        for i, s in chronic:
            print(f'  ({i}) 誤解{s["miscon"]}回: {bank[i]["statement"][:60]}')
    print(f'\n■ 〇×の癖: 正しい記述を×にした {biasT}/{nT}、誤った記述を〇にした {biasF}/{nF}')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('start')
    n = sub.add_parser('next'); n.add_argument('-n', type=int, default=10); n.add_argument('--subject'); n.add_argument('--topic')
    n.add_argument('--mode', default='mixed', choices=['mixed', 'new', 'review', 'weak'])
    an = sub.add_parser('answer'); an.add_argument('id'); an.add_argument('ans')
    sub.add_parser('save')
    r = sub.add_parser('report'); r.add_argument('--json', action='store_true')
    e = sub.add_parser('explain'); e.add_argument('id')
    a = p.parse_args()
    {'start': cmd_start, 'next': cmd_next, 'answer': cmd_answer, 'save': cmd_save, 'report': cmd_report, 'explain': cmd_explain}[a.cmd](a)


if __name__ == '__main__':
    main()
