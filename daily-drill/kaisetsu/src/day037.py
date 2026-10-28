D = dict(
    catch='共用部分の登記は、申請人と承諾に注意',
    intro='マンションの集会室など、規約で共用部分とされた建物に関する登記を問う問題です（不動産登記法51条・58条、不動産登記規則141条）。共用部分である旨の登記をすると、登記の記録がふつうの建物とは大きく変わります。\n\nこの記事では、だれが申請するのか、だれの承諾が必要なのか、登記官がどう処理するのか、そして規約を廃止したときの表題登記の期限を、具体的な場面で確認していきましょう。なお、この問題は「誤っているもの」を選ぶ問題です。',
    sections={
        'ア': ('共用部分である旨の登記がある建物の変更は、所有者が申請する',
               '建物の床面積などに変更があったときは、表題部所有者又は所有権の登記名義人が、変更があった日から一月以内に変更の登記を申請します。共用部分である旨の登記がある建物の場合は、申請するのは「所有者」です（不動産登記法51条1項かっこ書）。\n\n共用部分である旨の登記をすると、表題部所有者の登記や権利に関する登記が抹消されます（同法58条4項）。登記上の名義人がいなくなるため、「所有者」が申請することになります。本肢は正しいといえます。\n\n**たとえば**、規約で共用部分とされた集会室を増築して、床面積が増えたとします。集会室の所有者は、増築の日から一月以内に、表題部の変更の登記を申請します。'),
        'イ': ('共用部分である旨の登記を申請できるのは、名義人だけ',
               '共用部分である旨の登記は、その建物の表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法58条2項）。\n\n問題文のBは管理組合の理事長で、集会室の所有権の登記名義人はAです。申請人になれるのはAであり、理事長が管理者として申請することはできません。本肢は誤りです。\n\n**たとえば**、マンションの集会室が、規約で共用部分とされたとします。共用部分である旨の登記を申請できるのは、その集会室の名義人であるAさんです。理事長の立場であっても、申請人にはなれません。'),
        'ウ': ('抵当権者の承諾がなければ、共用部分である旨の登記は申請できない',
               '共用部分である旨の登記は、その建物に所有権等の登記以外の権利に関する登記があるときは、その権利の登記名義人の承諾があるときでなければ、申請することができません（不動産登記法58条3項）。\n\n抵当権は、この「所有権等の登記以外の権利」に当たります。本肢は正しいといえます。\n\n**たとえば**、集会室にC銀行の抵当権の登記があるとします。共用部分である旨の登記をすると、権利に関する登記が抹消されます（同条4項）。そのため、Cの承諾がなければ、Aさんは申請できません。'),
        'エ': ('所有権の登記がない建物は、表題部所有者を抹消する記号を記録する',
               '登記官は、共用部分である旨の登記をするときは、所有権の登記がない建物では表題部所有者に関する登記事項を抹消する記号を記録し、所有権の登記がある建物では権利に関する登記の抹消をします（不動産登記規則141条）。\n\n本肢は表題登記だけの区分建物なので、表題部所有者に関する登記事項を抹消する記号を記録します。本肢は正しいといえます。\n\n**たとえば**、新築したばかりで、表題登記だけがされた集会室の場合、権利に関する登記はまだありません。そこで、表題部の所有者の欄に、抹消を示す記号が記録されます。'),
        'オ': ('規約の廃止のあとに取得した者は、取得の日から一月以内に申請する',
               '共用部分である旨を定めた規約を廃止すると、建物の所有者は、廃止の日から一月以内に表題登記を申請します（不動産登記法58条6項）。\n\n規約を廃止した後に所有権を取得した者は、その取得の日から一月以内に表題登記を申請します（同条7項）。\n\n問題文のDは廃止の後に取得した者なのに、「規約の廃止の日から」としているので、本肢は誤りです。\n\n**たとえば**、6月1日に規約が廃止され、6月20日にDさんが所有権を取得したとします。Dさんの一月は、6月1日からではなく、取得した6月20日から数えます。'),
    },
    summary=[
        ('ア', '正', '共用部分である旨の登記がある建物の表題部の変更は、「所有者」が一月以内に申請する'),
        ('イ', '誤', '共用部分である旨の登記を申請できるのは、名義人だけで、理事長でも申請人になれない'),
        ('ウ', '正', '抵当権などの登記があるときは、その名義人の承諾がなければ申請できない'),
        ('エ', '正', '所有権の登記がない建物は、表題部所有者に関する登記事項を抹消する記号を記録する'),
        ('オ', '誤', '規約廃止のあとに所有権を取得した者の一月は、廃止の日ではなく取得の日から数える'),
    ],
    summary_tail='イは「申請できる人」、オは「一月の数え始め」を入れ替えた出題です。共用部分である旨の登記は、申請人、承諾、登記官の処理の順に整理しましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：共用部分である旨の登記の流れ\n\n共用部分である旨の登記は、次の順に進みます。\n\n| 段階 | 内容 |\n|---|---|\n| 申請できる人 | 表題部所有者又は所有権の登記名義人だけ（不動産登記法58条2項） |\n| 申請の条件 | 所有権等の登記以外の権利に関する登記があるときは、その権利の登記名義人の承諾が必要（同条3項） |\n| 登記官の処理 | 所有権の登記がない建物は、表題部所有者に関する登記事項を抹消する記号を記録する。所有権の登記がある建物は、権利に関する登記を抹消する（不動産登記規則141条） |\n\n**たとえば**、抵当権の付いた集会室を共用部分にするときは、名義人のAさんが、抵当権者の承諾を得て申請します。登記がされると、集会室の権利に関する登記は抹消されます。',
        '### 補足説明（オ）：規約を廃止したあとの表題登記の期限\n\n共用部分である旨を定めた規約を廃止したときの表題登記は、だれが申請するかによって、一月の数え始めが変わります。\n\n- 規約を廃止したときの所有者：規約の廃止の日から一月以内（不動産登記法58条6項）。\n- 規約を廃止した後に所有権を取得した者：その所有権の取得の日から一月以内（同条7項）。\n\n**たとえば**、6月1日に規約が廃止され、6月20日にDさんが所有権を取得したとします。廃止のときの所有者は6月1日から一月以内、Dさんは6月20日から一月以内です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第37日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法51条1項・58条2項・3項・4項・6項・7項、不動産登記規則141条は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（集会室の増築、抵当権の付いた集会室、6月1日と6月20日の例）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        'アの「登記上の名義人がいなくなるため、所有者が申請する」という説明は、58条4項の抹消と51条1項かっこ書を結び付けた条文からの一般的な整理です。',
    ],
    phrases=['共用部分の変更は所有者が申請します', '申請できるのは名義人だけです', '抵当権者の承諾が必要です', '所有権の登記がなければ記号で抹消', '規約廃止のあとは取得の日から'],
    header=dict(t1='共用部分の登記、', t2='だれが申請する？', topic='不動産登記法　共用部分の登記',
                kanji='共・用・部・分・登・記'),
    poster_intro='共用部分である旨の登記を、「申請する人と承諾」（グループA：ア・イ・ウ）と「登記官の処理と規約の廃止」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='共用部分の登記を整理', sub='不動産登記法 第51条・第58条（毎日ドリル 第37日）',
        col_a='申請する人と承諾', col_b='登記官の処理と規約の廃止', n_a=3,
        cards=[
            dict(h='共用部分の変更は所有者が申請',
                 ill='an isometric hall building model labeled 「共用部分」 with a newly added extension section. An owner figure with a name tag labeled 「所有者」, highlighted with a green glow, holds a form. A calendar page labeled 「一月以内」 sits beside the form. A green check mark sits beside the owner.',
                 words=['共用部分', '所有者', '一月以内'], tag='申請人は所有者'),
            dict(h='申請できるのは名義人だけ',
                 ill='a hall building model. A figure with a name tag labeled 「名義人」, highlighted with a green glow, submits a form. A second figure with a name tag labeled 「理事長」, drawn in faded gray, stands aside with empty hands. A green check mark sits beside the first figure.',
                 words=['名義人', '理事長'], tag='理事長は申請人でない'),
            dict(h='抵当権者の承諾がなければ申請できない',
                 ill='a hall building model with a record sheet labeled 「抵当権」 beside it. A bank figure holds a signed paper labeled 「承諾」 and hands it to the owner figure. A green check mark sits beside the paper.',
                 words=['抵当権', '承諾'], tag='権利の名義人の承諾'),
            dict(h='所有権の登記がなければ記号で抹消',
                 ill='a record sheet with an owner line labeled 「表題部所有者」. A single thin horizontal line, not an X shape, is drawn through the owner line as a record symbol. A registrar figure with a stamp stands beside the sheet. A green check mark sits beside the sheet.',
                 words=['表題部所有者'], tag='抹消の記号を記録'),
            dict(h='規約廃止のあとの取得者は取得の日から',
                 ill='a horizontal timeline. On the left a flag labeled 「規約廃止」; further right a second flag labeled 「所有権取得」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['規約廃止', '所有権取得', '一月以内'], tag='表題登記を申請'),
        ],
        kanji='共・用・部・分・所・有・者・月・以・内・名・義・人・理・事・長・申・請・承・諾・抵・当・権・表・題・抹・消・記・号・規・約・廃・止・取・得・登'.split('・')),
    nb_label='イ・ウ・オ肢', nb_intro='イ・ウ・オの補足説明に合わせた2枚です。1枚目は、共用部分である旨の登記の流れ（申請人、承諾、登記官の処理）を順に示します。2枚目は、規約を廃止したあとの表題登記の一月の数え始めを、時間の流れで示します。',
    notebooks=[
        dict(name='共用部分である旨の登記の流れ', args=dict(
            title='共用部分の登記は、どう進む？', sub='申請人・承諾・登記官の処理（毎日ドリル 第37日 イ・ウ）',
            req='a flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow in three blocks, connected by small downward arrows with no text.
Block 1 (blue accent), block header: 申請できる人. A single row with an owner figure carrying a name tag 名義人, with the label: 表題部所有者又は所有権の登記名義人だけ
Block 2 (green accent), block header: 申請の条件. A single row with a bank figure holding a signed paper, with the label: 抵当権などの登記があるときは、その名義人の承諾が必要
Block 3 (orange accent), block header: 登記官の処理. Two side-by-side rows:
Left row, with a record sheet whose owner line has one thin horizontal erase line (not an X): 所有権の登記がない建物は、表題部所有者を抹消する記号を記録
Right row, with a record sheet whose rows are erased with thin horizontal lines (not an X): 所有権の登記がある建物は、権利に関する登記を抹消
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='共用部分である旨の登記を申請できるのは、名義人だけです。\n抵当権などの登記があるときは、その名義人の承諾が必要で、登記をすると表題部所有者や権利に関する登記は抹消されます。',
            footer='不動産登記法58条2項から4項、不動産登記規則141条',
            kanji='共・用・部・分・登・記・申・請・名・義・人・承・諾・抵・当・権・抹・消・記・号'.split('・'), what='blocks',
            check='confirm there are exactly three blocks in the flow, that Block 3 has two side-by-side rows, and that no check mark and no cross mark is drawn, ')),
        dict(name='規約を廃止したあとの一月の数え始め', args=dict(
            title='表題登記の一月は、いつから？', sub='共用部分の規約の廃止（毎日ドリル 第37日 オ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 6月1日 with an icon of a rule book being crossed out by a thin horizontal line (not an X), and the right flag labeled 6月20日 with an icon of a deed document being handed to a buyer figure.
Upper lane (blue accent), lane label: 規約を廃止したときの所有者. A blue bracket starts at the left flag and extends to the right, labeled 廃止の日から一月以内.
Lower lane (green accent), lane label: 廃止の後に所有権を取得した者. A green bracket starts at the right flag and extends to the right, labeled 取得の日から一月以内.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and green).""",
            callout='規約を廃止した後に所有権を取得した者は、廃止の日ではなく、所有権を取得した日から一月以内に表題登記を申請します。\n廃止のときの所有者は、廃止の日から一月以内です。',
            footer='不動産登記法58条6項・7項',
            kanji='規・約・廃・止・所・有・権・取・得・月・以・内・表・題・登・記'.split('・'), what='timeline',
            check='confirm the two lanes have different bracket labels in different accent colors, ')),
    ],
)
