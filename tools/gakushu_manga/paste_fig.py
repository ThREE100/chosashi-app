"""ChatGPT・Codexが作ったページの画像に、Claudeが作った正確な図を、プロンプトで指定した枠にそのまま貼り直す。
使い方：python3 tools/gakushu_manga/paste_fig.py <生成した画像> <プロンプトのmd> <ページ番号> [出力（省略時は _fig を付けた名前）]
図は、プロンプトのmdと同じフォルダの fig/<名前>.png を使う。生成した画像は 1024×1536 にそろえてから貼る（縦横比を保ち中央で切る）。"""
import os
import re
import sys
from PIL import Image

W, H = 1024, 1536


def slots(md_path, page):
    out = []
    for line in open(md_path, encoding='utf-8'):
        m = re.match(r'\|\s*(\d+)\s*\|\s*`([^`]+)\.png`\s*\|\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\s*\|', line)
        if m and int(m.group(1)) == page:
            out.append((m.group(2), tuple(int(m.group(i)) for i in range(3, 7))))
    return out


def fit(img):
    img = img.convert('RGB')
    s = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    l, t = (img.width - W) // 2, (img.height - H) // 2
    return img.crop((l, t, l + W, t + H))


def main(src, md, page, dst=None):
    sl = slots(md, int(page))
    if not sl:
        sys.exit(f'{page}ページ目に図の枠がない')
    base = fit(Image.open(src))
    for name, (x, y, w, h) in sl:
        fig = Image.open(os.path.join(os.path.dirname(md), 'fig', name + '.png')).convert('RGB').resize((w, h), Image.LANCZOS)
        base.paste(fig, (x, y))
    dst = dst or re.sub(r'(\.\w+)$', r'_fig\1', src)
    base.save(dst)
    print('貼り直した：', dst, [n for n, _ in sl])


if __name__ == '__main__':
    main(*sys.argv[1:])
