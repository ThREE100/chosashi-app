"""ひっかけの型の診断（紙版・10問）のnote記事と見出し画像のプロンプトを作る。手で直さず、data.py を直して作り直す。
出力：article.md、header-prompts.md
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BASE))
sys.path.insert(0, HERE)
from data import TYPES, QUESTIONS  # noqa: E402

TITLE = '【土地家屋調査士試験】ひっかけの型がわかる10問チェック～点数より「間違え方」を見る～'
GYAKUBIKI_URL = '【公開後に条文の逆引き図鑑のURLを入れる】'
YJ = {**{f'H{n}': f'平成{n}年度' for n in range(17, 31)}, 'R01': '令和元年度', **{f'R0{n}': f'令和{n}年度' for n in range(2, 9)}}
TAG = re.compile(r'^(?:〔[^〕]*〕|【[^】]*】)+')
LAWJ = {'不動産登記事務取扱手続準則': '準則'}


def load():
    bank = json.load(open(os.path.join(ROOT, 'tools/drill/data/items.json'), encoding='utf-8'))['items']
    shi = {s['id']: s for s in json.load(open(os.path.join(ROOT, 'note-unei/jobun-gyakubiki/data/shi.json'), encoding='utf-8'))}
    by = {}
    for it in bank:
        for s in it['sources']:
            by[(s['q'], s['label'])] = it
    rows = []
    for q, lab, t in QUESTIONS:
        it = by[(q, lab)]
        sid = f'{q}-{lab}'
        sh = shi[sid]
        y, qn = q.split('-')
        rows.append({'q': q, 'label': lab, 'type': t, 'statement': TAG.sub('', it['statement']), 'bank_statement': it['statement'], 'truth': it['truth'],
                     'status': it['status'], 'heading': sh['heading'], 'cites': sh['cites'], 'path': sh['path'],
                     'src': f'{YJ[y]} 第{int(qn[1:])}問 {lab}', 'bank_id': it['id']})
    return rows


def jn(law, art):
    b, _, sub = art.partition('の')
    return f"{LAWJ.get(law, law)}第{b}条" + (f"の{sub}" if sub else '')


def article(rows):
    T = {t['key']: t for t in TYPES}
    L = []
    L.append(f'## {TITLE}\n')
    L.append('択一の点数が伸びないとき、「知識が足りないから」と考えて、テキストを最初から読み直していませんか。\n')
    L.append('でも、間違えた肢を並べてみると、**同じ形のひっかけに何度も引っかかっている**ことがあります。数字を入れ替えられる、主語を入れ替えられる、ないルールを足される……。この「型」がわかると、復習するところがぐっと絞れます。\n')
    L.append('この記事は、過去の本試験の肢から選んだ10問で、**あなたが引っかかりやすい型**を見つけるチェックです。点数ではなく、「どの型で間違えたか」を見てください。\n')
    L.append('### 使い方\n')
    L.append('1. 紙に1〜10の番号を書きます。\n2. 各問を読んで、正しいと思えば「○」、誤りだと思えば「×」を書きます。**自信がないときは「？」**と書いてください（当てずっぽうの○×より、診断が正確になります）。\n3. 時間の目安は5分です。\n4. 書き終えたら、答えと「型の表」で数えます。\n')
    L.append('問題の文は本試験の肢の文です。正誤は今の法令で決めています（出題当時と今で法令が変わったところは、今の法令の答えです）。\n')
    L.append('---\n')
    L.append('### 10問チェック\n')
    for i, r in enumerate(rows, 1):
        L.append(f'**問{i}**（{r["src"]}）  \n{r["statement"]}\n')
    L.append('---\n')
    L.append('ここから下に答えがあります。書き終えてから読んでください。\n')
    L.append('---\n')
    L.append('### 答えと型\n')
    L.append('| 問 | 答え | 型 |\n|---|---|---|')
    for i, r in enumerate(rows, 1):
        L.append(f'| {i} | {"○" if r["truth"] else "×"} | {r["type"]}：{T[r["type"]]["name"]} |')
    L.append('')
    L.append('### 数え方\n')
    L.append('答えと違ったもの、「？」と書いたものに印をつけて、型ごとに数えます。各型は2問ずつです。\n')
    L.append('| 型 | 問 | 印の数 |\n|---|---|---|')
    for t in TYPES:
        qs = '・'.join(str(i) for i, r in enumerate(rows, 1) if r['type'] == t['key'])
        L.append(f'| {t["key"]}：{t["name"]} | 問{qs} | ／2 |')
    L.append('')
    L.append('- **2つとも印**がついた型は、あなたが今いちばん引っかかりやすい型です。下の「直し方」から始めてください。\n- **1つ**の型は、知識はあるのに読み方で落としている可能性があります。\n- **0**の型は、今は大丈夫です。\n')
    L.append('### 型ごとの解説と直し方\n')
    for t in TYPES:
        L.append(f'#### {t["key"]}：{t["name"]}\n')
        L.append(f'{t["what"]}\n')
        for i, r in enumerate(rows, 1):
            if r['type'] != t['key']:
                continue
            c = '、'.join(jn(l, a) for l, a in r['cites'])
            L.append(f'- **問{i}（{"○" if r["truth"] else "×"}）**：{r["heading"]}。（根拠：{c}。解説の全文は「{r["src"]}」の記事）')
        L.append(f'\n**直し方**：{t["fix"]}\n')
    L.append('### 次にやること\n')
    L.append('印のついた型の問題は、根拠の条文に戻るのがいちばんの近道です。条文から「いつ・どの肢で出たか」を引ける**条文の逆引き図鑑**を作りました。上の根拠の条文を引くと、同じ条文で出た別の年度の肢がまとめて見られます。\n')
    L.append(f'条文の逆引き図鑑：{GYAKUBIKI_URL}\n')
    L.append('同じ型の肢を続けて解くと、型が「見える」ようになります。平成17年度から令和8年度までの択一は、全問・全肢を条文で確かめて解説しています。年度別のマガジンから読めます。\n')
    return '\n'.join(L)


def headers():
    common = ('Japanese study-blog header. One young woman MC character only (use the reference sheets "キャラクターシート_MC-01" to "MC-04"); no other characters. '
              'Soft watercolor sky background. She holds a sheet of paper with a small check list and looks thoughtful, then confident. '
              'Text in the image, exactly as written and nothing else: big title 「ひっかけの型がわかる」 / second line 「10問チェック」 / small subtitle 「点数より“間違え方”を見る」. '
              'only digits allowed: 10. No other letters, numbers, logos, URLs or hashtags. Clean, readable Japanese typography, high contrast.')
    return f"""# 見出し画像のプロンプト（ひっかけの型の診断）

`src/build.py` が作る。手で直さない。

## note用（1280×670）

{common} Canvas 1280x670, landscape. Title on the left two thirds, the MC on the right third.

## Instagram用（1080×1440、3:4）

{common} Canvas 1080x1440, portrait 3:4. Margins: 54px left/right, 72px top/bottom. Title in the upper half, the MC in the lower half. Do not add account names, URLs, hashtags or "see note" guidance.
"""


def main():
    rows = load()
    open(os.path.join(BASE, 'article.md'), 'w', encoding='utf-8').write(article(rows))
    open(os.path.join(BASE, 'header-prompts.md'), 'w', encoding='utf-8').write(headers())
    json.dump(rows, open(os.path.join(BASE, 'questions.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('○', sum(r['truth'] for r in rows), '×', sum(not r['truth'] for r in rows))


if __name__ == '__main__':
    main()
