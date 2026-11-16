# C-01 敷地権の割合の計算例
from fractions import Fraction as F

# 計算例の数値（床面積は区分所有法第14条第3項・規則第115条の内側線で測った値）
UNITS = [('101号室', '65.43'), ('102号室', '58.21'), ('201号室', '72.36')]
CENT = [(n, int(a.replace('.', ''))) for n, a in UNITS]   # 百分の一平方メートル単位の整数
TOTAL = sum(x for _, x in CENT)                            # 19600 → 196.00
TOTAL_S = '%d.%02d' % divmod(TOTAL, 100)
MOCHI = (3, 4)                                             # 土地を他人と共有するときの持分（4分の3）
N1, A1 = CENT[0]
DEN2 = TOTAL * MOCHI[1]
NUM2 = A1 * MOCHI[0]

LINES = (
    ['専有部分の床面積：' + '、'.join('%s %s㎡' % u for u in UNITS) + '。合計 %s㎡。' % TOTAL_S]
    + ['%s：%d分の%d（%s ÷ %s）' % (n, TOTAL, x, a, TOTAL_S) for (n, x), (_, a) in zip(CENT, UNITS)]
    + ['検算：分子の合計 %s ＝ %d（分母と一致）。' % (' ＋ '.join(str(x) for _, x in CENT), sum(x for _, x in CENT)),
       '土地を他人と共有し、持分が%d分の%dのとき：%sは %d分の%d × %d分の%d ＝ %d分の%d（土地全体に対する割合）。'
       % (MOCHI[1], MOCHI[0], N1, MOCHI[1], MOCHI[0], TOTAL, A1, DEN2, NUM2),
       '約分しても割合は同じ。%sの%d分の%d ＝ %d分の%d（どちらで書くかは、末尾の「原文は未確認」の点）。'
       % (CENT[2][0], TOTAL, CENT[2][1], F(CENT[2][1], TOTAL).denominator, F(CENT[2][1], TOTAL).numerator)]
)


def verify():
    assert TOTAL == 19600 and TOTAL_S == '196.00'
    assert sum(F(x, TOTAL) for _, x in CENT) == 1, '割合の合計は1'
    assert F(NUM2, DEN2) == F(MOCHI[0], MOCHI[1]) * F(A1, TOTAL)
    assert sum(F(MOCHI[0], MOCHI[1]) * F(x, TOTAL) for _, x in CENT) == F(MOCHI[0], MOCHI[1]), '共有のときの合計は持分'
    assert NUM2 == 19629 and DEN2 == 78400
    assert F(CENT[2][1], TOTAL) == F(1809, 4900)


