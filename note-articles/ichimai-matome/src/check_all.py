"""一枚まとめの機械チェック。NG 0件にする。
使い方：python3 note-articles/ichimai-matome/src/check_all.py [ID ...]
確かめること：スロットの欠け・字数・表の列数／法令名つきの「第N条」が原文にあるか／claims（原文の文言）／計算例のverify()／
禁止語（個人の演習結果・問題番号・年度・樹形図の語・確かめていない主張）／生成物（md・png）がそろい、画像が長すぎないか。"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import catalog  # noqa: E402
import lawlib  # noqa: E402
import render  # noqa: E402
from catalog import CAT  # noqa: E402

BAD = re.compile(r'決定木|判定木|ツリー|木に当て|誤答|演習結果|間違えた回数|頻出|必ず出る|アガルート|予備校|過去問集|第\d+問|令和\d+年度|平成\d+年度|午後の部|午前の部|図\d|画像\d')
LATIN_IN_HEADER = re.compile(r'[0-9A-Za-z０-９]')
ng = []


def bad(cid, msg):
    ng.append('%s: %s' % (cid, msg))


def norm(t):
    return re.sub(r'[\s　]+', '', t)


def all_strings(s):
    out = list(s['conclusion']) + list(s['traps']) + list(s['basis']) + list(s['example']['lines']) + [s['example']['title']]
    for b in s['blocks']:
        out.append(b.get('title', ''))
        out.append(b.get('note', ''))
        k = b['kind']
        if k == 'table':
            out += b['head'] + [x for r in b['rows'] for x in r]
        elif k == 'check':
            out += b['yes'] + b['no'] + [b.get('yes_label', ''), b.get('no_label', '')]
        elif k == 'steps':
            out += b['items']
        elif k == 'defs':
            out += [x for t in b['items'] for x in t]
        elif k == 'text':
            out.append(b['text'])
    out += [s.get('note_law', '')] + list(s.get('unverified', []))
    return [x for x in out if x]


def main(ids):
    from PIL import Image
    n = 0
    for c in CAT:
        if ids and c['id'] not in ids:
            continue
        p = os.path.join(HERE, 'sheets', c['id'] + '.py')
        if not os.path.exists(p):
            continue
        n += 1
        cid = c['id']
        spec = importlib.util.spec_from_file_location('sh_' + cid.replace('-', '_'), p)
        m = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(m)
        except Exception as e:  # 計算例のassertを含む
            bad(cid, 'データの読み込みで失敗（計算例のassertを含む）: %r' % e)
            continue
        s = m.SHEET
        if s.get('id') != cid:
            bad(cid, 'idが違う')
        for k in ('law', 'articles', 'conclusion', 'blocks', 'example', 'traps', 'basis', 'claims', 'header'):
            if k not in s:
                bad(cid, 'キー %s がない' % k)
        if any(k not in s for k in ('law', 'articles', 'conclusion', 'blocks', 'example', 'traps', 'basis', 'claims', 'header')):
            continue
        if s['law'] not in lawlib.FILES or not lawlib.FILES[s['law']]:
            bad(cid, 'lawが原文のない法令: %s' % s['law'])
            continue
        if len(s['conclusion']) != 3:
            bad(cid, '結論は3行（今 %d）' % len(s['conclusion']))
        if not 2 <= len(s['traps']) <= 3:
            bad(cid, 'ひっかけは2〜3つ（今 %d）' % len(s['traps']))
        if not 1 <= len(s['blocks']) <= 4:
            bad(cid, '本体のブロックは1〜4個（今 %d）' % len(s['blocks']))
        if s['example'].get('kind') not in ('計算例', '書き方の例'):
            bad(cid, 'exampleのkindは「計算例」か「書き方の例」')
        if c['kind'] == '計算の型' and s['example'].get('kind') != '計算例':
            bad(cid, '計算の型のシートは「計算例」を入れる')
        for x in s['conclusion'] + s['traps']:
            if len(x) > 150:
                bad(cid, '長すぎる（%d字）: %s…' % (len(x), x[:20]))
        for b in s['blocks']:
            if b['kind'] == 'table':
                if len(b['head']) > 4:
                    bad(cid, '表は4列まで')
                for r in b['rows']:
                    if len(r) != len(b['head']):
                        bad(cid, '表の列数が合わない: %s' % r)
                    for x in r:
                        if len(x) > 80:
                            bad(cid, '表のセルが長い（%d字）: %s…' % (len(x), x[:15]))
                if len(b['rows']) > 10:
                    bad(cid, '表は10行まで')
            elif b['kind'] == 'steps' and len(b['items']) > 8:
                bad(cid, '手順は8つまで')
            elif b['kind'] not in ('table', 'check', 'steps', 'defs', 'text'):
                bad(cid, 'ブロックの種類が不明: %s' % b['kind'])
        strs = all_strings(s)
        for x in strs:
            if x.count('**') % 2:
                bad(cid, '太字の ** が閉じていない: %s…' % x[:20])
            mm = BAD.search(x)
            if mm:
                bad(cid, '禁止語「%s」: %s…' % (mm.group(0), x[:25]))
        # 引用の実在
        for x in strs:
            for law, key, raw in lawlib.citations(x, s['law']):
                if law not in lawlib.FILES or not lawlib.FILES[law]:
                    continue
                if not lawlib.has(law, key):
                    bad(cid, '原文にない条文: %s（%s）' % (raw, law))
        # claims
        if len(s['claims']) < 4:
            bad(cid, 'claims（原文の文言の確認）は4つ以上')
        for law, key, phrase in s['claims']:
            if law not in lawlib.FILES or not lawlib.FILES[law]:
                bad(cid, 'claimsの法令が不明: %s' % law)
                continue
            if norm(phrase) not in norm(lawlib.text(law, key)):
                bad(cid, '%s第%s条に文言がない: 「%s」' % (law, key, phrase[:30]))
        # 見出し・図解
        h = s['header']
        for k in ('l1', 'l2', 'hl', 'left', 'right'):
            if k not in h:
                bad(cid, 'headerに %s がない' % k)
        if 'l1' in h and (LATIN_IN_HEADER.search(h['l1'] + h['l2'])):
            bad(cid, '見出し画像の文字に数字・英字がある')
        z = s.get('zukai')
        if z:
            if not 4 <= len(z['cards']) <= 6:
                bad(cid, 'zukaiのカードは4〜6枚')
        # 計算例の検算
        if hasattr(m, 'verify'):
            try:
                m.verify()
            except AssertionError as e:
                bad(cid, 'verify()が失敗: %s' % e)
        # 生成物
        for ext in ('md', 'png', 'html'):
            if not os.path.exists(os.path.join(ROOT, catalog.path(c, ext))):
                bad(cid, '生成物がない: %s（build.pyを実行）' % ext)
        png = os.path.join(ROOT, catalog.path(c, 'png'))
        if os.path.exists(png):
            w, hh = Image.open(png).size
            if w != render.W or hh > render.MAX_H:
                bad(cid, '画像が大きすぎる（%dx%d。高さ%d以内に。内容を減らすか「その2」に分ける）' % (w, hh, render.MAX_H))
        md = os.path.join(ROOT, catalog.path(c, 'md'))
        if os.path.exists(md):
            t = open(md, encoding='utf-8').read()
            for key in ('> 【画像挿入】', '## 見出し画像プロンプト（note用', '## 見出し画像プロンプト（Instagram用', '### 間違えやすい点'):
                if key not in t:
                    bad(cid, '記事に「%s」がない' % key)
            if BAD.search(t.split('## 見出し画像用フレーズ')[0]):
                bad(cid, '記事本文に禁止語: %s' % BAD.search(t.split('## 見出し画像用フレーズ')[0]).group(0))
    for x in ng:
        print('NG', x)
    print('%d枚を確認。NG %d件' % (n, len(ng)))
    return len(ng)


if __name__ == '__main__':
    sys.exit(1 if main(set(sys.argv[1:])) else 0)
