def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='規約を廃止したら一月以内に表題登記',
    intro='共用部分である旨の登記について、「だれが申請できるか」「申請に承諾が必要か」「登記官は何をするか」「規約を廃止したらどうなるか」を問う問題です（不動産登記法58条、不動産登記規則141条）。\n\nこの記事では、規約によって共用部分とされた建物（たとえばマンションの集会所や倉庫）の登記の流れを、具体的な場面で確認していきましょう。この問題は「正しいもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('所有権の登記がなければ、所有者の記録に抹消の記号が付く',
               '登記官は、共用部分である旨の登記をするときは、職権で、その建物について表題部所有者の登記又は権利に関する登記を抹消しなければなりません（不動産登記法58条4項）。\n\n抹消の方法は、所有権の登記がない建物では、表題部所有者に関する登記事項を抹消する記号を記録します。所有権の登記がある建物では、権利に関する登記の抹消をします（不動産登記規則141条）。本肢は正しいといえます。\n\n**たとえば**、新築した集会所の登記が、表題部所有者Aの名前だけで、所有権の登記がされていないとします。共用部分である旨の登記をすると、Aの所有者欄に抹消の記号が付けられます。'),
        'イ': ('抵当権の登記があるときは、抵当権者の承諾が要る',
               '共用部分である旨の登記は、その建物に所有権等の登記以外の権利に関する登記があるときは、その権利の登記名義人の承諾がなければ、申請することができません（不動産登記法58条3項）。\n\n問題文は、抵当権者であるB銀行の承諾がなくても申請できるとしているので、本肢は誤りです。\n\n**たとえば**、Aが所有する倉庫に、B銀行の抵当権の設定の登記があるとします。Aが倉庫を共用部分とする旨の登記を申請するには、B銀行の承諾を得る必要があります。なお、登記をすると、倉庫についての権利に関する登記は、登記官が職権で抹消します（同条4項）。'),
        'ウ': ('規約を廃止したら、廃止の日から一月以内に表題登記を申請する',
               '共用部分である旨の登記がある建物について、共用部分である旨を定めた規約を廃止したときは、その建物の所有者は、規約の廃止の日から一月以内に、建物の表題登記を申請しなければなりません（不動産登記法58条6項）。\n\n本肢は正しいといえます。\n\n**たとえば**、集会所を共用部分としていた規約を6月1日に廃止したとします。共用部分である旨の登記で表題部所有者や権利に関する登記が抹消されていますから、6月1日から一月以内に、あらためて建物の表題登記を申請します。'),
        'エ': ('規約の廃止の後に所有権を取得した人は、取得の日から数える',
               '規約を廃止した後にその建物の所有権を取得した人は、規約の廃止の日からではなく、その所有権の取得の日から一月以内に、建物の表題登記を申請しなければなりません（不動産登記法58条7項）。\n\n問題文は、Bが規約の廃止の日である6月1日から一月以内に申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、6月1日に規約を廃止し、7月10日にBがその建物の所有権を取得したとします。Bの一月は、6月1日ではなく、取得した7月10日から数えます。'),
        'オ': ('申請できるのは、表題部所有者や所有権の登記名義人だけ',
               '共用部分である旨の登記は、その建物の表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法58条2項）。\n\n問題文は、区分所有者であれば、附属の建物の所有権の登記名義人でなくても申請できるとしています。この点が条文と違うので、本肢は誤りです。\n\n**たとえば**、マンションに住んでいる区分所有者が、「あの倉庫は皆で使っているから、共用部分にしたい」と考えても、その倉庫の表題部所有者や所有権の登記名義人でなければ、自分で共用部分である旨の登記を申請することはできません。'),
    },
    summary=[
        ('ア', '正', '所有権の登記がない建物は、表題部所有者に関する登記事項を抹消する記号を記録する'),
        ('イ', '誤', '抵当権などの登記があるときは、その権利の登記名義人の承諾がなければ申請できない'),
        ('ウ', '正', '共用部分である旨の規約を廃止したときは、廃止の日から一月以内に表題登記を申請する'),
        ('エ', '誤', '規約の廃止の後に所有権を取得した人は、廃止の日ではなく、取得の日から一月以内に申請する'),
        ('オ', '誤', '共用部分である旨の登記を申請できるのは、表題部所有者又は所有権の登記名義人だけ'),
    ],
    summary_tail='イは「承諾の要否」、エは「一月の起算日」、オは「申請人の範囲」を入れ替えた出題です。共用部分である旨の登記は、する側（58条1項から4項）と、やめる側（6項・7項）で分けて整理しましょう。',
    supplements=[
        '### 補足説明（エ）：規約を廃止したときの、一月の数え始め\n\n共用部分である旨を定めた規約を廃止すると、建物の表題登記をやり直す必要があります（不動産登記法58条6項・7項）。その期限は、申請する人によって数え始めが違います。\n\n- 規約を廃止したときの建物の所有者：規約の廃止の日から一月以内（6項）。\n- 規約を廃止した後に所有権を取得した人：自分の所有権の取得の日から一月以内（7項）。\n\n**たとえば**、規約を6月1日に廃止し、7月10日にBが所有権を取得したとします。廃止の時の所有者は6月1日から、Bは7月10日からそれぞれ一月以内です。',
        '### 補足説明（イ・オ）：共用部分である旨の登記の申請\n\n共用部分である旨の登記をするときの、だれが申請し、だれの承諾が要り、登記官は何をするのかを整理します（不動産登記法58条）。\n\n| 項目 | 内容 | 根拠 |\n|---|---|---|\n| 申請できる人 | 建物の表題部所有者又は所有権の登記名義人 | 2項 |\n| 承諾が必要な人 | 抵当権などの権利の登記名義人（さらにその権利を目的とする第三者の権利の登記があれば、その第三者） | 3項 |\n| 登記官がすること | 職権で、表題部所有者の登記又は権利に関する登記を抹消する | 4項 |\n\n**たとえば**、抵当権が付いた倉庫を共用部分にするなら、倉庫の登記名義人が申請し、抵当権者の承諾を添えます。登記が済むと、抵当権の登記を含む権利に関する登記は、登記官によって抹消されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第81日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法58条2項・3項・4項・6項・7項、不動産登記規則141条は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例（集会所、倉庫、マンションの住人など）は、条文を日常の場面にかみ砕いた説明で、個別の登記実務の確認はしていません。ウの「あらためて表題登記が必要」という説明は、58条4項（登記の抹消）と6項からの一般的な整理です。',
        '補足説明（エ）の期限の説明は、58条6項・7項の文言のとおりです。具体例の日付（6月1日、7月10日）は説明のために置いた架空のものです。',
    ],
    phrases=['所有権の登記がなければ記号で抹消です', '抵当権者の承諾がいります', '規約を廃止したら表題登記を申請します', '廃止の後に取得したら取得の日からです', '区分所有者でも申請できません'],
    header=dict(t1='共用部分の登記、', t2='だれが何をする？', topic='不動産登記法　共用部分である旨の登記',
                kanji='共・用・部・分・登・記・法・毎'),
    poster_intro='共用部分である旨の登記を、「登記をするとき」（グループA：ア・イ）と「規約の廃止と申請人」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='共用部分の登記を整理', sub='不動産登記法 第58条（毎日ドリル 第81日）',
        col_a='登記をするとき', col_b='規約の廃止と申請人', n_a=2,
        cards=[
            dict(h='所有権の登記がなければ抹消の記号',
                 ill='a building record sheet whose owner column is covered by a single horizontal line mark. A small caption plate above the owner column reads 「表題部所有者」.',
                 words=['表題部所有者'], tag='記号で抹消する'),
            dict(h='抵当権者の承諾が必要',
                 ill='a bank figure carrying a name tag labeled 「抵当権者」 pressing an approval seal labeled 「承諾」 on a form, beside a building with a small lock icon.',
                 words=['抵当権者', '承諾'], tag='承諾があってはじめて'),
            dict(h='規約を廃止したら表題登記',
                 ill='a document labeled 「規約」 with a ribbon being torn away on the left. To the right, a building with a new record sheet labeled 「表題登記」.',
                 words=['規約', '表題登記'], tag='廃止の日から一月'),
            dict(h='廃止の後の取得者は取得の日から',
                 ill='a horizontal timeline. On the left a flag labeled 「廃止」, further right a second flag labeled 「取得」. A green bracket starts at the second flag and extends to the right.',
                 words=['廃止', '取得'], tag='起算日は取得の日'),
            dict(h='申請できるのは所有者だけ',
                 ill='a building owner figure carrying a name tag labeled 「所有者」 at a counter holding a form. A faded gray resident figure with no tag stands aside in the background.',
                 words=['所有者'], tag='住人は申請できない'),
        ],
        kanji=kj('表題部所有者抵当権承諾規約廃止登記取得申請', n=20)),
    nb_label='イ・エ・オ肢', nb_intro='エの補足説明に合わせた1枚目は、一月の数え始めを時間の流れで示します。イ・オの補足説明に合わせた2枚目は、共用部分である旨の登記で、だれが何をするのかを順に示します。',
    notebooks=[
        dict(name='規約廃止の後、一月の数え始め', args=dict(
            title='一月の数え始めは、いつ？', sub='不動産登記法58条6項・7項（毎日ドリル 第81日 エ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 六月一日 with an icon of a document being torn, and the right flag labeled 七月十日 with an icon of a building key being handed over.
Upper lane (blue accent), lane label: 規約を廃止したときの所有者. A blue bracket starts at the left flag and extends to the right, labeled 廃止の日から一月以内.
Lower lane (green accent), lane label: 廃止の後に取得した人. A green bracket starts at the right flag and extends to the right, labeled 取得の日から一月以内.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and green).""",
            callout='規約の廃止の後に所有権を取得した人は、廃止の日ではなく、自分の所有権の取得の日から一月以内に、表題登記を申請します。',
            footer='不動産登記法58条6項・7項',
            kanji=kj('規約廃止所有者取得一月以内表題登記六月七月', n=16), what='timeline',
            check='confirm the two lanes have different bracket labels in different accent colors, ')),
        dict(name='共用部分である旨の登記の流れ', args=dict(
            title='共用部分にする登記の流れ', sub='不動産登記法58条2項・3項・4項（毎日ドリル 第81日 イ・オ）',
            req='a step-by-step flow diagram',
            layout="""--- FLOW ---
A clean flat-design vertical flow with three steps connected by downward arrows.

Step 1 (blue box): 申請する
Figure with a name tag: 表題部所有者又は所有権の登記名義人
Icon: a building owner figure holding a form at a counter.

Step 2 (green box): 承諾を得る
Figure with a name tag: 抵当権などの権利の登記名義人
Icon: a bank figure pressing an approval seal.

Step 3 (orange box): 登記官が抹消する
Icon: a registrar figure erasing the owner column and the rights entries of a building record sheet.
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='共用部分である旨の登記は、建物の表題部所有者又は所有権の登記名義人だけが申請できます。\n抵当権などの登記があるときは、その権利者の承諾が要り、登記後は登記官が職権で抹消します。',
            footer='不動産登記法58条2項・3項・4項',
            kanji=kj('申請承諾抹消登記官表題部所有者権利抵当', n=16), what='flow',
            check='confirm there are exactly three steps in the flow and that no check mark or cross mark appears, ')),
    ],
)
