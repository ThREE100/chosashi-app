D = dict(
    catch='みなされる場合と取消権の期間',
    intro='制限行為能力者（未成年者、成年被後見人、被保佐人など）がした契約の「取消し」について、民法の決まりを問う問題です（民法9条・20条・124条から126条まで）。正しいものの組合せを選びます。\n\nこの記事では、相手方が催告したときに「追認したとみなされる」場合と「取り消したとみなされる」場合の違い、そして法定追認と取消権の期間を、具体的な場面で確認します。',
    sections={
        'ア': ('成年被後見人の売買は、同意があっても取り消せる',
               '成年被後見人の法律行為は、日用品の購入その他日常生活に関する行為を除き、取り消すことができます（民法9条）。\n\n問題文は、成年後見人の同意を得た売却について「取り消すことができない」としています。しかし、取り消せない場合は条文上、日常生活に関する行為に限られ、同意を得たことは例外とされていません。本肢は誤りです。\n\n**たとえば**、成年被後見人が、自分の土地を売却する契約をしたとします。土地の売却は日常生活に関する行為ではないので、後見人の同意を得ていても、取り消すことができます。'),
        'イ': ('成年になった本人が催告に答えないと、追認したとみなされる',
               '制限行為能力者の相手方は、その者が行為能力者となった後、一箇月以上の期間を定めて、追認するかどうかを確答するよう催告できます。その期間内に確答がないと、追認したものとみなされます（民法20条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、17歳のときに親に黙って土地を売却した人が、20歳になったとします。買主が「一箇月以内に、追認するかどうかを答えてください」と催告し、返事がなければ、売買を追認したものとして扱われます。'),
        'ウ': ('被保佐人への催告で通知がないと、取り消したとみなされる',
               '被保佐人に対し、保佐人の追認を得るよう催告した場合に、期間内に追認を得た旨の通知を発しないときは、その行為を取り消したものとみなされます（民法20条4項）。\n\n問題文は「追認したものとみなされる」としているので、本肢は誤りです。\n\n**たとえば**、被保佐人が保佐人の同意なしに土地を売却し、買主が「一箇月以内に、保佐人の追認を得てください」と催告したとします。通知がなければ、売買は取り消したものとして扱われます。'),
        'エ': ('成年後に異議なく代金を請求すると、追認したとみなされる',
               '追認をすることができる時以後に、取り消すことができる行為について、履行の請求（全部又は一部）などの事実があったときは、追認をしたものとみなされます。ただし、異議をとどめたときは別です（民法125条2号）。追認できる時とは、取消しの原因となっていた状況が消え、取消権を有することを知った後です（民法124条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、未成年のときに土地を売った人が、成年になり、取り消せることも知ったうえで、買主に「代金を払ってください」と請求したとします。何も断らずに請求すれば、追認したものとみなされます。'),
        'オ': ('取消権は、追認できる時から五年で消える',
               '取消権は、追認をすることができる時から五年間行使しないときは、時効によって消滅します。行為の時から二十年を経過したときも同じです（民法126条）。\n\n問題文は「十年間」としているので、本肢は誤りです。\n\n**たとえば**、だまされて土地を売った人が、だまされたと気づいて追認できる状態になってから、五年のあいだ何もしなければ、取消権は消えます。売買から二十年がたったときも、同じく消えます。'),
    },
    summary=[
        ('ア', '誤', '成年被後見人の売買は、後見人の同意があっても、日常生活に関する行為でなければ取り消せる'),
        ('イ', '正', '行為能力者となった本人が催告期間内に確答しないと、追認したものとみなされる'),
        ('ウ', '誤', '被保佐人が催告期間内に追認を得た旨の通知を発しないと、取り消したものとみなされる'),
        ('エ', '正', '追認できる時以後に異議なく履行を請求すると、法定追認になる'),
        ('オ', '誤', '取消権は、追認できる時から五年（十年ではない）で時効消滅する'),
    ],
    summary_tail='ウは「追認」と「取消し」の取り違え、オは「五年」を「十年」にすり替えた出題です。催告の相手によってみなされる効果が違うこと、取消権の期間は五年と二十年であることを押さえましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：催告の相手によって、みなされる効果が違う\n\n相手方が催告をして、期間内に答えが来なかったときの効果は、だれに催告したかで変わります。\n\n- 行為能力者となった本人に催告：期間内に答えがないと、追認したものとみなす（20条1項）。\n- 法定代理人、保佐人、補助人に催告：期間内に答えがないと、追認したものとみなす（20条2項）。\n- 被保佐人に保佐人の追認を得るよう催告：期間内に通知がないと、取り消したものとみなす（20条4項）。\n\n**たとえば**、成年になった元未成年者に聞いて返事がなければ追認、被保佐人本人に「保佐人の追認を得てください」と催告して通知がなければ取消し、と分けて覚えます。',
        '### 補足説明（エ・オ）：追認できる時と、取消権の期間\n\n取消権の話は、「追認できる時」が基準になります。\n\n- 追認できる時：取消しの原因となっていた状況が消え、取消権を有することを知った後（民法124条1項）。\n- その時以後に異議なく履行を請求するなどすると、追認したものとみなされる（民法125条）。\n- 追認できる時から五年、行為の時から二十年で、取消権は消える（民法126条）。\n\n**たとえば**、成年になって取消権を知ったあと、何も言わずに代金を請求すれば追認とみなされます。何もしないまま五年たてば、取消権は消えます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第26日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法9条、20条1項・2項・4項、124条1項、125条2号、126条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「同意があっても取り消せる」は、9条が取り消せない場合を日常生活に関する行為に限っていることからの一般的な整理で、成年後見人に同意権がないことを定めた条文の確認はしていません。',
        '各具体例（17歳で土地を売却した、被保佐人が土地を売却したなど）は、条文の文言を日常の場面に置き換えた説明で、個別の事例の判断ではありません。',
    ],
    phrases=['成年被後見人の売買は同意があっても取り消せます', '催告に答えなければ追認したとみなされます', '被保佐人への催告は取消しになります', '異議なく代金を請求すると追認です', '取消権は五年で消えます'],
    header=dict(t1='みなされるのは、', t2='追認？取消し？', topic='民法　制限行為能力者の取消し',
                kanji='追・認・取・消・毎・制・限・行・為'),
    poster_intro='制限行為能力者の取消しを、「取り消せるか、催告の効果」（グループA：ア・イ・ウ）と「法定追認と取消権の期間」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='取消しの決まりを整理', sub='民法9条・20条・124条から126条（毎日ドリル 第26日）',
        col_a='取り消せるか、催告の効果', col_b='法定追認と期間', n_a=3,
        cards=[
            dict(h='成年被後見人の土地の売却は取り消せる',
                 ill='an isometric scene of a land plot with a for-sale signpost, and a person figure carrying a name tag labeled 「成年被後見人」 handing a contract paper to a buyer figure. A guardian figure stands behind and nods with a small paper. A circular arrow around the contract paper suggests that it can be undone, and a green check mark sits beside the contract.',
                 words=['成年被後見人'], tag='同意があっても取消し'),
            dict(h='成年になって答えないと追認とみなされる',
                 ill='a horizontal timeline. On the left a flag labeled 「成年」; further right an end flag labeled 「確答なし」. A green bracket labeled 「一箇月以上」 spans the part between them. A stamp labeled 「追認」 sits at the right end. A green check mark sits beside the stamp.',
                 words=['成年', '確答なし', '一箇月以上', '追認'], tag='答えなければ追認'),
            dict(h='被保佐人は通知がないと取消しとみなされる',
                 ill='a person figure carrying a name tag labeled 「被保佐人」 next to a helper figure labeled 「保佐人」, and an empty envelope in the air. A stamp labeled 「取消し」 sits on the contract paper at the right. A green check mark sits beside the stamp.',
                 words=['被保佐人', '保佐人', '取消し'], tag='通知がなければ取消し'),
            dict(h='異議なく代金を請求すると追認になる',
                 ill='a seller figure holding an invoice paper toward a buyer figure with no raised hand of objection. A stamp labeled 「追認」 appears above the invoice. A green check mark sits beside the stamp.',
                 words=['追認'], tag='法定追認'),
            dict(h='取消権は五年で消える',
                 ill='a calendar page with a large 「五年」 mark on it. A stamp labeled 「取消権」 fades out on the right, drawn as a faint outline. A green check mark sits beside the calendar.',
                 words=['五年', '取消権'], tag='追認できる時から五年'),
        ],
        kanji='成・年・被・後・見・人・追・認・取・消・保・佐・確・答・権'.split('・')),
    nb_label='イ・ウ・エ・オ肢', nb_intro='イ・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、催告の相手によって、みなされる効果が違うことを早見表にします。2枚目は、追認できる時を基準に、法定追認と取消権の期間を時間の流れで示します。',
    notebooks=[
        dict(name='催告の相手によって、みなされる効果が違う', args=dict(
            title='催告に答えないと、どうなる？', sub='相手方の催告権（毎日ドリル 第26日 イ・ウ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Three columns and three data rows. The header row has the column names. Each data row has a small isometric icon at the left of its first cell (an adult figure for the first row, a helper figure with a small badge for the second row, a person figure with a helper beside for the third row). Use exactly these strings, and no others:
Header row: 催告の相手 | 期間内に答えがないと | 条文
Row 1: 行為能力者となった本人 | 追認したものとみなす | 20条1項
Row 2: 法定代理人、保佐人、補助人 | 追認したものとみなす | 20条2項
Row 3: 被保佐人（保佐人の追認を得るよう催告） | 取り消したものとみなす | 20条4項
In the middle column, draw the cells 「追認したものとみなす」 (Rows 1 and 2) in green and the cell 「取り消したものとみなす」 (Row 3) in orange; they are different strings and must never be confused or duplicated.""",
            callout='期間内に答えがないときの効果は、催告の相手で変わります。\n本人や保佐人に催告すれば追認、被保佐人に保佐人の追認を得るよう催告すれば取消しです。',
            footer='民法20条',
            kanji='催・告・追・認・取・消・本・人・保・佐・条'.split('・'), what='table',
            check='confirm the table has exactly 3 columns and 3 data rows, confirm 追認したものとみなす (green) and 取り消したものとみなす (orange) are different strings in different accent colors, ')),
        dict(name='追認できる時と、取消権の期間', args=dict(
            title='追認できる時が、スタート', sub='法定追認と取消権の期間（毎日ドリル 第26日 エ・オ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline. A common axis runs left to right with three flags.
Left flag: label 行為の時, with an icon of a contract paper.
Middle flag: label 追認できる時, with an icon of a person who has just turned adult and holds a small key. Below the middle flag, in small text: 状況が消え、取消権を知った後.
Right flag: label 異議なく請求, with an icon of an invoice paper. Above the right flag, a green stamp: 追認とみなす.
Above the axis, a blue bracket starts at the middle flag and extends to the far right, labeled 五年で取消権が消える.
Below the axis, an orange bracket starts at the left flag and extends to the far right, labeled 行為の時から二十年でも消える.
Use exactly these strings, and no others, for the labels. The two bracket labels are different strings; draw them in different accent colors (blue and orange).""",
            callout='追認できる時とは、取消しの原因が消え、取消権を知った後です。\nその時以後に異議なく請求すれば追認とみなされ、その時から五年、行為の時から二十年で取消権は消えます。',
            footer='民法124条から126条まで',
            kanji='追・認・行・為・取・消・権・状・況・異・議・請・求'.split('・'), what='timeline',
            check='confirm the two bracket labels are different strings in different accent colors, ')),
    ],
)
