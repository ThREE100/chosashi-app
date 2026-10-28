def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='建物の合体による登記等を整理', sub='不動産登記法 第49条・第50条（毎日ドリル 第109日）',
    col_a='合体の申請と存続登記', col_b='権利の消滅と表題登記', n_a=3,
    cards=[
        dict(h='持分を取得した人にも、申請の義務がある',
             ill='two small buildings merging into one larger building, and a new owner figure holding a form beside a calendar page labeled 「一月以内」. A green check mark sits beside the calendar.',
             words=['一月以内'], tag='持分の取得の日から'),
        dict(h='主と附属の一体化は、合体ではない',
             ill='a main house and an annex joined by a newly built connecting room, all on one single record sheet. A faded gray merge arrow icon sits aside, unused. A green check mark sits beside the record sheet.',
             words=[], tag='変更の登記で処理'),
        dict(h='賃借権は、存続登記にならない',
             ill='a merged building with a record sheet. A stamp labeled 「抵当権」 sits on the sheet and carries over to the new building with a thin arrow. A faded gray lease contract paper stays outside the building. A green check mark sits beside the stamp.',
             words=['抵当権'], tag='抵当権などは存続'),
        dict(h='抵当証券があれば、証券も提供する',
             ill='a mortgage certificate paper labeled 「抵当証券」 handed together with a consent form to a registry counter by an owner figure. A green check mark sits beside the certificate.',
             words=['抵当証券'], tag='承諾と証券の両方'),
        dict(h='全部が未登記なら、表題登記を申請する',
             ill='two unregistered small buildings merging into one, and an owner figure submitting a form labeled 「表題登記」 at a counter. A green check mark sits beside the form.',
             words=['表題登記'], tag='合体時の所有者'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='合体か、変更か', sub='建物が一つになったとき（毎日ドリル 第109日 イ）',
    req='a side-by-side comparison',
    layout="""IMPORTANT: the two panel headers are different strings and must not be confused: 「別々の二つの建物」 on the left and 「主と附属建物」 on the right. Draw them in different accent colors (blue and orange). This image uses no check marks and no cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 別々の二つの建物
Scene: an isometric scene of two separate houses, each with its own record sheet, joined into one house by a new connecting room.
Registration badge: 合体による登記等

RIGHT PANEL (orange accent):
Panel header: 主と附属建物
Scene: an isometric scene of a main house and an annex that share one single record sheet, joined by a new connecting room.
Registration badge: 建物の表題部の変更""",
    callout='合体は、別々に登記された二つ以上の建物が、一つの建物になる場合です。\n主である建物と附属建物は、もともと一つの建物なので、増築でつながっても合体にはならず、表題部の変更の登記をします。',
    footer='不動産登記法49条・51条',
    what='panels',
    check='confirm the two panel headers are different strings (別々の二つの建物 on the left and 主と附属建物 on the right) and that the two registration badges are different strings, ')
_N2 = dict(
    title='合体前の権利の行き先', sub='存続登記と権利の消滅（毎日ドリル 第109日 ウ・エ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a four-row table with two columns. The two column headers 「合体前の権利」 and 「扱い」 are different strings. Draw the 「合体前の権利」 column in blue and the 「扱い」 column in green so that they cannot be confused. This image uses no check marks and no cross marks.

--- TABLE ---
Row 1: 抵当権と質権と先取特権 | 存続登記にできる
Row 2: 賃借権 | 存続登記にできない
Row 3: 消滅させたい権利 | 権利者の承諾を証する情報を提供
Row 4: 抵当証券が発行された抵当権 | 承諾の情報と抵当証券を提供
Use exactly these strings, and no others.""",
    callout='合体後の建物に引き継げる存続登記は、所有権以外の所有権に関する登記と、先取特権、質権、抵当権の登記です。賃借権は含まれません。\n抵当証券が発行されている抵当権を消すときは、承諾の情報に加えて抵当証券も必要です。',
    footer='不動産登記令別表十三の項、不動産登記規則120条5項',
    what='table',
    check='confirm the table has exactly four rows and two columns with the exact strings, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='合体は別々の建物どうし、主と附属は変更',
    intro='建物の合体による登記等について、誤っているものを選ぶ問題です（不動産登記法47条・49条・50条、不動産登記令別表、不動産登記規則120条）。だれが申請するのか、どんな場合が合体に当たるのか、合体前の権利はどうなるのかが問われています。\n\nこの記事では、合体に当たる場合と当たらない場合の区別を、具体的な場面で確認していきましょう。この問題は、誤っている肢の組合せを選ぶ形です。',
    sections={
        'ア': ('持分を取得した人にも、合体による登記等の申請義務がある',
               '表題登記がない建物と表題登記がある建物が合体したときは、合体後に、表題登記がない建物の所有者から持分を取得した人も、その持分の取得の日から一月以内に、合体による登記等を申請しなければなりません（不動産登記法49条1項1号・3項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Aが所有する未登記の甲建物と、Bが表題部所有者の乙建物が合体し、その後にCが、Aから合体後の建物の持分を取得したとします。Cは、持分を取得した日から一月以内に、合体による登記等を申請します。'),
        'イ': ('主と附属建物が一つになるのは、合体ではない',
               '合体は、二以上の建物が合体して一個の建物となる場合の手続です（不動産登記法49条1項）。主である建物とその附属建物は、もともと一個の建物として一つの登記記録に載っています。\n\n増築で構造上一個の建物になっても、合体による登記等ではなく、建物の表題部の変更の登記で処理します（同法51条）。本肢は誤りです。\n\n**たとえば**、母屋と離れを新しい部屋でつないで一棟にしたとします。母屋と離れは、もともと一つの登記記録に載っている建物なので、「合体」ではなく、床面積などの変更の登記になります。'),
        'ウ': ('賃借権は、存続登記にできない',
               '合体前の建物にある権利のうち、合体後の建物に引き継いで申請できる存続登記は、所有権以外の所有権に関する登記と、先取特権、質権、抵当権の登記です（不動産登記令別表の十三の項申請情報欄）。\n\nこの定めに賃借権は入っていないので、賃借権の設定の登記は存続登記にできません。本肢は正しいといえます。\n\n**たとえば**、甲建物に賃借権の設定の登記があるまま、乙建物と合体したとします。この賃借権の登記を、合体後の建物に引き継ぐように申請することはできません。'),
        'エ': ('抵当証券があれば、承諾の情報だけでなく証券も提供する',
               '合体前の建物の権利を、合体後に消滅させるには、権利者が消滅を承諾したことを証する情報を提供します（不動産登記法50条）。\n\nその権利が、抵当証券の発行されている抵当権であるときは、さらに、その抵当証券も提供する必要があります（不動産登記規則120条5項3号）。問題文は、抵当証券を提供しなくても消滅の登記がされるとしているので、本肢は誤りです。\n\n**たとえば**、抵当証券が発行された抵当権のある建物が合体するとします。抵当権者の承諾の情報だけを付けて申請しても、抵当証券が付いていなければ、消滅の登記はされません。'),
        'オ': ('どちらも未登記の建物が合体したら、合体時の所有者が表題登記を申請する',
               '合体前の建物がいずれも表題登記がない建物のときは、抹消すべき表題部がありません。この場合は、合体時の所有者が、合体の日から一月以内に、合体後の建物の表題登記を申請します（不動産登記法49条2項、47条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、未登記の甲建物と乙建物の所有者が同じで、二つが合体して一棟になったとします。合体した時の所有者が、合体の日から一月以内に、合体後の建物の表題登記を申請します。'),
    },
    summary=[
        ('ア', '正', '合体前の表題登記がない建物の所有者から持分を取得した人にも、取得の日から一月以内の申請義務がある'),
        ('イ', '誤', '主である建物と附属建物は、もともと一個の建物なので、増築で一体になっても合体ではなく変更の登記'),
        ('ウ', '正', '賃借権の登記は、合体後の建物に引き継ぐ存続登記にできない'),
        ('エ', '誤', '抵当証券が発行された抵当権を消すには、承諾の情報に加えて、抵当証券も提供する'),
        ('オ', '正', 'どちらも表題登記がない建物が合体したら、合体時の所有者が、合体の日から一月以内に表題登記を申請する'),
    ],
    summary_tail='イは「合体になる建物の範囲」、エは「提供する書類の数」を入れ替えた出題です。合体は、別々に登記された建物どうしの話だと押さえましょう。',
    supplements=[
        '### 補足説明（イ）：合体なのか、変更なのか\n\n建物が一つになったときは、もともと別々の登記記録かどうかで手続が分かれます。\n\n- 別々の登記記録の二つ以上の建物が一つになった：合体による登記等（法49条）。\n- 主である建物と附属建物が一つになった：建物の表題部の変更の登記（法51条）。\n\n**たとえば**、隣り合う別々の二軒の家を、間をつないで一軒にしたなら合体です。一方、母屋と離れを新しい部屋でつないだなら、もともと一つの登記記録に載っている建物の増築なので、合体ではありません。',
        '### 補足説明（ウ・エ）：合体前の権利は、どうなる？\n\n合体前の建物に権利の登記があるとき、合体後の扱いは権利によって違います。\n\n- 抵当権、質権、先取特権：存続登記にして引き継げる。\n- 賃借権：存続登記にできない。\n- 消滅させたい権利：権利者が承諾したことを証する情報を提供する（法50条）。\n- 抵当証券が発行された抵当権：承諾の情報に加え、抵当証券も提供する（規則120条5項）。\n\n**たとえば**、合体前の建物に抵当権があるなら、そのまま合体後の建物に引き継ぐこともできますし、抵当権者が承諾すれば、消すこともできます。賃借権は、引き継ぐ登記の対象になりません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第109日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法47条、49条、50条、51条、不動産登記令別表十三の項、不動産登記規則120条は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「主である建物と附属建物は、もともと一個の建物なので合体に当たらない」という説明は、49条1項の文言からの一般的な整理です。登記先例の原文は手元になく、未確認です。',
        'ウの「賃借権が存続登記の対象に入らない」ことは令別表十三の項の列挙から確認しました。その理由（賃借権は持分を目的にできない等）は、先例に基づく説明で、原文は未確認のため、本文には書いていません。',
    ],
    phrases=['持分を取得した人にも申請義務があります', '主と附属の一体化は合体ではありません', '賃借権は存続登記にできません', '抵当証券があれば証券も提供します', '全部が未登記なら表題登記を申請します'],
    header=dict(t1='合体になるのは、', t2='どんなとき？', topic='不動産登記法　建物の合体',
                kanji='・'.join(_kj('合体になるのはどんなとき', '不動産登記法建物の合体', '毎', n=8))),
    poster_intro='建物の合体による登記等を、「合体の申請と存続登記」（グループA：ア・イ・ウ）と「権利の消滅と表題登記」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・ウ・エ肢', nb_intro='イ・ウ・エの補足説明に合わせた2枚です。1枚目は、合体と変更の登記の違いを左右の対比で示します。2枚目は、合体前の権利の行き先を表で整理します。',
    notebooks=[
        dict(name='合体か、変更か', args=_N1),
        dict(name='合体前の権利の行き先', args=_N2),
    ],
)
