"""音声合成のプロバイダ。

- openjtalk : オフラインで動く（クラウドのセッションでも使える）。既定。
- voicevox  : ローカルPCで VOICEVOX エンジン（http://127.0.0.1:50021）を起動しているときに使う。
              声の質が大きく上がるので、公開用の本番はこちらを推奨（キャラクターごとの利用規約とクレジット表記に従う）。

どちらも (numpy.float32 の波形, サンプリング周波数) を返す。
"""
from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000

# 読みの辞書（字幕はそのまま、音声だけ読みを置き換える）
_YOMI = None


def yomi_dict() -> list[tuple[str, str]]:
    global _YOMI
    if _YOMI is None:
        with open(os.path.join(HERE, "yomi_dict.json"), encoding="utf-8") as f:
            d = json.load(f)
        # 長い語から置き換える（「地積測量図」を「地積」より先に）
        _YOMI = sorted(d.items(), key=lambda kv: -len(kv[0]))
    return _YOMI


LETTERS = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [
    "エー", "ビー", "シイ",  # 「シー」だと前の語によって「スィー」と読まれる
    "ディー", "イー", "エフ", "ジー", "エイチ", "アイ", "ジェー", "ケー", "エル", "エム",
    "エヌ", "オー", "ピー", "キュー", "アール", "エス", "ティー", "ユー", "ブイ", "ダブリュー", "エックス", "ワイ", "ゼット"]))


def hira2kata(s: str) -> str:
    """読みはカタカナにして渡す（ひらがなだと Open JTalk が漢字に直して解析し直し、「はちいち」を「八一＝ハチジューイチ」と読む）。"""
    return "".join(chr(ord(c) + 0x60) if "ぁ" <= c <= "ゖ" else c for c in s)


def _apply(s: str, pairs) -> str:
    for k, v in sorted(pairs, key=lambda kv: -len(kv[0])):
        s = s.replace(k, hira2kata(v))
    return s


def to_reading(text: str, local: dict | None = None) -> str:
    """字幕の文字列を、音声合成に渡す読みの文字列にする。
    local＝その場面だけの読み（台本の beat の "yomi"）→ yomi_dict.json → 記号・角度・アルファベットの自動変換、の順。"""
    s = _apply(text, (local or {}).items())
    s = _apply(s, yomi_dict())
    # 全角の英数字を半角に
    s = s.translate({c: c - 0xFEE0 for c in range(ord("Ａ"), ord("ｚ") + 1)} | {c: c - 0xFEE0 for c in range(ord("０"), ord("９") + 1)})
    # 角度：325°06′51″ も 325度06分51秒 も「サンビャクニジューゴド ロップン ゴジューイチビョー」に（頭の0を読まない）
    s = re.sub(r"(\d+)°(\d+)′([\d.]+)″", r"\1度\2分\3秒", s)
    s = re.sub(r"(\d+)°", r"\1度", s)
    s = re.sub(r"(?<=度)0(\d)(?=分)", r"\1", s)
    s = re.sub(r"(?<=分)0(\d)(?=[.\d]*秒)", r"\1", s)
    # 記号の読み
    s = s.replace("＝", "イコール").replace("→", "から").replace("〜", "から").replace("−", "マイナス")
    s = re.sub(r"[「」『』（）()【】\[\]]", "、", s)
    # 「問1」は前の語によって「トエイチ」と読まれるので、カタカナにしておく
    s = re.sub(r"問(?=\d)", "トイ", s)
    # アルファベット（点名・略語）は1文字ずつ名前で読む。辞書に入れた語（F-789SG など）はすでにカタカナになっている
    s = re.sub(r"[A-Za-z]", lambda m: LETTERS[m.group().upper()], s)
    s = re.sub(r"、{2,}", "、", s).strip("、")
    return s


