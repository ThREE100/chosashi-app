D = dict(
    catch='地番だけの誤りなら図面は不要',
    intro='地図又は地図に準ずる図面の訂正について、だれが申出をできるのか、どんな情報を提供するのか、申出が却下されるのはどんなときか、登記官が自分で直せるのか、を問う問題です（不動産登記規則16条）。\n\nこの問題は、誤っている肢の組合せを選ぶ形式です。誤りの内容によって、提供する情報が変わる点に気をつけて確かめていきましょう。',
    sections={
        'ア': ('相続の登記をしていなくても、相続人は申し出られる',
               '地図に表示された土地の区画に誤りがあるときは、表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人は、その訂正の申出をすることができます（不動産登記規則16条1項）。\n\n本肢は正しいといえます。相続の登記をしていなくても、相続人であることを証する情報を提供すれば、相続人Bは申出ができます（同条5項3号）。\n\n**たとえば**、亡くなった父の名義のままで、相続の登記がされていない土地があるとします。相続人である子は、相続があったことを証する公務員作成の書類（戸籍に関する書類など）を提供して、地図の区画の誤りの訂正を申し出ることができます。'),
        'イ': ('共有者の一人からでも、地図訂正の申出ができる',
               '地図の訂正の申出ができるのは、所有権の登記名義人などです（不動産登記規則16条1項）。所有権の登記名義人が複数いる共有の土地でも、共有者の一人から申し出れば足りる、というのが登記実務の扱いです。\n\n本肢は正しいといえます。\n\n**たとえば**、兄Aと弟Bが共有している土地の地図の区画が誤っているとき、Aだけが法務局に申出をしても、受け付けてもらえます。Bの同意書や、AとBの連名の申出にしなくても構いません。'),
        'ウ': ('地番だけの誤りなら、土地所在図や地積測量図は不要',
               '地図又は地図に準ずる図面に表示された土地の区画又は位置若しくは形状に誤りがあるときは、誤りを証する情報に加えて、土地所在図又は地積測量図を提供します（不動産登記規則16条5項2号）。\n\n地番だけに誤りがあるときは、地番の誤りを証する情報（同項1号）を提供すれば足り、土地所在図や地積測量図は求められません。\n\n問題文は、地番の誤りの場合に土地所在図又は地積測量図を提供しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、図面上の地番が書き間違いで、本当は別の番号だったという場合は、書き間違いを示す資料を出せば足ります。土地の形が実際と違うときは、測量して作った図面が要ります。'),
        'エ': ('他の土地の区画も訂正することになるなら、却下される',
               '登記官は、地図又は地図に準ずる図面を訂正することによって、申出に係る土地以外の土地の区画又は位置若しくは形状を訂正すべきこととなるときは、理由を付した決定で、申出を却下しなければなりません（不動産登記規則16条13項6号）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地の持ち主Aが、境界の線を東にずらすように申し出たとします。ところが、東の乙土地の区画も変えないと辻褄が合わない場合、Aの申出だけで訂正を進めることはできず、却下されます。'),
        'オ': ('登記官は、地図の誤りを職権で訂正できる',
               '登記官は、地図等に誤りがあると認めるときは、職権で、その訂正をすることができます（不動産登記規則16条15項）。\n\n問題文は、Aから訂正の申出がない限り、登記官は訂正できないとしているので、本肢は誤りです。\n\n**たとえば**、登記官が現地の調査をしていて、地図の区画に誤りがあると気づいたとします。所有者から申出がなくても、登記官は自分の判断で、地図を訂正できます。'),
    },
    summary=[
        ('ア', '正', '相続人は、相続の登記をしていなくても、相続を証する情報を提供して地図訂正の申出ができる'),
        ('イ', '正', '共有の土地でも、共有者の一人から地図訂正の申出ができる'),
        ('ウ', '誤', '土地所在図又は地積測量図が要るのは区画・位置・形状の誤りのときで、地番だけの誤りでは要らない'),
        ('エ', '正', '訂正すると他の土地の区画等も訂正することになるときは、申出は却下される'),
        ('オ', '誤', '登記官は、地図等に誤りがあると認めるときは、申出がなくても職権で訂正できる'),
    ],
    summary_tail='ウは「地番だけの誤り」と「区画等の誤り」を同じ扱いにした出題、オは「申出がない限り」という条件を付けた出題です。誤りの内容で提供する情報が変わること、申出と職権の両方があることを覚えておきましょう。',
    supplements=[
        '### 補足説明（ウ）：誤りの内容によって、提供する情報が違う\n\n地図訂正の申出では、地図訂正申出情報と併せて、誤りの内容に応じた情報を提供します（不動産登記規則16条5項）。\n\n- どの誤りでも：誤りがあることを証する情報（1号）。\n- 区画、位置又は形状の誤りのとき：加えて、土地所在図又は地積測量図（2号）。\n- 相続人などが申出をするとき：加えて、相続その他の一般承継があったことを証する情報（3号）。\n\n**たとえば**、地番の書き間違いだけなら、書き間違いを示す資料で足ります。土地の形が違うなら、測量した図面が加わります。申出人が相続人なら、相続を証する書類もさらに加わります。',
        '### 補足説明（オ）：申出による訂正と、職権による訂正\n\n地図等の訂正には、申出による場合と、登記官の職権による場合があります（不動産登記規則16条）。\n\n- 申出による訂正：申出人が情報を提供し、登記官が調査して、訂正の必要があると認めるときは、訂正しなければならない（12項）。\n- 職権による訂正：登記官が、地図等に誤りがあると認めるときは、申出がなくても、訂正することができる（15項）。\n\n**たとえば**、所有者が「区画が違う」と申し出てきた場合は、前者です。登記官が自分で調べて誤りに気づいた場合は、申出がなくても、後者の職権による訂正ができます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第118日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則16条1項・5項・12項・13項・15項は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「共有者の一人からでも申出ができる」は、規則16条1項の文言（所有権の登記名義人）からの一般的な整理で、登記実務の扱いです。個別の通達・先例の原文は未確認です。',
        '具体例（相続登記前の土地、兄弟の共有地、境界線をずらす申出、登記官の現地調査）は、条文の文言を日常の場面に置き換えた仮の設定です。',
    ],
    phrases=['相続人も地図訂正を申し出られます', '共有者の一人からでも申出できます', '地番だけの誤りなら図面は要りません', '他の土地の区画も動くなら却下です', '登記官は職権で訂正することもできます'],
    header=dict(t1='地図の誤り、', t2='だれが直す？', topic='不動産登記規則　地図の訂正',
                kanji='地・図・訂・正・規・則・登・記・毎'),
    poster_intro='地図等の訂正を、「申出人と提供する情報」（グループA：ア・イ・ウ）と「却下と職権」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地図等の訂正を整理', sub='不動産登記規則 第16条（毎日ドリル 第118日）',
        col_a='申出人と提供する情報', col_b='却下と職権', n_a=3,
        cards=[
            dict(h='相続人も地図訂正を申し出られる',
                 ill='an isometric land plot on a map sheet. An heir figure carrying a name tag labeled 「相続人」 holds a form and a small document. A green check mark sits beside the heir.',
                 words=['相続人'], tag='相続の登記は不要'),
            dict(h='共有者の一人でも申し出られる',
                 ill='an isometric land plot on a map sheet owned by two co-owner figures. Only one co-owner figure steps forward at a counter holding a form, and the other stands behind. A name tag labeled 「共有者」 is on the figure at the counter. A green check mark sits beside that figure.',
                 words=['共有者'], tag='一人でも申出できる'),
            dict(h='地番だけの誤りなら図面は不要',
                 ill='a map sheet with one plot number circled by a pencil mark. Beside it lies a single document sheet labeled 「地番」. A faded gray stack of drawing sheets sits further away, labeled 「図面」, untouched. A green check mark sits beside the document sheet.',
                 words=['地番', '図面'], tag='図面は形の誤りのとき'),
            dict(h='他の土地も動くなら却下',
                 ill='a map sheet with two neighboring plots. Moving the boundary line of the left plot would also move the right plot, shown by two linked arrows. A registry official figure holds a stamp labeled 「却下」.',
                 words=['却下'], tag='他の土地も動くと却下'),
            dict(h='登記官は職権で訂正できる',
                 ill='a registry official figure at a desk with a magnifying glass over a map sheet, correcting a line with a pencil. A small tag on the desk is labeled 「職権」. A green check mark sits beside the official.',
                 words=['職権'], tag='申出がなくても訂正可'),
        ],
        kanji='相・続・人・共・有・者・地・番・図・面・却・下・職・権'.split('・')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、誤りの内容によって提供する情報が変わることを表で示します。2枚目は、申出による訂正と職権による訂正を左右の対比で示します。',
    notebooks=[
        dict(name='誤りの内容と、提供する情報', args=dict(
            title='訂正の申出で提供する情報', sub='誤りの内容によって変わる（毎日ドリル 第118日 ウ）',
            req='a three-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three data rows and two columns, with a header row. Header row: 誤りの内容 | 提供する情報.
Row 1 (green accent): left cell with a small map icon whose plot number is circled and the label 地番だけの誤り; right cell with a single document icon and the label 誤りを証する情報.
Row 2 (blue accent): left cell with a small map icon whose plot outline is redrawn and the label 区画、位置又は形状の誤り; right cell with two document icons and the label 誤りを証する情報に加えて、土地所在図又は地積測量図.
Row 3 (orange accent): left cell with an heir figure and the label 相続人などが申し出るとき; right cell with the label さらに、相続その他の一般承継を証する情報.
Use exactly these strings, and no others. The three right cells are different strings; draw them in different accent colors.""",
            callout='土地所在図や地積測量図が要るのは、区画、位置又は形状に誤りがあるときです。\n地番だけの誤りでは、誤りを証する情報を提供すれば足ります。',
            footer='不動産登記規則16条5項',
            kanji='誤・内・容・提・供・情・報・地・番・区・画・位・置・形・状・証・図・測・量・相・続・申・出'.split('・'), what='table',
            check='confirm there are exactly three data rows and that the three right cells are different strings in different accent colors, ')),
        dict(name='申出による訂正と、職権による訂正', args=dict(
            title='地図等の訂正の二つの道', sub='申出による訂正と職権による訂正（毎日ドリル 第118日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「申出による訂正」 on the left and 「職権による訂正」 on the right. Draw them in different accent colors (blue and green) so they can never be confused or duplicated. Do not draw any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 申出による訂正
Scene: an owner figure handing a form to a registry official figure at a counter.
Result badge: 調査して、必要があれば訂正しなければならない

RIGHT PANEL (green accent):
Panel header: 職権による訂正
Scene: a registry official figure alone at a desk, looking at a map sheet through a magnifying glass.
Result badge: 申出がなくても、訂正することができる""",
            callout='地図等の誤りは、申出を受けて直す場合のほかに、登記官が誤りに気づいたときに職権で直すこともできます。\n申出がなければ直せない、ということはありません。',
            footer='不動産登記規則16条12項・15項',
            kanji='申・出・訂・正・職・権・調・査・必・要・地・図・登・記'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (申出による訂正 on the left and 職権による訂正 on the right) drawn in different accent colors, and that no check mark or cross mark appears, ')),
    ],
)
