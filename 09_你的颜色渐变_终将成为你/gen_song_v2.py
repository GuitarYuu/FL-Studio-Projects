# -*- coding: utf-8 -*-
"""05「きみいろグラデーション」v2 —— 层次/密度/酸甜升级
v1 保留在 git。v2 变化:
  【颜色+1】橙 = E.Piano(prog4) 暖和声 + Vibraphone(prog11) 玻璃光泽 16 分闪光
  【酸甜】  借用 iv 级 Dm6 (V1无词尾/Pre末长音下/Bridge末/Outro2) + B7(V/V) + E9 转位,
            全部避开人声长音冲突音 (酸=悬停不解决, 甜=大七度/九和弦)
  【密度】  副歌钢琴16分drive+弦乐内声部8分移动+颤音琴高音16分+军鼓16分hat;
            主歌竖琴8分+贝斯经过音+16分hat ghost; 和声轨扩到全副歌+tag
人声主旋律/歌词不变 (复用已有 NEUTRINO 主唱), 和声轨重渲染。
输出: *_v2_complete.mid / *_v2_vocal_harm.musicxml 等 (main musicxml 不变不重出)
"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260927)
BPM = 100
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = HERE
os.makedirs(OUTDIR, exist_ok=True)

p = Piece('きみいろグラデーション v2 (四色酸甜)', BPM, key='A')
piano = p.add(Trk('Piano', 0, 0, vol=80, pan=58, reverb=30))       # 粉
mb = p.add(Trk('Music Box', 8, 1, vol=56, pan=44, reverb=56))      # 白
bells = p.add(Trk('Bells', 9, 2, vol=44, pan=76, reverb=60))
harp = p.add(Trk('Harp', 46, 3, vol=46, pan=36, reverb=50))
pizz = p.add(Trk('Pizz Strings', 45, 4, vol=52, pan=80, reverb=36))
strings = p.add(Trk('Strings', 48, 5, vol=46, pan=64, reverb=58))  # 蓝
obligo = p.add(Trk('Flute Obligo', 73, 6, vol=42, pan=30, reverb=44))
bass = p.add(Trk('Bass', 33, 7, vol=86, pan=64, reverb=14))
ep2 = p.add(Trk('E.Piano Warm', 4, 8, vol=52, pan=72, reverb=40))  # 橙
vibes = p.add(Trk('Vibraphone', 11, 12, vol=42, pan=20, reverb=52))  # 橙
dr = p.add(Drums(vol=94))

INTRO = ['Dmaj7', 'Dmaj7', 'Eadd9', 'Eadd9']
V8 = ['Aadd9', 'C#m7', 'Bm7', 'Eadd9', 'F#m7', 'B7', 'Bm7', 'E7']
PRE = ['Dmaj7', 'Eadd9', 'F#m7', 'Dm6']
C = ['A', 'E/G#', 'F#m7', 'Dmaj7', 'A/C#', 'D6', 'E9', 'A']
ITL = ['F#m7', 'Dmaj7', 'Bm7', 'Eadd9']
BRK = ['F#m7', 'Dmaj7', 'A', 'Eadd9', 'F#m7', 'Dmaj7', 'Dm6', 'E7']
TAG = ['A', 'Dmaj7', 'A']
SECS = [
    ('Intro', INTRO, 0), ('V1', V8, 0), ('Pre', PRE, 0), ('C1', C, 0),
    ('ITL', ITL, 0), ('V2', V8, 0), ('Pre', PRE, 0), ('C2', C, 0),
    ('Bridge', BRK, 0),
    ('C3', C + TAG, 1),
    ('Outro', ['Aadd9', 'Dm6', 'Eadd9', 'Aadd9'], 0),
]

# ============ 人声主旋律 (与 v1 完全一致) ============
MEL_V_A = [
    (0, 0, 1, 'A4', 78, 'し'), (0, 1, 1, 'B4', 80, 'ろ'), (0, 2, 1, 'C#5', 82, 'い'),
    (0, 3, 1.5, 'C#5', 82, 'キャン'), (1, 0.5, 0.5, 'B4', 78, 'バ'), (1, 1, 0.5, 'A4', 76, 'ス'),
    (1, 1.5, 1, 'B4', 80, 'に'),
]
MEL_V_B = [
    (2, 0, 0.5, 'E4', 76, 'は'), (2, 0.5, 0.5, 'F#4', 78, 'じ'), (2, 1, 0.5, 'G#4', 80, 'め'),
    (2, 1.5, 0.5, 'A4', 80, 'て'), (2, 2, 1, 'B4', 82, 'のっ'), (2, 3, 1, 'A4', 80, 'た'),
    (3, 0, 1, 'G#4', 80, 'ピン'), (3, 1, 1.5, 'F#4', 78, 'ク'),
]
MEL_V_C = [
    (4, 0, 1, 'A4', 80, 'き'), (4, 1, 1, 'B4', 82, 'み'), (4, 2, 1, 'C#5', 82, 'の'),
    (4, 3, 0.5, 'C#5', 80, 'え'), (4, 3.5, 0.5, 'B4', 78, 'が'), (5, 0, 1, 'A4', 80, 'お'),
    (5, 1, 0.5, 'G#4', 78, 'の'), (5, 1.5, 0.5, 'A4', 80, 'ひ'), (5, 2, 0.5, 'B4', 82, 'と'),
    (5, 2.5, 1.5, 'C#5', 84, 'み'),
]
MEL_V_D = [
    (6, 0, 1, 'D5', 84, 'ほ'), (6, 1, 1, 'C#5', 82, 'ん'), (6, 2, 0.5, 'B4', 80, 'と'),
    (6, 2.5, 0.5, 'A4', 80, 'の'), (6, 3, 1, 'G#4', 80, 'し'), (7, 0, 1, 'F#4', 80, 'ろ'),
    (7, 1, 0.5, 'F#4', 78, 'を'), (7, 1.5, 0.5, 'E4', 76, 'お'), (7, 2, 0.5, 'F#4', 78, 'し'),
    (7, 2.5, 0.5, 'G#4', 80, 'え'), (7, 3, 1, 'A4', 82, 'た'),
]
MEL_PRE_A = [
    (0, 0, 1, 'A4', 82, 'そ'), (0, 1, 0.5, 'B4', 82, 'っ'), (0, 1.5, 0.5, 'C#5', 84, 'と'),
    (0, 2, 1, 'D5', 84, 'ふ'), (0, 3, 1, 'C#5', 82, 'れ'), (1, 0, 1, 'B4', 82, 'て'),
    (1, 1, 0.5, 'A4', 80, 'み'), (1, 1.5, 0.5, 'B4', 82, 'た'), (1, 2, 2, 'C#5', 84, 'ら'),
]
MEL_PRE_B = [
    (2, 0, 1, 'D5', 86, 'あ'), (2, 1, 1, 'C#5', 84, 'お'), (2, 2, 1, 'B4', 82, 'く'),
    (2, 3, 0.5, 'A4', 82, 'こ'), (2, 3.5, 0.5, 'B4', 82, 'ぼ'), (3, 0, 1, 'C#5', 84, 'れ'),
    (3, 1, 2.5, 'D5', 86, 'た'),
]
MEL_C = [
    (0, 0, 0.75, 'E5', 88, 'き'), (0, 0.75, 0.75, 'E5', 86, 'み'), (0, 1.5, 1, 'D5', 88, 'い'),
    (0, 2.5, 0.75, 'C#5', 86, 'ろ'), (0, 3.25, 0.75, 'B4', 84, 'グ'),
    (1, 0, 0.5, 'C#5', 86, 'ラ'), (1, 0.5, 0.5, 'D5', 88, 'デ'), (1, 1, 1.5, 'E5', 90, 'デ'),
    (1, 2.5, 1, 'E5', 88, 'ー'), (1, 3.5, 0.5, 'D5', 84, 'ショ'), (2, 0, 0.5, 'C#5', 84, 'ン'),
    (2, 1, 0.75, 'B4', 84, 'ピン'), (2, 1.75, 0.75, 'C#5', 86, 'ク'), (2, 2.5, 0.5, 'B4', 82, 'と'),
    (2, 3, 0.5, 'A4', 82, 'あ'), (2, 3.5, 0.5, 'B4', 82, 'お'),
    (3, 0, 0.5, 'A4', 80, 'と'), (3, 0.5, 1, 'G#4', 82, 'し'), (3, 1.5, 2, 'A4', 84, 'ろ'),
    (4, 0, 0.5, 'A4', 84, 'ま'), (4, 0.5, 0.5, 'B4', 84, 'ざ'), (4, 1, 0.5, 'C#5', 86, 'り'),
    (4, 1.5, 0.5, 'D5', 86, 'あ'), (4, 2, 1, 'C#5', 86, 'う'), (4, 3, 0.5, 'B4', 82, 'こ'),
    (4, 3.5, 0.5, 'C#5', 84, 'こ'), (5, 0, 1.5, 'D5', 86, 'ろ'),
    (5, 1.5, 0.5, 'C#5', 86, 'ぬ'), (5, 2, 0.5, 'B4', 84, 'すっ'), (5, 2.5, 0.5, 'A4', 82, 'と'),
    (5, 3, 0.5, 'B4', 84, 'に'), (5, 3.5, 0.5, 'C#5', 84, 'じ'), (6, 0, 0.5, 'D5', 86, 'ん'),
    (6, 0.5, 0.5, 'E5', 88, 'で'), (6, 1, 1, 'D5', 86, 'く'),
    (6, 2, 0.5, 'C#5', 86, 'ぜ'), (6, 2.5, 0.5, 'B4', 84, 'ん'), (6, 3, 0.5, 'C#5', 86, 'ぶ'),
    (6, 3.5, 0.5, 'C#5', 86, 'ぜ'), (7, 0, 0.5, 'B4', 84, 'ん'), (7, 0.5, 0.5, 'A4', 82, 'ぶ'),
    (7, 1, 0.5, 'B4', 86, 'だ'), (7, 1.5, 0.5, 'C#5', 88, 'い'), (7, 2, 0.5, 'D5', 88, 'す'),
    (7, 2.5, 0.5, 'C#5', 86, 'き'), (7, 3, 0.5, 'B4', 84, 'の'), (7, 3.5, 0.5, 'A4', 84, 'い'),
]
MEL_BRK = [
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
MEL_TAG = [
    (0, 0, 1, 'E5', 90, 'き'), (0, 1, 1, 'E5', 88, 'み'), (0, 2, 1, 'D5', 88, 'い'),
    (0, 3, 1, 'C#5', 86, 'ろ'),
    (1, 0, 1, 'E5', 90, 'き'), (1, 1, 1, 'E5', 88, 'み'), (1, 2, 1, 'D5', 88, 'い'),
    (1, 3, 1, 'C#5', 86, 'ろ'),
    (2, 0, 1, 'D5', 88, 'や'), (2, 1, 1, 'C#5', 86, 'さ'), (2, 2, 1, 'C#5', 86, 'し'),
    (2, 3, 1, 'B4', 84, 'い'), (3, 0, 0.5, 'B4', 84, 'い'), (3, 0.5, 2.5, 'A4', 86, 'ろ'),
]
HOOK_MB = [
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


def dn3(name):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    m = npitch(name) - 3
    return names[m % 12] + str(m // 12 - 1)


# ---------------- 装配 ----------------
t0 = 0.0
xml_harm = []
for si, (name, chords, tr) in enumerate(SECS):
    cs = [Chord(c).shifted(tr) for c in chords]
    nbars = len(cs)
    start = t0
    for i, c in enumerate(cs):
        b = start + i * 4
        if name == 'Intro':
            tones = c.voice(low=64, high=88, n=4)
            for k in range(8):
                mb.n(b + k * 0.5, 0.45, tones[k % len(tones)], hum(rng, 56 - (4 if k % 2 else 0)))
            if i == 0:
                sing(mb, start, HOOK_MB, tr=tr)
            strings.chord(b, 3.9, c.voice(low=48, high=64, n=3), hum(rng, 24))
            if i >= 2:
                for k in range(8):      # 白渐入粉: 竖琴 16 分接入
                    harp.n(b + k * 0.5, 0.4, c.voice(low=57, high=76, n=3)[k % 3], hum(rng, 34))
        elif name in ('V1', 'V2'):
            # 粉 + 橙: 钢琴 8 分 + 小节尾 16 分经过 + 电钢琴切分 + 颤音琴点缀
            tones = c.voice(low=60, high=81, n=4)
            pat = [0, 2, 1, 3, 2, 1, 3, 2]
            for k in range(8):
                piano.n(b + k * 0.5, 0.45, tones[pat[k] % len(tones)], hum(rng, 64 - (8 if k % 2 else 0)))
            piano.n(b + 3.75, 0.22, tones[(pat[7] + 1) % len(tones)], hum(rng, 54))
            piano.n(b + 3.9375, 0.06, tones[(pat[7] + 2) % len(tones)], hum(rng, 44))
            ep2.chord(b + 0.5, 0.7, c.voice(low=59, high=74, n=3), hum(rng, 42))
            ep2.chord(b + 2.5, 0.6, c.voice(low=59, high=74, n=3), hum(rng, 38))
            ep2.chord(b + 3.5, 0.4, c.voice(low=62, high=78, n=2), hum(rng, 40))
            vibes.n(b, 0.8, c.voice(low=79, high=91, n=1)[0], hum(rng, 40))
            vibes.n(b + 2.0, 0.6, c.voice(low=79, high=91, n=1)[0] - 5, hum(rng, 34))
            pt = c.voice(low=55, high=71, n=2)
            for k in range(4):
                for pp2 in pt:
                    pizz.n(b + 0.5 + k, 0.2, pp2, hum(rng, 46))
            for k in range(4):          # 竖琴 8 分 (密度)
                harp.n(b + k, 0.85, c.voice(low=57, high=76, n=3)[k % 3], hum(rng, 32))
            r = c.bass_midi(2)
            bass.n(b, 0.9, r, hum(rng, 78))
            bass.n(b + 1.5, 0.4, r + 7, hum(rng, 66))
            bass.n(b + 2, 0.9, r, hum(rng, 72))
            bass.n(b + 3, 0.45, r + (10 if c.kind in ('m', 'm7') else 9), hum(rng, 62))
            bass.n(b + 3.5, 0.4, r + 12, hum(rng, 64))
            dr.hits(b, [(0, 36, 68), (1, 37, 60), (2, 36, 60), (2.5, 36, 56), (3, 37, 62),
                        (3.75, 37, 30)]
                    + [(k * 0.5, 42, 38 if k % 2 else 46) for k in range(8)]
                    + [(1.75, 42, 30), (3.25, 42, 30)])
            if i == nbars - 1:
                dr.hits(b, [(3.5, 42, 62), (3.625, 42, 70), (3.75, 42, 78), (3.875, 42, 86)])
        elif name == 'Pre':
            piano.chord(b, 1.9, c.voice(low=58, high=76, n=3), hum(rng, 62))
            piano.chord(b + 2, 1.9, c.voice(low=58, high=76, n=3), hum(rng, 58))
            ep2.chord(b + 1, 0.8, c.voice(low=59, high=74, n=3), hum(rng, 44))
            ep2.chord(b + 3, 0.8, c.voice(low=59, high=74, n=3), hum(rng, 42))
            sv = c.voice(low=57, high=76, n=3)
            strings.chord(b, 3.9, sv, hum(rng, 34 + i * 4))
            hc = sv + [sv[0] + 12]
            for k in range(4):
                harp.n(b + k, 0.9, hc[k % len(hc)], hum(rng, 40))
                harp.n(b + k + 0.5, 0.4, hc[(k + 1) % len(hc)], hum(rng, 30))
            vibes.n(b + 0.5, 0.5, sv[-1] + 12, hum(rng, 36))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 78))
            bass.n(b + 2, 1.9, c.bass_midi(2), hum(rng, 74))
            bass.n(b + 3.5, 0.4, c.bass_midi(2) + 5, hum(rng, 66))
            dr.hits(b, ([(0, 36, 74), (2, 36, 70)]
                        + [(k * 0.25, 42, min(86, 40 + k * 3)) for k in range(16)]
                        if i == nbars - 1 else
                        [(0, 36, 74), (2, 36, 70)] + [(k * 0.5, 42, 44) for k in range(8)]
                        + [(1.5, 37, 40), (3.5, 37, 42)]))
            if i == nbars - 1:
                dr.hits(b, [(3.5, 38, 86), (3.75, 38, 94)])
        elif name in ('C1', 'C2', 'C3'):
            # 蓝+橙 全奏高密度
            piano_drive16(piano, b, c, rng, vel=72)
            strings.chord(b, 3.85, c.voice(low=59, high=79, n=4), hum(rng, 46))
            sv2 = c.voice(low=64, high=80, n=2)     # 弦乐内声部 8 分移动 (层次)
            for k in range(4):
                strings.n(b + k, 0.85, sv2[k % 2], hum(rng, 36))
            synth_arp16(harp, b, c, rng, vel=42)
            vt = c.voice(low=79, high=93, n=2)
            for k in range(16):                      # 颤音琴 16 分玻璃闪光 (橙)
                vibes.n(b + k * 0.25, 0.2, vt[k % 2] + (12 if k % 8 == 4 else 0),
                        hum(rng, 38 if k % 4 else 46))
            bells.n(b, 0.6, c.voice(low=76, high=90, n=1)[0], hum(rng, 52))
            ep2.chord(b + 0.5, 0.4, c.voice(low=64, high=80, n=3), hum(rng, 46))
            ep2.chord(b + 2.5, 0.4, c.voice(low=64, high=80, n=3), hum(rng, 42))
            r = c.bass_midi(2)
            for k in range(4):
                bass.n(b + k, 0.75, r if k % 2 == 0 else r + 7, hum(rng, 86 - 6 * (k % 2)))
            bass.n(b + 3.5, 0.4, r + 12, hum(rng, 70))
            dr.hits(b, [(0, 36, 94), (1.5, 36, 76), (2.5, 36, 86), (2.75, 36, 62),
                        (1, 38, 86), (3, 38, 88)]
                    + [(k * 0.25, 42, 40 if k % 2 else 52) for k in range(16)])
            if i == 0:
                crash(dr, b, vel=76)
            if i == nbars - 1 and name != 'C3':
                dr.hits(b, [(3.5, 38, 90), (3.625, 38, 96), (3.75, 43, 98), (3.875, 45, 92)])
        elif name == 'ITL':
            for k in range(8):
                mb.n(b + k * 0.5, 0.45, c.voice(low=64, high=88, n=3)[k % 3], hum(rng, 50))
            sing(obligo, b, HOOK_MB[4:], tr=tr) if i == 1 else None
            ep2.chord(b + 0.5, 1.4, c.voice(low=59, high=76, n=3), hum(rng, 44))
            vibes.n(b, 1.5, c.voice(low=79, high=91, n=1)[0], hum(rng, 38))
            strings.chord(b, 3.9, c.voice(low=50, high=68, n=3), hum(rng, 28))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 72))
            bass.n(b + 2, 1.9, c.bass_midi(2) + 5, hum(rng, 66))
            dr.hits(b, [(0, 36, 62), (2, 36, 58)] + [(k * 0.5, 42, 36) for k in range(8)]
                    + [(1.75, 37, 34), (3.25, 42, 30)])
        elif name == 'Bridge':
            if i < 4:
                mb.n(b, 1.9, c.voice(low=72, high=86, n=1)[0], hum(rng, 46))
                mb.n(b + 2, 1.9, c.voice(low=72, high=86, n=1)[0] - 5, hum(rng, 42))
                strings.chord(b, 3.9, c.voice(low=52, high=68, n=3), hum(rng, 28))
                piano.n(b, 2.9, c.voice(low=54, high=70, n=2)[0], hum(rng, 50))
                ep2.chord(b + 2, 1.8, c.voice(low=59, high=74, n=2), hum(rng, 36))
                bass.n(b, 3.8, c.bass_midi(2), hum(rng, 62))
                dr.hits(b, [(0, 36, 46)])
            else:
                piano_drive16(piano, b, c, rng, vel=66)
                strings.chord(b, 3.9, c.voice(low=55, high=74, n=3), hum(rng, 36 + (i - 4) * 6))
                ep2.chord(b + 0.5, 0.7, c.voice(low=59, high=76, n=3), hum(rng, 44))
                ep2.chord(b + 2.5, 0.7, c.voice(low=59, high=76, n=3), hum(rng, 42))
                bass.n(b, 1.9, c.bass_midi(2), hum(rng, 76))
                bass.n(b + 2, 1.9, c.bass_midi(2), hum(rng, 72))
                dr.hits(b, [(0, 36, 66), (2, 36, 62)] +
                        ([(k * 0.25, 38, min(112, 42 + (i - 4) * 8 + k * 4)) for k in range(16)]
                         if i == 7 else [(k * 0.5, 42, 42) for k in range(8)]
                         + [(1.5, 37, 40), (3.5, 37, 42)]))
        elif name == 'Outro':
            if i < 3:
                mb.n(b, 3.8, c.voice(low=76, high=90, n=1)[0], hum(rng, 52 - i * 10))
                piano.chord(b, 3.8, c.voice(low=57, high=76, n=3), hum(rng, 56 - i * 8))
                strings.chord(b, 3.9, c.voice(low=57, high=73, n=3), hum(rng, 32 - i * 6))
                ep2.chord(b + 1, 2.4, c.voice(low=59, high=74, n=2), hum(rng, 40 - i * 6))
                vibes.n(b, 2.0, c.voice(low=79, high=91, n=1)[0], hum(rng, 38 - i * 8))
                bells.n(b, 2.5, c.voice(low=76, high=92, n=1)[0] + 12, hum(rng, 40 - i * 8))
                bass.n(b, 3.8, c.bass_midi(2), hum(rng, 60 - i * 8))
            if i == 0:
                crash(dr, b, vel=66, note=57)
                sing(mb, b, [(bb * 2, bt, d, pp, v) for (bb, bt, d, pp, v) in
                             [(0, 0.0, 0.5, 'E5', 84), (0, 0.5, 0.5, 'E5', 82),
                              (0, 1.0, 0.75, 'D5', 84), (0, 1.75, 0.75, 'C#5', 82),
                              (0, 2.5, 0.75, 'B4', 80), (1, 0.0, 2.0, 'A4', 82)]])

    # ---- 和声段 (v2 扩到全副歌 + tag 前 8 音) ----
    if name in ('C1', 'C2'):
        xml_harm += sing(None, 0, [], tr=0) if False else []
    t0 = start + nbars * 4

# 和声收集 (段起点: C1=16, C2=40, C3=56; tr: C3=1)
xml_harm = []
vg = Trk('gather', 0, 15)
for nm, stb, tr in [('C1', 16 * 4, 0), ('C2', 40 * 4, 0), ('C3', 56 * 4, 1)]:
    h3 = [(b, bt, d, dn3(pp), max(60, v - 16)) for (b, bt, d, pp, v, *_m) in MEL_C]
    xml_harm += sing(vg, stb, h3, tr=tr)
    if nm == 'C3':
        tg = [(b, bt, d, dn3(pp), max(60, v - 16)) for (b, bt, d, pp, v, *_m) in MEL_TAG]
        xml_harm += sing(vg, stb, tg, tr=tr)

print(f'harm notes: {len(xml_harm)}')
lo = min(m for _, _, m, _ in xml_harm); hi = max(m for _, _, m, _ in xml_harm)
names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
print(f'harm range: {names[lo%12]}{lo//12-1} ~ {names[hi%12]}{hi//12-1}')
for trk in p.tracks:
    print(f'  {trk.name:14s} ch{trk.channel:2d} prog{trk.program:3d} notes={len(trk.events)}')

TOTAL = int(t0 // 4)
base = os.path.join(OUTDIR, '05_你的颜色渐变_终将成为你')
p.save(base + '_v2_complete.mid')
print('saved:', base + '_v2_complete.mid')


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


write_musicxml(base + '_v2_vocal_harm.musicxml',
               [(bt, d, m, 'ら') for bt, d, m, _ in xml_harm], BPM, TOTAL)
