#!/usr/bin/env python3
"""総合記事（assemble.py の出力）の読みやすさを整える後処理。
1) 見出し・ラベル・段落・箇条書きの間に空行を入れる（Markdownでは単独の改行は同じ段落につながり、ラベルが本文に埋もれるため）
2) `**結論**：本文` のような長いラベル行を、ラベルだけの行と本文の段落に分ける
3) 長い段落を、文の区切り（。）で125字以内（目安90字）に分ける（note-articles/tools/split_paragraphs.py と同じ考え方。「」（）の中では分けない）
4) `1) …` `1）…` の並びを番号つきリストにする
5) 民法編（sokatsu-01）は、章ごとに分割した記事（sokatsu-01-minpou-ch1〜3）も作る
使い方: python3 tools/drill/sokatsu/postprocess.py   （リポジトリ直下で実行。assemble.py のあとに行う）"""
import re, sys, pathlib, collections, json

ROOT = pathlib.Path(__file__).resolve().parents[3]
COL = ROOT / "note-articles/column"
LIMIT, TARGET = 125, 90

def sentences(p):
    out, cur, depth = [], '', 0
    for ch in p:
        cur += ch
        if ch in '「（': depth += 1
        elif ch in '」）': depth = max(0, depth - 1)
        elif ch == '。' and depth == 0:
            out.append(cur); cur = ''
    if cur: out.append(cur)
    return out

def split_para(p, limit=LIMIT, target=TARGET):
    if len(p) <= limit: return [p]
    ss = sentences(p)
    if len(ss) < 2: return [p]
    n = min(max(2, round(len(p) / target)), len(ss))
    pre = [0]
    for s in ss: pre.append(pre[-1] + len(s))
    L = len(ss)
    from functools import lru_cache
    @lru_cache(None)
    def f(i, k):
        if k == 1: return ((pre[L] - pre[i] - target) ** 2, (L,))
        res = None
        for j in range(i + 1, L - k + 2):
            c, rest = f(j, k - 1)
            c += (pre[j] - pre[i] - target) ** 2
            if res is None or c < res[0]: res = (c, (j,) + rest)
        return res
    _, cuts = f(0, n)
    out, i = [], 0
    for j in cuts:
        out.append(''.join(ss[i:j])); i = j
    res = []
    for x in out:
        if not x: continue
        res.extend(split_para(x, limit, target) if (len(x) > limit and len(sentences(x)) >= 2 and x != p) else [x])
    return res

NUM_SPLIT = re.compile(r'(?:(?<=。)|(?<=\s)|(?<=^))(\d)[)）]\s*')

def numbered_items(body):
    """`1) a。 2) b。` の並びを項目に分ける。先頭が `1)` でなければ None。"""
    if not re.match(r'^\s*1[)）]', body): return None
    parts = NUM_SPLIT.split(body.strip())
    # split は [空, '1', 'a', '2', 'b', ...] になる
    items = []
    for k in range(1, len(parts) - 1, 2):
        items.append((int(parts[k]), parts[k + 1].strip()))
    return items if len(items) >= 2 else None

LABEL_RE = re.compile(r'^\*\*([^*]{1,30})\*\*：(.*)$')
INLINE_LABELS = {'この論点で出た肢', 'この章の対象'}
FORCE_LABELS = {'結論', '中身の整理', 'たとえば', 'なぜ繰り返し間違えるのか', '判断のしかた', '肢ごとの判定',
                'この章の誤りの傾向', 'この章の直前チェック', 'どんな間違いか', 'この科目で目立つ論点', '対策'}

