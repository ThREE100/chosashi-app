# G-03 相続（相続人と相続分）
from fractions import Fraction as F


def fr(x):
    """分数を「n分のm」で書く。"""
    x = F(x)
    return '%d分の%d' % (x.denominator, x.numerator) if x.denominator != 1 else str(x.numerator)


# 計算例：配偶者W、子A・B。Bは相続開始以前に死亡し、Bの子C・Dが代襲する。
W = F(1, 2)            # 民法第900条第1号
KIDS = 1 - W           # 子の側の全体
EACH = KIDS / 2        # 子2人（A・B）で等分（民法第900条第4号）
CD = EACH / 2          # Bの分をC・Dで等分（民法第901条第1項）
TOTAL = W + EACH + CD + CD


def verify():
    assert W == F(1, 2) and KIDS == F(1, 2)
    assert EACH == F(1, 4) and CD == F(1, 8)
    assert TOTAL == 1


SHEET = dict(
    id='G-03',
    law='民法',
    articles='民法第887条・第889条〜第892条・第900条・第901条・第923条・第939条',
    conclusion=[
        '配偶者は**常に相続人**。血族は、子→直系尊属→兄弟姉妹の**順位**で、先の順位の者がいないときに次の順位が相続人になる（民法第887条・第889条・第890条）。',
        '法定相続分は、配偶者と子が各**2分の1**、配偶者と直系尊属が**3分の2と3分の1**、配偶者と兄弟姉妹が**4分の3と4分の1**（民法第900条）。',
        '子が相続開始以前の**死亡・欠格・廃除**で相続権を失うと、その子が代襲する。**放棄**は代襲の原因にならない（民法第887条第2項・第939条）。',
    ],
    blocks=[
        dict(kind='table', title='相続人の組合せと法定相続分',
             head=['相続人', '配偶者', '血族の側（全体）'],
             rows=[['配偶者と子', '2分の1', '2分の1'],
                   ['配偶者と直系尊属', '3分の2', '3分の1'],
                   ['配偶者と兄弟姉妹', '4分の3', '4分の1'],
                   ['配偶者だけ', '全部', '―'],
                   ['血族だけ', '―', '全部（同順位の者で等分）']],
             note='同順位の血族は等分。父母の一方だけが同じ兄弟姉妹は、双方が同じ兄弟姉妹の2分の1（民法第900条第4号）。'),
        dict(kind='table', title='代襲するか（場合分け）',
             head=['事由', '代襲するか', '根拠'],
             rows=[['相続開始以前の死亡', 'する', '第887条第2項'],
                   ['欠格・廃除', 'する', '第887条第2項・第891条・第892条'],
                   ['相続の放棄', 'しない（初めから相続人でなかったとみなす）', '第939条'],
                   ['代襲者も相続権を失った', '子の系統は再代襲する', '第887条第3項'],
                   ['兄弟姉妹の子', '代襲する。再代襲の規定は準用されていない', '第889条第2項']]),
    ],
    example=dict(kind='計算例', title='子の一人が先に死亡し、孫二人が代襲する場合',
                 lines=['相続人：配偶者W、子A、代襲者C・D（相続開始以前に死亡した子Bの子）。',
                        f'配偶者W：{fr(W)}（民法第900条第1号）。',
                        f'子の側の{fr(KIDS)}を子A・Bで等分：各{fr(EACH)}（民法第900条第4号）。',
                        f'Bの分{fr(EACH)}をC・Dで等分：各{fr(CD)}（民法第901条第1項）。',
                        f'検算：{fr(W)}＋{fr(EACH)}＋{fr(CD)}＋{fr(CD)}＝{fr(TOTAL)}。']),
    traps=['相続を**放棄**した子の子は**代襲しない**。放棄した者は初めから相続人でなかったとみなす（民法第939条）。',
           '兄弟姉妹の子は代襲するが、**再代襲の規定は準用されていない**（民法第889条第2項は第887条第2項だけを準用）。',
           '限定承認は**共同相続人の全員**が共同してのみできる（民法第923条）。放棄は家庭裁判所に申述する（民法第938条）。'],
    basis=['民法第887条・第889条・第890条・第900条・第901条', '民法第891条・第892条', '第923条・第938条・第939条'],
    more=['topics/KM_10_daishuu-souzoku.md', 'topics/KM_11_hozonkoui-tanjunshounin.md'],
    claims=[
        ('民法', '890', '被相続人の配偶者は、常に相続人となる'),
        ('民法', '900', '子の相続分及び配偶者の相続分は、各二分の一とする'),
        ('民法', '900', '配偶者の相続分は、三分の二とし、直系尊属の相続分は、三分の一とする'),
        ('民法', '900', '配偶者の相続分は、四分の三とし、兄弟姉妹の相続分は、四分の一とする'),
        ('民法', '900', '父母の一方のみを同じくする兄弟姉妹の相続分は、父母の双方を同じくする兄弟姉妹の相続分の二分の一とする'),
        ('民法', '887', 'その者の子がこれを代襲して相続人となる'),
        ('民法', '889', '第八百八十七条第二項の規定は、前項第二号の場合について準用する'),
        ('民法', '901', 'その直系尊属が受けるべきであったものと同じとする'),
        ('民法', '939', '初めから相続人とならなかったものとみなす'),
        ('民法', '923', '共同相続人の全員が共同してのみこれをすることができる'),
        ('民法', '938', '家庭裁判所に申述しなければならない'),
    ],
    header=dict(l1='相続人と', l2='相続分の場合分け', hl='相続分',
                left='a simple family tree made of round portrait icons connected by lines, all without any text',
                right='a small house next to a round pie chart cut into slices, all without any text'),
    zukai=dict(title='相続人の決まり方', topics='配偶者・血族の順位・代襲・放棄',
               cards=[
                   dict(h='配偶者は常に相続人', illust='A family tree: the deceased in the center with a soft gray frame, the spouse beside highlighted.', words=['配偶者'], tag='常に相続人'),
                   dict(h='血族は順位で決まる', illust='Three steps of stairs with small figures: children on the first step, parents on the second, siblings on the third.', words=['子', '直系尊属', '兄弟姉妹'], tag='子→直系尊属→兄弟姉妹'),
                   dict(h='子が先に死亡なら孫が代襲', illust='A family tree where one child is shown with a gray frame and an arrow passes the share down to two grandchildren.', words=['代襲'], tag='死亡・欠格・廃除'),
                   dict(h='放棄した子の子は代襲しない', illust='A child figure stepping out of the family tree through a door; the grandchildren below have a crossed arrow.', words=[], tag='初めから相続人でない'),
                   dict(h='兄弟姉妹の子までで止まる', illust='A sibling line of the family tree going down one generation and stopping at a barrier.', words=[], tag='再代襲なし'),
               ]),
)
