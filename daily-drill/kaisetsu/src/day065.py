def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='区分建物の表題登記、', t2='だれが申請する？', topic='不動産登記法　区分建物の表題登記')
_PT = '区分建物の表題登記を整理'
_PS = '不動産登記法 第47条・第48条（毎日ドリル 第65日）'

_cards = [
    dict(h='区分建物の買主に申請義務はない',
         ill='an isometric new apartment building with one unit highlighted. A buyer figure holding a key stands outside a dotted frame labeled 「申請義務」, drawn in faded gray. A seller figure inside the frame holds a form labeled 「表題登記」. No check mark and no cross mark on this card.',
         words=['申請義務', '表題登記'], tag='買主は対象外'),
    dict(h='相続人が被相続人名義で申請できる',
         ill='an isometric apartment unit with a faded outline of an owner figure labeled 「所有者」 standing behind an heir figure. The heir holds a form labeled 「表題登記」. A green check mark sits beside the heir.',
         words=['所有者', '表題登記'], tag='相続人も申請可'),
    dict(h='他の区分建物も併せて、代わって申請',
         ill='an isometric two-story apartment building with two units, each with its own owner figure. One owner holds two forms together, both labeled 「表題登記」, one for each unit. A green check mark sits beside the owner.',
         words=['表題登記'], tag='併せて申請'),
    dict(h='既存の建物の変更登記も併せて申請',
         ill='an existing small house on the left joined by a short passage to a new apartment unit on the right. Two forms are clipped together in the middle, labeled 「表題登記」 and 「変更登記」. A green check mark sits beside the forms.',
         words=['表題登記', '変更登記'], tag='変更登記もセット'),
    dict(h='同じ所有者なら1個の建物にできる',
         ill='a row of four isometric rooms in one building. Two adjacent rooms are joined by a green bracket. An owner figure with a name tag labeled 「所有者」 stands beside the building. A green check mark sits beside the bracket.',
         words=['所有者'], tag='所有者の意思次第'),
]

_nb1_layout = """IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「区分建物以外の建物」 on the left and 「区分建物」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物以外の建物
Scene: an isometric detached house, with a builder figure labeled 「新築した人」 and a buyer figure labeled 「買った人」 standing beside it.
Result badge with a green check mark: 申請義務あり

RIGHT PANEL (gray accent):
Panel header: 区分建物
Scene: an isometric apartment building with one unit highlighted, and a buyer figure labeled 「買った人」 standing beside it.
Result badge with a red cross: 買った人は対象外"""

_nb2_layout = """--- FLOW ---
Render as a clean flat-design diagram in three stacked blocks, connected by small downward arrows with no text.
Block 1 (blue accent), block header: 新築の前. Scene: an isometric existing house with the label 表題登記がある建物.
Block 2 (green accent), block header: 区分建物を新築して接続. Scene: the existing house joined to a new apartment unit with the label 新築した区分建物. Beside the scene, two forms clipped together with the labels 区分建物の表題登記 and 建物の表題部の変更の登記, and a small tag 併せて申請.
Block 3 (orange accent), block header: 新築した区分建物の所有者. Scene: the owner of the new unit holding both forms, with the label 既存の建物の所有者に代わって申請できる.
Use exactly these strings, and no others."""

