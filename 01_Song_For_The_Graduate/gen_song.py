# -*- coding: utf-8 -*-
"""生成《启程的那天》毕业赠礼歌曲 MIDI (C大调, 76BPM, 56小节)
声部: Piano Melody / Piano Arp / Bass / Strings / Bells
"""
import struct

PPQ = 480
BPM = 76
END_BEAT = 224  # 56 小节

V1, V2, CH1, BR, CH2, CH2V, OUT = 16, 48, 80, 112, 128, 160, 192
INT = 0

# 和弦: 名称 -> (贝斯根音, 琶音音符组[根,5,8,10], 弦乐三音组)
CH = {
    'C':  (36, [48, 55, 60, 64], [60, 64, 67]),
    'G':  (43, [43, 50, 55, 59], [59, 62, 67]),
    'Am': (45, [45, 52, 57, 60], [57, 60, 64]),
    'Em': (40, [52, 59, 64, 67], [59, 64, 67]),
    'F':  (41, [41, 48, 53, 57], [57, 60, 65]),
    'Dm': (38, [50, 57, 62, 65], [57, 62, 65]),
}

PROG = {
    INT: ['C', 'G', 'Am', 'G'],
    V1:  ['C', 'G', 'Am', 'Em', 'F', 'C', 'Dm', 'G'],
    V2:  ['C', 'G', 'Am', 'Em', 'F', 'C', 'Dm', 'G'],
    CH1: ['F', 'G', 'Em', 'Am', 'Dm', 'G', 'C', 'C'],
    BR:  ['Am', 'F', 'C', 'G'],
    CH2: ['F', 'G', 'Em', 'Am', 'Dm', 'G', 'C', 'C'],
    CH2V:['F', 'G', 'Em', 'Am', 'Dm', 'G', 'C', 'C'],
    OUT: ['C', 'G', 'Am', 'F', 'C', 'G', 'F', 'C'],
}

melody = []  # (pitch, abs_beat, dur)

def verse(base, m8):
    seq = [(60,0,2),(62,2,1),(64,3,1),(62,4,2),(59,6,2),
           (57,8,1),(60,9,1),(64,10,2),
           (64,12,2),(62,14,2),
           (65,16,1),(64,17,1),(60,18,2),
           (67,20,2),(64,22,1),(67,23,1),
           (69,24,2),(67,26,1),(65,27,1)] + m8
    for p, s, d in seq:
        melody.append((p, base + s, d))

verse(V1, [(67,28,3)])
verse(V2, [(67,28,2),(69,30,1),(71,31,1)])

def chorus(base, variant):
    seq = [(72,0,2),(69,2,1),(72,3,1),
           (71,4,2),(74,6,2),
           (74,8,1.5),(71,9.5,1.5),(67,11,1),
           (69,12,1),(72,13,1),(76,14,2),
           (74,16,2),(72,18,1),(69,19,1),
           (71,20,2),(74,22,1),(71,23,1)]
    if variant == 'normal':
        seq += [(72,24,3),(67,27,1),(64,28,1),(67,29,1),(72,30,2)]
    else:
        seq += [(76,24,2),(74,26,1),(72,27,1),(72,28,4)]
    for p, s, d in seq:
        melody.append((p, base + s, d))

chorus(CH1, 'normal')
chorus(CH2, 'normal')
chorus(CH2V, 'final')

bridge = [(76,0,2),(74,2,2),(72,4,2),(74,6,1),(72,7,1),
          (69,8,1),(67,9,3),(62,12,2),(67,14,2)]
outro  = [(67,0,1.5),(64,1.5,0.5),(67,2,2),(62,4,2),(59,6,2),
          (60,8,2),(64,10,2),
          (65,12,2),(64,14,2),
          (64,16,2),(60,18,2),
          (62,20,2),(59,22,2),
          (60,24,1),(62,25,1),(64,26,1),(65,27,1),
          (64,28,2),(60,30,2)]
for p, s, d in bridge:
    melody.append((p, BR + s, d))
for p, s, d in outro:
    melody.append((p, OUT + s, d))

# ---------- Track builder ----------
def vlq(n):
    b = [n & 0x7F]
    n >>= 7
    while n:
        b.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(b))

