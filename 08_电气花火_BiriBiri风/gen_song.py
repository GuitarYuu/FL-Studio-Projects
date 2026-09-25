# -*- coding: utf-8 -*-
"""04「电气花火」 v2 —— 现代日系流行层次重构 (YOASOBI「BiriBiri」风 × 宝可梦)
A 大调 150bpm | 钩子与曲式骨架同 v1, 编曲全面重做:
  [声部register分离] 贝斯低音区/铺底中音区/钩子高音区/钟琴火花音区, 各占一层频段
  [侧链泵感] 垫与EP按"落-回"轮廓做 offbeat 恢复, 模拟 sidechain
  [四小节微变化] 镲片轮廓/军鼓鬼音/开镲位按小节轮换, 每遍副歌末尾不同 fill
  [riser/抽空] 预副歌末小节镲+军鼓双滚奏渐强, 副歌前留半拍真空
  [对钩子] 钟琴在钩子长音的空拍上插 8 分答句; 终副歌整条对旋律
  [低频层] 副歌加 sub 八度低音 + 滑音弯头
  [声像/力度] 左右双钢琴位、副歌 4-8 小节琶音上移八度做弧线
v1 见 git tag dianqi-v1。曲式同 v1: Intro8-A16-Pre4-B8-Post4-A16-Pre4-B8-Riff4-Break12-B3(+1)8-B3'(+1)8-Outro(+1)8
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260929)
BPM = 150
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '04_电气花火_BiriBiri风_complete.mid')
OUT_VOCAL = os.path.join(HERE, 'vocal_lead.mid')

p = Piece('电气花火 v2 (BiriBiri风格致敬)', BPM, key='A')
lead = p.add(Trk('Lead Vocal', 81, 3, vol=112, pan=64, reverb=40))
dbl = p.add(Trk('Lead Double', 80, 4, vol=64, pan=64, reverb=32))
glock = p.add(Trk('Glockenspiel', 9, 5, vol=80, pan=80, reverb=62))
piaL = p.add(Trk('Piano Drive L', 0, 0, vol=94, pan=46, reverb=42))
piaR = p.add(Trk('Piano Drive R', 0, 1, vol=88, pan=82, reverb=42))
ep = p.add(Trk('E.Piano', 4, 2, vol=84, pan=44, reverb=42))
arp = p.add(Trk('Arp Synth', 81, 6, vol=62, pan=84, reverb=36))
rgt = p.add(Trk('Riff Guitar', 29, 1, vol=92, pan=36, reverb=26))
bass = p.add(Trk('Slap Bass', 33, 7, vol=106, pan=64, reverb=12))
pad = p.add(Trk('Warm Pad', 89, 8, vol=58, pan=64, reverb=66))
dr = p.add(Drums(vol=108))

A16 = ['F#m7', 'Dmaj7', 'A', 'E'] * 4
PRE = ['Dmaj7', 'E', 'F#m7', 'E']
B8 = ['A', 'E', 'F#m7', 'D'] * 2
BRK = ['F#m7', 'E', 'Dmaj7', 'C#m7'] * 3
INTRO = ['A', 'A', 'F#m7', 'D'] * 2

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
# 终副歌对旋律 (填在钩子长音的空拍上)
COUNTER = [
    (0, 2.0, 0.5, 'C#6', 74), (0, 2.5, 0.5, 'B5', 70), (0, 3.0, 1, 'A5', 76),
    (1, 2.0, 0.5, 'E5', 70), (1, 2.5, 0.5, 'F#5', 72), (1, 3.0, 1, 'G#5', 76),
    (2, 2.0, 0.5, 'A5', 74), (2, 2.5, 0.5, 'G#5', 70), (2, 3.0, 1, 'F#5', 76),
    (3, 2.0, 0.5, 'E5', 72), (3, 2.5, 0.5, 'F#5', 74), (3, 3.0, 1, 'D5', 76),
    (4, 2.0, 0.5, 'C#6', 74), (4, 2.5, 0.5, 'B5', 70), (4, 3.0, 1, 'A5', 76),
    (5, 2.0, 0.5, 'E5', 70), (5, 2.5, 0.5, 'F#5', 72), (5, 3.0, 1, 'G#5', 76),
    (6, 2.0, 0.5, 'A5', 74), (6, 2.5, 0.5, 'B5', 76), (6, 3.0, 1, 'C#6', 78),
    (7, 2.0, 0.5, 'D6', 78), (7, 2.5, 0.5, 'C#6', 74), (7, 3.0, 2, 'B5', 80),
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


# ---------------- v2 层次构件 ----------------
def drum_v2(dr, b, style, rng, i=0, fill=False):
    def v(x):
        return x
    if style == 'verse':
        dr.hits(b, [(0, 36, v(100)), (1.5, 36, v(84)), (2.5, 36, v(94)),
                    (1, 39, v(84)), (3, 39, v(86)), (2.75, 38, v(28))])
        cont = [90, 42, 64, 42] if i % 2 == 0 else [90, 44, 74, 48]
        dr.hits(b, [(k * 0.25, 42, v(cont[k % 4] - (14 if k >= 8 else 0))) for k in range(16)])
        if i % 4 == 3:
            dr.hits(b, [(3.5, 46, v(74))])
        else:
            dr.hits(b, [(3.5, 42, v(56))])
        if fill:
            dr.hits(b, [(3, 38, v(96)), (3.25, 38, v(104)), (3.5, 45, v(112)), (3.75, 43, v(116))])
    elif style == 'chorus':
        dr.hits(b, [(0, 36, v(112)), (1, 36, v(100)), (2, 36, v(108)), (3, 36, v(104)),
                    (1, 39, v(104)), (1, 38, v(92)), (3, 39, v(106)), (3, 38, v(94))])
        dr.hits(b, [(k * 0.5, 42, v(90 if k % 2 == 0 else 66)) for k in range(8)])
        oh = 74 if i % 2 == 0 else 82
        dr.hits(b, [(0.5, 46, v(oh)), (1.5, 46, v(oh)), (2.5, 46, v(oh)), (3.5, 46, v(oh))])
        if i % 4 == 2:
            dr.hits(b, [(2.75, 38, v(34)), (3.625, 38, v(38))])
        if fill:
            dr.hits(b, [(3, 38, v(106)), (3.25, 38, v(112)), (3.5, 45, v(118)), (3.75, 43, v(122))])
    elif style == 'riser':
        dr.hits(b, [(k * 0.25, 42, min(118, 46 + k * 5)) for k in range(16)])
        dr.hits(b, [(k * 0.25, 38, min(126, 60 + (k - 8) * 9)) for k in range(8, 16)])
        dr.hits(b, [(0, 36, v(96))])
    elif style == 'break':
        dr.hits(b, [(0, 36, v(88)), (2, 38, v(86)), (1, 42, v(44)), (3, 42, v(44)),
                    (1.75, 38, v(26)), (3.5, 39, v(56))])
    elif style == 'heartbeat':
        dr.hits(b, [(0, 36, v(74)), (2, 36, v(66))] +
                [(k * 0.5, 42, v(38 if k % 2 == 0 else 28)) for k in range(8)])


def pad_pump(trk, b, chord, rng, vel=42, n=4, low=55, high=71):
    """侧链泵感: 重拍压低、反拍回弹"""
    tones = chord.voice(low=low, high=high, n=n)
    trk.chord(b, 1.4, tones, hum(rng, vel - 10, 2))
    trk.chord(b + 1.5, 0.4, tones, hum(rng, vel + 6, 2))
    trk.chord(b + 2, 1.4, tones, hum(rng, vel - 6, 2))
    trk.chord(b + 3.5, 0.4, tones, hum(rng, vel + 8, 2))


def glock_interlock(trk, b, chord, rng):
    """钟琴答句: 钩子长音的空拍上插下行 8 分"""
    tones = sorted(chord.voice(low=79, high=95, n=4), reverse=True)
    spec = [(1.5, 0, 66), (2.0, 1, 70), (2.5, 2, 66), (3.5, 3, 60)]
    for bt, idx, v in spec:
        trk.n(b + bt, 0.45, tones[idx % len(tones)], hum(rng, v, 3))


def bass_v2(trk, b, chord, rng, vel=92, sub=True, slide=False):
    """反拍 8 分 + sub 低八度层 + 落头滑音"""
    r = chord.bass_midi(2)
    if slide:
        trk.bend(b, -140)
        trk.bend(b + 0.12, 0)
    trk.n(b, 0.42, r, hum(rng, vel - 12))
    if sub:
        trk.n(b, 1.8, r - 12, hum(rng, vel - 26, 2))
    for k in range(4):
        trk.n(b + 0.5 + k, 0.34, r + (12 if k == 2 else 0), hum(rng, vel))


def piano_v2(trkL, trkR, b, chord, rng, vel=88):
    """双钢琴位驱动 16 分, 第三拍后半留缝 (律动气口)"""
    tones = chord.voice(low=60, high=84, n=4)
    patL = [i % len(tones) for i in (0, 1, 2, 3, 2, 3, 1, 2)]
    patR = [i % len(tones) for i in (3, 2, 1, 0, 1, 0, 2, 1)]
    for k in range(8):
        if k == 7:      # 气口
            continue
        trkL.n(b + k * 0.5, 0.24, tones[patL[k]], hum(rng, vel - (12 if k % 2 else 0)))
    for k in range(8):
        if k in (3, 7):
            continue
        trkR.n(b + 0.25 + k * 0.5, 0.22, tones[patR[k]], hum(rng, vel - 22))


def arp_v2(trk, b, chord, rng, i=0, vel=54, up=False):
    tones = chord.voice(low=76 if up else 64, high=100 if up else 84, n=4)
    base = (0, 1, 2, 3, 1, 2, 3, 2) if i % 2 == 0 else (0, 2, 1, 3, 2, 3, 1, 2)
    pat = [k % len(tones) for k in base]
    for k, idx in enumerate(pat):
        trk.n(b + k * 0.25, 0.2, tones[idx], hum(rng, vel - (10 if k % 4 == 0 else 0), 3))


def play_riff(rgt, dbl, b, rr, rng, dbl_on=False):
    for _rb, bt, rd, rn, rv in rr:
        rgt.n(b + bt, rd, npitch(rn), hum(rng, rv))
        if dbl_on:
            dbl.n(b + bt, rd, npitch(rn) - 12, hum(rng, rv - 34, 3))


# ---------------- 段落装配 ----------------
t0 = 0.0
for si, (name, chords_raw, st) in enumerate(SECS := [
        ('Intro', INTRO, 0), ('A1', A16, 0), ('Pre', PRE, 0), ('B1', B8, 0),
        ('Post', ['A', 'A', 'F#m7', 'D'], 0),
        ('A2', A16, 0), ('Pre', PRE, 0), ('B2', B8, 0),
        ('Riff', ['A', 'A', 'F#m7', 'D'], 0),
        ('Break', BRK, 0),
        ('B3', B8, 1), ('B3x', B8, 1),
        ('Outro', B8, 1)]):
    cs = [Chord(c).shifted(st) for c in chords_raw]
    nbars = len(cs)
    start = t0
    full_chorus = name in ('B1', 'B2', 'B3', 'B3x')
    for i, c in enumerate(cs):
        b = start + i * 4
        if name == 'Intro':
            pad_pump(pad, b, c, rng, vel=36 if i < 4 else 42)
            if i < 4:
                if i >= 2:
                    drum_v2(dr, b, 'heartbeat', rng, i=i)
            else:
                rr = shift_riff(RIFF[:12] if i % 2 == 0 else RIFF[12:], st)
                play_riff(rgt, dbl, b, rr, rng)
                bass_offbeat8(bass, b, c, rng, vel=74)
                drum_v2(dr, b, 'verse', rng, i=i)
        elif name in ('A1', 'A2'):
            bass_funk16(bass, b, c, cs[(i + 1) % nbars], rng, vel=90)
            ep_stabs(ep, b, c, rng, beats=((1.5, 0.75, 58), (3.5, 0.5, 56)), n=3)
            pad_pump(pad, b, c, rng, vel=30, n=3, low=52, high=68)
            drum_v2(dr, b, 'verse', rng, i=i, fill=(i == nbars - 1))
            if name == 'A2':
                arp_v2(arp, b, c, rng, i=i, vel=52)
                for k in range(4):
                    rgt.n(b + 0.5 + k, 0.18, c.voice(low=55, high=70, n=2)[k % 2],
                          hum(rng, 60 if k % 2 == 0 else 44))
        elif name == 'Pre':
            arp_v2(arp, b, c, rng, i=i, vel=58, up=(i >= 2))
            if i < 3:
                bass_offbeat8(bass, b, c, rng, vel=84)
            ep_stabs(ep, b, c, rng, beats=((0, 0.75, 62), (2, 0.75, 60), (2.75, 0.5, 58)), n=4)
            pad_pump(pad, b, c, rng, vel=36, n=3)
            if i < 3:
                drum_v2(dr, b, 'verse', rng, i=i + 1)
            else:
                drum_v2(dr, b, 'riser', rng)   # 末小节滚奏抽空
        elif full_chorus:
            piano_v2(piaL, piaR, b, c, rng, vel=88)
            arp_v2(arp, b, c, rng, i=i, vel=56, up=(i >= 4))
            bass_v2(bass, b, c, rng, vel=92, slide=(i % 2 == 0))
            ep.chord(b + 0.5, 0.3, c.voice(low=64, high=80, n=3), hum(rng, 44))
            pad_pump(pad, b, c, rng, vel=34)
            if name != 'B3x' and not (name == 'B2' and i >= 4):
                glock_interlock(glock, b, c, rng)
            drum_v2(dr, b, 'chorus', rng, i=i, fill=(i == nbars - 1))
            if i == 0:
                crash(dr, b, vel=98)
        elif name in ('Post', 'Riff'):
            rr = shift_riff(RIFF[:12] if i % 2 == 0 else RIFF[12:], st)
            play_riff(rgt, dbl, b, rr, rng, dbl_on=(name == 'Riff'))
            bass_offbeat8(bass, b, c, rng, vel=86)
            drum_v2(dr, b, 'verse', rng, i=i, fill=(i == 3))
        elif name == 'Break':
            pad_pump(pad, b, c, rng, vel=44, n=4, low=55, high=73)
            if i < 8:
                ep.chord(b, 3.6, c.voice(low=58, high=76, n=4), hum(rng, 50))
                if i % 2 == 0:
                    bass.n(b, 3.6, c.bass_midi(2), hum(rng, 74))
                drum_v2(dr, b, 'break', rng)
            elif i < 11:
                arp_v2(arp, b, c, rng, i=i, vel=min(70, 48 + (i - 8) * 8), up=(i >= 10))
                bass_offbeat8(bass, b, c, rng, vel=78)
                drum_v2(dr, b, 'riser', rng)
            # i==11: 只留旋律爬音, 全队抽空等 drop
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
        if name == 'B2':
            half = [(bb - 4, bt, d, pp, v) for (bb, bt, d, pp, v) in MEL_B if bb >= 4]
            glock.phrase(start + 16, soft(half, 0.62), tr=st + 12)
        if name == 'B3x':
            glock.phrase(start, soft(COUNTER, 0.9), tr=st)
    elif name == 'Break':
        lead.phrase(start, MEL_BRK)
    elif name == 'Intro':
        lead.phrase(start, soft([e for e in MEL_B if e[0] in (0, 1)], 0.78))
        glock.phrase(start + 8, soft([e for e in MEL_B if e[0] in (0, 1)], 0.6), tr=12)
    elif name == 'Outro':
        lead.phrase(start, soft(MEL_B, 0.72), tr=st)
        half = [(bb - 4, bt, d, pp, v) for (bb, bt, d, pp, v) in MEL_B if bb >= 4]
        glock.phrase(start + 16, soft(half, 0.5), tr=st + 12)
    t0 = start + nbars * 4

# 收束: 副歌开头与最后一小节全乐队 hit
for sect in (t0 - 32, t0 - 4):
    crash(dr, sect, vel=90)
    stab = Chord('A').shifted(1)
    piaL.chord(sect, 3.6, stab.voice(low=58, high=78, n=4), 84)
    bass.n(sect, 3.6, stab.bass_midi(2), 96)
    dr.hits(sect, [(0, 36, 112), (0, 39, 100)])

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s  sections={len(SECS)}')
for trk in p.tracks:
    print(f'  {trk.name:14s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
p.save(OUT)
print('saved:', os.path.abspath(OUT))

vp = Piece('电气花火 v2 vocal lead (for OpenUTAU/SynthV)', BPM, key='A')
vt = vp.add(Trk('Lead Vocal', 0, 0, vol=100, reverb=30))
vt.events = list(lead.events)
vp.save(OUT_VOCAL)
print('saved:', os.path.abspath(OUT_VOCAL), f'({len(vt.events)} notes)')
