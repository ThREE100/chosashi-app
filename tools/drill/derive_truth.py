#!/usr/bin/env python3
"""questions_raw.json から、標準形式（アからオ＋組合せ選択肢）の問題の肢ごとの正誤を、
正答番号と設問の極性（正しい／誤っている）から機械的に導く。記事の「ア（正）」表記があれば突き合わせる。
標準形式でないもの（対話・個数・空欄補充・1〜5の直接選択 等）は work/needs_llm.json に回す。"""
import json, re, os, glob, collections
HERE = os.path.dirname(__file__); WORK = os.path.join(HERE, 'work'); ROOT = os.path.join(HERE, '..', '..')
KANA = 'アイウエオ'
CH_RE = re.compile(r'(?:(\d)\s+([アイウエオ]{1,4})(?=\s|$))')

def split_quote(q):
    stem, alts, tail, mode = [], {}, [], 'stem'
    for ln in q:
        m = re.match(r'^([アイウエオ])\s+(.*)$', ln)
        if m and mode in ('stem', 'alts'):
            alts[m.group(1)] = m.group(2).strip(); mode = 'alts'; last = m.group(1); continue
        if mode == 'alts' and re.match(r'^[1-5１-５]\s', ln):
            tail.append(ln); mode = 'tail'; continue
        if mode == 'stem': stem.append(ln)
        elif mode == 'alts': alts[last] += ' ' + ln   # 肢の折り返し
        else: tail.append(ln)
    return ' '.join(stem), alts, ' '.join(tail)

def polarity(stem):
    if re.search(r'誤っ|誤り|不正確|適切なものとならない|できないもの|ことができない|取り扱うことのできない', stem): return 'wrong'
    if re.search(r'正しい|適切|できるもの|支持', stem): return 'right'
    return None

def main():
    raw = json.load(open(os.path.join(WORK, 'questions_raw.json'), encoding='utf-8'))
    note_marks = {}
    for x in raw:
        t = open(os.path.join(ROOT, x['note_path']), encoding='utf-8').read()
        m = re.findall(r'\*{0,2}([アイウエオ])[（(](正|誤)[）)]\*{0,2}', t)
        note_marks[x['id']] = dict(m) if len(m) == 5 else {}
    ok, queue, flags = [], [], []
    for x in raw:
        stem, alts, tail = split_quote(x['quote'])
        pol = polarity(stem)
        combos = {}
        for no, txt in CH_RE.findall(tail): combos[int(no)] = txt
        std = (len(alts) == 5 and len(combos) == 5 and '個' not in stem and '幾' not in stem
               and '対話' not in stem and '空欄' not in stem and pol is not None)
        ans = x['takuitsu_correctAnswer']
        if std and ans in combos:
            sel = set(combos[ans])
            truth = {l: ((l in sel) == (pol == 'right')) for l in KANA}
            nm = note_marks[x['id']]
            if nm and any((nm[l] == '正') != truth[l] for l in KANA):
                flags.append({'id': x['id'], 'reason': '記事の正誤表記と正答番号からの逆算が不一致', 'derived': truth, 'note': nm, 'answer': ans, 'combos': combos, 'pol': pol})
                queue.append({**x, 'why': 'conflict'}); continue
            ok.append({'id': x['id'], 'stem': stem, 'alts': alts, 'truth': truth, 'source': 'answer+polarity' + ('+note' if nm else '')})
        else:
            queue.append({**x, 'why': 'nonstandard' if not std else 'no_answer'})
    json.dump(ok, open(os.path.join(WORK, 'derived_ok.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(queue, open(os.path.join(WORK, 'needs_llm.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(flags, open(os.path.join(WORK, 'conflicts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('derived', len(ok), 'queue', len(queue), collections.Counter(q['why'] for q in queue))
main()