def reflow(text):
    L = text.rstrip('\n').split('\n')
    out = []
    def blank():
        if out and out[-1] != '': out.append('')
    def emit_para(body):
        items = numbered_items(body)
        if items:
            for n, t in items:
                out.append(f'{n}. {t}')
            blank(); return
        for part in split_para(body):
            blank(); out.append(part); blank()
    i = 0
    while i < len(L):
        ln = L[i].rstrip()
        i += 1
        if ln == '':
            blank(); continue
        if ln.startswith('#') or ln == '---':
            blank(); out.append(ln); blank(); continue
        m = LABEL_RE.match(ln)
        if m:
            lab, body = m.group(1), m.group(2).strip()
            if lab in INLINE_LABELS or (lab not in FORCE_LABELS and len(body) <= 40 and body):
                blank(); out.append(f'**{lab}**：{body}'); blank(); continue
            blank(); out.append(f'**{lab}**'); blank()
            if lab == 'この科目で目立つ論点' and body:
                for it in re.split(r'、(?=【)', body): out.append(f'- {it}')
                blank()
            elif body: emit_para(body)
            continue
        if re.match(r'^(\s*)- ', ln):
            body = ln.strip()[2:]
            indent = ln[:len(ln) - len(ln.lstrip())]
            if out and out[-1] != '' and not re.match(r'^\s*(- |\d+\. )', out[-1]): blank()
            if (not re.match(r'D\d{4} ', body)) and len(body) > LIMIT + 10 and not indent:
                parts = split_para(body, LIMIT, TARGET)
                for p in parts: out.append(f'- {p}')
            else:
                out.append(f'{indent}- {body}')
            continue
        if re.match(r'^\d+\. ', ln):
            if out and out[-1] != '' and not re.match(r'^\s*(- |\d+\. )', out[-1]): blank()
            out.append(ln); continue
        if re.match(r'^\d[)）]', ln):
            n, t = re.match(r'^(\d)[)）]\s*(.*)$', ln).groups()
            if out and out[-1] != '' and not re.match(r'^\s*(- |\d+\. )', out[-1]): blank()
            out.append(f'{n}. {t}'); continue
        if ln.startswith('>'):
            out.append(ln); continue
        if re.match(r'^【[A-Z0-9]+-\d+】', ln) and '、【' in ln and ln.endswith('肢）'):
            blank()
            for it in re.split(r'、(?=【)', ln.strip()): out.append(f'- {it}')
            blank(); continue
        emit_para(ln.strip())
    # 連続する空行をまとめる
    res = []
    for ln in out:
        if ln == '' and res and res[-1] == '': continue
        res.append(ln)
    while res and res[-1] == '': res.pop()
    return '\n'.join(res) + '\n'

def norm(t):
    return re.sub(r'[\s*#\-.)）：]', '', t)

# ---------------- 民法編の章分割 ----------------
CH_TITLES = {
    1: ('総則（意思表示・制限行為能力・代理・時効・条件）', '繰り返し間違える29肢を「誤答の型」ごとに一気読みで整理する'),
    2: ('物権（共有・占有・物権的請求権・通行権）', '繰り返し間違える20肢を「誰が・誰に」で整理する'),
    3: ('物権変動・対抗要件、地上権・質権、相続', '繰り返し間違える19肢を「いつ・誰に」で整理する'),
}
TYPE_LINES = [
    ('A', '原則と例外の取り違え', 'ただし書き・特則・例外を落とす'),
    ('B', '主体の取り違え', '誰が・誰に・誰を基準に、を取り違える'),
    ('C', '時点・期間・基準の取り違え', '完成の前か後か、いつからか、を取り違える'),
    ('D', '似た制度・似た登記との混同', '似ているが結論が逆の制度を同じに扱う'),
    ('E', '要件の欠落または過剰', '要らない要件を足す、必要な要件を落とす'),
    ('F', '数字・文言の暗記不足', '期間・割合・用語が出てこない'),
    ('G', '一般化のしすぎ・限定語の見落とし', '「必ず」「のみ」などに引きずられる'),
    ('H', '前提・事例の読み違い', '事例の設定や前提を読み違える'),
    ('I', '知識の空白', '制度そのものを知らず「わからない」と答える'),
    ('J', '結論の向きの逆転', 'できる／できない、有効／無効を逆に覚えている'),
]

