def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='区分建物の相続人は被承継人名義で申請',
    intro='区分建物（マンションの一室のように、構造上区分された建物の部分）の表題登記について、「だれが」「だれの名義で」「何と一緒に」申請するのかを問う問題です（不動産登記法47条・48条、不動産登記事務取扱手続準則78条、不動産登記規則116条）。\n\nこの記事では、相続人や買主が申請する場合、既存の建物に接続して新築した場合、建物の個数の考え方、そして区分建物の表題部の記録を、具体的な場面で確認していきましょう。この問題は「誤っているもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('相続人は、亡くなった人を表題部所有者として申請する',
               '区分建物を新築した人について相続があったときは、相続人も、被承継人（亡くなった人）を表題部所有者とする表題登記を申請することができます（不動産登記法47条2項）。\n\n問題文は、相続人B自身を表題部所有者とする表題登記を申請できるとしています。表題部所有者になるのはBではなく、亡くなったAなので、本肢は誤りです。\n\n**たとえば**、新築の区分建物の表題登記をしないうちに、所有者Aが亡くなったとします。相続人Bが申請するときも、表題部の所有者欄に記録されるのは、Bではなく、亡くなったAです。'),
        'イ': ('買った人は、新築した人に代わって表題登記を申請できる',
               '新築した建物の所有権を取得した人が自分名義で表題登記を申請できる、と定める47条1項は、「区分建物以外の」建物を取得した人について定めています。区分建物の転得者は、これに入りません。\n\nそこで、区分建物を買い受けた人は、新築した人に代位して、新築した人を表題部所有者とする表題登記を申請することができる扱いです（民法423条）。本肢は正しいといえます。\n\n**たとえば**、新築された区分建物をAから買ったCが、Aが表題登記をしないまま放置しているので困っているとします。Cは、Aに代わって、Aを所有者とする表題登記を申請できます。'),
        'ウ': ('既存の建物に接続した区分建物は、変更の登記と併せて申請する',
               '表題登記がある建物（区分建物を除く）に接続して、区分建物が新築されたときは、その区分建物の表題登記の申請は、既存の建物の表題部の変更の登記の申請と併せてしなければなりません（不動産登記法48条3項）。\n\n本肢は正しいといえます。\n\n**たとえば**、表題登記のある一戸建てに接続して、別の部屋を新築したとします。接続すると既存の建物も区分建物になるため、新築した部屋の表題登記と、既存の建物の表題部の変更の登記を、あわせて申請します。'),
        'エ': ('同じ所有者の建物は、所有者の意思に反しない限り1個にできる',
               '一棟の建物に、構造上区分されて独立して住居などに使える部分が複数あるときは、原則として各部分を別々の1個の建物として取り扱います。ただし、所有者が同一であるときは、その所有者の意思に反しない限り、一棟の建物の全部を1個の建物として取り扱います（不動産登記事務取扱手続準則78条2項）。\n\n問題文は、Aの意思にかかわらず各部分が別の建物になるとしています。ただし書を見落としているので、本肢は誤りです。\n\n**たとえば**、1階と2階がそれぞれ独立して住める二世帯住宅の全部を、同じ人が所有しているとします。所有者が「全体で1棟の家として登記したい」と望むなら、区分建物にはせず、1個の建物として登記できます。'),
        'オ': ('区分建物の表題部には、同じ一棟の他の建物の家屋番号も載る',
               '区分建物の登記記録の表題部には、建物の表題部の登記事項のほか、その建物が属する一棟の建物に属する他の建物の家屋番号を記録します（不動産登記規則116条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、3戸が入るアパートの101号室の登記記録には、同じ一棟に属する102号室と103号室の家屋番号も記録されます。'),
    },
    summary=[
        ('ア', '誤', '区分建物の相続人が申請する表題登記の表題部所有者は、相続人ではなく、被承継人'),
        ('イ', '正', '区分建物を買った人は、新築した人に代位して、新築した人を表題部所有者とする表題登記を申請できる'),
        ('ウ', '正', '表題登記のある建物に接続して区分建物が新築されたときは、既存の建物の表題部の変更の登記と併せて申請する'),
        ('エ', '誤', '同じ所有者の建物は、所有者の意思に反しない限り、一棟の全部を1個の建物として取り扱う'),
        ('オ', '正', '区分建物の表題部には、同じ一棟の建物に属する他の建物の家屋番号も記録する'),
    ],
    summary_tail='アは「だれの名義で記録されるか」、エは「所有者の意思」というただし書がひっかけでした。区分建物の表題登記は、申請する人と、記録される名義人が一致しないことがある点に注意しましょう。',
    supplements=[
        '### 補足説明（ア・イ）：申請する人と、記録される名義人\n\n表題登記では、申請する人と、表題部の所有者欄に記録される人が違うことがあります。\n\n| 申請する人 | 記録される表題部所有者 | 根拠 |\n|---|---|---|\n| 新築した人、区分建物以外の建物を取得した人 | 申請した本人 | 47条1項 |\n| 区分建物を新築した人の相続人 | 被承継人（亡くなった人） | 47条2項 |\n| 区分建物を買った人（転得者） | 新築した人（代位して申請） | 民法423条 |\n\n**たとえば**、新築の部屋を買ったCが申請しても、所有者欄に載るのはCではなく、新築したAです。その後、AからCへの所有権の移転の登記を行うことになります。',
        '### 補足説明（エ）：同じ所有者の建物は、区分建物になるとは限らない\n\n一棟の建物の中に、構造上区分された独立して使える部分が複数あるとき、それが区分建物として登記されるかどうかは、所有者が同じかどうかで変わります（不動産登記事務取扱手続準則78条2項）。\n\n| 所有者 | 取り扱い |\n|---|---|\n| 各部分の所有者が異なる | 各部分を別々の1個の建物として取り扱う |\n| 全部の所有者が同一 | 所有者の意思に反しない限り、一棟の全部を1個の建物として取り扱う |\n| 同一で、所有者が別々の登記を望む | 各部分を別々の1個の建物として取り扱う |\n\n**たとえば**、二世帯住宅を親が全部所有していて、1階と2階を別々に売ることを考えているなら、区分建物として登記しておくのが合理的です。いずれも売る予定がなければ、全体で1個の建物としておくこともできます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第80日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法47条、48条、不動産登記事務取扱手続準則78条2項、不動産登記規則116条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'イ（区分建物の転得者が代位して申請できること）は、条文に直接の明文がなく、47条1項が「区分建物以外の」建物の取得者に限っていることからの整理と、登記実務上の取扱いに基づく説明です。取扱いの根拠となる通達・先例の原文は未確認です。',
        'エの補足説明の第3の行（所有者が同じで別々の登記を望む場合）と、二世帯住宅の例の「合理的」という部分は、準則78条2項の文言からの一般的な整理です。個別の登記実務の確認はしていません。',
    ],
    phrases=['相続人は亡くなった人の名義で申請します', '買った人は新築した人に代わって申請', '接続して新築したら一緒に申請します', '一個にも区分にも所有者の意思しだい', '区分建物は他の部屋の番号も載ります'],
    header=dict(t1='区分建物の登記は、', t2='だれの名義？', topic='不動産登記法　区分建物の表題登記',
                kanji='区・分・建・物・登・記・名・義・毎'),
    poster_intro='区分建物の表題登記を、「申請のしかた」（グループA：ア・イ・ウ）と「建物の個数と記録」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='区分建物の表題登記を整理', sub='不動産登記法 第47条・第48条（毎日ドリル 第80日）',
        col_a='申請のしかた', col_b='建物の個数と記録', n_a=3,
        cards=[
            dict(h='相続人は亡くなった人の名義で申請',
                 ill='an heir figure at a counter holding a form. A pale gray portrait outline of the deceased owner appears on the form, labeled 「被承継人」. A green check mark sits beside the form.',
                 words=['被承継人'], tag='所有者欄は亡くなった人'),
            dict(h='買った人は代位して申請',
                 ill='a buyer figure at a counter holding a form. A thin arrow runs from the form to a seller figure standing behind, who carries a name tag labeled 「新築した人」. A green check mark sits beside the buyer.',
                 words=['新築した人'], tag='名義は新築した人'),
            dict(h='接続して新築したら併せて申請',
                 ill='an existing house on the left connected by a short corridor to a newly built unit on the right. Two forms are stapled together in front of them.',
                 words=[], tag='二つ同時に申請'),
            dict(h='同じ所有者なら意思しだい',
                 ill='a two-story house. An owner figure points at the house with a thought bubble showing either one single building or two separate buildings.',
                 words=[], tag='一棟全体も区分もできる'),
            dict(h='他の部屋の家屋番号も載る',
                 ill='a record sheet for one apartment unit with a small list beside it showing three door icons that stand for the other units in the same building.',
                 words=[], tag='同じ一棟の分'),
        ],
        kanji=kj('相続人被承継買代位新築接続併申請所有者意思区分家屋番号', n=24)),
    nb_label='ア・イ・エ肢', nb_intro='ア・イ・エの補足説明に合わせた2枚です。1枚目は、申請する人と記録される名義人の違いを表で示します。2枚目は、同じ所有者の建物の扱いを左右で対比します。',
    notebooks=[
        dict(name='申請する人と、記録される名義人', args=dict(
            title='申請する人と、名義人は？', sub='不動産登記法47条（毎日ドリル 第80日 ア・イ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and three body rows, in rounded panel style. Each body row carries a small figure icon at the left edge (a builder figure, an heir figure, a buyer figure).
Header row (blue accent), three column headers: 申請する人 | 表題部所有者 | 根拠
Row 1: 区分建物以外の建物の取得者 | 申請した本人 | 47条1項
Row 2: 区分建物の新築者の相続人 | 被承継人 | 47条2項
Row 3: 区分建物を買った人 | 新築した人 | 民法423条
Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='区分建物では、申請する人と、所有者欄に記録される人が違うことがあります。\n相続人は被承継人、買った人は新築した人が、表題部所有者として記録されます。',
            footer='不動産登記法47条1項・2項',
            kanji=kj('申請人表題部所有者区分建物相続被承継買新築', n=16), what='table',
            check='confirm the table has exactly three body rows and that no check mark or cross mark appears, ')),
        dict(name='同じ所有者の建物の扱い', args=dict(
            title='同じ所有者の建物はどうなる？', sub='不動産登記事務取扱手続準則78条2項（毎日ドリル 第80日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「所有者が異なる」 on the left and 「所有者が同一」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not use check marks or cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 所有者が異なる
Scene: an isometric two-story house where the first floor and the second floor have name tags of different owner figures.
Rows of text:
取り扱い: 各部分を別々の1個の建物とする

RIGHT PANEL (green accent):
Panel header: 所有者が同一
Scene: an isometric two-story house with a single owner figure holding keys for both floors.
Rows of text:
取り扱い: 所有者の意思に反しない限り、一棟の全部を1個の建物とする""",
            callout='所有者が同一のときは、その所有者の意思に反しない限り、一棟の全部を1個の建物として取り扱います。\n区分建物にするかどうかは、所有者の意思が関わります。',
            footer='不動産登記事務取扱手続準則78条2項',
            kanji=kj('所有者異同一各部分別建物取扱意思一棟全部', n=16), what='panels',
            check='confirm the two panel headers are different strings (所有者が異なる on the left and 所有者が同一 on the right) drawn in different accent colors, ')),
    ],
)
