"""答えの漏れの洗い出し：申請書の答え（登記の目的、新しい地番・家屋番号・符号、地積・床面積、原因の文言）が、問題ページ（答案用紙を含む）に
そのまま書かれていないかを探して、coverage/leak_report.md に書き出す（人が見て判断する候補の一覧。自動ではNGにしない）。
問題文で与えた値（登記記録の地番・地積など）も拾うので、候補ごとに「問題文で与えるべき値か、答えを明かしているか」を判断する。
あわせて、機械で決められる次の3つは NG として数え、1件でもあれば終了コード1を返す（check_all.py から呼ぶ）。
  H1 白紙の答案用紙に行の名前（（イ）（ロ）・地番・符号・合体前の甲建物など）が印刷されている
  H2 問題ページの題（q_title）に登記の目的の答えが入っている
  H3 問題ページの本文に登記の目的の答えがそのまま出ている（「…」「…」のうちから選ばせる候補の列挙は除く）
本番形式（sougou/）の第2部の申請書も同じように調べる。
使い方: python3 daily-drill/leak_check.py [PM-34 …]"""
import glob
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build as B  # noqa: E402

TOK = re.compile(r'\d+番(?:の)?\d+|\d+番地\d*|\d+\.\d{2}|符号\d+')


def text_of(h):
    h = re.sub(r'<style>.*?</style>', '', h, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', h))


def answers(p):
    out = []
    for it in p['form']['items']:
        if it['kind'] == 'field':
            out.append((it['label'], it['answer']))
        else:
            for r in it['rows']:
                for c, v in zip(it['cols'][1:] if it['cols'][0] == '' else it['cols'], r['cells']):
                    out.append((f'{it["label"]}/{r["name"]}/{c}', v))
    return out


def scan(p, qtext):
    hits = []
    for lab, v in answers(p):
        if not v:
            continue
        if lab.startswith('登記の目的') and v in qtext:
            hits.append(('目的', lab, v))
        for t in set(TOK.findall(v)):
            if t in qtext:
                hits.append(('値', lab, t))
        for ph in re.findall(r'[^\s、。]*(?:に分筆|から分筆|に合併|から一部合併|を合併|に一部合併|を合体|と合体|から区分|に区分|を分割|から分割)', v):
            if ph in qtext:
                hits.append(('原因', lab, ph))
    return hits


NOTE = re.compile(r'[^。]{0,30}(?:「[^」]*何[^」]*」の形|と書く|とする。)[^。]{0,10}')


# 事実として書かざるを得ないもの（承諾書の文言など）。答えを明かしていないことを人が確かめたものだけ足す
ALLOW = {('PM-67', '共用部分である旨の登記')}


def choice_list(q, v):
    """v が「…」「…」と並べた候補の1つとして出ているだけか"""
    for m in re.finditer(re.escape('「' + v + '」'), q):
        around = q[max(0, m.start() - 40):m.end() + 40]
        if around.count('「') >= 3:
            continue
        return False
    return v not in q.replace('「' + v + '」', '')


def hard(p, q):
    ng = []
    for nm in re.findall(r'<td class="rn">([^<]+)</td>', B.form_body(p)):
        ng.append(f'H1 {p["id"]} 白紙の答案用紙に行の名前「{nm}」がある')
    goal = [it['answer'] for it in p['form']['items'] if it['kind'] == 'field' and it['label'].startswith('登記の目的')]
    for g in [g for g in goal if g]:
        if g in B.q_title(p):
            ng.append(f'H2 {p["id"]} 題に登記の目的「{g}」がある')
        if g in q and not choice_list(q, g) and (p['id'], g) not in ALLOW:
            i = q.find(g)
            ng.append(f'H3 {p["id"]} 本文に登記の目的「{g}」がある：…{q[max(0, i - 20):i + len(g) + 10].strip()}…')
    return ng


def problems():
    for fp in sorted(glob.glob(os.path.join(HERE, 'evening', 'problems', 'PM-*.json')), key=lambda f: int(re.findall(r'\d+', os.path.basename(f))[0])):
        p = json.load(open(fp, encoding='utf-8'))
        if p['kind'] == 'shinsei2':
            yield p, text_of(B.pm_q(p))
    sys.path.insert(0, os.path.join(HERE, 'sougou'))
    import build_sougou as S  # noqa: E402
    for sid in sorted(d for d in os.listdir(os.path.join(HERE, 'sougou')) if re.fullmatch(r's\d+', d)):
        meta, parts = S.parts(sid)
        if 'form' in parts:
            p = parts['form']
            yield p, text_of(B.pm_q(p)) + ' ' + ' '.join(meta.get('lead', []))


def main():
    only = set(sys.argv[1:])
    rows, notes, ngs, n = [], [], [], 0
    for p, q in problems():
        if only and p['id'] not in only:
            continue
        ngs += hard(p, q)
        for kind, lab, t in scan(p, q):
            i = q.find(t)
            rows.append(f'| {p["id"]} | {kind} | {lab} | {t} | …{q[max(0, i - 25):i + len(t) + 15].strip()}… |')
            n += 1
        for m in NOTE.finditer(q):
            notes.append(f'| {p["id"]} | {m.group(0).strip()} |')
    out = ['# 答えの漏れの候補（leak_check.py で自動生成。人が判断する）', '',
           '申請書の答えの文字列が、問題ページにそのまま出ている箇所。「値」は問題文で与えるべきもの（登記記録の地番・地積など）も含むので、答えを明かしているものだけ直す。', '',
           f'候補 {n}件', '', '| 問 | 種類 | 答えの欄 | 文字列 | 問題ページでの前後 |', '|---|---|---|---|---|'] + [r.replace('\n', ' ') for r in rows] + [
        '', f'## 注で書き方を指定している箇所（{len(notes)}件）', '',
        '本番の注の程度（単位・「何階部分」の形・書かない欄の扱い）なら残す。原因の文言・行の組み立て・地積の決め方など、判断そのものを教えている注は直す（指示書のC-3）。', '',
        '| 問 | 注 |', '|---|---|'] + [r.replace('\n', ' ').replace('|', '｜', r.count('|') - 3) for r in notes] + [
        '', f'## NG（{len(ngs)}件）', ''] + [f'- {x}' for x in ngs]
    open(os.path.join(HERE, 'coverage', 'leak_report.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    for x in ngs:
        print('NG ' + x)
    print(f'答えの漏れ：NG {len(ngs)}件、候補 {n}件、書き方を指定する注 {len(notes)}件（coverage/leak_report.md）')
    return 1 if ngs else 0


if __name__ == '__main__':
    sys.exit(main())
