D = dict(
    catch='分筆では地番と権利の行き先を確かめる',
    intro='土地を二つに分ける「分筆の登記」について、新しい地番の付け方と、抵当権・地上権・地役権などの権利がどうなるかを問う問題です（不動産登記法40条、不動産登記規則102条から104条まで、不動産登記事務取扱手続準則67条）。正しいものの組合せを選びます。\n\nこの記事では、支号（枝番）のある土地を分けるときの地番と、権利を消すときの承諾、乙土地に権利を写す扱いを、具体的な場面で確認します。',
    sections={
        'ア': ('支号のある土地は、一方が従来の地番、他方は最終の支号の次',
               '本番に支号のある土地を分筆する場合は、その1筆に従来の地番を残し、他の各筆には、本番の最終の支号を追って順次支号を付けます（準則67条1項4号ただし書）。また、地番の支号には数字を用い、支号の支号は用いません（同項9号）。\n\n本肢は正しいといえます。\n\n**たとえば**、20番3の土地を2筆に分けるとき、20番の土地の支号が20番8まで使われているなら、一方は20番3のまま、もう一方は20番9になります。20番3の1のような付け方はしません。'),
        'イ': ('転抵当があるときは、転抵当権者の承諾も必要',
               '分筆の際に抵当権を消滅させるときは、抵当権者の承諾を証する情報を提供します。\n\nその抵当権を目的とする第三者の権利の登記があるときは、その第三者が承諾したことを証する情報も、併せて提供しなければ、消滅の登記はされません（不動産登記法40条かっこ書、不動産登記規則104条1項2号）。\n\n問題文は、Cの承諾を証する情報を提供することなく抵当権が消滅した旨の登記がされるとしているので、本肢は誤りです。\n\n**たとえば**、Bの抵当権を、さらにCが転抵当にとっているなら、乙土地の抵当権を消すには、Bだけでなくこの第三者のCの承諾も必要です。'),
        'ウ': ('消滅の記録は、甲土地の抵当権の登記に付記する',
               '乙土地について権利が消滅した旨は、分筆後の甲土地の登記記録のその権利の登記に、付記登記で記録します。このとき、消滅した権利の登記を乙土地の登記記録に転写することは要りません（不動産登記規則104条2項）。\n\n問題文は、乙土地に抵当権の登記を転写したうえで消滅を記録するとしているので、本肢は誤りです。\n\n**たとえば**、乙土地の登記記録には抵当権の登記そのものが写されません。甲土地の抵当権の登記の横に「乙土地について消滅した」と書き添えて、乙土地の側では何も写さない、というイメージです。'),
        'エ': ('地上権は乙土地に写し、甲土地が共に目的である旨も記録する',
               '分筆の登記で乙土地の登記記録に権利を転写するとき、所有権及び担保権以外の権利（地役権を除く）については、分筆後の甲土地が共にその権利の目的である旨を記録します（不動産登記規則102条1項）。地上権はこれに当たります。\n\n本肢は正しいといえます。\n\n**たとえば**、1筆の土地全体にBの地上権の登記があるとします。分筆すると、乙土地にも地上権の登記が写され、「甲土地と共にこの地上権の目的である」旨が記録されます。'),
        'オ': ('地役権の範囲が一部になるなら、範囲と図面番号を記録する',
               '承役地についての地役権の登記がある甲土地を分筆する場合に、地役権設定の範囲が分筆後の甲土地又は乙土地の一部となるときは、その土地の登記記録の地役権の登記に、設定の範囲と地役権図面番号を記録しなければなりません（不動産登記規則103条1項）。\n\n問題文は「記録することを要しない」としているので、本肢は誤りです。\n\n**たとえば**、通行のための地役権が土地の北のはしの幅2メートルだけにあるとします。分筆で乙土地がその一部を含むなら、乙土地の登記に、範囲と図面の番号を記録します。'),
    },
    summary=[
        ('ア', '正', '支号のある土地の分筆は、1筆に従来の地番を残し、他の筆は最終の支号の次の番号にする'),
        ('イ', '誤', '転抵当などの第三者の権利があるときは、その第三者の承諾を証する情報も必要'),
        ('ウ', '誤', '権利の消滅は、甲土地の登記に付記して記録する。乙土地には転写しない'),
        ('エ', '正', '地上権は乙土地に転写し、分筆後の甲土地が共に目的である旨を記録する'),
        ('オ', '誤', '地役権設定の範囲が土地の一部になるときは、範囲と地役権図面番号を記録する'),
    ],
    summary_tail='イは第三者の承諾の見落とし、ウは記録する登記記録の取り違え、オは「記録を要しない」への入れ替えです。分筆では、権利が甲土地・乙土地のどちらの登記記録にどう載るかを分けて覚えましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：分筆で権利を消すときの流れ\n\n分筆の登記では、権利者が承諾すれば、乙土地についてだけ抵当権などを消すことができます（不動産登記法40条）。流れは次のとおりです。\n\n1. 分筆の申請と一緒に、抵当権者の承諾を証する情報を提供する。\n2. その抵当権を目的とする第三者（転抵当権者など）がいれば、その承諾を証する情報も提供する。\n3. 登記官は、甲土地の登記記録のその抵当権の登記に、乙土地について消滅した旨を付記する。乙土地には転写しない。\n\n**たとえば**、1筆の土地に抵当権があり、売る部分の乙土地だけ抵当権を外したいときは、この流れで乙土地だけが担保から外れます。',
        '### 補足説明（エ・オ）：権利ごとの、乙土地への写し方\n\n分筆で乙土地に権利を写すとき、権利の種類によって扱いが違います（不動産登記規則102条・103条）。\n\n- 地上権などの所有権・担保権・地役権以外の権利：乙土地に転写し、分筆後の甲土地が共に目的である旨を記録する。\n- 抵当権などの担保権：乙土地に転写し、共同担保目録を作る。\n- 地役権：乙土地に存続する場合だけ転写する。範囲が土地の一部なら、範囲と地役権図面番号も記録する。\n\n**たとえば**、通行地役権が分筆後の乙土地の一部にだけかかるなら、乙土地の登記に範囲と図面番号が載ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第27日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、法40条、不動産登記規則102条1項、103条1項、104条1項・2項は、`note-articles/laws/` 配下の原文で、準則67条1項4号・9号は準則の原文で確認しました。',
        'イの「転抵当」は、抵当権を目的とする第三者の権利の例として挙げたものです。規則104条1項2号は「第三者の権利に関する登記」と定めており、権利の種類は転抵当に限りません。',
        '各具体例（20番3の分筆、地上権、通行地役権など）は、条文の文言を日常の場面に置き換えた説明で、個別の事例の判断ではありません。',
    ],
    phrases=['支号のある土地は最終の支号の次になります', '転抵当があれば第三者の承諾も要ります', '消滅は甲土地の登記に付記します', '地上権は乙土地にも写されます', '地役権は範囲と図面番号を記録します'],
    header=dict(t1='分筆すると、', t2='権利はどこへ？', topic='不動産登記法　分筆の登記',
                kanji='分・筆・権・利・毎・登・記'),
    poster_intro='分筆の登記を、「地番と権利の消滅」（グループA：ア・イ・ウ）と「権利の写し方」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='分筆の決まりを整理', sub='不動産登記法40条と不動産登記規則102条から104条まで（毎日ドリル 第27日）',
        col_a='地番と権利の消滅', col_b='権利の写し方', n_a=3,
        cards=[
            dict(h='支号のある土地は最終の次の支号',
                 ill='an isometric land plot split into two by a dotted line. The left piece carries a sign labeled 「20番3」 and the right piece carries a sign labeled 「20番9」. A green check mark sits beside the right piece.',
                 words=['20番3', '20番9'], tag='従来の地番と次の支号'),
            dict(h='転抵当があれば第三者の承諾も必要',
                 ill='three small figures standing in a row behind a stack of documents: the first figure carries a name tag 「抵当権者」, the second figure carries a name tag 「転抵当権者」, and both hold a small signed paper. A green check mark sits above the group.',
                 words=['抵当権者', '転抵当権者'], tag='第三者の承諾も必要'),
            dict(h='消滅の記録は甲土地の登記に付記',
                 ill='two record sheets side by side. The left sheet labeled 「甲土地」 has a small note stamped on its line. The right sheet labeled 「乙土地」 is blank and clean. A green arrow points from the note on the left sheet to a small green check mark.',
                 words=['甲土地', '乙土地'], tag='乙土地には写さない'),
            dict(h='地上権は乙土地にも写す',
                 ill='two neighboring land plots, the left labeled 「甲土地」 and the right labeled 「乙土地」, both covered by one shared translucent roof-shaped outline labeled 「地上権」. A green check mark sits beside the outline.',
                 words=['甲土地', '乙土地', '地上権'], tag='甲土地も共に目的'),
            dict(h='地役権は範囲と図面番号を記録',
                 ill='an isometric land plot with a narrow strip along one edge highlighted in green. A small blueprint sheet is attached to the strip and labeled 「図面番号」. A green check mark sits beside the strip.',
                 words=['図面番号'], tag='一部なら範囲を記録'),
        ],
        kanji='分・筆・番・支・号・抵・当・権・者・甲・乙・土・地・上・役・範・囲・図・面'.split('・')),
    nb_label='イ・ウ・エ・オ肢', nb_intro='イ・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、分筆で権利を消すときの承諾と記録の流れを示します。2枚目は、権利の種類ごとの乙土地への写し方を早見表にします。',
    notebooks=[
        dict(name='分筆で権利を消すときの流れ', args=dict(
            title='分筆で抵当権を消す流れ', sub='不動産登記法40条（毎日ドリル 第27日 イ・ウ）',
            req='a vertical flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow in three steps, connected by small downward arrows with no text.
Step 1 (blue accent): header 申請と一緒に提供. Content: a figure labeled 抵当権者 holding a signed paper labeled 承諾を証する情報.
Step 2 (green accent): header 第三者がいるとき. Content: a second figure labeled 転抵当権者 holding a signed paper labeled 承諾を証する情報.
Step 3 (orange accent): header 登記官の記録. Content: two record sheets side by side: the left sheet labeled 甲土地 carries a small stamp labeled 乙土地について消滅; the right sheet labeled 乙土地 is blank.
Use exactly these strings, and no others, for the labels.""",
            callout='権利を消す承諾は、権利者のほか、その権利を目的とする第三者の分も必要です。\n消えたことは甲土地の登記に付記して記録し、乙土地には消えた権利の登記を写しません。',
            footer='不動産登記法40条、不動産登記規則104条',
            kanji='分・筆・抵・当・権・者・承・諾・甲・乙・土・地・消・滅'.split('・'), what='flow',
            check='confirm there are exactly three steps connected by arrows, and that the left record sheet labeled 甲土地 carries the stamp while the right one labeled 乙土地 is blank, ')),
        dict(name='権利の種類ごとの、乙土地への写し方', args=dict(
            title='権利は、乙土地へどう写る？', sub='分筆と権利の転写（毎日ドリル 第27日 エ・オ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Two columns and three data rows. The header row has the column names. Each data row has a small isometric icon at the left of its first cell (a land plot with a roof outline for the first row, a house with a lock-shaped stamp for the second row, a narrow strip along a plot edge for the third row). Use exactly these strings, and no others:
Header row: 権利 | 乙土地への写し方
Row 1: 地上権 | 転写し、甲土地が共に目的である旨も記録
Row 2: 抵当権 | 転写し、共同担保目録を作る
Row 3: 地役権 | 存続する場合だけ転写し、一部なら範囲と図面番号も記録
Draw the three right-hand cells in three different accent colors (blue, green and orange) because they are three different strings.""",
            callout='権利の種類によって、乙土地への写し方は違います。\n地上権は甲土地が共に目的であることを記録し、地役権は範囲が一部なら範囲と図面番号まで記録します。',
            footer='不動産登記規則102条、103条',
            kanji='権・利・乙・土・地・上・抵・当・役・転・写・範・囲'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, confirm the three right-hand cells are in three different accent colors, ')),
    ],
)
