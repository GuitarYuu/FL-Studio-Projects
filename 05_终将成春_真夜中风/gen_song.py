# -*- coding: utf-8 -*-
"""02「终将成春」 ずっと真夜中でいいのに。(ZUTOMAYO) 风格致敬 ×《终将成为你》
F# 小调 142bpm 4/4 | 主题:不齐的心动=16分切分,副歌转关系大调A=「和你一起的春天」,
末段整体升全音=重迭的心意
曲式 Intro(riff)-V1-Pre-C1-ITL(riff)-V2-Pre-C2-Break-C3(+tag,升全音)-Outro(急停)≈ 3'03"
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260926)
BPM = 142
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '02_终将成春_真夜中风_complete.mid')

p = Piece('终将成春 (ずとまよ风格致敬)', BPM, key='F#m')
rgt = p.add(Trk('Riff Guitar', 29, 0, vol=96, pan=36, reverb=26))
bass = p.add(Trk('Slap Bass', 33, 1, vol=104, pan=64, reverb=12))
ep = p.add(Trk('E.Piano', 4, 2, vol=88, pan=44, reverb=46))
mgt = p.add(Trk('Mute Guitar', 27, 3, vol=76, pan=84, reverb=30))
lead = p.add(Trk('Lead Vocal', 80, 4, vol=110, pan=64, reverb=34))
sq = p.add(Trk('Synth Stab', 81, 5, vol=56, pan=76, reverb=30))
pad = p.add(Trk('Warm Pad', 89, 6, vol=52, pan=64, reverb=64))
dr = p.add(Drums(vol=106))

V8 = ['F#m7', 'F#m7', 'Dmaj7', 'Dmaj7', 'Bm7', 'Bm7', 'C#7sus4', 'C#7']
V16 = V8 + V8
PRE = ['Bm7', 'Bm7', 'C#7', 'C#7', 'Dmaj7', 'Dmaj7', 'Eadd9', 'E']
C = ['A', 'E/G#', 'F#m7', 'Dmaj7', 'A/C#', 'D', 'E', 'E7']
ITL = ['F#m7', 'Dmaj7', 'Bm7', 'C#7']
INTRO = ['F#m7', 'F#m7', 'Dmaj7', 'Dmaj7', 'F#m7', 'F#m7', 'Bm7', 'C#7']
BRK = ['F#m9', 'F#m9', 'Dmaj7', 'Dmaj7', 'Bm7', 'Bm7', 'C#7#9', 'C#7#9',
       'F#m9', 'F#m9', 'Dmaj7', 'Dmaj7', 'Bm7', 'C#7#9', 'F#m7', 'F#m7']
TAG = ['A', 'E/G#', 'F#m7', 'Dadd9']

SECS = [
    ('Intro', INTRO, 0), ('V1', V16, 0), ('Pre', PRE, 0), ('C1', C, 0),
    ('ITL', ITL, 0),
    ('V2', V16, 0), ('Pre', PRE, 0), ('C2', C, 0),
    ('Break', BRK, 0),
    ('C3', C + TAG, 2),
    ('Outro', ['G#m7', 'G#m7', 'G#m7', 'G#m7'], 2),
]

# riff (2 小节循环, F# 根; 移调时按根整体平移)
RIFF = [
    (0, 0.0, 0.4, 'F#2', 104), (0, 0.5, 0.2, 'A2', 88), (0, 0.75, 0.2, 'B2', 90),
    (0, 1.0, 0.4, 'C#3', 100), (0, 1.25, 0.2, 'B2', 80), (0, 1.5, 0.2, 'A2', 84),
    (0, 1.75, 0.2, 'F#2', 86), (0, 2.0, 0.4, 'F#2', 98), (0, 2.5, 0.2, 'C#3', 88),
    (0, 2.75, 0.2, 'A2', 82), (0, 3.0, 0.2, 'B2', 86), (0, 3.25, 0.2, 'A2', 78),
    (0, 3.5, 0.2, 'F#2', 88), (0, 3.75, 0.2, 'E2', 84),
    (1, 0.0, 0.4, 'D2', 102), (1, 0.5, 0.2, 'F#2', 88), (1, 0.75, 0.2, 'A2', 90),
    (1, 1.0, 0.4, 'B2', 98), (1, 1.25, 0.2, 'A2', 80), (1, 1.5, 0.2, 'F#2', 84),
    (1, 1.75, 0.2, 'D2', 84), (1, 2.0, 0.4, 'E2', 96), (1, 2.5, 0.2, 'F#2', 88),
    (1, 2.75, 0.2, 'E2', 80), (1, 3.0, 0.2, 'B2', 84), (1, 3.5, 0.3, 'C#3', 92),
    (1, 3.75, 0.2, 'D3', 88),
]

MEL_V_P1 = [
    (0, 3.5, 0.25, 'C#5', 88), (0, 3.75, 0.25, 'C#5', 84),
    (1, 0, 0.5, 'C#5', 92), (1, 0.5, 0.25, 'F#5', 90), (1, 0.75, 0.25, 'E5', 84),
    (1, 1, 0.5, 'C#5', 88), (1, 1.5, 0.25, 'B4', 82), (1, 1.75, 0.25, 'C#5', 84), (1, 2, 1.5, 'A4', 88),
    (2, 0, 0.5, 'A4', 84), (2, 0.5, 0.5, 'B4', 86), (2, 1, 1, 'D5', 90),
    (2, 2, 0.5, 'C#5', 84), (2, 2.5, 0.5, 'B4', 82), (2, 3, 1, 'A4', 86),
    (3, 0, 2, 'F#4', 88), (3, 2, 0.5, 'E4', 80), (3, 2.5, 0.5, 'F#4', 84), (3, 3, 1, 'A4', 86),
]
MEL_V_P2 = [
    (0, 0, 0.5, 'B4', 86), (0, 0.5, 0.5, 'C#5', 88), (0, 1, 1.5, 'D5', 92),
    (0, 2.5, 0.5, 'C#5', 84), (0, 3, 0.5, 'B4', 82), (0, 3.5, 0.5, 'A4', 80),
    (1, 0, 0.5, 'B4', 84), (1, 0.5, 0.5, 'A4', 80), (1, 1, 1, 'F#4', 86),
    (1, 2, 0.5, 'A4', 82), (1, 2.5, 0.5, 'B4', 84), (1, 3, 1, 'C#5', 88),
    (2, 0, 1, 'B4', 88), (2, 1, 0.5, 'C#5', 86), (2, 1.5, 0.5, 'E5', 90), (2, 2, 2, 'E5', 88),
    (3, 0, 0.5, 'D#5', 88), (3, 0.5, 0.5, 'E#5', 90), (3, 1, 3, 'F#5', 94),
]
MEL_V_P1V = MEL_V_P1[:15] + [
    (3, 0, 2, 'F#4', 88), (3, 2, 0.5, 'A4', 84), (3, 2.5, 0.5, 'B4', 86), (3, 3, 1, 'C#5', 88),
]
MEL_V_P2V = MEL_V_P2
MEL_PRE = [
    (0, 0, 1, 'F#4', 84), (0, 1, 1, 'B4', 88), (0, 2, 1, 'C#5', 90),
    (0, 3, 0.5, 'D5', 86), (0, 3.5, 0.5, 'C#5', 82),
    (1, 0, 1.5, 'B4', 88), (1, 1.5, 0.5, 'C#5', 84), (1, 2, 2, 'D5', 90),
    (2, 0, 1, 'C#5', 88), (2, 1, 0.5, 'D#5', 86), (2, 1.5, 0.5, 'E5', 88),
    (2, 2, 1, 'D#5', 86), (2, 3, 0.5, 'C#5', 84), (2, 3.5, 0.5, 'B4', 82),
    (3, 0, 2, 'C#5', 90), (3, 2, 2, 'B4', 84),
    (4, 0, 1, 'D5', 88), (4, 1, 0.5, 'C#5', 84), (4, 1.5, 0.5, 'B4', 82), (4, 2, 2, 'F#5', 94),
    (5, 0, 1.5, 'F#5', 90), (5, 1.5, 0.5, 'E5', 84), (5, 2, 2, 'D5', 88),
    (6, 0, 0.5, 'E5', 88), (6, 0.5, 0.5, 'D#5', 84), (6, 1, 1, 'E5', 88),
    (6, 2, 1, 'G#4', 82), (6, 3, 1, 'B4', 84),
    (7, 0, 0.5, 'B4', 86), (7, 0.25, 0.25, 'C#5', 88), (7, 0.5, 0.25, 'D#5', 90),
    (7, 0.75, 0.25, 'E5', 92), (7, 1, 2, 'E5', 94), (7, 3, 1, 'G#4', 80),
]
MEL_C = [
    (0, 0, 0.75, 'C#5', 92), (0, 0.75, 0.25, 'B4', 86), (0, 1, 1, 'A4', 90),
    (0, 2, 1, 'B4', 88), (0, 3, 1, 'C#5', 90),
    (1, 0, 0.5, 'B4', 86), (1, 0.5, 0.5, 'G#4', 84), (1, 1, 1, 'G#4', 86),
    (1, 2, 1, 'B4', 88), (1, 3, 0.5, 'C#5', 90), (1, 3.5, 0.5, 'B4', 84),
    (2, 0, 1, 'C#5', 92), (2, 1, 0.5, 'B4', 86), (2, 1.5, 0.5, 'A4', 84), (2, 2, 2, 'F#4', 88),
    (3, 0, 1.5, 'F#5', 98), (3, 1.5, 0.5, 'E5', 90), (3, 2, 2, 'D5', 94),
    (4, 0, 1, 'C#5', 90), (4, 1, 0.5, 'D5', 88), (4, 1.5, 0.5, 'C#5', 86),
    (4, 2, 1, 'B4', 88), (4, 3, 1, 'A4', 86),
    (5, 0, 1.5, 'D5', 94), (5, 1.5, 0.5, 'E5', 90), (5, 2, 2, 'F#5', 96),
    (6, 0, 0.5, 'G#4', 84), (6, 0.5, 0.5, 'B4', 86), (6, 1, 1, 'D5', 92), (6, 2, 2, 'E5', 94),
    (7, 0, 1, 'E5', 92), (7, 1, 0.5, 'D5', 88), (7, 1.5, 0.5, 'C#5', 86),
    (7, 2, 1, 'B4', 88), (7, 3, 1, 'G#4', 84),
]
MEL_TAG = [
    (0, 0, 2, 'E5', 92), (0, 2, 2, 'C#5', 88),
    (1, 0, 4, 'B4', 90),
    (2, 0, 2, 'F#5', 96), (2, 2, 2, 'E5', 90),
    (3, 0, 4, 'F#5', 94),
]
MEL_BRK = [
    (0, 0, 3, 'C#5', 86), (0, 3, 1, 'B4', 80),
    (1, 0, 4, 'A4', 84),
    (2, 0, 2, 'F#5', 90), (2, 2, 1, 'E5', 84), (2, 3, 1, 'C#5', 84),
    (3, 0, 3, 'B4', 86), (3, 3, 0.5, 'A4', 80), (3, 3.5, 0.5, 'B4', 82),
    (4, 0, 2, 'C#5', 88), (4, 2, 2, 'E5', 90),
    (5, 0, 3, 'D5', 88), (5, 3, 1, 'C#5', 82),
    (6, 0, 2, 'B4', 86), (6, 2, 2, 'D#5', 90),
    (7, 0, 4, 'E#5', 92),
    (8, 0, 3, 'C#5', 84), (8, 3, 1, 'B4', 80),
    (9, 0, 4, 'A4', 82),
    (10, 0, 2, 'F#5', 90), (10, 2, 2, 'E5', 86),
    (11, 0, 4, 'D5', 88),
    (12, 0, 2, 'C#5', 86), (12, 2, 1, 'B4', 84), (12, 3, 1, 'C#5', 86),
    (13, 0, 1, 'D#5', 88), (13, 1, 1, 'E#5', 90), (13, 2, 2, 'F#5', 94),
    (14, 0, 0.5, 'A4', 84), (14, 0.5, 0.5, 'B4', 86), (14, 1, 0.5, 'C#5', 88),
    (14, 1.5, 0.5, 'D5', 90), (14, 2, 0.5, 'D#5', 92), (14, 2.5, 0.5, 'E5', 94),
    (14, 3, 0.5, 'E#5', 96), (14, 3.5, 0.5, 'F#5', 98),
    (15, 0, 2, 'F#5', 100), (15, 2, 0.5, 'G#5', 96), (15, 2.5, 0.5, 'F#5', 90), (15, 3, 1, 'E#5', 88),
]

# riff 平移量 -> 音名整体移调
def shift_riff(events, st):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    out = []
    for b, bt, d, nm, v in events:
        m = npitch(nm) + st
        pc, oc = m % 12, m // 12 - 1
        out.append((b, bt, d, names[pc] + str(oc), v))
    return out

# ---------------- 段落装配 ----------------
t0 = 0.0
for si, (name, chords, tr) in enumerate(SECS):
    cs = [Chord(c).shifted(tr) for c in chords]
    nbars = len(cs)
    start = t0
    nxt_of = lambda i: cs[i + 1] if i + 1 < nbars else cs[0]
    riffed = name in ('Intro', 'ITL', 'Outro')

    for i, c in enumerate(cs):
        b = start + i * 4
        if riffed:
            if name == 'Outro' and i == 3:
                # 急停收束: 全乐队一记 G#m 和弦 + 镲, 然后静默
                stab = c.voice(low=55, high=78, n=4)
                bass.n(b, 1.8, c.bass_midi(2), 108)
                rgt.chord(b, 1.5, [p2 + 12 for p2 in c.voice(low=55, high=68, n=3)], 92)
                ep.chord(b, 1.5, stab, 84)
                dr.hits(b, [(0, 36, 112), (0, 38, 104), (0, 49, 100), (0, 57, 92)])
                continue
            evs = shift_riff(RIFF[0:14] if i % 2 == 0 else RIFF[14:27], tr)
            if i % 2 == 0:
                bass.bend(b, -180)
            for _rb, bt, rd, rn, rv in evs:
                bass.n(b + bt, rd, npitch(rn), hum(rng, rv))
                rgt.n(b + bt, rd, npitch(rn) + 12, hum(rng, rv - 6, 3))
                if bt in (0.0, 2.0):
                    ep.chord(b + bt, 0.5, c.voice(low=58, high=76, n=3), hum(rng, 66))
            if name != 'Intro' or i >= 4:
                drum_bar(dr, b, 'z_verse', rng)
        else:
            if name in ('V1', 'V2'):
                ep_stabs(ep, b, c, rng, beats=((1.5, 0.75, 56), (3.5, 0.5, 54)), n=3)
                gt_skank16(mgt, b, c, rng, vel_hi=62)
                bass_funk16(bass, b, c, nxt_of(i), rng, vel=88)
                pad.chord(b, 3.8, c.voice(low=52, high=68, n=3), hum(rng, 34))
                drum_bar(dr, b, 'z_verse', rng, fill=(i == nbars - 1))
            elif name == 'Pre':
                ep_stabs(ep, b, c, rng, beats=((0, 0.75, 60), (2, 0.75, 58), (2.75, 0.5, 56)), n=4)
                gt_skank16(mgt, b, c, rng, vel_hi=66)
                bass_funk16(bass, b, c, nxt_of(i), rng, vel=90)
                drum_bar(dr, b, 'z_pre' if i < 7 else 'z_build', rng)
            elif name in ('C1', 'C2', 'C3'):
                ep_stabs(ep, b, c, rng)
                gt_doublestop8(mgt, b, c, rng, vel=72)
                sq.chord(b + 0.5, 0.3, c.voice(low=63, high=80, n=3), hum(rng, 40))
                bass_funk16(bass, b, c, nxt_of(i), rng, vel=94)
                pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 38))
                drum_bar(dr, b, 'z_chorus', rng, fill=(i == nbars - 1))
                if i == 0:
                    crash(dr, b, vel=96 if name != 'C3' else 88)
            elif name == 'Break':
                if i < 12:
                    ep.chord(b, 3.6, c.voice(low=56, high=76, n=4), hum(rng, 46))
                    bass_folk(bass, b, c, rng, vel=64)
                    drum_bar(dr, b, 'z_break', rng)
                elif i < 14:
                    gt_skank16(mgt, b, c, rng, vel_hi=58)
                    bass_funk16(bass, b, c, nxt_of(i), rng, vel=86)
                    drum_bar(dr, b, 'z_verse', rng)
                else:
                    drum_bar(dr, b, 'z_build', rng)

    if name == 'C3':
        crash(dr, start, vel=100, note=57)
    # ---- 主旋律 ----
    if name == 'V1':
        lead.phrase(start, MEL_V_P1 + sh(MEL_V_P2, 4) + sh(MEL_V_P1V, 8) + sh(MEL_V_P2V, 12))
    elif name == 'V2':
        lead.phrase(start, MEL_V_P1 + sh(MEL_V_P2, 4) + sh(MEL_V_P1V, 8) + sh(MEL_V_P2V, 12))
    elif name == 'Pre':
        lead.phrase(start, MEL_PRE)
    elif name in ('C1', 'C2'):
        lead.phrase(start, MEL_C)
        if name == 'C2':
            lead.phrase(start + 28, [(0, 0, 0.5, 'G#5', 90), (0, 0.5, 0.5, 'A5', 88), (0, 1, 1.5, 'B5', 92)])
    elif name == 'C3':
        lead.phrase(start, MEL_C + sh(MEL_TAG, 8), tr=tr)
    elif name == 'Break':
        lead.phrase(start, MEL_BRK)
    t0 = start + nbars * 4

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s  sections={len(SECS)}')
for trk in p.tracks:
    print(f'  {trk.name:12s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
p.save(OUT)
print('saved:', os.path.abspath(OUT))
