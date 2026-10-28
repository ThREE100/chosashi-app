def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='強迫は善意でも取消し、請求で法定追認',
    intro='意思表示と取消しについて、意思表示の受領能力、第三者による強迫、法定追認、制限行為能力者の相手方の催告、錯誤を問う問題です（民法20条・95条・96条・98条の2・125条）。\n\nこの記事では、似た仕組みの違いを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('成年被後見人に届いた意思表示も、成年後見人が知れば対抗できる',
               '意思表示の相手方が、意思表示を受けた時に成年被後見人であったときは、その意思表示をもって相手方に対抗できません。ただし、相手方の法定代理人がその意思表示を知った後は、この限りではありません（民法98条の2）。\n\n成年後見人のCは、成年被後見人Bの法定代理人です。Cがその意思表示を知った後は、AはBに対抗できるので、本肢は正しいといえます。\n\n**たとえば**、Aさんが契約を解除する通知をBさんに送り、Bさんに届いたとします。届いた時点では、AさんはBさんに対抗できません。\n\nその後、成年後見人のCさんが通知の内容を知ったなら、Aさんは解除をBさんに対抗できます。'),
        'イ': ('第三者の強迫は、相手方が知らなくても取り消せる',
               '詐欺又は強迫による意思表示は、取り消すことができます（民法96条1項）。第三者が詐欺を行った場合は、相手方がその事実を知り、又は知ることができたときに限り、取り消せます（同条2項）。\n\nこの制限は、第三者が強迫を行った場合にはありません。Bが強迫の事実を知らず、知ることができなかったときでも、Aは強迫を理由に取り消せるので、本肢は誤りです。\n\n**たとえば**、Cさんに脅されて、AさんがBさんに土地を売る意思表示をしたとします。BさんがCさんの脅しをまったく知らなかったとしても、Aさんは、強迫を理由に取り消すことができます。'),
        'ウ': ('成年になって取消権を知った後に代金を請求すると、追認したとみなされる',
               '取り消せる行為について、追認をすることができる時以後に、履行の請求などの事実があったときは、追認をしたものとみなされます。ただし、異議をとどめたときは、この限りではありません（民法125条2号）。\n\n追認は、取消しの原因となっていた状況が消滅し、かつ、取消権を有することを知った後にしなければ、効力を生じません（同法124条1項）。\n\nAは、成年に達し、取消権を知った後に、異議をとどめずに代金の支払を請求しています。追認したものとみなされ、取り消せなくなるので（同法122条）、本肢は正しいといえます。\n\n**たとえば**、未成年のときに親の同意なく土地を売ったAさんが、成年になり、取り消せることも知ったうえで、買主に「代金を払ってください」と異議なく請求したなら、あとから取り消すことはできません。'),
        'エ': ('被保佐人への催告で通知がないと、取り消したとみなされる',
               '制限行為能力者の相手方は、被保佐人に対して、一箇月以上の期間を定めて、その期間内に保佐人の追認を得るべき旨を催告できます。被保佐人が、その期間内に追認を得た旨の通知を発しないときは、その行為を取り消したものとみなされます（民法20条4項）。\n\n問題文は、追認したものとみなされるとしているので、本肢は誤りです。なお、不動産の売却は、保佐人の同意が必要な行為です（同法13条1項3号）。\n\n**たとえば**、保佐人の同意なく土地を売った被保佐人のAさんに、買主のBさんが「1か月以内に保佐人の追認を得て、通知してください」と催告します。期間内に通知が来なければ、売買は取り消したものとみなされます。'),
        'オ': ('相手方も重大な過失で知らなかったなら、重過失の錯誤でも取り消せる',
               '錯誤が表意者の重大な過失によるものであった場合は、取り消すことができません。ただし、相手方が表意者に錯誤があることを知り、又は重大な過失によって知らなかったときは、取り消せます（民法95条3項1号）。\n\nBは、Aに錯誤があることを重大な過失によって知らなかったので、この例外に当たります。Aは取り消せるので、本肢は誤りです。\n\n**たとえば**、Aさんが不注意で土地の売値を勘違いして、売る意思表示をしたとします。買主のBさんも、少し注意すれば気づけたのに、重大な不注意で気づかなかったなら、Aさんは、錯誤を理由に取り消せます。'),
    },
    summary=[
        ('ア', '正', '成年被後見人に届いた意思表示は、法定代理人である成年後見人が知った後は対抗できる'),
        ('イ', '誤', '第三者が強迫を行った場合は、相手方が善意無過失でも取り消せる'),
        ('ウ', '正', '成年になり取消権を知った後に異議なく代金を請求すると、法定追認になり取り消せない'),
        ('エ', '誤', '被保佐人に保佐人の追認を得るよう催告して通知がないときは、取り消したものとみなされる'),
        ('オ', '誤', '重大な過失による錯誤でも、相手方が重大な過失で知らなかったときは取り消せる'),
    ],
    summary_tail='イは「詐欺と強迫」、エは「追認と取消し」、オは「例外の見落とし」をすり替えた出題です。似た仕組みは、条文ごとの結論を並べて比べましょう。',
    supplements=[
        '### 補足説明（イ）：第三者が行った詐欺と強迫の違い\n\n第三者が意思表示を取り消せる事情をつくった場合、詐欺と強迫では、取り消せる条件が違います（民法96条）。\n\n- 第三者の詐欺：相手方がその事実を知り、又は知ることができたときに限り、取り消せる（2項）。\n- 第三者の強迫：相手方が知らなくても、取り消せる（1項）。\n\n**たとえば**、第三者のCさんにだまされた場合は、買主のBさんがだまされた事実を知らず、知ることもできなかったなら、取り消せません。一方、Cさんに脅された場合は、Bさんが知らなくても、取り消せます。',
        '### 補足説明（エ）：催告の相手と、答えがないときの結果\n\n制限行為能力者の相手方の催告は、だれに催告するかで、答えがないときの結果が違います（民法20条）。\n\n- 行為能力者となった後の本人に催告し、確答がない：追認したものとみなされる（1項）。\n- 法定代理人、保佐人、補助人に催告し、確答がない：追認したものとみなされる（2項）。\n- 被保佐人に保佐人の追認を得るよう催告し、通知がない：取り消したものとみなされる（4項）。\n\n**たとえば**、同じ「返事がない」でも、保佐人に催告したなら追認、被保佐人に追認を得るよう催告したなら取消し、と結果が逆になります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第103日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法13条1項、20条、95条、96条、98条の2、122条、124条1項、125条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「成年後見人は成年被後見人の法定代理人である」という点は、成年後見人の権限を定める民法の条文の原文は確認しておらず、一般的な整理です。',
        '具体例の人物と場面は、理解のために設けた架空の例です。条文にない事実は断定していません。',
    ],
    phrases=['成年後見人が知れば対抗できます', '第三者の強迫は善意でも取り消せます', '異議なく請求すると追認とみなされます', '被保佐人への催告は取消しになります', '相手方も重過失なら錯誤を取り消せます'],
    header=dict(t1='意思表示の取消し、', t2='決め手は？', topic='民法　意思表示と取消し', kanji=''),
    poster_intro='意思表示と取消しを、「受領能力・強迫・法定追認」（グループA：ア・イ・ウ）と「催告と錯誤」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='意思表示と取消しを整理', sub='民法 第20条と第95条と第96条と第98条の2と第125条（毎日ドリル 第103日）',
        col_a='受領能力と強迫と追認', col_b='催告と錯誤', n_a=3,
        cards=[
            dict(h='成年後見人が知れば対抗できる',
                 ill='a letter handed to a seated person figure, with a guardian figure standing beside reading the same letter. A tag on the guardian is labeled 「成年後見人」. A green check mark sits beside the guardian.',
                 words=['成年後見人'], tag='知った後は対抗できる'),
            dict(h='第三者の強迫は相手方が善意でも取消し',
                 ill='a seller figure signing a contract, with a third figure standing behind him in a stern pointing posture, and a buyer figure unaware on the other side of the table. A round stamp labeled 「取消し」 sits on the contract. A green check mark sits beside the stamp.',
                 words=['取消し'], tag='相手方の善意は不問'),
            dict(h='異議なく代金を請求すると追認になる',
                 ill='an adult figure holding a payment request sheet labeled 「代金」, and a round stamp labeled 「追認」 pressed on the contract beside it. A green check mark sits beside the stamp.',
                 words=['代金', '追認'], tag='法定追認'),
            dict(h='被保佐人への催告は通知がなければ取消し',
                 ill='a buyer figure handing a notice to a seated figure with a helper figure standing behind, a calendar page, and a round stamp labeled 「取消し」. A tag on the helper is labeled 「保佐人」. A green check mark sits beside the stamp.',
                 words=['取消し', '保佐人'], tag='取り消したものとみなす'),
            dict(h='相手方も重過失なら錯誤を取り消せる',
                 ill='a seller figure and a buyer figure both with question-mark thought bubbles that contain no text, and a contract between them with a round stamp labeled 「錯誤」. A green check mark sits beside the stamp.',
                 words=['錯誤'], tag='例外で取り消せる'),
        ],
        kanji=[]),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、第三者が行った詐欺と強迫の違いを、左右の対比で示します。2枚目は、催告の相手と答えがないときの結果を表で整理します。',
    notebooks=[
        dict(name='第三者の詐欺と強迫の違い', args=dict(
            title='第三者が行った詐欺と強迫', sub='相手方が知らなかったとき（毎日ドリル 第103日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a red cross; the right side shows a green check mark. The two panel headers are different strings: 「第三者の詐欺」 on the left and 「第三者の強迫」 on the right; draw them in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 第三者の詐欺
Scene: a seller figure being misled by a third figure, with a buyer figure unaware on the other side of the table.
Label under the scene: 相手方が知らず、知ることもできなかったとき
Result badge with a red cross: 取り消せない

RIGHT PANEL (orange accent):
Panel header: 第三者の強迫
Scene: a seller figure being pressured by a third figure in a stern pointing posture, with a buyer figure unaware on the other side of the table.
Label under the scene: 相手方が知らず、知ることもできなかったとき
Result badge with a green check mark: 取り消せる
Use exactly these strings, and no others, for the labels.""",
            callout='第三者がだました場合は、相手方が知らず、知ることもできなかったなら、取り消せません。\n第三者が脅した場合は、相手方が知らなくても、取り消せます。',
            footer='民法96条1項・2項', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (第三者の詐欺 on the left and 第三者の強迫 on the right) and that the left panel shows a red cross while the right panel shows a green check mark, ')),
        dict(name='催告の相手と、答えがないときの結果', args=dict(
            title='催告して返事がないときの結果', sub='制限行為能力者の相手方（毎日ドリル 第103日 エ）',
            req='a three-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and three data rows under a header row. Use exactly these strings, and no others. Do not use any check mark or cross mark.
Header row: 催告する相手 | 催告の内容 | 返事がないとき
Row 1: 行為能力者となった本人 | 追認するか確答せよ | 追認したものとみなす
Row 2: 法定代理人、保佐人、補助人 | 追認するか確答せよ | 追認したものとみなす
Row 3: 被保佐人 | 保佐人の追認を得よ | 取り消したものとみなす
Draw rows 1 and 2 in a blue accent and row 3 in an orange accent so the different result is clear.""",
            callout='催告の相手によって、返事がないときの結果が違います。\n被保佐人に保佐人の追認を得るよう催告して通知がないときは、取り消したものとみなされます。',
            footer='民法20条1項・2項・4項', kanji=[], what='table',
            check='confirm the table has exactly three columns and three data rows with the given strings, and that row 3 is drawn in a different accent color from rows 1 and 2, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
