D = dict(
    catch='合体の登記は、所有権の有無で分かれる',
    intro='二つの建物が合体して一個の建物になったときの登記（合体による登記等）を問う問題です（不動産登記法49条・50条）。合体後の建物の表題登記と、合体前の建物の表題部の登記の抹消を、あわせて申請します。\n\nこの記事では、合体前の建物に「所有権の登記があるかどうか」で、申請のしかたや登記の記録のされ方がどう変わるかを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('所有権の登記がある建物があれば、表題部所有者は記録されない',
               '合体後の建物の表題登記をする場合に、合体前の建物に所有権の登記がある建物があるときは、合体後の建物の登記記録の表題部に表題部所有者に関する登記事項を記録することを要しません（不動産登記規則120条1項）。この場合は、甲区に「合体による所有権の登記をする旨」などが記録されます（同条2項）。\n\n問題文は「表題部所有者としてAの氏名及び住所が記録される」としていますが、甲建物に所有権の登記があるので、表題部には記録されません。本肢は誤りです。\n\n**たとえば**、Aの名義で所有権の登記がある母屋と、表題登記だけがされている離れがつながって、一つの建物になったとします。新しい建物の表題部には所有者の欄を設けず、Aの所有権は権利部の甲区に記録されます。乙建物が表題登記だけだからといって、表題部所有者が記録されるわけではありません。'),
        'イ': ('登記のない建物の所有者を名義人とする所有権の登記も、あわせて申請する',
               '合体前の建物が、表題登記がない建物と所有権の登記がある建物だけであるときは、表題登記がない建物の所有者か、所有権の登記がある建物の所有権の登記名義人が、合体の日から一月以内に合体による登記等を申請します（不動産登記法49条1項2号）。\n\nこのとき、表題登記がない建物の所有者を合体後の建物の登記名義人とする所有権の登記も、あわせて申請しなければなりません（同項後段）。本肢は正しいといえます。\n\n**たとえば**、Aの名義で登記された建物に、Bが建てた未登記の建物がつながって、一個の建物になったとします。Bが申請するときは、合体による登記等と一緒に、Bを登記名義人とする所有権の登記も申請します。'),
        'ウ': ('抵当権が消えた旨は付記登記でする。登記記録への移記はしない',
               '登記官は、抵当権者が「合体後の建物では抵当権を消滅させてよい」と承諾したことを証する情報が提供されたときは、抵当権が消滅した旨を登記します（不動産登記法50条）。\n\nこの登記は、付記登記によってします。消滅した権利の登記は、合体後の建物の登記記録に移記しなくてかまいません（不動産登記規則120条6項）。\n\n問題文は「主登記によってされ、その抵当権の登記は合体後の建物の登記記録に移記される」としているので、本肢は誤りです。\n\n**たとえば**、甲建物に銀行の抵当権が付いていて、銀行が合体後の建物では権利を消してよいと承諾したとします。このとき、抵当権が消えた旨は、もとの抵当権の登記に付記する形で記録します。新しい建物の登記記録に、抵当権の登記を写して引き継ぐことはしません。'),
        'エ': ('合体のあとに名義人となった者は、自分の登記の日から数える',
               '合体のあとに、合体前の所有権の登記がある建物の所有権の登記名義人となった者は、その者に係る所有権の登記があった日から一月以内に、合体による登記等を申請しなければなりません（不動産登記法49条4項）。\n\n問題文は「合体の日から一月以内」としていますが、合体のあとに名義人となった者の一月は、合体の日ではなく、自分に係る登記があった日から数えます。本肢は誤りです。\n\n**たとえば**、3月1日に二つの建物が合体し、4月10日にBが所有権の移転の登記を受けたとします。Bの一月は、3月1日からではなく、登記を受けた4月10日から数え始めます。'),
        'オ': ('申請情報には、所有権の登記がある建物の登記の内容を書く',
               '合体による登記等を申請するときは、合体前の建物に所有権の登記がある建物があれば、その建物の家屋番号、所有権の登記の申請の受付の年月日及び受付番号、順位事項、登記名義人の氏名又は名称を、申請情報の内容とします（不動産登記令別表の十三の項申請情報欄ロ）。本肢は正しいといえます。\n\n**たとえば**、登記がされた甲建物と未登記の乙建物が合体した場合、申請書には、甲建物の登記記録に載っている家屋番号や所有権の登記の受付の番号、登記名義人の氏名などを書き添えます。合体する前の建物のうち、登記のある建物を特定して示すイメージです。'),
    },
    summary=[
        ('ア', '誤', '合体前に所有権の登記がある建物があるときは、合体後の表題部に表題部所有者は記録されない'),
        ('イ', '正', '登記のない建物の所有者を名義人とする所有権の登記も、あわせて申請する'),
        ('ウ', '誤', '抵当権が消滅した旨は主登記ではなく付記登記でし、合体後の建物には移記しない'),
        ('エ', '誤', '合体のあとに名義人となった者の一月は、合体の日ではなく自分に係る登記があった日から数える'),
        ('オ', '正', '申請情報に、所有権の登記がある建物の家屋番号や順位事項などを書く'),
    ],
    summary_tail='アは「表題部所有者」の記録の有無、ウは「主登記と付記登記」「移記」、エは「一月の数え始め」を入れ替えた出題です。合体の登記は、まず合体前の建物に所有権の登記があるかどうかを確かめましょう。',
    supplements=[
        '### 補足説明（ウ）：抵当権を消すとき、残すとき\n\n合体前の建物に抵当権の登記があるとき、合体後の登記記録での扱いは、次の二つに分かれます。\n\n| 場面 | 登記のしかた |\n|---|---|\n| 抵当権者が、合体後の建物で権利を消滅させることを承諾した | 権利が消滅した旨を付記登記でする。合体後の建物の登記記録には移記しない（不動産登記法50条、不動産登記規則120条5項・6項） |\n| 合体後の建物の持分について、同じ内容の登記（存続登記）を残す | 合体前の建物の登記記録から、合体後の建物の登記記録に移記する（同規則120条4項、不動産登記令別表の十三の項申請情報欄ハ） |\n\n**たとえば**、銀行の抵当権が付いた甲建物が合体したとします。銀行が消滅を承諾すれば、抵当権は消え、その旨が付記登記で記録されます。持分について抵当権を残す場合は、抵当権の登記が新しい建物の登記記録に引き継がれます。',
        '### 補足説明（エ）：一月の数え始めは、人によって違う\n\n合体による登記等の申請は、だれが申請するかによって、一月の数え始めが変わります。\n\n- 合体のときに所有者や名義人だった者：合体の日から一月以内（不動産登記法49条1項）。\n- 合体のあとに名義人となった者：自分に係る登記があった日から一月以内（同条4項）。\n\n**たとえば**、3月1日に建物が合体し、4月10日に買主が所有権の移転の登記を受けたとします。合体のときの名義人は3月1日から一月以内、買主は4月10日から一月以内です。買う前に起きた合体でも、買主は自分の登記の日から数え始めます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第35日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法49条・50条、不動産登記令別表の十三の項、不動産登記規則120条は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（母屋と離れ、銀行の抵当権、3月1日と4月10日の例）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        '補足説明（ウ）の表の「存続登記」は、令別表の十三の項申請情報欄ハの定義と、規則120条4項の移記の規定をもとに、消滅の場合と対比して整理したものです。',
    ],
    phrases=['所有権の登記があれば表題部は不要です', '未登記の建物の所有者も名義人にします', '抵当権が消えた旨は付記登記です', '後から名義人なら自分の登記の日から', '申請情報に登記済みの建物を書きます'],
    header=dict(t1='合体のあとの登記、', t2='どう変わる？', topic='不動産登記法　建物の合体',
                kanji='合・体・登・記・変・建・物'),
    poster_intro='合体による登記等を、「合体後の建物の登記」（グループA：ア・イ・ウ）と「申請の期間と申請情報」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の合体の登記を整理', sub='不動産登記法 第49条・第50条（毎日ドリル 第35日）',
        col_a='合体後の建物の登記', col_b='申請の期間と申請情報', n_a=3,
        cards=[
            dict(h='所有権の登記があれば表題部所有者は不要',
                 ill='an isometric scene of two house models merging into one house model. Beside it, a record sheet divided into an upper section labeled 「表題部」 with an empty owner line, and a lower section labeled 「甲区」 with an owner name line drawn as a gray bar. A green check mark sits beside the lower section.',
                 words=['表題部', '甲区'], tag='所有者は甲区に記録'),
            dict(h='未登記の建物の所有者も名義人にする',
                 ill='an isometric scene of a registered house model on the left and an unregistered house model on the right being joined into one house model. Two forms are held together by a paper clip: one labeled 「合体」 and one labeled 「所有権」. A green check mark sits beside the forms.',
                 words=['合体', '所有権'], tag='所有権の登記も同時に'),
            dict(h='抵当権の消滅は付記登記で記録',
                 ill='a bank figure nodding beside a record sheet. On the record sheet, a main entry line has a small indented sub-line below it marked with a round stamp labeled 「付記」. To the right, a new house model with an empty record sheet beside it. A green check mark sits beside the stamp.',
                 words=['付記'], tag='移記はしない'),
            dict(h='後から名義人なら自分の登記の日から',
                 ill='a horizontal timeline. On the left a flag labeled 「合体」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['合体', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
            dict(h='申請情報に登記済みの建物の内容を書く',
                 ill='an application form with several empty lines on the left. An arrow points from a record sheet on the right, labeled 「家屋番号」 on its top line and 「順位事項」 on its second line, to the form. A green check mark sits beside the form.',
                 words=['家屋番号', '順位事項'], tag='家屋番号などを書く'),
        ],
        kanji='合・体・表・題・部・所・有・権・登・記・甲・区・付・移・自・分・月・以・内・家・屋・番・号・順・位・事・項・抵・当・消・滅'.split('・')),
    nb_label='ウ・エ肢', nb_intro='ウ・エの補足説明に合わせた2枚です。1枚目は、抵当権を消すときと残すときの登記のしかたを左右の対比で示します。2枚目は、合体のあとに名義人となった者の一月の数え始めを、時間の流れで示します。',
    notebooks=[
        dict(name='抵当権を消すとき、残すとき', args=dict(
            title='合体のとき、抵当権はどうなる？', sub='合体による登記等と抵当権（毎日ドリル 第35日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「消すとき」 on the left and 「残すとき」 on the right. Draw them large and in different accent colors (blue and orange) so they can never be confused or duplicated. Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 消すとき
Scene: an isometric scene of a bank figure nodding beside a record sheet. A small indented sub-line under the main entry line is marked with a round stamp labeled 付記. The new house model beside it has an empty record sheet.
Result badge: 付記登記で消滅を記録　移記しない

RIGHT PANEL (orange accent):
Panel header: 残すとき
Scene: an isometric scene of a record sheet on the left with a mortgage entry, and an arrow carrying that entry to a record sheet beside the new house model on the right. A small tag on the arrow is labeled 存続登記.
Result badge: 新しい建物の登記記録に移記する""",
            callout='権利を消す承諾があるときは、消滅した旨を付記登記で記録し、合体後の建物には移記しません。\n同じ内容の登記を残す存続登記のときは、合体後の建物の登記記録に移記します。',
            footer='不動産登記法50条、不動産登記規則120条',
            kanji='合・体・登・記・抵・当・消・残・付・移・存・続・建・物'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (消すとき on the left and 残すとき on the right) in different accent colors, and that no check mark and no cross mark is drawn, ')),
        dict(name='合体のあとの申請期間の数え始め', args=dict(
            title='一月の数え始めは、いつ？', sub='合体のあとに名義人となった者（毎日ドリル 第35日 エ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 3月1日 with an icon of two house models merging into one, and the right flag labeled 4月10日 with an icon of a deed document being handed to a buyer figure.
Upper lane (blue accent), lane label: 合体のときの名義人. A blue bracket starts at the left flag and extends to the right, labeled 合体の日から一月以内.
Lower lane (green accent), lane label: 合体のあとに名義人となった者. A green bracket starts at the right flag and extends to the right, labeled 自分の登記の日から一月以内.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and green).""",
            callout='合体のあとに名義人となった者は、合体の日ではなく、自分に係る登記があった日から一月以内に申請します。\n買う前に起きた合体でも、数え始めは自分の登記の日です。',
            footer='不動産登記法49条1項・4項',
            kanji='合・体・登・記・名・義・人・月・以・内・自・分・申・請'.split('・'), what='timeline',
            check='confirm the two lanes have different bracket labels in different accent colors, ')),
    ],
)
