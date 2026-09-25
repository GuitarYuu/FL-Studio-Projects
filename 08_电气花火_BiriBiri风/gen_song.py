# -*- coding: utf-8 -*-
"""04「电气花火」 v4 —— 洗脑钩子版 (YOASOBI「BiriBiri」风 × 宝可梦)
A 大调 160bpm | v2 钩子/曲式保留, 编曲按 BiriBiri 的"音墙"思路全面加厚:
  [双手钢琴墙] 左手八度泵 8分+每4小节一次上行琶音 run; 右手 16 分和弦脉冲无气口
  [锯齿和弦墙] 副歌持续/脉冲锯齿 6 声部, 现代 J-pop 的"满"
  [人声堆叠] 合唱(Aahs)三度和声 + Voice Oohs 长音垫 + Vocal Chop 回声
  [驱动贝斯] 恒 8 分 + 八度跳 + 16 分 pick-up + 换和弦滑音
  [管弦重音] 段落头弦乐长和弦重击 = drop 的"墙落地"
  [鼓组加密] 副歌四踩+全反拍开镲+16分鬼音, 段落头 crash
BPM 150->160 (BiriBiri 的冲劲)。v1=tag dianqi-v1, v2=tag dianqi-v2。
曲式: Intro8-A16-Pre4-B8-Post4-A16-Pre4-B8-Riff4-Break8-B3(+1)8-B3'(+1)8-Post2(+1)4-Outro(+1)8
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20261001)
BPM = 160
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '04_电气花火_BiriBiri风_complete.mid')
OUT_VOCAL = os.path.join(HERE, 'vocal_lead.mid')

p = Piece('电气花火 v4 (BiriBiri风格致敬)', BPM, key='A')
lead = p.add(Trk('Lead Vocal', 81, 3, vol=114, pan=64, reverb=40))
harm = p.add(Trk('Lead Harmony', 52, 11, vol=78, pan=64, reverb=48))
dbl = p.add(Trk('Lead Double', 80, 4, vol=66, pan=64, reverb=32))
ooh = p.add(Trk('Ooh Pad', 53, 12, vol=64, pan=64, reverb=62))
piaL = p.add(Trk('Piano LH', 0, 0, vol=100, pan=56, reverb=38))
piaR = p.add(Trk('Piano RH', 0, 1, vol=102, pan=72, reverb=38))
saw = p.add(Trk('Saw Wall', 81, 13, vol=58, pan=64, reverb=40))
chop = p.add(Trk('Vocal Chop', 80, 2, vol=64, pan=44, reverb=40))
arp = p.add(Trk('Arp Synth', 81, 6, vol=62, pan=88, reverb=36))
glock = p.add(Trk('Glockenspiel', 9, 5, vol=80, pan=80, reverb=60))
rgt = p.add(Trk('Riff Guitar', 29, 14, vol=92, pan=36, reverb=26))
bass = p.add(Trk('Slap Bass', 33, 7, vol=108, pan=64, reverb=12))
strs = p.add(Trk('Strings Hit', 48, 15, vol=70, pan=64, reverb=56))
pad = p.add(Trk('Warm Pad', 89, 8, vol=58, pan=64, reverb=66))
dr = p.add(Drums(vol=110))

A16 = ['F#m7', 'Dmaj7', 'A', 'E'] * 4
PRE = ['Dmaj7', 'E', 'F#m7', 'E']
B8 = ['A', 'E', 'F#m7', 'D'] * 2
BRK = ['F#m7', 'E', 'Dmaj7', 'C#m7'] * 2
INTRO = ['A', 'A', 'F#m7', 'D'] * 2
POSTC = ['A', 'A', 'F#m7', 'D']

SECS = [
    ('Intro', INTRO, 0), ('A1', A16, 0), ('Pre', PRE, 0), ('B1', B8, 0),
    ('Post', POSTC, 0),
    ('A2', A16, 0), ('Pre', PRE, 0), ('B2', B8, 0),
    ('Riff', POSTC, 0),
    ('Break', BRK, 0),
    ('B3', B8, 1), ('B3x', B8, 1),
    ('Post2', POSTC, 1),
    ('Outro', B8, 1),
]

MEL_A = [
    (0, 0, 0.5, 'C#5', 88), (0, 0.5, 0.5, 'C#5', 82), (0, 1, 1, 'A4', 86), (0, 2, 0.5, 'B4', 84), (0, 2.5, 0.5, 'C#5', 86), (0, 3, 1, 'A4', 88),
    (1, 0, 1, 'F#4', 86), (1, 1, 0.5, 'G#4', 82), (1, 1.5, 0.5, 'A4', 84), (1, 2, 2, 'B4', 88),
    (2, 0, 0.5, 'C#5', 88), (2, 0.5, 0.5, 'C#5', 82), (2, 1, 1, 'A4', 86), (2, 2, 0.5, 'B4', 84), (2, 2.5, 0.5, 'C#5', 86), (2, 3, 1, 'E5', 90),
    (3, 0, 1, 'D5', 90), (3, 1, 0.5, 'C#5', 86), (3, 1.5, 0.5, 'B4', 84), (3, 2, 2, 'C#5', 88),
    (4, 0, 0.5, 'C#5', 88), (4, 0.5, 0.5, 'C#5', 82), (4, 1, 1, 'A4', 86), (4, 2, 0.5, 'B4', 84), (4, 2.5, 0.5, 'C#5', 86), (4, 3, 1, 'A4', 88),
    (5, 0, 1, 'F#4', 86), (5, 1, 0.5, 'G#4', 82), (5, 1.5, 0.5, 'A4', 84), (5, 2, 2, 'B4', 88),
    (6, 0, 0.5, 'C#5', 88), (6, 0.5, 0.5, 'C#5', 82), (6, 1, 1, 'A4', 86), (6, 2, 0.5, 'B4', 84), (6, 2.5, 0.5, 'C#5', 86), (6, 3, 1, 'E5', 90),
    (7, 0, 1, 'D5', 90), (7, 1, 0.5, 'C#5', 86), (7, 1.5, 0.5, 'B4', 84), (7, 2, 0.5, 'A4', 86), (7, 2.5, 0.5, 'B4', 86), (7, 3, 2, 'B4', 90),
]
MEL_A2 = MEL_A[:36] + [
    (7, 0, 1, 'D5', 90), (7, 1, 0.5, 'C#5', 86), (7, 1.5, 0.5, 'B4', 84),
    (7, 2, 0.5, 'A4', 86), (7, 2.5, 0.5, 'G#4', 84), (7, 3, 1.5, 'B4', 90),
]
MEL_PRE = [
    (0, 0, 1, 'A4', 88), (0, 1, 1, 'B4', 90), (0, 2, 1, 'C#5', 92), (0, 3, 1, 'D5', 94),
    (1, 0, 0.5, 'E5', 94), (1, 0.5, 0.5, 'E5', 88), (1, 1, 0.5, 'F#5', 94), (1, 1.5, 0.5, 'F#5', 88),
    (1, 2, 0.5, 'E5', 92), (1, 2.5, 0.5, 'D5', 90), (1, 3, 1, 'C#5', 92),
    (2, 0, 1, 'D5', 92), (2, 1, 1, 'E5', 94), (2, 2, 2, 'F#5', 98),
    (3, 0, 1.5, 'F#5', 96), (3, 1.5, 0.5, 'G#5', 92), (3, 2, 0.5, 'A5', 98),
    (3, 2.5, 0.5, 'G#5', 92), (3, 3, 0.5, 'F#5', 94), (3, 3.5, 0.5, 'E5', 96),
]
MEL_B = [
    (0, 0, 0.25, 'E5', 100), (0, 0.25, 0.25, 'E5', 92), (0, 0.5, 0.5, 'E5', 98),
    (0, 1, 0.5, 'D5', 96), (0, 1.5, 0.5, 'C#5', 94), (0, 2, 2, 'B4', 98),
    (1, 0, 0.5, 'C#5', 94), (1, 0.5, 0.5, 'C#5', 88), (1, 1, 1, 'B4', 94),
    (1, 2, 0.5, 'A4', 90), (1, 2.5, 0.5, 'B4', 92), (1, 3, 1, 'C#5', 96),
    (2, 0, 0.25, 'E5', 100), (2, 0.25, 0.25, 'E5', 92), (2, 0.5, 0.5, 'E5', 98),
    (2, 1, 0.5, 'D5', 96), (2, 1.5, 0.5, 'C#5', 94), (2, 2, 2, 'D5', 98),
    (3, 0, 0.5, 'E5', 96), (3, 0.5, 0.5, 'D5', 92), (3, 1, 0.5, 'C#5', 94),
    (3, 1.5, 0.5, 'D5', 94), (3, 2, 2, 'E5', 100),
    (4, 0, 0.25, 'E5', 100), (4, 0.25, 0.25, 'E5', 92), (4, 0.5, 0.5, 'E5', 98),
    (4, 1, 0.5, 'D5', 96), (4, 1.5, 0.5, 'C#5', 94), (4, 2, 2, 'B4', 98),
    (5, 0, 0.5, 'C#5', 94), (5, 0.5, 0.5, 'C#5', 88), (5, 1, 1, 'B4', 94),
    (5, 2, 0.5, 'A4', 90), (5, 2.5, 0.5, 'B4', 92), (5, 3, 1, 'C#5', 96),
    (6, 0, 0.25, 'E5', 100), (6, 0.25, 0.25, 'E5', 92), (6, 0.5, 0.5, 'E5', 98),
    (6, 1, 0.5, 'D5', 96), (6, 1.5, 0.5, 'C#5', 94), (6, 2, 2, 'D5', 98),
    (7, 0, 0.5, 'C#5', 96), (7, 0.5, 0.5, 'B4', 92), (7, 1, 0.5, 'A4', 94),
    (7, 1.5, 0.5, 'B4', 94), (7, 2, 0.5, 'C#5', 96), (7, 2.5, 0.5, 'D5', 98), (7, 3, 1, 'E5', 100),
]
MEL_B_END = (7, 0, 0.5, 'E5', 100), (7, 0.5, 0.5, 'F#5', 98), (7, 1, 0.5, 'G#5', 100), \
            (7, 1.5, 0.5, 'A5', 104), (7, 2, 2.5, 'A5', 104)
MEL_BRK = [
    (0, 0, 0.25, 'E5', 92), (0, 0.25, 0.25, 'E5', 84), (0, 0.5, 0.5, 'E5', 90),
    (0, 1, 0.5, 'D5', 88), (0, 1.5, 0.5, 'C#5', 86), (0, 2, 2, 'B4', 90),
    (1, 0, 3.5, 'A4', 88),
    (2, 0, 2, 'C#5', 90), (2, 2, 1, 'D5', 90), (2, 3, 1, 'E5', 92),
    (3, 0, 3.5, 'E5', 92),
    (4, 0, 0.25, 'E5', 92), (4, 0.25, 0.25, 'E5', 84), (4, 0.5, 0.5, 'E5', 90),
    (4, 1, 0.5, 'D5', 88), (4, 1.5, 0.5, 'C#5', 86), (4, 2, 2, 'B4', 90),
    (5, 0, 3.5, 'A4', 88),
    (6, 0, 2, 'E5', 92), (6, 2, 0.5, 'F#5', 94), (6, 2.5, 0.5, 'G#5', 96), (6, 3, 1, 'A5', 98),
    (7, 0, 2, 'F#5', 96), (7, 2, 0.5, 'E5', 92), (7, 2.5, 0.5, 'D5', 90),
    (7, 3, 0.5, 'C#5', 92), (7, 3.5, 0.5, 'B4', 94),
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
# 终副歌钟琴对旋律: 每小节第4拍下行火花三连, 末小节上行冲
COUNTER = [
    (0, 3.0, 0.25, 'E6', 82), (0, 3.25, 0.25, 'D6', 78), (0, 3.5, 0.5, 'C#6', 82),
    (1, 3.0, 0.25, 'E6', 80), (1, 3.25, 0.25, 'D6', 76), (1, 3.5, 0.5, 'B5', 80),
    (2, 3.0, 0.25, 'F#6', 82), (2, 3.25, 0.25, 'E6', 78), (2, 3.5, 0.5, 'D6', 82),
    (3, 3.0, 0.25, 'E6', 80), (3, 3.25, 0.25, 'D6', 76), (3, 3.5, 0.5, 'C#6', 80),
    (4, 3.0, 0.25, 'E6', 82), (4, 3.25, 0.25, 'D6', 78), (4, 3.5, 0.5, 'C#6', 82),
    (5, 3.0, 0.25, 'F#6', 80), (5, 3.25, 0.25, 'E6', 76), (5, 3.5, 0.5, 'C#6', 80),
    (6, 3.0, 0.25, 'A6', 84), (6, 3.25, 0.25, 'F#6', 80), (6, 3.5, 0.5, 'E6', 82),
    (7, 3.0, 0.25, 'C#6', 82), (7, 3.25, 0.25, 'D6', 84), (7, 3.5, 0.25, 'E6', 86), (7, 3.75, 0.25, 'F#6', 88),
]

_ORDER = [9, 11, 1, 2, 4, 6, 8]
_SN = sorted(o * 12 + pc for o in range(3, 9) for pc in _ORDER if 40 <= o * 12 + pc <= 100)
def third_below(m):
    idx = None
    for i, p in enumerate(_SN):
        if p == m:
            idx = i; break
        if p > m:
            idx = i - 1; break
    if idx is None:
        idx = len(_SN) - 1
    return _SN[max(0, idx - 2)]

def soft(evs, k=0.72):
    return [(b, bt, d, p, int(v * k)) for (b, bt, d, p, v) in evs]

def shift_riff(events, st):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    out = []
    for b, bt, d, nm, v in events:
        m = npitch(nm) + st
        out.append((b, bt, d, names[m % 12] + str(m // 12 - 1), v))
    return out

def play_riff(rgt, b, rr, rng, dv=0):
    for _rb, bt, rd, rn, rv in rr:
        rgt.n(b + bt, rd, npitch(rn), hum(rng, rv + dv))

# ---------------- v3 音墙构件 ----------------
def piano_wall(plh, prh, b, chord, next_c, rng, i, run=False, vel=92):
    """左手八度泵 + 右手 16 分脉冲 + 每 4 小节上行 run"""
    tones = chord.voice(low=64, high=88, n=4)
    pat = [k % len(tones) for k in (0, 1, 2, 1, 3, 1, 2, 1, 0, 1, 2, 1, 3, 2, 1, 2)]
    n_pulse = 12 if (run and i % 4 == 3) else 16
    for k in range(n_pulse):
        idx = pat[k]
        prh.n(b + k * 0.25, 0.22, tones[idx],
              hum(rng, vel + (12 if k % 4 == 0 else -6)))
    r2 = chord.bass_midi(2)
    for k, off in enumerate((0, 0, 12, 0, 0, 12, 0, 7)):
        plh.n(b + k * 0.5, 0.42, r2 + off, hum(rng, vel - 4))
    if run and i % 4 == 3:
        rt = chord.voice(low=52, high=76, n=4)
        for k in range(4):
            plh.n(b + 3 + k * 0.25, 0.2, rt[k % len(rt)], hum(rng, vel + 4))
            prh.n(b + 3 + k * 0.25, 0.2, rt[k % len(rt)] + 12, hum(rng, vel))

def saw_wall(sw, b, chord, rng, i, pulse=False, vel=46):
    tones = chord.voice(low=55, high=79, n=6)
    if pulse:
        for k in range(8):
            sw.chord(b + k * 0.5, 0.4, tones, hum(rng, vel + (6 if k % 2 == 0 else 0), 2))
    else:
        sw.chord(b, 1.9, tones, hum(rng, vel, 2))
        sw.chord(b + 2, 1.9, tones, hum(rng, vel, 2))

def bass_drive(bass, b, chord, next_c, rng, vel=98, sub=False, slide=False):
    r = chord.bass_midi(2)
    if slide:
        bass.bend(b, -120)
        bass.bend(b + 0.12, 0)
    for k, off in enumerate((0, 0, 0, 12, 0, 7, 0)):
        bass.n(b + k * 0.5, 0.42, r + off, hum(rng, vel - (8 if off else 0)))
    nr = next_c.bass_midi(2)
    appr = nr - 2 if nr > r else nr + 2
    bass.n(b + 3.5, 0.2, r + 12, hum(rng, vel - 6))
    bass.n(b + 3.75, 0.2, appr, hum(rng, vel - 2))
    if sub:
        bass.n(b, 3.6, r - 12, hum(rng, vel - 30, 2))

def ooh_pad(oo, b, chord, rng, vel=44, kind='hold'):
    tones = chord.voice(low=59, high=74, n=3)
    if kind == 'hold':
        oo.chord(b, 3.8, tones, hum(rng, vel, 2))
    else:  # answer: 后半拍两音
        oo.n(b + 2, 1.2, tones[-1], hum(rng, vel + 4))
        oo.n(b + 3.5, 0.4, tones[-2], hum(rng, vel))

def strings_hit(st, b, chord, rng, vel=50, hold=3.8):
    st.chord(b, hold, chord.voice(low=55, high=79, n=5), hum(rng, vel, 2))

def fanfare(gl, b, st=0, vel=84):
    """宝可梦式上行三和弦 fanfare (原创造型): A5-C#6-E6 -> A5"""
    for bt, d, nm, v in [(0.0, 0.25, 'A5', vel), (0.25, 0.25, 'C#6', vel - 6),
                         (0.5, 0.5, 'E6', vel), (1.0, 1.5, 'A5', vel - 10)]:
        gl.n(b + bt, d, npitch(nm) + st, v)


