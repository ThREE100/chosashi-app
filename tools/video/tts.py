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
import urllib.error
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


# 語尾の上げ下げ（半音の数）。セリフの終わり方から自動で決め、↑・↓ の記号で手で指定もできる。
ENDINGS = {"up": 5.0, "soft_up": 3.5, "down": -3.0}


def ending_of(text: str) -> str | None:
    """セグメントの終わり方から語尾の上げ下げを決める。"""
    if "↓" in text:
        return "down"
    if "↑" in text or re.search(r"[？?]\s*$", text):
        return "up"
    if re.search(r"(ね|かな|よね|でしょう)[。．]?\s*$", text):
        return "soft_up"
    return None


def apply_prosody(y: np.ndarray, sr: int, intonation: float = 1.0, ending: str | None = None) -> np.ndarray:
    """抑揚を付け直す（Open JTalk 用）。声の高さの動きを intonation 倍に広げ、語尾を上げ下げする。
    WORLD（pyworld）で声を「高さ」と「声色」に分け、高さだけを変えて組み立て直す。"""
    if intonation == 1.0 and not ending:
        return y
    import pyworld as pw

    x = y.astype(np.float64)
    f0, t = pw.dio(x, sr, frame_period=5.0)
    f0 = pw.stonemask(x, f0, t, sr)
    voiced = f0 > 0
    if voiced.sum() < 5:
        return y
    lf = np.zeros_like(f0)
    lf[voiced] = np.log(f0[voiced])
    m = np.median(lf[voiced])
    lf[voiced] = m + (lf[voiced] - m) * intonation
    if ending:
        # 語尾の0.35秒を、文全体の中央の高さから ENDINGS 半音だけ上（下）の高さへ、なめらかに近づける。
        # （足し算だと、抑揚を広げたぶん深くなった Open JTalk の語尾の下がりに打ち消されてしまう）
        last = np.nonzero(voiced)[0][-1]
        n = min(last + 1, int(0.35 / 0.005))
        idx = np.arange(last + 1 - n, last + 1)
        w = np.linspace(0, 1, n) ** 1.2
        target = m + ENDINGS[ending] * np.log(2) / 12
        v = voiced[idx]
        blended = lf[idx[v]] * (1 - w[v]) + target * w[v]
        # 上げるときは今より高いときだけ、下げるときは今より低いときだけ動かす（もとから下がっている語尾をさらに上げない）
        lf[idx[v]] = np.minimum(lf[idx[v]], blended) if ending == "down" else np.maximum(lf[idx[v]], blended)
    f0[voiced] = np.exp(lf[voiced])
    sp = pw.cheaptrick(x, f0, t, sr)
    ap = pw.d4c(x, f0, t, sr)
    out = pw.synthesize(f0, sp, ap, sr, frame_period=5.0)[: len(y)]
    return out.astype(np.float32)


def apply_fx(y: np.ndarray, sr: int, fx: dict | None) -> np.ndarray:
    """声の加工（ボイスチェンジャー）。voices.json の各声に "fx" を書くと掛かる。

    "pitch": 1.35   声の高さの倍率。声の通り道（フォルマント）ごと上げるので、
                    マスコットキャラクターのような「機械で変換した声」になる。話す速さは変わらない。
    "tempo": 1.0    話す速さの倍率（加工のあとに掛ける）。
    "bright": 3     高い音を持ち上げる量（dB）。こもりを取って、軽い声にする。
    """
    if not fx:
        return y
    import subprocess

    p = float(fx.get("pitch", 1.0))
    t = float(fx.get("tempo", 1.0))
    chain = []
    if p != 1.0:
        chain += [f"asetrate={int(sr * p)}", f"aresample={sr}"]
        # atempo は 0.5〜2.0 の範囲なので、高さを上げた分だけ遅くして長さを戻す
        k = t / p
        while k < 0.5:
            chain.append("atempo=0.5")
            k /= 0.5
        chain.append(f"atempo={k:.5f}")
    elif t != 1.0:
        chain.append(f"atempo={t:.5f}")
    if fx.get("bright"):
        chain.append(f"treble=g={float(fx['bright'])}:f=3000")
    pcm = (np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()
    out = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "s16le", "-ar", str(sr), "-ac", "1", "-i", "pipe:0",
                          "-af", ",".join(chain), "-f", "s16le", "-ar", str(sr), "-ac", "1", "pipe:1"],
                         input=pcm, capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.int16).astype(np.float32) / 32768.0


