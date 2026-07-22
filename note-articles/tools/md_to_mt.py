#!/usr/bin/env python3
"""
note-articles配下のMarkdown解説記事(qNN-*.md)を、note.comのインポート機能が
受け付けるMT(Movable Type)形式のテキストファイルに一括変換するスクリプト。

使い方:
    python md_to_mt.py <記事フォルダ> [出力ファイル]

例:
    python md_to_mt.py ../r6-mondai ../exports/r6-mondai.mt.txt
    python md_to_mt.py ../r7-mondai ../exports/r7-mondai.mt.txt

新しい年度のフォルダ(例: r8-mondai)ができたら、そのフォルダパスを指定して
同じスクリプトをそのまま再利用できる。

変換時の方針:
    - 「## タイトル」「**出題年度：...**」「問題文の引用(> ブロック)」
      「各肢の解説」「まとめ表→箇条書きに変換」「結論文」「正解」
      「見出し画像用フレーズ」を本文として出力する。
    - noteの本文エディタは表組み(Markdownテーブル)を描画できないため、
      「まとめ表」は必ず箇条書き(<ul><li>)に変換する。
    - 「このまま使える点／使う前に確認したい点」(確認事項ブロック)は
      執筆時の内部メモであり読者向けの本文ではないため、出力からは除外する。
    - noteにインポートされた記事はすべて下書き状態になるため、
      STATUSは Draft に固定する(公開は手動で行う想定)。
"""

import sys
import re
import glob
import os
from html import escape


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def inline_md_to_html(text):
    """1行程度のインライン要素(太字)をHTMLに変換する。"""
    text = escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def parse_table_to_bullets(table_block):
    """
    | 肢 | 判定 | ポイント |
    |---|---|---|
    | ア | 誤 | ... |
    という形式のMarkdownテーブルを、
    <li><strong>ア（誤）</strong> ...</li>
    形式の箇条書きHTMLに変換する。
    """
    lines = [l.strip() for l in table_block.strip().splitlines() if l.strip()]
    rows = []
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        # 区切り行(|---|---|---|)はスキップ
        if all(re.fullmatch(r"-+", c) for c in cells):
            continue
        # ヘッダー行(「肢」「語句」等の見出し行)はスキップ。
        # 通常の「肢/判定/ポイント」表だけでなく、穴埋め問題の「語句/判定/ポイント」表など
        # 1列目の見出し語が変わる形式にも対応できるよう、2列目が「判定」であることで判定する。
        if cells[0] in ("肢", "語句") or cells[1] == "判定":
            continue
        rows.append(cells)

    items = []
    for label, verdict, point in rows:
        items.append(
            f"<li><strong>{escape(label)}（{escape(verdict)}）</strong>　{inline_md_to_html(point)}</li>"
        )
    return "<ul>\n" + "\n".join(items) + "\n</ul>"


