def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='合併できない場合と、できる例外',
    intro='二つの建物を一つにする「建物の合併の登記」と、一つの建物を分ける「建物の区分の登記」について、「どんなときにできないか」「だれが申請できるか」「登記記録はどう扱われるか」を問う問題です（不動産登記法30条・56条、不動産登記規則129条・131条）。\n\nこの記事では、合併の制限とその例外、相続人による申請、そして区分の登記で登記記録がどう扱われるかを、具体的な場面で確認していきましょう。この問題は「正しいもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('所有権の登記名義人が違う建物は、合併できない',
               '表題部所有者又は所有権の登記名義人が相互に異なる建物の合併の登記は、することができません（不動産登記法56条2号）。\n\n甲建物はAだけ、乙建物はAとBの共有ですから、所有権の登記名義人が相互に異なります。したがって、乙建物を甲建物の附属建物とする合併の登記はできません。本肢は正しいといえます。\n\n**たとえば**、自分だけの名義の母屋と、兄弟で共有している離れを、一つの建物にまとめたいと思っても、名義人が違うので、そのままでは合併の登記はできません。'),
        'イ': ('同一の抵当権の登記なら、例外として合併できる',
               '所有権等の登記以外の権利に関する登記がある建物は、原則として合併の登記ができません（不動産登記法56条5号）。ただし、法務省令で定める登記は例外です。担保権の登記であって、登記の目的、申請の受付の年月日及び受付番号並びに登記原因及びその日付が同一のものは、合併の登記をすることができます（不動産登記規則131条1号）。\n\n問題文は、同一の抵当権の登記があるのに合併できないとしています。例外を見落としているので、本肢は誤りです。\n\n**たとえば**、甲建物と乙建物に、同じ銀行の、同じ日に受け付けられた、同じ原因の抵当権の登記があるときは、合併の登記をすることができます。'),
        'ウ': ('賃借権の登記は、内容が同じでも合併できない',
               '合併後の建物の登記記録に登記できる例外は、規則131条が挙げる二つだけです。一つは同一の担保権の登記、もう一つは登記事項が同一の信託の登記です。\n\n賃借権は担保権ではありませんから、この例外に当たりません。内容が同一の賃借権の設定の登記が両方の建物にあっても、合併の登記はできません（不動産登記法56条5号）。問題文は「できる」としているので、本肢は誤りです。\n\n**たとえば**、甲建物と乙建物の両方に、同じ内容で、同じ人を賃借人とする賃借権の登記があっても、合併することはできません。抵当権のような例外は、賃借権には広がりません。'),
        'エ': ('相続人は、相続登記をしなくても、合併の登記を申請できる',
               '表題部所有者又は所有権の登記名義人が表示に関する登記の申請人となることができる場合に、その人について相続その他の一般承継があったときは、相続人その他の一般承継人が、その登記を申請することができます（不動産登記法30条）。建物の合併の登記は、表示に関する登記です。\n\n相続による所有権の移転の登記を先にしておく必要はありません。本肢は正しいといえます。\n\n**たとえば**、父名義の甲建物と乙建物が並んでいて、父が亡くなったとします。相続人である子は、相続の登記を済ませる前でも、2つの建物を合併する登記を申請することができます。'),
        'オ': ('区分建物でない建物を区分すると、元の記録は閉鎖される',
               '区分建物でない甲建物を区分して、甲建物と乙建物にするときは、区分後の各建物について、新たに登記記録を作成します（不動産登記規則129条1項）。区分前の甲建物の登記記録は、閉鎖されます（同条2項）。\n\n問題文は、甲建物の登記記録をそのまま用い、乙建物についてのみ新たに作成するとしているので、本肢は誤りです。\n\n**たとえば**、1軒の二世帯住宅を、玄関も別々にして、2つの建物に区分したとします。区分後の2つの建物それぞれに新しい登記記録が作られ、区分前の1軒分の登記記録は閉鎖されます。'),
    },
    summary=[
        ('ア', '正', '所有権の登記名義人が相互に異なる建物は、合併の登記ができない'),
        ('イ', '誤', '登記の目的・受付・原因などが同一の担保権の登記は、例外として、合併の登記ができる'),
        ('ウ', '誤', '賃借権の登記は例外に当たらず、内容が同一でも合併の登記ができない'),
        ('エ', '正', '所有権の登記名義人の相続人は、相続登記をしなくても、合併の登記を申請できる'),
        ('オ', '誤', '区分建物でない建物を区分するときは、区分後の各建物に新しい登記記録を作り、元の記録は閉鎖する'),
    ],
    summary_tail='イとウは、合併の制限の「例外が担保権と信託だけ」という点を問う、対になる出題でした。オは、区分建物でない建物の区分と、区分建物の区分の取り違えを狙っています。',
    supplements=[
        '### 補足説明（イ・ウ）：権利の登記がある建物は、合併できるか\n\n所有権等の登記以外の権利の登記がある建物は、原則として合併の登記ができません（不動産登記法56条5号）。例外は、規則131条が定める二つだけです。\n\n| 建物にある登記 | 合併の登記 |\n|---|---|\n| 同一の担保権の登記（登記の目的、受付の年月日及び受付番号、登記原因及びその日付が同一） | できる |\n| 登記事項が同一の信託の登記 | できる |\n| 内容が同一の賃借権の登記 | できない |\n| 同一でない担保権の登記 | できない |\n\n**たとえば**、甲建物にも乙建物にも同じ銀行の同じ抵当権の登記があれば合併できますが、受付の日が違う抵当権が付いている場合や、賃借権が付いている場合は、合併できません。',
        '### 補足説明（オ）：建物の区分で、登記記録はどうなるか\n\n建物の区分の登記は、区分する建物が区分建物かどうかで、登記記録の扱いが変わります。\n\n| 区分する建物 | 新しく作る登記記録 | 区分前の登記記録 |\n|---|---|---|\n| 区分建物でない甲建物 | 区分後の甲建物・乙建物の両方 | 閉鎖される（規則129条1項・2項） |\n| 区分建物である甲建物 | 乙建物だけ | 残る（規則129条3項・4項） |\n\n**たとえば**、一戸建ての二世帯住宅を2つに区分するときは、2つとも新しい登記記録になり、元の記録は閉鎖されます。すでにマンションの一室として登記されている部屋を、さらに2部屋に区分するときは、新しい部屋の分だけ記録を作り、元の部屋の記録は残ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第78日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法30条、56条、不動産登記規則129条、131条は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの「建物の合併の登記は表示に関する登記である」という説明は、法54条が表示に関する登記の款に置かれていることからの一般的な整理です。',
        '具体例（母屋と離れ、二世帯住宅、同じ銀行の抵当権など）は、条文の文言を日常の場面にかみ砕いた説明で、個別の登記実務の確認はしていません。',
    ],
    phrases=['名義人が違う建物は合併できません', '同一の抵当権なら合併できます', '賃借権があると合併できません', '相続登記の前でも合併を申請できます', '区分すると元の記録は閉鎖されます'],
    header=dict(t1='合併できる？', t2='できない？', topic='不動産登記法　建物の合併と区分',
                kanji='合・併・建・物・区・分・法・毎'),
    poster_intro='建物の合併と区分を、「合併の制限と例外」（グループA：ア・イ・ウ）と「申請人と区分の記録」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の合併と区分を整理', sub='不動産登記法 第30条・第56条（毎日ドリル 第78日）',
        col_a='合併の制限と例外', col_b='申請人と区分の記録', n_a=3,
        cards=[
            dict(h='名義人が違うと合併できない',
                 ill='two buildings side by side. The left building has a name tag showing one owner figure, and the right building has a name tag showing two owner figures. A thick gray barrier line runs between the two buildings.',
                 words=['名義人'], tag='名義人は同じこと'),
            dict(h='同じ抵当権なら合併できる',
                 ill='two buildings, each holding an identical mortgage sheet labeled 「抵当権」, joined by a green arrow into one larger building. A green check mark sits beside the larger building.',
                 words=['抵当権'], tag='同一なら例外'),
            dict(h='賃借権は例外にならない',
                 ill='two buildings, each holding a lease contract sheet labeled 「賃借権」. A thick gray barrier line runs between the two buildings and no joining arrow is drawn.',
                 words=['賃借権'], tag='内容が同じでも不可'),
            dict(h='相続人も合併を申請できる',
                 ill='an heir figure carrying a name tag labeled 「相続人」 holding a form at a counter, with two buildings standing behind the heir. A green check mark sits beside the heir.',
                 words=['相続人'], tag='相続登記の前でも可'),
            dict(h='区分すると元の記録は閉鎖',
                 ill='one building record sheet turning into two new record sheets side by side. The original sheet is stamped 「閉鎖」 and set aside to the left.',
                 words=['閉鎖'], tag='新しい記録が二つ'),
        ],
        kanji=kj('名義人合併抵当権賃借相続区分記録閉鎖建物', n=22)),
    nb_label='イ・ウ・オ肢', nb_intro='イ・ウ・オの補足説明に合わせた2枚です。1枚目は、権利の登記がある建物が合併できるかを表で示します。2枚目は、区分建物でない建物の区分と区分建物の区分を左右で対比します。',
    notebooks=[
        dict(name='権利の登記がある建物は、合併できるか', args=dict(
            title='権利の登記があると合併は？', sub='不動産登記法56条5号（毎日ドリル 第78日 イ・ウ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and four body rows, in rounded panel style. Each body row carries a small icon at the left edge (a mortgage sheet, a trust document, a lease contract sheet, a mortgage sheet with a different date).
Header row (blue accent), two column headers: 建物にある登記 | 合併の登記
Row 1: 同一の担保権の登記 | できる
Row 2: 登記事項が同一の信託の登記 | できる
Row 3: 内容が同一の賃借権の登記 | できない
Row 4: 同一でない担保権の登記 | できない
Draw the cells in the second column 「できる」 in green and 「できない」 in gray. Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='権利の登記がある建物は、原則として合併できません。\n例外は、同一の担保権の登記と、登記事項が同一の信託の登記だけです。賃借権は例外に入りません。',
            footer='不動産登記法56条5号、不動産登記規則131条',
            kanji=kj('合併建物登記担保権信託賃借権同一', n=14), what='table',
            check='confirm the table has exactly four body rows and that no check mark or cross mark appears, ')),
        dict(name='建物の区分で、登記記録はどうなるか', args=dict(
            title='区分の登記で、記録はどうなる？', sub='不動産登記規則129条（毎日ドリル 第78日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「区分建物でない建物」 on the left and 「区分建物」 on the right. Draw them large and in different accent colors (blue on the left, green on the right) so they can never be confused or duplicated. Do not use check marks or cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物でない建物
Scene: an isometric detached two-family house being split into two houses by a vertical line.
Rows of text:
新しい登記記録: 区分後の二つの建物
区分前の登記記録: 閉鎖される

RIGHT PANEL (green accent):
Panel header: 区分建物
Scene: an isometric apartment block where one room is being split into two rooms by a vertical line.
Rows of text:
新しい登記記録: 新しくできた建物だけ
区分前の登記記録: 残る""",
            callout='区分建物でない建物を区分するときは、区分後の建物すべてに新しい登記記録を作り、元の記録は閉鎖します。\n区分建物を区分するときは、新しくできる建物の分だけ記録を作ります。',
            footer='不動産登記規則129条1項から4項まで',
            kanji=kj('区分建物登記記録閉鎖新後前', n=14), what='panels',
            check='confirm the two panel headers are different strings (区分建物でない建物 on the left and 区分建物 on the right) drawn in different accent colors, ')),
    ],
)
