"""学習まんが版の定番ページ（扉・確かめクイズ・まとめ）の部品。gNN.py から使う。"""
S, T = 'S', 'T'

def tobira(title, question, s_line, t_line, art='The student sits at a study desk holding a big question card, smiling confidently. The bird teacher peeks in from the right edge with narrowed eyes.'):
    return dict(caption=f'扉：「{s_line[:14]}」', aim='問いを1枚の絵で見せ、生徒が自信満々で罠に向かう姿で興味を引く。',
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

def quiz(qs, t_end='よく言えたわね'):
    """qs: [(問いの文, 答え, 絵, 追加の語のリスト)] を3つ。正解の印（○・はんこ）は付けない（2026-11-28 ユーザー指示。○×は最後のページだけ）。"""
    panels = []
    pos = ['top', 'middle', 'bottom']
    for k, (q, a, art, extra) in enumerate(qs):
        last = k == len(qs) - 1
        p = dict(size=f'equal, {pos[k]}', art=f'Quiz card on the left half: {art} The student answers on the right half.'
                 + (' The teacher gives a small wing thumbs-up at the far right.' if last else ''),
                 chars='student center-right, teacher small at far right' if last else 'student only, right half',
                 talk=[(S, a)] + ([(T, t_end)] if last else []), words=[f'第{k+1}問', q] + extra)
        panels.append(p)
    return dict(caption='確かめクイズ', aim='読んだことを3問で確かめる。正誤の印は付けない。',
                layout='Three panels of equal height stacked vertically, each a quiz card.', panels=panels)

def matome(lines, typ, s_end, t_end):
    """まとめ（最後のページ）。○×はこのページだけに出す。○×は台本に書かず、gakushu.finalize が
    一問一答バンクの truth から付け、この肢の記述（claims.py）と凡例と並べて作る（2026-11-28 ユーザー指示）。
    lines：×の肢なら「正しくは」、○の肢なら「ポイント」として並べる正しい内容。"""
    return dict(kind='matome', lines=lines, typ=typ, s_end=s_end, t_end=t_end)

def jirei(caption, top, mids, bottom_talk, bottom_art='The teacher points at the scene; the student looks closely.'):
    """事例を絵で。top=(art, narration, words)、mids=[(art, narration, words)]（0〜2個）。"""
    lay = 'one wide panel across the top, ' + (f'{len(mids)} medium panels side by side in the middle, ' if mids else '') + 'and one wide strip across the bottom'
    ps = [dict(size='wide, top', art=top[0], narration=top[1], words=top[2])]
    for k, m in enumerate(mids):
        ps.append(dict(size=f"medium, middle {'left' if k == 0 else 'right'}" if len(mids) == 2 else 'medium, middle', art=m[0], narration=m[1], words=m[2]))
    ps.append(dict(size='wide strip, bottom', art=bottom_art, chars='student left, teacher right', talk=bottom_talk))
    return dict(caption=f'事例を絵で：{caption}', aim='長い問題文を、場面の絵に置きかえる。',
                layout=f'{len(ps)} panels: ' + lay + '.', panels=ps)

def zukai(caption, art, words, s_line, t_line):
    return dict(caption=f'図解の大ゴマ：{caption}', aim='1ページ全部を使って、この論点の地図を1枚で見せる。',
        layout='Two panels: one huge diagram panel filling about 80 percent of the page, and one short strip across the bottom.',
        panels=[dict(size='huge, top 80 percent', art='A big clean diagram with a title band across the top. ' + art, words=words),
                dict(size='short strip, bottom', art='Both characters small, pointing up at the diagram.', chars='student left, teacher right, small',
                     talk=[(S, s_line), (T, t_line)])])

def naze(caption, aim, top, talk, bottom):
    """top=(art, words)、bottom=(art, narration, words)。"""
    return dict(caption=caption, aim=aim,
        layout='Three panels: one wide panel on top, one wide panel in the middle, and one wide panel with a narration box at the bottom.',
        panels=[dict(size='wide, top', art=top[0], words=top[1]),
                dict(size='wide, middle', art='The teacher explains with one wing raised; the student listens with a notebook.', chars='student left, teacher right', talk=talk),
                dict(size='wide, bottom', art=bottom[0], narration=bottom[1], words=bottom[2])])

def hikaku(caption, aim, top, mid, s_line, t_line):
    """上下2段の比較。top/mid=(art, words)。"""
    return dict(caption=caption, aim=aim,
        layout='Three panels: a wide panel on top, a wide panel in the middle, and a short strip at the bottom.',
        panels=[dict(size='wide, top', art=top[0], words=top[1]), dict(size='wide, middle', art=mid[0], words=mid[1]),
                dict(size='short strip, bottom', art='The student counts on her fingers; the teacher nods.', chars='student left, teacher right',
                     talk=[(S, s_line), (T, t_line)])])
