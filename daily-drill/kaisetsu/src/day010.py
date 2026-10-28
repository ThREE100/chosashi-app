def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='分割に期限はなく、更正は名義人だけ',
    intro='建物の表題部の変更の登記、更正の登記、分割・合併の登記について、「いつまでに」「だれが」申請するのかを問う問題です（不動産登記法51条から54条まで）。\n\nこの記事では、一月以内の義務がある登記とない登記の違い、二つの建物が接続して区分建物になったときの申請方法、更正の登記を申請できる人を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('変更の後に名義人となった者は、自分の登記の日から一月以内',
               '建物の表題部の登記事項について変更があった後に所有権の登記名義人となった者は、その者に係る所有権の登記があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法51条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、5月10日に増築が終わり、6月20日にBへの所有権の移転の登記がされた場合、Bの一月は、増築の日の5月10日ではなく、自分の登記の日の6月20日から数えます。'),
        'イ': ('建物の分割の登記には、一月以内の申請義務がない',
               '建物の分割の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できません（不動産登記法54条1項）。しかし、条文は申請の期間を定めていません。\n\n問題文は、売る契約の日から一月以内に分割の登記を申請しなければならないとしています。本肢は誤りです。\n\n**たとえば**、母屋に登記されている倉庫だけを他人に売る契約をした場合、分割の登記を申請するかどうかは、所有者が決めます。変更の登記のように、契約の日から一月という期限は決まっていません。'),
        'ウ': ('接続して区分建物になったときは、一括して申請し、代わりに申請できる',
               '表題登記がある二以上の建物（区分建物を除く）が、増築その他の工事により相互に接続して区分建物になったときは、表題部の変更の登記の申請は一括してしなければなりません（不動産登記法52条3項）。\n\nこのとき、その一の建物の表題部所有者は、他の建物の表題部所有者に代わって申請できます（同条4項）。\n\n本肢は正しいといえます。\n\n**たとえば**、隣り合う二軒の家を増築でつないで、一棟の二戸の建物にした場合、一方の所有者が、もう一方に代わって申請することもできます。'),
        'エ': ('表題部の更正の登記は、表題部所有者と名義人だけが申請できる',
               '建物の表題部の更正の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法53条1項）。\n\n問題文のBは、買い受けた人ですが、登記記録に表題部所有者としても所有権の登記名義人としても載っていません。申請できないので、本肢は誤りです。\n\n**たとえば**、買った建物の床面積が間違って登記されていると気づいても、買主が名義を得る前には、自分で更正の登記を申請することはできません。'),
        'オ': ('附属建物の分割と別の建物への合併は、一の申請情報でできる',
               '申請情報は、一つの不動産ごとに作るのが原則ですが（不動産登記令4条）、甲建物の附属建物を分割して、それを乙建物の附属建物としようとするときは、分割の登記と合併の登記を一の申請情報で申請できます（不動産登記規則35条2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、母屋に登記されている倉庫を切り離して、同じ所有者の別の建物の附属建物にしたいとき、二つの登記を一つの書面でまとめて申請できます。'),
    },
    summary=[
        ('ア', '正', '変更の後に所有権の登記名義人となった者は、自分に係る所有権の登記があった日から一月以内に変更の登記を申請する'),
        ('イ', '誤', '建物の分割の登記には、申請の期間（一月以内の義務）の定めがない'),
        ('ウ', '正', '接続して区分建物になった二以上の建物の表題部の変更の登記は一括して申請し、一方が他方に代わって申請できる'),
        ('エ', '誤', '表題部の更正の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できない'),
        ('オ', '正', '附属建物を分割して他の建物の附属建物にするときは、分割と合併を一の申請情報で申請できる'),
    ],
    summary_tail='イは、一月以内の義務がある変更の登記と、義務のない分割の登記を取り違えた出題です。エは、実際には買主でも、登記記録に名義がなければ申請できない、という点を問うています。',
    supplements=[
        '### 補足説明（イ）：一月以内の義務がある登記、ない登記\n\n建物の表示に関する登記には、期限が決まっているものと、決まっていないものがあります。\n\n| 登記 | 一月以内の申請義務 | 条文 |\n|---|---|---|\n| 表題部の変更の登記 | あり | 51条1項 |\n| 建物の滅失の登記 | あり | 57条 |\n| 建物の分割・区分・合併の登記 | 条文に定めなし | 54条 |\n\n過料の規定（164条1項）にも、54条は入っていません。\n\n**たとえば**、増築をしたら、所有者は一月以内に変更の登記を申請しなければなりません。しかし、倉庫を切り離すかどうかは所有者の判断に委ねられていて、分割の登記に期限はありません。',
        '### 補足説明（エ）：更正の登記を申請できるのは、登記記録に名義がある人\n\n53条1項は、更正の登記を申請できる人を、登記記録上の表題部所有者又は所有権の登記名義人に限っています。\n\n| 人 | 登記記録上の地位 | 更正の登記の申請 |\n|---|---|---|\n| A | 表題部所有者 | できる |\n| B（買主） | 載っていない | できない |\n\n**たとえば**、BがAから建物を買い受けても、表題部所有者の変更はそのままではできません。Bは、実際の所有者であっても、登記記録に名義が載るまで、自分では更正の登記を申請できません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第10日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法51条1項・2項、52条3項・4項、53条1項、54条1項、57条、164条1項、不動産登記令4条、不動産登記規則35条2号は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「54条に申請の期間の定めがない」は、54条の条文に期間の記載がないことと、過料を定める164条1項に54条が含まれていないことからの整理です。',
        'エの「Bは名義が載るまで申請できない」は、53条1項の文言からの整理です。具体例は条文をかみ砕いた一般的な例で、個別の運用は確認していません。',
    ],
    phrases=['変更の後に名義人になったら自分の登記から', '分割の登記に期限はありません', '接続して区分建物になったら一括して申請です', '更正は登記記録の名義人だけです', '分割と合併は一つの申請でできます'],
    header=dict(t1='建物の変更と更正、', t2='だれが申請？', topic='不動産登記法　建物の表題部',
                kanji='建・物・表・題・部・更・正・毎'),
    poster_intro='建物の表題部の登記を、「変更と接続」（グループA：ア・ウ）と「分割・更正・申請の方法」（グループB：イ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の表題部の登記を整理', sub='不動産登記法 第51条から第54条まで（毎日ドリル 第10日）',
        col_a='変更と接続', col_b='分割・更正・申請の方法', n_a=2,
        cards=[
            dict(h='変更の後に名義人になったら自分の登記から',
                 ill='a horizontal timeline. On the left a flag labeled 「増築」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['増築', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
            dict(h='接続して区分建物になったら一括して申請',
                 ill='two isometric houses side by side joined by a new connecting section into one building. Two owner figures stand in front; one figure holds a form and a small arrow points to the other figure. A label above the building reads 「一括」. A green check mark sits beside the form.',
                 words=['一括'], tag='代わりに申請できる'),
            dict(h='分割の登記に期限はない',
                 ill='an isometric main house and a small storehouse linked by a dotted line. A scissors icon cuts the dotted line. A calendar page beside the scene is drawn in faded gray with no bracket. A green check mark sits beside the scissors.',
                 words=[], tag='期間の定めなし'),
            dict(h='更正の登記は登記記録の名義人だけ',
                 ill='a record sheet with a name plate labeled 「表題部所有者」 held by an owner figure highlighted with a green glow. A faded gray buyer figure stands aside with no name plate. A green check mark sits beside the owner.',
                 words=['表題部所有者'], tag='申請人は限定'),
            dict(h='分割と合併は一の申請情報で申請できる',
                 ill='an isometric main house and a small storehouse being cut apart, and the storehouse then joining another house, drawn as one continuous path. A single form labeled 「一の申請」 sits beside the path. A green check mark sits beside the form.',
                 words=['一の申請'], tag='まとめて申請'),
        ],
        kanji=kj('変更接続一括分割更正登記名義人申請合併表題部所有者増築')),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、一月以内の申請義務のある登記とない登記を左右の対比で示します。2枚目は、更正の登記を申請できる人と、できない人を示します。',
    notebooks=[
        dict(name='一月以内の義務がある登記、ない登記', args=dict(
            title='一月以内の義務があるのは？', sub='建物の表示に関する登記（毎日ドリル 第10日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「一月以内の義務あり」 on the left and 「条文に期間の定めなし」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 一月以内の義務あり
Scene: an isometric house being extended, with a calendar page.
Labels under the scene:
表題部の変更の登記
建物の滅失の登記

RIGHT PANEL (orange accent):
Panel header: 条文に期間の定めなし
Scene: an isometric main house and a small storehouse separated by a scissors icon.
Labels under the scene:
建物の分割の登記
建物の区分の登記
建物の合併の登記""",
            callout='建物の表題部の変更の登記や滅失の登記には、一月以内の申請義務があります。\n分割、区分、合併の登記は、申請できる人が限られているだけで、条文に申請の期間は定められていません。',
            footer='不動産登記法51条、54条、57条',
            kanji=kj('一月以内義務表題部変更滅失分割区分合併条文期間定'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='更正の登記を申請できる人', args=dict(
            title='更正の登記を申請できるのは？', sub='不動産登記法53条1項（毎日ドリル 第10日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「表題部所有者」 on the left and 「買主」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 表題部所有者
Scene: an isometric scene of an owner figure holding a record sheet that shows the owner's name plate, and a form for a corrected floor area.
Result badge with a green check mark: 申請できる

RIGHT PANEL (gray accent):
Panel header: 買主
Scene: an isometric scene of a buyer figure holding a sales contract. The record sheet beside the buyer shows no name plate for the buyer.
Result badge with a red cross: 申請できない""",
            callout='建物の表題部の更正の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できません。\n買い受けても、登記記録に名義が載っていない買主は、自分では申請できません。',
            footer='不動産登記法53条1項',
            kanji=kj('表題部所有者買主更正登記申請名義'), what='panels',
            check='confirm the two panel headers are different strings (表題部所有者 on the left and 買主 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
    ],
)