def chops(ch, b, st, rng, vel=56):
    """vocal chop: 洗脑 pickup 单元格回声 (E-E-E-D-C#)"""
    seq = [(0.0, 'E5'), (0.25, 'E5'), (0.5, 'E5'), (1.0, 'D5'), (1.5, 'C#5'),
           (2.5, 'B4'), (3.0, 'C#5'), (3.5, 'D5')]
    for bt, nm in seq:
        ch.n(b + bt, 0.18, npitch(nm) + st, hum(rng, vel))


def drum_v3(dr, b, style, rng, i=0, fill=False):
    if style == 'heartbeat':
        dr.hits(b, [(0, 36, 74), (2, 36, 66)] +
                [(k * 0.5, 42, 38 if k % 2 == 0 else 28) for k in range(8)])
    elif style == 'verse':
        dr.hits(b, [(0, 36, 100), (1.5, 36, 86), (2.5, 36, 96),
                    (1, 39, 88), (3, 39, 90), (1.75, 38, 30), (2.75, 38, 32), (3.625, 38, 28)])
        dr.hits(b, [(k * 0.25, 42, (86 if k % 4 == 0 else 60) if k % 2 == 0 else 42) for k in range(16)])
        dr.hits(b, [(3.5, 46, 72)])
        if fill:
            dr.hits(b, [(3, 38, 100), (3.25, 38, 106), (3.5, 45, 112), (3.75, 43, 116)])
    elif style == 'chorus':
        dr.hits(b, [(0, 36, 114), (1, 36, 104), (2, 36, 110), (3, 36, 106),
                    (1, 39, 106), (3, 39, 108),
                    (1.75, 38, 34), (2.75, 38, 36), (3.625, 38, 32)])
        dr.hits(b, [(k * 0.5, 46, 80) for k in range(4)])
        dr.hits(b, [(k * 0.25, 42, (92 if k % 4 == 0 else 66) if k % 2 == 0 else 48) for k in range(16)])
        if i % 2 == 1:
            dr.hits(b, [(0.25, 38, 30), (2.25, 38, 34)])
        if fill:
            dr.hits(b, [(3, 38, 108), (3.25, 38, 114), (3.5, 45, 120), (3.75, 43, 124)])
    elif style == 'riser':
        dr.hits(b, [(k * 0.25, 42, min(118, 46 + k * 5)) for k in range(16)])
        dr.hits(b, [(k * 0.25, 38, min(126, 62 + (k - 8) * 9)) for k in range(8, 16)])
        dr.hits(b, [(0, 36, 98)])
    elif style == 'break':
        dr.hits(b, [(0, 36, 90), (2, 38, 88), (1, 42, 46), (3, 42, 46),
                    (1.75, 38, 26), (3.5, 39, 58)])