def parse_article(md_text):
    """
    1本の記事Markdownを、MTエントリ用のフィールドに分解する。
    戻り値: dict(title, body_html)
    """
    lines = md_text.splitlines()

    # タイトル(最初の "## " 行)
    title = ""
    for l in lines:
        if l.startswith("## "):
            title = l[3:].strip()
            break

    body_parts = []

    # 出典行(**出題年度：...**)
    m = re.search(r"^\*\*(出題年度：.+?)\*\*", md_text, re.M)
    if m:
        body_parts.append(f"<p><strong>{escape(m.group(1))}</strong></p>")

    # 問題文の引用ブロック(連続する "> " 行)
    quote_lines = []
    in_quote = False
    for l in lines:
        if l.startswith(">"):
            in_quote = True
            quote_lines.append(l.lstrip(">").strip())
        elif in_quote and l.strip() == "":
            quote_lines.append("")
        elif in_quote:
            break
    if quote_lines:
        non_empty = [inline_md_to_html(q) for q in quote_lines if q]
        quote_html = "<br><br>\n".join(non_empty)
        body_parts.append(f"<blockquote><p>{quote_html}</p></blockquote>")

    # 「### まとめ表」または「### まとめ」より前、引用より後の本文
    # (導入文 + 各肢解説)
    after_quote = md_text.split("\n\n", 0)
    # 引用ブロックの終端位置を再検出してテキストを分割する
    quote_end_idx = None
    if quote_lines:
        # 最後の引用行が現れる位置を探す
        idx = md_text.find("\n> " + quote_lines[-1]) if quote_lines[-1] else -1
        # フォールバック: 最初の "1　" のような選択肢行を含む最後の "> " 行以降
    # シンプルに「まとめ表」または「まとめ」見出しで本文全体を前後に分割する
    summary_match = re.search(r"^###\s*まとめ表?\s*$", md_text, re.M)
    if not summary_match:
        raise ValueError("まとめ表(まとめ)セクションが見つかりません")

    head_text = md_text[: summary_match.start()]
    tail_text = md_text[summary_match.end():]

    # head_text から「導入文＋各肢解説」部分だけを取り出す
    # (タイトル行・出典行・引用ブロックの後ろから)
    quote_block_pattern = re.compile(r"(^>.*(?:\n>.*|\n)*)", re.M)
    qmatches = list(quote_block_pattern.finditer(head_text))
    if qmatches:
        explain_text = head_text[qmatches[-1].end():]
    else:
        explain_text = head_text

    # 導入文・各肢見出し(### ア：〜)・本文・「たとえば」段落をHTML化
    explain_lines = explain_text.strip("\n").split("\n")
    buf_paragraph = []

    def flush_paragraph():
        if buf_paragraph:
            text = " ".join(buf_paragraph).strip()
            if text and text != "---":
                body_parts.append(f"<p>{inline_md_to_html(text)}</p>")
            buf_paragraph.clear()

    for l in explain_lines:
        if l.strip() == "---":
            flush_paragraph()
            continue
        if l.startswith("### "):
            flush_paragraph()
            body_parts.append(f"<h3>{inline_md_to_html(l[4:].strip())}</h3>")
        elif l.strip() == "":
            flush_paragraph()
        else:
            buf_paragraph.append(l.strip())
    flush_paragraph()

    # まとめ表 → 箇条書き
    # tail_text の先頭のテーブル部分を抽出(次の空行2連続、または次の見出しまで)
    table_match = re.search(r"(\|.+\|(?:\n\|.+\|)*)", tail_text)
    if table_match:
        body_parts.append("<h3>まとめ</h3>")
        body_parts.append(parse_table_to_bullets(table_match.group(1)))
        after_table = tail_text[table_match.end():]
    else:
        # 既に箇条書き形式(- **ア（誤）** ...)の場合はそのまま使う
        bullets_match = re.search(r"((?:^-\s+\*\*.+$\n?)+)", tail_text, re.M)
        if bullets_match:
            body_parts.append("<h3>まとめ</h3>")
            items = []
            for bl in bullets_match.group(1).strip().splitlines():
                bl = bl.strip().lstrip("- ").strip()
                items.append(f"<li>{inline_md_to_html(bl)}</li>")
            body_parts.append("<ul>\n" + "\n".join(items) + "\n</ul>")
            after_table = tail_text[bullets_match.end():]
        else:
            after_table = tail_text

    # 結論文 + 正解行(「**正解：」を含む段落まで)を抽出
    conclusion_match = re.search(r"^\*\*正解：.+?\*\*\s*$", after_table, re.M)
    if conclusion_match:
        between = after_table[: conclusion_match.start()]
        for l in between.strip().splitlines():
            l = l.strip()
            if l and l != "---":
                body_parts.append(f"<p>{inline_md_to_html(l)}</p>")
        body_parts.append(f"<p>{inline_md_to_html(conclusion_match.group(0).strip())}</p>")
        rest_after_conclusion = after_table[conclusion_match.end():]
    else:
        rest_after_conclusion = after_table

    # 見出し画像用フレーズ セクションを抽出(確認事項ブロックはスキップして無視)
    headline_match = re.search(
        r"^##\s*見出し画像用フレーズ\s*$(.*)", rest_after_conclusion, re.M | re.S
    )
    if headline_match:
        body_parts.append("<h3>見出し画像用フレーズ</h3>")
        items = []
        for l in headline_match.group(1).strip().splitlines():
            l = l.strip()
            if l.startswith("- "):
                items.append(f"<li>{inline_md_to_html(l[2:].strip())}</li>")
        if items:
            body_parts.append("<ul>\n" + "\n".join(items) + "\n</ul>")

    body_html = "\n".join(body_parts)
    return {"title": title, "body_html": body_html}


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
        print("使い方: python md_to_mt.py <記事フォルダ> [出力ファイル] [author]")
        sys.exit(1)

    folder = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(folder, "_export.mt.txt")
    author = sys.argv[3] if len(sys.argv) > 3 else "chosashi-note"

    # DATEはインポート時の便宜上の値。Movable Type形式の日付書式(MM/DD/YYYY HH:MM:SS AM/PM)。
    # 実際の公開日時は note 側で公開操作をした時点のものに変わる場合がある。
    import datetime

    base_date = datetime.datetime(2026, 1, 1, 10, 0, 0)

    md_files = sorted(glob.glob(os.path.join(folder, "q*.md")))
    if not md_files:
        print(f"警告: {folder} に qNN-*.md 形式のファイルが見つかりませんでした。")
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
