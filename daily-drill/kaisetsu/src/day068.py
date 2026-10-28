def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='催告した相手で、', t2='結論が変わる？', topic='民法　制限行為能力者')
_PT = '制限行為能力者の取扱いを整理'
_PS = '民法（毎日ドリル 第68日）'

_cards = [
    dict(h='負担のない贈与は取り消せない',
         ill='a young person figure receiving a wrapped gift from a smiling giver figure. A thin dotted line shows no strings attached. A small stamp labeled 「取消し不可」 sits beside the young person. A green check mark sits beside the gift.',
         words=['取消し不可'], tag='同意は不要'),
    dict(h='保佐人の同意のない保証は取り消せる',
         ill='an assisted person figure signing a contract labeled 「保証」 while a guardian figure with a name tag labeled 「保佐人」 stands apart, not signing. A stamp labeled 「取消し可」 sits on the contract. A green check mark sits beside the stamp.',
         words=['保証', '保佐人', '取消し可'], tag='同意がなければ取消し'),
    dict(h='成年後の本人への催告は追認とみなす',
         ill='a horizontal timeline. On the left a flag labeled 「成年」; further right a letter labeled 「催告」 sent to an adult figure who stays silent. A green stamp labeled 「追認」 appears at the right end.',
         words=['成年', '催告', '追認'], tag='確答がなければ追認'),
    dict(h='保佐人の追認を求める催告は取消しとみなす',
         ill='a counterparty figure sending a letter labeled 「催告」 to an assisted person figure. A guardian figure labeled 「保佐人」 stands beside the assisted person, and no reply bubble appears. A green stamp labeled 「取消し」 appears at the right end.',
         words=['催告', '保佐人', '取消し'], tag='通知がなければ取消し'),
    dict(h='取り消されたら現存利益の限度で返す',
         ill='an adult figure with a guardian shape in the background holding a box of received goods. A balance scale shows a small weight labeled 「現存利益」 on the figure side. A green check mark sits beside the scale.',
         words=['現存利益'], tag='現に利益を受けた限度'),
]

_nb1_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and three data rows, with a column of small icons on the left.

Header row: 催告の相手 | 催告の内容 | 確答や通知がないとき

Row 1 (blue accent): 行為能力者となった後の本人 | 追認するかどうかを確答せよ | 追認したものとみなす
Row 2 (green accent): 法定代理人、保佐人、補助人 | 追認するかどうかを確答せよ | 追認したものとみなす
Row 3 (orange accent): 被保佐人、被補助人 | 保佐人、補助人の追認を得よ | 取り消したものとみなす