def impact(dr, strs, b, chord, rng, vel=1.0):
    crash(dr, b, vel=int(94 * vel))
    dr.hits(b, [(0, 36, int(116 * vel)), (0, 45, int(100 * vel))])
    strs.chord(b, 3.6, chord.voice(low=55, high=79, n=5), hum(rng, int(52 * vel)))

def glock_interlock(trk, b, chord, rng):
    tones = sorted(chord.voice(low=79, high=95, n=4), reverse=True)
    for bt, idx, v in [(1.5, 0, 68), (2.0, 1, 72), (2.5, 2, 68), (3.5, 3, 62)]:
        trk.n(b + bt, 0.45, tones[idx % len(tones)], hum(rng, v, 3))

# ---------------- 段落装配 ----------------
t0 = 0.0
for si, (name, chords_raw, st) in enumerate(SECS):
    cs = [Chord(c).shifted(st) for c in chords_raw]
    nbars = len(cs)
    start = t0
    chorus = name in ('B1', 'B2', 'B3', 'B3x', 'Outro')
    ov = 0.8 if name == 'Outro' else 1.0
    for i, c in enumerate(cs):
        b = start + i * 4
        nxt = cs[(i + 1) % nbars]
        if name == 'Intro':
            pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 42, 2))
            if i < 4:
                if i == 0:
                    fanfare(glock, b, st)
                if i >= 2:
                    drum_v3(dr, b, 'heartbeat', rng)
            else:
                piano_wall(piaL, piaR, b, c, nxt, rng, i, run=True, vel=84)
                rr = shift_riff(RIFF[:12] if i % 2 == 0 else RIFF[12:], st)
                play_riff(rgt, b, rr, rng)
                bass_drive(bass, b, c, nxt, rng, vel=88)
                drum_v3(dr, b, 'verse', rng, i=i)
                if i == 6:
                    ooh_pad(ooh, b, c, rng, kind='hold')
        elif name in ('A1', 'A2'):
            piano_wall(piaL, piaR, b, c, nxt, rng, i, run=True, vel=90)
            bass_drive(bass, b, c, nxt, rng, vel=94)
            drum_v3(dr, b, 'verse', rng, i=i, fill=(i == nbars - 1))
            saw_wall(saw, b, c, rng, i, vel=36 if name == 'A1' else 40)
            if name == 'A2':
                tones = c.voice(low=64, high=84, n=4)
                arp16 = [k % len(tones) for k in (0, 1, 2, 3, 1, 2, 3, 2)]
                for k, idx in enumerate(arp16):
                    arp.n(b + k * 0.25, 0.2, tones[idx], hum(rng, 54 - (8 if k % 4 == 0 else 0), 3))
                ooh_pad(ooh, b, c, rng, kind='answer') if i % 2 == 0 else None
            if i == 0:
                impact(dr, strs, b, c, rng, 0.85)
        elif name == 'Pre':
            piano_wall(piaL, piaR, b, c, nxt, rng, i, vel=92)
            bass_drive(bass, b, c, nxt, rng, vel=96)
            arp_t = c.voice(low=76 if i >= 2 else 64, high=100 if i >= 2 else 84, n=4)
            pat = [k % len(arp_t) for k in (0, 2, 1, 3, 2, 3, 1, 2)]
            for k, idx in enumerate(pat):
                arp.n(b + k * 0.25, 0.2, arp_t[idx], hum(rng, 58, 3))
            if i < 3:
                drum_v3(dr, b, 'verse', rng, i=i + 1)
            else:
                drum_v3(dr, b, 'riser', rng)
                saw.chord(b, 3.8, c.voice(low=55, high=79, n=6), hum(rng, 44, 2))
            if i == 0:
                strings_hit(strs, b, c, rng, 46)
        elif chorus:
            piano_wall(piaL, piaR, b, c, nxt, rng, i, run=True, vel=int(94 * ov))
            bass_drive(bass, b, c, nxt, rng, vel=int(100 * ov), sub=True, slide=(i % 2 == 0))
            drum_v3(dr, b, 'chorus', rng, i=i, fill=(i == nbars - 1 and name != 'Outro'))
            saw_wall(saw, b, c, rng, i, pulse=(name in ('B3', 'B3x')), vel=int(48 * ov))
            pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 36, 2))
            if name in ('B1', 'B3') or (name == 'B2' and i < 4):
                glock_interlock(glock, b, c, rng)
            if i % 2 == 0 and i > 0:
                strings_hit(strs, b, c, rng, 40, hold=1.8)
            if i == 0:
                if name == 'Outro':
                    fanfare(glock, b, st)
                else:
                    impact(dr, strs, b, c, rng, 1.0)
                    fanfare(glock, b, st)
        elif name in ('Post', 'Riff', 'Post2'):
            piano_wall(piaL, piaR, b, c, nxt, rng, i, run=True, vel=88)
            bass_drive(bass, b, c, nxt, rng, vel=92)
            drum_v3(dr, b, 'verse', rng, i=i, fill=(i == nbars - 1))
            rr = shift_riff(RIFF[:12] if i % 2 == 0 else RIFF[12:], st)
            play_riff(rgt, b, rr, rng)
            chops(chop, b, st, rng, vel=54 if name != 'Post2' else 60)
            if name == 'Post2':
                saw_wall(saw, b, c, rng, i, pulse=True, vel=44)
                drum_v3(dr, b, 'chorus', rng, i=i)
            if i == 0 and name != 'Post':
                crash(dr, b, vel=88)
        elif name == 'Break':
            pad_pump = None
            pad.chord(b, 3.8, c.voice(low=55, high=73, n=4), hum(rng, 46, 2))
            strings_hit(strs, b, c, rng, 46)
            ep_like = c.voice(low=58, high=76, n=4)
            if i < 5:
                chop.chord(b, 1.8, ep_like, hum(rng, 50))
                if i % 2 == 0:
                    bass.n(b, 3.6, c.bass_midi(2), hum(rng, 76))
                drum_v3(dr, b, 'break', rng)
            else:
                arp_t = c.voice(low=76, high=100, n=4)
                pat = [k % len(arp_t) for k in (0, 1, 2, 3, 2, 3, 1, 2)]
                for k, idx in enumerate(pat):
                    arp.n(b + k * 0.25, 0.2, arp_t[idx], hum(rng, min(72, 52 + (i - 5) * 6), 3))
                if i >= 6:
                    bass_drive(bass, b, c, nxt, rng, vel=90)
                    drum_v3(dr, b, 'riser' if i == 7 else 'break', rng)
    # ---- 主旋律 / 和声 / 加倍 ----
    if name == 'A1':
        lead.phrase(start, MEL_A + sh(MEL_A2, 8))
    elif name == 'A2':
        lead.phrase(start, soft(MEL_A, 0.94) + sh(MEL_A2, 8))
    elif name == 'Pre':
        lead.phrase(start, MEL_PRE)
    elif chorus:
        mel = MEL_B
        if name == 'B3x':
            mel = MEL_B[:len(MEL_B) - 7] + list(MEL_B_END)
        lead.phrase(start, mel, tr=st)
        dbl.phrase(start, mel, tr=st)
        harm.phrase(start, [(bb, bt, d, third_below(npitch(pp)) + st, v)
                            for (bb, bt, d, pp, v) in mel])
        if name == 'B2':
            half = [(bb - 4, bt, d, pp, v) for (bb, bt, d, pp, v) in MEL_B if bb >= 4]
            glock.phrase(start + 16, soft(half, 0.62), tr=st + 12)
        if name == 'B3x':
            glock.phrase(start, soft(COUNTER, 0.92), tr=st)
    elif name == 'Break':
        lead.phrase(start, MEL_BRK)
        harm.phrase(start, [(bb, bt, d, third_below(npitch(pp)), v) for (bb, bt, d, pp, v) in MEL_BRK])
    elif name == 'Intro':
        lead.phrase(start, soft([e for e in MEL_B if e[0] in (0, 1)], 0.8))
        glock.phrase(start + 8, soft([e for e in MEL_B if e[0] in (0, 1)], 0.6), tr=12)
    elif name == 'Outro':
        lead.phrase(start, soft(MEL_B, 0.72), tr=st)
        harm.phrase(start, [(bb, bt, d, third_below(npitch(pp)) + st, v)
                            for (bb, bt, d, pp, v) in MEL_B])
        half = [(bb - 4, bt, d, pp, v) for (bb, bt, d, pp, v) in MEL_B if bb >= 4]
        glock.phrase(start + 16, soft(half, 0.5), tr=st + 12)
    elif name == 'Post2':
        lead.phrase(start, soft([e for e in MEL_B if e[0] in (0, 1)], 0.8), tr=st)
    t0 = start + nbars * 4

