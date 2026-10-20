"""ジングルの楽譜（JSON）を音声にする小さな合成器。記事の JingleScript をまねた簡易版。

楽譜の形式（format: "jingle/1"）:
{
  "format": "jingle/1",
  "tempo": 112,                      # 1分あたりの拍数
  "length_beats": 10,                # 全体の長さ（拍）。省略時は最後の音の終わり
  "tracks": [
    {"instrument": "bell",  "vel": 0.6, "notes": [{"at": 0, "note": "E5", "len": 1}, ...]},
    {"instrument": "pad",   "vel": 0.3, "notes": [{"at": 0, "chord": "C", "len": 4}, ...]},
    {"instrument": "pluck", "notes": [{"at": 0, "chord": "C", "strum": "D-DU-UDU", "len": 4}]}
  ]
}
instrument: bell（鉄琴風）/ pluck（ウクレレ風の弦）/ pad（やわらかい和音）/ sine / chime（効果音の「ピンポン」）
"""
from __future__ import annotations

import json

import numpy as np

SR = 48000
NOTE_INDEX = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6,
              "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
CHORDS = {"": [0, 4, 7], "m": [0, 3, 7], "7": [0, 4, 7, 10], "maj7": [0, 4, 7, 11], "m7": [0, 3, 7, 10],
          "sus4": [0, 5, 7], "add9": [0, 4, 7, 14]}


def midi(note: str) -> int:
    name = note[:-1]
    octave = int(note[-1])
    return 12 * (octave + 1) + NOTE_INDEX[name]


def freq(m: float) -> float:
    return 440.0 * 2 ** ((m - 69) / 12)


def chord_notes(chord: str, octave: int = 4) -> list[int]:
    root = chord[:2] if len(chord) > 1 and chord[1] in "#b" else chord[:1]
    kind = chord[len(root):]
    base = 12 * (octave + 1) + NOTE_INDEX[root]
    return [base + i for i in CHORDS[kind]]


def voice(instrument: str, f: float, dur: float, vel: float) -> np.ndarray:
    t = np.arange(int(SR * dur)) / SR
    if instrument == "bell":
        y = (np.sin(2 * np.pi * f * t) + 0.45 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 6)
             + 0.25 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 9)) * np.exp(-t * 2.8)
    elif instrument == "pluck":
        # Karplus-Strong（弦をはじいた音）
        n = max(2, int(SR / f))
        buf = np.random.default_rng(int(f)).uniform(-1, 1, n)
        out = np.zeros(len(t))
        for i in range(len(t)):
            out[i] = buf[i % n]
            buf[i % n] = 0.5 * (buf[i % n] + buf[(i + 1) % n]) * 0.996
        y = out
    elif instrument == "pad":
        att = np.minimum(1, t / 0.15)
        rel = np.minimum(1, np.maximum(0, (dur - t) / 0.3))
        y = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2 * t) + 0.15 * np.sin(2 * np.pi * f * 1.003 * t)) * att * rel
    elif instrument == "chime":
        y = np.sin(2 * np.pi * f * t) * np.exp(-t * 4) + 0.3 * np.sin(2 * np.pi * f * 3 * t) * np.exp(-t * 8)
    else:  # sine
        y = np.sin(2 * np.pi * f * t) * np.minimum(1, (dur - t) / 0.05) * np.minimum(1, t / 0.01)
    return (y * vel).astype(np.float32)


def render(score: dict) -> np.ndarray:
    beat = 60.0 / score.get("tempo", 120)
    events = []
    for tr in score["tracks"]:
        inst = tr.get("instrument", "sine")
        tv = tr.get("vel", 0.6)
        for n in tr["notes"]:
            at = n["at"] * beat
            ln = n.get("len", 1) * beat
            v = n.get("vel", 1.0) * tv
            if "chord" in n:
                notes = chord_notes(n["chord"], n.get("octave", 4))
                strum = n.get("strum")
                if strum and inst == "pluck":
                    # 1小節（4拍）を8分音符8つに分けて D=下ストローク、U=上ストローク、-=休み
                    step = ln / len(strum)
                    for k, c in enumerate(strum):
                        if c in "DU":
                            order = notes if c == "D" else notes[::-1]
                            for j, m in enumerate(order):
                                events.append((at + k * step + j * 0.012, inst, freq(m), step * 2.5, v * (0.8 if c == "U" else 1)))
                else:
                    for m in notes:
                        events.append((at, inst, freq(m), ln, v / len(notes) * 1.8))
            else:
                events.append((at, inst, freq(midi(n["note"])), ln, v))
    end = max(e[0] + e[3] for e in events)
    if "length_beats" in score:
        end = max(end, score["length_beats"] * beat)
    out = np.zeros(int(SR * (end + 0.5)), dtype=np.float32)
    for at, inst, f, dur, v in events:
        y = voice(inst, f, dur, v)
        s = int(at * SR)
        out[s:s + len(y)] += y[: len(out) - s]
    peak = np.abs(out).max() or 1
    return out / peak * 0.5


def load(path: str) -> np.ndarray:
    with open(path, encoding="utf-8") as f:
        return render(json.load(f))
