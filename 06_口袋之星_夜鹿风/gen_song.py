# -*- coding: utf-8 -*-
"""03「口袋之星」 ヨルシカ (n-buna) 风格致敬 × 宝可梦
D 大调 92bpm 4/4 | 主题:清晨草丛出发的旅行感;钟琴=宝可梦的鸣叫与闪烁,
桥段借 bVI/bVII(Gm/Bb)=夜晚露营的篝火,最终副歌回到大调=进化与抵达
曲式 Intro-V1-Pre-C1-ITL-V2-Pre-C2-Bridge-C3-Outro ≈ 3'03"
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260927)
BPM = 92
OUT_MID = os.path.join(os.path.dirname(os.path.abspath(__file__)), '03_口袋之星_夜鹿风_complete.mid')

p = Piece('口袋之星 (ヨルシカ风格致敬)', BPM, key='D')
acg = p.add(Trk('Acoustic Gt', 25, 0, vol=100, pan=44, reverb=40))
cln = p.add(Trk('Clean Gt', 27, 1, vol=78, pan=84, reverb=44))
odg = p.add(Trk('Overdrive Gt', 29, 2, vol=64, pan=56, reverb=34))
bass = p.add(Trk('Bass', 33, 3, vol=96, pan=64, reverb=14))
glock = p.add(Trk('Glockenspiel', 9, 4, vol=80, pan=72, reverb=66))
acc = p.add(Trk('Accordion', 21, 5, vol=68, pan=48, reverb=52))
clar = p.add(Trk('Clarinet', 71, 6, vol=86, pan=64, reverb=58))
lead = p.add(Trk('Lead Vocal', 81, 7, vol=106, pan=64, reverb=46))
strs = p.add(Trk('Strings', 48, 8, vol=56, pan=64, reverb=76))
dr = p.add(Drums(vol=100))

V = ['D', 'A/C#', 'Bm7', 'G', 'D', 'A/C#', 'G', 'A']
PRE = ['Bm7', 'G', 'D', 'A']
C = ['G', 'A', 'F#m7', 'Bm7', 'G', 'A', 'D', 'D']
INTRO = ['D', 'A/C#', 'Bm7', 'G']
ITL = ['D', 'A/C#', 'Bm7', 'G']
BRG = ['Gm', 'Bb', 'F', 'C', 'Gm', 'Bb', 'Asus4', 'A7']
OUT = ['D', 'A/C#', 'Bm7', 'G', 'Dadd9', 'Dadd9']

SECS = [
    ('Intro', INTRO), ('V1', V), ('Pre', PRE), ('C1', C),
    ('ITL', ITL), ('V2', V), ('Pre', PRE), ('C2', C),
    ('Bridge', BRG), ('C3', C), ('Outro', OUT),
]

MEL_V = [
    (0, 0, 1.5, 'A4', 88), (0, 1.5, 0.5, 'F#4', 80), (0, 2, 1, 'G4', 84), (0, 3, 1, 'A4', 86),
    (1, 0, 1.5, 'C#5', 90), (1, 1.5, 0.5, 'B4', 82), (1, 2, 2, 'A4', 88),
    (2, 0, 1, 'B4', 88), (2, 1, 1, 'A4', 84), (2, 2, 2, 'F#4', 86),
    (3, 0, 1, 'G4', 84), (3, 1, 1, 'A4', 86), (3, 2, 2, 'B4', 88),
    (4, 0, 1.5, 'A4', 88), (4, 1.5, 0.5, 'F#4', 80), (4, 2, 1, 'G4', 84), (4, 3, 1, 'A4', 86),
    (5, 0, 1, 'B4', 88), (5, 1, 1, 'C#5', 90), (5, 2, 2, 'D5', 92),
    (6, 0, 2, 'D5', 92), (6, 2, 1, 'C#5', 86), (6, 3, 1, 'B4', 84),
    (7, 0, 3.5, 'A4', 92),
]
MEL_PRE = [
    (0, 0, 1, 'F#4', 84), (0, 1, 1, 'A4', 86), (0, 2, 2, 'B4', 90),
    (1, 0, 1, 'B4', 88), (1, 1, 1, 'D5', 92), (1, 2, 2, 'B4', 88),
    (2, 0, 1, 'D5', 90), (2, 1, 1, 'C#5', 86), (2, 2, 2, 'B4', 88),
    (3, 0, 2, 'C#5', 92), (3, 2, 2, 'E5', 96),
]
MEL_C = [
    (0, 0, 2, 'B4', 92), (0, 2, 1, 'D5', 94), (0, 3, 1, 'B4', 86),
    (1, 0, 1.5, 'A4', 92), (1, 1.5, 0.5, 'B4', 86), (1, 2, 2, 'C#5', 94),
    (2, 0, 1, 'C#5', 92), (2, 1, 1, 'B4', 88), (2, 2, 2, 'A4', 90),
    (3, 0, 1, 'F#4', 86), (3, 1, 1, 'A4', 88), (3, 2, 2, 'B4', 90),
    (4, 0, 2, 'D5', 96), (4, 2, 1, 'B4', 88), (4, 3, 1, 'G4', 86),
    (5, 0, 1, 'A4', 90), (5, 1, 1, 'B4', 90), (5, 2, 2, 'C#5', 94),
    (6, 0, 3, 'D5', 98), (6, 3, 1, 'A4', 84),
    (7, 0, 2, 'A4', 90),
]
MEL_C2_TAIL = [
    (7, 0, 3.5, 'E5', 94),
]
MEL_BRG = [
    (0, 0, 2, 'D5', 88), (0, 2, 1, 'C5', 84), (0, 3, 1, 'Bb4', 86),
    (1, 0, 2, 'F5', 92), (1, 2, 2, 'D5', 88),
    (2, 0, 1, 'C5', 88), (2, 1, 1, 'D5', 90), (2, 2, 2, 'F5', 92),
    (3, 0, 1, 'E5', 90), (3, 1, 1, 'G5', 92), (3, 2, 2, 'E5', 88),
    (4, 0, 2, 'D5', 90), (4, 2, 1, 'C5', 84), (4, 3, 1, 'Bb4', 86),
    (5, 0, 2, 'F5', 92), (5, 2, 2, 'G5', 90),
    (6, 0, 2, 'A5', 96), (6, 2, 2, 'G5', 90),
    (7, 0, 2, 'C#5', 92), (7, 2, 2, 'E5', 94),
]
GLOCK_INTRO = [
    (0, 0, 0.5, 'A5', 88), (0, 0.5, 0.5, 'B5', 80), (0, 1, 1, 'D6', 92), (0, 2, 0.5, 'A5', 82), (0, 2.5, 0.5, 'F#5', 78), (0, 3, 1, 'A5', 86),
    (1, 0, 0.5, 'C#6', 84), (1, 0.5, 0.5, 'B5', 78), (1, 1, 1, 'A5', 88), (1, 2, 0.5, 'E5', 76), (1, 2.5, 0.5, 'F#5', 78), (1, 3, 1, 'A5', 84),
    (2, 0, 0.5, 'B5', 84), (2, 0.5, 0.5, 'D6', 86), (2, 1, 1, 'F#5', 88), (2, 2, 0.5, 'B5', 80), (2, 2.5, 0.5, 'A5', 78), (2, 3, 1, 'F#5', 84),
    (3, 0, 0.5, 'G5', 82), (3, 0.5, 0.5, 'A5', 84), (3, 1, 1, 'B5', 88), (3, 2, 0.5, 'D6', 84), (3, 2.5, 0.5, 'B5', 80), (3, 3, 1, 'G5', 82),
]
GLOCK_C3 = ['B5', 'C#6', 'A5', 'F#5', 'B5', 'C#6', 'D6', 'D6']
GLOCK_OUT_TAIL = [
    (0, 0, 0.25, 'E5', 84), (0, 0.25, 0.25, 'F#5', 80),
    (0, 0.5, 0.25, 'E5', 82), (0, 0.75, 0.25, 'F#5', 78),
    (0, 1, 0.25, 'E5', 80), (0, 1.25, 0.25, 'F#5', 76),
    (0, 1.5, 3.5, 'D6', 92),
]

t0 = 0.0
for si, (name, chords_raw) in enumerate(SECS):
    cs = [Chord(c) for c in chords_raw]
    nbars = len(cs)
    start = t0
    nxt_of = lambda i: cs[i + 1] if i + 1 < nbars else cs[0]
    intro_like = name in ('Intro', 'ITL', 'Outro')
    chorus = name in ('C1', 'C2', 'C3')

    for i, c in enumerate(cs):
        b = start + i * 4
        if intro_like:
            ac_pick8(acg, b, c, rng, vel=66 if name != 'Outro' else 62)
            if not (name == 'Outro' and i >= 4):
                bass_folk(bass, b, c, rng, vel=64)
            if name == 'Outro' and i >= 4:
                bass_folk(bass, b, c, rng, vel=54)
                acc.chord(b, 3.8, c.voice(low=55, high=72, n=4), hum(rng, 40))
                odg.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 42))
        elif name in ('V1', 'V2'):
            ac_pick8(acg, b, c, rng, vel=70)
            bass_folk(bass, b, c, rng, vel=70)
            if name == 'V2':
                drum_bar(dr, b, 'y_verse', rng, fill=(i == 7))
            else:
                drum_bar(dr, b, 'y_verse', rng, fill=(i == 7), vel_scale=0.85)
        elif name == 'Pre':
            ac_pick8(acg, b, c, rng, vel=74)
            bass_folk(bass, b, c, rng, vel=74)
            if i == 3:
                strs.chord(b, 3.9, c.voice(low=50, high=70, n=4), hum(rng, 46))
            drum_bar(dr, b, 'y_pre', rng)
        elif chorus:
            ac_pick8(acg, b, c, rng, vel=76)
            odg.chord(b, 3.7, c.voice(low=55, high=72, n=4), hum(rng, 54 if name == 'C3' else 48))
            cln_ch = c.voice(low=64, high=84, n=4)
            for k in range(4):
                cln.n(b + 0.5 + k, 0.48, cln_ch[k % len(cln_ch)], hum(rng, 56))
            bass_folk(bass, b, c, rng, vel=80)
            if name != 'C1':
                pad_strings(strs, b, c, rng, vel=36)
            if name == 'C3':
                glock.n(b + 1, 2, npitch(GLOCK_C3[i]), 68)
            drum_bar(dr, b, 'y_chorus', rng, fill=(i == 7))
            if i == 0:
                crash(dr, b, vel=84)
        elif name == 'Bridge':
            ac_pick8(acg, b, c, rng, vel=64)
            acc.chord(b, 3.8, c.voice(low=55, high=72, n=4), hum(rng, 52))
            bass_folk(bass, b, c, rng, vel=66)
            drum_bar(dr, b, 'y_pre' if i == 7 else 'y_bridge', rng)

    # ---- 主旋律 ----
    if name == 'Intro':
        glock.phrase(start, GLOCK_INTRO)
    elif name == 'V1':
        lead.phrase(start, MEL_V)
    elif name == 'V2':
        lead.phrase(start, MEL_V)
    elif name in ('Pre',):
        lead.phrase(start, MEL_PRE)
    elif name == 'C1':
        lead.phrase(start, MEL_C)
    elif name == 'C2':
        lead.phrase(start, MEL_C[:len(MEL_C) - 1] + MEL_C2_TAIL)
    elif name == 'C3':
        lead.phrase(start, [(b, bt, d, p, min(127, v + 4)) for (b, bt, d, p, v) in MEL_C])
        lead.phrase(start + 28, [(0, 3, 1, 'F#5', 90)])
    elif name == 'Bridge':
        clar.phrase(start, MEL_BRG)
    elif name == 'ITL':
        glock.phrase(start, GLOCK_INTRO[:12])
        acc.phrase(start, [(0, 0, 2, 'D4', 70), (0, 2, 2, 'E4', 66),
                           (1, 0, 2, 'C#4', 70), (1, 2, 2, 'E4', 66)])
    elif name == 'Outro':
        glock.phrase(start, GLOCK_INTRO)
        glock.phrase(start + 16, GLOCK_OUT_TAIL)
    t0 = start + nbars * 4

# C3 结尾: crash 收束
crash(dr, t0 - 8, vel=88)

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s  sections={len(SECS)}')
for trk in p.tracks:
    print(f'  {trk.name:12s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
p.save(OUT_MID)
print('saved:', os.path.abspath(OUT_MID))
