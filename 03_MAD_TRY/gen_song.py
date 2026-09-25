# -*- coding: utf-8 -*-
"""《MAD之夜》MAD Night — 完整版作曲生成 (mido)
来源: FL Studio 工程 MAD_TRY.flp (140BPM, A小调方向): 原工程只有堆在第 0 小节的
Aqua 语音素材与三个空 pattern, 无任何音符。本曲为其编写完整的高能量伴奏
(语音素材无法进入 MIDI, 保留在原工程中, 结构留出可放置语音的乐句空间)。
结构: 前奏4 → 主歌A 16 → build 4 → 副歌1 16 → 间奏B 8 → build2 4 → 副歌2 16 →
桥段 8 → 终副歌 16 → 尾声 6 (共 98 小节, 140BPM ≈ 2:48)
"""
from mido import MidiFile, MidiTrack, Message, MetaMessage
import mido, os

PPQ = 480
BPM = 140
BARS = 98
END_BEAT = BARS * 4

INT, A, BLD, DRP1, B, BLD2, DRP2, BRK, DRP3, OUT = 0, 4, 20, 24, 40, 48, 52, 68, 76, 92

VOICING = {
    'Am': (45, [57, 60, 64, 69]),
    'F':  (41, [53, 57, 60, 65]),
    'C':  (36, [48, 55, 60, 64]),
    'G':  (43, [55, 59, 62, 67]),
    'Dm': (38, [50, 57, 62, 65]),
    'E':  (40, [52, 56, 59, 64]),
    'E7': (40, [52, 56, 59, 62]),
}
PROG = {
    INT:  ['Am', 'F', 'C', 'G'],
    A:    ['Am', 'F', 'C', 'G'] * 4,
    BLD:  ['Dm', 'Am', 'E', 'E'],
    DRP1: ['F', 'G', 'Am', 'Am', 'F', 'G', 'E7', 'Am', 'F', 'G', 'Am', 'Am', 'F', 'G', 'E', 'E'],
    B:    ['C', 'G', 'Am', 'F'] * 2,
    BLD2: ['Dm', 'Am', 'E', 'E'],
    DRP2: ['F', 'G', 'Am', 'Am', 'F', 'G', 'E7', 'Am', 'F', 'G', 'Am', 'Am', 'F', 'G', 'E', 'E'],
    BRK:  ['F', 'C', 'Dm', 'Am'] * 2,
    DRP3: ['F', 'G', 'Am', 'Am', 'F', 'G', 'E7', 'Am', 'F', 'G', 'Am', 'Am', 'F', 'G', 'E', 'E'],
    OUT:  ['Am', 'F', 'C', 'G', 'F', 'G'],
}

lead, chords, pad, bass, arp, piano, bells, strings, drums = [], [], [], [], [], [], [], [], []

# ---- 副歌 Hook (4 小节 = 16 拍乐句) ----
HOOK1 = [
    (69, 0, .5), (72, .5, .5), (76, 1, 1), (74, 2, .5), (72, 2.5, .5), (74, 3, .5), (72, 3.5, .5),
    (69, 4, .5), (72, 4.5, .5), (76, 5, .5), (79, 5.5, .5), (77, 6, 1.5), (76, 7.5, .5),
    (74, 8, .5), (72, 8.5, .5), (74, 9, .5), (76, 9.5, .5), (77, 10, 1), (76, 11, .5), (74, 11.5, .5),
    (72, 12, .5), (69, 12.5, .5), (72, 13, .5), (76, 13.5, .5), (74, 14, 1.5), (69, 15.5, .5),
]
HOOK2 = HOOK1[:20] + [(72, 12, .5), (74, 12.5, .5), (76, 13, 1), (79, 14, 1.5), (81, 15.5, .5)]
HOOK3 = HOOK1[:20] + [(72, 12, .5), (74, 12.5, .5), (76, 13, .5), (77, 13.5, .5), (76, 14, .5), (74, 14.5, .5), (72, 15, 1)]

# ---- 主歌旋律 (8 拍 + 8 拍对句) ----
V1 = [(69, 0, .75), (72, 1, .5), (74, 1.5, .5), (76, 2, 1), (74, 3, .5), (72, 3.5, .5),
      (67, 4, .75), (69, 5, .5), (72, 5.5, .5), (76, 6, 1.5), (74, 7.5, .5)]
V2 = [(72, 0, .75), (74, 1, .5), (76, 1.5, .5), (77, 2, 1), (76, 3, .5), (74, 3.5, .5),
      (72, 4, .75), (71, 5, .5), (69, 5.5, .5), (67, 6, 1.5), (69, 7.5, .5)]

