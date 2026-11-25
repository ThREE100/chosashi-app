"""条文の逆引き図鑑 note記事シリーズを組み立てる。使い方：python3 note-unei/jobun-gyakubiki/note-series/src/build.py
dNN.py（記事ごとのデータ）から、NN-<slug>/article.md・zukai-prompts.md・header-prompts.md と 00-mokuji.md を作る。
生成物は手で直さない（データを直して作り直す）。"""
import glob
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402

SERIES_NAME = '条文の逆引き図鑑'


def modules():
    out = []
    for p in sorted(glob.glob(os.path.join(HERE, 'd[0-9][0-9].py'))):
        out.append(importlib.import_module(os.path.basename(p)[:-3]))
    return out


def full_title(m):
    return f"【土地家屋調査士試験】{SERIES_NAME} 第{m.NO}回〜{m.TITLE}〜"


def folder(m):
    return os.path.join(lib.SERIES, f"{m.NO:02d}-{m.SLUG}")


def img(m, kind, k=None):
    base = f"jg{m.NO:02d}_{kind}" + (f"{k:02d}" if k is not None else '')
    return base


def marker(name, what):
    return f"> 📷 **画像挿入：{what}**（`{name}.png`）"


def render_shi(sid, point):
    t = lib.truth(sid)
    return f"- {lib.shi_ref(sid)}【{'○' if t else '×'}】→ {point}"


def render_article(m, all_mods):
    L = []
    L.append('# 投稿メモ（noteには貼らない）')
    L.append('')
    L.append(f"- タイトル：{full_title(m)}")
    L.append(f"- 関連：{m.LAWS}")
    L.append('- 図解・間違いノートのプロンプト：`zukai-prompts.md`（note用・Instagram用）／見出し画像：`header-prompts.md`（note用・Instagram用）')
    L.append('- ハッシュタグ案：#土地家屋調査士 #土地家屋調査士試験 #不動産登記法 #過去問 #条文')
    L.append('- 公開前に：本文の「★」に、関連マガジン・前後の回の記事のリンクを入れる。図鑑のURLは図鑑の公開後に有効になる（`../README.md`）。')
    L.append('')
    L.append('## 本文')
    L.append('')
    L.append(f"## {full_title(m)}")
    L.append('')
    L.append(f"**関連：{m.LAWS}**")
    L.append('')
    for p in m.LEAD:
        L.append(p)
        L.append('')
    if getattr(m, 'POSTER', None):
        L.append(marker(img(m, 'soron'), f"総論（{m.POSTER['title']}）"))
        L.append('')
    if m.JOBUN:
        L.append('### この記事の読み方')
        L.append('')
        L.append('- **出た年度**は、平成17年度〜令和8年度の択一式の全肢解説のうち、その条文を法令名つきで引いている肢を数えたものです（図鑑と同じ数え方）。')
        L.append('- **出題された肢**の【○】【×】は、出題された文そのものの正誤（現行法令で確かめたもの）です。→ の後ろが、覚えておく正しい結論です。')
        L.append('- 肢の一覧は、本試験でくり返し出る形の肢を選んで載せています（出た年度の肢を全部は載せていません）。令和8年度の肢は、正誤を一問一答のデータで確かめられないので載せていません。')
        L.append('')
    for sec in getattr(m, 'SECTIONS', []):
        L.append(f"### {sec['h']}")
        L.append('')
        for p in sec['body']:
            if p == '__MOKUJI__':
                for o in all_mods:
                    if o.NO:
                        L.append(f"- 第{o.NO}回　{o.TITLE}（{o.LAWS}）")
                L.append('')
                continue
            L.append(p)
            L.append('')
        if sec.get('zu'):
            L.append(marker(img(m, 'kakuron', sec['zu_no']), f"各論（{sec['zu']['title']}）"))
            L.append('')
    zk = 0
    for j in m.JOBUN:
        zk += 1
        law, art = j['law'], j['art']
        cap = lib.caption(law, art)
        L.append(f"### {lib.law_name(law)} {lib.jn(art)}" + (f"（{cap}）" if cap else ''))
        L.append('')
        L.append(f"**出た年度**：{lib.band(law, art)}")
        L.append('')
        L.append('**条文（必要な部分）**')
        L.append('')
        for q in j['quotes']:
            L.append(f"> {q}")
            L.append('>')
        if L[-1] == '>':
            L.pop()
        L.append('')
        L.append('**本番で見るところ**')
        L.append('')
        for p in j['points']:
            L.append(f"- {p}")
        L.append('')
        L.append('**出題された肢**')
        L.append('')
        for sid, pt in j['shi']:
            L.append(render_shi(sid, pt))
        L.append('')
        L.append(marker(img(m, 'kakuron', zk), f"各論（{j['zu']['title']}）"))
        L.append('')
    if m.MISTAKES:
        L.append('### 間違いノート')
        L.append('')
        L.append('過去問で取り違えやすいところを、「よくある思い込み」→「正しい判断」→「見分けるコツ」の順に並べました。')
        L.append('')
        for k, x in enumerate(m.MISTAKES, 1):
            L.append(f"#### {k}. {x['title']}")
            L.append('')
            L.append(f"**よくある思い込み**：{x['wrong']}")
            L.append('')
            L.append(f"**正しい判断**：{x['right']}")
            L.append('')
            L.append('**見分けるコツ**：')
            for s in x['steps']:
                L.append(f"- {s}")
            L.append('')
            L.append(f"**誤りやすいポイント**：{x['callout']}")
            L.append('')
            if x.get('shi'):
                L.append('**このわなが出た肢**：' + '、'.join(f"{lib.shi_ref(s)}【{'○' if lib.truth(s) else '×'}】" for s in x['shi']))
                L.append('')
            L.append(marker(img(m, 'machigai', k), f"間違いノート（{x['title']}）"))
            L.append('')
    L.append('### まとめ')
    L.append('')
    for s in m.SUMMARY:
        L.append(f"- {s}")
    L.append('')
    if m.JOBUN:
        L.append('### 図鑑で続きを引く')
        L.append('')
        L.append('この記事で扱った条文の、ほかの年度の肢は図鑑のページにすべて並んでいます（各肢から年度別の全肢解説へ進めます）。')
        L.append('')
        for j in m.JOBUN:
            L.append(f"- {lib.law_name(j['law'])} {lib.jn(j['art'])}：{lib.page_url(j['law'], j['art'])}")
        L.append('')
    L.append('### 次回')
    L.append('')
    L.append(m.NEXT)
    L.append('')
    L.append('★ 関連マガジン（リンクを設定）')
    L.append('')
    L.append('わかりにくかったところ、図鑑で引いてみてほしい条文があれば、コメントで教えてください。フォローしていただくと、次の回の公開をお知らせできます。')
    L.append('')
    L.append('### 確認事項')
    L.append('')
    L.append('- 条文は、`note-articles/laws/` に収録した原文（法令の公布・改正を反映したもの）で確かめ、引用は原文と機械的に照合しています。')
    L.append('- 出題された肢の【○】【×】は、平成17年度〜令和7年度の択一式を肢ごとに分けた一問一答の問題集（現行法令で確かめた正誤）から取りました。出題当時の正答と、法改正のために食い違う肢があります。令和8年度の肢は、正誤を確かめ終えていないため載せていません。')
    L.append('- 年度の数・肢の数は、年度別の全肢解説で法令名つきで引いている条文だけを数えたものです。法令名のない「法第○条」は数えていないので、実際より少なめです。')
    for n in getattr(m, 'NOTES', []):
        L.append(f"- {n}")
    L.append('')
    L.append('（本文ここまで）')
    L.append('')
    return '\n'.join(L)


