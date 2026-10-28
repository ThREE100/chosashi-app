def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '家屋番号の決め方は、', 'どの地番を使う？', '不動産登記事務取扱手続準則　家屋番号'
_cards = [
    dict(h='一筆に二個の建物なら支号を付ける',
         ill='an isometric single land plot labeled 「五番」 with two small houses standing on it. A small tag labeled 「五番の一」 hangs on the left house and a small tag labeled 「五番の二」 hangs on the right house. A green check mark sits beside the houses.',
         words=['五番', '五番の一', '五番の二'], tag='支号で区別する'),
    dict(h='二筆にまたがれば床面積の多い方',
         ill='an isometric house lying across the border between two land plots, the left plot labeled 「五番」 and the right plot labeled 「六番」. The larger part of the house on the right plot is highlighted with a green glow, and a tag labeled 「六番」 hangs on the house. A green check mark sits beside the highlighted part.',
         words=['五番', '六番'], tag='多い部分の地番を使う'),
    dict(h='附属建物があれば主たる建物の敷地',
         ill='an isometric scene with a main house on the left plot labeled 「五番」 and a larger outbuilding on the right plot labeled 「六番」. The main house is highlighted with a green glow and carries a tag labeled 「五番」. A green check mark sits beside the main house.',
         words=['五番', '六番'], tag='主たる建物の地番を使う'),
    dict(h='合併したら上位の家屋番号',
         ill='an isometric scene of two houses on the left, tagged 「七番の一」 and 「七番の二」, joined by an arrow into one larger house on the right tagged 「七番の一」. A green check mark sits beside the larger house.',
         words=['七番の一', '七番の二'], tag='上位の番号を使う'),
    dict(h='先に登記した建物の番号は据え置き',
         ill='an isometric land plot labeled 「八番」 with an older house on the left tagged 「八番」 and a newly built house on the right tagged 「八番の二」. A small padlock icon sits on the older house tag. A green check mark sits beside the older house.',
         words=['八番', '八番の二'], tag='最初の建物は変更不要'),
]

