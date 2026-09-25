# -*- coding: utf-8 -*-
"""02「きみと春めき」(原名 终将成春) v4 —— 层次感/密度/动漫感升级版
在 v2 作曲骨架上加四层 (人声仍由 NEUTRINO 提供, 不写入本 MIDI):
  strings  ch4  弦乐组 prog48: 主歌低音持续 / 预副歌上行 swell / 副歌高声部叠唱 / Break 与人声同度齐奏
  bells    ch5  钟琴   prog9:  前奏音乐盒 hook 预告+与人声齐奏 / 副歌每小节第1拍高光 / Outro 回声
  obligo   ch10 回调合成 prog81: 人声 4 小节乐句后以高八度片段回应 (ZUTOMAYO 式 oblique)
  arp      ch11 琶音   prog80: 副歌 16 分琶音密度层
其余 riff/bass/ep/mute/stab/pad/drums 与 v2 完全一致 (RNG 同种子)。
输出: 02_..._v4.mid (不含 lead/harm GM 轨)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260926)   # 与 v2 同种子 -> 基础轨 humanization 完全一致
BPM = 142
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = HERE

p = Piece('きみと春めき (ずとまよ风格致敬 vocal v4)', BPM, key='F#m')
rgt = p.add(Trk('Riff Guitar', 29, 0, vol=96, pan=36, reverb=26))
bass = p.add(Trk('Slap Bass', 33, 1, vol=104, pan=64, reverb=12))
ep = p.add(Trk('E.Piano', 4, 2, vol=88, pan=44, reverb=46))
mgt = p.add(Trk('Mute Guitar', 27, 3, vol=76, pan=84, reverb=30))
strings = p.add(Trk('Strings', 48, 4, vol=46, pan=64, reverb=56))
bells = p.add(Trk('Bells', 9, 5, vol=52, pan=52, reverb=64))
sq = p.add(Trk('Synth Stab', 81, 6, vol=56, pan=76, reverb=30))
pad = p.add(Trk('Warm Pad', 89, 7, vol=52, pan=64, reverb=64))
obligo = p.add(Trk('Obligo Synth', 81, 10, vol=44, pan=30, reverb=40))
arp = p.add(Trk('Arp Synth', 80, 11, vol=34, pan=88, reverb=34))
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


def shift_riff(events, st):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    out = []
    for b, bt, d, nm, v in events:
        m = npitch(nm) + st
        pc, oc = m % 12, m // 12 - 1
        out.append((b, bt, d, names[pc] + str(oc), v))
    return out


# ---- 人声旋律引用 (仅用于 oblique 回应与 Break 齐奏; 不写轨) ----
V_C_A = [(0, 0.0, 0.5, 'E5', 92), (0, 0.5, 0.5, 'E5', 90), (0, 1.0, 1.0, 'E5', 94),
         (0, 2.0, 1.0, 'D5', 90), (0, 3.0, 1.0, 'C#5', 88),
         (1, 0.0, 1.5, 'D5', 92), (1, 1.5, 0.5, 'D5', 84)]
V_C_B = [(2, 0.0, 0.5, 'C#5', 90), (2, 0.5, 0.5, 'C#5', 88), (2, 1.0, 1.0, 'C#5', 92),
         (2, 2.0, 1.0, 'B4', 88), (2, 3.0, 1.0, 'A4', 86),
         (3, 0.0, 1.5, 'B4', 90), (3, 1.5, 0.5, 'B4', 82)]
V_BRK_A = [(0, 0, 1.5, 'A4', 82), (0, 1.5, 0.5, 'B4', 80), (0, 2, 2, 'C#5', 84),
           (1, 0, 1, 'B4', 82), (1, 1, 1, 'A4', 82), (1, 2, 2, 'F#4', 84),
           (2, 0, 1, 'E4', 80), (2, 1, 1, 'F#4', 82), (2, 2, 1.5, 'A4', 84),
           (2, 3.5, 0.5, 'B4', 82), (3, 0, 3, 'C#5', 86)]
HOOK = [(0, 0.0, 0.5, 'E5', 92), (0, 0.5, 0.5, 'E5', 90), (0, 1.0, 1.0, 'E5', 94),
        (0, 2.0, 1.0, 'D5', 90), (0, 3.0, 1.0, 'C#5', 88), (1, 0.0, 2.0, 'D5', 92)]


def sing(trk, sec_start, evts, tr=0, vel_scale=1.0, oct_shift=0):
    for b, bt, d, p, v in evts:
        m = npitch(p) + tr + oct_shift * 12
        trk.n(sec_start + b * 4 + bt, d, m, int(min(127, v * vel_scale)))


# ---------------- 装配 ----------------
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
                stab = c.voice(low=55, high=78, n=4)
                bass.n(b, 1.8, c.bass_midi(2), 108)
                rgt.chord(b, 1.5, [p2 + 12 for p2 in c.voice(low=55, high=68, n=3)], 92)
                ep.chord(b, 1.5, stab, 84)
                strings.chord(b, 1.5, c.voice(low=52, high=70, n=4), 88)
                bells.n(b, 2.0, npitch('C#6') + tr, 90)
                bells.n(b + 0.5, 1.5, npitch('F#6') + tr, 74)
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
            # --- v4 新层: riff 段的铃声点缀 (小节头 1 拍高光) ---
            if name in ('ITL', 'Outro'):
                bells.n(b, 0.8, c.voice(low=74, high=88, n=1)[0] + 12, hum(rng, 58))
            # ITL 弦乐持续铺底
            if name == 'ITL':
                strings.chord(b, 3.9, c.voice(low=50, high=66, n=3), hum(rng, 36))
        else:
            if name in ('V1', 'V2'):
                ep_stabs(ep, b, c, rng, beats=((1.5, 0.75, 56), (3.5, 0.5, 54)), n=3)
                gt_skank16(mgt, b, c, rng, vel_hi=62)
                bass_funk16(bass, b, c, nxt_of(i), rng, vel=88)
                pad.chord(b, 3.8, c.voice(low=52, high=68, n=3), hum(rng, 34))
                # v4: 主歌弦乐低音持续 (大提琴区)
                strings.chord(b, 3.85, [c.bass_midi(3), c.bass_midi(3) + 7], hum(rng, 34))
                drum_bar(dr, b, 'z_verse', rng, fill=(i == nbars - 1))
            elif name == 'Pre':
                ep_stabs(ep, b, c, rng, beats=((0, 0.75, 60), (2, 0.75, 58), (2.75, 0.5, 56)), n=4)
                gt_skank16(mgt, b, c, rng, vel_hi=66)
                bass_funk16(bass, b, c, nxt_of(i), rng, vel=90)
                # v4: 预副歌弦乐上行 swell (每小节一个高音二声部)
                sv = c.voice(low=57, high=74, n=2)
                strings.chord(b, 3.9, sv, hum(rng, 40 + i * 2))
                bells.n(b, 0.5, sv[-1] + 12, hum(rng, 40))
                drum_bar(dr, b, 'z_pre' if i < 7 else 'z_build', rng)
            elif name in ('C1', 'C2', 'C3'):
                ep_stabs(ep, b, c, rng)
                gt_doublestop8(mgt, b, c, rng, vel=72)
                sq.chord(b + 0.5, 0.3, c.voice(low=63, high=80, n=3), hum(rng, 40))
                bass_funk16(bass, b, c, nxt_of(i), rng, vel=94)
                pad.chord(b, 3.8, c.voice(low=55, high=71, n=4), hum(rng, 38))
                # v4: 副歌弦乐高声部叠唱 (与人声和声层呼应)
                strings.chord(b, 3.85, c.voice(low=62, high=78, n=3), hum(rng, 40))
                # v4: 16 分琶音密度层
                synth_arp16(arp, b, c, rng, vel=46)
                # v4: 钟琴小节头高光 + 句尾闪烁
                bells.n(b, 0.6, c.voice(low=76, high=90, n=1)[0], hum(rng, 56))
                bells.n(b + 3.5, 0.3, c.voice(low=76, high=90, n=1)[0] + 2, hum(rng, 40))
                drum_bar(dr, b, 'z_chorus', rng, fill=(i == nbars - 1))
                if i == 0:
                    crash(dr, b, vel=96 if name != 'C3' else 88)
            elif name == 'Break':
                if i < 12:
                    ep.chord(b, 3.6, c.voice(low=56, high=76, n=4), hum(rng, 46))
                    bass_folk(bass, b, c, rng, vel=64)
                    # v4: Break 弦乐 = 和声长音 (气声段的温暖支撑)
                    strings.chord(b, 3.9, c.voice(low=53, high=69, n=3), hum(rng, 34))
                    drum_bar(dr, b, 'z_break', rng)
                elif i < 14:
                    gt_skank16(mgt, b, c, rng, vel_hi=58)
                    bass_funk16(bass, b, c, nxt_of(i), rng, vel=86)
                    drum_bar(dr, b, 'z_verse', rng)
                else:
                    # v4: build 加钟琴滚奏上行
                    for k in range(8):
                        bells.n(b + k * 0.5, 0.3, npitch('C5') + tr + k, hum(rng, 40 + k * 6))
                    drum_bar(dr, b, 'z_build', rng)

    if name == 'C3':
        crash(dr, start, vel=100, note=57)

    # ---- v4 层: oblique 回应 (人声句后高八度尾迹) / Break 齐奏 ----
    if name in ('C1', 'C2'):
        for k, ph in enumerate((V_C_A, V_C_B)):
            sing(obligo, start, ph[-3:], tr=tr, vel_scale=0.62, oct_shift=1)
    elif name == 'C3':
        sing(obligo, start, V_C_A[-3:], tr=tr, vel_scale=0.62, oct_shift=1)
        sing(obligo, start, V_C_B[-3:], tr=tr, vel_scale=0.62, oct_shift=1)
    elif name in ('V1', 'V2'):
        # 8 小节器乐尾段: bells + obligo 合奏 hook 缩影
        sing(bells, start + 8 * 4, HOOK[:4], tr=tr, vel_scale=0.55)
        sing(obligo, start + 12 * 4, HOOK[3:], tr=tr, vel_scale=0.55, oct_shift=1)
    elif name == 'Break':
        # 人声同度齐奏 (弦乐层, 动漫式 soaring)
        sing(strings, start, V_BRK_A, tr=tr, vel_scale=0.5)
        sing(strings, start, [(b + 12, bt, d, p, v) for (b, bt, d, p, v) in V_BRK_A[:6]],
             tr=tr, vel_scale=0.5)
    elif name == 'Intro':
        # i1-2: 音乐盒 hook 预告 (与 NEUTRINO 人声 bar4-5 预告呼应)
        sing(bells, start, [(b + 16, bt, d, p, v) for (b, bt, d, p, v) in HOOK],
             tr=tr, vel_scale=0.5)
    t0 = start + nbars * 4

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s')
for trk in p.tracks:
    print(f'  {trk.name:12s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')
base = os.path.join(OUTDIR, '02_终将成春_真夜中风')
p.save(base + '_v4.mid')
print('saved:', base + '_v4.mid')
