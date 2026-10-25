"""noteに貼るための画像を書き出す：朝・夜の「問題」ページだけ（解答・解説は書き出さない）。
印刷と同じ見た目（ヘッダー・フッターなし、背景あり、A4）でPDFにしてから、ページごとにPNGにする（images/ に dayNNN-am.png、2枚あれば dayNNN-pm-1.png・-2.png）。
PNGには文書情報（作成者・PCのユーザー名・ファイルの場所など）を入れない。
必要なもの：Google Chrome または Microsoft Edge、Python のパッケージ pypdfium2 と pillow（pip install pypdfium2 pillow）。
使い方: python daily-drill/make_images.py                 （全日）
        python daily-drill/make_images.py day001 day002   （日を絞る）
        python daily-drill/make_images.py --width 1600    （画像の横幅。既定 1240 ピクセル＝A4を150dpi）"""
import glob
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_pdf as MP  # noqa: E402

IMG = os.path.join(HERE, 'images')


def main():
    try:
        import pypdfium2 as pdfium
        from PIL import Image
    except ImportError:
        sys.exit('pypdfium2 と pillow がない。 pip install pypdfium2 pillow で入れる。')
    args = sys.argv[1:]
    width = 1240
    if '--width' in args:
        k = args.index('--width')
        width = int(args[k + 1])
        del args[k:k + 2]
    files = sorted(f for f in glob.glob(os.path.join(MP.OUT, 'day*-am.html')) + glob.glob(os.path.join(MP.OUT, 'day*-pm.html')))
    if args:
        files = [f for f in files if any(os.path.basename(f).startswith(p) for p in args)]
    os.makedirs(IMG, exist_ok=True)
    browser = MP.find_browser()
    n_img, ng = 0, 0
    with tempfile.TemporaryDirectory() as td:
        for i, html in enumerate(files, 1):
            name = os.path.basename(html)[:-5]
            pdf = os.path.join(td, name + '.pdf')
            if not MP.render(browser, html, pdf, os.path.join(td, 'profile')):
                print(f'NG {name}: PDFにできなかった'); ng += 1; continue
            doc = pdfium.PdfDocument(pdf)
            for k in range(len(doc)):
                page = doc[k]
                scale = width / page.get_width()
                im = page.render(scale=scale).to_pil().convert('RGB')
                im = im.quantize(colors=64, method=Image.Quantize.MEDIANCUT)   # 色数を減らしてファイルを約3分の1に（文字・図の見た目は同じ）
                out = os.path.join(IMG, f'{name}.png' if len(doc) == 1 else f'{name}-{k + 1}.png')
                im.save(out, 'PNG', optimize=True)      # 文書情報（テキストのチャンク）は付けない
                n_img += 1
            doc.close()
            if i % 50 == 0:
                print(f'… {i}/{len(files)}')
    print(f'{len(files)}ページ分から {n_img}枚の画像を {IMG} に書き出し。NG {ng}件')
    sys.exit(1 if ng else 0)


if __name__ == '__main__':
    main()
