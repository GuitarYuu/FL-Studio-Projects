# -*- coding: utf-8 -*-
"""01「苍鸟与莉兹」 YOASOBI 风格致敬 ×《莉兹与青鸟》
Bb 大调 134bpm 4/4 | 主题:长笛=青鸟、双簧管=莉兹,以二重对话织体写"离别与飞翔"
曲式 Intro-A1-A2-Pre-C1-ITL-A3-A4-Pre-C2-Bridge-C3(+tag,升半音)-Outro ≈ 3'00"
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260925)
BPM = 134
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_苍鸟与莉兹_YOASOBI风_complete.mid')

p = Piece('苍鸟与莉兹 (YOASOBI风格致敬)', BPM, key='Bb')
pia = p.add(Trk('Piano Main', 0, 0, vol=104, pan=60, reverb=52))
pia2 = p.add(Trk('Piano Off', 0, 1, vol=78, pan=76, reverb=52))
ep = p.add(Trk('E.Piano', 4, 2, vol=70, pan=44, reverb=44))
lead = p.add(Trk('Lead Vocal', 81, 3, vol=108, pan=64, reverb=40))
dbl = p.add(Trk('Lead Synth', 80, 4, vol=58, pan=64, reverb=36))
flt = p.add(Trk('Flute', 73, 5, vol=84, pan=40, reverb=72))
obo = p.add(Trk('Oboe', 68, 6, vol=80, pan=88, reverb=72))
bass = p.add(Trk('Finger Bass', 33, 7, vol=96, pan=64, reverb=16))
strs = p.add(Trk('Strings', 48, 8, vol=64, pan=64, reverb=78))
dr = p.add(Drums(vol=104))

A = ['Ebmaj7', 'F', 'Gm7', 'Cm7', 'Ebmaj7', 'F', 'Gm7', 'F7']
PRE = ['Cm7', 'Cm7', 'Dm7', 'F7']
C = ['Bb', 'F/A', 'Gm7', 'Ebmaj7', 'Bb/D', 'Eb/F', 'F', 'F7']
INTRO = ['Ebmaj9', 'F', 'Gm7', 'F', 'Ebmaj9', 'F', 'Gm7', 'F']
ITL = ['Ebmaj9', 'F', 'Gm7', 'F']
BRG = ['Ebmaj7', 'Ebm7', 'Bb/D', 'Cm7', 'Abmaj7', 'Bb', 'Gm7', 'Cm7',
       'Ab/Bb', 'Bb', 'F7sus4', 'F7']
TAG = ['Bb', 'F/A', 'Gm7', 'Eb/F']
OUTC = ['Ebmaj9', 'F', 'Ebmaj9', 'F', 'Ebmaj9', 'F', 'Bbadd9', 'Bbadd9']

SECS = [
    ('Intro', INTRO, 0), ('A1', A, 0), ('A2', A, 0), ('Pre', PRE, 0),
    ('C1', C, 0), ('ITL', ITL, 0),
    ('A3', A, 0), ('A4', A, 0), ('Pre', PRE, 0),
    ('C2', C, 0),
    ('Bridge', BRG, 0),
    ('C3', C + TAG, 1),
    ('Outro', OUTC, 1),
]

# ---------------- 旋律 (bar, beat, dur, pitch, vel) ----------------
MEL_A1 = [
    (0, 0, 0.5, 'G4', 84), (0, 0.5, 0.5, 'G4', 78), (0, 1, 0.5, 'Bb4', 84), (0, 1.5, 0.5, 'D5', 86), (0, 2, 2, 'C5', 88),
    (1, 0, 1.5, 'C5', 84), (1, 1.5, 0.5, 'Bb4', 80), (1, 2, 1, 'A4', 84), (1, 3, 1, 'G4', 80),
    (2, 0, 1.5, 'Bb4', 86), (2, 1.5, 0.5, 'A4', 78), (2, 2, 1.5, 'G4', 84),
    (3, 0, 0.5, 'G4', 78), (3, 0.5, 0.5, 'F4', 76), (3, 1, 0.5, 'Eb4', 80), (3, 1.5, 0.5, 'D4', 78), (3, 2, 2, 'C4', 84),
    (4, 0, 0.5, 'G4', 84), (4, 0.5, 0.5, 'Bb4', 80), (4, 1, 0.5, 'D5', 86), (4, 1.5, 0.5, 'Eb5', 88), (4, 2, 2, 'D5', 86),
    (5, 0, 1, 'D5', 84), (5, 1, 1, 'C5', 82), (5, 2, 2, 'Bb4', 86),
    (6, 0, 0.5, 'Bb4', 80), (6, 0.5, 0.5, 'A4', 78), (6, 1, 1, 'G4', 84), (6, 2, 1, 'F4', 80), (6, 3, 1, 'G4', 82),
    (7, 0, 2, 'A4', 86),
]
MEL_A2 = MEL_A1[:17] + [
    (4, 0, 0.5, 'Bb4', 84), (4, 0.5, 0.5, 'C5', 82), (4, 1, 0.5, 'D5', 86), (4, 1.5, 0.5, 'Eb5', 88), (4, 2, 2, 'Eb5', 86),
    (5, 0, 1.5, 'Eb5', 84), (5, 1.5, 0.5, 'D5', 82), (5, 2, 2, 'C5', 86),
    (6, 0, 0.5, 'C5', 80), (6, 0.5, 0.5, 'Bb4', 78), (6, 1, 0.5, 'A4', 82), (6, 1.5, 0.5, 'G4', 80), (6, 2, 2, 'Bb4', 84),
    (7, 0, 3, 'A4', 88),
]
MEL_PRE = [
    (0, 0, 1, 'G4', 82), (0, 1, 1, 'Bb4', 86), (0, 2, 2, 'C5', 88),
    (1, 0, 1.5, 'C5', 86), (1, 1.5, 0.5, 'D5', 84), (1, 2, 1, 'C5', 84), (1, 3, 1, 'Bb4', 82),
    (2, 0, 1, 'A4', 84), (2, 1, 1, 'C5', 86), (2, 2, 2, 'D5', 88),
    (3, 0, 1.5, 'Eb5', 90), (3, 1.5, 1, 'D5', 86), (3, 2.5, 1.5, 'C5', 84),
]
MEL_C = [
    (0, 0, 1.5, 'F5', 94), (0, 1.5, 0.5, 'D5', 88), (0, 2, 2, 'C5', 92),
    (1, 0, 0.5, 'A4', 84), (1, 0.5, 0.5, 'Bb4', 86), (1, 1, 1, 'C5', 88), (1, 2, 2, 'F5', 96),
    (2, 0, 1, 'F5', 90), (2, 1, 1, 'D5', 88), (2, 2, 2, 'Bb4', 90),
    (3, 0, 0.5, 'Bb4', 84), (3, 0.5, 0.5, 'C5', 86), (3, 1, 1, 'D5', 90), (3, 2, 2, 'Eb5', 92),
    (4, 0, 1.5, 'D5', 92), (4, 1.5, 0.5, 'C5', 86), (4, 2, 2, 'Bb4', 90),
    (5, 0, 0.5, 'C5', 84), (5, 0.5, 0.5, 'Bb4', 82), (5, 1, 1, 'A4', 84), (5, 2, 2, 'G4', 86),
    (6, 0, 1, 'A4', 86), (6, 1, 1, 'Bb4', 88), (6, 2, 2, 'C5', 90),
    (7, 0, 1, 'C5', 88), (7, 1, 1, 'D5', 90), (7, 2, 2, 'Eb5', 92),
]
MEL_TAG = [
    (0, 0, 2, 'D5', 92), (0, 2, 2, 'C5', 86),
    (1, 0, 1.5, 'Bb4', 90), (1, 1.5, 0.5, 'C5', 86), (1, 2, 2, 'D5', 92),
    (2, 0, 1, 'Eb5', 94), (2, 1, 1, 'D5', 90), (2, 2, 2, 'Bb4', 90),
    (3, 0, 4, 'C5', 94),
]
MEL_BRG = [
    (0, 0, 2, 'Eb5', 82), (0, 2, 1, 'D5', 78), (0, 3, 1, 'C5', 80),
    (1, 0, 2, 'Db5', 80), (1, 2, 1, 'C5', 78), (1, 3, 1, 'Bb4', 80),
    (2, 0, 3, 'Bb4', 84),
    (3, 0, 2, 'C5', 82), (3, 2, 1, 'D5', 84), (3, 3, 1, 'Eb5', 86),
    (4, 0, 2, 'Eb5', 84), (4, 2, 1, 'F5', 86), (4, 3, 1, 'Eb5', 80),
    (5, 0, 3, 'D5', 86), (5, 3, 1, 'C5', 78),
    (6, 0, 1.5, 'Bb4', 82), (6, 1.5, 0.5, 'C5', 80), (6, 2, 2, 'D5', 84),
    (7, 0, 1, 'Eb5', 84), (7, 1, 1, 'D5', 80), (7, 2, 2, 'C5', 82),
    (8, 0, 2, 'F5', 88), (8, 2, 2, 'Eb5', 84),
    (9, 0, 3, 'D5', 90), (9, 3, 1, 'D5', 80),
]
FLT_INTRO = [
    (4, 2, 0.25, 'G5', 72), (4, 2.25, 0.25, 'F5', 68), (4, 2.5, 1, 'Eb5', 76),
    (6, 2, 0.25, 'Bb5', 76), (6, 2.25, 0.25, 'A5', 70), (6, 2.5, 1.5, 'G5', 80),
]
FLT_ITL = [
    (0, 0, 1.5, 'G5', 88), (0, 1.5, 0.5, 'F5', 82), (0, 2, 1, 'Eb5', 86), (0, 3, 1, 'F5', 84),
    (1, 0, 2, 'D5', 88), (1, 2, 2, 'C5', 84),
    (2, 0, 1.5, 'F5', 88), (2, 1.5, 0.5, 'G5', 84), (2, 2, 1, 'A5', 90), (2, 3, 1, 'G5', 84),
    (3, 0, 2, 'F5', 90), (3, 2, 1, 'Eb5', 84), (3, 3, 1, 'C5', 82),
]
OBO_ITL = [
    (2, 0, 1, 'Bb4', 82), (2, 1, 1, 'C5', 84), (2, 2, 1, 'D5', 86), (2, 3, 1, 'Eb5', 84),
    (3, 0, 2, 'C5', 86), (3, 2, 2, 'A4', 84),
]
FLT_ANS = [
    (4, 2, 0.5, 'D5', 78), (4, 2.5, 0.5, 'Eb5', 80), (4, 3, 1, 'F5', 84),
    (5, 0, 1, 'G5', 82), (5, 1, 1, 'F5', 78), (5, 2, 2, 'Eb5', 80),
]
FLT_C3 = [
    (0, 2, 0.5, 'E5', 78), (0, 2.5, 0.5, 'F#5', 80), (0, 3, 1, 'G#5', 84),
    (1, 0, 1, 'B5', 86), (1, 1, 1, 'A5', 80), (1, 2, 2, 'G#5', 82),
]
FLT_OUT = [
    (4, 0, 0.5, 'G5', 80), (4, 0.5, 0.5, 'F5', 76), (4, 1, 1.5, 'Eb5', 82),
    (4, 2.5, 0.5, 'F5', 78), (4, 3, 3, 'D5', 84),
]

# ---------------- 段落装配 ----------------
t0 = 0.0
for si, (name, chords, tr) in enumerate(SECS):
    cs = [Chord(c).shifted(tr) for c in chords]
    nbars = len(cs)
    start = t0
    nxt_of = lambda i: cs[i + 1] if i + 1 < nbars else cs[0]

    if name == 'Intro':
        for i, c in enumerate(cs):
            b = start + i * 4
            piano_riff16(pia, b, c, rng, vel=82)
            if i >= 4:
                drum_bar(dr, b, 'yo_intro', rng)
            if i == 7:
                crash(dr, b)

    elif name in ('A1', 'A2', 'A3', 'A4'):
        full = name in ('A2', 'A4')
        for i, c in enumerate(cs):
            b = start + i * 4
            piano_arp8(pia, b, c, rng, vel=66 if full else 60)
            if full:
                piano_blocks(pia2, b, c, rng, hits=((1, 0.5, 58), (3, 0.5, 60)), n=3)
            if name in ('A3', 'A4'):
                ep_stabs(ep, b, c, rng, beats=((1.5, 0.5, 54), (3.5, 0.5, 56)), n=3)
            bass_8(bass, b, c, nxt_of(i), rng, vel=74, walking=full)
            drum_bar(dr, b, 'yo_verse', rng, fill=(i == 7))

    elif name == 'Pre':
        for i, c in enumerate(cs):
            b = start + i * 4
            piano_blocks(pia, b, c, rng, hits=((0, 2, 74), (2, 1, 70), (3, 1, 72)), n=4)
            bass_8(bass, b, c, nxt_of(i), rng, vel=78)
            drum_bar(dr, b, 'yo_pre' if i < 3 else 'yo_pre_snare', rng)

    elif name in ('C1', 'C2', 'C3'):
        for i, c in enumerate(cs):
            b = start + i * 4
            piano_drive16(pia, b, c, rng, vel=90)
            if name != 'C1':
                ep_stabs(ep, b, c, rng)
                pad_strings(strs, b, c, rng, vel=52 if name == 'C3' else 44)
            bass_8(bass, b, c, nxt_of(i), rng, vel=84)
            drum_bar(dr, b, 'yo_chorus', rng, fill=(i == nbars - 1))
        crash(dr, start)

    elif name == 'ITL':
        for i, c in enumerate(cs):
            b = start + i * 4
            piano_riff16(pia, b, c, rng, vel=78)
            bass_8(bass, b, c, nxt_of(i), rng, vel=76)
            drum_bar(dr, b, 'yo_verse', rng)

    elif name == 'Bridge':
        for i, c in enumerate(cs):
            b = start + i * 4
            piano_blocks(pia, b, c, rng, hits=((0, 3.5, 70),), n=4)
            ep.chord(b, 3.8, c.voice(low=56, high=74, n=4), hum(rng, 50))
            pad_strings(strs, b, c, rng, vel=min(62, 40 + i * 2))
            bass_8(bass, b, c, nxt_of(i), rng, vel=70, walking=(i >= 6))
            drum_bar(dr, b, 'yo_bridge' if i < 10 else ('yo_pre' if i == 10 else 'yo_pre_snare'), rng)
        crash(dr, start)

    elif name == 'Outro':
        for i, c in enumerate(cs):
            b = start + i * 4
            vs = max(0.55, 1.0 - i * 0.06)
            piano_riff16(pia, b, c, rng, vel=int(76 * vs))
            bass_8(bass, b, c, nxt_of(i), rng, vel=int(72 * vs), walking=False)
            if i < 7:
                drum_bar(dr, b, 'yo_verse', rng, vel_scale=vs, fill=(i == 6))
            else:
                crash(dr, b, vel=70)
                dr.d(b, 36, 80)
            if i >= 6:
                pia2.chord(b, 3.8, c.voice(low=58, high=76, n=4), hum(rng, int(60 * vs)))

    # ---- 通用声部 ----
    if name in ('A1', 'A2', 'A3', 'A4'):
        lead.phrase(start, MEL_A1 if name in ('A1', 'A3') else MEL_A2)
    elif name == 'Pre':
        lead.phrase(start, MEL_PRE)
        dbl.phrase(start + 12, [(0, 0, 0.5, 'Eb5', 66), (0, 0.5, 0.5, 'D5', 60), (0, 1, 1.5, 'C5', 62)])
    elif name == 'C1':
        lead.phrase(start, MEL_C)
    elif name == 'C2':
        lead.phrase(start, MEL_C)
        dbl.phrase(start, MEL_C)
        flt.phrase(start, FLT_ANS)
    elif name == 'C3':
        lead.phrase(start, MEL_C + sh(MEL_TAG, 8), tr=tr)
        dbl.phrase(start, MEL_C + sh(MEL_TAG, 8), tr=tr)
        flt.phrase(start + 32, FLT_C3)
    elif name == 'ITL':
        flt.phrase(start, FLT_ITL)
        obo.phrase(start, OBO_ITL)
    elif name == 'Bridge':
        lead.phrase(start, MEL_BRG)
    elif name == 'Intro':
        flt.phrase(start, FLT_INTRO)
    elif name == 'Outro':
        flt.phrase(start, FLT_OUT)
    t0 = start + nbars * 4

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s  sections={len(SECS)}')
for trk in p.tracks:
    print(f'  {trk.name:12s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
p.save(OUT)
print('saved:', os.path.abspath(OUT))
