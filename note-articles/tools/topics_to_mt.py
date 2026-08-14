#!/usr/bin/env python3
"""
note-articles/topics配下の分野別記事(1問1答形式ではない、任意の見出し構成の
記事)を、note.comのインポート機能が受け付けるMT(Movable Type)形式の
テキストファイルに一括変換するスクリプト。

使い方:
    python topics_to_mt.py <記事フォルダ> [出力ファイル]

例:
    python topics_to_mt.py ../topics ../exports/topics.mt.txt

md_to_mt.py との違い:
    topics配下の記事は「出題年度」「問題文の引用」「まとめ表→正解」という
    q-article特有の固定構造を持たない(見出しの数・種類が記事ごとに違う)。
    そのため、このスクリプトは決め打ちのセクション抽出ではなく、
    タイトル行以降を「見出し(###)・段落・箇条書き・引用・表」という
    汎用Markdown要素として順番にHTML化する。

変換時の方針:
    - 「## タイトル」の次行以降、本文終端(下記の除外セクション開始)までを
      本文として出力する。
    - 「**対象条文：...**」のような太字のみの1行は<p><strong>...</strong></p>
      として出力する。
    - 「### 見出し」は<h3>に変換する。
    - 「> 引用」の連続行は<blockquote>に変換する。
    - 「- 箇条書き」の連続行は<ul><li>に変換する(表内の**太字**はinlineで変換)。
    - Markdownの表組み(| ... |)は、noteが表組みを描画できないため、
      1行目(ヘッダー)をラベルとして使い、各データ行を
      「先頭列を<strong>見出し</strong>にし、残りの列を『ヘッダー名：値』で
      連結した<li>」に変換する。
    - 「## 見出し画像用フレーズ」は<h3>+<ul>として出力する。
    - 以下は執筆時の内部メモであり読者向けの本文ではないため、出力から除外する:
        - 「**このまま使える点／使う前に確認したい点**」の確認事項ブロック
          (直前の`---`区切りから、次の`---`または次の見出しまで)
        - 「見出し画像用フレーズ」より後に続く「参照した過去問記事一覧」
          「対象とした過去問記事」等の出典メモ見出し以降すべて
    - noteにインポートされた記事はすべて下書き状態になるため、
      STATUSは Draft に固定する(公開は手動で行う想定)。
"""

import sys
import re
import glob
import os
import datetime
from html import escape


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def inline_md_to_html(text):
    """1行程度のインライン要素(太字・リンク)をHTMLに変換する。"""
    text = escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Markdownリンク。リポジトリ内の.mdへの相対リンク(シリーズの回またぎリンク等)は
    # note.com上では解決できないため、リンクを外してラベルの文字列だけを残す。
    # 外部URL(http/https)へのリンクはそのまま<a>タグにする。
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2">\1</a>',
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)\s]*\)", r"\1", text)
    return text


def table_block_to_bullets_html(table_block):
    """
    任意の列数のMarkdown表を、ヘッダー名付きの箇条書きHTMLに変換する。
    1列目を項目名(<strong>)、2列目以降を「ヘッダー：値」で連結する。
    """
    lines = [l.strip() for l in table_block.strip().splitlines() if l.strip()]
    rows = []
    header = None
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        if header is None:
            header = cells
            continue
        rows.append(cells)

    items = []
    for row in rows:
        if not row:
            continue
        lead = inline_md_to_html(row[0])
        rest_parts = []
        for i in range(1, len(row)):
            label = header[i] if header and i < len(header) else ""
            value = inline_md_to_html(row[i])
            if label:
                rest_parts.append(f"{inline_md_to_html(label)}：{value}")
            else:
                rest_parts.append(value)
        rest = "／".join(p for p in rest_parts if p)
        if rest:
            items.append(f"<li><strong>{lead}</strong>　{rest}</li>")
        else:
            items.append(f"<li><strong>{lead}</strong></li>")
    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def strip_excluded_sections(md_text):
    """
    確認事項ブロックと、その後の「参照した過去問記事一覧」等の出典メモ見出し
    以降を本文から除外する。
    """
    # 確認事項ブロックの開始位置(直前の "---" ごと切り落とす)。
    # 「## 見出し画像用フレーズ」の手前で止める(非貪欲マッチ)ことで、
    # 確認事項ブロックの後ろに続く見出し画像用フレーズ節を巻き込まないようにする。
    conf_match = re.search(
        r"\n-{3,}\n\s*\*\*このまま使える点／使う前に確認したい点\*\*.*?"
        r"(?=\n##\s*見出し画像用フレーズ|\Z)",
        md_text,
        re.S,
    )
    if conf_match:
        head = md_text[: conf_match.start()]
        tail = md_text[conf_match.end():]
    else:
        head = md_text
        tail = ""

    # tail側に残る「見出し画像用フレーズ」だけは本文として使うため拾っておく
    headline_match = re.search(
        r"(^##\s*見出し画像用フレーズ\s*$.*?)(?=^#{1,6}\s|\Z)",
        tail,
        re.M | re.S,
    )
    headline_section = headline_match.group(1) if headline_match else ""

    return head, headline_section


