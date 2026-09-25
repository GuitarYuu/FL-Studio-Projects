# -*- coding: utf-8 -*-
"""04「电气花火」 YOASOBI「BiriBiri」风格致敬 × 宝可梦
A 大调 150bpm 4/4 | 抓耳洗脑 2 小节循环钩子 + 四踩/16分律动 + 逐段加层的层次感编曲
无人声: Lead Vocal 轨即"虚拟歌姬位", 另导出 vocal_lead.mid 供 OpenUTAU/SynthV 填词
层次设计: Intro(垫+铃片花) -> A(贝斯鼓EP四层) -> Pre(加琶音+滚奏) -> B drop(七层全开)
         -> A2(+闷音吉他+琶音常驻) -> B2(+钟琴高八度对钩子) -> Break(减到三层) -> 升全音终副歌
曲式 Intro8-A16-Pre4-B8-Post4-A16-Pre4-B8-Riff4-Break12-B3(+1)8-B3'(+1)8-Outro(+1)8 ≈ 3'00"
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260928)
BPM = 150
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '04_电气花火_BiriBiri风_complete.mid')
OUT_VOCAL = os.path.join(HERE, 'vocal_lead.mid')

p = Piece('电气花火 (BiriBiri风格致敬)', BPM, key='A')
lead = p.add(Trk('Lead Vocal', 81, 3, vol=112, pan=64, reverb=40))
dbl = p.add(Trk('Lead Double', 80, 4, vol=62, pan=64, reverb=32))
glock = p.add(Trk('Glockenspiel', 9, 5, vol=78, pan=78, reverb=60))
pia = p.add(Trk('Piano Drive', 0, 0, vol=96, pan=56, reverb=44))
ep = p.add(Trk('E.Piano', 4, 2, vol=84, pan=44, reverb=42))
arp = p.add(Trk('Arp Synth', 81, 6, vol=60, pan=84, reverb=36))
rgt = p.add(Trk('Riff Guitar', 29, 1, vol=90, pan=40, reverb=26))
bass = p.add(Trk('Slap Bass', 33, 7, vol=104, pan=64, reverb=12))
pad = p.add(Trk('Warm Pad', 89, 8, vol=56, pan=64, reverb=66))
dr = p.add(Drums(vol=106))

A16 = ['F#m7', 'Dmaj7', 'A', 'E'] * 4
PRE = ['Dmaj7', 'E', 'F#m7', 'E']
B8 = ['A', 'E', 'F#m7', 'D'] * 2
BRK = ['F#m7', 'E', 'Dmaj7', 'C#m7'] * 3
INTRO = ['A', 'A', 'F#m7', 'D'] * 2

SECS = [
    ('Intro', INTRO, 0), ('A1', A16, 0), ('Pre', PRE, 0), ('B1', B8, 0),
    ('Post', ['A', 'A', 'F#m7', 'D'], 0),
    ('A2', A16, 0), ('Pre', PRE, 0), ('B2', B8, 0),
    ('Riff', ['A', 'A', 'F#m7', 'D'], 0),
    ('Break', BRK, 0),
    ('B3', B8, 1), ('B3x', B8, 1),
    ('Outro', B8, 1),
]

MEL_A = [
    (0, 0, 0.5, 'C#5', 88), (0, 0.5, 0.5, 'C#5', 82), (0, 1, 0.5, 'B4', 86), (0, 1.5, 0.5, 'A4', 84), (0, 2, 2, 'F#4', 86),
    (1, 0, 0.5, 'A4', 84), (1, 0.5, 0.5, 'B4', 86), (1, 1, 1, 'C#5', 88), (1, 2, 0.5, 'D5', 90), (1, 2.5, 0.5, 'C#5', 86), (1, 3, 1, 'B4', 88),
    (2, 0, 0.5, 'B4', 86), (2, 0.5, 0.5, 'C#5', 88), (2, 1, 1, 'E5', 92), (2, 2, 1.5, 'E5', 90), (2, 3.5, 0.5, 'D5', 84),
    (3, 0, 0.5, 'C#5', 88), (3, 0.5, 0.5, 'B4', 84), (3, 1, 2, 'A4', 90), (3, 3, 1, 'G#4', 82),
    (4, 0, 0.5, 'C#5', 88), (4, 0.5, 0.5, 'C#5', 82), (4, 1, 0.5, 'B4', 86), (4, 1.5, 0.5, 'A4', 84), (4, 2, 2, 'F#4', 86),
    (5, 0, 0.5, 'A4', 84), (5, 0.5, 0.5, 'B4', 86), (5, 1, 1, 'C#5', 88), (5, 2, 0.5, 'D5', 90), (5, 2.5, 0.5, 'C#5', 86), (5, 3, 1, 'B4', 88),
    (6, 0, 0.5, 'D5', 90), (6, 0.5, 0.5, 'C#5', 88), (6, 1, 1, 'E5', 92), (6, 2, 2, 'F#5', 96),
    (7, 0, 0.5, 'E5', 92), (7, 0.5, 0.5, 'D5', 88), (7, 1, 0.5, 'C#5', 90), (7, 1.5, 0.5, 'B4', 86), (7, 2, 2, 'C#5', 92),
]
MEL_A2 = MEL_A[:33] + [
    (6, 0, 2, 'F#5', 96), (6, 2, 1, 'E5', 90), (6, 3, 1, 'D5', 86),
    (7, 0, 0.5, 'E5', 92), (7, 0.5, 0.5, 'D5', 88), (7, 1, 2, 'C#5', 92),
]
MEL_PRE = [
    (0, 0, 1, 'A4', 88), (0, 1, 1, 'B4', 90), (0, 2, 2, 'D5', 94),
    (1, 0, 1, 'D5', 92), (1, 1, 1, 'E5', 94), (1, 2, 2, 'E5', 94),
    (2, 0, 0.5, 'E5', 94), (2, 0.5, 0.5, 'F#5', 96), (2, 1, 2.5, 'F#5', 98),
    (3, 0, 1.5, 'E5', 96), (3, 1.5, 0.5, 'D5', 92), (3, 2, 0.5, 'C#5', 92),
    (3, 2.5, 0.5, 'B4', 92), (3, 3, 0.5, 'A4', 92), (3, 3.5, 0.5, 'B4', 94),
]
MEL_B = [
    (0, 0, 0.5, 'E5', 98), (0, 0.5, 0.5, 'E5', 92), (0, 1, 0.5, 'D5', 96), (0, 1.5, 0.5, 'C#5', 94), (0, 2, 1.5, 'B4', 96),
    (1, 0, 0.5, 'C#5', 94), (1, 0.5, 0.5, 'C#5', 88), (1, 1, 0.5, 'B4', 92), (1, 1.5, 0.5, 'A4', 90), (1, 2, 2, 'B4', 94),
    (2, 0, 0.5, 'E5', 98), (2, 0.5, 0.5, 'E5', 92), (2, 1, 0.5, 'D5', 96), (2, 1.5, 0.5, 'C#5', 94), (2, 2, 1.5, 'B4', 96),
    (3, 0, 0.5, 'A4', 92), (3, 0.5, 0.5, 'B4', 94), (3, 1, 0.5, 'C#5', 96), (3, 1.5, 0.5, 'A4', 92), (3, 2, 2, 'E5', 98),
    (4, 0, 0.5, 'E5', 98), (4, 0.5, 0.5, 'E5', 92), (4, 1, 0.5, 'D5', 96), (4, 1.5, 0.5, 'C#5', 94), (4, 2, 1.5, 'B4', 96),
    (5, 0, 0.5, 'C#5', 94), (5, 0.5, 0.5, 'C#5', 88), (5, 1, 0.5, 'B4', 92), (5, 1.5, 0.5, 'A4', 90), (5, 2, 2, 'B4', 94),
    (6, 0, 0.5, 'E5', 98), (6, 0.5, 0.5, 'E5', 92), (6, 1, 0.5, 'F#5', 100), (6, 1.5, 0.5, 'E5', 96), (6, 2, 1.5, 'D5', 96),
    (7, 0, 0.5, 'C#5', 94), (7, 0.5, 0.5, 'B4', 92), (7, 1, 0.5, 'A4', 94), (7, 1.5, 0.5, 'B4', 94), (7, 2, 2, 'C#5', 98),
]
MEL_B_END = (7, 0, 0.5, 'E5', 98), (7, 0.5, 0.5, 'F#5', 100), (7, 1, 0.5, 'G#5', 102), \
            (7, 1.5, 0.5, 'A5', 104), (7, 2, 2.5, 'A5', 104)
MEL_BRK = [
    (0, 0, 3.5, 'F#5', 92), (1, 0, 3.5, 'E5', 90), (2, 0, 3.5, 'D5', 90),
    (3, 0, 1.5, 'C#5', 90), (3, 1.5, 0.5, 'B4', 86), (3, 2, 2, 'C#5', 90),
    (4, 0, 3.5, 'F#5', 92), (5, 0, 3.5, 'E5', 90), (6, 0, 3.5, 'D5', 90),
    (7, 0, 1.5, 'C#5', 90), (7, 1.5, 0.5, 'D5', 88), (7, 2, 2, 'E5', 92),
    (8, 0, 3.5, 'F#5', 94), (9, 0, 2, 'E5', 92), (9, 2, 0.5, 'E5', 88),
    (9, 2.5, 0.5, 'F#5', 92), (9, 3, 1, 'G#5', 96),
    (10, 0, 2, 'A5', 100), (10, 2, 0.5, 'G#5', 92), (10, 2.5, 0.5, 'F#5', 90),
    (10, 3, 0.5, 'E5', 92), (10, 3.5, 0.5, 'D5', 94),
    (11, 0, 0.5, 'C#5', 94), (11, 0.5, 0.5, 'B4', 92), (11, 1, 0.5, 'A4', 92),
    (11, 1.5, 0.5, 'B4', 92), (11, 2, 0.5, 'C#5', 94), (11, 2.5, 0.5, 'D5', 96),
    (11, 3, 0.5, 'C#5', 94), (11, 3.5, 0.5, 'B4', 96),
]
RIFF = [
    (0, 0.0, 0.2, 'A4', 100), (0, 0.5, 0.2, 'A4', 88), (0, 0.75, 0.2, 'B4', 92),
    (0, 1.0, 0.2, 'C#5', 98), (0, 1.5, 0.2, 'E5', 100), (0, 1.75, 0.2, 'D5', 88),
    (0, 2.0, 0.2, 'C#5', 96), (0, 2.5, 0.2, 'B4', 90), (0, 3.0, 0.2, 'A4', 94),
    (0, 3.25, 0.2, 'B4', 88), (0, 3.5, 0.2, 'C#5', 94), (0, 3.75, 0.2, 'E5', 96),
    (1, 0.0, 0.2, 'D5', 100), (1, 0.5, 0.2, 'C#5', 92), (1, 0.75, 0.2, 'B4', 90),
    (1, 1.0, 0.2, 'C#5', 96), (1, 1.5, 0.2, 'A4', 98), (1, 2.0, 0.2, 'E4', 92),
    (1, 2.5, 0.2, 'A4', 90), (1, 3.0, 0.2, 'B4', 92), (1, 3.5, 0.3, 'C#5', 96),
]


def soft(evs, k=0.72):
    return [(b, bt, d, p, int(v * k)) for (b, bt, d, p, v) in evs]


def shift_riff(events, st):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    out = []
    for b, bt, d, nm, v in events:
        m = npitch(nm) + st
        out.append((b, bt, d, names[m % 12] + str(m // 12 - 1), v))
    return out


def play_riff(rr, who, start, i, st):
    for _rb, bt, rd, rn, rv in rr:
        who.n(start + i * 4 + bt, rd, npitch(rn), hum(rng, rv))


# ---------------- 段落装配 ----------------
t0 = 0.0
for si, (name, chords_raw, st) in enumerate(SECS):
    cs = [Chord(c).shifted(st) for c in chords_raw]
    nbars = len(cs)
    start = t0
    full_chorus = name in ('B1', 'B2', 'B3', 'B3x')
    for i, c in enumerate(cs):
        b = start + i * 4
        if name == 'Intro':
            pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 40))
            synth_arp16(arp, b, c, rng, vel=40) if i >= 4 else None
            if i < 4:
                bass_offbeat8(bass, b, c, rng, vel=64) if i >= 2 else None
                drum_bar(dr, b, 'bi_light', rng)
            else:
                rr = shift_riff(RIFF[:12] if i % 2 == 0 else RIFF[12:], st)
                for _rb, bt, rd, rn, rv in rr:
                    rgt.n(b + bt, rd, npitch(rn), hum(rng, rv - 8, 3))
                bass_offbeat8(bass, b, c, rng, vel=76)
                drum_bar(dr, b, 'bi_verse', rng)
        elif name in ('A1', 'A2'):
            bass_funk16(bass, b, c, cs[(i + 1) % nbars], rng, vel=90)
            ep_stabs(ep, b, c, rng, beats=((1.5, 0.75, 58), (3.5, 0.5, 56)), n=3)
            drum_bar(dr, b, 'bi_verse', rng, fill=(i == nbars - 1))
            if name == 'A2':
                synth_arp16(arp, b, c, rng, vel=54)
                gt_skank16(rgt, b, c, rng, vel_hi=58)
                pad.chord(b, 3.8, c.voice(low=52, high=68, n=3), hum(rng, 32))
        elif name == 'Pre':
            synth_arp16(arp, b, c, rng, vel=58)
            bass_offbeat8(bass, b, c, rng, vel=84)
            ep_stabs(ep, b, c, rng, beats=((0, 0.75, 62), (2, 0.75, 60), (2.75, 0.5, 58)), n=4)
            drum_bar(dr, b, 'bi_build' if i == 3 else 'bi_verse', rng)
        elif full_chorus:
            piano_drive16(pia, b, c, rng, vel=88)
            synth_arp16(arp, b, c, rng, vel=56)
            bass_offbeat8(bass, b, c, rng, vel=92)
            ep.chord(b + 0.5, 0.3, c.voice(low=64, high=80, n=3), hum(rng, 42))
            pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 34))
            drum_bar(dr, b, 'bi_chorus', rng, fill=(i == nbars - 1))
            if i == 0:
                crash(dr, b, vel=96)
        elif name in ('Post', 'Riff'):
            rr = shift_riff(RIFF[:12] if i % 2 == 0 else RIFF[12:], st)
            for _rb, bt, rd, rn, rv in rr:
                rgt.n(b + bt, rd, npitch(rn), hum(rng, rv))
                if name == 'Riff':
                    dbl.n(b + bt, rd, npitch(rn) - 12, hum(rng, rv - 30, 3))
            bass_offbeat8(bass, b, c, rng, vel=86)
            drum_bar(dr, b, 'bi_verse', rng, fill=(i == 3))
        elif name == 'Break':
            pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 46))
            if i < 10:
                bass_offbeat8(bass, b, c, rng, vel=70) if i % 2 == 0 else \
                    bass.n(b, 3.6, c.bass_midi(2), hum(rng, 72))
                drum_bar(dr, b, 'bi_break', rng)
                ep.chord(b, 3.6, c.voice(low=58, high=76, n=4), hum(rng, 52))
            else:
                drum_bar(dr, b, 'bi_build', rng)
    # ---- 主旋律 ----
    if name == 'A1':
        lead.phrase(start, MEL_A + sh(MEL_A2, 8))
    elif name == 'A2':
        lead.phrase(start, soft(MEL_A, 0.94) + sh(MEL_A2, 8))
    elif name == 'Pre':
        lead.phrase(start, MEL_PRE)
    elif name in ('B1', 'B2', 'B3', 'B3x'):
        mel = MEL_B
        if name == 'B3x':
            mel = MEL_B[:len(MEL_B) - 5] + list(MEL_B_END)
        lead.phrase(start, mel, tr=st)
        dbl.phrase(start, mel, tr=st)
        if name in ('B2', 'B3'):
            half = [(b - 4, bt, d, pp, v) for (b, bt, d, pp, v) in MEL_B if b >= 4]
            glock.phrase(start + 16, soft(half, 0.62), tr=st + 12)
        if name == 'B3x':
            glock.phrase(start, soft(MEL_B, 0.62), tr=st + 12)
    elif name == 'Break':
        lead.phrase(start, MEL_BRK)
    elif name == 'Intro':
        lead.phrase(start, soft([e for e in MEL_B if e[0] in (0, 1)], 0.8))
        glock.phrase(start, soft([e for e in MEL_B if e[0] in (0, 1)], 0.6), tr=12)
    elif name == 'Outro':
        lead.phrase(start, soft(MEL_B, 0.7 + 0.0), tr=st)
        glock.phrase(start, soft(MEL_B, 0.62), tr=st + 12)
    t0 = start + nbars * 4

# Outro 收束: 开头一记 hit, 最后一小节再全乐队收
crash(dr, t0 - 32, vel=90)
crash(dr, t0 - 4, vel=92)
for sect in (t0 - 32, t0 - 4):
    stab = Chord('A').shifted(1)
    pia.chord(sect, 3.6, stab.voice(low=58, high=78, n=4), 84)
    bass.n(sect, 3.6, stab.bass_midi(2), 96)
    dr.hits(sect, [(0, 36, 112), (0, 39, 100)])

dur_s = t0 * 60 / BPM
print(f'bars={int(t0 // 4)}  time={dur_s:.1f}s  sections={len(SECS)}')
for trk in p.tracks:
    print(f'  {trk.name:12s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
p.save(OUT)
print('saved:', os.path.abspath(OUT))

# 虚拟歌姬用: 仅主旋律轨 (A大调 150bpm; 终段已含 +1 移调)
vp = Piece('电气花火 vocal lead (for OpenUTAU/SynthV)', BPM, key='A')
vt = vp.add(Trk('Lead Vocal', 0, 0, vol=100, reverb=30))
vt.events = list(lead.events)
for b, cents in lead.bends:
    vt.bends.append((b, cents))
vp.save(OUT_VOCAL)
print('saved:', os.path.abspath(OUT_VOCAL), f'({len(vt.events)} notes)')