class Track:
    def __init__(self, name, ch, program):
        self.name, self.ch, self.program = name, ch, program
        self.events = []

    def note(self, pitch, start, dur, vel):
        vel = max(1, min(127, int(vel)))
        s = int(round(start * PPQ)); e = int(round((start + dur) * PPQ))
        self.events.append((s, 3, bytes([0x90 | self.ch, pitch, vel])))
        self.events.append((e, 1, bytes([0x80 | self.ch, pitch, 0])))

    def render(self, end_beat):
        ev = list(self.events)
        name_b = self.name.encode('ascii', 'replace')
        ev.append((0, 0, bytes([0xFF, 0x03, len(name_b)]) + name_b))
        ev.append((0, 2, bytes([0xC0 | self.ch, self.program])))
        ev.append((int(end_beat * PPQ), 0, bytes([0xFF, 0x2F, 0x00])))
        ev.sort(key=lambda x: (x[0], x[1]))
        data = b''; last = 0
        for tick, _, payload in ev:
            data += vlq(tick - last) + payload
            last = tick
        return b'MTrk' + struct.pack('>I', len(data)) + data

# ---------- 1. Piano Melody ----------
t_mel = Track('Piano Melody', 0, 0)
for p, s, d in melody:
    vel = 96
    if d >= 2: vel += 8
    if s >= CH1: vel += 6
    if s >= CH2V: vel += 4
    t_mel.note(p, s, d, vel)

# ---------- 2. Piano Arp (八分音符琶音) ----------
t_arp = Track('Piano Arp', 1, 0)
IDX = [0, 1, 2, 3, 2, 1, 2, 3]
for sec, bars in PROG.items():
    for i, cname in enumerate(bars):
        bar = sec + i * 4
        notes = CH[cname][1]
        base_vel = 48 if sec == INT else (60 if sec in (V1, V2) else
                   (56 if sec == BR else (68 if sec in (CH1, CH2, CH2V) else 50)))
        if sec == OUT and bar == 220:
            for k, nn in enumerate([48, 55, 60, 64]):  # 结尾柱式和弦(轻微分解)
                t_arp.note(nn, bar + 0.05 * k, 4 - 0.05 * k, 60)
            continue
        for j, idx in enumerate(IDX):
            t_arp.note(notes[idx], bar + 0.5 * j, 0.48, base_vel + (8 if j == 0 else 0))

# ---------- 3. Bass (V2 起) ----------
t_bass = Track('Bass', 2, 33)
for sec in (V2, CH1, BR, CH2, CH2V, OUT):
    bars = PROG[sec]
    vel = 70 if sec == BR else (78 if sec == OUT else 92)
    for i, cname in enumerate(bars):
        bar = sec + i * 4
        root = CH[cname][0]
        if sec == OUT and bar == 220:
            t_bass.note(root, bar, 4, 90)
        else:
            t_bass.note(root, bar, 1.75, vel)
            t_bass.note(root + 7, bar + 2, 1.75, vel - 14)

# ---------- 4. Strings ----------
t_str = Track('Strings', 3, 48)
str_events = [(V2 + 24, 'Dm', 44), (V2 + 28, 'G', 44)]   # V2 尾部渐入
for sec, vel in ((CH1, 48), (BR, 34), (CH2, 48), (CH2V, 52)):
    for i, cname in enumerate(PROG[sec]):
        str_events.append((sec + i * 4, cname, vel))
str_events += [(OUT + 24, 'F', 44), (OUT + 28, 'C', 46)]
for bar, cname, vel in str_events:
    for p in CH[cname][2]:
        t_str.note(p, bar, 3.95, vel)

# ---------- 5. Bells (副歌高八度叠奏) ----------
t_bell = Track('Bells', 4, 9)
for p, s, d in melody:
    if (CH1 <= s < BR) or (CH2 <= s < OUT):
        t_bell.note(p + 12, s, d, 52)

# ---------- 组装文件 ----------
def tempo_track():
    mpqn = round(60_000_000 / BPM)
    ev = b''
    name = b'Tempo'
    ev += vlq(0) + bytes([0xFF, 0x03, len(name)]) + name
    ev += vlq(0) + bytes([0xFF, 0x58, 0x04, 0x04, 0x02, 0x18, 0x08])
    ev += vlq(0) + bytes([0xFF, 0x51, 0x03]) + mpqn.to_bytes(3, 'big')
    ev += vlq(int(END_BEAT * PPQ)) + bytes([0xFF, 0x2F, 0x00])
    return b'MTrk' + struct.pack('>I', len(ev)) + ev

tracks = [tempo_track(), t_mel.render(END_BEAT), t_arp.render(END_BEAT),
          t_bass.render(END_BEAT), t_str.render(END_BEAT), t_bell.render(END_BEAT)]
header = b'MThd' + struct.pack('>IHHH', 6, 1, len(tracks), PPQ)
out = header + b''.join(tracks)
path = r'C:\Users\25448\Desktop\Song_For_The_Graduate\graduation_song.mid'
with open(path, 'wb') as f:
    f.write(out)
print('written', path, len(out), 'bytes;', len(melody), 'melody notes')