def render_zukai(m):
    L = [f"# 第{m.NO}回「{m.TITLE}」図解・間違いノートのプロンプト", '',
         '`src/build.py` が `src/d%02d.py` から作る（手で直さない）。画像の生成はChatGPTで行う。各図に note用（縦長）と Instagram用（1080×1440）の2つがある。文字はどちらも同じで、大きさと余白だけ違う。' % m.NO, '',
         '## 確かめること', '',
         '- 文字が「」の中と1字ずつ一致しているか（簡体字・繁体字・余計な文字がないか）。図番が入っていないか。',
         '- ○（正しい）は青、×（思い込み）は赤。1つの箱に○と×が両方入っていないか。',
         '- 背景が不透明か。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足す。', '']
    items = []
    if getattr(m, 'POSTER', None):
        p = m.POSTER
        sub = f"{SERIES_NAME} 第{m.NO}回"
        items.append((img(m, 'soron'), f"総論：{p['title']}",
                      lib.poster_prompt(p['title'], p['topics'], sub, p['cards'], p.get('size', '1080x1920')),
                      lib.poster_prompt(p['title'], p['topics'], sub, p['cards'], note=False)))
    zk = 0
    for sec in getattr(m, 'SECTIONS', []):
        if sec.get('zu'):
            z = sec['zu']
            items.append((img(m, 'kakuron', sec['zu_no']), f"各論：{z['title']}",
                          lib.explainer_prompt(z['title'], z['sub'], z['layout'], z['footer'], z.get('size', '1080x1500')),
                          lib.explainer_prompt(z['title'], z['sub'], z['layout'], z['footer'], note=False)))
    for j in m.JOBUN:
        zk += 1
        z = j['zu']
        items.append((img(m, 'kakuron', zk), f"各論：{z['title']}",
                      lib.explainer_prompt(z['title'], z['sub'], z['layout'], z['footer'], z.get('size', '1080x1500')),
                      lib.explainer_prompt(z['title'], z['sub'], z['layout'], z['footer'], note=False)))
    for k, x in enumerate(m.MISTAKES, 1):
        items.append((img(m, 'machigai', k), f"間違いノート：{x['title']}", lib.mistake_prompt(x), lib.mistake_prompt(x, note=False)))
    L.append('## 図の一覧')
    L.append('')
    for name, what, _, _ in items:
        L.append(f"- `{name}.png`（Instagram用 `{name}_ig.png`）：{what}")
    L.append('')
    for name, what, pn, pi in items:
        L.append(f"## {what}")
        L.append('')
        L.append(f"### note用（`{name}.png`）")
        L.append('')
        L.append('```')
        L.append(pn)
        L.append('```')
        L.append('')
        L.append(f"### Instagram用（`{name}_ig.png`）")
        L.append('')
        L.append('```')
        L.append(pi)
        L.append('```')
        L.append('')
    return '\n'.join(L), items


