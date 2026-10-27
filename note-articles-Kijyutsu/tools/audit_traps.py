"""会話形式の記事で、藍子の誤答・質問のあと、近くに画像挿入マーカーがない箇所を洗い出す（品質チェック 6-2 の機械化）。

使い方: python3 note-articles-Kijyutsu/tools/audit_traps.py <記事.md> [近さ（段落数。省略は6）]

藍子の発言のうち、次のどれかを含むものを「わなの候補」として拾う（誤答・質問・思い込み）：
  「？」「ですか」「ですよね」「いりま」「要りま」「ですね！」「です！」（断定の誤答に多い）、「あれ」「えっ」
その段落から数えて N 段落以内（話者の行と空行は数えない）に「> 【画像挿入】」があれば図あり、なければ「図なし」と表示する。
「図なし」のすべてが誤りとは限らない（正しい答えを言っただけのセリフなど）ので、人が見て、
トリ先生が「違う」「要らない」と答えているセリフ（藍子の質問への否定）を中心に、図が要るかを判断する。
2026-10-26、R3/Q22 の品質チェックで作った。
"""
import re
import sys

path = sys.argv[1]
near = int(sys.argv[2]) if len(sys.argv) > 2 else 6
text = open(path, encoding='utf-8').read()
paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
KEYS = ['？', 'ですか', 'ですよね', 'いりま', '要りま', 'ですね！', 'です！', 'あれ', 'えっ']
n_no = 0
for i, p in enumerate(paras):
    if not p.startswith('**藍子**'):
        continue
    body = p.split('\n', 1)[-1]
    if not any(k in body for k in KEYS):
        continue
    after = [q for q in paras[i + 1:i + 1 + near] if not q.startswith('**')]
    has = any(q.startswith('> 【画像挿入】') for q in paras[i + 1:i + 1 + near])
    if not has:
        n_no += 1
        print(f'図なし: 段落{i + 1}  {body[:60].strip()}…')
print(f'わなの候補で、あと{near}段落以内に図がないもの：{n_no}件')
