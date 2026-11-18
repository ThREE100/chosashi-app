"""シートのデータ（src/sheets/<ID>.py）から、note記事(.md)・画像(.png/.html)・プロンプトを作り、目次も作り直す。
使い方：python3 note-articles/ichimai-matome/src/build.py [ID ...]    （IDなしは、データのあるシート全部）
手で直すのは src/sheets/<ID>.py だけ。sheets/ の中の生成物は手で直さない。"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import catalog  # noqa: E402
import prompts  # noqa: E402
import render  # noqa: E402
from catalog import CAT, BY_ID, FIELDS  # noqa: E402


def load(cid):
    p = os.path.join(HERE, 'sheets', cid + '.py')
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location('sheet_' + cid.replace('-', '_'), p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    assert m.SHEET['id'] == cid, cid
    return m.SHEET


def cell(x):
    return x.replace('|', '／').replace('\n', ' ')


def block_md(b):
    L = []
    if b.get('title'):
        L += ['### ' + b['title'], '']
    k = b['kind']
    if k == 'table':
        L.append('| ' + ' | '.join(cell(h) for h in b['head']) + ' |')
        L.append('|' + '---|' * len(b['head']))
        for r in b['rows']:
            L.append('| ' + ' | '.join(cell(x) for x in r) + ' |')
    elif k == 'check':
        L += ['**' + b.get('yes_label', '書くもの') + '**', '']
        L += ['- ' + x for x in b['yes']]
        L += ['', '**' + b.get('no_label', '書かないもの') + '**', '']
        L += ['- ' + x for x in b['no']]
    elif k == 'steps':
        L += ['%d. %s' % (i, x) for i, x in enumerate(b['items'], 1)]
    elif k == 'defs':
        for t, d in b['items']:
            L += ['- **%s**：%s' % (t, d)]
    elif k == 'text':
        L.append(b['text'])
    if b.get('note'):
        L += ['', b['note']]
    L.append('')
    return L


def article(c, s, size):
    fname = FIELDS[c['field']][0]
    img = os.path.basename(catalog.path(c, 'png'))
    h = s['header']
    L = ['## 【土地家屋調査士試験】%s_一枚まとめ_%s～%s～' % (c['id'].replace('-', '_'), c['title'], c['catch']), '',
         '**一枚まとめ　%s　｜　対象条文：%s**' % (fname, s['articles']), '',
         '> 【画像挿入】%s　（この一枚の画像。保存しておけば、通信なしで見返せます）' % img, '',
         '### この一枚で言えること', '']
    L += ['- ' + x for x in s['conclusion']] + ['']
    for b in s['blocks']:
        L += block_md(b)
    ex = s['example']
    L += ['### %s：%s' % (ex['kind'], ex['title']), '']
    L += ['- ' + x if not x.startswith(('　', ' ')) else x for x in ex['lines']] + ['']
    L += ['### 間違えやすい点', '']
    L += ['%d. %s' % (i, t) for i, t in enumerate(s['traps'], 1)] + ['']
    L += ['### 根拠とくわしい記事', '']
    L += ['- 根拠：' + '、'.join(s['basis'])]
    if s.get('more'):
        L += ['- くわしく読める記事：' + '、'.join('`%s`' % m for m in s['more'])]
    L += ['']
    if s.get('unverified'):
        L += ['**確認事項（原文を確かめられなかった根拠）**', '']
        L += ['- ' + x for x in s['unverified']] + ['']
    if s.get('note_law'):
        L += ['**法改正・時点の注**：' + s['note_law'], '']
    L += ['---', '', '## 見出し画像用フレーズ', '',
          '- 1行目：%s' % h['l1'], '- 2行目：%s（強調：%s）' % (h['l2'], h['hl']), '- 副題：%s' % prompts.sub_line(c), '', '---', '',
          '## 見出し画像プロンプト（note用・1280×670）', '',
          '女性のMCキャラクター1人だけを描く（トリ先生・藍子は入れない）。キャラクターシート（MC-01〜MC-04）の4枚を添付してから貼る。', '',
          '```', prompts.header_prompt(c, h), '```', '', '---', '',
          '## 見出し画像プロンプト（Instagram用・1080×1440）', '',
          '```', prompts.header_prompt_ig(c, h), '```', '']
    z = s.get('zukai')
    if z:
        L += ['---', '', '## インフォグラフィック プロンプト（イラスト図解・note用）', '',
              '文字の一枚（画像`%s`）とは別に、仕組みを絵で見せたいときに使う。画像の生成と目視確認はChatGPTで行う。' % img, '',
              '```', prompts.zukai_prompt(c, z, False), '```', '', '---', '',
              '## インフォグラフィック プロンプト（イラスト図解・Instagram用・1080×1440）', '',
              '```', prompts.zukai_prompt(c, z, True), '```', '']
    L += ['---', '', '*画像（%s）のサイズ：%d×%d。HTMLで組んで書き出した文字の図。*' % (img, size[0], size[1]), '']
    return '\n'.join(L)


def mokuji():
    built = {c['id'] for c in CAT if load(c['id'])}
    L = ['## 【土地家屋調査士試験】一枚まとめ_目次', '',
         '移動中やすきま時間に、分野ごとの要点を確かめるためのシリーズです。1つの論点を、スマホで読み切れる「一枚」にまとめます。**すべて無料で公開します。**', '',
         '- 記事は1枚につき1本です。画像（PNG）も同じ内容で用意するので、保存すれば通信なしで見返せます。',
         '- 年度別の解説とは役割が違います。年度別の解説は解いたあとの復習で、この一枚まとめは解く前や移動中に、要点だけをさっと確かめるためのものです。',
         '- 一枚に入りきらない論点は「その2」に分けます。詰め込みません。', '',
         '### 一枚の読み方', '',
         '1. 何についての一枚か（条文番号つき）', '2. この一枚で言えること（3行）', '3. 本体（表・手順・書くものと書かないもの、のどれか）',
         '4. 数値の入った計算例、または書き方の例', '5. 間違えやすい点（3つまで）', '6. 根拠の条文と、くわしく読める記事', '']
    L += ['### 第1弾（12枚）', '', '| 順 | ID | タイトル | 形 | 状況 |', '|---|---|---|---|---|']
    order = ['E-01', 'C-01', 'C-02', 'E-02', 'E-03', 'A-01', 'A-02', 'A-03', 'B-01', 'D-01', 'D-02', 'H-01']
    assert set(order) == {c['id'] for c in CAT if c['first']}
    for i, cid in enumerate(order, 1):
        c = BY_ID[cid]
        st = '公開可' if cid in built else '準備中'
        link = '[%s](sheets/%s/%s_%s.md)' % (c['title'], c['field'], cid, c['slug']) if cid in built else c['title']
        L.append('| %d | %s | %s | %s | %s |' % (i, cid, link, c['kind'], st))
    L += ['', '### 全体の分野（全%d枚。「その2」を含む）' % len(CAT), '']
    for f, (fname, _, _) in FIELDS.items():
        cs = [c for c in CAT if c['field'] == f]
        L += ['#### %s　%s（%d枚）' % (f, fname, len(cs)), '']
        for c in cs:
            t = c['title']
            if c['id'] in built:
                t = '[%s](sheets/%s/%s_%s.md)' % (t, f, c['id'], c['slug'])
            if c['first']:
                t = '**' + t + '**'
            L.append('- %s　%s' % (c['id'], t))
        L.append('')
    L += ['### ご要望をお寄せください', '', '「この論点を一枚にしてほしい」という声があれば、コメントでお知らせください。順番や内容に反映します。', '',
          '### 確認事項', '',
          '- 法令の内容は、条文の原文で確かめて作ります。通達や先例など原文を確かめられなかった根拠は、その一枚の末尾に分けて書きます。',
          '- 法改正があったものは、一枚の末尾に改正の時点を書きます。', '']
    open(os.path.join(ROOT, '01-mokuji.md'), 'w', encoding='utf-8').write('\n'.join(L))


def main(ids):
    jobs, metas = [], []
    for c in CAT:
        if ids and c['id'] not in ids:
            continue
        s = load(c['id'])
        if not s:
            continue
        jobs.append((render.sheet_html(c, s), os.path.join(ROOT, catalog.path(c, 'png'))))
        metas.append((c, s))
    res = render.render_many(jobs)
    for (c, s), (w, h, over) in zip(metas, res):
        md = article(c, s, (w, h))
        open(os.path.join(ROOT, catalog.path(c, 'md')), 'w', encoding='utf-8').write(md)
        print('%s %dx%d%s' % (c['id'], w, h, '  [はみ出し %d]' % over if over else ''))
    mokuji()


if __name__ == '__main__':
    main(set(sys.argv[1:]))
