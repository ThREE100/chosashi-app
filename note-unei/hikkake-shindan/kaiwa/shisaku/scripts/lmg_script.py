"""第1回の台本を learning-manga-generator の台本JSONの形にする（APIを使わずに手で流し込むため）。"""
import json, sys
from source import ITEM
SP = {'S': 'the young woman on the LEFT', 'T': 'the round bird teacher on the RIGHT'}
CH = ("Two characters only. THE TEACHER: the plump round bird teacher from the attached sheets (round red glasses, blue shirt, red neckerchief, wings as hands), always on the RIGHT. "
      "THE STUDENT: the young woman from the attached sheets I-01 to I-03, redrawn in the same art style as the bird teacher, always on the LEFT. "
      "Never write any name or role word in the image; the speaker is shown only by position and the bubble tail.")
pages = []
for i, p in enumerate(ITEM['pages'], 1):
    panels = []
    desc = []
    for j, pn in enumerate(p['panels'], 1):
        panels.append(dict(panelNumber=j, size='中ゴマ', composition=pn['mood'],
                           dialogue=[dict(speaker=SP[w], text=t, type='speech') for w, t in pn['talk']],
                           narration=''))
        desc.append(f"Panel {j}: {pn['mood']}. Center diagram: {pn['fig']}. Words allowed in the diagram: {'、'.join(pn['words'])}.")
    prompt = ("Vertical Japanese study-comic page, 1080x1920 (9:16), exactly 3 panels stacked top to bottom. Clean flat pastel illustration. " + CH + " " + " ".join(desc))
    pages.append(dict(pageNumber=i, title=p['caption'], summary=p['lead'], panels=panels, imageGenerationPrompt=prompt))
script = dict(title='ひっかけ診断ノート_01（試作）', unitName='取得時効と登記', struggleSummary=ITEM['key'],
              targetAudience='土地家屋調査士の受験生', testKeywords=['取得時効', '当事者', '第三者', '対抗関係'],
              characterDesign=dict(teacher=dict(name='（名前なし・右の鳥）', appearance='plump round bird, round red glasses, blue shirt, red neckerchief', personality='sharp-tongued but caring'),
                                   student=dict(name='（名前なし・左の女性）', appearance='as in attached sheets I-01..03', personality='earnest, falls into traps')),
              pages=pages, createdAt='2026-11-28T00:00:00Z')
json.dump(script, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
