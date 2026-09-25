# -*- coding: utf-8 -*-
"""《五月之舞》Dance in May — 完整版作曲生成 (mido)
来源: FL Studio 工程 2026-5-28.flp (130BPM) 中用户写下的 22 音符 G 大调动机,
原样保留作为主旋律主题, 在此基础上编写完整编曲。
结构: 前奏8 → 主歌A1 8 → 主歌A2 8 → 预副歌8 → 副歌16 → 桥段12 → 再build 4 → 副歌2 16 → 尾声10 (共90小节, 130BPM ≈ 2:46)
"""
from mido import MidiFile, MidiTrack, Message, MetaMessage
import mido, os

PPQ = 480
BPM = 130
BARS = 90
END_BEAT = BARS * 4

# ---- 段落起始小节 (与文档一致) ----
INT, A1, A2, BLD, DRP1, BRK, BLD2, DRP2, OUT = 0, 8, 16, 24, 32, 48, 60, 64, 80

# ---- 用户原始动机 (2026-5-28.flp pattern 原样提取, 11.5拍) ----
MOTIF = [
    (50, 0.0, 0.5), (67, 0.5, 0.5), (69, 1.0, 0.5), (71, 1.5, 0.5),
    (71, 2.0, 0.5), (69, 2.5, 0.5), (67, 3.0, 0.5), (62, 3.5, 0.5),
    (62, 4.0, 0.5), (67, 4.5, 0.5), (69, 5.0, 0.5), (71, 5.5, 0.5),
    (71, 6.0, 0.5), (62, 6.5, 0.5), (71, 7.0, 0.5), (69, 7.5, 0.5),
    (71, 8.0, 0.5), (72, 8.5, 0.5), (72, 9.0, 0.5), (72, 9.5, 1.0),
    (71, 10.5, 0.5), (69, 11.0, 0.5),
]
# 每次陈述后的 4 拍对句 (补满 4 小节乐句)
ANSWER_A = [(74, 12, 0.5), (71, 12.5, 0.5), (74, 13, 0.5), (76, 13.5, 0.5), (74, 14, 2.0)]
ANSWER_B = [(74, 12, 0.5), (76, 12.5, 0.5), (79, 13, 0.5), (76, 13.5, 0.5), (74, 14, 1.0), (71, 15, 1.0)]
ANSWER_C = [(74, 12, 1.0), (71, 13, 0.5), (67, 13.5, 0.5), (69, 14, 1.5), (71, 15.5, 0.5)]

# ---- 和声 ----
VOICING = {  # 和弦: (bass根音, 四声部排列 48-72)
    'G':  (43, [55, 59, 62, 67]),
    'D':  (38, [54, 57, 62, 66]),
    'Em': (40, [52, 59, 64, 67]),
    'C':  (36, [48, 55, 60, 64]),
    'Am': (45, [57, 60, 64, 69]),
    'Bm': (47, [59, 62, 66, 71]),
}
PROG = {
    INT:  ['G', 'D', 'Em', 'C', 'G', 'D', 'C', 'D'],
    A1:   ['G', 'D', 'Em', 'C', 'G', 'D', 'Em', 'C'],
    A2:   ['G', 'D', 'Em', 'C', 'G', 'D', 'Em', 'C'],
    BLD:  ['Em', 'C', 'G', 'D', 'Em', 'C', 'C', 'D'],
    DRP1: ['C', 'G', 'D', 'Em', 'C', 'G', 'D', 'G', 'C', 'G', 'D', 'Em', 'C', 'G', 'D', 'D'],
    BRK:  ['Em', 'C', 'G', 'D', 'Em', 'C', 'G', 'D', 'Am', 'Am', 'C', 'D'],
    BLD2: ['Am', 'C', 'C', 'D'],
    DRP2: ['C', 'G', 'D', 'Em', 'C', 'G', 'D', 'G', 'C', 'G', 'D', 'Em', 'C', 'G', 'D', 'G'],
    OUT:  ['C', 'G', 'Em', 'C', 'C', 'G', 'Am', 'D', 'C', 'G'],
}

lead, chords, pad, bass, arp, piano, bells, drums = [], [], [], [], [], [], [], []