# 收束: 倒数第 8 小节 & 最后一小节全乐队 hit
for sect in (t0 - 32, t0 - 4):
    stab = Chord('A').shifted(1)
    crash(dr, sect, vel=92)
    strs.chord(sect, 3.6, stab.voice(low=55, high=79, n=5), 56)
    dr.hits(sect, [(0, 36, 116), (0, 39, 104)])

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s  sections={len(SECS)}')
for trk in p.tracks:
    print(f'  {trk.name:14s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
p.save(OUT)
print('saved:', os.path.abspath(OUT))

vp = Piece('电气花火 v4 vocal lead (for OpenUTAU/SynthV)', BPM, key='A')
vt = vp.add(Trk('Lead Vocal', 0, 0, vol=100, reverb=30))
vt.events = list(lead.events)
vp.save(OUT_VOCAL)
print('saved:', os.path.abspath(OUT_VOCAL), f'({len(vt.events)} notes)')

# ================= 虚拟歌姬 UST 工程 + 歌词 =================
VERSE1 = [
    "あ さ の ひ か り", "あ び た ら",
    "ほ ら す す め ば", "み え る よ",
    "び り び り き ら", "め く そ ら",
    "ど こ ま で も い", "け る き が す る",
]
VERSE2 = [
    "ち い さ な て を", "つ な い だ",
    "き み と す す め", "は る か へ",
    "び り び り こ え", "き ら め く",
    "ま ぶ し さ へ と", "は し り だ す よ",
]
PRE_L = ["い ま す ぐ", "と び こ え て ゆ く", "は て へ", "ゆ め の つ づ き"]
HOOK = [
    "び り び り ひ かっ", "て き み と い く",
    "ぴ か ぴ か む ね", "の お く へ と",
    "び り び り ひ かっ", "て ゆ め が は し",
    "て こ こ ろ が は", "し り だ す よ う に",
]
HOOKX = HOOK[:7] + ["き ら め く よ"]
BRK_L = [
    "も っ と も っ と", "あ", "は て へ", "あ",
    "も っ と も っ と", "あ", "い ざ ゆ く", "と び き り の",
]
LYRICS = {"A1": VERSE1, "A2": VERSE2, "Pre": PRE_L, "B1": HOOK, "B2": HOOK,
          "B3": HOOK, "B3x": HOOKX, "Break": BRK_L, "Outro": HOOK}

# 各段起始拍
_starts, _occ, _t = {}, {}, 0.0
for _n, _cs, _st in SECS:
    _i = _occ.get(_n, 0)
    _starts.setdefault(_n, []).append(_t)
    _occ[_n] = _i + 1
    _t += len(_cs) * 4

sung = []   # (start_beat, dur, pitch, mora)
for name, _cs, _st in SECS:
    if name not in LYRICS:
        continue
    tpl = LYRICS[name]
    s = _starts[name][0] if name != 'Pre' else _starts['Pre'][0]
    inst = 0
    for k, (n2, _c2, _s2) in enumerate(SECS[: [x[0] for x in SECS].index(name) + 1]):
        if n2 == name:
            pass
    # 找第几次出现
    cnt = [x[0] for x in SECS].count(name)
    s = _starts[name][0]
    nbars = len(tpl)
    notes = sorted([e for e in lead.events if s - 1e-6 <= e[0] < s + nbars * 4])
    for bar in range(nbars):
        bn = [e for e in notes if s + bar * 4 <= e[0] < s + (bar + 1) * 4]
        moras = tpl[bar].split()
        assert len(bn) == len(moras), (name, bar, len(bn), len(moras), tpl[bar])
        for (t, d, p, v), m in zip(bn, moras):
            sung.append((t, d, p, m))

# Pre 第二次出现用同样歌词
_pre2 = _starts['Pre'][1] if len(_starts.get('Pre', [])) > 1 else None
if _pre2 is not None:
    s = _pre2
    nbars = len(PRE_L)
    notes = sorted([e for e in lead.events if s - 1e-6 <= e[0] < s + nbars * 4])
    for bar in range(nbars):
        bn = [e for e in notes if s + bar * 4 <= e[0] < s + (bar + 1) * 4]
        moras = PRE_L[bar].split()
        assert len(bn) == len(moras), ('Pre2', bar, len(bn), len(moras))
        for (t, d, p, v), m in zip(bn, moras):
            sung.append((t, d, p, m))

sung.sort()
ust = ["[#SETTING]", "Tempo=%.2f" % BPM, "Tracks=1",
       "ProjectName=DianqiHuohua_v4", "VoiceDir="]
cursor = 0.0
for t, d, p, m in sung:
    if t > cursor + 1e-6:
        ust += ["[#%04d]" % len(ust), "Length=%d" % int(round((t - cursor) * 480)),
                "Lyric=R", "NoteNum=60"]
    ust += ["[#%04d]" % len(ust), "Length=%d" % int(round(d * 480)),
            "Lyric=%s" % m, "NoteNum=%d" % p, "Velocity=80", "Modulation=0"]
    cursor = t + d
ust.append("[#TRACKEND]")
OUT_UST = os.path.join(HERE, 'vocal_project.ust')
io_open = open
with io_open(OUT_UST, 'w', encoding='utf-8') as f:
    f.write(chr(10).join(ust) + chr(10))
print('saved:', os.path.abspath(OUT_UST), f'({sum(1 for e in sung)} 音, 含休止 {len(ust)} 块)')

# 中文对照歌词
CN = {
    "A1": ["晨光中 沐浴过后", "看吧只要前进", "就能看见", "电光闪耀的天", "空", "仿佛哪里都", "能去的感觉"],
    "B1": ["电光火花 点亮了", "和你一起出发", "闪闪发光 在心中", "的深处", "电光火花 梦想奔跑", "让心也奔跑起来"],
}
txt = ["《电气花火 v4》虚拟歌姬歌词对照 (A大调 160bpm)", ""]
order = [('A1', '主歌1'), ('Pre', '预副歌'), ('B1', '副歌'), ('A2', '主歌2'),
         ('Pre', '预副歌'), ('B2', '副歌'), ('Break', '间奏'), ('B3', '副歌(升半音)'),
         ('B3x', '副歌(升半音+对旋律)'), ('Outro', '尾声')]
for name, label in order:
    txt.append(f"—— {label} ({name}) ——")
    for bar in LYRICS[name]:
        txt.append("  " + bar.replace(" ", ""))
    txt.append("")
OUT_LYR = os.path.join(HERE, 'lyrics_v4.txt')
with io_open(OUT_LYR, 'w', encoding='utf-8') as f:
    f.write(chr(10).join(txt) + chr(10))
print('saved:', os.path.abspath(OUT_LYR))