def markdown_body_to_html(md_text):
    """
    タイトル行を除いた本文Markdownを、順番にHTML要素へ変換する。
    """
    lines = md_text.split("\n")
    body_parts = []
    buf_paragraph = []
    buf_quote = []
    buf_bullets = []
    buf_table = []

    def flush_paragraph():
        if buf_paragraph:
            text = " ".join(buf_paragraph).strip()
            if text and text != "---":
                body_parts.append(f"<p>{inline_md_to_html(text)}</p>")
            buf_paragraph.clear()

    def flush_quote():
        if buf_quote:
            html_lines = [inline_md_to_html(q) for q in buf_quote if q.strip()]
            body_parts.append(
                "<blockquote><p>" + "<br>\n".join(html_lines) + "</p></blockquote>"
            )
            buf_quote.clear()

    def flush_bullets():
        if buf_bullets:
            items = "\n".join(
                f"<li>{inline_md_to_html(b)}</li>" for b in buf_bullets
            )
            body_parts.append(f"<ul>\n{items}\n</ul>")
            buf_bullets.clear()

    def flush_table():
        if buf_table:
            body_parts.append(table_block_to_bullets_html("\n".join(buf_table)))
            buf_table.clear()

    def flush_all():
        flush_paragraph()
        flush_quote()
        flush_bullets()
        flush_table()

    for raw in lines:
        l = raw.rstrip()
        stripped = l.strip()

        if stripped.startswith("|"):
            flush_paragraph()
            flush_quote()
            flush_bullets()
            buf_table.append(stripped)
            continue
        else:
            flush_table()

        if stripped.startswith(">"):
            flush_paragraph()
            flush_bullets()
            buf_quote.append(stripped.lstrip(">").strip())
            continue
        else:
            flush_quote()

        if re.match(r"^-\s+", stripped):
            flush_paragraph()
            buf_bullets.append(re.sub(r"^-\s+", "", stripped))
            continue
        else:
            flush_bullets()

        if stripped.startswith("### "):
            flush_paragraph()
            body_parts.append(f"<h3>{inline_md_to_html(stripped[4:].strip())}</h3>")
            continue

        if stripped.startswith("#### "):
            flush_paragraph()
            body_parts.append(f"<h4>{inline_md_to_html(stripped[5:].strip())}</h4>")
            continue

        if stripped == "":
            flush_paragraph()
            continue

        if stripped == "---":
            flush_paragraph()
            continue

        buf_paragraph.append(stripped)

    flush_all()
    return "\n".join(body_parts)


def headline_section_to_html(headline_section):
    if not headline_section:
        return ""
    lines = headline_section.strip().splitlines()
    items = []
    for l in lines[1:]:
        l = l.strip()
        if l.startswith("- "):
            items.append(f"<li>{inline_md_to_html(l[2:].strip())}</li>")
    if not items:
        return ""
    return "<h3>見出し画像用フレーズ</h3>\n<ul>\n" + "\n".join(items) + "\n</ul>"


def parse_article(md_text):
    lines = md_text.splitlines()
    title = ""
    title_line_idx = None
    for i, l in enumerate(lines):
        if l.startswith("## "):
            title = l[3:].strip()
            title_line_idx = i
            break
    if title_line_idx is None:
        raise ValueError("タイトル行(## ...)が見つかりません")

    rest = "\n".join(lines[title_line_idx + 1:])
    head, headline_section = strip_excluded_sections(rest)

    body_html_parts = [markdown_body_to_html(head)]
    headline_html = headline_section_to_html(headline_section)
    if headline_html:
        body_html_parts.append(headline_html)

    return {"title": title, "body_html": "\n".join(p for p in body_html_parts if p)}


def build_mt_entry(title, body_html, author, date_str):
    return (
        f"AUTHOR: {author}\n"
        f"TITLE: {title}\n"
        f"STATUS: Draft\n"
        f"ALLOW COMMENTS: 1\n"
        f"CONVERT BREAKS: 0\n"
        f"DATE: {date_str}\n"
        f"-----\n"
        f"BODY:\n"
        f"{body_html}\n"
        f"-----\n"
        f"--------\n"
    )


def main():
    if len(sys.argv) < 2:
        print("使い方: python topics_to_mt.py <記事フォルダ> [出力ファイル] [author]")
        sys.exit(1)

    folder = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(folder, "_export.mt.txt")
    author = sys.argv[3] if len(sys.argv) > 3 else "chosashi-note"

    base_date = datetime.datetime(2026, 1, 1, 10, 0, 0)

    md_files = sorted(glob.glob(os.path.join(folder, "*.md")))
    md_files = [p for p in md_files if os.path.basename(p) != "README.md"]
    if not md_files:
        print(f"警告: {folder} に .md ファイルが見つかりませんでした。")
        sys.exit(1)

    entries = []
    errors = []
    for i, path in enumerate(md_files):
        try:
            text = read_file(path)
            parsed = parse_article(text)
            date_str = (base_date + datetime.timedelta(minutes=i)).strftime(
                "%m/%d/%Y %I:%M:%S %p"
            )
            entries.append(build_mt_entry(parsed["title"], parsed["body_html"], author, date_str))
            print(f"OK: {os.path.basename(path)} -> 「{parsed['title']}」")
        except Exception as e:
            errors.append((path, str(e)))
            print(f"NG: {os.path.basename(path)} -> {e}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(entries))

    print(f"\n{len(entries)}件を {out_path} に書き出しました。")
    if errors:
        print(f"{len(errors)}件でエラーが発生しました:")
        for path, err in errors:
            print(f"  - {os.path.basename(path)}: {err}")


if __name__ == "__main__":
    main()
