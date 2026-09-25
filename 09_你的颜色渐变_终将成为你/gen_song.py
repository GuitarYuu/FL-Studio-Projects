# -*- coding: utf-8 -*-
"""05「きみいろグラデーション」(你的颜色渐变) —— 终将成为你 粉蓝白渐变甜美风
A 大调 100bpm | 白=music box 留白 → 粉=钢琴/拨弦 → 蓝=弦乐/合唱
hook: 「きみいろグラデーション」落在 Dmaj7 的 maj7 音 (G#4) 上 = 甜味来源
曲式: Intro4 - V8 - Pre4 - C8 - ITL4 - V8 - Pre4 - C8 - Bridge8 - C3(8+3, +1半音) - Outro4 ≈ 3'00"
输出: complete.mid + vocal_main/harm.musicxml (+ 分轨 mid)
"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260927)
BPM = 100
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = HERE
os.makedirs(OUTDIR, exist_ok=True)

p = Piece('きみいろグラデーション (终将成为你 甜美渐变)', BPM, key='A')
piano = p.add(Trk('Piano', 0, 0, vol=78, pan=58, reverb=30))
mb = p.add(Trk('Music Box', 8, 1, vol=58, pan=44, reverb=56))     # 白
bells = p.add(Trk('Bells', 9, 2, vol=46, pan=76, reverb=60))
harp = p.add(Trk('Harp', 46, 3, vol=42, pan=36, reverb=50))
pizz = p.add(Trk('Pizz Strings', 45, 4, vol=50, pan=80, reverb=36))
strings = p.add(Trk('Strings', 48, 5, vol=44, pan=64, reverb=58))  # 蓝
obligo = p.add(Trk('Flute Obligo', 73, 6, vol=40, pan=30, reverb=44))
bass = p.add(Trk('Bass', 33, 7, vol=84, pan=64, reverb=14))
dr = p.add(Drums(vol=92))

INTRO = ['Dmaj7', 'Dmaj7', 'Eadd9', 'Eadd9']
V8 = ['Aadd9', 'C#m7', 'Bm7', 'Eadd9', 'F#m7', 'Dmaj7', 'Bm7', 'Eadd9']
PRE = ['Dmaj7', 'Eadd9', 'F#m7', 'Bm7']
C = ['A', 'E/G#', 'F#m7', 'Dmaj7', 'A/C#', 'D6', 'Eadd9', 'A']
ITL = ['F#m7', 'Dmaj7', 'Bm7', 'Eadd9']
BRK = ['F#m7', 'Dmaj7', 'A', 'Eadd9', 'F#m7', 'Dmaj7', 'Bm7', 'Eadd9']
TAG = ['A', 'Dmaj7', 'A']
SECS = [
    ('Intro', INTRO, 0), ('V1', V8, 0), ('Pre', PRE, 0), ('C1', C, 0),
    ('ITL', ITL, 0), ('V2', V8, 0), ('Pre', PRE, 0), ('C2', C, 0),
    ('Bridge', BRK, 0),
    ('C3', C + TAG, 1),
    ('Outro', ['Aadd9', 'Aadd9', 'Aadd9', 'Aadd9'], 0),
]

# ================= 人声旋律 (bar, beat, dur, pitch, vel, mora) =================
MEL_V_A = [  # しろいキャンバスに
    (0, 0, 1, 'A4', 78, 'し'), (0, 1, 1, 'B4', 80, 'ろ'), (0, 2, 1, 'C#5', 82, 'い'),
    (0, 3, 1.5, 'C#5', 82, 'キャン'), (1, 0.5, 0.5, 'B4', 78, 'バ'), (1, 1, 0.5, 'A4', 76, 'ス'),
    (1, 1.5, 1, 'B4', 80, 'に'),
]
MEL_V_B = [  # はじめてのったピンク
    (2, 0, 0.5, 'E4', 76, 'は'), (2, 0.5, 0.5, 'F#4', 78, 'じ'), (2, 1, 0.5, 'G#4', 80, 'め'),
    (2, 1.5, 0.5, 'A4', 80, 'て'), (2, 2, 1, 'B4', 82, 'のっ'), (2, 3, 1, 'A4', 80, 'た'),
    (3, 0, 1, 'G#4', 80, 'ピン'), (3, 1, 1.5, 'F#4', 78, 'ク'),
]
MEL_V_C = [  # きみのえがおのひとみ
    (4, 0, 1, 'A4', 80, 'き'), (4, 1, 1, 'B4', 82, 'み'), (4, 2, 1, 'C#5', 82, 'の'),
    (4, 3, 0.5, 'C#5', 80, 'え'), (4, 3.5, 0.5, 'B4', 78, 'が'), (5, 0, 1, 'A4', 80, 'お'),
    (5, 1, 0.5, 'G#4', 78, 'の'), (5, 1.5, 0.5, 'A4', 80, 'ひ'), (5, 2, 0.5, 'B4', 82, 'と'),
    (5, 2.5, 1.5, 'C#5', 84, 'み'),
]
MEL_V_D = [  # ほんとのしろをおしえた
    (6, 0, 1, 'D5', 84, 'ほ'), (6, 1, 1, 'C#5', 82, 'ん'), (6, 2, 0.5, 'B4', 80, 'と'),
    (6, 2.5, 0.5, 'A4', 80, 'の'), (6, 3, 1, 'G#4', 80, 'し'), (7, 0, 1, 'F#4', 80, 'ろ'),
    (7, 1, 0.5, 'F#4', 78, 'を'), (7, 1.5, 0.5, 'E4', 76, 'お'), (7, 2, 0.5, 'F#4', 78, 'し'),
    (7, 2.5, 0.5, 'G#4', 80, 'え'), (7, 3, 1, 'A4', 82, 'た'),
]
MEL_PRE_A = [  # そっとふれてみたら
    (0, 0, 1, 'A4', 82, 'そ'), (0, 1, 0.5, 'B4', 82, 'っ'), (0, 1.5, 0.5, 'C#5', 84, 'と'),
    (0, 2, 1, 'D5', 84, 'ふ'), (0, 3, 1, 'C#5', 82, 'れ'), (1, 0, 1, 'B4', 82, 'て'),
    (1, 1, 0.5, 'A4', 80, 'み'), (1, 1.5, 0.5, 'B4', 82, 'た'), (1, 2, 2, 'C#5', 84, 'ら'),
]
MEL_PRE_B = [  # あおくこぼれた
    (2, 0, 1, 'D5', 86, 'あ'), (2, 1, 1, 'C#5', 84, 'お'), (2, 2, 1, 'B4', 82, 'く'),
    (2, 3, 0.5, 'A4', 82, 'こ'), (2, 3.5, 0.5, 'B4', 82, 'ぼ'), (3, 0, 1, 'C#5', 84, 'れ'),
    (3, 1, 2.5, 'D5', 86, 'た'),
]
MEL_C = [  # hook: きみいろグラデーション
    (0, 0, 0.75, 'E5', 88, 'き'), (0, 0.75, 0.75, 'E5', 86, 'み'), (0, 1.5, 1, 'D5', 88, 'い'),
    (0, 2.5, 0.75, 'C#5', 86, 'ろ'), (0, 3.25, 0.75, 'B4', 84, 'グ'),
    (1, 0, 0.5, 'C#5', 86, 'ラ'), (1, 0.5, 0.5, 'D5', 88, 'デ'), (1, 1, 1.5, 'E5', 90, 'デ'),
    (1, 2.5, 1, 'E5', 88, 'ー'), (1, 3.5, 0.5, 'D5', 84, 'ショ'), (2, 0, 0.5, 'C#5', 84, 'ン'),
    # ピンクとあおとしろ
    (2, 1, 0.75, 'B4', 84, 'ピン'), (2, 1.75, 0.75, 'C#5', 86, 'ク'), (2, 2.5, 0.5, 'B4', 82, 'と'),
    (2, 3, 0.5, 'A4', 82, 'あ'), (2, 3.5, 0.5, 'B4', 82, 'お'),
    (3, 0, 0.5, 'A4', 80, 'と'), (3, 0.5, 1, 'G#4', 82, 'し'), (3, 1.5, 2, 'A4', 84, 'ろ'),
    # まざりあうこころ
    (4, 0, 0.5, 'A4', 84, 'ま'), (4, 0.5, 0.5, 'B4', 84, 'ざ'), (4, 1, 0.5, 'C#5', 86, 'り'),
    (4, 1.5, 0.5, 'D5', 86, 'あ'), (4, 2, 1, 'C#5', 86, 'う'), (4, 3, 0.5, 'B4', 82, 'こ'),
    (4, 3.5, 0.5, 'C#5', 84, 'こ'), (5, 0, 1.5, 'D5', 86, 'ろ'),
    # ぬすっとにじんでく
    (5, 1.5, 0.5, 'C#5', 86, 'ぬ'), (5, 2, 0.5, 'B4', 84, 'すっ'), (5, 2.5, 0.5, 'A4', 82, 'と'),
    (5, 3, 0.5, 'B4', 84, 'に'), (5, 3.5, 0.5, 'C#5', 84, 'じ'), (6, 0, 0.5, 'D5', 86, 'ん'),
    (6, 0.5, 0.5, 'E5', 88, 'で'), (6, 1, 1, 'D5', 86, 'く'),
    # ぜんぶぜんぶ だいすきのいろ
    (6, 2, 0.5, 'C#5', 86, 'ぜ'), (6, 2.5, 0.5, 'B4', 84, 'ん'), (6, 3, 0.5, 'C#5', 86, 'ぶ'),
    (6, 3.5, 0.5, 'C#5', 86, 'ぜ'), (7, 0, 0.5, 'B4', 84, 'ん'), (7, 0.5, 0.5, 'A4', 82, 'ぶ'),
    (7, 1, 0.5, 'B4', 86, 'だ'), (7, 1.5, 0.5, 'C#5', 88, 'い'), (7, 2, 0.5, 'D5', 88, 'す'),
    (7, 2.5, 0.5, 'C#5', 86, 'き'), (7, 3, 0.5, 'B4', 84, 'の'), (7, 3.5, 0.5, 'A4', 84, 'い'),
]
MEL_C_END = [(8, 0, 0, None, 0, '')]  # ろ 落在下一拍 (8,0) 由调用端并段后自然衔接
MEL_BRK = [  # Bridge 气声段
    (0, 0, 1, 'C#5', 76, 'し'), (0, 1, 1, 'B4', 74, 'ろ'), (0, 2, 1, 'A4', 74, 'かっ'),
    (0, 3, 1.5, 'B4', 76, 'た'), (1, 0, 1, 'A4', 74, 'こ'), (1, 1, 1, 'G#4', 74, 'こ'),
    (1, 2, 2, 'F#4', 76, 'ろ'),
    (2, 0, 1, 'F#4', 76, 'い'), (2, 1, 1, 'G#4', 76, 'ろ'), (2, 2, 1, 'A4', 78, 'ど'),
    (2, 3, 1, 'B4', 78, 'ら'), (3, 0, 0.5, 'C#5', 80, 'れ'), (3, 0.5, 0.5, 'B4', 78, 'て'),
    (3, 1, 2.5, 'A4', 78, 'く'),
    (4, 0, 0.5, 'A4', 78, 'か'), (4, 0.5, 0.5, 'B4', 80, 'わ'), (4, 1, 0.5, 'C#5', 80, 'っ'),
    (4, 1.5, 0.5, 'D5', 82, 'て'), (4, 2, 0.5, 'C#5', 80, 'の'), (4, 2.5, 0.5, 'B4', 78, 'が'),
    (4, 3, 0.5, 'A4', 78, 'こ'), (4, 3.5, 0.5, 'B4', 78, 'わ'), (5, 0, 0.5, 'C#5', 82, 'く'),
    (5, 0.5, 0.5, 'B4', 78, 'て'), (5, 1, 2, 'A4', 78, 'ー'),
    (6, 0, 0.5, 'A4', 80, 'で'), (6, 0.5, 0.5, 'B4', 82, 'も'), (6, 1, 0.5, 'C#5', 84, 'き'),
    (6, 1.5, 0.5, 'D5', 84, 'み'), (6, 2, 1, 'E5', 86, 'と'), (6, 3, 0.5, 'D5', 84, 'な'),
    (6, 3.5, 0.5, 'C#5', 82, 'ら'), (7, 0, 1.5, 'B4', 84, 'きー'), (7, 1.5, 2.5, 'D5', 86, 'と'),
]
MEL_TAG = [  # (+1 后) きみいろ きみいろ / やさしいいろ
    (0, 0, 1, 'E5', 90, 'き'), (0, 1, 1, 'E5', 88, 'み'), (0, 2, 1, 'D5', 88, 'い'),
    (0, 3, 1, 'C#5', 86, 'ろ'),
    (1, 0, 1, 'E5', 90, 'き'), (1, 1, 1, 'E5', 88, 'み'), (1, 2, 1, 'D5', 88, 'い'),
    (1, 3, 1, 'C#5', 86, 'ろ'),
    (2, 0, 1, 'D5', 88, 'や'), (2, 1, 1, 'C#5', 86, 'さ'), (2, 2, 1, 'C#5', 86, 'し'),
    (2, 3, 1, 'B4', 84, 'い'), (3, 0, 0.5, 'B4', 84, 'い'), (3, 0.5, 2.5, 'A4', 86, 'ろ'),
]

HOOK_MB = [  # hook 缩影 (music box / flute 用)
    (0, 0.0, 0.5, 'E5', 88), (0, 0.5, 0.5, 'E5', 86), (0, 1.0, 0.75, 'D5', 88),
    (0, 1.75, 0.75, 'C#5', 86), (0, 2.5, 0.75, 'B4', 84), (0, 3.25, 0.75, 'C#5', 86),
    (1, 0.0, 0.75, 'D5', 88), (1, 0.75, 1.5, 'E5', 90),
]


def sing(trk, sec_start, evts, tr=0):
    out = []
    for e in evts:
        b, bt, d, pp, v = e[0], e[1], e[2], e[3], e[4]
        mora = e[5] if len(e) > 5 else None
        m = npitch(pp) + tr
        trk.n(sec_start + b * 4 + bt, d, m, v)
        out.append((sec_start + b * 4 + bt, d, m, mora))
    return out


def sh(evs, nbars):
    return [(b + nbars, bt, d, p, v) + tuple(e[5:]) for e in evs]


# ---------------- 装配 ----------------
t0 = 0.0
xml_main, xml_harm = [], []
for si, (name, chords, tr) in enumerate(SECS):
    cs = [Chord(c).shifted(tr) for c in chords]
    nbars = len(cs)
    start = t0
    for i, c in enumerate(cs):
        b = start + i * 4
        if name == 'Intro':
            # 白: music box 分解 + 长铃
            tones = c.voice(low=64, high=88, n=4)
            for k in range(8):
                mb.n(b + k * 0.5, 0.45, tones[k % len(tones)], hum(rng, 56 - (4 if k % 2 else 0)))
            if i == 0:
                sing(mb, start, [(bb, bt, d, pp, v) for (bb, bt, d, pp, v) in HOOK_MB],
                     tr=tr)
            pad_long = c.voice(low=48, high=64, n=3)
            strings.chord(b, 3.9, pad_long, hum(rng, 24))
        elif name in ('V1', 'V2'):
            # 粉: 钢琴 8 分分解 + 拨弦反拍 + 软鼓
            tones = c.voice(low=60, high=81, n=4)
            pat = [0, 2, 1, 3, 2, 1, 3, 2]
            for k in range(8):
                piano.n(b + k * 0.5, 0.45, tones[pat[k] % len(tones)], hum(rng, 62 - (8 if k % 2 else 0)))
            pt = c.voice(low=55, high=71, n=2)
            for k in range(4):
                for pp2 in pt:
                    pizz.n(b + 0.5 + k, 0.2, pp2, hum(rng, 44))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 74))
            bass.n(b + 2, 1.9, c.bass_midi(2) + (7 if c.kind not in ('m', 'm7') else 3), hum(rng, 68))
            dr.hits(b, [(0, 36, 66), (1, 37, 58), (2, 36, 58), (2.5, 36, 54), (3, 37, 60)]
                    + [(k * 0.5, 42, 36 if k % 2 else 44) for k in range(8)])
            if i == nbars - 1:
                dr.hits(b, [(3.5, 42, 60), (3.75, 42, 68)])
        elif name == 'Pre':
            piano.chord(b, 1.9, c.voice(low=58, high=76, n=3), hum(rng, 60))
            piano.chord(b + 2, 1.9, c.voice(low=58, high=76, n=3), hum(rng, 56))
            sv = c.voice(low=57, high=76, n=3)
            strings.chord(b, 3.9, sv, hum(rng, 32 + i * 4))
            harp_chord = sv + [sv[0] + 12]
            for k in range(4):
                harp.n(b + k, 0.9, harp_chord[k % len(harp_chord)], hum(rng, 38))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 76))
            bass.n(b + 2, 1.9, c.bass_midi(2), hum(rng, 72))
            dr.hits(b, ([(0, 36, 72), (2, 36, 68)]
                        + [(k * 0.25, 42, min(84, 38 + k * 3)) for k in range(16)]
                        if i == nbars - 1 else
                        [(0, 36, 72), (2, 36, 68)] + [(k * 0.5, 42, 42) for k in range(8)]))
            if i == nbars - 1:
                dr.hits(b, [(3.5, 38, 84), (3.75, 38, 92)])
        elif name in ('C1', 'C2', 'C3'):
            # 蓝: 全奏
            for k in range(8):
                piano.n(b + k * 0.5, 0.42, c.voice(low=60, high=84, n=3)[k % 3]
                        if k % 2 else c.bass_midi(3) + 12, hum(rng, 68))
            strings.chord(b, 3.85, c.voice(low=59, high=79, n=4), hum(rng, 44))
            synth_arp16(harp, b, c, rng, vel=40)
            bells.n(b, 0.6, c.voice(low=76, high=90, n=1)[0], hum(rng, 52))
            bass_funk = c.bass_midi(2)
            for k in range(4):
                bass.n(b + k, 0.8, bass_funk if k % 2 == 0 else bass_funk + 7, hum(rng, 82 - 6 * (k % 2)))
            dr.hits(b, [(0, 36, 92), (1.5, 36, 74), (2.5, 36, 84), (1, 38, 84), (3, 38, 86)]
                    + [(k * 0.5, 42, 44 if k % 2 else 56) for k in range(8)])
            if i == 0:
                crash(dr, b, vel=74)
            if i == nbars - 1 and name != 'C3':
                dr.hits(b, [(3.5, 38, 88), (3.75, 43, 92)])
        elif name == 'ITL':
            for k in range(8):
                mb.n(b + k * 0.5, 0.45, c.voice(low=64, high=88, n=3)[k % 3], hum(rng, 50))
            strings.chord(b, 3.9, c.voice(low=50, high=68, n=3), hum(rng, 26))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 70))
            bass.n(b + 2, 1.9, c.bass_midi(2) + 5, hum(rng, 64))
            dr.hits(b, [(0, 36, 60), (2, 36, 56)] + [(k * 0.5, 42, 34) for k in range(8)])
            sing(obligo, b, HOOK_MB[4:], tr=tr, ) if i == 1 else None
        elif name == 'Bridge':
            if i < 4:
                # 音乐盒独白 + 弦乐软垫, 鼓几乎静默
                mb.n(b, 1.9, c.voice(low=72, high=86, n=1)[0], hum(rng, 46))
                mb.n(b + 2, 1.9, c.voice(low=72, high=86, n=1)[0] - 5, hum(rng, 42))
                strings.chord(b, 3.9, c.voice(low=52, high=68, n=3), hum(rng, 26))
                piano.n(b, 2.9, c.voice(low=54, high=70, n=2)[0], hum(rng, 48))
                bass.n(b, 3.8, c.bass_midi(2), hum(rng, 60))
                dr.hits(b, [(0, 36, 44)])
            else:
                # build: 钢琴 8 分 + 军鼓滚入
                piano.chord(b, 1.9, c.voice(low=58, high=78, n=3), hum(rng, 62))
                strings.chord(b, 3.9, c.voice(low=55, high=74, n=3), hum(rng, 34 + (i - 4) * 6))
                bass.n(b, 1.9, c.bass_midi(2), hum(rng, 74))
                dr.hits(b, [(0, 36, 64), (2, 36, 60)] +
                        ([(k * 0.25, 38, min(110, 40 + (i - 4) * 8 + k * 4)) for k in range(16)]
                         if i == 7 else [(k * 0.5, 42, 40) for k in range(8)]))
        elif name == 'Outro':
            if i < 3:
                mb.n(b, 3.8, c.voice(low=76, high=90, n=1)[0], hum(rng, 52 - i * 10))
                piano.chord(b, 3.8, c.voice(low=57, high=76, n=3), hum(rng, 54 - i * 8))
                strings.chord(b, 3.9, c.voice(low=57, high=73, n=3), hum(rng, 30 - i * 6))
                bells.n(b, 2.5, c.voice(low=76, high=92, n=1)[0] + 12, hum(rng, 40 - i * 8))
                bass.n(b, 3.8, c.bass_midi(2), hum(rng, 58 - i * 8))
            if i == 0:
                crash(dr, b, vel=66, note=57)
                sing(mb, b, [(bb * 2, bt, d, pp, v) for (bb, bt, d, pp, v) in
                             [(0, 0.0, 0.5, 'E5', 84), (0, 0.5, 0.5, 'E5', 82),
                              (0, 1.0, 0.75, 'D5', 84), (0, 1.75, 0.75, 'C#5', 82),
                              (0, 2.5, 0.75, 'B4', 80), (1, 0.0, 2.0, 'A4', 82)]])

    # ---- 人声段 ----
    t0 = start + nbars * 4


def dn3(name):
    """下方三度"""
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    m = npitch(name) - 3
    return names[m % 12] + str(m // 12 - 1)


# 段落起点重算 (与上面硬编码一致, 校验)
offs = {}
t0 = 0.0
for name, chords, tr in SECS:
    offs[name + str(t0)] = t0
    t0 = start = t0 + len(chords) * 4
print('total bars:', int(t0 // 4), ' time: %.1fs' % (t0 * 60 / BPM))
print('sections:', [(k, int(v // 4)) for k, v in offs.items()][:6], '...')

# 硬编码段起点核对: V1=4, Pre=12, C1=16, V2=28, Pre=36, C2=40, Bridge=48, C3=56
# 由 SECS 累加: Intro4 V8(->12) Pre4(->16) C8(->24) ITL4(->28) V8(->36) Pre4(->40) C8(->48)
# Bridge8(->56) C3 11(->67) Outro4(->71)
# 修正: 上面 vgather 的段起点有误, 重算
xml_main, xml_harm = [], []
vgather = Trk('gather', 0, 15)
sec_start_map = {'V1': 4, 'Pre1': 12, 'C1': 16, 'V2': 28, 'Pre2': 36, 'C2': 40,
                 'Bridge': 48, 'C3': 56}
for nm, st, tr in [('V1', 4, 0), ('Pre', 12, 0), ('C1', 16, 0), ('V2', 28, 0),
                   ('Pre', 36, 0), ('C2', 40, 0), ('Bridge', 48, 0), ('C3', 56, 1)]:
    stb = st * 4
    if nm == 'V1':
        xml_main += sing(vgather, stb, MEL_V_A + MEL_V_B + MEL_V_C + MEL_V_D, tr=tr)
    elif nm == 'Pre':
        xml_main += sing(vgather, stb, MEL_PRE_A + MEL_PRE_B, tr=tr)
        xml_harm += sing(vgather, stb, [(3, 1, 2.5, 'A4', 70, 'ら')], tr=tr)
    elif nm in ('C1', 'C2'):
        xml_main += sing(vgather, stb, MEL_C, tr=tr)
        h3 = [(b, bt, d, dn3(p), max(60, v - 16)) for (b, bt, d, p, v, *_m) in MEL_C[:16]]
        xml_harm += sing(vgather, stb, h3, tr=tr)
    elif nm == 'Bridge':
        xml_main += sing(vgather, stb, MEL_BRK, tr=tr)
    elif nm == 'C3':
        xml_main += sing(vgather, stb, MEL_C + MEL_TAG, tr=tr)
        h3 = [(b, bt, d, dn3(p), max(60, v - 16)) for (b, bt, d, p, v, *_m) in MEL_C[:16]]
        xml_harm += sing(vgather, stb, h3, tr=tr)

print(f'vocal main: {len(xml_main)} notes, harm: {len(xml_harm)} notes')
lo = min(m for _, _, m, _ in xml_main); hi = max(m for _, _, m, _ in xml_main)
names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
print(f'range: {names[lo%12]}{lo//12-1} ~ {names[hi%12]}{hi//12-1}')

# ================= 输出 =================
TOTAL = int(t0 // 4)
base = os.path.join(OUTDIR, '05_你的颜色渐变_终将成为你')
p.save(base + '_complete.mid')
print('saved:', base + '_complete.mid')

# 分轨 vocal mid
pv = Piece('vocal main', BPM, key='A')
tvm = pv.add(Trk('Lead Vocal', 53, 0, vol=100, pan=64, reverb=34))
for bt, d, m, mora in xml_main:
    tvm.n(bt, d, m, 100)
pv.save(base + '_vocal_main.mid')
ph2 = Piece('vocal harm', BPM, key='A')
tvh = ph2.add(Trk('Harm Vocal', 53, 0, vol=100, pan=64, reverb=40))
for bt, d, m, mora in xml_harm:
    tvh.n(bt, d, m, 100)
ph2.save(base + '_vocal_harm.mid')


def pitch_step(midi):
    sharps = {1: ('C', 1), 3: ('D', 1), 6: ('F', 1), 8: ('G', 1), 10: ('A', 1)}
    names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    pc, octave = midi % 12, midi // 12 - 1
    if pc in sharps:
        s, a = sharps[pc]
    else:
        s, a = names[[0, 2, 4, 5, 7, 9, 11].index(pc)], 0
    return s, a, octave


def note_type(d):
    if d >= 3.75: return 'whole'
    if d >= 1.75: return 'half'
    if d >= 0.875: return 'quarter'
    if d >= 0.43: return 'eighth'
    return '16th'


def rest_xml(dur_beats, DIV):
    return ('<note><rest/><duration>%d</duration><voice>1</voice><type>%s</type></note>'
            % (int(round(dur_beats * DIV)), note_type(dur_beats)))


def write_musicxml(path, notes, bpm, total_bars, key_fifths=3):
    DIV = 4
    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" '
         '"http://www.musicxml.org/dtds/partwise.dtd">',
         '<score-partwise version="3.1">',
         '<part-list><score-part id="P1"><part-name>Vocal</part-name></score-part></part-list>',
         '<part id="P1">']
    by_bar = {}
    for bt, d, m, mora in notes:
        by_bar.setdefault(int(bt // 4), []).append((bt - int(bt // 4) * 4, d, m, mora))
    for bar in range(total_bars):
        L.append(f'<measure number="{bar + 1}">')
        if bar == 0:
            L.append('<attributes><divisions>%d</divisions><key><fifths>%d</fifths></key>'
                     '<time><beats>4</beats><beat-type>4</beat-type></time></attributes>'
                     % (DIV, key_fifths))
            L.append('<direction placement="above"><direction-type><metronome>'
                     '<beat-unit>quarter</beat-unit><per-minute>%d</per-minute></metronome>'
                     '</direction-type><sound tempo="%d"/></direction>' % (bpm, bpm))
        pos = 0.0
        for bt, d, m, mora in sorted(by_bar.get(bar, []), key=lambda x: x[0]):
            if bt > pos + 1e-6:
                L.append(rest_xml(bt - pos, DIV))
                pos = bt
            step, alter, octave = pitch_step(m)
            L.append('<note><pitch><step>%s</step>%s<octave>%d</octave></pitch>'
                     '<duration>%d</duration><voice>1</voice><type>%s</type>'
                     % (step, ('<alter>%d</alter>' % alter) if alter else '',
                        octave, int(round(d * DIV)), note_type(d)))
            if mora:
                L.append('<lyric number="1"><text>%s</text></lyric>' % html.escape(mora))
            L.append('</note>')
            pos = bt + d
        if pos < 4 - 1e-6:
            L.append(rest_xml(4 - pos, DIV))
        L.append('</measure>')
    L.append('</part></score-partwise>')
    open(path, 'w', encoding='utf-8').write('\n'.join(L))
    print('saved:', path)


write_musicxml(base + '_vocal_main.musicxml', xml_main, BPM, TOTAL)
write_musicxml(base + '_vocal_harm.musicxml', [(bt, d, m, 'ら') for bt, d, m, _ in xml_harm],
               BPM, TOTAL)
