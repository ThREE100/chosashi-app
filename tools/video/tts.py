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


def to_reading(text: str) -> str:
    s = text
    for k, v in yomi_dict():
        s = s.replace(k, v)
    # 記号の読み
    s = s.replace("＝", "イコール").replace("→", "から").replace("〜", "から")
    s = re.sub(r"[「」『』（）()【】]", "、", s)
    s = re.sub(r"、{2,}", "、", s).strip("、")
    return s


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
