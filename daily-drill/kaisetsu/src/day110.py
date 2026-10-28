def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='代襲相続と遺産分割を整理', sub='民法 第887条から第909条（毎日ドリル 第110日）',
    col_a='代襲相続', col_b='遺産の分割', n_a=3,
    cards=[
        dict(h='放棄したら、その子は代襲しない',
             ill='a simple family diagram with a parent at the top, a child figure holding a form labeled 「放棄」, and a grandchild figure drawn in faded gray beside the child, not stepping into the heir position. A green check mark sits beside the form.',
             words=['放棄'], tag='初めから相続人でない'),
        dict(h='欠格でも、その子は代襲する',
             ill='a simple family diagram with a parent at the top, a child figure carrying a name tag labeled 「欠格」 stepping aside, and a grandchild figure stepping up into the heir position. A green check mark sits beside the grandchild.',
             words=['欠格'], tag='その子が代わりに'),
        dict(h='兄弟姉妹の場合は、甥と姪まで',
             ill='a simple family diagram with the deceased person at the top, a sibling figure, and a nephew-or-niece figure highlighted inside a frame as the last eligible heir. A further grandchild figure in faded gray stands outside the frame. A green check mark sits beside the framed figure.',
             words=[], tag='再代襲はなし'),
        dict(h='遺言による分割の禁止は、五年まで',
             ill='a calendar page labeled 「五年」 beside a property document secured with a padlock and a will document. A green check mark sits beside the calendar.',
             words=['五年'], tag='五年を超えない期間'),
        dict(h='分割の効力は、開始の時にさかのぼる',
             ill='a horizontal timeline with a left flag labeled 「相続開始」 and a right flag labeled 「分割」. A curved arrow loops back from the right flag to the left flag. A green check mark sits beside the curved arrow.',
             words=['相続開始', '分割'], tag='第三者の権利は害さない'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='代襲の原因になるもの、ならないもの', sub='民法887条2項・939条（毎日ドリル 第110日 ア・イ）',
    req='a side-by-side comparison',
    layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「代襲の原因になる」 on the left and 「代襲の原因にならない」 on the right; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 代襲の原因になる
Scene: an isometric scene with three small icons stacked vertically, each followed by a label: 相続開始以前の死亡 | 欠格 | 廃除
Result badge with a green check mark: その子が代襲する

RIGHT PANEL (orange accent):
Panel header: 代襲の原因にならない
Scene: an isometric scene with one small icon followed by a label: 相続の放棄
Result badge with a red cross: その子は代襲しない""",
    callout='子が相続人になれない理由が、死亡、欠格、廃除のどれかであれば、その子が代襲します。\n相続の放棄は、代襲の原因ではありません。放棄した人は初めから相続人でなかったことになります。',
    footer='民法887条2項・891条・939条',
    what='panels',
    check='confirm the two panel headers are different strings (代襲の原因になる on the left and 代襲の原因にならない on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')
_N2 = dict(
    title='代襲できる範囲は、どこまで？', sub='子と兄弟姉妹の違い（毎日ドリル 第110日 ウ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a four-row table with two columns. The two column headers 「相続人になる人」 and 「代襲できるか」 are different strings. The rows with a green check mark mean the person can inherit by representation; the row with a red cross means the person cannot. Draw the 「相続人になる人」 column in blue and the 「代襲できるか」 column in green.

--- TABLE ---
Row 1: 子の子（孫） | 代襲できる（green check mark）
Row 2: 孫の子（ひ孫） | さらに代襲できる（green check mark）
Row 3: 兄弟姉妹の子（甥と姪） | 代襲できる（green check mark）
Row 4: 甥と姪の子 | 代襲できない（red cross）
Use exactly these strings, and no others.""",
    callout='被相続人の子の場合は、孫、ひ孫と、代襲が続きます。\n兄弟姉妹が相続人になる場合は、その子（甥と姪）までで、その子の子は相続人になりません。',
    footer='民法887条・889条2項',
    what='table',
    check='confirm the table has exactly four rows, that rows 1 to 3 carry green check marks and row 4 carries a red cross, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='放棄は代襲なし、兄弟姉妹は甥姪まで',
    intro='代襲相続と遺産の分割について、誤っているものを選ぶ問題です（民法887条・889条・891条・908条・909条・939条）。だれが、どんな理由で相続できなくなったとき、その子が代わりに相続人になるのかが問われています。\n\nこの記事では、代襲の原因と代襲できる範囲、遺産分割の禁止と効力を、具体的な場面で確認していきましょう。この問題は、誤っている肢の組合せを選ぶ形です。',
    sections={
        'ア': ('相続の放棄では、その子は代襲しない',
               '代襲相続が起こる原因は、被相続人の子が、相続の開始以前に死亡したとき、相続欠格に当たるとき、廃除されたときの三つです（民法887条2項）。相続の放棄は含まれません。\n\n相続の放棄をした人は、初めから相続人にならなかったものとみなされます（同法939条）。放棄した人の子は、代襲しません。本肢は正しいといえます。\n\n**たとえば**、父Aが亡くなり、長男Bが相続を放棄したとします。Bは初めから相続人でなかったことになり、Bの子Cが、Bに代わって相続人になることはありません。'),
        'イ': ('相続欠格でも、その子は代襲する',
               '相続に関する被相続人の遺言書を偽造した人は、相続人となることができません（民法891条5号）。これが相続欠格です。\n\n欠格は代襲の原因の一つなので、その人の子は、代襲して相続人になります（同法887条2項）。問題文は代襲できないとしているので、本肢は誤りです。\n\n**たとえば**、長男Bが父Aの遺言書を偽造して欠格になったとします。Bは相続人になれませんが、Bの子Cは、Bに代わって、Aの相続人になります。'),
        'ウ': ('兄弟姉妹の相続では、その子の子は相続人にならない',
               '被相続人の子も直系尊属もいないとき、兄弟姉妹が相続人になります（民法889条1項2号）。兄弟姉妹の相続では、子の代襲を定める887条2項は準用されますが、さらにその子が代襲する再代襲を定める887条3項は、準用されていません（同法889条2項）。\n\n兄弟姉妹の子（甥と姪）までは相続人になりますが、その子は相続人になりません。本肢は誤りです。\n\n**たとえば**、Aには子も親もなく、兄Bも、Bの子Cも、Aより先に亡くなっていたとします。Cの子Dは、Aの相続人になりません。'),
        'エ': ('遺言で遺産の分割を禁止できるのは、五年を超えない期間',
               '被相続人は、遺言で、相続開始の時から五年を超えない期間を定めて、遺産の分割を禁止できます（民法908条1項）。\n\n五年間の禁止は、この範囲に収まるので、認められます。本肢は正しいといえます。\n\n**たとえば**、Aが遺言で「相続が始まってから五年間は、遺産を分けないでほしい」と定めた場合は、認められます。「十年間は分けない」と定めても、五年を超える部分は認められません。'),
        'オ': ('遺産の分割は、相続開始の時にさかのぼって効力を生ずる',
               '遺産の分割は、相続開始の時にさかのぼって効力を生じます。ただし、第三者の権利を害することはできません（民法909条）。\n\n本肢は正しいといえます。\n\n**たとえば**、父Aが亡くなり、子BとCが話し合って、甲土地はBが取得すると決めたとします。話し合いが成立した日からではなく、父が亡くなった時からBの土地だったものとして扱われます。ただし、第三者がすでに得ていた権利までは、これによって奪えません。'),
    },
    summary=[
        ('ア', '正', '相続を放棄した人の子は代襲しない（放棄は代襲の原因ではない）'),
        ('イ', '誤', '相続欠格は代襲の原因なので、欠格になった人の子は代襲して相続人になる'),
        ('ウ', '誤', '兄弟姉妹の相続では、再代襲は認められず、甥と姪の子は相続人にならない'),
        ('エ', '正', '遺言で、相続開始の時から五年を超えない期間、遺産の分割を禁止できる'),
        ('オ', '正', '遺産の分割は、相続開始の時にさかのぼって効力を生ずるが、第三者の権利を害することはできない'),
    ],
    summary_tail='アとイは「放棄」と「欠格」の取り違え、ウは「代襲できる範囲」を広げた出題です。放棄は代襲しない、欠格は代襲する、兄弟姉妹は甥と姪まで、と整理しましょう。',
    supplements=[
        '### 補足説明（ア・イ）：代襲の原因になるものと、ならないもの\n\n相続人になるはずだった子が相続できなくなった理由によって、その子の子が代襲するかが決まります。\n\n- 相続開始以前の死亡：代襲する。\n- 相続欠格：代襲する。\n- 廃除：代襲する。\n- 相続の放棄：代襲しない。\n\n**たとえば**、長男が遺言書を偽造して欠格になった場合と、相続を放棄した場合を比べます。欠格では、長男の子が代わりに相続人になりますが、放棄では、長男の子は相続人になりません。',
        '### 補足説明（ウ）：代襲できる範囲は、子と兄弟姉妹で違う\n\n被相続人の子が相続人の場合は、孫、ひ孫と代襲が続きます（887条2項・3項）。兄弟姉妹が相続人の場合は、その子（甥と姪）までです（889条2項）。\n\n**たとえば**、Aに子も親もいないとき、Aの兄Bの子（甥のC）は、Bが先に亡くなっていれば相続人になります。しかし、Cも先に亡くなっているなら、Cの子Dは相続人になりません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第110日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法887条、889条、891条、908条、909条、939条は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「第三者がすでに得ていた権利は奪えない」という具体例は、909条ただし書の文言をかみ砕いた一般的な説明で、どのような権利が保護されるかの個別の検討はしていません。',
        'エの「十年間は分けない」と定めた場合の説明は、908条1項の「五年を超えない期間」の文言から導いた一般的な整理です。',
    ],
    phrases=['放棄したら、その子は代襲しません', '欠格なら、その子が代襲します', '兄弟姉妹は甥と姪までです', '遺言による分割の禁止は五年までです', '分割の効力は開始の時にさかのぼります'],
    header=dict(t1='代襲するのは、', t2='どんなとき？', topic='民法　代襲相続と遺産分割',
                kanji='・'.join(_kj('代襲するのはどんなとき', '民法代襲相続と遺産分割', '毎', n=8))),
    poster_intro='代襲相続と遺産分割を、「代襲相続」（グループA：ア・イ・ウ）と「遺産の分割」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='ア・イ・ウ肢', nb_intro='ア・イ・ウの補足説明に合わせた2枚です。1枚目は、代襲の原因になるものとならないものを左右の対比で示します。2枚目は、子の場合と兄弟姉妹の場合で、代襲できる範囲の違いを表で整理します。',
    notebooks=[
        dict(name='代襲の原因になるもの、ならないもの', args=_N1),
        dict(name='代襲できる範囲は、どこまで？', args=_N2),
    ],
)
