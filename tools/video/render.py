#!/usr/bin/env python3
"""KaisetsuScript（台本JSON）から解説動画（MP4）を作る。

    python3 render.py episodes/R7_Q21_ep01.json            # 動画・サムネイル・YouTube用メタデータを out/<id>/ に書き出す
    python3 render.py episodes/R7_Q21_ep01.json --tts voicevox   # ローカルPCで VOICEVOX を使う
    python3 render.py episodes/R7_Q21_ep01.json --preview  # 音声なしで各場面の静止画だけを書き出す（台本の見た目の確認用）

台本の形式は README.md の「KaisetsuScript の書き方」を参照。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import wave

import numpy as np

import characters
import chars_prep
import jingle
import tts

HERE = os.path.dirname(os.path.abspath(__file__))
FPS_MOUTH = 12.5          # 口の開閉を切り替える回数（1秒あたり）
PAGE_CHARS = 56           # 字幕1ページの最大文字数（44px・2行。1行に約31文字入る）
GAP = 0.28                # 同じ話者のページの間のすき間（秒）
GAP_TURN = 0.45           # 話者が替わるときのすき間（秒）
FPS = 30                  # 動画のコマ数（図の移動・切り替えの動きはこの細かさで作る）
T_ZOOM = 0.55             # 同じ図の中で、見せる範囲を動かす（ズーム・移動）のにかける時間（秒）
T_FADE = 0.40             # 別の図に切り替える（重ねて入れ替える）時間（秒）
LEAD = 0.15               # 図が動き終わってから、話し始めるまでの間（秒）
LEAD_UI = 0.22            # 注釈・強調・カードの追加だけのとき、話し始めるまでの間（秒）
STAGE_KINDS = ("image", "bullets", "card", "cards", "rows", "html")


def split_pages(text: str, limit: int = PAGE_CHARS) -> list[str]:
    """文の切れ目で字幕のページに分ける。"""
    sents = [s for s in re.split(r"(?<=[。！？!?])", text) if s.strip()]
    pages, cur = [], ""
    for s in sents:
        while len(s) > limit:  # 1文が長すぎるときは読点で切る
            cut = s.rfind("、", 0, limit)
            cut = cut + 1 if cut > 10 else limit
            if cur:
                pages.append(cur)
                cur = ""
            pages.append(s[:cut])
            s = s[cut:]
        if len(cur) + len(s) > limit and cur:
            pages.append(cur)
            cur = s
        else:
            cur += s
    if cur:
        pages.append(cur)
    return pages


def mouth_track(x: np.ndarray, sr: int) -> list[bool]:
    hop = int(sr / FPS_MOUTH)
    n = max(1, len(x) // hop)
    rms = np.array([np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n)])
    th = np.percentile(rms, 90) * 0.22
    opened = rms > th
    # 開きっぱなしを避けるため、長く続く「開」は1つおきに閉じる（ぱくぱく感を出す）
    out, run = [], 0
    for o in opened:
        run = run + 1 if o else 0
        out.append(bool(o and (run % 3 != 0)))
    return out


class Renderer:
    def __init__(self, script_path: str, tts_name: str | None, preview: bool, check_only: bool = False):
        self.script_path = os.path.abspath(script_path)
        with open(self.script_path, encoding="utf-8") as f:
            self.sc = json.load(f)
        assert self.sc.get("format") in ("kaisetsuscript/1", "kaisetsuscript/2"), "format が kaisetsuscript/1 か /2 ではありません"
        self.sdir = os.path.dirname(self.script_path)
        self.base = os.path.normpath(os.path.join(self.sdir, self.sc.get("base_dir", ".")))
        self.out = os.path.join(HERE, "out", self.sc["id"])
        self.frames = os.path.join(self.out, "frames")
        if not check_only:
            shutil.rmtree(self.out, ignore_errors=True)
            os.makedirs(self.frames)
        self.preview = preview
        with open(os.path.join(HERE, "voices.json"), encoding="utf-8") as f:
            voices = json.load(f)
        self.tts = None if (preview or check_only) else tts.make_provider(tts_name or self.sc.get("tts", "openjtalk"), voices)
        self.chars = self.sc["characters"]
        with open(os.path.join(HERE, "poses.json"), encoding="utf-8") as f:
            self.pose_cfg = json.load(f)
        self.pose = {k: 1 for k in self.chars}   # 今のポーズ（聞き手のときは最後のポーズのまま）
        self.turns = {k: 0 for k in self.chars}
        self.audio: list[np.ndarray] = []
        self.t = 0.0
        self.segments: list[tuple[str, float]] = []  # (画像ファイル, 秒)
        self.chapters: list[tuple[float, str]] = []
        self.moves: list[tuple[float, str]] = []
        self.problems: dict[str, str] = {}   # 画面の点検で見つかった問題 → 章
        self.srt: list[tuple[float, float, str, str]] = []
        self.n = 0

    # ---------- 画面 ----------
    def char_html(self, key: str, mouth_open: bool) -> str:
        c = self.chars[key]
        state = "open" if mouth_open else "closed"
        imgs = c.get("images")
        if imgs:
            p = os.path.join(self.sdir, imgs[state])
            return f'<img src="file://{p}">'
        # assets/characters/<キャラ>_<番号>_closed.png・_open.png があれば、破片を消して口の位置を合わせた写しを使う
        prep = chars_prep.prepared(c.get("avatar", key), self.pose[key])
        if prep:
            return f'<img src="file://{prep[1] if mouth_open else prep[0]}">'
        return characters.BUILTIN[c.get("avatar", key)](mouth_open)

    def choose_pose(self, key: str, beat: dict) -> int:
        """beat の "pose"（名前か番号）か、なければセリフから自動で選ぶ。"""
        cfg = self.pose_cfg.get(c_key := self.chars[key].get("avatar", key), {})
        names = cfg.get("names", {})
        p = beat.get("pose")
        if p is None:
            for pat, name in cfg.get("auto", []):
                if re.search(pat, beat.get("text", "")):
                    p = name
                    break
        if p is None:
            seq = cfg.get("default", [1])
            p = seq[self.turns[key] % len(seq)]
        self.turns[key] += 1
        if isinstance(p, str):
            if p not in names:
                raise SystemExit(f"{c_key} にポーズ「{p}」はありません（poses.json）: {list(names)}")
            p = names[p]
        return int(p)

    def state(self, chapter: str, stage: dict, speaker: str | None, text: str | None, mouth_open: bool = False,
              prev: dict | None = None, fade: float | None = None, ui: float | None = None) -> dict:
        st = {"series": self.sc.get("series", ""), "chapter": chapter, "stage": stage, "sub": None,
              "prev": prev, "fade": fade, "ui": ui}
        for key, c in self.chars.items():
            st[c["side"]] = {"html": self.char_html(key, mouth_open and key == speaker), "name": c["name"],
                             "dim": speaker is not None and key != speaker}
        if speaker and text:
            c = self.chars[speaker]
            st["sub"] = {"name": c["name"], "cls": c.get("cls", ""), "text": text}
        return st

    def shot(self, st: dict) -> str:
        self.n += 1
        path = os.path.join(self.frames, f"f{self.n:05d}.png")
        self.page.evaluate("st => setState(st)", st)
        self.page.wait_for_function("Array.from(document.images).every(i => i.complete)")
        if st.get("prev") is None and st.get("ui") is None:  # 動いている途中のコマは点検しない
            for p in self.page.evaluate("problems()"):
                self.problems.setdefault(p, st["chapter"])
        self.page.screenshot(path=path)
        return path

    def trimmed(self, p: str, crop: list | None = None) -> str:
        """図のまわりの白い余白を切り落とした写しを作る（図を画面いっぱいに見せるため）。
        crop=[左, 上, 右, 下]（0〜1の割合）を指定すると、先にその範囲を切り出す（図の一部の拡大）。"""
        from PIL import Image, ImageChops

        tag = "_".join(f"{c:.2f}" for c in crop) if crop else "full"
        dst = os.path.join(self.frames, f"trim_{tag}_" + os.path.basename(p))
        if not os.path.exists(dst):
            im = Image.open(p).convert("RGB")
            if crop:
                im = im.crop((int(crop[0] * im.width), int(crop[1] * im.height), int(crop[2] * im.width), int(crop[3] * im.height)))
            box = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).point(lambda v: 255 if v > 12 else 0).getbbox()
            if box:
                m = 24
                im = im.crop((max(0, box[0] - m), max(0, box[1] - m), min(im.width, box[2] + m), min(im.height, box[3] + m)))
            im.save(dst)
        return dst

    def image_info(self, beat: dict) -> dict:
        from PIL import Image

        p = os.path.join(self.base, beat["image"])
        if not os.path.exists(p):
            raise SystemExit(f"画像がありません: {p}\n（高解像度の図は prep_figures.py で作る。README の「図を動画用にする」を参照）")
        if beat.get("crop") or beat.get("trim"):  # 余白を切り落とした写し（旧来の方法。ズームは view を使う）
            p = self.trimmed(p, beat.get("crop"))
        w, h = Image.open(p).size
        return {"kind": "image", "src": "file://" + p, "nw": w, "nh": h, "view": [0, 0, 1, 1]}

    def stage_of(self, beat: dict, cur: dict) -> dict:
        """beat の指定から、次の「図の枠」の状態を作る。
        図・箇条書き・カードなどの新しい指定があれば入れ替え（注釈・強調はリセット）、なければ今の状態に view・callout・focus・reveal を重ねる。"""
        new = None
        if "image" in beat:
            new = {"kind": "none"} if beat["image"] in (None, "none") else self.image_info(beat)
        elif "bullets" in beat:
            new = {"kind": "bullets", **beat["bullets"]}
        elif "card" in beat:
            new = {"kind": "card", **beat["card"]}
        elif "cards" in beat:
            new = {"kind": "cards", **beat["cards"]}
        elif "rows" in beat:
            new = {"kind": "rows", **beat["rows"]}
        elif "html" in beat:
            new = {"kind": "html", "html": beat["html"]}
        if new is None:
            new = dict(cur)
        if new["kind"] == "image":
            nw, nh = new["nw"], new["nh"]
            if "view_px" in beat:
                x0, y0, x1, y1 = beat["view_px"]
                new["view"] = [x0 / nw, y0 / nh, x1 / nw, y1 / nh]
            elif "view" in beat:
                new["view"] = beat["view"]
            if "focus_px" in beat:
                new["focus"] = [[x0 / nw, y0 / nh, x1 / nw, y1 / nh] for x0, y0, x1, y1 in beat["focus_px"]]
            elif "focus" in beat:
                new["focus"] = beat["focus"]
        for k in ("callout", "reveal", "focus_item"):
            if k in beat:
                new[k] = beat[k]
        return new

    @staticmethod
    def classify(a: dict, b: dict) -> str:
        """図の枠の変わり方: 'cut'（別の図に入れ替え）/ 'zoom'（同じ図で見せる範囲を動かす）/ 'ui'（注釈・強調・カードの追加だけ）/ 'same'"""
        def core(x):
            return json.dumps({k: v for k, v in x.items() if k not in ("view", "focus", "callout", "reveal", "focus_item")}, sort_keys=True)

        if core(a) != core(b):
            return "cut"
        if a.get("kind") == "image" and a.get("view") != b.get("view"):
            return "zoom"
        ui = ("callout", "focus", "reveal", "focus_item")
        return "ui" if any(a.get(k) != b.get(k) for k in ui) else "same"

    # ---------- 音 ----------
    def add_audio(self, y: np.ndarray):
        self.audio.append(y.astype(np.float32))
        self.t += len(y) / tts.SR

    def silence(self, sec: float) -> np.ndarray:
        return np.zeros(int(sec * tts.SR), dtype=np.float32)

    def hold(self, img: str, sec: float, y: np.ndarray | None = None):
        """静止画を sec 秒出す。y を渡すと、それを同じ長さに合わせて鳴らす。"""
        if y is None:
            y = self.silence(sec)
        else:
            y = np.concatenate([y, self.silence(max(0, sec - len(y) / tts.SR))])[: int(sec * tts.SR)]
        self.segments.append((img, sec))
        self.add_audio(y)

    def card(self, spec: dict, chapter: str = ""):
        st = self.state(chapter, {"kind": "card", **{k: spec.get(k, "") for k in ("top", "title", "bottom")}}, None, None)
        img = self.shot(st)
        y = jingle.load(os.path.join(HERE, "jingles", spec["jingle"] + ".json")) if spec.get("jingle") else None
        sec = max(spec.get("seconds", 0), (len(y) / tts.SR) if y is not None else 0) or 3
        self.hold(img, sec, y)
        return img

    def transition(self, chapter: str, a: dict, b: dict, kind: str, spk: str, text: str):
        """図の枠を a から b へ動かす（口は閉じたまま、次に話す字幕を出しておく）。"""
        T = T_ZOOM if kind == "zoom" else T_FADE
        n = max(2, round(T * FPS))
        for i in range(1, n + 1):
            t = i / n
            e = t * t * (3 - 2 * t)  # なめらかに動き出して、なめらかに止まる
            u = min(1.0, max(0.0, (t - 0.6) / 0.4))  # 注釈・強調は、動きが止まる直前に出す（動いている途中で文字に重ならないように）
            if kind == "zoom":
                st = dict(b)
                st["view"] = [a["view"][j] + (b["view"][j] - a["view"][j]) * e for j in range(4)]
                stage = self.state(chapter, st, spk, text, False, ui=u)
            else:
                stage = self.state(chapter, b, spk, text, False, prev=a, fade=e, ui=u)
            self.segments.append((self.shot(stage), 1.0 / FPS))
            self.add_audio(self.silence(1.0 / FPS))
        self.moves.append((self.t, kind))

    def speak(self, chapter: str, stage: dict, beat: dict, prev_speaker: str | None, prev_stage: dict | None = None):
        spk = beat["speaker"]
        self.pose[spk] = self.choose_pose(spk, beat)
        voice = self.chars[spk]["voice"]
        local_yomi = beat.get("yomi", {})
        change = self.classify(prev_stage, stage) if prev_stage is not None else "cut"
        for i, page in enumerate(split_pages(beat["text"])):
            shown = re.sub(r"[|↑↓]", "", page)  # 「|」は間、「↑」「↓」は語尾の上げ下げの記号。字幕には出さない
            closed = self.shot(self.state(chapter, stage, spk, shown, False))
            if i == 0 and change in ("zoom", "cut") and not self.preview and prev_stage is not None and prev_stage.get("kind") != "none":
                # 図が動く／入れ替わる間は話さない。先に図を見せてから話し始める
                self.transition(chapter, prev_stage, stage, "zoom" if change == "zoom" else "fade", spk, shown)
                self.hold(closed, LEAD)
            elif i == 0 and change == "ui":
                self.moves.append((self.t, "ui"))
                self.hold(closed, LEAD_UI + (0.1 if prev_speaker not in (None, spk) else 0))
            else:
                gap = GAP_TURN if (i == 0 and prev_speaker not in (None, spk)) else GAP
                self.hold(closed, gap)
            if self.preview:
                self.hold(closed, max(1.5, len(shown) * 0.12))
                continue
            opened = self.shot(self.state(chapter, stage, spk, shown, True))
            y, sr = tts.synth_with_pauses(self.tts, voice, tts.to_reading(page, local_yomi))
            t0 = self.t
            hop = 1.0 / FPS_MOUTH
            track = mouth_track(y, sr)
            # 口の開閉ごとに静止画をつなぐ（同じ絵が続くところはまとめる）
            run_img, run_len = None, 0.0
            for o in track:
                img = opened if o else closed
                if img == run_img:
                    run_len += hop
                else:
                    if run_img:
                        self.segments.append((run_img, run_len))
                    run_img, run_len = img, hop
            rest = len(y) / sr - len(track) * hop
            self.segments.append((run_img or closed, run_len + max(0.0, rest)))
            self.add_audio(y)
            self.srt.append((t0, self.t, self.chars[spk]["name"], shown))
        if beat.get("pause"):
            self.hold(self.segments[-1][0], beat["pause"])

    def ensure_figures(self):
        """台本に "figures" があり、高解像度の図がまだなければ、prep_figures.py で作る。"""
        for fg in self.sc.get("figures", []):
            out = os.path.normpath(os.path.join(self.sdir, fg["out"]))
            if os.path.isdir(out) and any(f.endswith(".png") for f in os.listdir(out)):
                continue
            draw = os.path.normpath(os.path.join(self.sdir, fg["draw"]))
            print(f"高解像度の図を作ります: {draw}")
            cmd = [sys.executable, os.path.join(HERE, "prep_figures.py"), draw, "--out", out,
                   "--scale", str(fg.get("scale", 2))]
            if fg.get("font_scales"):
                cmd += ["--font-scales", fg["font_scales"]]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)

    # ---------- 全体 ----------
    def run(self):
        self.ensure_figures()
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--allow-file-access-from-files"])
            self.page = browser.new_page(viewport={"width": 1920, "height": 1080})
            self.page.goto("file://" + os.path.join(HERE, "template.html"))
            sc = self.sc
            thumb_src = self.card(sc["intro"])
            for ch in sc["chapters"]:
                self.chapters.append((self.t, ch["title"]))
                if ch.get("card", True):
                    self.card({"top": sc.get("series", ""), "title": ch["title"], "jingle": "chapter", "seconds": 2.2}, ch["title"])
                stage, prev = {"kind": "none"}, None
                for beat in ch["beats"]:
                    before, stage = stage, self.stage_of(beat, stage)
                    if "speaker" in beat:
                        self.speak(ch["title"], stage, beat, prev, before)
                        prev = beat["speaker"]
                    else:  # 話者なしで図だけを見せる
                        if not self.preview and before.get("kind") != "none" and self.classify(before, stage) in ("zoom", "cut"):
                            self.transition(ch["title"], before, stage, "zoom" if self.classify(before, stage) == "zoom" else "fade", "", "")
                        self.hold(self.shot(self.state(ch["title"], stage, None, None)), beat.get("seconds", 2.5))
            self.chapters.append((self.t, "まとめ・エンディング"))
            self.card(sc["outro"])
            self.thumbnail()
            browser.close()
        self.write_video()
        self.write_meta()
        self.write_pacing()
        shutil.rmtree(self.frames, ignore_errors=True) if not self.preview else None

    def thumbnail(self):
        th = self.sc.get("thumbnail") or {}
        st = self.state("", {"kind": "card", "top": th.get("top", ""), "title": th.get("title", self.sc["intro"].get("title", "")),
                             "bottom": th.get("bottom", "")}, None, None)
        st["sub"] = None
        self.page.evaluate("st => setState(st)", st)
        png = os.path.join(self.out, "thumbnail.png")
        self.page.screenshot(path=png)
        # YouTube のサムネイル: 16:9・1280×720・2MB以下（JPG）
        from PIL import Image

        Image.open(png).convert("RGB").resize((1280, 720), Image.LANCZOS).save(os.path.join(self.out, "thumbnail.jpg"), quality=92)

    def write_video(self):
        lst = os.path.join(self.out, "frames.txt")
        with open(lst, "w") as f:
            for img, d in self.segments:
                f.write(f"file '{img}'\nduration {d:.4f}\n")
            f.write(f"file '{self.segments[-1][0]}'\n")
        wav_path = os.path.join(self.out, "audio.wav")
        a = np.concatenate(self.audio)
        a = np.clip(a / max(1e-6, np.abs(a).max()) * 0.9, -1, 1)
        with wave.open(wav_path, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(tts.SR)
            w.writeframes((a * 32767).astype(np.int16).tobytes())
        mp4 = os.path.join(self.out, f"{self.sc['id']}.mp4")
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav_path,
               # YouTube の推奨: H.264 + AAC-LC、MP4、16:9。色は BT.709 にそろえる（指定しないと色がずれる）
               "-vf", f"fps={FPS},scale=out_color_matrix=bt709:out_range=tv,format=yuv420p", "-c:v", "libx264", "-profile:v", "high",
               "-preset", "medium", "-crf", "18", "-tune", "stillimage", "-g", str(FPS * 2),
               "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
               "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", mp4]
        if self.preview:
            return
        subprocess.run(cmd, check=True)
        os.remove(lst)
        os.remove(wav_path)

    def write_pacing(self):
        """話す速さ・字幕の長さ・図の動きの間隔を集計する（会話のリズムの点検用）。"""
        lines = []
        pages = [(a, b, name, text) for a, b, name, text in self.srt]
        if not pages:  # プレビュー（音声なし）では、画面の点検だけ表示する
            print("画面の点検（はみ出し・字幕の行数）: " + ("問題なし" if not self.problems else ""))
            for p, ch in self.problems.items():
                print(f"  [{ch}] {p}")
            return
        cps = [len(t) / max(0.1, b - a) for a, b, _, t in pages]
        durs = [b - a for a, b, _, _ in pages]
        lines.append(f"全体 {self.t:.1f}秒 / 字幕 {len(pages)}ページ / 話す速さ 平均 {sum(len(t) for *_, t in pages) / sum(durs):.1f}文字/秒（最速 {max(cps):.1f}・最遅 {min(cps):.1f}）")
        lines.append(f"字幕1ページの長さ 平均 {sum(durs) / len(durs):.1f}秒（最長 {max(durs):.1f}秒）/ 最長の字幕 {max(len(t) for *_, t in pages)}文字")
        moves = sorted(self.moves)
        lines.append(f"図の変化: ズーム {sum(1 for _, k in moves if k == 'zoom')}回・入れ替え {sum(1 for _, k in moves if k == 'fade')}回・"
                     f"注釈/強調/カードの追加 {sum(1 for _, k in moves if k == 'ui')}回")
        gaps = [b[0] - a[0] for a, b in zip(moves, moves[1:])]
        if gaps:
            lines.append(f"図が変わる間隔 平均 {sum(gaps) / len(gaps):.1f}秒（最短 {min(gaps):.1f}・最長 {max(gaps):.1f}）")
        warn = []
        for (a, b, name, t), c in zip(pages, cps):
            if c > 8.5:
                warn.append(f"  速すぎ({c:.1f}文字/秒) {a:.0f}秒 {name}「{t[:24]}…」")
            if len(t) > 62:
                warn.append(f"  字幕が長い({len(t)}文字) {a:.0f}秒")
        if gaps and max(gaps) > 28:
            warn.append(f"  図が{max(gaps):.0f}秒変わらない場面がある（視聴者が飽きる目安は25秒）")
        warn += [f"  [{ch}] {p}" for p, ch in self.problems.items()]
        txt = "\n".join(lines + (["要確認:"] + warn if warn else ["要確認: なし"]))
        print(txt)
        with open(os.path.join(self.out, "pacing.txt"), "w", encoding="utf-8") as f:
            f.write(txt + "\n")

    def write_meta(self):
        def ts(t, srt=False):
            h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
            if srt:
                return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
            return f"{h}:{m:02d}:{int(s):02d}" if h else f"{m}:{int(s):02d}"

        yt = self.sc.get("youtube", {})
        chap = ["0:00 オープニング"] + [f"{ts(t)} {name}" for t, name in self.chapters]
        lines = [f"# {yt.get('title', self.sc['intro'].get('title', ''))}", "", "## 概要欄", "",
                 yt.get("description", ""), "", "■ チャプター", *chap, "", "■ クレジット", *yt.get("credits", []), "",
                 "## タグ", ", ".join(yt.get("tags", [])), "", f"## 長さ\n{ts(self.t)}"]
        with open(os.path.join(self.out, "youtube.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        with open(os.path.join(self.out, f"{self.sc['id']}.srt"), "w", encoding="utf-8") as f:
            for i, (a, b, name, text) in enumerate(self.srt, 1):
                f.write(f"{i}\n{ts(a, True)} --> {ts(b, True)}\n{name}「{text}」\n\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--tts", choices=["openjtalk", "voicevox", "elevenlabs"])
    ap.add_argument("--preview", action="store_true")
    a = ap.parse_args()
    r = Renderer(a.script, a.tts, a.preview)
    r.run()
    print(f"書き出し先: {r.out}（{r.t:.1f}秒）")
    if r.tts is not None and hasattr(r.tts, "chars_billed"):
        print(f"ElevenLabs: 今回の課金対象 {r.tts.chars_billed} 文字／キャッシュ再利用 {r.tts.chars_cached} 文字")


if __name__ == "__main__":
    main()
