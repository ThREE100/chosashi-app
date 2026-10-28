D = dict(
    catch='三年と二年、数え始めに注意',
    intro='所有権の保存の登記、相続による所有権の移転の登記、住所等の変更の登記について、「いつまでに申請するのか」「登記官はどう動くのか」を問う問題です（不動産登記法76条〜76条の6）。\n\nこの記事では、相続登記の三年と住所変更の二年の数え始めの違いを、具体的な場面で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('相続登記の三年は、死亡の日ではなく、知った日から数える',
               '所有権の登記名義人について相続の開始があったときは、相続により所有権を取得した者は、自己のために相続の開始があったことを知り、かつ、その所有権を取得したことを知った日から三年以内に、所有権の移転の登記を申請しなければなりません（不動産登記法76条の2第1項）。\n\n問題文は「4月1日（死亡の日）から三年以内」としていますが、数え始めは、死亡を知り、自分が取得したことも知った5月1日です。本肢は誤りです。\n\n**たとえば**、父が4月1日に亡くなり、遠方に住む子が、5月1日に父の死亡と自分が土地を相続することを知ったとします。三年は5月1日から数え始めます。'),
        'イ': ('住所を移したら、変更の日から二年以内に登記を申請する',
               '所有権の登記名義人の住所について変更があったときは、その登記名義人は、変更があった日から二年以内に、住所についての変更の登記を申請しなければなりません（不動産登記法76条の5）。\n\n本肢は正しいといえます。\n\n**たとえば**、令和8年6月1日に引っ越して住所が変わった土地の所有者は、同じ6月1日から二年以内に、登記記録上の住所を新しい住所に直す登記を申請します。'),
        'ウ': ('法人の住所の変更は、申出がなくても登記官が職権で登記できる',
               '登記官は、所有権の登記名義人の住所について変更があったと認めるべき場合として法務省令で定める場合には、職権で変更の登記をすることができます。ただし、登記名義人が自然人であるときは、申出があるときに限ります（不動産登記法76条の6）。\n\nこの「申出があるときに限る」は、自然人だけの決まりです。会社法人等番号が登記された法人について、法人の登記簿の情報で住所の変更を確認した場合は、申出がなくても職権で登記できます（不動産登記規則158条の44第1項2号）。本肢は誤りです。\n\n**たとえば**、株式会社が本店を移転して法人の登記簿が書き換わると、登記官がその情報を確認して、会社の不動産の登記記録の住所を職権で直すことができます。'),
        'エ': ('敷地権付き区分建物の保存の登記では、登記原因と日付も登記する',
               '所有権の保存の登記では、登記原因及びその日付を登記することを要しません。ただし、敷地権付き区分建物について、区分建物の表題部所有者から所有権を取得した者が申請する保存の登記（74条2項）をする場合は、この限りではありません（不動産登記法76条1項）。\n\n問題文は「登記原因及びその日付は登記されない」としていますが、このただし書の場合は登記されます。本肢は誤りです。\n\n**たとえば**、分譲マンションの新築で、売主が表題部所有者として表題登記をされた後、その部屋を買った人が直接、自分名義の保存の登記を申請する場合です。このときは、登記原因とその日付が登記されます。'),
        'オ': ('申請義務違反の通知は、催告しても申請がないときに限る',
               '登記官は、相続登記や住所等の変更の登記の申請義務に違反した者がいることを職務上知ったときでも、相当の期間を定めて申請を催告し、その期間内に申請がされないときに限り、遅滞なく管轄地方裁判所にその事件を通知します（不動産登記規則187条1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、住所を移したまま登記をしていない所有者がいることを登記官が知ったとします。登記官はまず期間を決めて申請を促し、それでも申請されないときに、裁判所へ通知します。通知をするかどうかを決めるのは、過料の手続のためです（過料の上限は、相続登記が十万円、住所等の変更の登記が五万円。同法164条）。'),
    },
    summary=[
        ('ア', '誤', '相続登記の三年は、死亡の日ではなく、相続の開始と所有権の取得を知った日から数える'),
        ('イ', '正', '住所の変更の登記は、変更があった日から二年以内に申請する'),
        ('ウ', '誤', '申出が必要なのは自然人だけ。法人は、法人の登記簿の情報で確認できれば、申出がなくても職権で登記できる'),
        ('エ', '誤', '敷地権付き区分建物の保存の登記（74条2項）では、ただし書により登記原因及びその日付を登記する'),
        ('オ', '正', '申請義務違反の通知は、催告をしても期間内に申請がないときに限る'),
    ],
    summary_tail='アは「起算日のすり替え」、ウは「申出が必要な範囲のすり替え」、エは「ただし書の見落とし」の出題です。数字は、相続登記が三年、住所等の変更が二年と、数え始めの日と一緒に覚えましょう。',
    supplements=[
        '### 補足説明（ア・イ）：申請義務の期間と数え始め\n\n申請義務のある登記は、期間だけでなく、「いつから数えるか」が場面ごとに違います。\n\n- 相続で所有権を取得したとき：相続の開始と所有権の取得を知った日から三年以内（76条の2第1項）。\n- 遺産分割で法定相続分を超えて取得したとき：遺産分割の日から三年以内（同条2項）。\n- 氏名・名称や住所に変更があったとき：変更があった日から二年以内（76条の5）。\n\n**たとえば**、父の死亡を5月1日に知った子は5月1日から三年、その子が令和8年6月1日に引っ越したのであれば、住所変更の二年は6月1日から数えます。同じ人でも、登記ごとに別々の期限が進みます。',
        '### 補足説明（ウ）：職権で住所の変更の登記ができる場合\n\n登記官が職権で住所等の変更の登記をするとき、登記名義人が自然人か法人かで、申出の要否が変わります（76条の6）。\n\n- 自然人：申出があるときに限り、職権で登記できる。\n- 法人（会社法人等番号が登記されたもの）：法人の登記簿の情報で住所の変更を確認すれば、申出がなくても職権で登記できる（規則158条の44第1項2号）。\n\n**たとえば**、個人の所有者が引っ越した場合は、本人が申出をして初めて登記官が職権で動けます。会社が本店を移転した場合は、会社が何もしなくても、登記官が法人の登記簿の情報を確認して住所を直せます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第15日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法74条、76条、76条の2、76条の5、76条の6、164条、不動産登記規則158条の44、187条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの具体例（遠方の子が後から知った場合）、ウの具体例（本店移転）、エの具体例（分譲マンションの購入者の保存の登記）は、条文の文言から導いた一般的な説明です。個別の運用・先例の確認はしていません。',
        'オの「通知をするのは過料の手続のため」という説明は、不動産登記規則187条1号が不動産登記法164条の過料を前提としていることからの整理です。',
    ],
    phrases=['相続登記の三年は知った日から数えます', '住所の変更は二年以内に登記です', '法人の住所変更は職権でもできます', '区分建物の保存登記は原因も登記します', '催告しても申請がないときだけ通知です'],
    header=dict(t1='三年と二年、', t2='数え始めは？', topic='不動産登記法　申請義務',
                kanji='三・年・数・登・記・申・請・義・務'),
    poster_intro='申請義務に関する決まりを、「申請の期限」（グループA：ア・イ）と「登記官の扱い」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='申請義務と職権登記を整理', sub='不動産登記法 第76条〜第76条の6（毎日ドリル 第15日）',
        col_a='申請の期限', col_b='登記官の扱い', n_a=2,
        cards=[
            dict(h='相続は知った日から三年以内',
                 ill='a horizontal timeline. On the left a faded gray flag with no label; further right a second flag labeled 「知った日」. A green bracket labeled 「三年以内」 starts at the second flag and extends to the right. A green check mark sits beside the bracket.',
                 words=['知った日', '三年以内'], tag='起算日は知った日'),
            dict(h='住所の変更は二年以内',
                 ill='an isometric house on the left and a second house on the right, with a thin arrow between them. A flag labeled 「変更の日」 stands beside the left house, and a calendar page labeled 「二年以内」 sits above the arrow. A green check mark sits beside the right house.',
                 words=['変更の日', '二年以内'], tag='変更の日から'),
            dict(h='法人は申出がなくても職権で',
                 ill='an isometric company building with a registry officer figure beside it, pressing a round stamp labeled 「職権」 onto a record sheet. A green check mark sits beside the stamp.',
                 words=['職権'], tag='法人は申出が要らない'),
            dict(h='区分建物の保存登記は原因も登記',
                 ill='an isometric apartment building next to a record sheet that has two lines, labeled 「原因」 and 「日付」. A green check mark sits beside the record sheet.',
                 words=['原因', '日付'], tag='原因と日付を登記'),
            dict(h='催告しても申請がなければ通知',
                 ill='a registry officer figure handing a notice sheet labeled 「催告」 to a person, and further right a courthouse building labeled 「地方裁判所」 with a thin arrow pointing to it. A green check mark sits beside the courthouse.',
                 words=['催告', '地方裁判所'], tag='催告のあとに通知'),
        ],
        kanji='申・請・義・務・相・続・知・年・内・住・所・変・更・法・人・職・権・原・因・日・付・催・告'.split('・')),
    nb_label='ア・イ・ウ肢', nb_intro='ア・イ・ウの補足説明に合わせた2枚です。1枚目は、申請義務の期間と数え始めを表で整理します。2枚目は、職権で住所の変更の登記ができる場合を、自然人と法人の左右の対比で示します。',
    notebooks=[
        dict(name='申請義務の期間と数え始め', args=dict(
            title='三年と二年、いつから数える？', sub='相続登記と住所等の変更の登記（毎日ドリル 第15日 ア・イ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 3 columns and 3 data rows, plus a header row. The column headers are exactly: 場面 / 期間 / 数え始め. Each row has a small isometric icon beside the first cell.
Row 1: first cell 相続で取得 (icon: a house with a family figure); second cell 三年以内; third cell 相続の開始と取得を知った日.
Row 2: first cell 遺産分割で相続分を超えて取得 (icon: a document with a split line); second cell 三年以内; third cell 遺産分割の日.
Row 3: first cell 住所や氏名の変更 (icon: a moving box beside a house); second cell 二年以内; third cell 変更があった日.
Use exactly these strings, and no others, for the cell text. The three 数え始め cells are different strings; draw each of them in a different accent color (blue, green and orange).""",
            callout='相続登記の三年は、死亡の日ではなく、相続の開始と所有権の取得を知った日から数えます。\n住所や氏名の変更の二年は、変更があった日から数えます。',
            footer='不動産登記法76条の2、76条の5',
            kanji='相・続・取・得・遺・産・分・割・住・所・氏・名・変・更・期・間・数・知・日・年・内・開・始'.split('・'), what='table',
            check='confirm the table has exactly 3 columns and 3 data rows, and confirm the three cells in the 数え始め column are different strings drawn in different accent colors, ')),
        dict(name='職権で住所の変更の登記ができる場合', args=dict(
            title='職権の登記、申出は必要？', sub='自然人と法人の違い（毎日ドリル 第15日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings, 「自然人」 on the left and 「法人」 on the right. Draw them in different accent colors (blue and green) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 自然人
Scene: an isometric scene of a person figure holding a sheet labeled 「申出」, handing it to a registry officer figure at a counter.
Result badge: 申出があるときに限る

RIGHT PANEL (green accent):
Panel header: 法人
Scene: an isometric scene of a company building and a registry officer figure who checks a record sheet and presses a round stamp labeled 「職権」. No person figure hands over any sheet.
Result badge: 申出がなくても職権で""",
            callout='申出があるときに限るのは、登記名義人が自然人のときだけです。\n会社法人等番号が登記された法人は、法人の登記簿の情報で住所の変更を確認できれば、申出がなくても登記官が職権で登記できます。',
            footer='不動産登記法76条の6、不動産登記規則158条の44',
            kanji='自・然・人・法・申・出・職・権・限'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (自然人 on the left and 法人 on the right) drawn in different accent colors, ')),
    ],
)
