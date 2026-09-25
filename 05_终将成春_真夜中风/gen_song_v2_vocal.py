# -*- coding: utf-8 -*-
"""02「终将成春」v2 —— 人声版改编
v1 (song2_yagate_haru.py) 伴奏原样保留；主旋律按女声重写：
  - 音域 F#4~E5 (tag 顶点 F#5), 去掉 v1 的 C#5~G#5 顶部盘旋
  - hook = 同音三连 E5-E5-E5 + 级进下落 D5-C#5-D5 (副歌句1), 模进句2
  - 乐句 <= 4 小节, 句间留 >= 1 拍呼吸口
  - C 段加三度和声轨 harm; Break 保留 chromatic 冲刺但封顶 F#5 一瞬
日语歌词 (ZUTOMAYO 风 × 终将成为你), 一音一字直接内嵌在 sing() 事件里
输出: 02_..._v2.mid / 02_..._vocal_main.mid / _vocal_harm.mid / 两个 .musicxml
"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260926)
BPM = 142
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = HERE

p = Piece('终将成春 v2 (ずとまよ风格致敬 vocal版)', BPM, key='F#m')
rgt = p.add(Trk('Riff Guitar', 29, 0, vol=96, pan=36, reverb=26))
bass = p.add(Trk('Slap Bass', 33, 1, vol=104, pan=64, reverb=12))
ep = p.add(Trk('E.Piano', 4, 2, vol=88, pan=44, reverb=46))
mgt = p.add(Trk('Mute Guitar', 27, 3, vol=76, pan=84, reverb=30))
vmain = p.add(Trk('Lead Vocal', 53, 4, vol=46, pan=68, reverb=34))
harm = p.add(Trk('Harm Vocal', 53, 5, vol=40, pan=48, reverb=40))
sq = p.add(Trk('Synth Stab', 81, 6, vol=56, pan=76, reverb=30))
pad = p.add(Trk('Warm Pad', 89, 7, vol=52, pan=64, reverb=64))
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


# ================= 人声旋律 (v2) =================
# 事件: (bar, beat, dur, pitch, vel, mora)  mora=None 表示纯唱「ラ」由合成器分句时给
V_INTRO = [   # m4-5: hook 雏形预告 (前 4 小节器乐, XML 里写 rest)
    (4, 0.0, 0.5, 'E5', 86, 'ら'), (4, 0.5, 0.5, 'E5', 84, 'ら'), (4, 1.0, 1.0, 'E5', 88, 'ら'),
    (4, 2.0, 1.0, 'D5', 86, 'ら'), (4, 3.0, 1.0, 'C#5', 84, 'ら'),
    (5, 0.0, 2.0, 'D5', 86, 'ら'),
]
V_V1_A = [  # 「まちがいだらけの」
    (0, 3.5, 0.25, 'A4', 84, 'ま'), (0, 3.75, 0.25, 'B4', 82, 'ち'),
    (1, 0.0, 0.5, 'A4', 88, 'が'), (1, 0.5, 0.25, 'C#5', 86, 'い'), (1, 0.75, 0.25, 'B4', 82, 'だ'),
    (1, 1.0, 0.5, 'A4', 86, 'ら'), (1, 1.5, 0.25, 'G#4', 80, 'け'), (1, 1.75, 0.25, 'A4', 82, 'の'),
    (1, 2.0, 1.5, 'F#4', 86, 'ー'),
]
V_V1_B = [  # 「よなきはつづくの」
    (0, 3.5, 0.25, 'A4', 84, 'よ'), (0, 3.75, 0.25, 'B4', 82, 'な'),
    (1, 0.0, 0.5, 'C#5', 88, 'き'), (1, 0.5, 0.25, 'D5', 86, 'は'), (1, 0.75, 0.25, 'C#5', 82, 'つ'),
    (1, 1.0, 0.5, 'B4', 86, 'づ'), (1, 1.5, 0.25, 'A4', 80, 'く'), (1, 1.75, 0.25, 'B4', 82, 'の'),
    (1, 2.0, 1.5, 'G#4', 86, 'ー'),
]
V_V1_C = [  # 「きみのこよみのなか」
    (0, 3.5, 0.25, 'C#5', 86, 'き'), (0, 3.75, 0.25, 'B4', 82, 'み'),
    (1, 0.0, 0.5, 'A4', 88, 'の'), (1, 0.5, 0.25, 'B4', 84, 'こ'), (1, 0.75, 0.25, 'C#5', 86, 'よ'),
    (1, 1.0, 0.5, 'D5', 88, 'み'), (1, 1.5, 0.25, 'C#5', 84, 'の'), (1, 1.75, 0.25, 'B4', 82, 'な'),
    (1, 2.0, 1.5, 'A4', 88, 'か'),
]
V_V1_D = [  # 「きみにあいにいくよ」
    (0, 3.5, 0.25, 'A4', 84, 'き'), (0, 3.75, 0.25, 'G#4', 80, 'み'),
    (1, 0.0, 0.5, 'F#4', 86, 'に'), (1, 0.5, 0.25, 'G#4', 82, 'あ'), (1, 0.75, 0.25, 'A4', 84, 'い'),
    (1, 1.0, 0.5, 'B4', 86, 'に'), (1, 1.5, 0.25, 'B4', 82, 'い'), (1, 1.75, 0.5, 'C#5', 86, 'く'),
    (1, 2.25, 1.25, 'C#5', 90, 'よ'),
]
V_PRE_A = [  # 「かさもささげずに」
    (0, 0, 1, 'B4', 84, 'か'), (0, 1, 1, 'C#5', 86, 'さ'), (0, 2, 1, 'D5', 88, 'も'),
    (0, 3, 0.5, 'C#5', 84, 'さ'), (0, 3.5, 0.5, 'D5', 84, 'さ'),
    (1, 0, 1.5, 'E5', 90, 'げ'), (1, 1.5, 0.5, 'C#5', 82, 'ず'),
    (1, 2, 2, 'B4', 86, 'に'),
]
V_PRE_B = [  # 「はるはまってないから」
    (2, 0, 1, 'A4', 84, 'は'), (2, 1, 1, 'B4', 86, 'る'), (2, 2, 1, 'C#5', 88, 'は'),
    (2, 3, 0.5, 'D5', 86, 'ま'), (2, 3.5, 0.5, 'C#5', 84, 'っ'),
    (3, 0, 1.5, 'D5', 88, 'て'), (3, 1.5, 0.5, 'E5', 86, 'な'),
    (3, 2, 2, 'E5', 92, 'から'),
]
V_C_A = [  # hook 句1「やがてはるになる」 同音三连 + 级进下落
    (0, 0.0, 0.5, 'E5', 92, 'や'), (0, 0.5, 0.5, 'E5', 90, 'が'), (0, 1.0, 1.0, 'E5', 94, 'て'),
    (0, 2.0, 1.0, 'D5', 90, 'は'), (0, 3.0, 1.0, 'C#5', 88, 'る'),
    (1, 0.0, 1.5, 'D5', 92, 'に'), (1, 1.5, 0.5, 'D5', 84, 'る'),
]
V_C_B = [  # hook 句2「きみとはるになる」 模进
    (2, 0.0, 0.5, 'C#5', 90, 'き'), (2, 0.5, 0.5, 'C#5', 88, 'み'), (2, 1.0, 1.0, 'C#5', 92, 'と'),
    (2, 2.0, 1.0, 'B4', 88, 'は'), (2, 3.0, 1.0, 'A4', 86, 'る'),
    (3, 0.0, 1.5, 'B4', 90, 'に'), (3, 1.5, 0.5, 'B4', 82, 'る'),
]
V_C_C = [  # 句3「こわくないよふたりなら」 上行爆发
    (4, 0.0, 0.5, 'A4', 86, 'こ'), (4, 0.5, 0.5, 'B4', 86, 'わ'),
    (4, 1.0, 0.5, 'C#5', 88, 'く'), (4, 1.5, 0.5, 'D5', 88, 'な'),
    (4, 2.0, 1.0, 'E5', 94, 'い'), (4, 3.0, 1.0, 'D5', 88, 'よ'),
    (5, 0.0, 1.0, 'C#5', 90, 'ふ'), (5, 1.0, 1.0, 'B4', 88, 'た'),
    (5, 2.0, 0.75, 'A4', 90, 'り'), (5, 2.75, 0.5, 'C#5', 86, 'な'), (5, 3.25, 0.75, 'A4', 88, 'ら'),
]
V_C_D = [  # 句4「そのこころがすき」 点题句
    (6, 0.0, 0.5, 'E5', 92, 'そ'), (6, 0.5, 0.5, 'D5', 88, 'の'),
    (6, 1.0, 1.0, 'C#5', 92, 'こ'), (6, 2.0, 0.5, 'B4', 88, 'こ'), (6, 2.5, 0.5, 'A4', 86, 'ろ'),
    (6, 3.0, 1.0, 'B4', 90, 'が'),
    (7, 0.0, 1.5, 'C#5', 94, 'す'), (7, 1.5, 0.5, 'B4', 86, 'き'),
    (7, 2.0, 2.0, 'A4', 90, 'ー'),
]
V_ADLIB = [  # C2 末 (m75 后 2 拍) 下行装饰
    (0, 2.0, 0.5, 'E5', 92, 'ら'), (0, 2.5, 0.5, 'D5', 88, 'ら'),
    (0, 3.0, 0.5, 'C#5', 90, 'ら'), (0, 3.5, 0.5, 'B4', 86, 'ら'),
]
V_BRK_A = [  # 「くちなしのにおいのばしょで」
    (0, 0, 1.5, 'A4', 82, 'く'), (0, 1.5, 0.5, 'B4', 80, 'ち'), (0, 2, 2, 'C#5', 84, 'なし'),
    (1, 0, 1, 'B4', 82, 'の'), (1, 1, 1, 'A4', 82, 'に'), (1, 2, 2, 'F#4', 84, 'おい'),
    (2, 0, 1, 'E4', 80, 'の'), (2, 1, 1, 'F#4', 82, 'ば'), (2, 2, 1.5, 'A4', 84, 'しょ'),
    (2, 3.5, 0.5, 'B4', 82, 'で'),
    (3, 0, 3, 'C#5', 86, 'ー'),
]
V_BRK_B = [  # 「かくせないこのきもちたち」
    (4, 0, 1.5, 'C#5', 84, 'か'), (4, 1.5, 0.5, 'D5', 82, 'く'), (4, 2, 2, 'E5', 88, 'せ'),
    (5, 0, 1, 'D#5', 84, 'な'), (5, 1, 1, 'C#5', 84, 'い'), (5, 2, 2, 'B4', 86, 'この'),
    (6, 0, 1, 'A4', 84, 'き'), (6, 1, 1, 'G#4', 82, 'も'), (6, 2, 1, 'F#4', 84, 'ち'),
    (6, 3, 1, 'G#4', 82, 'た'),
    (7, 0, 3, 'G#4', 84, 'ち'),
]
V_BRK_C = [  # 「ひかりをかりてゆれていた」
    (8, 0, 1.5, 'A4', 82, 'ひ'), (8, 1.5, 0.5, 'B4', 80, 'か'), (8, 2, 2, 'C#5', 84, 'りを'),
    (9, 0, 1, 'B4', 82, 'か'), (9, 1, 1, 'A4', 82, 'り'), (9, 2, 2, 'F#4', 84, 'て'),
    (10, 0, 1, 'E4', 80, 'ゆ'), (10, 1, 1, 'F#4', 82, 'れ'), (10, 2, 1.5, 'A4', 84, 'て'),
    (10, 3.5, 0.5, 'B4', 82, 'い'),
    (11, 0, 3, 'C#5', 86, 'た'),
]
V_BRK_BUILD = [  # chromatic 冲刺 (m14-15 原样保留, 封顶 F#5 一瞬)
    (12, 0, 2, 'C#5', 86, 'ら'), (12, 2, 1, 'B4', 84, 'ら'), (12, 3, 1, 'C#5', 86, 'ら'),
    (13, 0, 1, 'D5', 88, 'ら'), (13, 1, 1, 'D#5', 88, 'ら'), (13, 2, 2, 'E5', 92, 'ら'),
    (14, 0, 0.5, 'A4', 86, 'ら'), (14, 0.5, 0.5, 'B4', 88, 'ら'), (14, 1.0, 0.5, 'C#5', 90, 'ら'),
    (14, 1.5, 0.5, 'D5', 90, 'ら'), (14, 2.0, 0.5, 'D#5', 92, 'ら'), (14, 2.5, 0.5, 'E5', 94, 'ら'),
    (14, 3.0, 0.5, 'E#5', 96, 'ら'), (14, 3.5, 0.5, 'F#5', 98, 'ら'),
    (15, 0, 2, 'F#5', 100, 'は'), (15, 2, 2, 'E5', 92, 'る'),
]
V_TAG = [  # tag「やがてきみとはる」 未移调音高 (C3 段 sing 时 +2 → B 大调 F#5/D#5/C#5)
    (0, 0, 2, 'E5', 96, 'や'), (0, 2, 2, 'C#5', 90, 'が'),
    (1, 0, 4, 'B4', 94, 'て'),
    (2, 0, 2, 'E5', 96, 'き'), (2, 2, 2, 'D5', 92, 'み'),
    (3, 0, 2, 'C#5', 92, 'と'), (3, 2, 2, 'E5', 98, 'はる'),
]

# 和声 (C 段句1-2 平行下方三度 + Pre 末长音下五度)
sh3 = lambda evs: [(b, bt, d, dn(p, -3), max(70, v - 18), None) for (b, bt, d, p, v, _m) in evs]


def dn(name, semis):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    m = npitch(name) + semis
    return names[m % 12] + str(m // 12 - 1)


def sing(trk, sec_start, evts, tr=0):
    """vocal 事件写入 trk; 返回 [(abs_beat, dur, midi, mora)] 供 XML"""
    out = []
    for b, bt, d, p, v, mora in evts:
        m = npitch(p) + tr
        trk.n(sec_start + b * 4 + bt, d, m, v)
        out.append((sec_start + b * 4 + bt, d, m, mora))
    return out


# ---------------- 装配 ----------------
t0 = 0.0
xml_main = []   # (abs_beat, dur, midi, mora)
xml_harm = []
vocal_done = set()
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

    # ---- 人声 ----
    if name == 'Intro':
        xml_main += sing(vmain, start, V_INTRO)
    elif name in ('V1', 'V2'):
        # 4 句各 2 小节 = 前 8 小节人声, 后 8 小节器乐呼吸段
        # V2 直接复用 V1 旋律, 歌词由下方 LYR_V2 映射阶段替换
        sec = start
        for phrase in (V_V1_A, V_V1_B, V_V1_C, V_V1_D):
            xml_main += sing(vmain, sec, phrase, tr=tr)
            sec += 8
    elif name == 'Pre':
        xml_main += sing(vmain, start, V_PRE_A + V_PRE_B, tr=tr)
        xml_harm += sing(harm, start, [(3, 2, 2, 'B4', 78, None)], tr=tr)
    elif name in ('C1', 'C2'):
        xml_main += sing(vmain, start, V_C_A + V_C_B + V_C_C + V_C_D, tr=tr)
        xml_harm += sing(harm, start, sh3(V_C_A) + sh3(V_C_B), tr=tr)
        if name == 'C2':
            xml_main += sing(vmain, start + 28, V_ADLIB, tr=tr)
    elif name == 'Break':
        xml_main += sing(vmain, start,
                         V_BRK_A + V_BRK_B + V_BRK_C + V_BRK_BUILD, tr=tr)
    elif name == 'C3':
        xml_main += sing(vmain, start, V_C_A + V_C_B + V_C_C + V_C_D + V_TAG, tr=tr)
        xml_harm += sing(harm, start, sh3(V_C_A) + sh3(V_C_B), tr=tr)
    t0 = start + nbars * 4

print(f'bars={int(t0 // 4)}  time={t0 * 60 / BPM:.1f}s')
for trk in p.tracks:
    print(f'  {trk.name:12s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')

# ---- V2 段歌词替换: xml_main 里 V2 区间 (m44-59) 的 mora 换成 V2 词 ----
LYR_V2 = list('よふかしだらけのー'[:9]) + list('こたえはきみのなか') + \
         list('みらいのわたしより') + list('いまをいきていたい')
V2_RANGE = (44 * 4, 60 * 4)
idx = 0
for i, (bt, d, m, mora) in enumerate(xml_main):
    if V2_RANGE[0] <= bt < V2_RANGE[1]:
        if mora is not None:
            xml_main[i] = (bt, d, m, LYR_V2[idx] if idx < len(LYR_V2) else 'ら')
            idx += 1

# ================= 输出 =================
base = os.path.join(OUTDIR, '02_终将成春_真夜中风')
p.save(base + '_v2.mid')
print('saved:', base + '_v2.mid')

# vocal 分轨 (独立 mid 供分轨渲染)
pv = Piece('vocal main', BPM, key='F#m')
tvm = pv.add(Trk('Lead Vocal', 53, 0, vol=100, pan=64, reverb=34))
for bt, d, m, mora in xml_main:
    tvm.n(bt, d, m, 100)
pv.save(base + '_vocal_main.mid')
pv2 = Piece('vocal harm', BPM, key='F#m')
tvh = pv2.add(Trk('Harm Vocal', 53, 0, vol=100, pan=64, reverb=40))
for bt, d, m, mora in xml_harm:
    tvh.n(bt, d, m, 100)
pv2.save(base + '_vocal_harm.mid')
print('saved vocal midi')

# ---- MusicXML (Sinsy) ----
def write_musicxml(path, notes, bpm, total_bars, key_fifths=3):
    DIV = 4  # per quarter
    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" '
         '"http://www.musicxml.org/dtds/partwise.dtd">',
         '<score-partwise version="3.1">',
         '<part-list><score-part id="P1"><part-name>Vocal</part-name></score-part></part-list>',
         '<part id="P1">']
    # 按 bar 组织
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
        items = sorted(by_bar.get(bar, []), key=lambda x: x[0])
        for bt, d, m, mora in items:
            if bt > pos + 1e-6:
                L.append(rest_xml(bt - pos, DIV))
                pos = bt
            names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
            alter = (m % 12) - [0, 2, 4, 5, 7, 9, 11][(m % 12) in (1, 3, 6, 8, 10) and 0 or
                                                     [0, 2, 4, 5, 7, 9, 11].index(m % 12)] if False else 0
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


def pitch_step(midi):
    """转 step/alter/octave, 黑键用升号 (F#m/A/B 均为升号调)"""
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


TOTAL = min(int(t0 // 4), 104)  # Outro 4 小节无人声, XML 到 tag 末为止
write_musicxml(base + '_vocal_main.musicxml', xml_main, BPM, TOTAL)
write_musicxml(base + '_vocal_harm.musicxml',
               [(bt, d, m, 'ら') for bt, d, m, _ in xml_harm], BPM, TOTAL)

# 音域自检
lo = min(m for _, _, m, _ in xml_main); hi = max(m for _, _, m, _ in xml_main)
names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
print(f'vocal main: {len(xml_main)} notes, range {names[lo%12]}{lo//12-1} ~ {names[hi%12]}{hi//12-1} '
      f'({lo}~{hi}), harm {len(xml_harm)} notes')
