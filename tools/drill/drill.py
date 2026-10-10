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
  drill.py mark <ID> <miscon|unknown|known> [--note ..]   直前の回答の判定を訂正（正解でも理解が誤っていたとき）
  drill.py tag <ID> <タグ> [--note ..]  肢にタグを付ける（例: nigate＝苦手分析シリーズ候補）
  drill.py tags [タグ] [--json]        タグ付けした肢を一括で表示（タグ省略で件数）
  drill.py untag <ID> <タグ>           タグを解除
  drill.py checks [--severity error|warn|unverified]   事前の条文照合の結果（指摘）を一覧
  drill.py issue <ID> "問題点" [--proposal "訂正案"]   引用した記事の解説の誤りの指摘と訂正案を記録（記事は書き換えない）

回答は 〇(o)・×(x)・？(?) の3択。
  〇/× が正解   → 定着(known)
  〇/× が不正解 → 誤解(miscon)   間違って覚えている（最優先で復習）
復習の区分（誤解＋未習得の通算回数W、その後の連続正解数c）: c<W 要復習 / c=W チェック / c>W 除外。
mixed の出題は 要復習3・チェック1・新規1（Wの多い順）。
  ？            → 未習得(unknown) 知らない（正誤は問わない）
"""
import argparse, collections, re, datetime as dt, json, math, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BANK = os.path.join(HERE, 'data', 'items.json')
LOGDIR = os.path.join(ROOT, '.drill-log')
LOG = os.path.join(LOGDIR, 'log.jsonl')
SESSION = os.path.join(LOGDIR, 'session.json')
FOCUS = os.path.join(LOGDIR, 'focus.json')
TAGS = os.path.join(LOGDIR, 'tags.jsonl')
ISSUES = os.path.join(LOGDIR, 'issues.jsonl')
BRANCH = 'drill-log'
SUBJECTS = ['民法', '不動産登記法', '土地家屋調査士法']
SUBJ_ALIAS = {'調査士法': '土地家屋調査士法', '不登法': '不動産登記法'}
# （旧）復習間隔。2026-10-10から出題は下の「要復習／チェック／除外」のルールで決める（due_at は互換のため残してある）。
# 誤答・？は日付をまたいだ翌日（日本時間0時）以降に出す。同じ日には出さない
INTERVALS = [1, 1, 3, 7, 21, 60]
FIRST_TRY_STREAK = 4      # 初見で正解した肢は streak=4（21日後に確認）から始める
RETIRE_STREAK = 6         # これ以上は復習に出さない（定着）
JST = dt.timezone(dt.timedelta(hours=9))   # 「日付をまたぐ」は日本時間の午前0時で数える


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
    # 訂正（amend）レコード: 直前の同じ肢の回答の判定を上書きする（正解でも理解が誤っていたときなど）
    recs = [r for r in out if not r.get('amend')]
    for a in [r for r in out if r.get('amend')]:
        for r in reversed(recs):
            if r['id'] == a['id'] and r['t'] <= a['t']:
                r['res'] = a['res']; r['amended'] = True; r['amend_note'] = a.get('note', '')
                break
    return recs


def item_state(logs):
    """肢ごとの履歴から 現在の状態を出す。"""
    st = {}
    for r in logs:
        s = st.setdefault(r['id'], {'n': 0, 'known': 0, 'miscon': 0, 'unknown': 0, 'streak': 0, 'cons': 0, 'last': None, 'last_res': None, 'ever_fail': False})
        s['n'] += 1
        s[r['res']] += 1
        t = dt.datetime.fromisoformat(r['t'])
        if r['res'] == 'known':
            s['cons'] += 1
            if s['n'] == 1:
                s['streak'] = FIRST_TRY_STREAK
            else:
                s['streak'] += 1
        else:
            s['streak'] = 0
            s['cons'] = 0
            s['ever_fail'] = True
        s['last'] = t
        s['last_res'] = r['res']
    return st


def wrong_total(s):
    """誤解＋未習得の通算回数。"""
    return s['miscon'] + s['unknown']


def review_class(s):
    """復習の区分（2026-10-10 ユーザー指示）。誤解・未習得の通算回数 W と、その後の連続正解数 c で決める。
      c < W  → 'must'  要復習（優先して出す）
      c == W → 'check' チェック（優先度を下げて出す）
      c > W  → 'done'  復習から除外
    一度も間違えていない肢は None。"""
    if not s['ever_fail']:
        return None
    w = wrong_total(s)
    return 'must' if s['cons'] < w else 'check' if s['cons'] == w else 'done'


def due_at(s):
    if s['streak'] >= RETIRE_STREAK:
        return None
    days = INTERVALS[min(s['streak'], len(INTERVALS) - 1)]
    last_day = s['last'].astimezone(JST).date()
    return dt.datetime.combine(last_day + dt.timedelta(days=days), dt.time(0, 0), tzinfo=JST)


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


def sync_main():
    """origin/main の最新を取得する（記事はここから読む）。失敗してもドリルは動く。"""
    try:
        r = subprocess.run(['git', 'fetch', 'origin', 'main'], cwd=ROOT, capture_output=True, text=True, timeout=30)
        ok = r.returncode == 0
    except Exception:
        ok = False
    sha = subprocess.run(['git', 'rev-parse', '--short', 'origin/main'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    when = subprocess.run(['git', 'log', '-1', '--format=%cd', '--date=format:%Y-%m-%d %H:%M', 'origin/main'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if ok and sha:
        print(f'記事の参照元: origin/main {sha}（最終更新 {when}）— 取得しました')
    elif sha:
        print(f'⚠️ mainの最新を取得できませんでした。取得済みの origin/main {sha}（最終更新 {when}）を参照します')
    else:
        print('⚠️ origin/main がありません。ローカルのファイルを参照します（古い可能性があります）')
    # 照合結果を出した時点から、mainで更新された記事の数
    ck = load_checks()
    cur = subprocess.run(['git', 'log', '-1', '--format=%H', 'origin/main', '--', 'note-articles'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if cur and cur == ck.get('meta', {}).get('note_articles_commit'):
        stale = []   # note-articles/ に照合後の変更がない → 全記事が照合した版のまま
    else:
        stale = [pth for pth, v in ck.get('checked', {}).items() if v.get('sha') and article_hash(read_article(pth)) != v['sha']]
    if stale:
        print(f'⚠️ 条文照合のあとにmainで更新された記事: {len(stale)}本（その記事の照合結果は参考値）')


def cmd_start(a):
    ensure_log_branch()
    sync_main()
    bank = load_bank(); logs = read_log(); st = item_state(logs)
    total = len(bank)
    seen = len(st)
    cls = collections.Counter(review_class(s) for i, s in st.items() if i in bank)
    print(f'問題バンク {total}肢 / 解答済み {seen}肢 / 要復習 {cls["must"]}肢・チェック {cls["check"]}肢・復習から除外 {cls["done"]}肢 / 記録 {len(logs)}件')
    by = collections.Counter(bank[i]['subject'] for i in st if i in bank)
    for s in SUBJECTS:
        n = sum(1 for x in bank.values() if x['subject'] == s)
        print(f'  {s}: {by.get(s, 0)}/{n}')
    if logs:
        print('直近の記録: ' + logs[-1]['t'][:16])
    rm = prune_resolved_article_fix()
    if rm:
        print(f'🏷 処理済みの条文照合タグ（#article-fix）を {len(rm)}肢 解除しました: ' + '、'.join(rm))


def read_focus():
    if os.path.exists(FOCUS):
        try:
            d = json.load(open(FOCUS, encoding='utf-8'))
            return d if d.get('remaining', 0) > 0 else None
        except Exception:
            return None
    return None


def count_focus():
    """回答を1件記録したとき、出題フォーカスの残りを減らす。0になったらランダム出題に戻す。"""
    fo = read_focus()
    if not fo:
        return
    fo['remaining'] -= 1
    if fo['remaining'] <= 0:
        os.remove(FOCUS)
        print('🔔 出題フォーカス（除外指定）が終わりました。次の出題から、全分野のランダム出題に戻ります。')
    else:
        json.dump(fo, open(FOCUS, 'w', encoding='utf-8'), ensure_ascii=False)


def cmd_focus(a):
    ensure_log_branch()
    if a.action == 'off':
        if os.path.exists(FOCUS):
            os.remove(FOCUS)
        print('出題フォーカスを解除しました（全分野のランダム出題）。')
    elif a.action == 'on':
        subs = [SUBJ_ALIAS.get(x, x) for x in (a.exclude_subject or [])]
        fo = {'exclude_subjects': subs, 'exclude_topics': a.exclude_topic or [], 'remaining': a.count,
              'started': now().isoformat(timespec='seconds')}
        json.dump(fo, open(FOCUS, 'w', encoding='utf-8'), ensure_ascii=False)
        print(f'出題フォーカスを開始: 除外 科目={subs} 論点={fo["exclude_topics"]}、残り{a.count}問')
    else:
        fo = read_focus()
        print('出題フォーカス: ' + (json.dumps(fo, ensure_ascii=False) if fo else 'なし（全分野ランダム）'))


# 新規の出題順（2026-10-05ユーザー指示、2026-10-08に段階を追加）：
#   R7〜H28 → H27〜H20 → H19〜H17（年度なしは最後）。各段階の未出題が残っている間は、次の段階の新規は出さない
PRIORITY_TIERS = ((28, 99), (20, 27), (0, 19))


def item_year(it):
    """肢の出典のうち最も新しい年度を平成換算で返す（R元年=平成31年）。出典に年度がなければ0。"""
    best = 0
    for src in it.get('sources', []):
        m = re.match(r'([RH])(\d+)', src.get('q', ''))
        if m:
            y = int(m.group(2)) + (30 if m.group(1) == 'R' else 0)
            best = max(best, y)
    return best


def spread_by_topic(cands, bank, st, n):
    """候補（優先順）から、論点が偏らないよう論点ごとの出題数が少ない順に n 問選ぶ。"""
    answered = collections.Counter()
    for iid, s in st.items():
        if iid in bank:
            answered[(bank[iid]['subject'], bank[iid]['topic'])] += s['n']
    chosen, used = [], collections.Counter()
    rest = list(cands)
    while rest and len(chosen) < n:
        # 今回すでに選んだ数が少ない論点を優先し、同数なら解答済みの少ない論点、さらに元の優先順
        best = min(range(len(rest)), key=lambda k: (used[(bank[rest[k]]['subject'], bank[rest[k]]['topic'])],
                                                    answered[(bank[rest[k]]['subject'], bank[rest[k]]['topic'])] // 5, k))
        iid = rest.pop(best)
        chosen.append(iid)
        used[(bank[iid]['subject'], bank[iid]['topic'])] += 1
    return chosen


def pick(bank, st, n, subject, topic, mode):
    nowt = now()
    last_session = []
    if os.path.exists(SESSION):
        try:
            last_session = json.load(open(SESSION, encoding='utf-8')).get('recent', [])
        except Exception:
            pass
    pool = {i: x for i, x in bank.items()
            if x.get('status', 'verified') in ('verified', 'provisional')
            and (not subject or x['subject'] == subject)
            and (not topic or x['topic'] == topic)}
    fo = read_focus()
    if fo and not subject and not topic:   # 出題フォーカス中は、除外した科目・論点を新規にも復習にも出さない（復習の期限は変えない）
        pool = {i: x for i, x in pool.items()
                if x['subject'] not in fo.get('exclude_subjects', []) and x['topic'] not in fo.get('exclude_topics', [])}
    ts = topic_stats(bank, st)
    answered_topics = collections.Counter()
    for iid, s in st.items():
        if iid in bank:
            answered_topics[(bank[iid]['subject'], bank[iid]['topic'])] += s['n']

    today = nowt.astimezone(JST).date()

    def eligible(i):   # 同じ日（日本時間）に答えた肢と、直前の出題の肢は出さない
        return i in st and st[i]['last'].astimezone(JST).date() < today and i not in last_session

    def review_order(i):   # 誤解・未習得の通算回数が多い順。同数なら最後に答えたのが古い順
        return (-wrong_total(st[i]), st[i]['last'])

    must = sorted((i for i in pool if eligible(i) and review_class(st[i]) == 'must'), key=review_order)
    check = sorted((i for i in pool if eligible(i) and review_class(st[i]) == 'check'), key=review_order)
    new = [i for i in pool if i not in st]

    def prio_new(i):
        it = pool[i]; key = (it['subject'], it['topic'])
        covered = answered_topics.get(key, 0)
        explore = 1.0 / (1 + covered / 3)            # まだ解いていない論点を先に（診断）
        weak = weakness(ts[key]) if key in ts else 0.35
        return explore * 1.5 + weak * 1.5 + 0.15 * min(it.get('freq', 1), 5) + random.random() * 0.6

    new.sort(key=prio_new, reverse=True)
    # 年度の優先：上の段階の未出題が残っている間は、下の段階の新規は出さない（科目・論点の指定時は適用しない）
    if not subject and not topic:
        for lo, hi in PRIORITY_TIERS:
            tier_new = [i for i in new if lo <= item_year(pool[i]) <= hi]
            if tier_new:
                new = tier_new
                break
    if mode == 'review':
        chosen = (must + check)[:n]
    elif mode == 'new':
        chosen = spread_by_topic(new, bank, st, n)
    elif mode == 'weak':
        # 弱い論点の肢（未出題＋復習が近いもの）を弱さ順に
        cand = [i for i in pool if i not in last_session and (i not in st or review_class(st[i]) != 'done')]
        cand.sort(key=lambda i: -(weakness(ts[(pool[i]['subject'], pool[i]['topic'])]) if (pool[i]['subject'], pool[i]['topic']) in ts else 0.35) - random.random() * 0.3)
        chosen = cand[:n]
    else:  # mixed: 要復習3・チェック1・新規1（5問のとき）。足りない区分は 要復習 → チェック → 新規 の順で埋める
        n_rv = round(n * 0.6); n_ck = round(n * 0.2); n_nw = n - n_rv - n_ck
        c_rv = must[:n_rv]
        c_ck = check[:n_ck]
        c_nw = spread_by_topic(new, bank, st, n_nw)
        chosen = c_rv + c_ck + c_nw
        if len(chosen) < n:
            rest = [i for i in must if i not in chosen] + [i for i in check if i not in chosen] + [i for i in new if i not in chosen]
            chosen += rest[:n - len(chosen)]
    # 同じ論点が連続しないよう軽く散らす
    random.shuffle(chosen)
    return chosen


def stmt_text(it):
    """肢の文。元の出題に前提条件・図があるものは、先頭に前提を付ける。"""
    out = ''
    if it.get('premise'):
        out += '【前提条件】' + it['premise'].replace('\n', '\n  ') + '\n  【肢】'
    if it.get('figure_missing'):
        out += '（※元の出題には図があります。図は省略されています）'
    return out + it['statement']


def cmd_next(a):
    ensure_log_branch()
    bank = load_bank(); st = item_state(read_log())
    subj = SUBJ_ALIAS.get(a.subject, a.subject)
    ids = pick(bank, st, a.n, subj, a.topic, a.mode)
    if not ids:
        print('出題できる問題がありません（要復習・チェック・新規なし）。--mode new か別の科目を試してください。')
        return
    sess = {'started': now().isoformat(), 'ids': ids, 'recent': ids}
    json.dump(sess, open(SESSION, 'w', encoding='utf-8'), ensure_ascii=False)
    for k, i in enumerate(ids, 1):
        it = bank[i]
        if i in st:
            s_ = st[i]; cl = review_class(s_)
            tag = ('要復習' if cl == 'must' else 'チェック' if cl == 'check' else '復習') + f'（誤答{wrong_total(s_)}回）' if cl else '復習'
        else:
            tag = '新規'
        print(f'[{k}/{len(ids)}] ({i}) {tag}・{it["subject"]}／{it["topic"]}')
        print(f'  {stmt_text(it)}')
        print()


_ART_CACHE = {}


def read_article(note_path):
    """記事の本文を返す。**origin/main の最新**を優先して読む（git show。作業ツリーのコピーは使わない）。
    取得できないとき（オフライン等）だけ、ローカルのファイルにフォールバックする。記事は編集しない。"""
    if note_path in _ART_CACHE:
        return _ART_CACHE[note_path]
    text = None
    try:
        r = subprocess.run(['git', 'show', f'origin/main:{note_path}'], cwd=ROOT, capture_output=True, timeout=10)
        if r.returncode == 0:
            text = r.stdout.decode('utf-8')
    except Exception:
        text = None
    if text is None:
        path = os.path.join(ROOT, note_path)
        if os.path.exists(path):
            text = open(path, encoding='utf-8').read()
    _ART_CACHE[note_path] = text
    return text


def article_hash(text):
    import hashlib
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16] if text is not None else None


def article_quote(note_path, label):
    """記事（note-articles/、origin/main）の該当肢の解説を、そのまま取り出す。独自の解説は作らない。"""
    text = read_article(note_path)
    if text is None:
        return None
    lines = text.split('\n')
    key = re.sub(r'[正誤]$', '', label)
    head = re.compile(r'^###\s*(?:肢|空欄)?[（(【]?' + re.escape(key) + r'(?![0-9])')
    summ = re.compile(r'^[-・]\s*\*\*' + re.escape(key) + r'(?:[（(]|\*\*).*')
    section = ''
    for i, ln in enumerate(lines):
        if head.match(ln):
            j = i + 1
            while j < len(lines) and not re.match(r'^(###\s|##\s|---)', lines[j]):
                j += 1
            section = '\n'.join(lines[i:j]).strip()
            break
    summary = next((ln for ln in lines if summ.match(ln)), '')
    if not section and not summary:
        return None
    return {'section': section, 'summary': summary}


CHECKS = os.path.join(HERE, 'data', 'article_checks.json')
_CHECKS_CACHE = {}


def load_checks():
    if not _CHECKS_CACHE:
        if os.path.exists(CHECKS):
            _CHECKS_CACHE.update(json.load(open(CHECKS, encoding='utf-8')))
        else:
            _CHECKS_CACHE.update({'meta': {}, 'checked': {}, 'findings': []})
    return _CHECKS_CACHE


def print_checks(note_path, label, item_id=None):
    """事前に行った条文照合の結果。指摘があるときだけ詳しく出し、なければ1行。"""
    ck = load_checks()
    key = re.sub(r'[正誤]$', '', label)
    cov = ck['checked'].get(note_path)
    if cov is None:
        print('条文照合: 未実施（事前照合の対象外）')
        return
    stale = bool(cov.get('sha') and article_hash(read_article(note_path)) != cov['sha'])
    if stale:
        print('⚠️ 条文照合: この記事は、照合したあとにmainで更新されています。以下の照合結果は古い版に対するものです（再照合が必要）。')
    fs = [f for f in ck['findings'] if f['note_path'] == note_path and f['label'] in (key, '') and not f.get('resolved')]
    if not fs:
        print('条文照合: 指摘なし（事前に法令DBと照合済み）')
        return
    icon = {'error': '⚠️ 誤り', 'warn': '⚠️ 要修正', 'unverified': '❔ 根拠を確認できない'}
    print('【条文照合（事前確認）— 解説に指摘があります】')
    for f in fs:
        print(f'{icon.get(f["severity"], f["severity"])}: {f["problem"]}')
        if f.get('law_ref'):
            print(f'  照合した原文: {f["law_ref"]}')
        if f.get('proposal'):
            print(f'  訂正案（提案）: {f["proposal"]}')
    if item_id and not stale:
        auto_tag_article_fix(item_id, note_path, label, fs)


def auto_tag_article_fix(item_id, note_path, label, fs):
    """条文照合に指摘のある肢に、記事修正対象のタグ（article-fix）を自動で付ける（同じ肢に重複して付けない）。"""
    try:
        ensure_log_branch()
        if any(t['id'] == item_id and t['tag'] == 'article-fix' for t in read_tags()):
            return
        f = fs[0]
        note = f'{os.path.basename(note_path)} {label}: ' + (f.get('problem', '')[:90]) + ' → ' + (f.get('proposal', '')[:120])
        rec = {'t': now().isoformat(timespec='seconds'), 'id': item_id, 'tag': 'article-fix', 'note': '【自動】' + note}
        with open(TAGS, 'a', encoding='utf-8') as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
        print('🏷 記事修正対象として自動タグ付けしました（#article-fix）')
    except Exception as e:  # タグ付けの失敗で出題を止めない
        print(f'（自動タグ付けに失敗: {e}）')


def prune_resolved_article_fix():
    """自動で付けた #article-fix のうち、指摘がすべて処理済み（resolved）になったものを解除する。
    別セッションの古い記録を取り込んだときなどに、処理済みの肢へタグが戻るのを防ぐ。手動で付けたタグ（【自動】でないもの）は触らない。"""
    try:
        ck = load_checks()
        open_f = [f for f in ck.get('findings', []) if not f.get('resolved')]
        removed = []
        for t in read_tags():
            if t['tag'] != 'article-fix' or not t.get('note', '').startswith('【自動】'):
                continue
            m = re.match(r'【自動】(\S+?) (\S*?): ', t['note'])
            if not m:
                continue
            base, label = m.group(1), re.sub(r'[正誤]$', '', m.group(2))
            if any(f['note_path'].endswith('/' + base) and f['label'] in (label, '') for f in open_f):
                continue
            with open(TAGS, 'a', encoding='utf-8') as fh:
                fh.write(json.dumps({'t': now().isoformat(timespec='seconds'), 'id': t['id'], 'tag': 'article-fix', 'removed': True}, ensure_ascii=False) + '\n')
            removed.append(t['id'])
        return removed
    except Exception as e:  # 解除の失敗で処理を止めない
        print(f'（article-fix の整理に失敗: {e}）')
        return []


def print_explanation(it, limit=1):
    srcs = it.get('sources', [])
    print('【記事の解説（note-articles／mainから引用。独自の解説ではありません）】')
    shown = 0
    for sr in srcs:
        if shown >= limit:
            break
        q = article_quote(sr.get('note_path', ''), sr.get('label', ''))
        print(f'― {sr["q"]}{sr.get("label", "")}（{sr.get("note_path", "")}）')
        if q is None:
            print('  該当肢の解説が記事から取り出せませんでした。記事を直接開いて確認してください。')
        else:
            if q['section']:
                print(q['section'])
            if q['summary']:
                print('記事のまとめ: ' + q['summary'].lstrip('-・ ').strip())
        print_checks(sr.get('note_path', ''), sr.get('label', ''), it.get('id'))
        shown += 1
    if len(srcs) > shown:
        print(f'（ほか{len(srcs) - shown}件の出典は explain で表示）')


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
    count_focus()
    mark = {'known': '✅ 定着（正解）', 'miscon': '❌ 誤解（逆に覚えている）', 'unknown': '❔ 未習得（？）'}[res]
    print(mark)
    print(f'正解: {"〇（正しい記述）" if truth else "×（誤った記述）"}')
    srcs = '、'.join(f'{s["q"]}{s.get("label", "")}' for s in it.get('sources', [])[:4])
    print(f'出典: {srcs}' + (f'（ほか {len(it["sources"]) - 4}）' if len(it.get('sources', [])) > 4 else ''))
    if it.get('pair'):
        print(f'対比: {", ".join(it["pair"][:2])}（逆の結論になる類似肢）')
    print_explanation(it, limit=1)
    # 履歴
    st = item_state(read_log())[a.id]
    print(f'この肢: {st["n"]}回目（定着{st["known"]}／誤解{st["miscon"]}／未習得{st["unknown"]}）')
    cl = review_class(st)
    if cl:
        w = wrong_total(st)
        label = {'must': '要復習（優先して出す）', 'check': 'チェック扱い（優先度を下げて出す）', 'done': '復習から除外'}[cl]
        print(f'復習の状態: {label} — 誤解・未習得の通算{w}回、その後の連続正解{st["cons"]}回')
    if res != 'known':
        print('→ 復習には、日付をまたいだ翌日（日本時間0時）以降に出ます。')


def cmd_save(a):
    ensure_log_branch()
    sh('git', 'add', 'log.jsonl', cwd=LOGDIR)
    for fn, pth in (('tags.jsonl', TAGS), ('issues.jsonl', ISSUES)):
        if os.path.exists(pth):
            sh('git', 'add', fn, cwd=LOGDIR)
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
            # 別セッションの記録とぶつかったら、競合したファイルだけを行単位の和集合（時刻順）で統合する。
            # 競合していないファイルには触らない（以前は競合の有無に関わらずlog.jsonlを上書きし、空になる事故があった）
            names = sh('git', 'diff', '--name-only', '--diff-filter=U', check=False, cwd=LOGDIR).stdout.split()
            for fn in names:
                if fn not in ('log.jsonl', 'tags.jsonl', 'issues.jsonl'):
                    raise SystemExit(f'想定外の競合: {fn}（手動で解消してください）')
                ours = sh('git', 'show', f':2:{fn}', check=False, cwd=LOGDIR).stdout.splitlines()
                theirs = sh('git', 'show', f':3:{fn}', check=False, cwd=LOGDIR).stdout.splitlines()
                base = ours + [l for l in theirs if l not in set(ours)]
                lines = sorted((l for l in dict.fromkeys(base) if l.strip()), key=lambda l: json.loads(l).get('t', ''))
                open(os.path.join(LOGDIR, fn), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
                sh('git', 'add', fn, cwd=LOGDIR)
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
    print(f'({a.id}) {it["subject"]}／{it["topic"]}')
    print(stmt_text(it))
    print(f'正解: {"〇（正しい記述）" if it["truth"] else "×（誤った記述）"}')
    if it.get('pair'):
        print(f'対比: {", ".join(it["pair"])}（逆の結論になる類似肢）')
    print_explanation(it, limit=len(it.get('sources', [])))


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
    biasT = sum(1 for r in logs if r['truth'] and r['res'] == 'miscon' and not r.get('amended')); nT = sum(1 for r in logs if r['truth'] and r['ans'] != '?')
    biasF = sum(1 for r in logs if (not r['truth']) and r['res'] == 'miscon' and not r.get('amended')); nF = sum(1 for r in logs if (not r['truth']) and r['ans'] != '?')
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


def cmd_mark(a):
    """直前の回答の判定を訂正する（例: 〇×は合っていたが理解が誤っていた → miscon）。同じ肢は復習に戻る。"""
    ensure_log_branch()
    bank = load_bank()
    if a.id not in bank:
        raise SystemExit(f'ID不明: {a.id}')
    if not any(r['id'] == a.id for r in read_log()):
        raise SystemExit('この肢の回答記録がありません')
    rec = {'t': now().isoformat(timespec='seconds'), 'id': a.id, 'amend': True, 'res': a.res, 'note': a.note or ''}
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    st = item_state(read_log())[a.id]
    print(f'訂正しました: {a.id} → {a.res}（{"誤解" if a.res == "miscon" else "未習得" if a.res == "unknown" else "定着"}扱い）')
    cl = review_class(st)
    print('復習の状態: ' + ({'must': '要復習', 'check': 'チェック扱い', 'done': '復習から除外', None: '復習なし'}[cl]) + f'（誤解・未習得の通算{wrong_total(st)}回、連続正解{st["cons"]}回）')


def read_tags():
    """解除（removed）を反映した、現在有効なタグの一覧。"""
    if not os.path.exists(TAGS):
        return []
    cur = {}
    for l in open(TAGS, encoding='utf-8'):
        if not l.strip():
            continue
        r = json.loads(l)
        if r.get('removed'):
            cur.pop((r['id'], r['tag']), None)
        else:
            cur[(r['id'], r['tag'])] = r
    return list(cur.values())


def cmd_untag(a):
    ensure_log_branch()
    rec = {'t': now().isoformat(timespec='seconds'), 'id': a.id, 'tag': a.tag, 'removed': True}
    with open(TAGS, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f'タグを解除しました: {a.id} #{a.tag}')


def cmd_issue(a):
    """引用した解説（記事）の誤りの指摘と訂正案を記録する。記事そのものは書き換えない。"""
    ensure_log_branch()
    bank = load_bank()
    if a.id not in bank:
        raise SystemExit(f'ID不明: {a.id}')
    rec = {'t': now().isoformat(timespec='seconds'), 'id': a.id, 'sources': [f'{x["q"]}{x.get("label", "")}' for x in bank[a.id].get('sources', [])],
           'problem': a.problem, 'proposal': a.proposal or ''}
    with open(ISSUES, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f'記事の指摘を記録しました: {a.id}')


def cmd_tag(a):
    """肢にタグを付ける（例: nigate = 苦手分析シリーズの候補）。drill-log ブランチの tags.jsonl に追記。"""
    ensure_log_branch()
    bank = load_bank()
    if a.id not in bank:
        raise SystemExit(f'ID不明: {a.id}')
    rec = {'t': now().isoformat(timespec='seconds'), 'id': a.id, 'tag': a.tag, 'note': a.note or ''}
    with open(TAGS, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f'タグを付けました: {a.id} #{a.tag}' + (f'（{a.note}）' if a.note else ''))


def cmd_tags(a):
    """タグ付けした肢を一括で呼び出す。タグ名を省略すると、タグごとの件数を表示。"""
    ensure_log_branch()
    bank = load_bank()
    if a.tag in (None, 'article-fix'):
        prune_resolved_article_fix()
    tags = read_tags()
    if not a.tag:
        c = collections.Counter(t['tag'] for t in tags)
        for k, v in c.items():
            print(f'#{k}: {len(set(t["id"] for t in tags if t["tag"] == k))}肢')
        if not c:
            print('タグはありません')
        return
    seen = {}
    for t in tags:
        if t['tag'] == a.tag:
            seen[t['id']] = t   # 同じ肢は最後のメモを採用
    if a.json:
        print(json.dumps([{'id': i, 'subject': bank[i]['subject'], 'topic': bank[i]['topic'], 'statement': bank[i]['statement'],
                           'truth': bank[i]['truth'], 'sources': bank[i].get('sources', []), 'note': t['note'], 't': t['t']}
                          for i, t in seen.items() if i in bank], ensure_ascii=False, indent=1))
        return
    for i, t in seen.items():
        it = bank.get(i)
        if not it:
            continue
        srcs = '、'.join(f'{x["q"]}{x.get("label", "")}' for x in it.get('sources', [])[:4])
        print(f'({i}) {it["subject"]}／{it["topic"]}  出典: {srcs}')
        print(f'  {stmt_text(it)}')
        print(f'  正解: {"〇" if it["truth"] else "×"}' + (f'  メモ: {t["note"]}' if t['note'] else ''))
        print()


def cmd_checks(a):
    """事前の条文照合の結果を表示する。"""
    ck = load_checks()
    m = ck['meta']
    if not m:
        print('照合結果がありません（data/article_checks.json）'); return
    print(f'照合: {m.get("articles")}記事 / 指摘 {m.get("findings")} / 法令DB: {m.get("law_db")} / 実施日 {m.get("checked_at")}')
    sev = a.severity
    rows = [f for f in ck['findings'] if (not sev or f['severity'] == sev) and not f.get('resolved')]  # resolved＝記事側で処理済み
    for f in rows:
        print(f'\n[{f["severity"]}] {f["note_path"]} {f["label"]}')
        print(f'  {f["problem"]}')
        if f.get('law_ref'):
            print(f'  原文: {f["law_ref"]}')
        if f.get('proposal'):
            print(f'  訂正案: {f["proposal"]}')


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
    m = sub.add_parser('mark'); m.add_argument('id'); m.add_argument('res', choices=['miscon', 'unknown', 'known']); m.add_argument('--note')
    tg = sub.add_parser('tag'); tg.add_argument('id'); tg.add_argument('tag'); tg.add_argument('--note')
    ts = sub.add_parser('tags'); ts.add_argument('tag', nargs='?'); ts.add_argument('--json', action='store_true')
    ck = sub.add_parser('checks'); ck.add_argument('--severity', choices=['error', 'warn', 'unverified'])
    ut = sub.add_parser('untag'); ut.add_argument('id'); ut.add_argument('tag')
    fc = sub.add_parser('focus')
    fc.add_argument('action', choices=['on', 'off', 'status'])
    fc.add_argument('--exclude-subject', action='append')
    fc.add_argument('--exclude-topic', action='append')
    fc.add_argument('--count', type=int, default=100)
    isu = sub.add_parser('issue'); isu.add_argument('id'); isu.add_argument('problem'); isu.add_argument('--proposal')
    a = p.parse_args()
    {'start': cmd_start, 'next': cmd_next, 'answer': cmd_answer, 'save': cmd_save, 'report': cmd_report, 'explain': cmd_explain, 'mark': cmd_mark, 'tag': cmd_tag, 'tags': cmd_tags, 'untag': cmd_untag, 'checks': cmd_checks, 'issue': cmd_issue, 'focus': cmd_focus}[a.cmd](a)


if __name__ == '__main__':
    main()