SHEET = dict(
    id='C-01',
    law='区分所有法',
    articles='区分所有法第14条・第22条・第32条、不動産登記規則第115条、不動産登記規則第118条',
    conclusion=[
        '敷地権の割合は、規約がなければ**専有部分の床面積の割合**で決まる（区分所有法第22条第2項本文・第14条第1項）。',
        '床面積は**壁その他の区画の内側線**で測る（区分所有法第14条第3項、規則第115条）。登記の専有部分と同じ測り方。',
        '規約で**別の割合**を定めれば、その割合による（区分所有法第22条第2項ただし書）。その規約を設定したことを証する情報を添付する。',
    ],
    blocks=[
        dict(kind='table', title='割合の決まり方（場合分け）',
             head=['場面', '割合', '根拠'],
             rows=[['規約がない', '専有部分の床面積の割合（合計が分母）', '区分所有法第22条第2項本文・第14条第1項'],
                   ['規約で別の割合を定めた', '規約の割合', '区分所有法第22条第2項ただし書'],
                   ['一部共用部分で床面積があるもの', '共用すべき者の床面積の割合で配分して算入', '区分所有法第14条第2項'],
                   ['専有部分の全部を1人が所有（土地も単独）', '同じ決まりを準用する', '区分所有法第22条第3項'],
                   ['最初に専有部分の全部を所有する者', '公正証書で割合の規約を設定できる', '区分所有法第32条'],
                   ['土地を他人と共有', '自分の持分を床面積の割合で割り振る', '区分所有法第22条第1項・第2項']],
             note='規約の割合によるときは、表題登記に「規約を設定したことを証する情報」を添付する（令別表12の項添付情報欄ヘ（2））。'),
    ],
    example=dict(kind='計算例', title='3戸の区分建物（規約なし）', lines=LINES),
    traps=['床面積は**壁心ではなく内側線**。一棟の建物の床面積（壁心）で割合を出さない。',
           '区分所有法第22条第2項は、**1人が数個の専有部分を所有する**ときの割り振りの決まり。新築して全部を持つ分譲者が、その典型である。',
           '規約の割合は、床面積の割合と違っていてよい。規約の割合を使うのに、規約を証する情報を添付し忘れない。'],
    basis=['区分所有法第14条・第22条・第32条', '不動産登記規則第115条、不動産登記規則第118条', '令別表12の項添付情報欄ヘ'],
    more=['joubun-nigate/kubun-tatemono-hani/03-shikichi-seiritsu.md', 'topics/KE_15_shitchiken-bunrishobun-kanou-kiyaku.md'],
    claims=[
        ('区分所有法', '14', 'その有する専有部分の床面積の割合による'),
        ('区分所有法', '14', '壁その他の区画の内側線で囲まれた部分の水平投影面積による'),
        ('区分所有法', '14', '一部共用部分の床面積は、これを共用すべき各区分所有者の専有部分の床面積の割合により配分して'),
        ('区分所有法', '22', '各専有部分に係る敷地利用権の割合は、第十四条第一項から第三項までに定める割合による'),
        ('区分所有法', '22', '規約でこの割合と異なる割合が定められているときは、その割合による'),
        ('区分所有法', '22', '建物の専有部分の全部を所有する者の敷地利用権が単独で有する所有権その他の権利である場合に準用する'),
        ('区分所有法', '32', '第二十二条第一項ただし書及び第二項ただし書'),
        ('不動産登記規則', '115', '区分建物にあっては、壁その他の区画の内側線'),
        ('不動産登記規則', '118', '敷地権の割合'),
    ],
    unverified=['敷地権の割合を、床面積の合計を分母にしたまま（約分せずに）表示する書き方は、登記実務の扱いとして見られるが、原文は未確認。',
                '土地を他人と共有するとき、敷地権の割合を「持分×床面積の割合」で土地全体に対する割合として表示する扱いは、原文は未確認（区分所有法第22条は敷地利用権の割合を定めるだけ）。'],
    note_law='区分所有法は令和7年法律第47号による改正（令和8年4月1日施行）後の条文で確かめた。第14条・第22条の文言はこの論点に関わる変更がない。',
    header=dict(l1='敷地権の割合の', l2='計算の型', hl='計算の型',
                left='a stack of floor plans of apartment units with a calculator and a pencil, all without any text',
                right='a small apartment building standing on a plot of land divided into colored slices like a pie, all without any text'),
    zukai=dict(title='敷地権の割合の計算', topics='床面積の割合・内側線・規約の割合・共有の土地',
               cards=[
                   dict(h='床面積の割合で分ける', illust='An apartment building with three units of different sizes; below it, a plot of land split into three slices whose sizes match the units.', words=[], tag='床面積の割合'),
                   dict(h='床面積は内側線で測る', illust='A floor plan of one unit with a thick wall; a bold line traces the inner face of the wall, a faint line marks the wall center and is crossed out.', words=['内側線'], tag='壁心ではない'),
                   dict(h='規約があれば規約の割合', illust='A document with a seal placed on top of the land slices, changing their sizes.', words=['規約'], tag='規約の割合が優先'),
                   dict(h='土地が共有なら持分の中で', illust='A plot of land with three quarters shaded for the building owner and one quarter for a neighbor; the shaded part is split among the units.', words=[], tag='持分を割り振る'),
                   dict(h='分子の合計で検算', illust='Three small fraction cards being added together into one full circle.', words=[], tag='合計は分母と一致'),
               ]),
)
