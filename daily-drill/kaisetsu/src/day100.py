def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='表題登記の買主申請は区分建物以外だけ',
    intro='建物の表題登記と表題部の変更の登記について、だれが、いつまでに、どのように申請するのかを問う問題です（不動産登記法47条・51条・52条）。区分建物かどうかで扱いが分かれる点が、ポイントです。\n\nこの記事では、買主が申請できる場合、一月の数え始め、区分建物の特別な扱いを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('区分建物の買主は、自分名義の表題登記を申請できない',
               '新築した建物又は区分建物以外の表題登記がない建物の所有権を取得した者は、その取得の日から一月以内に、表題登記を申請しなければなりません（不動産登記法47条1項）。買って取得した人が申請するのは、区分建物以外の建物です。\n\n甲建物は区分建物なので、買主のBは、自己を表題部所有者とする表題登記を申請できません。本肢は誤りです。\n\n**たとえば**、新築マンションの一室（区分建物）を、表題登記の前に、建てたAさんから買ったBさんは、自分名義の表題登記を申請できません。\n\nBさんは、AさんからBさんへの所有権の移転の登記を受けるか、自己名義で所有権の保存の登記を申請することになります（同法74条2項）。'),
        'イ': ('変更の後に所有権の登記を受けた人は、自分の登記の日から一月',
               '表題部の登記事項について変更があった後に、所有権の登記名義人となった人は、その人に係る所有権の登記があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法51条2項）。\n\nCは、増築の後に所有権の移転の登記を受けています。一月は、増築の日ではなく、Cの所有権の登記があった8月10日から数えるので、本肢は誤りです。\n\n**たとえば**、7月1日に増築があり、8月10日にCさんが所有権の移転の登記を受けたなら、Cさんの一月は8月10日から数えます。増築の時の名義人だったAさんの一月は、7月1日から数えます（同条1項）。'),
        'ウ': ('区分建物になる場合は、表題部の変更と新築の表題登記を併せて申請する',
               '表題登記がある建物（区分建物を除く。）に接続して区分建物が新築され、一棟の建物となったことで、その建物が区分建物になった場合、表題部の変更の登記は、新築した区分建物の表題登記と併せて申請しなければなりません（不動産登記法52条1項）。\n\n本肢は正しいといえます。この場合、Dは、Eに代わって、新築した建物の表題登記を申請することもできます（同条2項）。\n\n**たとえば**、Dさんの一戸建てに接続して、Eさんが別の住戸を新築し、全体が一棟の建物になったとします。Dさんは、自分の建物の変更の登記と、Eさんの住戸の表題登記を、併せて申請します。'),
        'エ': ('一棟の建物の構造の変更は、他の区分建物にも効力が及ぶ',
               '建物が区分建物である場合、一棟の建物の構造などに関する変更の登記は、同じ一棟の建物に属する他の区分建物についてされた変更の登記としての効力を有します（不動産登記法51条5項）。\n\nこの変更の登記がされたときは、登記官が、職権で、他の区分建物についても変更の登記をします（同条6項）。問題文は、他の区分建物の所有者が別に申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、4戸が入った一棟のアパートの構造が変わり、1戸の所有者のFさんが変更の登記を申請して登記されたとします。ほかの3戸の所有者は、自分で同じ申請をする必要はなく、登記官が職権で3戸分も登記します。'),
        'オ': ('区分建物以外の買主は、取得の日から一月以内に表題登記を申請する',
               '新築した建物又は区分建物以外の表題登記がない建物の所有権を取得した者は、その取得の日から一月以内に、表題登記を申請しなければなりません（不動産登記法47条1項）。\n\n己建物は区分建物ではないので、買主のHは、取得の日から一月以内に、表題登記を申請する義務があります。本肢は正しいといえます。\n\n**たとえば**、Gさんが新築した一戸建てを、表題登記の前にHさんが買ったとします。Hさんは、買ってから一月以内に、表題登記を申請しなければなりません。'),
    },
    summary=[
        ('ア', '誤', '区分建物の買主は、自己を表題部所有者とする表題登記を申請できない'),
        ('イ', '誤', '変更の後に所有権の登記名義人となった人の一月は、増築の日ではなく自分の登記の日から数える'),
        ('ウ', '正', '区分建物になった建物の表題部の変更の登記は、新築した区分建物の表題登記と併せて申請する'),
        ('エ', '誤', '一棟の建物の構造の変更の登記は他の区分建物にも効力があり、登記官が職権で登記する'),
        ('オ', '正', '区分建物以外の表題登記がない建物の買主は、取得の日から一月以内に表題登記を申請する'),
    ],
    summary_tail='アは「区分建物かどうか」、イは「起算日」、エは「申請の要否」をすり替えた出題です。区分建物は特別な扱いが多いので、区分建物以外の原則と分けて整理しましょう。',
    supplements=[
        '### 補足説明（ア・オ）：表題登記がない建物を買ったとき\n\n表題登記がない建物を買った人が、自分名義で表題登記を申請できるかは、建物の種類で分かれます。\n\n- 区分建物以外の建物：買主が、取得の日から一月以内に、表題登記を申請する（47条1項）。\n- 区分建物：買主は、自己を表題部所有者とする表題登記を申請できない。\n\n**たとえば**、一戸建てを買ったHさんは、自分で表題登記を申請します。新築マンションの一室を買ったBさんは、表題登記の前なら、建てたAさんを表題部所有者とする表題登記を経て、移転の登記などを受けます。',
        '### 補足説明（イ）：一月の数え始めは、人によって違う\n\n建物の表題部の変更の登記は、だれが申請するかによって、一月の数え始めが変わります。\n\n- 変更があったときの所有権の登記名義人：変更があった日から一月以内（51条1項）。\n- 変更の後に所有権の登記名義人となった人：自分の所有権の登記があった日から一月以内（51条2項）。\n\n**たとえば**、7月1日に増築があり、8月10日にCさんが所有権の移転の登記を受けたとします。売主のAさんは7月1日から一月以内、買主のCさんは8月10日から一月以内です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第100日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法47条1項、51条1項・2項・5項・6項、52条1項・2項、74条2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「区分建物の表題登記は新築した人を表題部所有者とする」という説明は、47条1項が区分建物以外の取得者に限っていることからの一般的な整理です。なお、同法48条の区分建物の表題登記の申請方法は、この記事では扱っていません。',
        'ウの具体例（長屋のように接続した一棟）と、そのほかの人物と場面は、理解のために設けた架空の例です。',
    ],
    phrases=['区分建物の買主名義の表題登記はできません', '変更の後の名義人は自分の登記から一月です', '区分建物になるなら二つの登記を併せて申請です', '一棟の構造の変更は職権で他の区分建物にも', '区分建物以外の買主は一月以内に申請です'],
    header=dict(t1='建物の登記、', t2='いつ、だれが？', topic='不動産登記法　建物の表題登記', kanji=''),
    poster_intro='建物の表題登記と変更の登記を、「申請する人・期間・一括申請」（グループA：ア・イ・ウ）と「職権の変更と取得の義務」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の表題登記を整理', sub='不動産登記法 第47条と第51条と第52条（毎日ドリル 第100日）',
        col_a='申請する人と期間と一括', col_b='職権の変更と取得の義務', n_a=3,
        cards=[
            dict(h='区分建物の買主名義の表題登記はできない',
                 ill='an isometric condominium building with one unit highlighted. A builder figure holds a sheet labeled 「表題登記」, and a buyer figure stands aside holding a faded gray application form. No check mark and no cross mark on this card.',
                 words=['表題登記'], tag='新築した人の名義'),
            dict(h='変更の後の名義人は自分の登記から一月',
                 ill='a horizontal timeline with two flags: the left flag labeled 「増築」 and the right flag labeled 「自分の登記」. A green bracket starts at the right flag and extends to the right. The part of the timeline before the right flag is drawn in gray with no bracket.',
                 words=['増築', '自分の登記'], tag='起算日は自分の登記'),
            dict(h='区分建物になるなら二つの登記を併せて申請',
                 ill='a detached house and a newly built unit connected side by side into one building. Two forms, one labeled 「表題部の変更」 and one labeled 「表題登記」, are clipped together. A green check mark sits beside the clip.',
                 words=['表題部の変更', '表題登記'], tag='併せて申請'),
            dict(h='一棟の構造の変更は職権で他の区分にも',
                 ill='an isometric apartment building with four units. One owner figure holds a form, and thin arrows spread from the form to the other three units, where a registrar figure presses a round stamp labeled 「職権」. A green check mark sits beside the stamp.',
                 words=['職権'], tag='他の区分建物にも効力'),
            dict(h='区分建物以外の買主は一月以内に表題登記',
                 ill='an isometric single-family house, a buyer figure holding a form in front of it, and a calendar page labeled 「一月以内」 beside the buyer. A green check mark sits beside the calendar.',
                 words=['一月以内'], tag='取得の日から数える'),
        ],
        kanji=[]),
    nb_label='ア・イ・オ肢', nb_intro='ア・イ・オの補足説明に合わせた2枚です。1枚目は、表題登記がない建物を買ったときの扱いを、建物の種類で左右に対比します。2枚目は、一月の数え始めが人によって違うことを、時間の流れで示します。',
    notebooks=[
        dict(name='表題登記がない建物を買ったとき', args=dict(
            title='買主は表題登記を申請できる？', sub='区分建物と区分建物以外（毎日ドリル 第100日 ア・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panels must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「区分建物以外」 on the left and 「区分建物」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物以外
Scene: an isometric single-family house, a buyer figure holding an application form, and a calendar page.
Label under the scene: 取得の日から一月以内に買主が申請
Result badge with a green check mark: 買主が申請する

RIGHT PANEL (orange accent):
Panel header: 区分建物
Scene: an isometric condominium building with a buyer figure holding a faded gray application form, and a builder figure holding a sheet.
Label under the scene: 買主名義の表題登記はできない
Result badge with a red cross: 買主は申請できない
Use exactly these strings, and no others, for the labels.""",
            callout='区分建物以外の建物を買った人は、取得の日から一月以内に表題登記を申請します。\n区分建物の買主は、自己を表題部所有者とする表題登記を申請できません。',
            footer='不動産登記法47条1項', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (区分建物以外 on the left and 区分建物 on the right) drawn in different accent colors, and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='一月の数え始めは、人によって違う', args=dict(
            title='変更の登記の一月は、いつから？', sub='建物の表題部の変更（毎日ドリル 第100日 イ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 7月1日 with an icon of a house with an extension, and the right flag labeled 8月10日 with an icon of a deed document being handed to a buyer figure.
Upper lane (blue accent), lane label: 増築の時の名義人. A blue bracket starts at the left flag and extends to the right, labeled 変更の日から一月以内.
Lower lane (green accent), lane label: 変更の後に登記を受けた人. A green bracket starts at the right flag and extends to the right, labeled 自分の登記の日から一月以内.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and green). Do not use any check mark or cross mark.""",
            callout='変更の後に所有権の登記名義人となった人は、変更の日ではなく、自分の所有権の登記があった日から一月以内に申請します。\n増築の時の名義人は、変更の日から数えます。',
            footer='不動産登記法51条1項・2項', kanji=[], what='timeline',
            check='confirm the two lanes have different bracket labels in different accent colors, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
