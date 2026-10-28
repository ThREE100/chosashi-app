def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


_P = ['表題部所有者の整理', '不動産登記法 第27条・第32条・第33条（毎日ドリル 第95日）', '証明と変更と記録事項', '更正の登記',
      '請負人の証明でも所有権の証拠になる', '所有権を証する情報', '買主は保存登記のあとに移転登記', '保存', '移転', '保存が先、移転があと',
      '共用部分の登記では所有者は記録されない', '共用部分', '所有者は除かれる',
      '真の所有者は承諾を得て更正', '承諾', '承諾があれば申請可', '持分の更正は他の共有者の承諾が要る', '他の共有者の承諾']

D = dict(
    catch='更正は承諾、変更は保存登記が先',
    intro='表題部所有者について、所有権を証する情報、変更の登記、更正の登記を問う問題です（不動産登記法27条・32条・33条）。\n\nこの記事では、「変更」と「更正」の違いと、更正の登記で承諾が必要になる場面を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('建物の所有権を証する情報は、請負人の証明などでもよい',
               '建物の表題登記を申請するとき、表題部所有者となる人の所有権を証する情報には、建築確認と検査があったことを証する情報のほか、建築請負人又は敷地所有者の証明情報、固定資産税の納付証明に係る情報なども当たります（不動産登記事務取扱手続準則87条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Aさんが自分の土地に家を新築したとき、建てた工務店が「Aさんに引き渡しました」と証明した書類や、固定資産税を納めたことを示す証明を、「この家はAさんのものです」という証拠として法務局に出すことができます。'),
        'イ': ('買主が直接、表題部所有者の変更を申請することはできない',
               '表題部所有者又はその持分についての変更は、その不動産について所有権の保存の登記をした後に、所有権の移転の登記の手続をするのでなければ、登記することができません（不動産登記法32条）。\n\n問題文は、買主Bが表題部所有者をAからBとする変更の登記を申請できるとしていますが、実際は、Aの所有権の保存の登記をしたうえで、AからBへの所有権の移転の登記の手続をする順序になります。本肢は誤りです。\n\n**たとえば**、新築後に表題登記だけがされている家を、持ち主のAさんから買ったBさんが、「表題部の持ち主の欄をAからBに書き換えてください」と直接申請することはできません。\n\nAさんの保存登記のあと、AからBへ売買による所有権の移転の登記を受ける流れになります。'),
        'ウ': ('共用部分である旨の登記がある建物は、所有者の氏名と住所が除かれる',
               '所有権の登記がない不動産の所有者の氏名又は名称及び住所は、表示に関する登記の登記事項ですが、共用部分である旨の登記又は団地共用部分である旨の登記がある建物は除かれています（不動産登記法27条3号）。\n\n問題文は、共用部分である旨の登記がある建物の表題部に、所有者の氏名又は名称及び住所が記録されるとしているので、本肢は誤りです。\n\n**たとえば**、規約で共用部分と定められた別棟の集会所に、共用部分である旨の登記がされている場合、その表題部には、所有者の氏名や住所は記録されません。'),
        'エ': ('真の所有者は、表題部所有者の承諾を得て更正を申請できる',
               '表題部所有者が真の所有者と異なる場合に、表題部所有者を直す更正の登記は、その不動産の所有者以外の人は申請できません（不動産登記法33条1項）。所有者が申請するには、今の表題部所有者の承諾が必要です（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、表題部所有者がAさんと記録されているものの、実際にその建物の所有者はBさんだったとします。Bさんは、Aさんの承諾を得れば、表題部所有者をBさんに直す更正の登記を申請できます。Aさんの承諾がなければ、Bさんは申請できません。'),
        'オ': ('持分の更正には、他の共有者の承諾が要る',
               '表題部所有者である共有者の持分の更正の登記は、その共有者以外の人は申請できません（不動産登記法33条3項）。更正の登記をする共有者は、更正によって持分が変わることになる他の共有者の承諾がなければ、申請できません（同条4項）。\n\n問題文は、Dの承諾がなくても単独で申請できるとしているので、本肢は誤りです。\n\n**たとえば**、土地がCさんとDさんの2分の1ずつと記録されているが、実際はCさんが3分の2、Dさんが3分の1だったとします。Cさんの持分を増やす更正は、持分が変わることになるDさんの承諾がなければ、Cさんだけでは申請できません。'),
    },
    summary=[
        ('ア', '正', '建物の所有権を証する情報には、建築請負人の証明情報や固定資産税の納付証明に係る情報も当たる'),
        ('イ', '誤', '表題部所有者の変更は、所有権の保存の登記をした後に、移転の登記の手続によらなければならない'),
        ('ウ', '誤', '共用部分である旨の登記がある建物は、所有者の氏名又は名称及び住所が登記事項から除かれている'),
        ('エ', '正', '真の所有者は、今の表題部所有者の承諾を得て、表題部所有者の更正の登記を申請できる'),
        ('オ', '誤', '共有者の持分の更正は、持分が変わることになる他の共有者の承諾がなければ申請できない'),
    ],
    summary_tail='イは「変更の手順」、オは「承諾の要否」をすり替えた出題です。変更は保存登記が先、更正は承諾が要る、と分けて整理しましょう。',
    supplements=[
        '### 補足説明（イ）：変更と更正は、直し方が違う\n\n表題部所有者の記録を直す方法は、「変更」と「更正」で手順が違います。\n\n- 変更（32条）：所有権の保存の登記をした後に、所有権の移転の登記の手続によって行います。\n- 更正（33条）：真の所有者が、今の表題部所有者の承諾を得て、更正の登記を申請します。\n\n**たとえば**、Aさんの名義で表題登記がされた家を、Bさんが買った場合は、「変更」の場面です。Aさんの保存登記のあとに、AからBへの移転の登記をします。\n\n一方、表題登記のときから本当の所有者はBさんだった場合は、「更正」の場面で、Bさんは、Aさんの承諾を得て更正の登記を申請します。',
        '### 補足説明（エ・オ）：更正で承諾が必要な相手\n\n更正の登記で、だれの承諾が必要かは、更正の種類によって決まります。\n\n- 表題部所有者の更正（33条1項・2項）：申請するのは真の所有者で、承諾するのは今の表題部所有者です。\n- 持分の更正（33条3項・4項）：申請するのは共有者で、承諾するのは持分が変わることになる他の共有者です。\n\n**たとえば**、CさんとDさんが共有する土地の持分の更正で、Dさんの持分が変わるなら、Dさんの承諾が要ります。承諾を得られないまま、Cさんが一人で申請することはできません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第95日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法27条3号、32条、33条と、不動産登記事務取扱手続準則87条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「Aの所有権の保存の登記をしたうえで」という説明は、32条の文言（保存の登記をした後に、移転の登記の手続をする）から導いた一般的な整理です。',
        '「変更」と「更正」の使い分けは、条文からの一般的な整理です。具体例の人物と場面は、理解のために設けた架空の例です。',
    ],
    phrases=['請負人の証明も所有権の証拠になります', '変更の登記は保存登記のあとです', '共用部分の登記は所有者が除かれます', '真の所有者は承諾を得て更正します', '持分の更正は他の共有者の承諾が要ります'],
    header=dict(t1='表題部所有者の、', t2='直し方は？', topic='不動産登記法　表題部所有者',
                kanji='・'.join(kj('表題部所有者の直し方は不動産登記法'))),
    poster_intro='表題部所有者を、「所有権を証する情報・変更の順序・記録事項」（グループA：ア・イ・ウ）と「更正の登記と承諾」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='表題部所有者を整理', sub='不動産登記法 第27条・第32条・第33条（毎日ドリル 第95日）',
        col_a='証明と変更と記録事項', col_b='更正の登記と承諾', n_a=3,
        cards=[
            dict(h='請負人の証明でも所有権の証拠になる',
                 ill='an isometric newly built house with a contractor figure handing a certificate sheet labeled 「証明書」 to an owner figure. A green check mark sits beside the certificate.',
                 words=['証明書'], tag='所有権を証する情報'),
            dict(h='買主は保存登記のあとに移転登記',
                 ill='a horizontal two-step flow. On the left a house with a round stamp labeled 「保存」; an arrow in the middle; on the right a seller figure handing a deed document labeled 「移転」 to a buyer figure. A green check mark sits above the flow.',
                 words=['保存', '移転'], tag='保存が先、移転があと'),
            dict(h='共用部分の登記では所有者は記録されない',
                 ill='a small isometric meeting-room building with a record sheet beside it. The owner line of the record sheet is left blank and drawn in faded gray. A tag on the building is labeled 「共用部分」. No check mark and no cross mark on this card.',
                 words=['共用部分'], tag='所有者は除かれる'),
            dict(h='真の所有者は承諾を得て更正',
                 ill='two figures at a desk: the true owner figure holds a correction form, and the current record-holder figure presses a round approval stamp labeled 「承諾」 on it. A green check mark sits beside the stamp.',
                 words=['承諾'], tag='承諾があれば申請可'),
            dict(h='持分の更正は他の共有者の承諾が要る',
                 ill='on the left a round pie chart split into two equal halves, an arrow in the middle, and on the right a pie chart split into one larger and one smaller part. A round approval stamp labeled 「承諾」 sits beside the smaller part. A green check mark sits beside the stamp.',
                 words=['承諾'], tag='他の共有者の承諾'),
        ],
        kanji=kj(*_P)),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、変更と更正の手順の違いを左右の対比で示します。2枚目は、更正の登記で承諾が必要な相手を表で整理します。',
    notebooks=[
        dict(name='変更と更正は、直し方が違う', args=dict(
            title='変更と更正の直し方', sub='表題部所有者の記録（毎日ドリル 第95日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「変更」 on the left and 「更正」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not use any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 変更
Scene: a vertical two-step flow with a small arrow between the steps. Step one: a house with a round stamp, with the label 所有権の保存の登記. Step two: a seller figure handing a deed document to a buyer figure, with the label 所有権の移転の登記.

RIGHT PANEL (orange accent):
Panel header: 更正
Scene: a vertical flow. Step one: a record sheet with an owner name line crossed out and rewritten, with the label 真の所有者が申請. Step two: a current record-holder figure pressing an approval stamp, with the label 今の表題部所有者の承諾.
Use exactly these strings, and no others, for the labels.""",
            callout='変更は、保存の登記をしたあとに、移転の登記の手続で行います。\n更正は、真の所有者が、今の表題部所有者の承諾を得て申請します。',
            footer='不動産登記法32条・33条',
            kanji=kj('変更と更正の直し方表題部所有者保存登記移転真承諾'), what='panels',
            check='confirm the two panel headers are different strings (変更 on the left and 更正 on the right) drawn in different accent colors, ')),
        dict(name='更正で承諾が必要な相手', args=dict(
            title='更正で承諾が要る人', sub='表題部所有者と持分の更正（毎日ドリル 第95日 エ・オ）',
            req='a two-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and two rows under a header row. Use exactly these strings, and no others.
Header row: 更正の種類 | 申請する人 | 承諾する人
Row 1: 表題部所有者の更正 | 真の所有者 | 今の表題部所有者
Row 2: 持分の更正 | 共有者 | 持分が変わる他の共有者
Next to each row, draw a small icon: row 1 shows two figures at a desk, row 2 shows a pie chart split into two parts. Do not use any check mark or cross mark.""",
            callout='承諾が必要な相手は、更正の種類で決まります。\n表題部所有者の更正は今の表題部所有者、持分の更正は持分が変わる他の共有者です。',
            footer='不動産登記法33条1項から4項まで',
            kanji=kj('更正で承諾が要る人表題部所有者持分申請真共有変わる今'), what='table',
            check='confirm the table has exactly three columns and two data rows with the given strings, ')),
    ],
)
