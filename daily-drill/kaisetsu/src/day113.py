def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='区分建物の表題登記を整理', sub='不動産登記法 第47条・第48条（毎日ドリル 第113日）',
    col_a='だれが申請するか', col_b='接続と区分の選び方', n_a=3,
    cards=[
        dict(h='合併した会社も、被承継人名義で申請できる',
             ill='two company buildings merging into one larger company building, with a form labeled 「表題登記」 held by a figure in front of the merged building. A faded gray outline of one old company building stands behind. A green check mark sits beside the form.',
             words=['表題登記'], tag='所有者は消えた会社'),
        dict(h='区分建物を買った人に、申請義務はない',
             ill='an isometric apartment building with one unit handed from a developer figure to a buyer figure. The developer holds a form and a calendar page labeled 「一月以内」, while the buyer figure holds no form. A green check mark sits beside the developer.',
             words=['一月以内'], tag='義務は新築した人'),
        dict(h='他の区分建物の所有者に代わって申請できる',
             ill='two unit owner figures in front of a new apartment building. One owner holds two forms at a counter, one for each unit. A green check mark sits beside the owner with the two forms.',
             words=[], tag='一括申請のため'),
        dict(h='非区分建物に接続したら、その変更と併せる',
             ill='an existing house with a new apartment unit attached to its side, and two forms joined by a paper clip at a counter. One form is labeled 「変更」. A green check mark sits beside the paper clip.',
             words=['変更'], tag='抹消ではなく変更'),
        dict(h='全部が同じ人の物なら、区分しなくてもよい',
             ill='an isometric building with several units and a single owner figure holding one large form that covers the whole building. A green check mark sits beside the owner.',
             words=[], tag='区分建物にするのは任意'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='買った人に申請義務があるか', sub='新築した建物の取得者（毎日ドリル 第113日 イ）',
    req='a side-by-side comparison',
    layout="""IMPORTANT: the two panel headers are different strings and must not be confused: 「区分建物以外」 on the left and 「区分建物」 on the right. Draw them in different accent colors (blue and orange). This image uses no check marks and no cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物以外
Scene: an isometric scene of a developer figure handing a detached house to a buyer figure. The buyer figure holds a form and a calendar page.
Result badge: 買った人も申請義務あり

RIGHT PANEL (orange accent):
Panel header: 区分建物
Scene: an isometric scene of a developer figure handing one unit of an apartment building to a buyer figure. The developer holds the form and the buyer figure holds nothing.
Result badge: 買った人に申請義務なし""",
    callout='表題登記がない建物の所有権を取得した人に申請義務があるのは、区分建物以外の建物です。\n区分建物を買った人には義務がなく、新築した人が引き続き申請します。',
    footer='不動産登記法47条1項',
    what='panels',
    check='confirm the two panel headers are different strings (区分建物以外 on the left and 区分建物 on the right) and that the two result badges are different strings, ')
_N2 = dict(
    title='区分建物が新築されたとき、何と併せる？', sub='区分建物の表題登記の申請（毎日ドリル 第113日 ウ・エ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a two-row table with two columns. The two column headers 「場面」 and 「併せて申請するもの」 are different strings. Draw the 「場面」 column in blue and the 「併せて申請するもの」 column in green so that they cannot be confused. This image uses no check marks and no cross marks.

--- TABLE ---
Row 1: 一棟の建物が新築された | 他の区分建物の表題登記
Row 2: 登記のある建物に接続して区分建物が新築された | その建物の表題部の変更の登記
Use exactly these strings, and no others.""",
    callout='一棟の建物が新築されたときは、他の区分建物の表題登記と併せて申請し、他の区分建物の所有者に代わって申請することもできます。\n登記のある建物に接続して新築したときは、その建物の登記を抹消するのではなく、表題部の変更の登記と併せて申請します。',
    footer='不動産登記法48条',
    what='table',
    check='confirm the table has exactly two rows and two columns with the exact strings, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='区分建物の転得者に申請義務はない',
    intro='区分建物の表題登記について、正しいものを選ぶ問題です（不動産登記法47条・48条、建物の区分所有等に関する法律1条）。だれが、いつ、何と併せて申請するのかが問われています。\n\nこの記事では、申請義務のある人、他人に代わって申請できる場合、既存の建物に接続して新築した場合を、具体的な場面で確認していきましょう。この問題は、正しい肢の組合せを選ぶ形です。',
    sections={
        'ア': ('合併で消滅した会社の区分建物は、承継した会社が申請できる',
               '区分建物を新築した所有者について、相続その他の一般承継があったときは、一般承継人も、被承継人を表題部所有者とする表題登記を申請できます（不動産登記法47条2項）。会社の合併は、その他の一般承継に当たります。\n\n本肢は正しいといえます。\n\n**たとえば**、A社が区分建物を新築した後、表題登記の前にB社に合併されて消滅したとします。B社は、表題部所有者をA社として、表題登記を申請できます。登記されるのは、B社ではなくA社の名前です。'),
        'イ': ('区分建物を買った人に、申請義務はない',
               '表題登記がない建物の所有権を取得した人に申請義務があるのは、新築した建物、又は区分建物以外の建物です（不動産登記法47条1項）。表題登記がない区分建物を、新築した人から買った人は、この義務を負いません。\n\n問題文は、買ったBが申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、A社が新築した区分建物の全部のうち、一戸をBに売ったとします。Bに申請義務はなく、新築したA社が引き続き表題登記を申請します。'),
        'ウ': ('他の区分建物の所有者に代わって申請できる',
               '一棟の建物が新築されたときの区分建物の表題登記は、他の区分建物の表題登記と併せて申請します（不動産登記法48条1項）。そのため、区分建物の所有者は、他の区分建物の所有者に代わって、その区分建物の表題登記を申請できます（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、AとBが、それぞれの専有部分を持つ二戸の建物を新築し、Bが申請に協力しないとします。この場合、Aは、Bに代わって、Bの区分建物の表題登記を申請できます。'),
        'エ': ('既存の建物に接続して区分建物を新築したら、その建物の変更と併せる',
               '表題登記がある建物（区分建物を除く）に接続して区分建物が新築されたときは、その区分建物の表題登記は、既存の建物の表題部の変更の登記と併せて申請します（不動産登記法48条3項）。\n\n問題文は、既存の建物の表題部の登記の抹消と併せて申請するとしています。抹消ではなく変更なので、本肢は誤りです。\n\n**たとえば**、Aの家に、新しい区分建物を接続して建てたとします。Aの家の登記は、なくなるのではなく、区分建物の関係として変更されます。'),
        'オ': ('全部が同じ人の物なら、区分建物にしなくてもよい',
               '区分所有法1条は、構造上区分され、独立して使える数個の部分は、それぞれ所有権の目的とすることができると定めています。「することができる」という書き方なので、区分建物にするかどうかは、所有者が選べます。\n\n一棟の全部を新築した人は、それぞれの部分を区分建物にすることも、一棟の全部を一個の建物として登記することもできます。区分建物にしなければならないとする本肢は、誤りです。\n\n**たとえば**、一人で三戸のアパートを建てた人は、三戸を区分建物として登記しても、アパート全体を一個の建物として登記しても構いません。'),
    },
    summary=[
        ('ア', '正', '区分建物の所有者に一般承継があったときは、一般承継人が、被承継人を表題部所有者とする表題登記を申請できる'),
        ('イ', '誤', '表題登記がない区分建物を買った人には、申請義務がなく、新築した人が引き続き申請する'),
        ('ウ', '正', '一棟の新築では、区分建物の所有者が、他の区分建物の所有者に代わって表題登記を申請できる'),
        ('エ', '誤', '既存の建物に接続して区分建物を新築したときは、その建物の表題部の変更の登記と併せて申請し、抹消はしない'),
        ('オ', '誤', '全部が同じ人の物なら、区分建物とせず、一棟の全部を一個の建物として登記することもできる'),
    ],
    summary_tail='イは「申請義務がある人の範囲」、エは「変更と抹消」、オは「できる」と「しなければならない」を入れ替えた出題です。区分建物は、非区分建物と取扱いが違う点に注意しましょう。',
    supplements=[
        '### 補足説明（イ）：買った人に申請義務があるのは、区分建物以外\n\n表題登記がない建物の所有権を取得した人の申請義務は、建物の種類によって違います（不動産登記法47条1項）。\n\n- 区分建物以外の建物：新築した人から買った人も、取得の日から一月以内に申請しなければならない。\n- 区分建物：買った人に義務はない。新築した人が引き続き申請する。\n\n**たとえば**、新築した一戸建てを買った人は、一月以内に表題登記を申請しなければなりません。一方、新築したマンションの一室を買った人は、自分で申請する義務はありません。',
        '### 補足説明（ウ・エ）：区分建物が新築されたときの申請のしかた\n\n区分建物が新築されたときは、状況によって、併せて申請するものが違います（不動産登記法48条）。\n\n- 一棟の建物が新築された：他の区分建物の表題登記と併せて申請する。他の区分建物の所有者に代わって申請できる。\n- 登記のある建物に接続して区分建物が新築された：その建物の表題部の変更の登記と併せて申請する。\n\n**たとえば**、新築のマンションの一戸の所有者は、同じ棟の他の戸の分も代わって申請できます。一方、既存の家に接続して区分建物を建てたときは、既存の家の変更の登記と一緒に申請します。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第113日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法47条、48条、建物の区分所有等に関する法律1条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「新築した人が引き続き申請する」、オの「一棟の全部を一個の建物として登記することもできる」という説明は、条文の文言からの整理で、登記実務の取扱い（先例）の原文は手元になく、未確認です。',
        'エの「既存の建物の登記は、区分建物の関係として変更される」という説明は、48条3項の文言をかみ砕いた一般的な整理で、個別の記録方法の確認はしていません。',
    ],
    phrases=['合併した会社も被承継人名義で申請できます', '区分建物を買った人に義務はありません', '他の区分建物の所有者に代われます', '非区分建物に接続したら変更と併せます', '区分建物にするかは所有者が選べます'],
    header=dict(t1='区分建物の登記は、', t2='だれが申請？', topic='不動産登記法　区分建物の表題登記',
                kanji='・'.join(_kj('区分建物の登記はだれが申請', '不動産登記法区分建物の表題登記', '毎', n=8))),
    poster_intro='区分建物の表題登記を、「だれが申請するか」（グループA：ア・イ・ウ）と「接続と区分の選び方」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・ウ・エ肢', nb_intro='イ・ウ・エの補足説明に合わせた2枚です。1枚目は、買った人に申請義務があるかどうかを、区分建物とそれ以外で左右の対比にして示します。2枚目は、区分建物が新築されたときに、何と併せて申請するのかを表で整理します。',
    notebooks=[
        dict(name='買った人に申請義務があるか', args=_N1),
        dict(name='区分建物が新築されたとき、何と併せる？', args=_N2),
    ],
)
