"""Instagramの投稿スケジュール（schedule.csv）を作る。

使い方：
    python3 note-unei/instagram/make_schedule.py                    # 開始日 2026-11-09
    python3 note-unei/instagram/make_schedule.py --start 2026-12-01

決めたこと（2026-10-30、README.md の「1. 全体の形」）：
- 年度は令和8年度から平成17年度へさかのぼる（22年度）。
- 1つの年度のかたまり（ブロック）は24枚＝問1〜問20（20枚）＋つなぎの4枚（F1〜F4）。24は3の倍数なので、
  年度の切れ目がプロフィールのグリッド（3列）の行の切れ目にそろう。
- 1日3枚。1日＝グリッドの1行。1ブロックは8日。
- グリッドは新しい投稿が左上に来て、1行は「左＝最後に投稿したもの」になる。そこで、その日の3枚は
  右から先に投稿する（Q3→Q2→Q1の順）と、行が左から Q1・Q2・Q3 と並ぶ。
  `slot` が投稿する順番、`grid_col` がグリッドで置かれる列（1＝左）。
"""
import argparse
import csv
import datetime as dt
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))

# 令和8年度 → 平成17年度
YEARS = [('R', n) for n in range(8, 0, -1)] + [('H', n) for n in range(30, 16, -1)]
FILLER_ROLE = {
    1: '年度のまとめ（この年度の狙われどころ一覧・次の年度の予告）',
    2: '個別テーマ解説（note-articles/topics など）',
    3: '4コマ解説（tools/drill/manga）',
    4: '案内（メンバーシップ・毎朝ドリル・Xのいずれか）',
}
COLS = {1: '左', 2: '中', 3: '右'}


def year_label(k, n):
    return f'令和{n}年度' if k == 'R' else f'平成{n}年度'


def year_code(k, n):
    return f'{k}{n:02d}'


def article_info(k, n, q):
    folder = os.path.join(ROOT, 'note-articles', f'{k.lower()}{n}-mondai')
    hits = sorted(glob.glob(os.path.join(folder, f'q{q:02d}-*.md')))
    if len(hits) != 1:
        raise SystemExit(f'{year_label(k, n)} 第{q}問の記事が{len(hits)}件ある：{folder}')
    path = hits[0]
    head = open(path, encoding='utf-8').readline()
    m = re.search(r'第\d+問(?:（改）)?[〜～](.+?)[〜～]\s*$', head)
    if not m:
        raise SystemExit(f'タイトルを読み取れない：{path}')
    return os.path.relpath(path, ROOT), m.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--start', default='2026-11-09', help='最初の日（YYYY-MM-DD）')
    args = ap.parse_args()
    start = dt.date.fromisoformat(args.start)

    rows = []
    seq = 0
    day = 0
    for k, n in YEARS:
        code = year_code(k, n)
        block = []  # グリッドで左→右、上→下に並べたい順
        for q in range(1, 21):
            src, title = article_info(k, n, q)
            block.append(dict(item=f'Q{q:02d}', kind='過去問の図解', source=src, title=title))
        for f in range(1, 5):
            block.append(dict(item=f'F{f}', kind='つなぎ', source='', title=FILLER_ROLE[f]))
        assert len(block) == 24
        for d in range(8):
            day += 1
            date = start + dt.timedelta(days=day - 1)
            three = block[d * 3:d * 3 + 3]  # 左・中・右
            # 投稿する順番は右→中→左
            for slot, col in enumerate((3, 2, 1), start=1):
                seq += 1
                it = three[col - 1]
                rows.append({
                    'seq': seq, 'date': date.isoformat(), 'weekday': '月火水木金土日'[date.weekday()],
                    'day': day, 'slot': slot, 'grid_col': COLS[col],
                    'block': f'{code}（{year_label(k, n)}）', 'day_in_block': d + 1,
                    'item': it['item'], 'kind': it['kind'], 'title': it['title'], 'source': it['source'],
                    'feed_image': f'ig{seq:03d}_{code}_{it["item"]}.png',
                    'story_image': '', 'status': '未作成',
                })
    out = os.path.join(HERE, 'schedule.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f'{len(rows)}枚・{day}日分を書き出した：{out}（{rows[0]["date"]}〜{rows[-1]["date"]}）')


if __name__ == '__main__':
    main()
