D = dict(
    catch='登記できる権利と順位と第三者',
    intro='登記することができる権利、権利の順位、登記がないことを主張することができない第三者について、5つの場面を問う問題です（不動産登記法3条・4条・5条、民法177条）。\n\nこの記事では、似た言葉の取り違えに注意しながら、各肢を具体的な場面で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('留置権は、登記することができる権利に入っていない',
               '登記ができるのは、不動産の表示のほか、所有権、地上権、永小作権、地役権、先取特権、質権、抵当権、賃借権、配偶者居住権、採石権の10の権利についてです（不動産登記法3条）。留置権は、この中に入っていません。\n\n問題文は「留置権の保存の登記を受けることができる」としているので、本肢は誤りです。\n\n**たとえば**、修理代金を払ってもらえない業者が、直した建物を手元に留めておく権利（留置権）を持っていても、その権利を登記簿に載せることはできません。同じ担保の権利でも、先取特権は登記できます。'),
        'イ': ('同じ主登記に付いた付記登記どうしは、前後で順位が決まる',
               '付記登記の順位は、主登記の順位によります。ただし、同じ主登記に付いた付記登記どうしの順位は、その前後によります（不動産登記法4条2項）。\n\n問題文は「互いに同順位となる」としているので、本肢は誤りです。\n\n**たとえば**、抵当権の登記（主登記）に、先に付記1号、後で付記2号が付いたとします。どちらも主登記の順位を基準にしますが、付記1号と付記2号の間では、先にされた付記1号が上位、後の付記2号が下位です。'),
        'ウ': ('強迫で申請を妨げた者は、登記がないことを主張できない',
               '詐欺又は強迫によって登記の申請を妨げた第三者は、その登記がないことを主張することができません（不動産登記法5条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、AがBに甲土地を売ったあと、CがBを脅して、Bが所有権の移転の登記を申請できないようにしました。その後、CがAから甲土地を買ったとしても、CはBに「あなたは登記をしていない」とは言えません。'),
        'エ': ('相手方の原因が自分の原因より後なら、登記がないと主張できる',
               '他人のために登記を申請する義務を負う第三者は、その登記がないことを主張できません。ただし、その登記の登記原因が自己の登記の登記原因の後に生じたときは、主張できます（不動産登記法5条2項）。\n\n本肢では、Cの登記原因は4月1日の売買、Bの登記原因は5月1日の売買です。Bの原因がCの原因の後なので、CはBの登記がないことを主張できます。問題文は「主張することができない」としているので、本肢は誤りです。\n\n**たとえば**、Cが先にAから土地を買っていたのに、Aが後からBにも売り、Cがその登記の申請を頼まれたとします。Cのほうが先に買っているので、Cは自分の権利を主張できます。'),
        'オ': ('背信的悪意者からの転得者は、本人が背信的でなければ保護される',
               '不動産の物権の得喪は、登記をしなければ第三者に対抗できません（民法177条）。背信的悪意者は、この第三者として保護されませんが、その背信的悪意者からさらに買った転得者は、本人が背信的悪意者でない限り、第三者として保護されるというのが判例の考え方です。\n\n本肢は正しいといえます。\n\n**たとえば**、Aが土地をBに売ったのに登記がされないうちに、Aが意地悪な目的のCにも売り、さらにCから普通の買主Dが買って登記を受けたとします。Dは第三者として保護されるので、Bは登記がなければDに対抗できません。'),
    },
    summary=[
        ('ア', '誤', '留置権は、3条に掲げられた登記できる権利に入っておらず、保存の登記は受けられない'),
        ('イ', '誤', '同じ主登記に付いた付記登記どうしの順位は、同順位ではなく、前後による'),
        ('ウ', '正', '強迫によって登記の申請を妨げた第三者は、登記がないことを主張できない'),
        ('エ', '誤', '相手方の登記原因が自分の登記原因の後に生じたときは、登記がないことを主張できる'),
        ('オ', '正', '背信的悪意者からの転得者は、本人が背信的悪意者でなければ第三者として保護される'),
    ],
    summary_tail='アは「似た制度の取り違え」、イは「付記登記相互の順位」、エは「ただし書の見落とし」の出題です。登記できる権利は10個の列挙、第三者は5条と判例の考え方を、分けて覚えましょう。',
    supplements=[
        '### 補足説明（ア）：登記できる権利と、できない権利\n\n3条は、登記ができる権利を10個に限っています。担保の権利でも、登記できるものとできないものがあります。\n\n- 登記できる：所有権、地上権、永小作権、地役権、先取特権、質権、抵当権、賃借権、配偶者居住権、採石権。\n- 登記できない：留置権など、3条に掲げられていない権利。\n\n**たとえば**、同じ「お金を回収するための権利」でも、抵当権や先取特権は登記簿に載せられますが、留置権は載せられません。名前が似ていても、列挙にあるかどうかで判断します。',
        '### 補足説明（エ）：他人のために登記を申請する義務を負う者\n\n5条2項は、他人のために登記を申請する義務を負う人が、登記がないことを主張できないと定めています。ただし、その登記の原因が、自分の登記の原因より後に生じたときは、主張できます。\n\n- 原則：他人の登記を申請する義務を負うなら、その登記がないことは主張できない。\n- 例外：相手方の登記原因が、自分の登記原因より後なら、主張できる。\n\n**たとえば**、Cの売買が4月1日、Bの売買が5月1日なら、Bの原因はCの原因の後です。CはBの登記がないことを主張できます。順序が逆なら、主張できません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第18日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法3条、4条2項、5条、民法177条は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの背信的悪意者からの転得者が保護されるという結論は、判例の考え方に基づく一般的な整理で、判例の原文は確認していません。条文（民法177条）は「第三者」の範囲を定めていません。',
        'ウ・エ・オの具体例は、条文の文言から導いた一般的な説明です。イの具体例（付記1号と付記2号）も、4条2項の文言をかみ砕いたものです。',
    ],
    phrases=['留置権は登記できません', '付記登記どうしは前後で順位が決まります', '強迫で妨げた人は主張できません', '相手の原因が後なら主張できます', '転得者は自分が悪質でなければ保護されます'],
    header=dict(t1='登記できる？', t2='主張できる？', topic='不動産登記法　権利の登記と第三者',
                kanji='登・記・主・張・権・利・第・三・者'),
    poster_intro='権利の登記と第三者に関する決まりを、「登記できる権利と順位」（グループA：ア・イ）と「登記がないことを主張できない第三者」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記できる権利と第三者を整理', sub='不動産登記法第3条から第5条と民法（毎日ドリル 第18日）',
        col_a='登記できる権利と順位', col_b='登記がなくても言える人、言えない人', n_a=2,
        cards=[
            dict(h='留置権は登記できない',
                 ill='an isometric record sheet with two lines filled in, labeled 「抵当権」 and 「先取特権」, each with a green check mark. Beside the sheet, a faded gray tag labeled 「留置権」 floats outside the sheet, not attached to it.',
                 words=['抵当権', '先取特権', '留置権'], tag='留置権は載らない'),
            dict(h='付記登記どうしは前後で決まる',
                 ill='a wide bar labeled 「主登記」 on top, with two smaller bars stacked below it, labeled 「付記一号」 and 「付記二号」. A thin arrow along the side points from the upper small bar to the lower small bar. A green check mark sits beside the stack.',
                 words=['主登記', '付記一号', '付記二号'], tag='後の付記は後順位'),
            dict(h='強迫で妨げた者は主張できない',
                 ill='two faceless person figures at a counter. One figure is holding a form toward a clerk, while the second figure stands in front and blocks the way with an outstretched arm. A green check mark sits beside the blocked figure.',
                 words=[], tag='登記がないと言えない'),
            dict(h='自分の原因が先なら主張できる',
                 ill='a horizontal timeline with two flags. The left flag is labeled 「自分の売買」 and the right flag is labeled 「相手の売買」. A green bracket spans from the left flag toward the right. A green check mark sits above the left flag.',
                 words=['自分の売買', '相手の売買'], tag='原因が先なら主張可'),
            dict(h='背信的でない転得者は保護される',
                 ill='three person figures in a row, connected by thin arrows. The middle figure is faded gray with a name tag labeled 「背信的悪意者」. The right figure carries a name tag labeled 「転得者」 and is highlighted with a green glow. A green check mark sits beside the right figure.',
                 words=['背信的悪意者', '転得者'], tag='転得者は保護される'),
        ],
        kanji='留・置・権・登・記・付・順・位・強・迫・主・張・原・因・背・信・悪・意・転・得・者'.split('・')),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、登記できる権利と、できない留置権を左右の対比で示します。2枚目は、登記原因の前後で結論が変わることを、時間の流れで示します。',
    notebooks=[
        dict(name='登記できる権利と、できない権利', args=dict(
            title='登記できる権利、できない権利', sub='3条の列挙と留置権（毎日ドリル 第18日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「抵当権など」 on the left and 「留置権」 on the right; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 抵当権など
Scene: an isometric scene of a record sheet with three small stacked icons, each followed by a label: a house with a key and the label 抵当権, a stack of coins with the label 先取特権, a house with a rental sign and the label 賃借権.
Result badge with a green check mark: 登記できる

RIGHT PANEL (orange accent):
Panel header: 留置権
Scene: an isometric scene of a repaired building with a repair worker figure holding a key behind a closed gate. A blank record sheet with a dashed outline sits beside it.
Result badge with a red cross: 登記できない""",
            callout='登記ができる権利は、3条に掲げられた10個に限られます。\n留置権は、その中に入っていないので、保存の登記を受けることはできません。同じ担保の権利でも、先取特権は登記できます。',
            footer='不動産登記法3条',
            kanji='抵・当・権・先・取・特・賃・借・留・置・登・記・不・動・産'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (抵当権など on the left and 留置権 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='登記原因の前後で結論が変わる', args=dict(
            title='原因の前後で、結論が変わる', sub='他人のために登記を申請する義務を負う者（毎日ドリル 第18日 エ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with a common axis running left to right with two flags: the left flag labeled 4月1日 with an icon of a person figure buying a house, and the right flag labeled 5月1日 with an icon of a second person figure buying the same house.
Under the left flag, a blue label: 先の売買. Under the right flag, a green label: 後の売買.
A bracket under the axis connects the two flags and is labeled 相手の原因が後.
--- RESULT BOX ---
Below the timeline, one result box with a green check mark: 先に買った人は登記がないことを主張できる.
Use exactly these strings, and no others, for the labels. The two flag labels 先の売買 and 後の売買 are different strings; draw them in different accent colors (blue and green).""",
            callout='他人のために登記を申請する義務を負う者は、原則として、その登記がないことを主張できません。\nただし、相手方の登記原因が自分の登記原因の後に生じたときは、主張できます。',
            footer='不動産登記法5条2項',
            kanji='売・買・先・後・登・記・主・張・相・手・原・因'.split('・'), what='timeline',
            check='confirm the two flag labels are different strings drawn in different accent colors, ')),
    ],
)
