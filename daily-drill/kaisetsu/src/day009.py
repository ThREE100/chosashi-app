def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='解体して建て直せば、滅失と新築',
    intro='建物の合併の登記、滅失の登記、共用部分である旨の登記について、「できるか」「どの登記になるか」「だれが申請できるか」を問う問題です（不動産登記法56条から58条まで）。\n\nこの記事では、抵当権があっても合併できる場合、解体移転とえい行移転の違い、共用部分の規約を廃止したときの登記を、具体的な場面で確認していきましょう。この問題は、正しいものを選ぶ問題です。',
    sections={
        'ア': ('担保権の登記の内容が同じなら、抵当権があっても合併できる',
               '所有権の登記以外の権利に関する登記がある建物の合併の登記は、原則としてできません（不動産登記法56条5号）。\n\nただし、担保権の登記で、登記の目的、申請の受付の年月日及び受付番号並びに登記原因及びその日付が同一のものは、例外です（不動産登記規則131条1号）。\n\n本肢は、甲建物と乙建物のB銀行の抵当権が、これらの点でそろっています。合併の登記を申請することができるので、正しいといえます。\n\n**たとえば**、同じ日に同じ契約で、居宅と物置にまとめてB銀行の抵当権がついている場合です。抵当権があるというだけで、あきらめる必要はありません。'),
        'イ': ('建物を解体して別の土地に建てれば、元の建物は滅失したことになる',
               '建物を解体移転した場合は、既存の建物が滅失し、新たな建物が建築されたものとして取り扱います（不動産登記事務取扱手続準則85条1項）。\n\n問題文は、所在に関する変更の登記を申請すれば足りるとしています。解体移転では、元の建物の滅失の登記と、新しい建物の表題登記が必要です。本肢は誤りです。\n\n**たとえば**、古い家を解体し、その材料で別の土地に同じ間取りの家を建て直したとします。見た目が同じでも、元の家は滅失し、別の新築の家ができたものとして扱われます。'),
        'ウ': ('一棟の建物の全部が滅失したときは、所有者の一人から申請できる',
               '建物が滅失したときは、表題部所有者又は所有権の登記名義人は、滅失の日から一月以内に、滅失の登記を申請しなければなりません（不動産登記法57条）。\n\n区分建物が属する一棟の建物の全部が滅失した場合は、区分建物の所有者の一人から申請すれば足りる、という取扱いです。\n\n本肢は正しいといえます。\n\n**たとえば**、三人がそれぞれ部屋を所有するマンションが全焼したとき、三人が揃わなくても、そのうちの一人が滅失の登記を申請できます。'),
        'エ': ('共用部分の規約を廃止したら、表題部の変更ではなく表題登記',
               '共用部分である旨の登記がある建物について、その旨を定めた規約を廃止した場合には、所有者は、規約の廃止の日から一月以内に、その建物の表題登記を申請しなければなりません（不動産登記法58条6項）。\n\n問題文は「建物の表題部の変更の登記」としているので、本肢は誤りです。\n\n**たとえば**、集会室として共用部分にしていた部屋を、規約を廃止して一つの区分建物に戻すとします。このときは、表題部の変更ではなく、改めて表題登記をします。'),
        'オ': ('共用部分である旨の登記は、所有者と名義人しか申請できない',
               '共用部分である旨の登記は、その建物の表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法58条2項）。\n\n問題文は、区分所有者の管理者であるBも申請できるとしています。本肢は誤りです。\n\n**たとえば**、専有部分を集会室とする規約を作った場合でも、その部屋の所有権の登記名義人であるAが申請するのであり、管理者であるBが代わりに申請することはできません。'),
    },
    summary=[
        ('ア', '正', '担保権の登記の内容がそろっているときは、抵当権の登記があっても建物の合併の登記を申請できる'),
        ('イ', '誤', '建物を解体して別の土地に建てるときは、元の建物の滅失と新しい建物の表題登記になる'),
        ('ウ', '正', '一棟の建物の全部が滅失したときは、区分建物の所有者の一人から滅失の登記を申請できる'),
        ('エ', '誤', '共用部分の規約を廃止したときは、表題部の変更ではなく、表題登記を申請する'),
        ('オ', '誤', '共用部分である旨の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できない'),
    ],
    summary_tail='アは「抵当権があるから合併できない」と即断させる出題、イは解体移転を所在の変更と取り違える出題です。エは登記の種類、オは申請人の範囲を入れ替えています。この問題は正しいものを選ぶ形なので、正解はアとウの組合せになります。',
    supplements=[
        '### 補足説明（イ）：解体移転とえい行移転は、扱いが違う\n\n建物を別の場所に移すといっても、移し方によって登記が変わります。\n\n| 移し方 | 扱い | 必要な登記 |\n|---|---|---|\n| 解体して別の土地に建て直す（解体移転） | 元の建物は滅失し、新しい建物が建築された | 滅失の登記と、新しい建物の表題登記 |\n| 解体せずに引いて動かす（えい行移転） | 建物の所在が変わった | 所在の変更の登記 |\n\n**たとえば**、小さな家を土台ごと引いて隣の敷地に動かしたときは、同じ建物のままなので所在の変更で足ります。解体して建て直したときは、別の建物になります。',
        '### 補足説明（エ・オ）：共用部分である旨の登記と、その廃止\n\n規約で専有部分を共用部分にすると、登記の流れは次のようになります。\n\n- 共用部分である旨の登記：表題部所有者又は所有権の登記名義人だけが申請する（58条2項）。\n- 登記をするとき：登記官が職権で、表題部所有者の登記や権利に関する登記を抹消する（58条4項）。\n- 規約を廃止したとき：所有者が一月以内に、その建物の表題登記を申請する（58条6項）。\n\n**たとえば**、集会室にしていた部屋の登記記録は、共用部分になったときに権利が抹消されています。規約を廃止して元の専有部分に戻すときは、一から表題登記をするイメージです。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第9日（朝）　択一」とし、note の引用の出典欄は空欄にします。この問題は「正しいものの組合せ」を選ぶ形です。',
        '各肢の根拠のうち、不動産登記法56条、57条、58条2項・4項・6項、不動産登記規則131条1号、不動産登記事務取扱手続準則85条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの「区分建物が属する一棟の建物の全部が滅失したときは、区分建物の所有者の一人から申請すれば足りる」は、不動産登記法57条に明記された規定ではなく、先例の取扱いに基づく内容です。先例の原文は手元にないため、番号は書かず、原文は未確認です。',
        'アの具体例（同じ日に同じ契約でまとめて抵当権がついた場面）は、規則131条1号の要件をかみ砕いた一般的な例です。エ・オ・補足説明の具体例も、条文からの一般的な整理です。',
    ],
    phrases=['抵当権があっても合併できる場合があります', '解体して建てれば別の建物です', '一棟の滅失は一人から申請できます', '規約を廃止したら表題登記なんです', '共用部分の登記は名義人だけの申請です'],
    header=dict(t1='建物を動かしたら、', t2='どの登記？', topic='不動産登記法　建物の合併と滅失',
                kanji='建・物・合・併・滅・失・毎'),
    poster_intro='建物の合併・滅失・共用部分の登記を、「合併と滅失」（グループA：ア・イ・ウ）と「共用部分である旨の登記」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の合併・滅失・共用部分を整理', sub='不動産登記法 第56条から第58条まで（毎日ドリル 第9日）',
        col_a='合併と滅失', col_b='共用部分', n_a=3,
        cards=[
            dict(h='担保権の内容が同じなら、合併できる',
                 ill='two small isometric buildings, a house and a shed, each with an identical lock-shaped stamp on the roof, connected by a thin arrow into one combined building. A green check mark sits beside the combined building.',
                 words=[], tag='内容がそろえば合併可'),
            dict(h='解体して建て直せば、滅失と新築',
                 ill='an isometric scene: on the left a demolished old house shown as a pile of materials, an arrow in the middle, and a new house on a different land plot on the right. A stamp labeled 「滅失」 sits beside the pile and a form labeled 「表題登記」 sits beside the new house. A green check mark sits beside the arrow.',
                 words=['滅失', '表題登記'], tag='滅失と表題登記'),
            dict(h='一棟の全部が滅失したら一人から申請',
                 ill='an isometric apartment building burnt down on the left, and three owner figures on the right, only one of them stepping forward with a form labeled 「滅失」. A green check mark sits beside the stepping figure.',
                 words=['滅失'], tag='所有者の一人から'),
            dict(h='規約を廃止したら、表題登記を申請',
                 ill='an isometric meeting room with a sign reading 「共用部分」 on the left, a thin arrow, and the same room as an ordinary unit on the right with a form labeled 「表題登記」. A green check mark sits beside the form.',
                 words=['共用部分', '表題登記'], tag='表題部の変更ではない'),
            dict(h='共用部分である旨の登記は名義人だけ',
                 ill='an isometric meeting room with an owner figure carrying a name tag 「名義人」 holding a form, highlighted with a green glow. A faded gray manager figure stands aside with no form. A green check mark sits beside the owner.',
                 words=['名義人'], tag='申請人は限定'),
        ],
        kanji=kj('合併滅失表題登記共用部分規約廃止名義人担保権')),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、建物の移し方による登記の違いを左右の対比で示します。2枚目は、共用部分である旨の登記の流れを示します。',
    notebooks=[
        dict(name='解体移転とえい行移転', args=dict(
            title='建物を移したら、どの登記？', sub='解体移転とえい行移転（毎日ドリル 第9日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「解体移転」 on the left and 「えい行移転」 on the right. Draw them large and in different accent colors (orange on the left, blue on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 解体移転
Scene: an isometric scene of an old house turned into a pile of materials on one land plot, and a new house standing on another land plot.
Text rows:
扱い: 元の建物は滅失、新たな建物が建築された
登記: 滅失の登記と表題登記

RIGHT PANEL (blue accent):
Panel header: えい行移転
Scene: an isometric scene of a house on rollers sliding from one land plot to the next.
Text rows:
扱い: 建物の所在の変更
登記: 所在の変更の登記""",
            callout='建物を解体して別の土地に建て直すと、元の建物は滅失し、新しい建物ができたものとして扱います。\n解体せずに引いて動かすえい行移転は、建物の所在の変更です。',
            footer='不動産登記事務取扱手続準則85条',
            kanji=kj('解体移転引行建物滅失表題登記所在変更'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='共用部分である旨の登記の流れ', args=dict(
            title='共用部分の登記と、その廃止', sub='不動産登記法58条（毎日ドリル 第9日 エ・オ）',
            req='a step-by-step flow diagram',
            layout="""--- FLOW ---
A clean flat-design vertical flow with three steps connected by downward arrows.

Step 1 (blue box): 共用部分である旨の登記
Icon: an owner figure with a name tag 所有者 holding a form.
Side text: 表題部所有者又は所有権の登記名義人だけが申請

Step 2 (blue box): 職権で、表題部所有者の登記や権利に関する登記を抹消
Icon: a registry officer figure erasing a record line.

Step 3 (green box): 規約を廃止したら、一月以内に表題登記
Icon: an isometric meeting room turning back into an ordinary unit, with a calendar page.""",
            callout='共用部分である旨の登記は、表題部所有者又は所有権の登記名義人だけが申請できます。\n規約を廃止したときは、表題部の変更ではなく、所有者が一月以内に表題登記を申請します。',
            footer='不動産登記法58条2項・4項・6項',
            kanji=kj('共用部分登記所有者申請職権抹消規約廃止表題'), what='flow',
            check='confirm the three steps are connected by downward arrows and that the third step reads 規約を廃止したら、一月以内に表題登記, ')),
    ],
)