def synth_with_pauses(provider, voice_key: str, reading: str):
    parts = []
    fx = provider.voices[voice_key].get("fx")
    for text, sec in segments(reading):
        ending = ending_of(text)
        y, sr = provider.synth(voice_key, text.replace("↑", "").replace("↓", ""), ending=ending)
        y = apply_fx(y, sr, fx)
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

    def synth(self, voice_key: str, text: str, ending: str | None = None):
        v = self.voices[voice_key]
        eng = self._engine(voice_key)
        eng.set_speed(v.get("speed", 1.0))
        eng.add_half_tone(v.get("half_tone", 0.0))
        labels = self.pj.extract_fullcontext(text)
        x = eng.synthesize(labels)
        sr = eng.get_sampling_frequency()
        eng.refresh()
        x = apply_prosody((x / 32768.0).astype(np.float32), sr, v.get("intonation", 1.0), ending) * v.get("gain", 1.0)
        if sr != SR:
            x = np.interp(np.linspace(0, len(x), int(len(x) * SR / sr), endpoint=False), np.arange(len(x)), x).astype(np.float32)
        return x, SR


class Voicevox:
    def __init__(self, voices: dict, url: str = "http://127.0.0.1:50021"):
        self.voices = voices
        self.url = url

    def synth(self, voice_key: str, text: str, ending: str | None = None):
        v = self.voices[voice_key]
        sp = v["speaker"]
        q = urllib.request.urlopen(urllib.request.Request(
            f"{self.url}/audio_query?speaker={sp}&text={urllib.parse.quote(text)}", method="POST"))
        query = json.load(q)
        query["speedScale"] = v.get("speed", 1.0)
        query["intonationScale"] = v.get("intonation", 1.0)
        query["outputSamplingRate"] = SR
        if ending and query.get("accent_phrases"):
            # 最後のモーラの高さを上げ下げする（VOICEVOX の高さはおよそ対数。0.06 ≒ 1半音）
            mora = query["accent_phrases"][-1]["moras"][-1]
            if mora.get("pitch", 0) > 0:
                mora["pitch"] += ENDINGS[ending] * 0.06
        req = urllib.request.Request(f"{self.url}/synthesis?speaker={sp}", data=json.dumps(query).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        wav = urllib.request.urlopen(req).read()
        x = np.frombuffer(wav[44:], dtype=np.int16).astype(np.float32) / 32768.0
        return x * v.get("gain", 1.0), SR


class ElevenLabs:
    """ElevenLabs の Text to Speech API。キーは環境変数 ELEVENLABS_API_KEY だけから読む（ファイル・リポジトリには書かない）。
    同じ（声・モデル・設定・文）の音声は voices_cache/elevenlabs/ に保存して再利用し、書き出しをやり直しても課金されない。
    ピッチ・語尾の上げ下げは声側に任せる（Open JTalk 用の apply_prosody は使わない）。"""

    URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=pcm_24000"

    def __init__(self, voices: dict):
        self.voices = voices
        self.key = os.environ.get("ELEVENLABS_API_KEY")
        self.cache = os.path.join(HERE, "voices_cache", "elevenlabs")
        os.makedirs(self.cache, exist_ok=True)
        self.chars_billed = 0
        self.chars_cached = 0

    def synth(self, voice_key: str, text: str, ending: str | None = None):
        import hashlib

        v = self.voices[voice_key]
        body = {"text": text, "model_id": v.get("model_id", "eleven_multilingual_v2"),
                "voice_settings": v.get("voice_settings", {})}
        if v.get("language_code"):
            body["language_code"] = v["language_code"]
        h = hashlib.sha256(json.dumps([v["voice_id"], body], ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:24]
        path = os.path.join(self.cache, h + ".pcm")
        if os.path.exists(path):
            self.chars_cached += len(text)
            raw = open(path, "rb").read()
        else:
            if not self.key:
                raise SystemExit("環境変数 ELEVENLABS_API_KEY がありません（キーはチャットやファイルに書かず、環境変数に設定してください）")
            req = urllib.request.Request(self.URL.format(voice_id=v["voice_id"]), data=json.dumps(body).encode(),
                                         headers={"xi-api-key": self.key, "Content-Type": "application/json"}, method="POST")
            try:
                raw = urllib.request.urlopen(req, timeout=120).read()
            except urllib.error.HTTPError as e:
                raise SystemExit(f"ElevenLabs のエラー {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
            open(path, "wb").write(raw)
            self.chars_billed += len(text)
        x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
        x = np.interp(np.linspace(0, len(x), int(len(x) * 2), endpoint=False), np.arange(len(x)), x).astype(np.float32)  # 24k→48k
        return x * v.get("gain", 1.0), SR


def make_provider(name: str, voices: dict):
    if name == "elevenlabs":
        return ElevenLabs(voices["elevenlabs"])
    if name == "openjtalk":
        return OpenJTalk(voices["openjtalk"])
    if name == "voicevox":
        return Voicevox(voices["voicevox"])
    raise SystemExit(f"未知のTTS: {name}")
