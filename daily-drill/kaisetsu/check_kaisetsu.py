"""ドリルの解説記事（kaisetsu/*.md）の形式チェック。使い方: python3 daily-drill/kaisetsu/check_kaisetsu.py"""
import json, glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ng = 0


def bad(f, m):
    global ng
    ng += 1
    print(f'NG {os.path.basename(f)}: {m}')


for f in sorted(glob.glob(os.path.join(HERE, 'day*-kaisetsu.md'))):
    s = open(f, encoding='utf-8').read()
    lines = s.split('\n')
    t = lines[0]
    m = re.fullmatch(r'## 【土地家屋調査士受験生向け】毎朝ドリル_Day(\d{3})_択一解説～(.+)～', t)
    if not m:
        bad(f, 'タイトル行の形')
    else:
        if len(m.group(2)) > 25:
            bad(f, f'キャッチフレーズが25字超（{len(m.group(2))}字）')
        if m.group(1) != re.search(r'day(\d{3})-', os.path.basename(f)).group(1):
            bad(f, 'タイトルのDay番号とファイル名が合わない')
    if not re.search(r'^\*\*出題：毎日ドリル　第\d+日（朝）　択一\*\*$', s, re.M):
        bad(f, '出題行')
    body = s.split('\n## 見出し画像用フレーズ')[0]
    prose = '\n'.join(l for l in body.split('\n') if not l.startswith('>'))
    if re.search(r'\([^()`]*[ぁ-んァ-ヶ一-龥][^()`]*\)', prose):
        bad(f, '半角括弧の日本語')
    for w in ('決定木', '判定木', 'ツリー', '照合済み', '.md', '.py', 'note-articles'):
        if w in body.replace('`note-articles/laws/`', ''):
            bad(f, f'本文に禁止語「{w}」')
    if re.search(r'昭和?\d+\.\d+\.\d+民|登記研究\d|最判', body):
        bad(f, '判例・先例・専門誌の番号')
    heads = re.findall(r'^### ([アイウエオ])：', body, re.M)
    if heads != list('アイウエオ'):
        bad(f, f'肢の見出し {heads}')
    for h in re.split(r'^### ', body, flags=re.M)[1:6]:
        if '**たとえば**、' not in h:
            bad(f, f'「たとえば」がない肢: {h[:3]}')
    mm = re.search(r'### まとめ\n\n((?:- \*\*[アイウエオ]（[正誤]）\*\* .+\n)+)', body)
    if not mm or mm.group(1).count('\n') != 5:
        bad(f, 'まとめの箇条書き（5項目）')
    if not re.search(r'^\*\*正解：.+の組合せ（選択肢[1-5]番）\*\*$', body, re.M):
        bad(f, '正解の行')
    if body.find('**正解') < body.find('### まとめ'):
        bad(f, '正解がまとめより前')
    fr = s.split('## 見出し画像用フレーズ')[1].split('\n## ')[0]
    if len(re.findall(r'^- ', fr, re.M)) != 5:
        bad(f, '見出し画像用フレーズが5つでない')
    # PDCA追加（Day001-003作成時）: 問題データとの一致、補足説明があれば④が要る
    jf = os.path.join(HERE, '..', 'morning', 'problems', f'AM-{m.group(1)}.json') if m else ''
    if jf and os.path.exists(jf):
        pj = json.load(open(jf, encoding='utf-8'))
        qs = '\n'.join(l for l in lines if l.startswith('>'))
        if pj['stem'] not in qs:
            bad(f, '引用の問題文が問題データと一致しない')
        for st in pj['statements']:
            if f"{st['label']}　{st['text']}" not in qs:
                bad(f, f'引用の肢{st["label"]}が問題データと一致しない')
        want = pj.get('mode') != '正しい'
        wr = [st['label'] for st in pj['statements'] if st['truth'] != want]
        ix = [i + 1 for i, c in enumerate(pj['choices']) if list(c) == wr]
        if not re.search(rf'^\*\*正解：{"・".join(wr)}の組合せ（選択肢{ix[0] if ix else 0}番）\*\*$', body, re.M):
            bad(f, '正解の行が問題データの正解と一致しない')
        for st in pj['statements']:
            mt = re.search(rf'- \*\*{st["label"]}（([正誤])）\*\*', body)
            if not mt or (mt.group(1) == '正') != st['truth']:
                bad(f, f'まとめの肢{st["label"]}の正誤が問題データと一致しない')
    if '### 補足説明' in body and '・間違いノート）' not in s:
        bad(f, '補足説明があるのに④（間違いノート）のプロンプトがない')
    if re.search(r'^- .*[?!]', fr, re.M):
        bad(f, '見出し画像用フレーズに半角の？！がある')
    if m:
        dn = f'Day{m.group(1)}'
        if f'毎朝ドリル　{dn}　' not in s:
            bad(f, f'見出し画像のサブタイトルに「毎朝ドリル　{dn}　」がない')
        if 'peaceful morning room' not in s:
            bad(f, '見出し画像の背景（朝日の差し込む部屋）の指定がない')
        if 'OUTFIT OVERRIDE' not in s or 'horizontal navy-blue stripes' not in s:
            bad(f, '見出し画像に服装の指定（白の長袖に紺の横ライン・襟なし）がない')
        if 'POSE AND EXPRESSION (changes every time)' not in s:
            bad(f, '見出し画像にポーズ・表情の指定がない')
        if re.search(r'第[一二三四五六七八九十]+日　', s):
            bad(f, '見出し画像に漢数字の「第○日」が残っている')
    # PDCA追加（Day005-120作成時）: 段落の長さ、絵に入れる語のラテン文字
    for para in body.split('\n\n'):
        if para.startswith(('>', '- ', '###', '**', '---', '#', '1. ')) or para.lstrip().startswith('|'):
            continue
        if len(para) > 140:
            bad(f, f'1段落が140字超（{len(para)}字）: {para[:20]}')
    for pb in re.findall(r'```text\n(.*?)\n```', s, re.S)[1:]:
        for wm in re.finditer(r'「([^」]*)」', pb):
            if re.search(r'[A-Za-z]', wm.group(1)) and 'Day' not in wm.group(1):
                bad(f, f'絵に入れる語にラテン文字: 「{wm.group(1)}」')
    if re.search(r'^\s*\|.*\|\s*$', re.sub(r'```.*?```', '', s, flags=re.S), re.M):
        bad(f, 'Markdownの表がある（noteでは表示できない。箇条書きにする）')
    blocks = re.findall(r'```text\n(.*?)\n```', s, re.S)
    if len(blocks) < 3:
        bad(f, 'プロンプトのコードブロックが足りない')
    for i, b in enumerate(blocks):
        needs = ('TEXT (critical)', 'BACKGROUND (critical)', 'Final check before rendering') if i == 0 else ('CRITICAL TEXT REQUIREMENT', 'BACKGROUND REQUIREMENT', 'Final check before rendering')
        for need in needs:
            if need not in b:
                bad(f, f'プロンプト{i + 1}に {need} がない')
        if 'transparent' not in b:
            bad(f, f'プロンプト{i + 1}に透過禁止の語がない')
        if i >= 1 and 'ILLUSTRATION TEXT RULE' not in b:
            bad(f, f'プロンプト{i + 1}に ILLUSTRATION TEXT RULE がない')
        # Final check の漢字リストが本文に実在するか
        mk = re.search(r'paying special attention to ([^\s,]+(?:・[^\s,]+)+)', b.split('Final check')[-1])
        if mk:
            for ch in mk.group(1).split('・'):
                if ch not in b.split('Final check')[0]:
                    bad(f, f'プロンプト{i + 1}の注意漢字「{ch}」が本文にない')
        lists = re.findall(r'[一-龥](?:・[一-龥]){2,}', b)  # 3字以上の並び（「条・準」のような2字の語は注意漢字リストとみなさない）
        rest = b
        for l in lists:
            rest = rest.replace(l, '')
        for l in lists:
            for ch in l.split('・'):
                if ch not in rest:
                    bad(f, f'プロンプト{i + 1}の注意漢字「{ch}」がプロンプトの本文にない')
    ov = blocks[1] if len(blocks) > 1 else ''
    if ov:
        if 'NO NUMBERING' not in ov:
            bad(f, '総論に NO NUMBERING がない')
        if len(re.findall(r'^--- COLUMN [AB], CARD \d', ov, re.M)) != 5:
            bad(f, '総論のカードが5枚でない')
        if len(re.findall(r'^Words allowed inside this illustration', ov, re.M)) != 5:
            bad(f, '総論の Words allowed が5つでない')
print(f'NG {ng}件')
sys.exit(1 if ng else 0)