for rep in range(4):
    base = A * 4 + rep * 16
    for p, s, d in V1 + [(q, s2 + 8, d2) for q, s2, d2 in V2]:
        lead.append((p, base + s, d, 90 if rep < 2 else 96))
# B 段: V1 高四度 (D 小调色彩) 用 F/G 和声
for rep in range(2):
    base = B * 4 + rep * 16
    for p, s, d in V2 + [(q, s2 + 8, d2) for q, s2, d2 in V1]:
        lead.append((p + 3, base + s, d, 94))
# 副歌 hook
for base, hook, tr, vel in ((DRP1 * 4, HOOK1, 0, 102), (DRP1 * 4 + 16, HOOK2, 0, 104),
                            (DRP1 * 4 + 32, HOOK1, 0, 104), (DRP1 * 4 + 48, HOOK3, 0, 106),
                            (DRP2 * 4, HOOK2, 12, 104), (DRP2 * 4 + 16, HOOK1, 12, 106),
                            (DRP2 * 4 + 32, HOOK3, 12, 106), (DRP2 * 4 + 48, HOOK2, 12, 108),
                            (DRP3 * 4, HOOK1, 12, 108), (DRP3 * 4 + 16, HOOK2, 12, 108),
                            (DRP3 * 4 + 32, HOOK3, 12, 110), (DRP3 * 4 + 48, HOOK1, 12, 112)):
    for p, s, d in hook:
        lead.append((p + tr, base + s, d, vel))
# 尾声: hook 头部渐弱
for p, s, d in HOOK1[:8]:
    lead.append((p, OUT * 4 + s, d, 70))

# ---- 和弦 stab / pad / strings ----
for sec, bars in PROG.items():
    for i, name in enumerate(bars):
        bar = sec + i
        notes = VOICING[name][1]
        if sec in (INT, BRK):
            for p in notes:
                piano.append((p, bar * 4, 3.9, 58 if sec == INT else 62))
        else:
            stab = 74 if sec in (A, B, BLD, BLD2) else 88
            for b in range(4):
                for p in notes:
                    chords.append((p, bar * 4 + b + 0.5, 0.2, stab + (6 if b in (0, 2) else 0)))
for sec in (INT, BRK, DRP1, DRP2, DRP3):
    vel = 40 if sec in (INT, BRK) else 46
    for i, name in enumerate(PROG[sec]):
        bar = sec + i
        for p in VOICING[name][1]:
            (strings if sec in (BRK, DRP3) else pad).append((p, bar * 4, 3.95, vel))

# ---- 贝斯 ----
for sec, bars in PROG.items():
    if sec == INT:
        continue
    vel = 84 if sec in (A, B, BLD, BLD2) else 98
    for i, name in enumerate(bars):
        bar = sec + i
        root = VOICING[name][0]
        if sec in (DRP1, DRP2, DRP3):  # 16 分泵动
            for j in range(16):
                p = root + (12 if j % 8 == 6 else 0)
                bass.append((p, bar * 4 + 0.25 * j, 0.2, vel if j % 4 == 0 else vel - 14))
        else:
            for b in range(8):
                bass.append((root + (12 if b % 4 == 3 else 0), bar * 4 + 0.5 * b, 0.42,
                             vel if b % 2 == 0 else vel - 12))
# 前奏末小节进低音
for b in range(8):
    bass.append((45, (INT + 3) * 4 + 0.5 * b, 0.42, 78))

