"""つなぎの投稿（F2〜F4）に使える素材の一覧（filler-pool.csv）を作る。

素材は、すでにリポジトリにあるもの：
- テーマ別解説（note-articles/topics/*.md）
- 苦手分析シリーズ（note-articles/column/nigate-*.md）
- 4コマ解説図解のプロンプト（tools/drill/manga/D*_prompt.md）
- 論点別の復習用図解（note-articles/fukushu-ronten-zukai/T*）
使うと決めたら、schedule.csv の該当行の source と title に書き写す（このスクリプトは書き換えない）。
"""
import csv
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))


def rel(p):
    return os.path.relpath(p, ROOT)


def first_title(path):
    for line in open(path, encoding='utf-8'):
        m = re.match(r'#+\s*(.+)', line.strip())
        if m:
            t = m.group(1)
            t = re.sub(r'^【土地家屋調査士受験生向け】', '', t)
            return t.strip()
    return ''


def main():
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'note-articles', 'topics', '*.md'))):
        if os.path.basename(p) == 'README.md':
            continue
        rows.append(('F2 個別テーマ解説', rel(p), first_title(p), '1080×1440で図解を作り直す'))
    for p in sorted(glob.glob(os.path.join(ROOT, 'note-articles', 'column', 'nigate-*.md'))):
        rows.append(('F2 個別テーマ解説（苦手分析）', rel(p), first_title(p), '判定の流れ図を1枚にまとめる'))
    for p in sorted(glob.glob(os.path.join(ROOT, 'note-articles', 'fukushu-ronten-zukai', 'T*'))):
        if os.path.isdir(p):
            rows.append(('F2 個別テーマ解説（論点別の復習図解）', rel(p), os.path.basename(p), 'フォルダ内のプロンプトの図解（複数枚）から選ぶ'))
    for p in sorted(glob.glob(os.path.join(ROOT, 'tools', 'drill', 'manga', 'D*_prompt.md'))):
        t = ''
        for line in open(p, encoding='utf-8'):
            m = re.search(r'4コマ解説図解(D\d+)～(.+?)～', line)
            if m:
                t = f'{m.group(1)} {m.group(2)}'
                break
        rows.append(('F3 4コマ解説', rel(p), t, '縦1080×1920を3:4（1080×1440）に作り直すか、中央を切り出す'))
    out = os.path.join(HERE, 'filler-pool.csv')
    with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['使いみち', 'source', 'title', 'メモ'])
        w.writerows(rows)
    print(f'{len(rows)}件を書き出した：{out}')


if __name__ == '__main__':
    main()