IMPORTANT: Row 1 and Row 2 end with the string 追認したものとみなす, and Row 3 ends with the different string 取り消したものとみなす. Draw the two strings in different colors (green for 追認したものとみなす, red for 取り消したものとみなす) so they can never be confused or duplicated.
Use exactly these strings, and no others."""

_nb2_layout = """--- FLOW ---
Render as a clean flat-design diagram in two blocks stacked vertically, connected by a small downward arrow with no text.
Block 1 (blue accent), block header: 原則. Scene: an exchange of goods and money between two figures, with the label: 取り消された行為は、初めから無効. The label under it: 受け取った物を返して、元の状態に戻す
Block 2 (green accent), block header: 制限行為能力者だった人. Scene: a figure holding a box with part of the contents already used up, with the label: 現に利益を受けている限度で返す
Use exactly these strings, and no others."""

D = dict(
    catch='催告の相手で、みなす結果が変わる',
    intro='未成年者・被保佐人・成年被後見人といった制限行為能力者について、同意の要否、相手方の催告、取り消した後の返還を問う問題です（民法5条・9条・13条・20条・121条の2）。\n\nこの記事では、催告の相手によって、確答や通知がないときの結果が変わることを、具体的な場面で確認します。この問題は、誤っているものを選ぶ形式です。',
    sections={
        'ア': ('負担のない贈与を受けるのに、同意はいらない',
               '未成年者が法律行為をするには、法定代理人の同意を得なければなりません。ただし、単に権利を得、又は義務を免れる法律行為は、この限りではありません（民法5条1項）。同意に反する行為は取り消せますが、同意が不要な行為は取り消せません（同条2項）。\n\n負担のない贈与を受けることは、単に権利を得る行為です。本肢は正しいといえます。\n\n**たとえば**、17歳のAが、おじのBから、何の条件もつかない贈与で時計をもらう契約をしたとします。法定代理人の同意がなくても、Aは、未成年者であることを理由に取り消すことができません。'),
        'イ': ('保佐人の同意のない保証は、取り消せる',
               '被保佐人が、借財又は保証をするには、保佐人の同意を得なければなりません（民法13条1項2号）。同意又はこれに代わる許可を得ないでしたものは、取り消すことができます（同条4項）。\n\n本肢は正しいといえます。\n\n**たとえば**、被保佐人Aが、保佐人に相談せず、Bの借入金の保証人になる契約をしたとします。この保証契約は、同意がないので、Aが取り消すことができます。'),
        'ウ': ('成年後の本人への催告は、確答がないと追認とみなす',
               '制限行為能力者の相手方は、本人が行為能力者となった後、その本人に、一箇月以上の期間を定めて、追認するかどうかを確答せよと催告できます。期間内に確答がないときは、追認したものとみなされます（民法20条1項）。\n\n問題文は「取り消したものとみなされる」としているので、本肢は誤りです。\n\n**たとえば**、未成年者だったAが18歳になった後、契約の相手方Bが、1箇月以上の期間を定めて「追認するかどうか答えてください」と催告したとします。Aが期間内に何も答えなかったときは、契約を追認したものとみなされます。'),
        'エ': ('保佐人の追認を求める催告は、通知がないと取消しとみなす',
               '制限行為能力者の相手方は、被保佐人に対しては、期間内に保佐人の追認を得るように催告できます。被保佐人が、期間内にその追認を得た旨の通知を発しないときは、その行為を取り消したものとみなされます（民法20条4項）。\n\n問題文は「追認したものとみなされる」としているので、本肢は誤りです。\n\n**たとえば**、被保佐人Aと保佐人の同意が必要な契約をしたCが、Aに「1箇月以内に保佐人の追認を得てください」と催告したとします。Aが期間内に追認を得た旨の通知をしなければ、契約は取り消したものとみなされます。'),
        'オ': ('取り消された後は、現に利益を受けている限度で返す',
               '取り消された行為は、初めから無効であったものとみなされます（民法121条）。原則は、受け取った物を返して元の状態に戻す義務を負います（121条の2第1項）。\n\nただし、行為の時に制限行為能力者であった人は、その行為によって現に利益を受けている限度で返還すれば足ります（同条3項）。本肢は正しいといえます。\n\n**たとえば**、成年被後見人Aが日常生活に関する行為ではない契約をして、物を受け取り、後に契約が取り消されたとします。Aは、今も利益として残っている限度で返還すれば足ります。'),
    },
    summary=[
        ('ア', '正', '負担のない贈与を受けるのは単に権利を得る行為で、法定代理人の同意はいらない'),
        ('イ', '正', '被保佐人が保佐人の同意なしにした保証は、取り消すことができる'),
        ('ウ', '誤', '成年後の本人に催告して確答がないときは、追認したものとみなされる'),
        ('エ', '誤', '被保佐人に保佐人の追認を得るよう催告して通知がないときは、取り消したものとみなされる'),
        ('オ', '正', '取り消された場合、行為の時に制限行為能力者だった人は、現に利益を受けている限度で返還する'),
    ],
    summary_tail='ウとエは、みなす結果を入れ替えた出題です。確答を求めるときは「追認」、保佐人の追認を求めるときは「取消し」と、催告の相手と内容で結果が変わります。',
    supplements=[
        '### 補足説明（ウ・エ）：催告の相手によって、みなす結果が変わる\n\n制限行為能力者の相手方が催告をしたとき、確答や通知がないときの結果は、催告の相手と内容によって変わります（民法20条）。\n\n| 催告の相手 | 催告の内容 | 確答や通知がないとき |\n|---|---|---|\n| 行為能力者となった後の本人 | 追認するかどうかを確答せよ（1項） | 追認したものとみなす |\n| 法定代理人、保佐人、補助人 | 追認するかどうかを確答せよ（2項） | 追認したものとみなす |\n| 被保佐人、被補助人 | 保佐人、補助人の追認を得よ（4項） | 取り消したものとみなす |\n\n**たとえば**、同じ被保佐人との契約でも、保佐人に「追認しますか」と催告して返事がなければ追認になります。被保佐人本人に「保佐人の追認を得てください」と催告して通知がなければ、取消しになります。',
        '### 補足説明（オ）：取り消した後の返還の範囲\n\n取り消された行為に基づいて物や代金を受け取っていたときの返還の範囲を整理します（民法121条の2）。\n\n- 原則：相手方を元の状態に戻す義務を負う（1項）。\n- 行為の時に制限行為能力者であった人：現に利益を受けている限度で返還する（3項）。\n\n**たとえば**、成年被後見人が契約で受け取った品物が、手元にまだ残っているとします。この場合、その品物は返さなければなりません。「現に利益を受けている限度」とは、受け取った利益が今も残っている範囲、という意味です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第68日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法5条、9条、13条、20条、121条、121条の2は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「利益が今も残っている範囲」という説明は、121条の2第3項の「現に利益を受けている限度」を、条文からの一般的な整理として言い換えたものです。個別の判例の確認はしていません。',
        'イのように被保佐人が取り消せることは、13条4項から導いています。取消権者の範囲（120条）については確認していません。',
    ],
    phrases=['負担のない贈与なら同意はいりません', '保佐人の同意のない保証は取り消せます', '成年後の本人に催告すれば追認です', '保佐人の追認を求める催告は取消しです', '取り消したら現存利益の限度で返します'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='制限行為能力者の取扱いを、「同意と取消し」（グループA：ア・イ）と「催告と返還」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='同意と取消し', col_b='催告と返還', n_a=2,
        cards=_cards,
        kanji=K(_PT, _PS, '同意と取消し催告と返還', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、催告の相手と内容によって、みなす結果が変わることを表で示します。2枚目は、取り消した後の返還の範囲を示します。',
    notebooks=[
        dict(name='催告の相手で、みなす結果が変わる', args=dict(
            title='催告したら、どうみなされる？', sub='制限行為能力者の相手方の催告権（毎日ドリル 第68日 ウ・エ）',
            req='a table',
            layout=_nb1_layout,
            callout='行為能力者となった本人や、法定代理人、保佐人に確答を求めたときは、確答がないと追認したものとみなされます。\n被保佐人に保佐人の追認を得るよう求めたときは、通知がないと取り消したものとみなされます。',
            footer='民法20条1項・2項・4項',
            kanji=K('催告したらどうみなされる制限行為能力者の相手方の催告権追認取り消したもの行為能力者となった本人法定代理人保佐人補助人被保佐人被補助人確答通知'), what='table',
            check='confirm that the strings 追認したものとみなす (rows 1 and 2) and 取り消したものとみなす (row 3) are different strings drawn in different colors, ')),
        dict(name='取り消した後の返還の範囲', args=dict(
            title='取り消した後、どこまで返す？', sub='原状回復と現存利益（毎日ドリル 第68日 オ）',
            req='a diagram',
            layout=_nb2_layout,
            callout='取り消された行為は、初めから無効とみなされ、原則は元の状態に戻す義務を負います。\n行為の時に制限行為能力者であった人は、現に利益を受けている限度で返せば足ります。',
            footer='民法121条、121条の2第1項・3項',
            kanji=K('取り消した後どこまで返す原状回復と現存利益初めから無効元の状態に戻す制限行為能力者現に利益を受けている限度民法'), what='blocks',
            check='confirm there are exactly two blocks connected by one downward arrow with no text, ')),
    ],
)
