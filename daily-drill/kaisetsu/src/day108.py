def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='附属建物の取扱いを整理', sub='不動産登記事務取扱手続準則 第5条など（毎日ドリル 第108日）',
    col_a='管轄と記録の書き方', col_b='滅失と主である建物の変更', n_a=3,
    cards=[
        dict(h='附属建物でまたがっても、管轄は元のまま',
             ill='two registry office buildings side by side on a map divided by a dotted border. A main house sits in the left region and a small annex sits across the border in the right region. A thin line connects them and an arrow points to the left registry office. A green check mark sits beside the left registry office.',
             words=[], tag='管轄は変わらない'),
        dict(h='同じ内容でも、略さずに書き分ける',
             ill='a record sheet with two rows of entries, each filled out in full with plain lines. A faded gray ditto mark icon made of two small ticks sits aside, unused. A green check mark sits beside the two rows.',
             words=[], tag='略記はしない'),
        dict(h='同じ一棟なら、一棟の記録を重ねない',
             ill='an isometric apartment building with one header record sheet attached to the whole building, and two small unit icons below it. A thin line from each unit points to the single header sheet. A green check mark sits beside the header sheet.',
             words=[], tag='一棟の記録は一度'),
        dict(h='滅失の登記では、附属建物の原因は空欄',
             ill='a record sheet with a main building row stamped 「滅失」 and an annex building row whose cause cell is highlighted and left blank. A green check mark sits beside the blank cell.',
             words=['滅失'], tag='附属建物は記録なし'),
        dict(h='主が取り壊されたら、附属建物が主になる',
             ill='a demolished main house shown as a pile of rubble on the left and a small annex on the right wearing a crown-shaped badge labeled 「主」. A thin arrow runs from the rubble to the annex. A green check mark sits beside the annex.',
             words=['主'], tag='残った建物が主に'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='附属建物の欄に記録する、しない', sub='不動産登記事務取扱手続準則（毎日ドリル 第108日 イ・エ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a three-row table with two columns. The two column headers 「場面」 and 「附属建物の欄の記録」 are different strings. Draw the 「場面」 column in blue and the 「附属建物の欄の記録」 column in green so that they cannot be confused. This image uses no check marks and no cross marks.

--- TABLE ---
Row 1: 内容が前の附属建物と同じとき | 略さず、そのまま書く
Row 2: 滅失の登記をするとき | 原因の欄は記録なし
Row 3: 表題登記で、新築の日が主と同じとき | 原因の欄は記録なし
Use exactly these strings, and no others.""",
    callout='附属建物の種類と構造と床面積が前の附属建物と同じでも、略して書いてはいけません。\n滅失の登記では、附属建物の原因とその日付の欄に、何も記録しません。',
    footer='不動産登記事務取扱手続準則92条・93条・101条',
    what='table',
    check='confirm the table has exactly three rows and two columns with the exact strings, ')
_N2 = dict(
    title='主である建物が取り壊されたとき', sub='附属建物がある建物（毎日ドリル 第108日 オ）',
    req='a flow diagram',
    layout="""--- FLOW ---
Render as a clean flat-design flow with three steps in a row from left to right, joined by thin arrows, and one extra branch below the last step.
Step 1 (blue accent): a main house and a small annex shown together in one record sheet, with the labels: 甲建物（主） | 乙建物（附属）
Step 2 (orange accent): the main house shown as rubble, with the label: 甲建物を取り壊す
Step 3 (green accent): the annex wearing a crown-shaped badge, with the label: 乙建物を主に変更する登記
Branch below Step 3 (gray accent): a newly built house on the same plot, with the labels: 丙建物を新築 | 別に表題登記
Use exactly these strings, and no others. This image uses no check marks and no cross marks.""",
    callout='取り壊した甲建物と新築した丙建物は、同じ建物ではありません。\n甲建物の記録は、残った乙建物を主である建物に変更する登記をし、丙建物は別に表題登記をします。',
    footer='不動産登記事務取扱手続準則83条・102条',
    what='flow',
    check='confirm there are exactly three steps in a row plus one branch below, with no check marks or cross marks, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='管轄は元の登記所のまま、「同上」は禁止',
    intro='附属建物に関する、不動産登記事務取扱手続準則のきまりを問う問題です（準則5条・89条・92条・101条など）。管轄、記録の書き方、滅失の登記が出題されています。\n\nこの記事では、附属建物がある建物の登記記録を、具体的な場面で確認していきましょう。この問題は、正しい肢の組合せを選ぶ形です。',
    sections={
        'ア': ('附属建物でまたがっても、管轄は元の登記所のまま',
               '甲登記所で登記されている建物について、乙登記所の管轄区域に附属建物が新築され、建物が乙登記所の管轄区域にまたがることとなった場合でも、その建物の管轄登記所は甲登記所です（不動産登記事務取扱手続準則5条）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲登記所の管内にある母屋に、境を越えた乙登記所の管内に離れを新築して附属建物にしたとします。登記を扱う登記所は、そのまま甲登記所です。'),
        'イ': ('附属建物が同じ内容でも、「同上」と略さない',
               '表題部に附属建物を記録するとき、種類、構造、床面積が直前の附属建物と同じでも、「同上」のように略して記録してはいけません（不動産登記事務取扱手続準則92条）。\n\n問題文は「同上」と略記するとしているので、本肢は誤りです。\n\n**たとえば**、符号1の附属建物も符号2の附属建物も、同じ種類・同じ構造・同じ床面積だったとします。それでも、符号2のところは、符号1と同じ内容を略さずに書きます。'),
        'ウ': ('同じ一棟なら、一棟の建物の所在や構造は重ねて書かない',
               '主である建物と附属建物が、同じ一棟の建物に属する区分建物であるときは、附属建物の登記事項を記録するときに、その一棟の建物の所在、地番、構造、床面積を記録する必要はありません（不動産登記事務取扱手続準則89条）。\n\n本肢は正しいといえます。\n\n**たとえば**、同じマンションの中で、101号室を主である建物、同じ階の倉庫部分を附属建物とする場合、マンション全体の所在や構造は、主である建物のところに書かれています。附属建物のところに、もう一度書く必要はありません。'),
        'エ': ('滅失の登記では、附属建物の原因欄に何も記録しない',
               '建物の滅失の登記をするときは、その登記記録に附属建物があっても、附属建物の表示欄の原因及びその日付の欄には、何も記録する必要がありません（不動産登記事務取扱手続準則101条）。\n\n問題文は、附属建物の欄に取壊しの日を記録するとしているので、本肢は誤りです。\n\n**たとえば**、主である建物を5月1日に、附属建物を5月20日に、それぞれ取り壊して、全体の滅失の登記をするとします。この場合も、附属建物のところに「5月20日取壊し」とは記録しません。'),
        'オ': ('取り壊した主である建物を、新築した建物に置き換えることはできない',
               '既存の建物を全部取り壊して建物を建てた場合は、既存の建物が滅失し、新たな建物が建築されたものとして取り扱われます（不動産登記事務取扱手続準則83条）。取り壊した甲建物と、新築した丙建物は、別の建物です。\n\n主である建物が取り壊されて附属建物が残るときは、附属建物を主である建物に変更する、表題部の変更の登記をします（同準則102条）。主である建物の表示を丙建物に変更する登記はできないので、本肢は誤りです。\n\n**たとえば**、母屋を取り壊して、同じ場所に同じ広さの新しい母屋を建てても、新しい母屋は別の建物です。登記記録の母屋の欄を、新しい母屋に書き換えることはできません。'),
    },
    summary=[
        ('ア', '正', '附属建物の新築で他の登記所の管轄区域にまたがっても、管轄登記所は元の登記所のまま'),
        ('イ', '誤', '附属建物が前の附属建物と同じ内容でも、「同上」のように略して記録してはならない'),
        ('ウ', '正', '同じ一棟の区分建物が附属建物なら、一棟の建物の所在や構造などを重ねて記録する必要はない'),
        ('エ', '誤', '滅失の登記では、附属建物の取壊しの日は、附属建物の欄に記録しない'),
        ('オ', '誤', '取り壊した主である建物の表示を、新築した建物の表示に置き換える変更の登記はできない'),
    ],
    summary_tail='イは「略してよいか」、エは「記録するか」、オは「置き換えられるか」を入れ替えた出題です。附属建物の記録は、原則の書き方を一つずつ確かめましょう。',
    supplements=[
        '### 補足説明（イ・エ）：附属建物の欄に、記録するか、しないか\n\n附属建物の記録の書き方には、似た決まりが並んでいます。\n\n- 内容が前の附属建物と同じとき：略さずに、そのまま書く（92条）。\n- 滅失の登記をするとき：附属建物の原因とその日付の欄は、記録しない（101条）。\n- 表題登記で、附属建物の新築の日が主である建物と同じとき：原因とその日付の欄は、記録しない（93条1項）。\n\n**たとえば**、新築の表題登記で、母屋と離れが同じ日に建てられたなら、離れの欄に日付は書きません。しかし、離れの種類と構造と床面積が別の離れと同じであっても、「同上」とは書かず、そのまま書きます。',
        '### 補足説明（オ）：主である建物が取り壊されたときの流れ\n\n主である建物（甲建物）と附属建物（乙建物）が一つの登記記録に載っているとします。\n\n- 甲建物を取り壊す。\n- 甲建物の記録は、乙建物を主である建物に変更する表題部の変更の登記をする（準則102条）。\n- 新築した丙建物は、別に表題登記をする。\n\n**たとえば**、母屋を取り壊して、同じ場所に同じ広さの母屋を新築したときも、新しい母屋は別の建物です。残った離れが新しい主である建物になり、新しい母屋は、これとは別に登記します。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第108日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記事務取扱手続準則5条、83条、89条、92条、93条、101条、102条は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「取り壊した建物と新築した建物は別の建物で、主である建物の表示を置き換える変更の登記はできない」という結論は、準則83条・102条から導く説明です。登記先例の原文は手元になく、未確認です。',
        'ウとアの具体例（マンションの倉庫部分、境を越えた離れ）は、準則89条・5条の文言をかみ砕いた一般的な説明で、個別の運用の確認はしていません。',
    ],
    phrases=['またがっても管轄は元の登記所です', '附属建物は同上と略記しません', '同じ一棟の記録は重ねて書きません', '滅失の登記は附属建物の原因が空欄です', '残った附属建物が主になります'],
    header=dict(t1='附属建物は、', t2='どう記録する？', topic='不動産登記法　附属建物',
                kanji='・'.join(_kj('附属建物はどう記録する', '不動産登記法附属建物', '毎', n=8))),
    poster_intro='附属建物の取扱いを、「管轄と記録の書き方」（グループA：ア・イ・ウ）と「滅失と主である建物の変更」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、附属建物の欄に記録する場合としない場合を表で整理します。2枚目は、主である建物が取り壊されたときの手続の流れを示します。',
    notebooks=[
        dict(name='附属建物の欄に記録する、しない', args=_N1),
        dict(name='主である建物が取り壊されたとき', args=_N2),
    ],
)