D = dict(
    catch='区分建物の表題登記は、一括して申請',
    intro='区分建物の表題登記について、「だれが申請するのか」「どのように申請するのか」を問う問題です（不動産登記法47条・48条）。あわせて、数個の部分を1個の建物として扱えるかも問われています（不動産登記事務取扱手続準則78条2項）。\n\nこの記事では、申請義務を負う人の範囲と、区分建物をほかの建物と併せて申請する仕組みを、具体的な場面で確認します。この問題は、誤っているものを選ぶ形式です。',
    sections={
        'ア': ('区分建物の買主には、申請義務がない',
               '新築した建物又は区分建物以外の表題登記がない建物の所有権を取得した者は、その所有権の取得の日から一月以内に、表題登記を申請しなければなりません（不動産登記法47条1項）。\n\nこの申請義務の対象は、建物を新築した人と、区分建物以外の建物を取得した人です。表題登記がない区分建物を買い受けたBは、対象に入っていません。本肢は誤りです。\n\n**たとえば**、新築マンションの1室を、表題登記がされる前に、新築した業者Aから買ったBがいるとします。このとき、Bには47条1項の申請義務はありません。\n\n区分建物の表題登記は、一棟の建物に属するほかの区分建物の表題登記と併せて申請する決まりだからです（同法48条1項）。'),
        'イ': ('相続人は、被相続人を表題部所有者として申請できる',
               '区分建物を新築した場合に、その所有者に相続その他の一般承継があったときは、相続人その他の一般承継人も、被承継人を表題部所有者とする表題登記を申請することができます（不動産登記法47条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、マンションの1室を新築した人が、表題登記をする前に亡くなったとします。この場合、相続人は、亡くなった人を表題部所有者とする表題登記を申請できます。表題部所有者になるのは、相続人ではなく、亡くなった人です。'),
        'ウ': ('同じ一棟の区分建物は、併せて、代わって申請できる',
               '区分建物が属する一棟の建物が新築された場合、その区分建物の表題登記は、同じ一棟の建物に属する他の区分建物の表題登記と併せて申請しなければなりません（不動産登記法48条1項）。\n\nこの場合、区分建物の所有者は、他の区分建物の所有者に代わって、その表題登記を申請することができます（同条2項）。本肢は正しいといえます。\n\n**たとえば**、新築した一棟の建物に101号室と102号室があり、所有者がAとBに分かれているとします。Aは、自分の101号室の表題登記と併せて、Bの102号室の表題登記を、Bに代わって申請できます。'),
        'エ': ('既存の建物の変更登記も、代わって申請できる',
               '表題登記がある建物（区分建物を除く）に接続して区分建物が新築されたときは、その区分建物の表題登記を、既にある建物の表題部の変更の登記と併せて申請しなければなりません（不動産登記法48条3項）。\n\nこの場合、区分建物の所有者は、既にある建物の表題部所有者や所有権の登記名義人に代わって、その変更の登記を申請することができます（同条4項）。問題文は「申請することはできない」としているので、本肢は誤りです。\n\n**たとえば**、Cの一戸建て（表題登記済み）に、Dが区分建物を新築してつなげ、一棟の建物になったとします。Dは、自分の区分建物の表題登記と併せて、Cの建物の表題部の変更の登記を、Cに代わって申請できます。'),
        'オ': ('同じ所有者なら、隣接する部分を1個の建物にできる',
               '一棟の建物に、構造上区分され、独立して住居、店舗、事務所、倉庫などの用途に供することができる数個の部分があるときは、その各部分を、それぞれ1個の建物として取り扱うのが原則です（準則78条2項本文）。\n\nただし、所有者が同一であるときは、その所有者の意思に反しない限り、一棟の全部又は隣接する数個の部分を1個の建物として取り扱います（同項ただし書）。本肢は正しいといえます。\n\n**たとえば**、Aが所有する一棟の建物に、独立した住居として使える部屋が4つ並んでいるとします。Aが、隣り合う2部屋を1個の建物にしたいと考えているなら、その意思に反しない限り、1個の建物として取り扱われます。'),
    },
    summary=[
        ('ア', '誤', '区分建物を買い受けた人は、47条1項の申請義務の対象に入らない'),
        ('イ', '正', '区分建物を新築した人の相続人は、被相続人を表題部所有者として申請できる'),
        ('ウ', '正', '同じ一棟の区分建物は併せて申請し、他の区分建物の所有者に代わって申請できる'),
        ('エ', '誤', '既存の建物に接続して区分建物を新築した人は、既存の建物の変更登記を代わって申請できる'),
        ('オ', '正', '同じ所有者なら、その意思に反しない限り、隣接する数個の部分を1個の建物にできる'),
    ],
    summary_tail='アは、申請義務の対象を区分建物の買主にまで広げた出題です。エは、代わって申請できる場面を否定した出題です。区分建物の表題登記は、「併せて申請」と「代わって申請」がセットだと覚えておきましょう。',
    supplements=[
        '### 補足説明（ア）：建物の表題登記を申請する義務があるのは、だれか\n\n47条1項が申請義務を定めているのは、次の人です。\n\n| 場面 | 47条1項の申請義務 |\n|---|---|\n| 建物を新築した人 | 対象になる |\n| 表題登記がない、区分建物以外の建物の所有権を取得した人 | 対象になる |\n| 表題登記がない区分建物の所有権を取得した人 | 対象に入っていない |\n\n**たとえば**、戸建ての家を新築した人は、新築の日から一月以内に表題登記を申請します。新築の戸建てを、表題登記の前に買った人も同じです。一方、新築マンションの1室を、表題登記の前に買った人は、この条文の対象ではありません。',
        '### 補足説明（エ）：既存の建物に区分建物をつなげて新築したとき\n\n表題登記がある建物に接続して区分建物が新築されたときの流れを、順に整理します（不動産登記法48条3項・4項）。\n\n1. 表題登記がある建物（区分建物ではない）がある。\n2. その建物に接続して、区分建物が新築され、一棟の建物になる。\n3. 区分建物の表題登記を、既存の建物の表題部の変更の登記と併せて申請する（3項）。\n4. 区分建物の所有者は、既存の建物の所有者に代わって、その変更の登記を申請できる（4項）。\n\n**たとえば**、Cの店舗（表題登記済み）に、Dが居室の区分建物を新築してつなげたとします。Dは、居室の表題登記と併せて、店舗の表題部の変更の登記を、Cに代わって申請できます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第65日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法47条1項・2項、48条1項から4項まで、不動産登記事務取扱手続準則78条2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの具体例（新築マンションの買主）は、47条1項が「区分建物以外の」と限定していることからの整理です。区分建物の承継取得者が申請する場合の取扱いは、個別の先例・通達の確認はしていません。',
        '補足説明の表は、47条1項の文言を整理したもので、「対象に入っていない」は条文に区分建物の承継取得者が挙げられていないことを指します。',
    ],
    phrases=['区分建物の買主に義務はありません', '相続人も申請できるんです', '同じ一棟なら併せて代わって申請できます', '既存の建物の変更登記もセットです', '同じ所有者なら一個の建物にできます'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='区分建物の表題登記を、「申請義務と相続」（グループA：ア・イ）と「併せて申請と建物の取扱い」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='申請義務と相続', col_b='併せて申請と建物の取扱い', n_a=2,
        cards=_cards,
        kanji=K(_PT, _PS, '申請義務と相続併せて申請と建物の取扱い', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、表題登記の申請義務の対象かどうかを左右の対比で示します。2枚目は、既存の建物に区分建物をつなげて新築したときの流れを示します。',
    notebooks=[
        dict(name='申請義務の対象になる人、ならない人', args=dict(
            title='表題登記の申請義務があるのは？', sub='建物を取得した人の申請義務（毎日ドリル 第65日 ア）',
            req='a side-by-side comparison',
            layout=_nb1_layout,
            callout='47条1項の申請義務の対象は、建物を新築した人と、区分建物以外の建物を取得した人です。\n表題登記がない区分建物を買った人は、この条文の対象に入っていません。',
            footer='不動産登記法47条1項、48条1項',
            kanji=K('表題登記の申請義務があるのは建物を取得した人区分建物以外新築買った対象不動産登記法'), what='panels',
            check='confirm the two panel headers are different strings (区分建物以外の建物 on the left and 区分建物 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='既存の建物に区分建物をつなげたとき', args=dict(
            title='既存の建物につなげて新築したら', sub='併せて申請と代わって申請（毎日ドリル 第65日 エ）',
            req='a flow diagram',
            layout=_nb2_layout,
            callout='区分建物の表題登記は、既存の建物の表題部の変更の登記と併せて申請します。\n新築した区分建物の所有者は、既存の建物の所有者に代わって、変更の登記を申請できます。',
            footer='不動産登記法48条3項・4項',
            kanji=K('既存の建物につなげて新築したら併せて申請と代わって区分建物表題登記変更所有者'), what='blocks',
            check='confirm there are exactly three blocks connected by downward arrows with no text, ')),
    ],
)
