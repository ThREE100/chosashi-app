"""朝の択一ドリル（morning/problems/*.json）の機械チェック。
- 組合せ選択肢は5つ・互いに異なり、正解がちょうど1つ
- 各肢の根拠の引用が、法令の原文（note-articles/laws/）の該当条に一字一句あること
- 「書いて説明」の採点ポイントが、模範解答と引用条文の両方に含まれること
- 個人の演習結果・過去問の出典を入れていないこと
- 独立した照合（morning/review/<ID>.json）が、現在の問題文と同じ版に対して行われ、全肢の判定が一致していること
使い方: python3 daily-drill/check_am.py
"""
import glob
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lawtext import article, normalize  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LABELS = ['ア', 'イ', 'ウ', 'エ', 'オ']
BANNED = re.compile(r'誤答|正答率|回答回数|復習中|演習結果|令和[0-9０-９元]+年度|平成[0-9０-９元]+年度|第[0-9０-９]+問|年度.{0,6}問')
nerr = 0


def err(pid, msg):
    global nerr
    nerr += 1
    print(f'NG {pid}: {msg}')


def content_hash(p):
    """問題文・肢・選択肢の版。これが変わると独立照合をやり直す。"""
    s = json.dumps({'stem': p['stem'], 'mode': p['mode'], 'st': [(x['label'], x['text']) for x in p['statements']], 'ch': p['choices']}, ensure_ascii=False)
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def answer_set(p):
    want = (p['mode'] == '正しい')
    return {s['label'] for s in p['statements'] if s['truth'] == want}


def check(p):
    pid = p['id']
    if [s['label'] for s in p['statements']] != LABELS:
        err(pid, '肢はアイウエオの5つ')
    if p['mode'] not in ('正しい', '誤り'):
        err(pid, 'mode は「正しい」か「誤り」')
    ans = answer_set(p)
    ch = [tuple(c) for c in p['choices']]
    if len(ch) != 5 or len(set(map(frozenset, ch))) != 5:
        err(pid, '選択肢は互いに異なる5つ')
    hits = [i + 1 for i, c in enumerate(ch) if set(c) == ans]
    if len(hits) != 1:
        err(pid, f'正解の選択肢がちょうど1つではない（該当 {hits}、正解の組合せ {sorted(ans)}）')
    if len(ans) < 2:
        err(pid, '正解の組合せが1つ以下')
    for s in p['statements']:
        if not s['basis']:
            err(pid, f"{s['label']}: 根拠がない")
        for b in s['basis']:
            check_quote(pid, s['label'], b)
    w = p['write']
    cited = ''
    for b in w['basis']:
        check_quote(pid, '書く', b)
        cited += normalize(article(b['law'], b['article']) or '')
    model = normalize(''.join(w['model']))
    for pt in w['points']:
        if normalize(pt) not in model:
            err(pid, f'採点ポイント「{pt}」が模範解答にない')
        if normalize(pt) not in cited:
            err(pid, f'採点ポイント「{pt}」が引用条文にない（条文の言葉で採点ポイントを立てる）')
    blob = json.dumps(p, ensure_ascii=False)
    m = BANNED.search(blob)
    if m:
        err(pid, f'禁止語「{m.group()}」（個人の演習結果・過去問の出典は入れない）')
    # 独立照合
    rp = os.path.join(HERE, 'morning', 'review', pid + '.json')
    if not os.path.exists(rp):
        err(pid, '独立照合（morning/review/）がない')
    else:
        r = json.load(open(rp, encoding='utf-8'))
        if r.get('hash') != content_hash(p):
            err(pid, '独立照合が古い版に対するもの（問題文を直したら照合をやり直す）')
        for s in p['statements']:
            v = r.get('verdicts', {}).get(s['label'])
            if v is None:
                err(pid, f"独立照合に {s['label']} の判定がない")
            elif v != s['truth']:
                err(pid, f"独立照合の判定と不一致 {s['label']}（問題の想定 {s['truth']}、照合 {v}）")


def check_quote(pid, where, b):
    art = article(b['law'], b['article'])
    if art is None:
        err(pid, f"{where}: {b['law']}{b['article']} が原文にない")
        return
    if normalize(b['quote']) not in normalize(art):
        err(pid, f"{where}: 引用が{b['law']}{b['article']}の原文と一致しない「{b['quote'][:30]}…」")


def main():
    files = sorted(glob.glob(os.path.join(HERE, 'morning', 'problems', '*.json')))
    ids = []
    for fp in files:
        p = json.load(open(fp, encoding='utf-8'))
        ids.append(p['id'])
        check(p)
    print(f'{len(files)}問を確認。NG {nerr}件')
    return nerr


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
