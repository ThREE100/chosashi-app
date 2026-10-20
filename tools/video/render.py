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
import wave

import numpy as np

import characters
import jingle
import tts

HERE = os.path.dirname(os.path.abspath(__file__))
FPS_MOUTH = 12.5          # 口の開閉を切り替える回数（1秒あたり）
PAGE_CHARS = 84           # 字幕1ページの最大文字数（42px・3行）
GAP = 0.28                # 同じ話者のページの間のすき間（秒）
GAP_TURN = 0.45           # 話者が替わるときのすき間（秒）


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
    def __init__(self, script_path: str, tts_name: str | None, preview: bool):
        self.script_path = os.path.abspath(script_path)
        with open(self.script_path, encoding="utf-8") as f:
            self.sc = json.load(f)
        assert self.sc.get("format") == "kaisetsuscript/1", "format が kaisetsuscript/1 ではありません"
        self.sdir = os.path.dirname(self.script_path)
        self.base = os.path.normpath(os.path.join(self.sdir, self.sc.get("base_dir", ".")))
        self.out = os.path.join(HERE, "out", self.sc["id"])
        self.frames = os.path.join(self.out, "frames")
        shutil.rmtree(self.out, ignore_errors=True)
        os.makedirs(self.frames)
        self.preview = preview
        with open(os.path.join(HERE, "voices.json"), encoding="utf-8") as f:
            voices = json.load(f)
        self.tts = None if preview else tts.make_provider(tts_name or self.sc.get("tts", "openjtalk"), voices)
        self.chars = self.sc["characters"]
        self.audio: list[np.ndarray] = []
        self.t = 0.0
        self.segments: list[tuple[str, float]] = []  # (画像ファイル, 秒)
        self.chapters: list[tuple[float, str]] = []
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
        # assets/characters/<key>_closed.png と <key>_open.png を置けば、台本を書き換えなくてもそちらを使う
        for ext in ("png", "webp"):
            p = os.path.join(HERE, "assets", "characters", f"{key}_{state}.{ext}")
            if os.path.exists(p):
                return f'<img src="file://{p}">'
        return characters.BUILTIN[c.get("avatar", key)](mouth_open)

    def state(self, chapter: str, stage: dict, speaker: str | None, text: str | None, mouth_open: bool = False) -> dict:
        st = {"series": self.sc.get("series", ""), "chapter": chapter, "stage": stage, "sub": None}
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

    def stage_of(self, beat: dict, cur: dict) -> dict:
        if "image" in beat:
            if beat["image"] in (None, "none"):
                return {"kind": "none"}
            p = os.path.join(self.base, beat["image"])
            if not os.path.exists(p):
                raise SystemExit(f"画像がありません: {p}")
            return {"kind": "image", "src": "file://" + self.trimmed(p, beat.get("crop"))}
        if "bullets" in beat:
            return {"kind": "bullets", **beat["bullets"]}
        if "card" in beat:
            return {"kind": "card", **beat["card"]}
        return cur

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

    def speak(self, chapter: str, stage: dict, beat: dict, prev_speaker: str | None):
        spk = beat["speaker"]
        voice = self.chars[spk]["voice"]
        local_yomi = beat.get("yomi", {})
        for i, page in enumerate(split_pages(beat["text"])):
            shown = re.sub(r"[|↑↓]", "", page)  # 「|」は間、「↑」「↓」は語尾の上げ下げの記号。字幕には出さない
            gap = GAP_TURN if (i == 0 and prev_speaker not in (None, spk)) else GAP
            closed = self.shot(self.state(chapter, stage, spk, shown, False))
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

    # ---------- 全体 ----------
    def run(self):
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
                    stage = self.stage_of(beat, stage)
                    if "speaker" in beat:
                        self.speak(ch["title"], stage, beat, prev)
                        prev = beat["speaker"]
                    else:  # 話者なしで図だけを見せる
                        self.hold(self.shot(self.state(ch["title"], stage, None, None)), beat.get("seconds", 2.5))
            self.chapters.append((self.t, "まとめ・エンディング"))
            self.card(sc["outro"])
            self.thumbnail()
            browser.close()
        self.write_video()
        self.write_meta()
        shutil.rmtree(self.frames, ignore_errors=True) if not self.preview else None

    def thumbnail(self):
        th = self.sc.get("thumbnail") or {}
        st = self.state("", {"kind": "card", "top": th.get("top", ""), "title": th.get("title", self.sc["intro"].get("title", "")),
                             "bottom": th.get("bottom", "")}, None, None)
        st["sub"] = None
        self.page.evaluate("st => setState(st)", st)
        self.page.screenshot(path=os.path.join(self.out, "thumbnail.png"))

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
               "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-tune", "stillimage",
               "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", mp4]
        if self.preview:
            return
        subprocess.run(cmd, check=True)
        os.remove(lst)
        os.remove(wav_path)

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
    ap.add_argument("--tts", choices=["openjtalk", "voicevox"])
    ap.add_argument("--preview", action="store_true")
    a = ap.parse_args()
    r = Renderer(a.script, a.tts, a.preview)
    r.run()
    print(f"書き出し先: {r.out}（{r.t:.1f}秒）")


if __name__ == "__main__":
    main()