def split_minpou(text, stem='sokatsu-01-minpou'):
    L = text.split('\n')
    idx = [i for i, l in enumerate(L) if re.match(r'^### 民法[①②③]', l)]
    cross = next(i for i, l in enumerate(L) if l.startswith('### 章をまたいで出る論点'))
    appendix = next(i for i, l in enumerate(L) if l.startswith('### 付録'))
    lead = next(l for l in L if l.startswith('この記事は、択一式の一問一答で'))
    bounds = idx + [cross]
    # 付録の肢の一覧（論点ID別）
    app_lines = [l for l in L[appendix:] if re.match(r'^- D\d{4} ', l)]
    made = []
    for k in (1, 2, 3):
        a, b = bounds[k - 1], bounds[k]
        chunk = L[a:b]
        while chunk and chunk[-1].strip() in ('', '---'): chunk.pop()
        title_line = chunk[0]
        body = chunk[1:]
        # 章の要素を取り出す
        txt = '\n'.join(body)
        n_items = int(re.search(r'\*\*この章の対象\*\*：(\d+)肢', txt).group(1))
        n_topics = int(re.search(r'(\d+)つの論点にまとめています', txt).group(1))
        ch_name, sub = CH_TITLES[k]
        title = f'## 【土地家屋調査士受験生向け】直前期の苦手論点つぶし総合記事①民法編（{k}/3）{ch_name}〜{sub}〜'
        o = [title, '', '**対象科目：民法（択一式）**', '']
        o.append(f'この記事は、択一式の一問一答で繰り返し間違えている肢、または「わからない」と答えた肢を、科目ごとに集めて一気に読めるようにまとめた総合記事（全3本）の民法編を、章ごとに分けた第{k}章です。対象は{n_items}肢で、{n_topics}つの論点に整理しています。同じ論点・似た論点は1つの論点にまとめ、肢ごとの判定は各論点の最後に置いています。')
        o += ['', '---', '', '### この記事の使い方', '',
              '1. まず、下の「誤答の10の型」を読みます。自分の間違い方の癖に名前を付けておくと、肢を読むときに「今これを疑っている」と自覚できます。',
              '2. 論点を順に読みます。各論点は「結論 → 中身の整理 → たとえば → なぜ繰り返し間違えるのか → 判断のしかた → 肢ごとの判定」の順です。時間がない日は、結論と判断のしかた、章末の直前チェックだけでも一周できます。',
              '3. 最後に、付録の「最優先で潰す肢」で仕上げます。',
              '', '正誤の基準は現行法令です。「判例の立場」「実務の取扱い」と書いた項目は、条文に直接の根拠がない暗記項目なので、理屈で解こうとせず結論を覚えてください。',
              '', '---', '', '### 誤答の10の型', '',
              '各肢の誤答の原因を、最も近い型に分けています。実際にどう考えたかは本人にしか分かりませんから、型は「考えられる原因」の目安です。', '']
        o += [f'- 型{t}　{n}：{d}' for t, n, d in TYPE_LINES]
        o += ['', '全体版（直し方つき）は `note-articles/column/sokatsu-01-minpou.md` にあります。', '', '---', '']
        # 章の本文：論点 #### → ###、章の見出しは落とす
        body_txt = []
        for l in body:
            if l.startswith('#### '): l = '### ' + l[5:]
            body_txt.append(l)
        bt = '\n'.join(body_txt)
        # 「この章の対象」行は導入に反映済みなので落とす
        bt = re.sub(r'\*\*この章の対象\*\*：[^\n]*\n', '', bt)
        # 「この章の誤りの傾向」を見出しにする
        bt = bt.replace('**この章の誤りの傾向**\n', '### この章の誤りの傾向\n')
        bt = bt.replace('**この章の直前チェック**\n', '### この章の直前チェック\n')
        # 関連記事行は末尾へ
        rel = re.search(r'\n関連記事[：:][^\n]*\n?$', bt.rstrip('\n') + '\n')
        o.append(bt.strip('\n'))
        o += ['']
        ids = {f'M{k}'}
        pre = f'（M{k}-'
        mine = [l for l in app_lines if pre in l]
        o += ['---', '', '### 付録　最優先で潰す肢（誤答が3回以上の肢）', '']
        if mine:
            o += [f'誤答が3回以上に達した肢の一覧です（{len(mine)}肢）。誤答が多い順に並べ、〇×は正解、カッコ内は解説した論点です。試験直前は、まずここを声に出して判定し、迷った肢だけ該当の論点に戻ります。', '']
            o += mine
        else:
            o += ['この章には、誤答が3回以上の肢はありません。']
        o += ['', '---', '', '### 次に読む', '']
        if k < 3:
            o.append(f'次は、第{k + 1}章「{CH_TITLES[k + 1][0]}」です。')
        else:
            o.append('全体の串刺しチェック（登記が要るかの整理など）は、全体版 `note-articles/column/sokatsu-01-minpou.md` の「章をまたいで出る論点の串刺しチェック」にあります。')
        text_out = reflow('\n'.join(o))
        path = COL / f'{stem}-ch{k}.md'
        path.write_text(text_out, encoding='utf-8')
        made.append((path.name, len(text_out)))
    return made

def main():
    rep = []
    for f in ['sokatsu-01-minpou.md', 'sokatsu-02-fudousan-touki-hou.md', 'sokatsu-03-chousashi-hou.md']:
        p = COL / f
        before = p.read_text(encoding='utf-8')
        after = reflow(before)
        assert norm(before) == norm(after), f'{f}: 文字が増減した'
        p.write_text(after, encoding='utf-8')
        rep.append((f, before.count('\n'), after.count('\n')))
    print(rep)
    print(split_minpou((COL / 'sokatsu-01-minpou.md').read_text(encoding='utf-8')))

if __name__ == '__main__':
    main()
