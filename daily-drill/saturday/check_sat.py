"""土曜の20問模擬（saturday/q/SATnn-Qmm.json）の機械チェック。
1問ごと：
- 肢はア〜オの5つ、問う向き（正しい／誤っている）に当てはまる肢がちょうど2つ
- 選択肢は「2つの組合せ」が互いに異なる5つで、正解の組合せと一致するものがちょうど1つ（有効な選択肢がない・2つある問題を防ぐ）
- 各肢の根拠の引用が、法令の原文（note-articles/laws/）の該当条に一字一句あること。解説（note）とひっかけの型があること
- 会話形式の問は、会話の中で ア〜オ の発言が1回ずつ出ること
- 個人の演習結果・過去問の出典を入れていないこと
- 独立に解いた結果（saturday/review/SATnn.json）が、今の問題文の版に対するもので、全肢の判定と選んだ番号が想定と一致すること
回全体：民法3・不登法16・調査士法1、会話形式1問、正解の番号の偏り（同じ番号は6問まで、各番号を2問以上）
使い方: python3 daily-drill/saturday/check_sat.py [SAT01]"""
import glob
import hashlib
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from lawtext import article, normalize  # noqa: E402

LABELS = ['ア', 'イ', 'ウ', 'エ', 'オ']
BANNED = re.compile(r'誤答|正答率|回答回数|復習中|演習結果|令和[0-9０-９元]+年度|平成[0-9０-９元]+年度|第[0-9０-９]+問|年度.{0,6}問')
TAX = json.load(open(os.path.join(os.path.dirname(HERE), 'taxonomy.json'), encoding='utf-8'))
nerr = 0


def err(pid, msg):
    global nerr
    nerr += 1
    print(f'NG {pid}: {msg}')


def content_hash(q):
    """問題文・会話・肢・選択肢の版。変わったら独立に解き直す"""
    s = json.dumps({'stem': q['stem'], 'mode': q['mode'], 'dlg': q.get('dialogue'), 'st': [(x['label'], x['text']) for x in q['statements']], 'ch': q['choices']}, ensure_ascii=False)
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def answer_set(q):
    want = q['mode'] == '正しい'
    return sorted(s['label'] for s in q['statements'] if s['truth'] == want)


def answer_no(q):
    ans = set(answer_set(q))
    hits = [i + 1 for i, c in enumerate(q['choices']) if set(c) == ans]
    return hits[0] if len(hits) == 1 else None


def check_doc(pid, where, b):
    """先例・判例など、条文の原文では決まらない根拠は、リポジトリの過去問の解説（note-articles/）の記載に一字一句あることで確かめる"""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if 'saturday' not in __file__ else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    fp = os.path.join(root, b['doc'])
    if not b['doc'].startswith('note-articles') or not os.path.exists(fp):
        err(pid, f"{where}: 根拠の文書 {b['doc']} がない（note-articles/ の過去問の解説に限る）")
        return
    if normalize(b['quote']) not in normalize(open(fp, encoding='utf-8').read()):
        err(pid, f"{where}: 引用が {b['doc']} の記載と一致しない「{b['quote'][:30]}…」")


def check_quote(pid, where, b):
    if 'doc' in b:
        return check_doc(pid, where, b)
    art = article(b['law'], b['article'])
    if art is None:
        err(pid, f"{where}: {b['law']}{b['article']} が原文にない")
    elif normalize(b['quote']) not in normalize(art):
        err(pid, f"{where}: 引用が{b['law']}{b['article']}の原文と一致しない「{b['quote'][:30]}…」")


