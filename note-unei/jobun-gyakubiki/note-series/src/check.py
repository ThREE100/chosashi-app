"""条文の逆引き図鑑 note記事シリーズの機械チェック。使い方：python3 note-unei/jobun-gyakubiki/note-series/src/check.py
NGが1件でもあれば終了コード1。確かめること：
 1. 条文の引用（quotes）が note-articles/laws/ の原文にある
 2. 出題された肢・間違いノートの肢が図鑑にあり、その条文を引いている。○×は一問一答バンクの正誤（令和8年度・正誤なしは使わない）
 3. 本文の「（法令名） 第N条」が laws/ にある
 4. 書かない語（個人の演習結果・作り話の印）が本文と画像の文字にない
 5. 画像のプロンプト：図番・樹形図の「木」がない、「」の文字列に半角英字がない、見出し画像の文字に数字がない
 6. 画像挿入マーカーの数＝プロンプトの数（note用・Instagram用がそろう）、コードフェンスが偶数、本文に表がない、本文の半角括弧
 7. 生成物がデータと一致する（build.py を実行し直して差分がない）
"""
import glob
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402
import build  # noqa: E402

NG_BODY = ['誤答', '正答率', '回間違え', '回まちがえ', '回目で正解', '自己採点', '何度も間違え', '私が間違え', '私も間違え', '【要確認】',
           '演習記録', '演習の記録', '合格するまで更新', '予備校の解答例と照合', 'わからない（？）']
LAWS_RE = re.compile(r'(不動産登記事務取扱手続準則|準則|不動産登記法施行令|不動産登記令|不動産登記規則|不動産登記法|区分所有法|民法|土地家屋調査士法施行規則|土地家屋調査士法)第([0-9]+)条(の[0-9]+)?')
LAWMAP = {'準則': '不動産登記事務取扱手続準則'}


def body_of(text):
    return text.split('## 本文', 1)[-1].split('（本文ここまで）', 1)[0]


def check_module(m):
    ng = []
    d = build.folder(m)
    # 1. 引用
    for j in m.JOBUN:
        if (j['law'], j['art']) not in lib.JOBUN:
            ng.append(f"{j['law']}第{j['art']}条が図鑑にない")
        for q in j['quotes']:
            if not lib.quote_ok(j['law'], j['art'], q):
                ng.append(f"{j['law']}第{j['art']}条の引用が原文と合わない：{q[:30]}…")
        # 2. 肢
        for sid, _ in j['shi']:
            s = lib.SHI.get(sid)
            if s is None:
                ng.append(f"{sid} が図鑑にない")
                continue
            if [j['law'], j['art']] not in s['cites']:
                ng.append(f"{sid} は{j['law']}第{j['art']}条を引いていない")
            try:
                lib.truth(sid)
            except ValueError as e:
                ng.append(str(e))
    for x in m.MISTAKES:
        for sid in x.get('shi', []):
            try:
                lib.truth(sid)
            except (ValueError, KeyError) as e:
                ng.append(f"間違いノート：{e}")
    art = open(os.path.join(d, 'article.md'), encoding='utf-8').read()
    body = body_of(art)
    # 3. 条文
    for mm in LAWS_RE.finditer(body.replace(' ', '')):
        law = LAWMAP.get(mm.group(1), mm.group(1))
        num = mm.group(2) + (mm.group(3) or '')
        if law not in lib.lawtext.LAW_FILES:
            continue
        if lib.lawtext.article(law, lib.jn(num)) is None:
            ng.append(f"本文の{law}第{num}条が laws/ にない")
    # 4. 書かない語
    zk = open(os.path.join(d, 'zukai-prompts.md'), encoding='utf-8').read()
    hd = open(os.path.join(d, 'header-prompts.md'), encoding='utf-8').read()
    for w in NG_BODY:
        if w in body:
            ng.append(f"本文に書かない語「{w}」")
        for s in lib.strings_in(zk + hd):
            if w in s:
                ng.append(f"画像の文字に書かない語「{w}」")
    # 5. 画像のプロンプト
    for s in lib.strings_in(zk):
        if re.search(r'図\s*[0-9０-９]+', s):
            ng.append(f"画像の文字に図番：{s}")
        if re.search(r'[A-Za-z]', s):
            ng.append(f"画像の文字に半角英字：{s}")
    if lib.TREE_NG.search(zk + body):
        ng.append('樹形図の意味の「木」「ツリー」がある')
    for blk in re.findall(r'```\n(.*?)```', hd, re.S):
        for key in ('Line 1 (', 'Line 2 (', 'subtitle band with navy text:\n'):
            pass
        tl = re.findall(r'\):\n(.+)\n|navy text:\n(.+)\n', blk)
        for a, b in tl:
            t = a or b
            if re.search(r'[0-9０-９]', t):
                ng.append(f"見出し画像の文字に数字：{t}")
    # 6. 形
    n_mark = len(re.findall(r'> 📷 \*\*画像挿入', body))
    _, items = build.render_zukai(m)
    if n_mark != len(items):
        ng.append(f"画像挿入マーカー{n_mark}か所とプロンプト{len(items)}本が合わない")
    for name, *_ in items:
        if f"`{name}.png`" not in body:
            ng.append(f"本文に {name}.png のマーカーがない")
    if zk.count('```') % 2 or hd.count('```') % 2:
        ng.append('コードフェンスが奇数')
    if re.search(r'^\|.*\|\s*$', body, re.M):
        ng.append('本文に表（noteで表示できない）')
    plain = re.sub(r'`[^`]*`|https?://\S+', '', body)
    if re.search(r'[()]', plain):
        ng.append('本文に半角括弧（全角にする）')
    return ng


def main():
    mods = build.modules()
    # 7. 生成物の一致
    before = {p: open(p, encoding='utf-8').read() for p in glob.glob(os.path.join(lib.SERIES, '*', '*.md')) + [os.path.join(lib.SERIES, '00-mokuji.md')] if os.path.exists(p)}
    build.main()
    total = 0
    for p, t in before.items():
        if os.path.exists(p) and open(p, encoding='utf-8').read() != t:
            print(f"注意 {os.path.relpath(p, lib.SERIES)} を作り直した（データと食い違っていた）")
    nos = [m.NO for m in mods]
    if nos != list(range(len(mods))):
        print('NG 回の番号が0からの連番になっていない', nos)
        total += 1
    for m in mods:
        ng = check_module(m)
        total += len(ng)
        print(f"== 第{m.NO}回 {m.TITLE}：NG {len(ng)}件")
        for x in ng:
            print('  NG', x)
    print(f"合計 NG {total}件")
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
