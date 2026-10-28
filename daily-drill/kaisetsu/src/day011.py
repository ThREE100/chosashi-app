def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='相続人は自分名義で、合体は一つの申請',
    intro='建物の表題登記と、二つの建物が一つになる「合体」による登記等について、だれが何を申請するのかを問う問題です（不動産登記法47条から49条まで）。この問題は、正しいものを選ぶ形です。\n\nこの記事では、相続人が表題登記を申請するときの名義、一棟の区分建物の申請方法、合体したときの所有権の登記と登記識別情報、登録免許税を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('被承継人を表題部所有者とできるのは、区分建物の場合だけ',
               '新築した建物（区分建物以外）の所有権を取得した者は、一月以内に表題登記を申請しなければなりません（不動産登記法47条1項）。被承継人を表題部所有者とする表題登記を相続人が申請できるのは、区分建物を新築した場合に限られます（同条2項）。\n\n本肢の甲建物は区分建物でないので、Bは、Aを表題部所有者とする表題登記を申請できません。本肢は誤りです。\n\n**たとえば**、一戸建てを新築した父Aが登記をする前に亡くなったときは、相続したBが、自分の名義で表題登記を申請します。'),
        'イ': ('区分建物は、一棟の全部を併せて申請し、他の所有者に代わって申請できる',
               '区分建物が属する一棟の建物が新築されたときは、その区分建物の表題登記は、同じ一棟に属する他の区分建物の表題登記と併せて申請します（不動産登記法48条1項）。このとき、区分建物の所有者は、他の区分建物の所有者に代わって申請できます（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、AとBが一室ずつを所有する新築のマンションでは、Aが、Bの部屋の分の表題登記もまとめて申請することができます。'),
        'ウ': ('合体で所有権の登記がある建物が含まれるときは、所有権の登記も併せて申請する',
               '二以上の建物が合体して一個の建物となったときは、合体の日から一月以内に、合体後の建物の表題登記と、合体前の建物の表題部の登記の抹消を申請します（不動産登記法49条1項）。\n\n合体前の建物が、表題登記がない建物と、所有権の登記がある建物のときは、表題登記がない建物の所有者を登記名義人とする所有権の登記も併せて申請しなければなりません（同項後段）。本肢は正しいといえます。\n\n**たとえば**、Aの未登記の建物と、A名義で登記された建物がつながって一つの建物になったときは、合体後の建物について、Aを名義人とする所有権の登記も一緒に申請します。'),
        'エ': ('同じ名義人の建物なら、登記識別情報は一個分で足りる',
               '登記名義人が同一である所有権の登記がある建物の合体による登記等の申請では、合体に係る建物のうち、いずれか一個の建物の所有権の登記名義人の登記識別情報を提供すれば足ります（不動産登記令8条2項2号）。\n\n問題文は、甲建物と乙建物の両方の登記識別情報を提供しなければならないとしています。本肢は誤りです。\n\n**たとえば**、A名義の居宅と物置が合体するときは、居宅の登記識別情報か、物置の登記識別情報の、どちらか一個を出せば足ります。'),
        'オ': ('合体による登記等そのものには、登録免許税がかからない',
               '登録免許税は、登録免許税法の別表第一に掲げる登記等について課されます（登録免許税法2条）。表示に関する登記で別表第一に掲げられているのは、土地の分筆、建物の分割・区分、土地の合筆、建物の合併で、建物の合体による登記等は含まれていません。\n\n問題文は、登録免許税を納付しなければならないとしています。本肢は、合体前の建物がいずれも所有権の登記がある場合を前提に、誤りと整理されます。\n\n**たとえば**、いずれもAの名義で登記されていた居宅と物置が合体したときは、合体後の建物について所有権の登記を新たにしません。課税される登記がないので、納付する税もありません。'),
    },
    summary=[
        ('ア', '誤', '被承継人を表題部所有者とする表題登記を相続人が申請できるのは、区分建物を新築した場合だけ'),
        ('イ', '正', '一棟の区分建物の表題登記は併せて申請し、区分建物の所有者は他の所有者に代わって申請できる'),
        ('ウ', '正', '表題登記がない建物と所有権の登記がある建物が合体したときは、所有権の登記も併せて申請する'),
        ('エ', '誤', '登記名義人が同一なら、いずれか一個の建物の登記識別情報を提供すれば足りる'),
        ('オ', '誤', '合体による登記等は登録免許税法の別表第一に掲げられておらず、課税されない'),
    ],
    summary_tail='アは「区分建物だけ」という範囲をすり替えた出題、エは「一個で足りる」を「両方必要」とした出題です。この問題は正しいものを選ぶ形なので、正解はイとウの組合せになります。',
    supplements=[
        '### 補足説明（ア）：相続人が表題登記を申請するときの名義\n\n建物を新築した人が、表題登記の前に亡くなったときは、建物の種類で名義が変わります。\n\n| 亡くなった人が新築した建物 | 相続人が申請するときの名義 | 条文 |\n|---|---|---|\n| 区分建物以外 | 相続人自身が所有権を取得した者として申請 | 47条1項 |\n| 区分建物 | 被承継人（亡くなった人）を表題部所有者として申請できる | 47条2項 |\n\n**たとえば**、新築の一戸建てを遺して亡くなったAの建物は、相続したBが、自分の名義で表題登記を申請します。マンションの一室だったときは、Aを表題部所有者とする申請も認められます。',
        '### 補足説明（ウ・オ）：合体前の建物の組み合わせと、所有権の登記\n\n合体による登記等のとき、所有権の登記を併せて申請するかどうかは、合体前の建物の組み合わせで決まります（不動産登記法49条1項）。\n\n| 合体前の建物 | 併せて申請する所有権の登記 |\n|---|---|\n| 表題登記がない建物と所有権の登記がある建物 | 表題登記がない建物の所有者を名義人とする所有権の登記 |\n| 表題登記がある建物と所有権の登記がある建物 | 表題登記がある建物の表題部所有者を名義人とする所有権の登記 |\n| いずれも所有権の登記がある建物 | 申請しない |\n\n**たとえば**、いずれも所有権の登記がある居宅と物置が合体したときは、新しい所有権の登記は不要で、課税される登記もありません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第11日（朝）　択一」とし、note の引用の出典欄は空欄にします。この問題は「正しいものの組合せ」を選ぶ形です。',
        '各肢の根拠のうち、不動産登記法47条、48条、49条1項、不動産登記令8条2項2号、登録免許税法2条は、`note-articles/laws/` 配下の原文で確認しました。登録免許税法の別表第一は、収録されている部分で、土地の分筆などの表示に関する登記が課税対象とされていることを確認しました。',
        'オの問題文には、乙建物にも所有権の登記があるかが書かれていません。記事では、甲建物も乙建物もAが所有権の登記名義人である場合として説明しています。乙建物に所有権の登記がなければ、合体後の建物の所有権の登記が併せて申請され、その登記に登録免許税がかかるため、結論が変わります。',
        'ア・イ・エの具体例は、条文をかみ砕いた一般的な例です。',
    ],
    phrases=['相続人は自分の名義で申請します', '区分建物は一棟まとめて申請です', '合体したら所有権の登記も併せて申請です', '登記識別情報は一個分で足ります', '合体の登記そのものは非課税なんです'],
    header=dict(t1='建物が合体したら、', t2='何を申請する？', topic='不動産登記法　建物の表題登記と合体',
                kanji='建・物・合・体・表・題・登・記・毎'),
    poster_intro='建物の表題登記と合体による登記等を、「表題登記の申請」（グループA：ア・イ）と「合体による登記等」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の表題登記と合体を整理', sub='不動産登記法 第47条から第49条まで（毎日ドリル 第11日）',
        col_a='表題登記の申請', col_b='合体による登記等', n_a=2,
        cards=[
            dict(h='相続人は自分の名義で表題登記',
                 ill='an isometric single detached house with a bequest document on the left, and an heir figure on the right holding a form with a name plate labeled 「相続人」. A green check mark sits beside the heir figure.',
                 words=['相続人'], tag='区分建物以外'),
            dict(h='区分建物は一棟の全部を併せて申請',
                 ill='an isometric apartment building with two rooms highlighted, two owner figures in front; one figure holds one form that covers both rooms, with a small arrow to the other figure. A label above the building reads 「併せて申請」. A green check mark sits beside the form.',
                 words=['併せて申請'], tag='代わりに申請できる'),
            dict(h='合体で所有権の登記がある建物があれば併せて申請',
                 ill='an isometric scene of two buildings, one with a registry sign and one without, merging into one building. A form labeled 「所有権の登記」 sits beside the merged building. A green check mark sits beside the form.',
                 words=['所有権の登記'], tag='併せて申請'),
            dict(h='登記識別情報は一個分で足りる',
                 ill='two small keys beside two buildings, with one of the keys highlighted by a green glow and the other drawn faded. A label above the highlighted key reads 「一個」. A green check mark sits beside the highlighted key.',
                 words=['一個'], tag='名義人が同一'),
            dict(h='合体による登記等は課税されない',
                 ill='two buildings merging into one, with a coin icon beside the arrow. The coin icon is drawn faded with a green circle around the arrow showing a free pass. The label beside the arrow reads 「非課税」. A green check mark sits beside the label.',
                 words=['非課税'], tag='別表第一にない'),
        ],
        kanji=kj('相続人表題登記区分建物併申請合体所有権識別情報非課税')),
    nb_label='ア・ウ・オ肢', nb_intro='ア・ウ・オの補足説明に合わせた2枚です。1枚目は、相続人が表題登記を申請するときの名義を左右の対比で示します。2枚目は、合体前の建物の組み合わせと所有権の登記の関係を整理します。',
    notebooks=[
        dict(name='相続人が表題登記を申請するときの名義', args=dict(
            title='相続人は、どの名義で申請する？', sub='不動産登記法47条（毎日ドリル 第11日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「区分建物以外」 on the left and 「区分建物」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物以外
Scene: an isometric single detached house and an heir figure holding a form.
Text row: 相続人自身が所有権を取得した者として申請

RIGHT PANEL (green accent):
Panel header: 区分建物
Scene: an isometric apartment building with one room highlighted and an heir figure holding a form.
Text row: 被承継人を表題部所有者として申請できる""",
            callout='新築した建物の持ち主が登記前に亡くなったとき、区分建物以外の建物は、相続人が自分の名義で表題登記を申請します。\n被承継人を表題部所有者とできるのは、区分建物の場合だけです。',
            footer='不動産登記法47条1項・2項',
            kanji=kj('区分建物以外相続人自身所有権取得者申請被承継表題部'), what='panels',
            check='confirm the two panel headers are different strings drawn in different accent colors, and that no check mark or cross mark appears anywhere, ')),
        dict(name='合体前の建物の組み合わせと所有権の登記', args=dict(
            title='合体したとき、所有権の登記は？', sub='不動産登記法49条1項（毎日ドリル 第11日 ウ・オ）',
            req='a three-row table-like diagram',
            layout="""IMPORTANT: the three row headers are different strings. Draw them in three different accent colors (blue, green, gray) so they can never be confused or duplicated. Do not draw any cross mark or check mark in this image.

--- THREE ROWS ---
Three horizontal rounded rows stacked vertically, each with a left header box, an icon and a right result box.

ROW 1 (blue accent): header 表題登記がない建物と所有権の登記がある建物
Icon: two buildings merging, one with a registry sign and one without.
Result box: 表題登記がない建物の所有者を名義人とする所有権の登記も併せて申請

ROW 2 (green accent): header 表題登記がある建物と所有権の登記がある建物
Icon: two buildings merging, both with a registry sign, one with a name plate.
Result box: 表題登記がある建物の表題部所有者を名義人とする所有権の登記も併せて申請

ROW 3 (gray accent): header いずれも所有権の登記がある建物
Icon: two buildings merging, both with name plates.
Result box: 所有権の登記は申請しない""",
            callout='合体前の建物の組み合わせによって、合体後の建物の所有権の登記を併せて申請するかどうかが決まります。\nいずれも所有権の登記がある建物の合体では、課税される登記がありません。',
            footer='不動産登記法49条1項',
            kanji=kj('表題登記建物所有権名義人併申請合体'), what='table',
            check='confirm the three row headers are three different strings drawn in three different colors, and that no check mark or cross mark appears anywhere, ')),
    ],
)