D = dict(
    catch='家屋番号は敷地の地番を手がかりに',
    intro='建物に付ける「家屋番号」を、どのように決めるのかを問う問題です（不動産登記事務取扱手続準則79条）。家屋番号は、基本的に建物が建っている土地の地番をもとに決まります。この問題は、正しいものの組合せを選びます。\n\nこの記事では、建物が2つの土地にまたがる場合や、建物を合併する場合など、迷いやすい場面での決め方を、具体例で確認していきましょう。',
    sections={
        'ア': ('一筆の土地に建物が二個あれば、「五番の一」「五番の二」のように定める',
               '1筆の土地の上に2個以上の建物が存する場合には、敷地の地番と同一の番号に、1、2、3の支号を付けて家屋番号を定めます。たとえば、地番が「5番」であれば、「5番の1」「5番の2」のようにします（不動産登記事務取扱手続準則79条2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、5番の土地に、Aさんの母屋と離れが別々の建物として建っているとします。母屋は「5番の1」、離れは「5番の2」のように、支号で区別します。'),
        'イ': ('二筆にまたがる建物は、床面積の多い部分の地番で定める（若い地番ではない）',
               '2筆以上の土地にまたがって1個の建物が存する場合、附属建物がないときは、床面積の多い部分が存する敷地の地番と同一の番号で家屋番号を定めます（不動産登記事務取扱手続準則79条3号）。\n\n問題文は、床面積の多い部分が6番の土地の上にあるのに、若い地番の「5番」としています。本肢は誤りです。\n\n**たとえば**、Bさんの建物が5番と6番の土地にまたがり、床面積の大半が6番の上にあるなら、家屋番号は「6番」です。地番の若い順で決めるのではありません。'),
        'ウ': ('附属建物があるときは、床面積が少なくても、主たる建物の敷地の地番で定める',
               '2筆以上の土地にまたがって1個の建物が存する場合、附属建物があるときは、主たる建物が存する敷地の地番と同一の番号で家屋番号を定めます（不動産登記事務取扱手続準則79条3号）。附属建物の床面積の大小は関係ありません。\n\n本肢は正しいといえます。\n\n**たとえば**、Cさんの建物の主たる建物（住居）が5番の土地に、それより大きい附属建物（倉庫）が6番の土地にあるとします。倉庫のほうが広くても、家屋番号は主たる建物の敷地の「5番」です。'),
        'エ': ('合併後の家屋番号は、原則として、合併前の家屋番号のうち上位のもの',
               '建物の合併の登記をする場合、合併後の家屋番号は、合併前の建物の家屋番号のうち上位のものとします（不動産登記事務取扱手続準則79条9号）。上位の家屋番号によることが相当でないと認められる場合は、他の番号を用いても差し支えありません。\n\n問題文は「床面積の多い建物の家屋番号」としているので、本肢は誤りです。床面積で決めるのは、二筆以上にまたがる建物の場合です。\n\n**たとえば**、「7番の1」と「7番の2」を合併するときは、床面積の大小にかかわらず、原則として上位の「7番の1」が合併後の家屋番号になります。'),
        'オ': ('最初に登記された建物の家屋番号は、必ずしも変更する必要はない',
               '家屋番号が敷地の地番と同一である建物の敷地上に、他の建物を登記する場合は、その建物の家屋番号を、敷地の地番に2、3の支号を付けた番号とします。この場合、最初に登記された建物の家屋番号は、必ずしも変更することを要しません（不動産登記事務取扱手続準則79条7号）。\n\n問題文は「8番の1に変更しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、「8番」の建物がある敷地に、Dさんが新しい建物を建てた場合、新しい建物は「8番の2」とします。最初の建物は「8番」のままで構いません。'),
    },
    summary=[
        ('ア', '正', '一筆の土地に建物が二個あれば、敷地の地番に支号を付けて「五番の一」「五番の二」のように定める'),
        ('イ', '誤', '二筆にまたがる建物は、床面積の多い部分の地番で定める（若い地番ではない）'),
        ('ウ', '正', '附属建物があるときは、主たる建物の敷地の地番で定める（床面積の大小は関係ない）'),
        ('エ', '誤', '合併後の家屋番号は、原則として上位のもの（床面積の多い方ではない）'),
        ('オ', '誤', '最初に登記された建物の家屋番号は、必ずしも変更する必要はない'),
    ],
    summary_tail='イは「床面積の多い部分」と「若い地番」、エは「上位」と「床面積」、オは「変更を要しない」を入れ替えた出題です。家屋番号は、場面ごとに「何を基準にするか」が違います。',
    supplements=[
        '### 補足説明（イ・ウ）：二筆にまたがる建物は、附属建物の有無で基準が変わる\n\n建物が2筆以上の土地にまたがるとき、何を基準にするかは、附属建物があるかどうかで変わります（79条3号）。\n\n| 場面 | 基準にするもの |\n|---|---|\n| 附属建物がない | 床面積の多い部分が存する敷地の地番 |\n| 附属建物がある | 主たる建物が存する敷地の地番 |\n| 主たる建物自体が2筆以上にまたがる | 主たる建物の床面積の多い部分が存する敷地の地番 |\n\n**たとえば**、5番と6番にまたがる建物で、附属建物がなく、6番の上の床面積が多ければ「6番」です。主たる建物が5番、附属建物が6番にあれば、附属建物のほうが広くても「5番」です。',
        '### 補足説明（エ・オ）：すでに建物がある場合と、合併する場合\n\n家屋番号を新たに定める場面が、すでに家屋番号のある建物に関わるときは、決め方が次のようになります。\n\n- 敷地の地番と同じ家屋番号の建物がある敷地に、他の建物を登記する場合：新しい建物に敷地の地番に2、3の支号を付けた番号を定める。最初の建物の家屋番号は、必ずしも変更しない（79条7号）。\n- 建物を合併する場合：合併前の家屋番号のうち上位のものとする。相当でないときは他の番号も可（79条9号）。\n\n**たとえば**、「9番」の建物がある敷地に新しい建物を建てれば、新しい建物は「9番の2」です。のちに「9番の1」と「9番の2」を合併するなら、原則として「9番の1」が残ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第87日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠は、不動産登記事務取扱手続準則79条2号・3号・7号・9号で、`note-articles/laws/` 配下の準則の原文で確認しました。家屋番号の定めの大枠は、不動産登記規則112条にもあります。',
        'エの「床面積で決めるのは、二筆以上にまたがる建物の場合です」は、準則79条3号の内容を対比のために書いたものです。',
        '補足説明の「主たる建物自体が2筆以上にまたがる」の行は、準則79条3号の後段（主たる建物が2筆以上の土地にまたがる場合）に基づく整理です。',
    ],
    phrases=['一筆に二個なら支号を付けます', '二筆にまたがれば床面積の多い方です', '附属建物があれば主たる建物の敷地です', '合併したら上位の家屋番号です', '最初の建物の番号は変えなくてよい'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='家屋番号の決め方を、「基本の決め方」（グループA：ア・イ・ウ）と「合併と追加の場面」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='家屋番号の決め方を整理', sub='不動産登記事務取扱手続準則 第79条（毎日ドリル 第87日）',
        col_a='基本の決め方', col_b='合併と追加の場面', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '家屋番号の決め方を整理基本の決め方合併と追加の場面', n=24)),
    nb_label='イ・ウ・エ・オ肢', nb_intro='イ・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、二筆にまたがる建物の家屋番号の決め方を、附属建物の有無で分かれる流れで示します。2枚目は、すでに建物がある場合と合併する場合の決め方を表で整理します。',
    notebooks=[
        dict(name='二筆にまたがる建物の家屋番号の決め方', args=dict(
            title='二筆にまたがる建物の家屋番号', sub='附属建物の有無で基準が変わる（毎日ドリル 第87日 イ・ウ）',
            req='a branching flow diagram',
            layout="""--- BRANCHING FLOW ---
Render as a clean flat-design branching flow diagram, top to bottom.
Top box: 二筆以上の土地にまたがる建物
It splits into two branches with different accent colors. The two branch labels are different strings: 「附属建物がない」 (blue) and 「附属建物がある」 (green).
Blue branch ends in a box: 床面積の多い部分が存する敷地の地番. Beside it, a small icon of one house lying across two plots with its larger part highlighted.
Green branch ends in a box: 主たる建物が存する敷地の地番. Beside it, a small icon of a main house on one plot and a larger outbuilding on the next plot, with the main house highlighted.
Use exactly these strings, and no others, for the labels. Do not use check marks or crosses.""",
            callout='附属建物がないときは、床面積の多い部分の敷地の地番です。附属建物があるときは、附属建物が広くても、主たる建物の敷地の地番です。\n「若い地番だから」という理由では決まりません。',
            footer='不動産登記事務取扱手続準則79条3号',
            kanji='・'.join(_k('二筆土地建物附属家屋番号基準床面積多部分敷地地番主若不動産登記事務取扱手続準則')), what='flow diagram',
            check='confirm the two branch labels (附属建物がない and 附属建物がある) are different strings drawn in different accent colors, ')),
        dict(name='すでに建物がある場合と合併する場合', args=dict(
            title='支号の付け方と合併後の番号', sub='家屋番号を定める場面ごとの決め方（毎日ドリル 第87日 エ・オ）',
            req='a three-row table',
            layout="""--- TABLE ---
A table with three rows. Each row has a scene on the left and the rule on the right, connected by a thin arrow. The rule texts are different strings; draw the three rule boxes in three different accent colors (blue, green, orange).
Row 1: scene 「一筆に二個の建物」 (one plot with two houses) → 敷地の地番に支号を付ける（五番の一、五番の二）
Row 2: scene 「家屋番号が地番と同じ建物がある敷地に、新しい建物」 (an older house tagged 「八番」 and a new house tagged 「八番の二」) → 新しい建物に支号を付ける。最初の建物は変更不要
Row 3: scene 「建物の合併」 (two houses tagged 「七番の一」 and 「七番の二」 joined into one) → 合併前の家屋番号のうち上位のもの""",
            callout='すでに「八番」の建物がある敷地に新しい建物を建てても、最初の建物を「八番の一」に変える必要はありません。\n合併では、床面積の多い方ではなく、上位の家屋番号が合併後の番号になります。',
            footer='不動産登記事務取扱手続準則79条2号、7号、9号',
            kanji='・'.join(_k('一筆二個建物敷地地番支号付合併上位家屋番号最初変更不要新不動産登記事務取扱手続準則')), what='table',
            check='confirm the three rule boxes are drawn in three different accent colors and that the strings 八番, 八番の二, 七番の一 and 七番の二 are copied verbatim, ')),
    ],
)