def render_header(m):
    h = m.HEADER
    L = [f"# 第{m.NO}回「{m.TITLE}」見出し画像のプロンプト", '',
         'MC1人（キャラクターシート MC-01〜MC-04 を添付）。このシリーズは、ほかのシリーズの水彩の空とは雰囲気を変え、世界の有名な本屋をオマージュした店内を背景にする（店名・ロゴ・看板の文字は描かせない）。ポーズと表情は回ごとに変える（`00-mokuji.md` の一覧）。画像に数字は入れない（条文番号は漢数字）。', '',
         f"- オマージュ元：{h['store']}",
         f"- ポーズ：{h['pose_ja']}",
         f"- 表情：{h['face_ja']}", '',
         f"## note用（1280×670）", '', f"ファイル名：`jg{m.NO:02d}_header_note.png`", '', '```', lib.header_prompt(h), '```', '',
         f"## Instagram用（1080×1440）", '', f"ファイル名：`jg{m.NO:02d}_header_ig.png`", '', '```', lib.header_prompt(h, ig=True), '```', '']
    return '\n'.join(L)


def render_mokuji(mods):
    c = lib.total_counts()
    L = [f"# {SERIES_NAME} note記事シリーズ 目次", '',
         f"図鑑（{c['jobun']}条文・{c['shi_cited']}肢）を題材にした、全{len(mods)}回のnote記事。第0回で図鑑の使い方と全体像を示し、第1回からは本試験でくり返し出る条文を、つながりのある順に2〜5条ずつ取り上げる。", '',
         '各回にそろえるもの：記事（`NN-*/article.md`）、総論の図解1枚、条文ごとの各論の図解、間違いノートの図解、見出し画像（いずれも note用・Instagram用の2種類。`zukai-prompts.md`・`header-prompts.md`）。', '',
         '## 目次', '']
    for m in mods:
        L.append(f"- **第{m.NO}回 {m.TITLE}**（{m.LAWS}）")
        L.append(f"  - フォルダ：`{m.NO:02d}-{m.SLUG}/`")
        if m.JOBUN:
            L.append('  - 出た年度：' + '／'.join(f"{lib.law_name(j['law'])}{lib.jn(j['art'])} {lib.JOBUN[(j['law'], j['art'])]['years']}年度" for j in m.JOBUN))
        L.append(f"  - 見出し画像：{m.HEADER['store']}をオマージュ／{m.HEADER['pose_ja']}／{m.HEADER['face_ja']}")
    L.append('')
    L.append('## 並べ方の考え方')
    L.append('')
    L.append('- 土地の登記（第1回〜第4回）→建物の登記（第5回〜第8回）→申請人と共有（第9回・第10回）→地図と保存期間（第11回）→民法（第12回）→土地家屋調査士法（第13回）の順。前の回の知識を次の回で使う順にした（例：第3回の「まとめて申請」は第1回・第2回の分筆・合筆と、第7回の合併で使う）。')
    L.append('- 取り上げる条文は、図鑑で出た年度が多い条文と、一問一答の演習で取り違えが重なった論点の条文から選んだ。演習の記録は、論点の選び方と間違いノートの題材選びにだけ使い、記事・画像には数字も「何回間違えた」も出さない（`../README.md`、`senryaku.md` 6-1）。')
    L.append('')
    return '\n'.join(L)


def main():
    mods = modules()
    for m in mods:
        d = folder(m)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'article.md'), 'w', encoding='utf-8').write(render_article(m, mods))
        z, _ = render_zukai(m)
        open(os.path.join(d, 'zukai-prompts.md'), 'w', encoding='utf-8').write(z)
        open(os.path.join(d, 'header-prompts.md'), 'w', encoding='utf-8').write(render_header(m))
    open(os.path.join(lib.SERIES, '00-mokuji.md'), 'w', encoding='utf-8').write(render_mokuji(mods))
    print(f"{len(mods)}回分を作成")


if __name__ == '__main__':
    main()
