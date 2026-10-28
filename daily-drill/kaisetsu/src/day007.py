def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='表題登記がない土地は、取得から一月以内',
    intro='土地の表示に関する登記について、登記事項、地番、表題登記の期限、所有者の氏名の載る場所を問う問題です（不動産登記法27条・34条から36条まで）。\n\nこの記事では、土地の表題登記を申請する期限と、所有者の氏名と住所が「表題部」に載る場合と「権利部」に載る場合の違いを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('土地の登記事項には、所在・地番・地目・地積がある',
               '土地の表示に関する登記の登記事項には、土地の所在する市、区、郡、町、村及び字、地番、地目、地積があります（不動産登記法34条1項1号から4号まで）。\n\n本肢は正しいといえます。\n\n**たとえば**、ある土地を特定するときは、「どこにあるか（所在）」「何番か（地番）」「何に使われているか（地目）」「どれだけの広さか（地積）」の四つを登記記録で確認できます。'),
        'イ': ('地番は、登記所が一筆の土地ごとに付ける',
               '登記所は、法務省令で定めるところにより、地番を付すべき区域を定め、一筆の土地ごとに地番を付さなければなりません（不動産登記法35条）。\n\n本肢は正しいといえます。\n\n**たとえば**、ある町の中で、一筆ごとに「1番」「2番」と番号が付けられているのは、登記所が決めた番号です。住所の「丁目・番・号」とは別のものです。'),
        'ウ': ('新たに生じた土地は、所有権の取得から一月以内に表題登記',
               '新たに生じた土地又は表題登記がない土地の所有権を取得した者は、その所有権の取得の日から一月以内に、表題登記を申請しなければなりません（不動産登記法36条）。\n\n本肢は正しいといえます。\n\n**たとえば**、海の一部を埋め立てて新しい土地ができ、その所有権を取得した人は、取得の日から一月以内に、その土地の表題登記を申請します。'),
        'エ': ('表題登記がない土地の期限は、二月ではなく一月',
               '表題登記がない土地の所有権を取得した者の申請期限は、取得の日から「一月以内」です（不動産登記法36条）。\n\n問題文は「二月以内」としているので、本肢は誤りです。\n\n**たとえば**、これまで一度も登記されたことのない山林を買った人は、買った日から一月以内に表題登記を申請します。二月まで待てるわけではありません。'),
        'オ': ('所有権の登記がある土地は、所有者の氏名を表題部に載せない',
               '土地の表示に関する登記の登記事項のうち、所有者の氏名又は名称及び住所は、所有権の登記がない不動産についてのものです（不動産登記法27条3号）。\n\n問題文は、所有権の登記がある不動産についても、所有者の氏名等が登記されるとしています。本肢は誤りです。\n\n**たとえば**、売買で買主の名前で所有権の登記がされた土地は、買主の氏名と住所が権利部に載ります。表題部に所有者として載せるのは、所有権の登記がされる前の段階の土地です。'),
    },
    summary=[
        ('ア', '正', '土地の登記事項には、所在・地番・地目・地積がある'),
        ('イ', '正', '地番は、登記所が一筆の土地ごとに付ける'),
        ('ウ', '正', '新たに生じた土地の所有権を取得した者は、取得の日から一月以内に表題登記を申請する'),
        ('エ', '誤', '表題登記がない土地の所有権を取得した者の期限は、二月ではなく一月以内'),
        ('オ', '誤', '所有者の氏名又は名称及び住所が表示に関する登記の登記事項になるのは、所有権の登記がない不動産'),
    ],
    summary_tail='エは期間の数字を入れ替えた出題、オは「所有権の登記がない不動産」という限定を外した出題です。期限は一月、所有者の氏名が表題部に載るのは所有権の登記がない土地だけ、と押さえましょう。',
    supplements=[
        '### 補足説明（エ）：土地の登記の期限は、どれも一月以内。数え始めが違う\n\n土地の登記で、一月以内の申請が求められる主な場面を並べます。\n\n| 場面 | 期限の数え始め | 条文 |\n|---|---|---|\n| 新たに生じた土地、表題登記がない土地 | 所有権の取得の日 | 36条 |\n| 地目や地積の変更 | 変更があった日 | 37条1項 |\n| 土地の滅失 | 滅失の日 | 42条 |\n\n**たとえば**、登記されたことのない山林を買った人は、買った日から一月以内に表題登記を申請します。数え始めは、買った日、つまり所有権を取得した日です。',
        '### 補足説明（オ）：所有者の氏名は、表題部か権利部のどちらかに載る\n\n登記記録は、表題部と権利部に分けて作られます（不動産登記法12条）。所有者の氏名の載る場所は、所有権の登記があるかないかで決まります。\n\n| | 所有者の氏名・住所が載る場所 |\n|---|---|\n| 所有権の登記がない土地 | 表題部（表示に関する登記の登記事項） |\n| 所有権の登記がある土地 | 権利部の甲区（所有権に関する登記） |\n\n**たとえば**、表題登記だけがされた土地では、表題部に「所有者」として氏名と住所が載ります。その後に所有権の保存の登記がされると、所有者は権利部の甲区に載ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第7日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法12条、27条3号、34条1項、35条、36条は、`note-articles/laws/` 配下の原文で確認しました。権利部の甲区に所有権に関する登記が記録されることは、不動産登記規則4条4項の原文で確認しました。',
        'イの具体例（住所の丁目・番・号との違い）は、条文からの一般的な整理です。',
        '補足説明（オ）の「表題登記だけの段階では表題部に所有者が載る」「所有権の保存の登記後は甲区に載る」は、27条3号と不動産登記規則4条4項の文言からの整理で、記録の細かな方法までは確認していません。',
    ],
    phrases=['土地の登記事項は四つあります', '地番は登記所が付けます', '新しい土地も一月以内に表題登記です', '二月ではなく一月以内なんです', '所有権の登記がある土地は権利部に載ります'],
    header=dict(t1='表題登記は、', t2='いつまでに？', topic='不動産登記法　土地の表示に関する登記',
                kanji='表・題・登・記・土・地・毎'),
    poster_intro='土地の表示に関する登記を、「土地の登記事項と地番」（グループA：ア・イ）と「表題登記の期限と所有者の記録」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='土地の表示に関する登記を整理', sub='不動産登記法 第27条・第34条から第36条まで（毎日ドリル 第7日）',
        col_a='登記事項と地番', col_b='表題登記と所有者の記録', n_a=2,
        cards=[
            dict(h='土地の登記事項は所在・地番・地目・地積',
                 ill='a record sheet with four rows, each row with a small icon: a map pin, a number plate, a field, and a ruler. Labels beside the icons are 「所在」, 「地番」, 「地目」 and 「地積」. A green check mark sits beside the sheet.',
                 words=['所在', '地番', '地目', '地積'], tag='登記事項は四つ'),
            dict(h='地番は登記所が一筆ごとに付ける',
                 ill='an isometric row of three land plots in a line, each with a number plate in front. A registry officer figure carrying a name tag 「登記所」 attaches the plates. A green check mark sits beside the officer.',
                 words=['登記所'], tag='一筆ごとに'),
            dict(h='新たに生じた土地も一月以内に表題登記',
                 ill='an isometric newly formed land plot rising from the sea, with a calendar page labeled 「一月以内」 beside it and a form labeled 「表題登記」. A green check mark sits beside the calendar.',
                 words=['一月以内', '表題登記'], tag='取得の日から'),
            dict(h='表題登記がない土地も一月以内',
                 ill='an isometric untouched land plot without a registry sign, with a buyer figure holding a form labeled 「表題登記」 and a calendar page labeled 「一月以内」. A green check mark sits beside the calendar.',
                 words=['表題登記', '一月以内'], tag='期限は一月'),
            dict(h='所有権の登記がある土地は権利部に載る',
                 ill='a registry record divided into two parts. The upper part is labeled 「表題部」 and the lower part is labeled 「権利部」. A name plate of an owner sits in the lower part. A green check mark sits beside the lower part.',
                 words=['表題部', '権利部'], tag='氏名は権利部'),
        ],
        kanji=kj('土地登記事項所在地番目積一月表題部権利部取得')),
    nb_label='エ・オ肢', nb_intro='エ・オの補足説明に合わせた2枚です。1枚目は、土地の表題登記の期限を時間の流れで示します。2枚目は、所有者の氏名が載る場所を左右の対比で示します。',
    notebooks=[
        dict(name='土地の表題登記の期限', args=dict(
            title='表題登記は、取得から一月以内', sub='不動産登記法36条（毎日ドリル 第7日 エ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline. A single axis runs left to right with two flags.

Left flag labeled 所有権の取得の日, with an icon of a buyer figure receiving a land plot.
Right flag labeled 一月後, with an icon of a calendar page.
A green bracket spans from the left flag to the right flag, labeled 一月以内に表題登記を申請.

Below the axis, two small boxes side by side, each with an icon:
Box 1: 新たに生じた土地 (a land plot rising from the sea)
Box 2: 表題登記がない土地 (a land plot with no registry sign)
Both boxes have the same bracket label: 一月以内.""",
            callout='新たに生じた土地も、表題登記がない土地も、所有権を取得した人は、取得の日から一月以内に表題登記を申請します。\n期限は二月ではなく一月です。',
            footer='不動産登記法36条',
            kanji=kj('所有権取得一月表題登記申請土地'), what='timeline',
            check='confirm the single green bracket reads 一月以内に表題登記を申請 and that both lower boxes show the same label 一月以内, ')),
        dict(name='所有者の氏名が載る場所', args=dict(
            title='所有者の氏名は、どこに載る？', sub='表題部と権利部（毎日ドリル 第7日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「所有権の登記がない」 on the left and 「所有権の登記がある」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 所有権の登記がない
Scene: a record sheet whose upper part labeled 表題部 holds a name plate of an owner.
Label under the scene: 所有者の氏名と住所は表題部に載る

RIGHT PANEL (green accent):
Panel header: 所有権の登記がある
Scene: a record sheet whose lower part labeled 権利部 holds a name plate of an owner.
Label under the scene: 所有者の氏名と住所は権利部に載る""",
            callout='所有者の氏名又は名称及び住所が表示に関する登記の登記事項になるのは、所有権の登記がない不動産です。\n所有権の登記がある土地では、所有者は権利部に記録されます。',
            footer='不動産登記法12条、27条3号',
            kanji=kj('所有権登記表題部氏名住所載'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
    ],
)
