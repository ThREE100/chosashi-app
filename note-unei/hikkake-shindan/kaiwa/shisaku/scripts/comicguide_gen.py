"""comic-guide-skill の手順（--prompts-only、--style custom、--lang ja、--aspect 3:4）を、
SKILL.md と references/prompt-template.md の5段構成どおりに第1回の台本へ当てはめる。
台詞と図の語は d01.py のものだけを使い、新しい法律の説明は足さない。"""
import sys
from pathlib import Path
from source import ITEM
out = Path(sys.argv[1]); (out / 'prompts').mkdir(parents=True, exist_ok=True)
STYLE = ("Custom style: clean, warm flat digital illustration for a Japanese study comic, the same style as the attached bird-teacher "
         "character sheets (simple outlines, soft pastel colors, same line weight). Checks/YES in blue, crosses/NO in red, neutral lines dark navy.")
LAYOUT = ("Layout: portrait 3:4 ratio, 4 panels arranged in a 2x2 grid with thin black panel borders and rounded corners, "
          "white gutters between panels, each panel clearly separated. Reading order: top-left, top-right, bottom-left, bottom-right.")
CHARS = ("Characters: THE TEACHER is the plump round bird from the attached sheets (round red glasses, blue shirt, red neckerchief, wings as hands), "
         "always on the RIGHT side of a panel. THE STUDENT is the young woman from the attached sheets I-01 to I-03, redrawn in the bird teacher's art style, "
         "always on the LEFT side. Never write any name or role word in the image; the speaker is shown only by position and bubble tail.")
TEXT = ("All text in Japanese (日本語), reproduced exactly as given, no other words, numbers or letters. Speech bubbles: rounded rectangle with a pointed tail "
        "directed at the speaker. Title text: bold large font in a pale yellow banner. Labels: clean sans-serif, readable.")
QUALITY = ("High quality illustration, professional comic panel layout, consistent character designs across all panels, clean readable text, "
           "educational content, bright well-lit scenes, no watermarks, no artist signatures.")
SIDE = {'S': 'STUDENT (left)', 'T': 'TEACHER (right)'}
sb, pr = ['# storyboard.md（comic-guide の第2段）', ''], []
for i, p in enumerate(ITEM['pages'], 1):
    a, b, c = p['panels']
    panels = [
        ('top-left, title', f"Title banner 「{p['caption']}」. {a['mood']}.", a['talk'][:1], []),
        ('top-right, dialogue', b['mood'] + '.', b['talk'], []),
        ('bottom-left, diagram', f"Cartoon-style diagram: {a['fig']}. Words in the diagram: " + '、'.join(a['words']), a['talk'][1:], a['words']),
        ('bottom-right, summary', f"Summary signboard. {c['mood']}. Diagram: {c['fig']}. Words: " + '、'.join(c['words']), c['talk'], c['words']),
    ]
    sb.append(f"## 第{i}話　{p['caption']}"); 
    body = [STYLE, '', LAYOUT, '', CHARS, '']
    for n, (pos, desc, talk, _) in enumerate(panels, 1):
        sb.append(f"- Panel {n}（{pos}）：{desc}" + ''.join(f" ／{SIDE[w]}「{t}」" for w, t in talk))
        body.append(f"Panel {n} ({pos}):\n{desc}\n" + '\n'.join(f"Speech bubble from the {SIDE[w]}, tail pointing at the speaker: 「{t}」" for w, t in talk))
        body.append('')
    sb.append('')
    body += [TEXT, '', QUALITY]
    (out / 'prompts' / f'0{i}.md').write_text(f"# 第{i}話のプロンプト（ChatGPTに、キャラクターシート6枚を添付して貼る）\n\n```\n" + '\n'.join(body) + "\n```\n")
sb.append('注：comic-guide の分鏡規則（各話 title→dialogue→diagram→summary の4コマ、2x2）に合わせたため、元の台本（1ページ3コマを縦に積む）とは並びが変わる。第1話は台詞の順が元の台本と入れ替わる。')
(out / 'storyboard.md').write_text('\n'.join(sb) + '\n')
(out / 'characters.md').write_text("# characters.md（comic-guide の第3段）\n\n## 先生役（右）\n- 外見：キャラクターシート_トリ先生_01〜03（丸い赤眼鏡・青いシャツ・赤いネッカチーフ・翼を手として使う丸い鳥）\n- 表情：説明では落ち着いた顔、指摘では目を細める、最後はうなずく\n- 吹き出し：白、しっぽは右へ\n\n## 生徒役（左）\n- 外見：キャラクターシート_I-01〜03 の女性を、先生のシートと同じ画風で\n- 表情：自信→驚き→納得\n- 吹き出し：白、しっぽは左へ\n\n画像にもこの表にも、名前は書かない（会話編の決まり）。\n")
print('ok')
