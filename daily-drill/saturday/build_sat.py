"""土曜の20問模擬を A4 の HTML にする。
  out/satNN.html      問題（20問・解答用紙つき。本番どおり 1問あたり約3分、20問で60分）
  out/satNN-ans.html  正解一覧・各肢の正誤と解説・根拠条文（原文の引用）
使い方: python3 daily-drill/saturday/build_sat.py [SAT01]"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import build as B  # noqa: E402
from check_sat import load, answer_no, answer_set  # noqa: E402

E, CIRC = B.E, B.CIRC
TRAPS = B._TAX['traps_morning']


def q_html(q):
    s = f'<div class="q" style="margin-top:3mm"><b>第{q["no"]}問</b>　{E(q["stem"])}</div>'
    if q['format'] == '会話':
        s += '<table class="pt">' + ''.join(
            f'<tr><td style="width:12mm;vertical-align:top">{E(t["speaker"])}</td><td>{("（" + E(t["label"]) + "）") if t.get("label") else ""}{E(t["text"])}</td></tr>'
            for t in q['dialogue']) + '</table>'
    else:
        s += '<table class="pt">' + ''.join(f'<tr><td style="width:7mm;vertical-align:top">{E(x["label"])}</td><td>{E(x["text"])}</td></tr>' for x in q['statements']) + '</table>'
    s += '<p style="margin:1mm 0 0 7mm">' + '　　'.join(f'{CIRC[i]} {"".join(c)}' for i, c in enumerate(q['choices'])) + '</p>'
    return s


def sheet_html():
    cells = ''.join(f'<tr><td style="width:14mm">第{n}問</td>' + ''.join(f'<td style="text-align:center">{c}</td>' for c in CIRC) + '<td style="width:20mm"></td></tr>' for n in range(1, 21))
    return ('<h2>解答用紙（番号に○。迷った問は右の欄に印）</h2><table class="pt"><tr><th></th>' + ''.join(f'<th>{c}</th>' for c in CIRC) + '<th>迷い</th></tr>' + cells + '</table>')


def build(sid):
    qs = load(sid)
    head = B.head(f'{sid[3:]}回（土曜）', '択一式20問の模擬', '民法3問・不動産登記法16問（うち会話形式1問）・土地家屋調査士法1問。目安60分（1問3分）', 60)
    body = head + sheet_html()
    body += ''.join(q_html(q) for q in qs)
    open(os.path.join(B.OUT, f'{sid.lower()}.html'), 'w', encoding='utf-8').write(B.page(f'土曜模擬 {sid}', body, f'{sid} 問題', flow=True, right='オリジナル問題（過去問の転載ではない）'))
    a = B.head(f'{sid[3:]}回（土曜）', '解答・解説', '正解の一覧、各肢の正誤と解説、根拠条文の原文', 60)
    a += '<h2>正解の一覧</h2><table class="pt"><tr>' + ''.join(f'<th>第{q["no"]}問</th>' for q in qs[:10]) + '</tr><tr>' + ''.join(f'<td style="text-align:center">{CIRC[answer_no(q) - 1]}</td>' for q in qs[:10]) + '</tr><tr>' + ''.join(f'<th>第{q["no"]}問</th>' for q in qs[10:]) + '</tr><tr>' + ''.join(f'<td style="text-align:center">{CIRC[answer_no(q) - 1]}</td>' for q in qs[10:]) + '</tr></table>'
    a += '<p class="src">採点：20問中14問（7割）以上を目標に。</p>'
    for q in qs:
        n = answer_no(q)
        a += f'<div class="q" style="margin-top:3mm"><b>第{q["no"]}問　正解 {CIRC[n - 1]}（{"・".join(answer_set(q))}）</b>　{E(q["theme"])}（{E(q["field"])}。{E(q["mode"])}ものを選ぶ）</div>'
        for x in q['statements']:
            mark = '<span class="ok">○ 正しい</span>' if x['truth'] else '<span class="ng">× 誤り</span>'
            tr = f'　<span class="src">［{E(x["trap"])} {E(TRAPS.get(x["trap"], ""))}］</span>' if x.get('trap') else ''
            a += f'<div style="margin:1mm 0 0 3mm"><b>{E(x["label"])}</b>　{mark}　{E(x["note"])}{tr}</div>'
            a += ''.join(B.quote_block(b) for b in x['basis'])
    open(os.path.join(B.OUT, f'{sid.lower()}-ans.html'), 'w', encoding='utf-8').write(B.page(f'土曜模擬 {sid} 解答', a, f'{sid} 解答', flow=True))
    print(f'out/{sid.lower()}.html・{sid.lower()}-ans.html を書き出し')


if __name__ == '__main__':
    for sid in sys.argv[1:] or sorted({os.path.basename(f).split('-')[0] for f in glob.glob(os.path.join(HERE, 'q', 'SAT*-Q*.json'))}):
        build(sid)