# 間（ま）の長さ（秒）。文の終わり・沈黙の記号・手で入れる区切りの記号で、音声をいったん切ってすき間を入れる。
PAUSES = [
    (r"(?:……|…|・・・|‥|――|—)+", 0.65),   # 言いよどみ・沈黙
    (r"\|\|", 0.7),                          # 手で入れる長い間（yomi に「||」と書く）
    (r"\|", 0.3),                             # 手で入れる短い間（yomi に「|」と書く）
    (r"(?<=[。．])", 0.35),                   # 文の終わり
    (r"(?<=[！？!?])", 0.4),                  # 感嘆・疑問の終わり
]


def segments(reading: str) -> list[tuple[str, float]]:
    """読みの文字列を、(読み上げる部分, その後の間の秒数) の並びに分ける。"""
    pat = "|".join(f"({p})" for p, _ in PAUSES)
    out, pos = [], 0
    for m in re.finditer(pat, reading):
        if m.start() == m.end() and m.start() == pos and out:
            continue
        sec = next(PAUSES[i][1] for i, g in enumerate(m.groups()) if g is not None)
        part = reading[pos:m.start()]
        if part.strip("、 　"):
            out.append((part.strip("、 　"), sec))
        elif out:  # 記号が続いたときは、長いほうの間をとる
            out[-1] = (out[-1][0], max(out[-1][1], sec))
        pos = m.end()
    rest = reading[pos:].strip("、 　")
    if rest:
        out.append((rest, 0.0))
    if out:
        out[-1] = (out[-1][0], 0.0)  # ページの最後の間は、ページの間のすき間に任せる
    return out


def synth_with_pauses(provider, voice_key: str, reading: str):
    parts = []
    for text, sec in segments(reading):
        y, sr = provider.synth(voice_key, text)
        parts += [y, np.zeros(int(sec * sr), dtype=np.float32)]
    return (np.concatenate(parts) if parts else np.zeros(int(0.2 * SR), dtype=np.float32)), SR


class OpenJTalk:
    def __init__(self, voices: dict):
        import pyopenjtalk

        self.pj = pyopenjtalk
        self.engines = {}
        self.voices = voices

    def _engine(self, key):
        if key not in self.engines:
            v = self.voices[key]
            path = os.path.join(HERE, v["htsvoice"])
            if not os.path.exists(path):
                raise SystemExit(f"声データがありません: {path}\n先に ./setup_voices.sh を実行してください")
            self.engines[key] = self.pj.HTSEngine(path.encode())
        return self.engines[key]

    def synth(self, voice_key: str, text: str):
        v = self.voices[voice_key]
        eng = self._engine(voice_key)
        eng.set_speed(v.get("speed", 1.0))
        eng.add_half_tone(v.get("half_tone", 0.0))
        labels = self.pj.extract_fullcontext(text)
        x = eng.synthesize(labels)
        sr = eng.get_sampling_frequency()
        eng.refresh()
        x = (x / 32768.0).astype(np.float32) * v.get("gain", 1.0)
        if sr != SR:
            x = np.interp(np.linspace(0, len(x), int(len(x) * SR / sr), endpoint=False), np.arange(len(x)), x).astype(np.float32)
        return x, SR


class Voicevox:
    def __init__(self, voices: dict, url: str = "http://127.0.0.1:50021"):
        self.voices = voices
        self.url = url

    def synth(self, voice_key: str, text: str):
        v = self.voices[voice_key]
        sp = v["speaker"]
        q = urllib.request.urlopen(urllib.request.Request(
            f"{self.url}/audio_query?speaker={sp}&text={urllib.parse.quote(text)}", method="POST"))
        query = json.load(q)
        query["speedScale"] = v.get("speed", 1.0)
        query["outputSamplingRate"] = SR
        req = urllib.request.Request(f"{self.url}/synthesis?speaker={sp}", data=json.dumps(query).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        wav = urllib.request.urlopen(req).read()
        x = np.frombuffer(wav[44:], dtype=np.int16).astype(np.float32) / 32768.0
        return x * v.get("gain", 1.0), SR


def make_provider(name: str, voices: dict):
    if name == "openjtalk":
        return OpenJTalk(voices["openjtalk"])
    if name == "voicevox":
        return Voicevox(voices["voicevox"])
    raise SystemExit(f"未知のTTS: {name}")
