"""定番のページ（扉・つまずき・図解の大ゴマ・確かめクイズ・まとめ）。ひっかけ診断ノートの kata.py と同じ形に、
○×を付けないまとめ（一枚まとめ・記述式の答え）と、図の枠を持てる大ゴマを足した。"""
S, T = 'S', 'T'


def tobira(title, question, s_line, t_line,
           art='The student sits at a study desk holding a big question card, smiling confidently. The bird teacher peeks in from the right edge with narrowed eyes.'):
    return dict(caption='扉：' + title, aim='問いを1枚の絵で見せ、生徒が自信満々で罠に向かう姿で興味を引く。',
        layout='Two panels: one very large title panel filling the top three quarters of the page, and one wide short strip panel across the bottom.',
        panels=[dict(size='very large, top three quarters',
                     art='Title page. ' + art + ' Large title lettering at the top in dark navy with the key word on a yellow highlighter band; the question is written on the card.',
                     chars='student at center-left (large), teacher peeking from the right edge', words=[title, question]),
                dict(size='wide short strip across the bottom', art='The student gives a confident thumbs-up; the teacher crosses his wings, unimpressed.',
                     chars='student left, teacher right', talk=[(S, s_line), (T, t_line)])])


def tsumazuki(s_line, t_stop, t_ask, s_reply, card_words, card_art, caption):
    return dict(caption=f'つまずき：{caption}', aim='生徒が誤答し、先生が止める。読者も一緒に立ち止まる。',
        layout='Three panels: two small panels side by side on top, and one very large panel filling the bottom two thirds.',
        panels=[dict(size='small, top left', art='The student points at the question card confidently.', chars='student only', talk=[(S, s_line)]),
                dict(size='small, top right', art='The bird teacher flaps both wings in a dramatic STOP gesture, with speed lines.', chars='teacher only', talk=[(T, t_stop)]),
                dict(size='very large, bottom two thirds', art='The teacher holds up a giant card toward the reader; the student, on the left, sweats and leans back in surprise. ' + card_art,
                     chars='student left, teacher right, both medium size', talk=[(T, t_ask), (S, s_reply)], words=card_words)])


def zukai(caption, aim, art, words, talk, fig=None):
    """図解の大ゴマ。fig を渡すと、Claudeが作った図を大ゴマにそのまま置く（rect は上80％の中）。"""
    big = dict(size='huge, top 80 percent', art=art, words=words)
    if fig:
        big['fig'] = fig
    return dict(caption=f'図解：{caption}', aim=aim,
                layout='Two panels: one huge diagram panel filling about 80 percent of the page, and one short strip across the bottom.',
                panels=[big, dict(size='short strip, bottom', art='Both characters small, pointing up at the diagram.',
                                  chars='student left, teacher right, small', talk=talk)])


def quiz(qs, t_end='全部正解よ'):
    """qs: [(問いの文, 答え, 絵, 追加の語のリスト)] を3つ。"""
    panels = []
    pos = ['top', 'middle', 'bottom']
    for k, (q, a, art, extra) in enumerate(qs):
        last = k == len(qs) - 1
        panels.append(dict(size=f'equal, {pos[k]}', art=f'Quiz card on the left half: {art} The student answers on the right half; a blue circle stamp appears.'
                           + (' The teacher gives a small wing thumbs-up at the far right.' if last else ''),
                           chars='student center-right, teacher small at far right' if last else 'student only, right half',
                           talk=[(S, a)] + ([(T, t_end)] if last else []), words=[f'第{k+1}問', q] + extra))
    return dict(caption='確かめクイズ', aim='読んだことを3問で確かめる。正解の印は青。',
                layout='Three panels of equal height stacked vertically, each a quiz card.', panels=panels)


def matome(head, lines, s_end, t_end, mark=None, tag=None):
    """まとめの板。mark='○'/'×' なら赤・青のはんこ、None なら見出しだけ（一枚まとめ・記述式の答え）。tag は板の下のラベル。"""
    if mark:
        top = f'At the top a big {"red" if mark == "×" else "blue"} stamp-like mark beside the words {head}.'
    else:
        top = f'At the top the heading {head} on a yellow highlighter band.'
    words = [head] + lines + ([tag] if tag else [])
    return dict(caption=f'まとめ：{head}', aim='結論・覚え方を1ページにまとめ、生徒が自分の言葉で言い直す。',
        layout='Two panels: one large panel filling the top two thirds, and one wide panel at the bottom.',
        panels=[dict(size='large, top two thirds',
                     art=f'A large summary board. {top} Below, a checklist with blue check marks, one line each.'
                         + (' At the bottom of the board, a rounded label.' if tag else ''), words=words),
                dict(size='wide, bottom', art='The student, relieved and determined, holds her pencil up; the teacher smiles warmly with wings on hips.',
                     chars='student left, teacher right', talk=[(S, s_end), (T, t_end)])])