def check_q(q):
    pid = q['id']
    if [s['label'] for s in q['statements']] != LABELS:
        err(pid, '肢はアイウエオの5つ')
    if q['mode'] not in ('正しい', '誤り'):
        err(pid, 'mode は「正しい」か「誤り」')
    want_word = '正しいもの' if q['mode'] == '正しい' else '誤っているもの'
    if want_word not in q['stem']:
        err(pid, f'問いの文に「{want_word}」がない（mode と問いの文が食い違う）')
    ans = answer_set(q)
    if len(ans) != 2:
        err(pid, f'問う向きに当てはまる肢が2つでない（{ans}）')
    ch = [tuple(c) for c in q['choices']]
    if len(ch) != 5 or any(len(c) != 2 or not set(c) <= set(LABELS) for c in ch) or len(set(map(frozenset, ch))) != 5:
        err(pid, '選択肢は、ア〜オから2つを選ぶ組合せの、互いに異なる5つ')
    hits = [i + 1 for i, c in enumerate(ch) if set(c) == set(ans)]
    if len(hits) != 1:
        err(pid, f'正解の組合せ{ans}に当たる選択肢がちょうど1つでない（{hits or "有効な選択肢がない"}）')
    for s in q['statements']:
        if not s.get('basis'):
            err(pid, f"{s['label']}: 根拠がない")
        for b in s.get('basis', []):
            check_quote(pid, s['label'], b)
        if len(s.get('note', '')) < 15:
            err(pid, f"{s['label']}: 解説が短い（なぜ正しい／誤りかを書く）")
        names = TAX['traps_morning']
        if s.get('trap') and s['trap'] not in names:
            err(pid, f"{s['label']}: ひっかけの型 {s['trap']} が taxonomy.json にない")
    if not any(s.get('trap') for s in q['statements'] if s['truth'] is False):
        err(pid, '誤りの肢に、ひっかけの型（trap）が1つもない')
    if q['format'] == '会話':
        labs = [t.get('label') for t in q.get('dialogue', []) if t.get('label')]
        if sorted(labs) != LABELS:
            err(pid, f'会話の中で ア〜オ の発言が1回ずつ出ていない（{labs}）')
        texts = {s['label']: s['text'] for s in q['statements']}
        for t in q.get('dialogue', []):
            if t.get('label') and t['text'] != texts.get(t['label']):
                err(pid, f"会話の{t['label']}の発言と肢の文が一致しない")
    blob = json.dumps(q, ensure_ascii=False)
    m = BANNED.search(blob)
    if m:
        err(pid, f'禁止語「{m.group()}」（個人の演習結果・過去問の出典は入れない）')


def check_set(sid, qs, plan):
    if [q['no'] for q in qs] != list(range(1, 21)):
        err(sid, f'問1〜問20がそろっていない（{[q["no"] for q in qs]}）')
    f = Counter(q['field'] for q in qs)
    if f != Counter({'不登法': 16, '民法': 3, '調査士法': 1}):
        err(sid, f'分野の配分が民法3・不登法16・調査士法1でない（{dict(f)}）')
    if sum(q['format'] == '会話' for q in qs) != 1:
        err(sid, '会話形式の問がちょうど1問でない')
    for q in qs:
        pl = plan[q['no'] - 1]
        if (q['field'], q['format']) != (pl['field'], pl['format']):
            err(q['id'], f'計画（plan.json）の分野・形式と違う')
    nos = Counter(answer_no(q) for q in qs)
    if max(nos.values()) > 6 or any(nos.get(k, 0) < 2 for k in range(1, 6)):
        err(sid, f'正解の番号が偏っている（{dict(sorted(nos.items(), key=lambda x: (x[0] is None, x[0] or 0)))}）')
    # 独立に解いた結果
    rp = os.path.join(HERE, 'review', sid + '.json')
    if not os.path.exists(rp):
        err(sid, '独立に解いた結果（saturday/review/）がない')
        return
    rv = json.load(open(rp, encoding='utf-8'))
    for q in qs:
        r = rv.get(q['id'])
        if r is None:
            err(q['id'], '独立に解いた結果がない')
            continue
        if r.get('hash') != content_hash(q):
            err(q['id'], '独立に解いた結果が古い版に対するもの（問題文を直したら解き直す）')
        for s in q['statements']:
            v = r.get('verdicts', {}).get(s['label'])
            if v != s['truth']:
                err(q['id'], f"独立に解いた判定と不一致 {s['label']}（想定 {s['truth']}、解いた結果 {v}）")
        if r.get('choice') != answer_no(q):
            err(q['id'], f"独立に選んだ番号と正解が違う（正解 {answer_no(q)}、選んだ {r.get('choice')}）")


def load(sid):
    qs = []
    for fp in sorted(glob.glob(os.path.join(HERE, 'q', f'{sid}-Q*.json'))):
        q = json.load(open(fp, encoding='utf-8'))
        q['id'] = os.path.basename(fp)[:-5]
        qs.append(q)
    return qs


def main():
    plan = json.load(open(os.path.join(HERE, 'plan.json'), encoding='utf-8'))
    one = [a for a in sys.argv[1:] if '-Q' in a]
    if one:                       # 作成中は1問ずつ：python3 check_sat.py SAT01-Q05 SAT01-Q06
        for pid in one:
            q = json.load(open(os.path.join(HERE, 'q', pid + '.json'), encoding='utf-8'))
            q['id'] = pid
            check_q(q)
            print(f'{pid}：正解 {answer_set(q)} ＝ 選択肢 {answer_no(q)}')
        print(f'NG {nerr}件')
        return nerr
    sids = sys.argv[1:] or sorted({os.path.basename(f).split('-')[0] for f in glob.glob(os.path.join(HERE, 'q', 'SAT*-Q*.json'))})
    for sid in sids:
        qs = load(sid)
        for q in qs:
            check_q(q)
        check_set(sid, qs, plan)
        print(f'{sid}：{len(qs)}問を確認')
    print(f'NG {nerr}件')
    return nerr


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
