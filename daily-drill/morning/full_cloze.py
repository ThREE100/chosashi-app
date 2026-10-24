"""空欄補充（write.cloze）を「問題対象の条文の全文」の形に組み直す。
各空欄を含む区間（…で区切られた部分）が原文のどの条のどの号・項にあるかを探し、その条の全文を号・項ごとの行にして、空欄の語の位置に {n} を入れる。
空欄のない号・項は、問題ページで番号だけの「（略）」になる（build.py の cloze_lines）。条が複数あるときは、条ごとに「第○条」の見出し行を置く。
表（不動産登記令別表・登録免許税法別表第一）にしかない区間を含む問は組み直さない（報告する）。
使い方: python3 daily-drill/morning/full_cloze.py [--write] [AM-002 …]"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import lawtext as LT  # noqa: E402
import check_am as C  # noqa: E402

KAN = {c: i for i, c in enumerate('〇一二三四五六七八九')}


def kan2int(s):
    if s.isdigit():
        return int(s)
    n, cur = 0, 0
    for ch in s:
        if ch in KAN:
            cur = KAN[ch]
        elif ch == '十':
            n += (cur or 1) * 10; cur = 0
        elif ch == '百':
            n += (cur or 1) * 100; cur = 0
    return n + cur


def arabic(head):
    m = re.match(r'第([0-9〇一二三四五六七八九十百]+)条(?:の([0-9〇一二三四五六七八九十百]+))?', head)
    return f'第{kan2int(m.group(1))}条' + (f'の{kan2int(m.group(2))}' if m.group(2) else '')


SKIP_LAWS = {'不動産登記令別表'}


def articles():
    """(法令, 条の番号, 表示用の行のリスト)。本則の最初の出現だけ。"""
    out = []
    for law, fns in LT.LAW_FILES.items():
        if law in SKIP_LAWS:
            continue
        seen = set()
        for fn in fns:
            lines = LT._lines(fn)
            for i, ln in enumerate(lines):
                m = re.match(r'^#{3,6} (第[0-9〇一二三四五六七八九十百]+条(?:の[0-9〇一二三四五六七八九十百]+)?)', ln)
                if not m:
                    continue
                aid = arabic(m.group(1))
                if aid in seen:
                    continue
                seen.add(aid)
                body = []
                for j in range(i + 1, len(lines)):
                    if re.match(r'^#{1,6} ', lines[j]):
                        break
                    t = re.sub(r'^\s*- ', '', lines[j]).strip()
                    if not t or re.fullmatch(r'（[^）]{1,30}）', t):
                        continue
                    body.append(t)
                out.append((law, aid, body))
    return out


ARTS = None


def nfind(line, seg):
    """空白を無視して line の中の seg の位置（元の line の添字）を返す。"""
    idx = [k for k, ch in enumerate(line) if not ch.isspace()]
    nl = ''.join(line[k] for k in idx)
    ns = re.sub(r'\s+', '', seg)
    p = nl.find(ns)
    if p < 0 or not ns:
        return None
    return idx[p], idx[p + len(ns) - 1] + 1


def rebuild(p):
    global ARTS
    if ARTS is None:
        ARTS = articles()
    w = p['write']
    pref = [b['law'] for b in w.get('basis', []) if 'law' in b]
    order = sorted(ARTS, key=lambda a: (a[0] not in pref,))
    placed = {}          # (law, aid) -> {行番号: 行}
    first = []
    for cl in w['cloze']:
        cl = re.sub(r'^(【[^】]*】|第[0-9]+条(?:の[0-9]+)?)\s*', '', cl)      # 行の頭の条の見出しは除いて探す
        for seg in cl.split('…'):
            if not re.search(r'\{\d+\}', seg):
                continue
            seg = seg.strip()
            filled = C.fill([seg], w['blanks'])[0]
            # seg を「文字」と「空欄」の部品に分け、埋めた文の何文字目がどの部品かを対応させる
            toks = []
            for i, part in enumerate(re.split(r'(\{\d+\})', seg)):
                if i % 2:
                    toks.append((part, len(w['blanks'][int(part[1:-1]) - 1])))
                else:
                    toks += [(ch, 1) for ch in part]
            hit = None
            for law, aid, body in order:
                key = (law, aid)
                cur = placed.get(key, {})
                src = [cur.get(k, ln) for k, ln in enumerate(body)]
                for k in range(len(src)):
                    for span in range(1, 6):          # 号・項をまたぐ区間は、続く行をつないで探す
                        if k + span > len(src):
                            break
                        joined = ''.join(re.sub(r'\s+', '', x) for x in src[k:k + span])
                        nseg = re.sub(r'\s+', '', filled)
                        q = joined.find(nseg)
                        if q >= 0 and nseg:
                            hit = (key, k, span, src, q)
                            break
                    if hit:
                        break
                if hit:
                    break
            if not hit:
                return None, f'区間「{filled[:30]}」が原文の条に見つからない（表など）'
            key, k, span, src, q = hit
            # 区間の各文字（空白を除く）が、どの行のどの位置かを求め、行ごとに置き換える
            pos = []
            for kk in range(k, k + span):
                pos += [(kk, ci) for ci, ch in enumerate(src[kk]) if not ch.isspace()]
            pos = pos[q:q + len(re.sub(r'\s+', '', filled))]
            t, out_by_line, cursor = 0, {}, 0
            nf = [ch for ch in filled if not ch.isspace()]
            for tok, ln_ in toks:
                if tok.isspace():
                    continue
                n = ln_ if len(tok) > 1 else 1
                kk = pos[cursor][0]
                out_by_line.setdefault(kk, []).append((pos[cursor][1], pos[cursor + n - 1][1] + 1, tok))
                cursor += n
            d = placed.setdefault(key, {})
            for kk, reps in out_by_line.items():
                line = d.get(kk, src[kk])
                for a, b, tok in sorted(reps, reverse=True):
                    line = line[:a] + tok + line[b:]
                d[kk] = line
            if key not in first:
                first.append(key)
    lines, basis = [], []
    body_of = {(l, a): b for l, a, b in ARTS}
    for key in first:
        law, aid = key
        if len(first) > 1:
            lines.append(f'【{law}{aid}】')
        for k, ln in enumerate(body_of[key]):
            lines.append(placed[key].get(k, ln))
        basis.append({'law': law, 'article': aid, 'quote': next(x for x in body_of[key] if x)[:40]})
    return lines, basis


def main():
    write = '--write' in sys.argv
    only = {a for a in sys.argv[1:] if a.startswith('AM-')}
    ok, ng = 0, []
    for fp in sorted(glob.glob(os.path.join(HERE, 'problems', 'AM-*.json'))):
        p = json.load(open(fp, encoding='utf-8'))
        if only and p['id'] not in only:
            continue
        lines, basis = rebuild(p)
        if lines is None:
            ng.append((p['id'], basis))
            continue
        found = sorted(int(x) for x in re.findall(r'\{(\d+)\}', '\n'.join(lines)))
        if found != list(range(1, len(p['write']['blanks']) + 1)):
            ng.append((p['id'], f'空欄の番号が揃わない {found}'))
            continue
        ok += 1
        if write:
            w = p['write']
            w['cloze'] = lines
            w['basis'] = basis
            w['model'] = C.fill(lines, w['blanks'])
            w['points'] = list(w['blanks'])
            w['prompt'] = '次の条文の空欄（　）に、条文の言葉を入れなさい（空欄のない号・項は（略）とした）。'
            json.dump(p, open(fp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for x in ng:
        print('組み直せない', *x)
    print(f'組み直し {ok}問、組み直せない {len(ng)}問' + ('（書き込み済み）' if write else '（試し）'))


if __name__ == '__main__':
    main()