def motif_statement(base_beat, answer, transpose=0, vel=96):
    seq = MOTIF + answer
    for p, s, d in seq:
        lead.append((p + transpose, base_beat + s, d, vel))

# ---- 主旋律 ----
# A1: 原样动机 ×2 (对句 A/B)
motif_statement(A1 * 4, ANSWER_A, vel=88)
motif_statement(A1 * 4 + 16, ANSWER_B, vel=92)
# A2: 原样 + 高八度回声
motif_statement(A2 * 4, ANSWER_A, vel=92)
motif_statement(A2 * 4 + 16, ANSWER_B, transpose=12, vel=96)
# DROP1: 陈述 + 铃声同度 + 变化对句
motif_statement(DRP1 * 4, ANSWER_A, vel=104)
motif_statement(DRP1 * 4 + 16, ANSWER_B, vel=104)
motif_statement(DRP1 * 4 + 32, ANSWER_C, vel=106)
motif_statement(DRP1 * 4 + 48, ANSWER_B, vel=108)
# BRK: 动机头部稀疏回顾 (钢琴区, 弱)
for p, s, d in MOTIF[:8]:
    piano.append((p + 12, BRK * 4 + s, d, 58))
# DROP2: 高八度主奏
motif_statement(DRP2 * 4, ANSWER_A, transpose=12, vel=106)
motif_statement(DRP2 * 4 + 16, ANSWER_B, transpose=12, vel=106)
motif_statement(DRP2 * 4 + 32, ANSWER_C, transpose=12, vel=108)
motif_statement(DRP2 * 4 + 48, ANSWER_B, transpose=12, vel=110)

# ---- 和弦 stab (强拍反拍) 与长音 pad ----
def chord_at(bar, name):
    return VOICING[name][1]

for sec, bars in PROG.items():
    for i, name in enumerate(bars):
        bar = sec + i
        notes = chord_at(bar, name)
        if sec in (INT, BRK):  # 长音
            for j, p in enumerate(notes):
                piano.append((p, bar * 4, 3.9, 60 if sec == INT else 54))
        else:
            stab_vel = 72 if sec in (A1, A2) else (84 if sec in (DRP1, DRP2) else 78)
            for b in range(4):
                for j, p in enumerate(notes):
                    chords.append((p, bar * 4 + b + 0.5, 0.22, stab_vel + (6 if b == 0 else 0)))
# pad: 前奏/桥段/副歌 长和弦
for sec in (INT, BRK, DRP1, DRP2):
    for i, name in enumerate(PROG[sec]):
        bar = sec + i
        vel = 40 if sec in (INT, BRK) else 48
        for p in VOICING[name][1]:
            pad.append((p, bar * 4, 3.95, vel))

# ---- 贝斯: 八分音符泵动 ----
for sec, bars in PROG.items():
    if sec == INT:
        continue
    vel = 84 if sec in (A1, A2, BLD) else (96 if sec in (DRP1, DRP2) else 76)
    for i, name in enumerate(bars):
        bar = sec + i
        root = VOICING[name][0]
        for b in range(8):
            p = root + (12 if b % 4 == 3 else 0)
            bass.append((p, bar * 4 + 0.5 * b, 0.42, vel if b % 2 == 0 else vel - 10))
# 前奏最后2小节进入低音
for b in range(8):
    bass.append((43, (INT + 6) * 4 + 0.5 * b, 0.42, 80))

