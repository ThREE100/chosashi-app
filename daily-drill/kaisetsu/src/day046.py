D = dict(
    catch='地積の変更は期限あり、更正は所有者だけ',
    intro='土地の地積に関する変更の登記と更正の登記について、期限、添付する書類、端数の処理、申請できる人を問う問題です（不動産登記法37条・38条、不動産登記規則100条、不動産登記令別表の六の項）。\n\n変更は「あとから変わった」とき、更正は「最初から誤っていた」ときの登記です。この記事では、この違いを具体的な場面で確かめていきましょう。この問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('変更の後に名義人となった者は、自分の登記の日から一月',
               '地積について変更があった後に所有権の登記名義人となった者は、その者に係る所有権の登記があった日から一月以内に、地積に関する変更の登記を申請しなければなりません（不動産登記法37条2項）。起算日は、変更の日ではなく、自分の登記があった日です。\n\n本肢は正しいといえます。\n\n**たとえば**、3月1日に川の浸食で土地の一部が削られて面積が小さくなり、4月10日にBが所有権の移転の登記を受けたとします。Bの一月は、3月1日からではなく、4月10日から数えます。'),
        'イ': ('地積の更正の登記に、抵当権者の承諾書は要らない',
               '地積に関する更正の登記を申請するときの添付情報は、地積測量図です（不動産登記令別表の六の項）。抵当権者の承諾を証する情報は、添付情報として挙げられていません。\n\n問題文は、B銀行の承諾を証する情報を提供しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、土地に抵当権を付けて銀行から融資を受けている所有者が、測量をやり直して地積を小さく直す場合でも、銀行の承諾書を用意する必要はありません。地積測量図を添えて申請します。'),
        'ウ': ('宅地の地積は、百分の一平方メートル未満を切り捨てる',
               '地積は、水平投影面積により、平方メートルを単位として定めます。一平方メートルの百分の一未満の端数は切り捨てますが、宅地及び鉱泉地以外の土地で十平方メートルを超えるものは、一平方メートル未満の端数を切り捨てます（不動産登記規則100条）。\n\n宅地は、小数点以下第2位まで残す土地です。本肢は正しいといえます。\n\n**たとえば**、宅地の面積を計算して123.456平方メートルになったときは、四捨五入せず、切り捨てて123.45平方メートルとします。山林なら、同じ計算結果でも123平方メートルとします。'),
        'エ': ('更正の登記には、一月以内という申請義務がない',
               '地目又は地積について変更があったときに、一月以内の申請を義務付けているのは、変更の登記を定めた37条です。更正の登記は、最初から誤っていたものを直す登記で、この37条の期間の定めはありません。\n\n問題文は、誤りを知った日から一月以内に更正の登記を申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、令和8年9月1日に、登記記録の地積が実際と違っていると気づいたとします。そのときから一月以内という期限は、更正の登記にはありません。'),
        'オ': ('抵当権者は、地積の更正の登記を申請できない',
               '地積は、土地の表題部の登記事項です（不動産登記法34条1項4号）。地積に関する更正の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（同法38条）。\n\n問題文は、抵当権の設定の登記を受けているB銀行が申請できるとしているので、本肢は誤りです。\n\n**たとえば**、融資をした銀行が、担保にしている土地の地積が実際と違うと気づいても、自分で更正の登記を申請することはできません。土地の所有者に申請してもらいます。'),
    },
    summary=[
        ('ア', '正', '変更の後に名義人となった者の一月は、自分に係る登記があった日から数える'),
        ('イ', '誤', '地積の更正の登記に、抵当権者の承諾を証する情報は要らない（添付情報は地積測量図）'),
        ('ウ', '正', '宅地の地積は、一平方メートルの百分の一未満の端数を切り捨てる'),
        ('エ', '誤', '更正の登記には、変更の登記のような一月以内という申請義務がない'),
        ('オ', '誤', '地積の更正の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できない'),
    ],
    summary_tail='イとエは、変更と更正を取り違えさせる出題です。オは、申請できる人の範囲を広げた出題です。変更は期限あり、更正は期限なしで申請人は所有者などに限る、と分けて覚えましょう。',
    supplements=[
        '### 補足説明（ウ）：地積の端数の切り捨て\n\n地積は、土地の種類と広さで、どこまで残すかが変わります（不動産登記規則100条）。\n\n| 土地の種類と広さ | 切り捨てる端数 | 123.456平方メートルなら |\n|---|---|---|\n| 宅地・鉱泉地 | 百分の一平方メートル未満 | 123.45平方メートル |\n| 宅地・鉱泉地以外で、十平方メートルを超える | 一平方メートル未満 | 123平方メートル |\n| 宅地・鉱泉地以外で、十平方メートル以下 | 百分の一平方メートル未満 | （例）5.678平方メートルなら5.67平方メートル |\n\n**たとえば**、同じ面積の計算結果でも、宅地なら小数点以下第2位まで、広い山林や畑なら整数までしか登記に載りません。',
        '### 補足説明（エ・オ）：変更の登記と更正の登記\n\n地積の登記には、「変更」と「更正」があります。原因、期限、申請人が違います。\n\n| | 変更の登記 | 更正の登記 |\n|---|---|---|\n| 原因 | 登記した後に、土地の状態が変わった | 登記したときから、誤りがあった |\n| 申請の期限 | 変更の日（後から名義人になった者は自分の登記の日）から一月以内（37条） | 一月以内という定めはない |\n| 申請できる人 | 表題部所有者又は所有権の登記名義人 | 表題部所有者又は所有権の登記名義人以外は申請できない（38条） |\n\n**たとえば**、川の浸食で面積が減ったのは変更、最初の測量が間違っていたのは更正です。どちらの場合も、抵当権者や借りている人は、自分では申請できません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第46日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法34条1項4号・37条・38条、不動産登記規則100条、不動産登記令別表の六の項は、`note-articles/laws/` 配下の原文で確認しました。',
        'イについて、抵当権者の承諾が要らない理由（地積の更正は土地の状況を正しく公示するための登記で、権利の内容を変えるものではない）は、令別表の六の項に承諾書が挙げられていないことからの一般的な整理です。',
        'エの更正の登記に期間の定めがないという点は、37条が変更の登記だけを定めていることからの整理です。具体例（川の浸食、融資をした銀行）は、場面を思い描くための例です。',
    ],
    phrases=['変更後の名義人は自分の登記の日から', '更正に抵当権者の承諾書は要りません', '宅地は百分の一まで切り捨てです', '更正には一月以内の期限がありません', '抵当権者は更正を申請できません'],
    header=dict(t1='変更と更正、', t2='何が違う？', topic='不動産登記法　地積の登記',
                kanji='変・更・正・地・積・登・記'),
    poster_intro='地積に関する変更の登記と更正の登記を、「申請に必要なもの」（グループA：ア・イ）と「端数・期限・申請人」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地積の変更と更正を整理', sub='不動産登記法 第37条と第38条（毎日ドリル 第46日）',
        col_a='申請に必要なもの', col_b='端数と期限と申請人', n_a=2,
        cards=[
            dict(h='あとから名義人になったら自分の登記から',
                 ill='a horizontal timeline. On the left a flag labeled 「変更」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
                 words=['変更', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
            dict(h='更正の添付は地積測量図',
                 ill='an isometric land plot with a measuring tape along one side. Beside it, a drawing sheet labeled 「地積測量図」 is highlighted with a green glow. A green check mark sits beside the sheet. A small bank building stands faded in gray in the background with nothing in its hands.',
                 words=['地積測量図'], tag='銀行の承諾書は不要'),
            dict(h='宅地は百分の一まで切り捨て',
                 ill='a land plot labeled 「宅地」 beside a calculator-like sheet. The number is cut off by a pair of scissors at the second digit after the decimal point, drawn as a dotted line. A green check mark sits beside the cut line.',
                 words=['宅地'], tag='四捨五入しない'),
            dict(h='更正の登記に一月の期限はない',
                 ill='a calendar page with no deadline mark, beside a record sheet labeled 「更正」 with one line corrected by a pencil. An owner figure holds the sheet calmly. A green check mark sits beside the owner.',
                 words=['更正'], tag='期限の定めなし'),
            dict(h='更正を申請できるのは所有者など',
                 ill='an isometric land plot. An owner figure at a desk, carrying a name tag labeled 「所有者」, holds a form and is highlighted with a green glow. A faded gray bank figure with no tag stands aside in the background. A green check mark sits beside the owner.',
                 words=['所有者'], tag='抵当権者は不可'),
        ],
        kanji='変・更・正・地・積・測・量・図・宅・所・有・者・月・以・内・自・分・登・記・名・義・人'.split('・')),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、地積の端数を切り捨てる位置を、土地の種類ごとの表で示します。2枚目は、変更の登記と更正の登記の違いを左右の対比で示します。',
    notebooks=[
        dict(name='地積の端数の切り捨て', args=dict(
            title='どこまで切り捨てる？', sub='地積の端数の処理（毎日ドリル 第46日 ウ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with three rows and three columns, and a small isometric icon at the left of each row.
Column headers: 土地の種類 | 切り捨てる端数 | 計算結果が123.456なら
Row 1 (blue accent), icon: a house on a land plot. Cells: 宅地と鉱泉地 | 百分の一平方メートル未満 | 123.45
Row 2 (green accent), icon: a mountain forest. Cells: 宅地と鉱泉地以外で十平方メートルを超える土地 | 一平方メートル未満 | 123
Row 3 (gray accent), icon: a small garden plot. Cells: 宅地と鉱泉地以外で十平方メートル以下の土地 | 百分の一平方メートル未満 | （例）5.678なら5.67
Use exactly these strings, and no others, for the table text. Rows 1 and 3 share the same rule in the second column; draw them in different accent colors.""",
            callout='地積は、四捨五入ではなく、切り捨てて定めます。\n宅地と、十平方メートル以下のその他の土地は小数点以下第2位まで、広いその他の土地は整数までです。',
            footer='不動産登記規則100条',
            kanji='地・積・宅・鉱・泉・切・捨・土・種・類・端・数・計・算・結・果・例'.split('・'), what='table',
            check='confirm the second column of rows 1 and 3 shows the same string while row 2 shows a different string, ')),
        dict(name='変更の登記と更正の登記', args=dict(
            title='変更と更正は、どこが違う？', sub='地積に関する登記（毎日ドリル 第46日 エ・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 変更の登記 and the right header is 更正の登記. Draw them in different accent colors (blue on the left and orange on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 変更の登記
Scene: an isometric scene of a land plot whose edge is being worn away by a river, drawn as a smaller outline inside a dotted larger outline.
Result badges (stacked): 登記の後に状態が変わった | 変更の日から一月以内

RIGHT PANEL (orange accent):
Panel header: 更正の登記
Scene: an isometric scene of a record sheet with one number corrected by a pencil, beside a land plot with a measuring tape.
Result badges (stacked): 最初から誤りがあった | 一月以内の定めはない

Below both panels, one wide banner with a name tag icon: 申請できるのは、表題部所有者又は所有権の登記名義人だけ""",
            callout='変更は、登記した後に状態が変わったときの登記で、一月以内に申請します。\n更正は、最初から誤っていたときの登記で、期限の定めはありません。どちらも抵当権者は申請できません。',
            footer='不動産登記法37条・38条',
            kanji='変・更・正・登・記・状・態・最・初・誤・定・申・請・表・題・部・所・有・者・名・義・人'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (変更の登記 on the left and 更正の登記 on the right) in different accent colors, ')),
    ],
)