# ---- 琶音 ----
ARP_IDX = [0, 2, 1, 3, 2, 0, 3, 1]
for sec in (A, BLD, DRP1, DRP2, DRP3):
    vel = 54 if sec == A else (62 if sec == BLD else 68)
    for i, name in enumerate(PROG[sec]):
        bar = sec + i
        notes = VOICING[name][1]
        for j in range(16):
            arp.append((notes[ARP_IDX[j % 8]] + (12 if (j // 8) % 2 else 0),
                        bar * 4 + 0.25 * j, 0.18, vel + (6 if j % 4 == 0 else 0)))

# ---- 铃声 ----
for base in (DRP1 * 4 + 16, DRP1 * 4 + 48, DRP2 * 4 + 32, DRP3 * 4 + 16, DRP3 * 4 + 48):
    for p, s, d in HOOK1[:14]:
        bells.append((p + 12, base + s, d, 54))

# ---- 鼓组 ----
for bar in range(BARS):
    sec = next((s for s in (OUT, DRP3, BRK, DRP2, BLD2, DRP1, B, BLD, A, INT) if bar >= s), INT)
    t0 = bar * 4
    if sec == INT:
        if bar >= 2:
            for b in range(8):
                drums.append((42, t0 + 0.5 * b, 0.2, 54 + (8 if b % 2 == 0 else 0)))
    elif sec in (A, B):
        for b in range(4):
            drums.append((36, t0 + b, 0.2, 98))
            drums.append((39, t0 + b + 1, 0.2, 80))
        for b in range(8):
            drums.append((42, t0 + 0.5 * b, 0.2, 64 + (10 if b % 2 == 0 else 0)))
        if bar % 8 == 7:  # 过门
            for j, p in enumerate((48, 48, 47, 45)):
                drums.append((p, t0 + 3 + 0.25 * j, 0.15, 84 + j * 4))
    elif sec in (BLD, BLD2):
        for b in range(4):
            drums.append((36, t0 + b, 0.2, 102))
        for b in range(16):
            drums.append((38, t0 + 0.25 * b, 0.12, 44 + b * 3))
        for b in range(8):
            drums.append((42, t0 + 0.5 * b, 0.2, 66))
    elif sec in (DRP1, DRP2, DRP3):
        if bar in (DRP1, DRP1 + 8, DRP2, DRP2 + 8, DRP3, DRP3 + 8):
            drums.append((49, t0, 1.0, 100))
        for b in range(4):
            drums.append((36, t0 + b, 0.2, 110))
            if b in (1, 3):
                drums.append((39, t0 + b, 0.2, 92))
            drums.append((46, t0 + b + 0.5, 0.25, 66))
        for b in range(16):
            drums.append((42, t0 + 0.25 * b, 0.1, 62 + (12 if b % 4 == 0 else 0)))
        if bar % 4 == 3:
            drums.append((36, t0 + 3.5, 0.2, 96))
        if bar % 8 == 7:
            for j, p in enumerate((48, 48, 47, 45, 43, 45, 47, 48)):
                drums.append((p, t0 + 2 + 0.25 * j, 0.12, 90))
    elif sec == BRK:
        if bar >= BRK + 6:
            for b in range(8):
                drums.append((42, t0 + 0.5 * b, 0.2, 60))
    elif sec == OUT:
        for b in range(4):
            drums.append((36, t0 + b, 0.2, max(56, 96 - (bar - OUT) * 8)))
# 终止镲 + 定音鼓
drums.append((49, (BARS - 1) * 4, 2.0, 96))
for b in range(4):
    bass.append((45, (BARS - 1) * 4 + b, 0.9, 100))
    bass.append((33, (BARS - 1) * 4 + b, 0.9, 100))

# ---- mido ----
mid = MidiFile(ticks_per_beat=PPQ, type=1)
t0 = MidiTrack()
t0.append(MetaMessage('track_name', name='Tempo', time=0))
t0.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))
t0.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0))
t0.append(MetaMessage('marker', text='MAD Night - completed backing for MAD_TRY', time=0))
t0.append(MetaMessage('end_of_track', time=END_BEAT * PPQ))
mid.tracks.append(t0)

def build_track(name, ch, program, notes):
    tr = MidiTrack()
    events = []
    for p, s, d, v in notes:
        st = int(round(s * PPQ)); et = int(round((s + d) * PPQ))
        events.append((st, 1, Message('note_on', channel=ch, note=p, velocity=int(min(v, 127)), time=0)))
        events.append((et, 0, Message('note_off', channel=ch, note=p, velocity=0, time=0)))
    events.append((0, -1, MetaMessage('track_name', name=name, time=0)))
    events.append((0, 2, Message('program_change', channel=ch, program=program, time=0)))
    events.append((END_BEAT * PPQ, -1, MetaMessage('end_of_track', time=0)))
    events.sort(key=lambda x: (x[0], x[1]))
    last = 0
    for tick, _, msg in events:
        tr.append(msg.copy(time=tick - last))
        last = tick
    mid.tracks.append(tr)

build_track('Lead', 0, 81, lead)
build_track('Chord Stabs', 1, 62, chords)
build_track('Warm Pad', 2, 89, pad)
build_track('Bass', 3, 38, bass)
build_track('Arp Pluck', 4, 46, arp)
build_track('Piano', 5, 0, piano)
build_track('Bells', 6, 9, bells)
build_track('Strings', 7, 48, strings)
build_track('Drums', 9, 0, drums)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MAD_TRY_complete.mid')
mid.save(out)
total = sum(len(x) for x in (lead, chords, pad, bass, arp, piano, bells, strings, drums))
print('saved:', out)
print('notes: lead=%d chords=%d pad=%d bass=%d arp=%d piano=%d bells=%d strings=%d drums=%d total=%d' % (
    len(lead), len(chords), len(pad), len(bass), len(arp), len(piano), len(bells), len(strings), len(drums), total))
print('bars=%d  duration=%.1fs' % (BARS, END_BEAT * 60 / BPM))