# ---- 琶音 (16分, A2/BLD/DRP) ----
ARP_IDX = [0, 1, 2, 3, 2, 1, 0, 2]
for sec in (A2, BLD, DRP1, DRP2):
    vel = 56 if sec == A2 else (64 if sec == BLD else 66)
    for i, name in enumerate(PROG[sec]):
        bar = sec + i
        notes = VOICING[name][1]
        for j in range(16):
            arp.append((notes[ARP_IDX[j % 8] % 4] + (12 if (j // 8) % 2 else 0),
                        bar * 4 + 0.25 * j, 0.2, vel + (6 if j % 4 == 0 else 0)))

# ---- 铃声: 副歌高八度点缀 ----
for beat_base in (DRP1 * 4 + 16, DRP1 * 4 + 48, DRP2 * 4 + 16, DRP2 * 4 + 48):
    for p, s, d in MOTIF:
        bells.append((p + 12, beat_base + s, d, 56))
for p, s, d in MOTIF[:10]:
    bells.append((p + 24, DRP2 * 4 + 32 + s, d, 52))

# ---- 鼓组 ----
def bar_beats(bar):
    return bar * 4

for bar in range(BARS):
    sec = next((s for s in (OUT, DRP2, BLD2, BRK, DRP1, BLD, A2, A1, INT) if bar >= s), INT)
    t0 = bar_beats(bar)
    if sec == INT:
        if bar >= 4:
            for b in range(8):
                drums.append((42, t0 + 0.5 * b, 0.2, 52 + (8 if b % 2 == 0 else 0)))
    elif sec in (A1, A2):
        for b in range(4):
            drums.append((36, t0 + b, 0.2, 96))
            drums.append((39, t0 + b + 1, 0.2, 78))
        for b in range(8):
            drums.append((42, t0 + 0.5 * b, 0.2, 62 + (10 if b % 2 == 0 else 0)))
        if sec == A2:
            drums.append((46, t0 + 2.5, 0.3, 66))
    elif sec in (BLD, BLD2):
        for b in range(4):
            drums.append((36, t0 + b, 0.2, 100))
        frac = 2 if (sec == BLD and bar < BLD + 4) else 4  # 后半 16 分军鼓
        if sec == BLD2 or bar >= (BLD + 4):
            for b in range(16):  # 军鼓滚奏渐强
                drums.append((38, t0 + 0.25 * b, 0.15, 48 + b * 3))
        else:
            for b in range(8):
                drums.append((38 if b % 4 == 2 else 42, t0 + 0.5 * b, 0.15, 66 if b % 4 == 2 else 58))
        for b in range(8):
            drums.append((42, t0 + 0.5 * b, 0.2, 64))
    elif sec in (DRP1, DRP2):
        drums.append((49, t0, 1.0, 96)) if bar in (DRP1, DRP1 + 8, DRP2, DRP2 + 8) else None
        for b in range(4):
            drums.append((36, t0 + b, 0.2, 108))
            if b in (1, 3):
                drums.append((39, t0 + b, 0.2, 88))
            drums.append((46, t0 + b + 0.5, 0.25, 62))  # 反拍开镲
        for b in range(16):
            drums.append((42, t0 + 0.25 * b, 0.1, 60 + (12 if b % 4 == 0 else 0)))
        if bar % 4 == 3:
            drums.append((36, t0 + 3.5, 0.2, 92))  # 第4小节加一脚
    elif sec == BRK:
        if bar >= BRK + 8:
            for b in range(8):
                drums.append((42, t0 + 0.5 * b, 0.2, 60))
    elif sec == OUT:
        for b in range(4):
            drums.append((36, t0 + b, 0.2, max(60, 96 - (bar - OUT) * 6)))
        for b in range(4):
            drums.append((42, t0 + b + 0.5, 0.2, max(40, 60 - (bar - OUT) * 4)))
# 结尾镲
drums.append((49, (BARS - 1) * 4, 2.0, 90))

# ---- mido 构建 ----
mid = MidiFile(ticks_per_beat=PPQ, type=1)
t0 = MidiTrack()
t0.append(MetaMessage('track_name', name='Tempo', time=0))
t0.append(MetaMessage('time_signature', numerator=4, denominator=4, time=0))
t0.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0))
t0.append(MetaMessage('marker', text='Dance in May - completed from 2026-5-28 motif', time=0))
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
build_track('Drums', 9, 0, drums)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '2026-5-28_complete.mid')
mid.save(out)
total = sum(len(t) for t in (lead, chords, pad, bass, arp, piano, bells, drums))
print('saved:', out)
print('notes: lead=%d chords=%d pad=%d bass=%d arp=%d piano=%d bells=%d drums=%d total=%d' % (
    len(lead), len(chords), len(pad), len(bass), len(arp), len(piano), len(bells), len(drums), total))
print('bars=%d  duration=%.1fs' % (BARS, END_BEAT * 60 / BPM))
