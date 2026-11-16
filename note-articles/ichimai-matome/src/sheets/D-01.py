# D-01 表示に関する登記の期限（起算点で整理する）
import datetime


def _deadline(day):
    """「その日から一月以内」の末日。初日は算入せず（民法第140条）、最後の月の応当日の前日に満了する。
    応当日がないときは、その月の末日（民法第143条第2項）。"""
    start = day + datetime.timedelta(days=1)          # 起算日（初日不算入）
    y, m = (start.year + (start.month // 12), start.month % 12 + 1)  # 一月後の月
    try:
        return datetime.date(y, m, start.day) - datetime.timedelta(days=1)
    except ValueError:                                  # 応当日がない
        nxt = datetime.date(y + (m // 12), m % 12 + 1, 1)
        return nxt - datetime.timedelta(days=1)


EX1 = datetime.date(2026, 8, 2)   # 新築の日
EX2 = datetime.date(2027, 1, 30)  # 滅失の日（起算日が1月31日になる）


def _md(d):
    return '%d月%d日' % (d.month, d.day)


SHEET = dict(
    id='D-01',
    law='不動産登記法',
    articles='不動産登記法第36条・第37条・第42条・第47条・第49条・第51条・第57条・第58条・第164条、民法第140条、民法第143条',
    conclusion=[
        '表示に関する登記の多くは、**一月以内**に申請する義務がある。怠ると十万円以下の過料（法第164条第1項）。',
        '一月は同じでも**起算点**が違う。表題登記は「所有権の取得の日」、変更は「変更があった日」、滅失は「滅失の日」、合体は「合体の日」。',
        '**分筆・合筆、更正の登記、建物の分割・区分・合併には期限がない**。表示の登記で過料の対象になる申請は、法第164条第1項に列挙されたものだけである。',
    ],
    blocks=[
        dict(kind='table', title='この日から一月以内（起算点と根拠）',
             head=['登記', '起算点', '土地', '建物'],
             rows=[['表題登記', '所有権の取得の日', '法第36条', '法第47条第1項'],
                   ['変更（地目・地積、建物の表題部）', '変更があった日', '法第37条第1項', '法第51条第1項'],
                   ['変更の後に名義人になった人', '表題部所有者の更正の登記または所有権の登記があった日', '法第37条第2項', '法第51条第2項'],
                   ['滅失', '滅失の日', '法第42条', '法第57条'],
                   ['合体による登記等', '合体の日（合体の後に持分を取得した人は、その取得の日）', '―', '法第49条第1項・第3項'],
                   ['共用部分である旨の規約の廃止', '廃止の日（廃止の後に取得した人は、その取得の日）', '―', '法第58条第6項・第7項']]),
        dict(kind='check', title='期限があるもの、ないもの',
             yes_label='一月以内の申請義務あり', cols_yes=2,
             yes=['表題登記', '地目・地積の変更', '建物の表題部の変更', '土地・建物の滅失', '合体による登記等', '共用部分の規約の廃止'],
             no_label='期限の定めがない', cols_no=2,
             no=['分筆・合筆', '地目・地積の更正', '建物の表題部の更正', '建物の分割・区分・合併', '表題部所有者の住所の変更'],
             ),
    ],
    example=dict(kind='計算例', title='一月の数え方（初日は数えない）',
                 lines=[f'{_md(EX1)}に新築：初日を数えず{_md(EX1 + datetime.timedelta(days=1))}から数える。一月後の応当日の前日、**{_md(_deadline(EX1))}**までに申請する（民法第140条、民法第143条第2項）。',
                        f'{_md(EX2)}に取り壊した：{_md(EX2 + datetime.timedelta(days=1))}から数える。翌月に応当日がないので、その月の末日の**{_md(_deadline(EX2))}**まで（民法第143条第2項ただし書）。',
                        ]),
    traps=['区分建物を新築した人から買った人には、表題登記の申請義務がない。法第47条第1項が取得者に義務を課すのは、**区分建物以外**の表題登記がない建物だけである。',
           '同じ一月でも、変更の後に名義人になった人は「**更正の登記または所有権の登記があった日**」から数える（法第37条第2項・第51条第2項）。',
           '表示の登記の「一月」と、権利の登記の「三年」（相続。法第76条の2）・「二年」（住所の変更。法第76条の5、過料は五万円以下）を混ぜない。'],
    basis=['不動産登記法第36条・第37条・第42条・第47条・第49条・第51条・第57条・第58条・第164条', '民法第140条、民法第143条'],
    more=['kigen-suuji-zukan/01-fudousan-touki-hou-kigen-suuji-zukan.md'],
    claims=[
        ('不動産登記法', '36', 'その所有権の取得の日から一月以内に、表題登記を申請しなければならない'),
        ('不動産登記法', '37', 'その変更があった日から一月以内に'),
        ('不動産登記法', '37', 'その者に係る表題部所有者についての更正の登記又は所有権の登記があった日から一月以内に'),
        ('不動産登記法', '42', 'その滅失の日から一月以内に'),
        ('不動産登記法', '47', '新築した建物又は区分建物以外の表題登記がない建物の所有権を取得した者は'),
        ('不動産登記法', '49', '当該合体の日から一月以内に'),
        ('不動産登記法', '49', 'その持分の取得の日から一月以内に'),
        ('不動産登記法', '51', '当該変更があった日から一月以内に'),
        ('不動産登記法', '57', 'その滅失の日から一月以内に、当該建物の滅失の登記を申請しなければならない'),
        ('不動産登記法', '58', '当該規約の廃止の日から一月以内に'),
        ('不動産登記法', '164', '十万円以下の過料に処する'),
        ('不動産登記法', '164', '五万円以下の過料に処する'),
        ('民法', '140', '期間の初日は、算入しない'),
        ('民法', '143', '最後の月に応当する日がないときは、その月の末日に満了する'),
    ],
    header=dict(l1='表示の登記の', l2='期限と起算点', hl='起算点',
                left='a wall calendar with one day circled by a plain red ring and a small hourglass, all without any text',
                right='a small house and a plot of land with a blank document and a pen beside them, all without any text'),
    zukai=dict(title='表示の登記の期限', topics='一月以内・起算点・期限のない登記',
               cards=[
                   dict(h='表題登記は取得の日から', illust='A newly built house with a key being handed over; a calendar page next to it with one day circled.', words=[], tag='所有権の取得の日'),
                   dict(h='変更は変更があった日から', illust='A house with a new extension attached on one side; a calendar page with one day circled.', words=[], tag='変更があった日'),
                   dict(h='滅失は滅失の日から', illust='A house being demolished by a small excavator; a calendar page with one day circled.', words=[], tag='滅失の日'),
                   dict(h='合体は合体の日から', illust='Two small buildings joined by a new middle section into one building; a calendar page with one day circled.', words=[], tag='合体の日'),
                   dict(h='初日は数えない', illust='A calendar with the first day crossed out lightly and counting starting from the next day, shown by small dots.', words=[], tag='翌日から一月'),
                   dict(h='分筆・合筆に期限はない', illust='A plot of land divided by a dashed line, next to a calendar with no circled day.', words=[], tag='期限の定めなし'),
               ]),
)


def verify():
    assert _deadline(EX1) == datetime.date(2026, 9, 2), _deadline(EX1)
    assert _deadline(EX2) == datetime.date(2027, 2, 28), _deadline(EX2)
    assert _deadline(datetime.date(2026, 3, 31)) == datetime.date(2026, 4, 30)
