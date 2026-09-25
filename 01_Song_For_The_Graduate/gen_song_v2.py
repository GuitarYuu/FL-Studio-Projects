# -*- coding: utf-8 -*-
"""生成《启程的那天》毕业赠礼歌曲 MIDI v2 (mido 编码)
C大调, 76BPM, 56小节; 声部: Piano Melody / Piano Arp / Bass / Strings / Bells
"""
import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage

PPQ = 480
BPM = 76
END_BEAT = 224

V1, V2, CH1, BR, CH2, CH2V, OUT = 16, 48, 80, 112, 128, 160, 192
INT = 0

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

melody = []

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

# ---------- mido 构建 ----------
mid = MidiFile(ticks_per_beat=PPQ, type=1)

# Tempo 轨
t0 = MidiTrack()
t0.append(MetaMessage('track_name', name='Tempo', time=0))
t0.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))
t0.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0))
t0.append(MetaMessage('end_of_track', time=END_BEAT))
mid.tracks.append(t0)

def build_track(name, ch, program, notes):
    """notes: list of (pitch, start_beat, dur_beat, vel); 绝对tick转delta"""
    tr = MidiTrack()
    events = []
    for p, s, d, v in notes:
        s_tick = int(round(s * PPQ))
        e_tick = int(round((s + d) * PPQ))
        events.append((s_tick, 1, Message('note_on', channel=ch, note=p, velocity=int(v), time=0)))
        events.append((e_tick, 0, Message('note_off', channel=ch, note=p, velocity=0, time=0)))
    events.append((0, -1, MetaMessage('track_name', name=name, time=0)))
    events.append((0, 2, Message('program_change', channel=ch, program=program, time=0)))
    events.append((END_BEAT * PPQ, -1, MetaMessage('end_of_track', time=0)))
    events.sort(key=lambda x: (x[0], x[1]))
    last = 0
    for tick, _, msg in events:
        m = msg.copy(time=tick - last)
        tr.append(m)
        last = tick
    mid.tracks.append(tr)
    return tr

# 1. Piano Melody
mel_notes = []
for p, s, d in melody:
    vel = 96
    if d >= 2: vel += 8
    if s >= CH1: vel += 6
    if s >= CH2V: vel += 4
    mel_notes.append((p, s, d, vel))
build_track('Piano Melody', 0, 0, mel_notes)

# 2. Piano Arp
IDX = [0, 1, 2, 3, 2, 1, 2, 3]
arp_notes = []
for sec, bars in PROG.items():
    for i, cname in enumerate(bars):
        bar = sec + i * 4
        notes = CH[cname][1]
        base_vel = 48 if sec == INT else (60 if sec in (V1, V2) else
                   (56 if sec == BR else (68 if sec in (CH1, CH2, CH2V) else 50)))
        if sec == OUT and bar == 220:
            for k, nn in enumerate([48, 55, 60, 64]):
                arp_notes.append((nn, bar + 0.05 * k, 4 - 0.05 * k, 60))
            continue
        for j, idx in enumerate(IDX):
            arp_notes.append((notes[idx], bar + 0.5 * j, 0.48, base_vel + (8 if j == 0 else 0)))
build_track('Piano Arp', 1, 0, arp_notes)

# 3. Bass
bass_notes = []
for sec in (V2, CH1, BR, CH2, CH2V, OUT):
    bars = PROG[sec]
    vel = 70 if sec == BR else (78 if sec == OUT else 92)
    for i, cname in enumerate(bars):
        bar = sec + i * 4
        root = CH[cname][0]
        if sec == OUT and bar == 220:
            bass_notes.append((root, bar, 4, 90))
        else:
            bass_notes.append((root, bar, 1.75, vel))
            bass_notes.append((root + 7, bar + 2, 1.75, vel - 14))
build_track('Bass', 2, 33, bass_notes)

# 4. Strings
str_notes = []
str_events = [(V2 + 24, 'Dm', 44), (V2 + 28, 'G', 44)]
for sec, vel in ((CH1, 48), (BR, 34), (CH2, 48), (CH2V, 52)):
    for i, cname in enumerate(PROG[sec]):
        str_events.append((sec + i * 4, cname, vel))
str_events += [(OUT + 24, 'F', 44), (OUT + 28, 'C', 46)]
for bar, cname, vel in str_events:
    for p in CH[cname][2]:
        str_notes.append((p, bar, 3.95, vel))
build_track('Strings', 3, 48, str_notes)

# 5. Bells
bell_notes = []
for p, s, d in melody:
    if (CH1 <= s < BR) or (CH2 <= s < OUT):
        bell_notes.append((p + 12, s, d, 52))
build_track('Bells', 4, 9, bell_notes)

path = r'C:\Users\25448\Desktop\Song_For_The_Graduate\graduation_song.mid'
mid.save(path)
print('saved', path, 'tracks:', len(mid.tracks))
