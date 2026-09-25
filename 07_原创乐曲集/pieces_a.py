# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Piece, Trk, Drums, P

OUT = r"C:\Users\25448\Downloads\原创乐曲"

def bass8(t, bass, root, pat=None, vel=88):
    """driving 8th-note bass; pat = semitone offsets per 8th"""
    if pat is None: pat = [0,12,0,12,0,12,0,12]
    for i, off in enumerate(pat):
        if off is None: continue
        bass.n(t + i*0.5, 0.47, root + off, vel)

# ============================================================ 1. New Song
def piece_new_song():
    pc = Piece('Undercurrent (after New Song.mid)', 140, 4, 4, 'Dm')
    lead = pc.add(Trk('Lead Saw', 81, 0, vol=105, pan=70))
    bass = pc.add(Trk('Synth Bass', 38, 1, vol=95, pan=56))
    pad  = pc.add(Trk('Warm Pad', 89, 2, vol=58, pan=40))
    dr   = pc.add(Drums(vol=88))
    # 原始 riff 量化保留: D D Eb C# Eb (来自 New Song.mid)
    riffD  = [(P('D4'),1.0),(P('D4'),0.75),(P('D#4'),0.75),(P('C#4'),0.5),(P('D#4'),0.5)]
    riffD2 = [(P('D4'),1.0),(P('D4'),0.75),(P('D#4'),0.75),(P('C#4'),0.5),(P('D4'),0.5)]
    # intro 4 bars
    for i in range(4):
        pat = [0,12,0,12,0,12,-2,12] if i >= 2 else None
        bass8(i*4, bass, P('D2'), pat=pat)
    dr.d(0, Drums.CRASH, 60); dr.beat(0, 'rock', 4, fill=True)
    pad.chord(8, 4, [P('D3'),P('F3'),P('A3')], 70); pad.chord(12, 4, [P('Bb2'),P('D3'),P('F3')], 70)
    # A (bars 4-11): Dm Dm Bb C x2
    prog = [P('D2'),P('D2'),P('A#1'),P('C2')]*2
    for i, r in enumerate(prog):
        bass8((4+i)*4, bass, r, pat=[0,12,0,12,0,7,0,12])
    for i in range(8):
        lead.mel((4+i)*4, riffD if i % 2 == 0 else riffD2)
        if i % 4 in (0, 1):
            ch = [P('D3'),P('F3'),P('A3')]
        elif i % 4 == 2:
            ch = [P('A#2'),P('D3'),P('F3')]
        else:
            ch = [P('C3'),P('E3'),P('G3')]
        pad.chord((4+i)*4, 4, ch, 66)
    dr.beat(4, 'rock', 7, fill=True); dr.d(4*4, Drums.CRASH, 70)
    # B (bars 12-19): 动机移到 F、E 上的下行模进
    riffF = [(P('F4'),1.0),(P('F4'),0.75),(P('F#4'),0.75),(P('E4'),0.5),(P('F#4'),0.5)]
    riffE = [(P('E4'),1.0),(P('E4'),0.75),(P('F4'),0.75),(P('D#4'),0.5),(P('F4'),0.5)]
    bprog = [P('D2'),P('D2'),P('A#1'),P('C2'),P('D2'),P('D2'),P('A#1'),P('C2')]
    for i, r in enumerate(bprog):
        bass8((12+i)*4, bass, r, pat=[0,12,0,12,3,12,0,12])
    lead.mel(12*4, riffF); lead.mel(13*4, [(P('D5'),2.5)])
    lead.mel(14*4, riffE); lead.mel(15*4, [(P('C#5'),2.5)])
    lead.mel(16*4, [(x+12, y) for x, y in riffF]); lead.mel(17*4, [(P('D6'),2.5)])
    lead.mel(18*4, [(x+12, y) for x, y in riffE]); lead.mel(19*4, [(P('C#6'),2.5)])
    for i in range(8):
        if i % 4 in (0, 1):
            ch = [P('D3'),P('F3'),P('A3'),P('C4')]
        elif i % 4 == 2:
            ch = [P('A#2'),P('D3'),P('F3'),P('A3')]
        else:
            ch = [P('C3'),P('E3'),P('G3'),P('A#3')]
        pad.chord((12+i)*4, 4, ch, 70)
    dr.beat(12, 'rock', 8, fill=True); dr.d(12*4, Drums.CRASH, 70)
    # A' (bars 20-27): 高八度 riff
    for i, r in enumerate(prog):
        pat = [0,0,12,0,0,7,10,12] if i % 4 == 3 else [0,12,0,12,0,7,0,12]
        bass8((20+i)*4, bass, r, pat=pat)
    for i in range(8):
        lead.mel((20+i)*4, [(x+12, y) for x, y in (riffD if i % 2 == 0 else riffD2)])
        if i % 4 in (0, 1):
            ch = [P('D3'),P('F3'),P('A3')]
        elif i % 4 == 2:
            ch = [P('A#2'),P('D3'),P('F3')]
        else:
            ch = [P('C3'),P('E3'),P('G3')]
        pad.chord((20+i)*4, 4, ch, 72)
    dr.beat(20, 'rock', 7, fill=True); dr.d(20*4, Drums.CRASH, 75)
    # breakdown (bars 28-31)
    for i, r in enumerate([P('D2'),P('D2'),P('A#1'),P('C2')]):
        bass8((28+i)*4, bass, r, pat=[0,0,12,0,0,12,0,0])
    lead.mel(28*4, [(P('D5'),1.5),(P('E5'),0.5),(P('F5'),2.0)])
    lead.mel(30*4, [(P('D5'),1.5),(P('C5'),0.5),(P('A#4'),2.0)])
    dr.beat(28, 'soft', 3); dr.beat(31, 'rock', 1, fill=True)
    # outro (bars 32-35)
    for i, r in enumerate([P('D2'),P('A#1'),P('C2'),P('D2')]):
        bass8((32+i)*4, bass, r, vel=80-i*8)
    for i in range(4):
        v = max(95-i*15, 40)
        lead.mel((32+i)*4, [(x, y, v) for x, y in (riffD if i % 2 == 0 else riffD2)])
        pad.chord((32+i)*4, 4, [P('D3'),P('F3'),P('A3')], max(60-i*10, 25))
    dr.beat(32, 'rock', 4); dr.d(35*4+3.5, Drums.CRASH, 40)
    return pc.save(os.path.join(OUT, '01_暗涌_基于New Song_原创.mid'))

# ============================================================ 2. unknown1
def piece_unknown1():
    pc = Piece('September Blocks (after unknown1.mid)', 112, 4, 4, 'C')
    rh = pc.add(Trk('Piano Melody', 0, 0, vol=100, pan=64))
    lh = pc.add(Trk('Piano LH', 0, 1, vol=78, pan=48))
    strs = pc.add(Trk('Strings', 48, 2, vol=52, pan=80))
    C  = [P('C2'),P('G2'),P('E3')]; G  = [P('G2'),P('D3'),P('B3')]
    F  = [P('F2'),P('C3'),P('A3')]; Dm = [P('D3'),P('A3'),P('F4')]
    G7 = [P('G2'),P('D3'),P('F3')]
    def lhb(t, r):
        seq = [0,1,2,1,0,1,2,1]
        for i, k in enumerate(seq):
            lh.n(t+i*0.5, 0.45, r[k], 60)
    # intro 2 bars
    lhb(0, C); lhb(4, G)
    rh.mel(7, [(P('E4'),0.5),(P('G4'),0.5)])
    # A (bars 2-9): 原主题原样保留
    A_rh = [[(P('C4'),1),(P('E4'),1),(P('C4'),1),(P('E4'),1)],
            [(P('D4'),1.5),(None,0.5),(P('D4'),1.5),(None,0.5)],
            [(P('C4'),1),(P('E4'),1),(P('C4'),1),(P('E4'),1)],
            [(P('D4'),1.5),(None,0.5),(P('D4'),1.5),(None,0.5)],
            [(P('C4'),1),(P('E4'),1),(P('G4'),1),(P('E4'),1)],
            [(P('D4'),1.5),(None,0.5),(P('D4'),1.5),(None,0.5)],
            [(P('A4'),1),(P('E4'),1),(P('E4'),1),(P('A4'),1)],
            [(P('G4'),1),(P('G4'),2.5),(None,0.5)]]
    progA = [C,G,C,G,C,G,F,G]
    for i, (bars, ch) in enumerate(zip(A_rh, progA)):
        t = (2+i)*4
        rh.mel(t, bars); lhb(t, ch)
        strs.chord(t, 4, [ch[0]+12, ch[2]], 40)
    # A' (bars 10-17): 加花变奏
    A2 = [[(P('C4'),0.5),(P('E4'),0.5),(P('G4'),0.5),(P('E4'),0.5),(P('C4'),0.5),(P('E4'),0.5),(P('G4'),0.5),(P('E4'),0.5)],
          [(P('D4'),0.5),(P('F4'),0.5),(P('D4'),1.0),(None,0.5),(P('D4'),0.5),(P('F4'),0.5),(P('D4'),1.0)],
          [(P('C4'),0.5),(P('E4'),0.5),(P('G4'),0.5),(P('E4'),0.5),(P('C4'),0.5),(P('E4'),0.5),(P('G4'),0.5),(P('E4'),0.5)],
          [(P('D4'),0.5),(P('F4'),0.5),(P('D4'),1.0),(None,0.5),(P('D4'),0.5),(P('F4'),0.5),(P('D4'),1.0)],
          [(P('C4'),0.5),(P('E4'),0.5),(P('G4'),0.5),(P('B4'),0.5),(P('C5'),1),(P('G4'),1)],
          [(P('D4'),0.5),(P('F4'),0.5),(P('A4'),1),(None,0.5),(P('F4'),0.5),(P('A4'),1)],
          [(P('A4'),0.5),(P('C5'),0.5),(P('A4'),0.5),(P('E4'),0.5),(P('A4'),0.5),(P('C5'),0.5),(P('A4'),0.5),(P('E4'),0.5)],
          [(P('G4'),1),(P('B4'),1),(P('D5'),2)]]
    for i, (bars, ch) in enumerate(zip(A2, progA)):
        t = (10+i)*4
        rh.mel(t, bars); lhb(t, ch)
        strs.chord(t, 4, [ch[0]+12, ch[2]], 44)
    # B (bars 18-25): 上行模进 Dm-G-Dm-G-F-C-F-G
    seq = [[(P('D4'),0.5),(P('F4'),0.5),(P('D4'),0.5),(P('F4'),0.5),(P('D4'),0.5),(P('F4'),0.5),(P('D4'),0.5),(P('F4'),0.5)],
           [(P('E4'),1),(None,0.5),(P('E4'),1.5),(None,0.5)],
           [(P('D4'),0.5),(P('F4'),0.5),(P('A4'),0.5),(P('F4'),0.5),(P('D4'),0.5),(P('F4'),0.5),(P('A4'),0.5),(P('F4'),0.5)],
           [(P('E4'),1),(None,0.5),(P('E4'),1.5),(None,0.5)],
           [(P('F4'),0.5),(P('A4'),0.5),(P('F4'),0.5),(P('A4'),0.5),(P('F4'),0.5),(P('A4'),0.5),(P('F4'),0.5),(P('A4'),0.5)],
           [(P('G4'),1),(None,0.5),(P('G4'),1.5),(None,0.5)],
           [(P('A4'),0.5),(P('B4'),0.5),(P('C5'),0.5),(P('B4'),0.5),(P('A4'),1),(P('G4'),1)],
           [(P('E4'),1.5),(P('D4'),1.5),(None,1)]]
    progB = [Dm,G7,Dm,G7,F,C,F,G7]
    for i, (bars, ch) in enumerate(zip(seq, progB)):
        t = (18+i)*4
        rh.mel(t, bars); lhb(t, ch)
        strs.chord(t, 4, [ch[0]+12, ch[2]], 46)
    # A'' (bars 26-33) + coda (34-35)
    for i, (bars, ch) in enumerate(zip(A_rh, progA)):
        t = (26+i)*4
        rh.mel(t, bars); lhb(t, ch)
        strs.chord(t, 4, [ch[0]+12, ch[2]], 44)
    rh.mel(34*4, [(P('C4'),0.5),(P('E4'),0.5),(P('G4'),0.5),(P('C5'),0.5),(P('E5'),2)])
    lhb(34*4, C); lhb(35*4, C)
    rh.mel(35*4, [(P('C5'),4,80)])
    strs.chord(34*4, 8, [P('C3'),P('E3'),P('G3'),P('C4')], 50)
    return pc.save(os.path.join(OUT, '02_九月的方块_基于unknown1_原创.mid'))

# ============================================================ 3. unifish2
def piece_unifish2():
    pc = Piece('Little Fish Run (after unifish2.mid)', 126, 4, 4, 'F')
    mb = pc.add(Trk('Marimba', 12, 0, vol=100, pan=60))
    vib = pc.add(Trk('Vibraphone', 11, 1, vol=70, pan=30))
    bass = pc.add(Trk('Bass', 32, 2, vol=90, pan=48))
    dr = pc.add(Drums(vol=72))
    F, Bb, C = P('F2'), P('A#1'), P('C2')
    def bassroots(t, r):
        for i in range(8):
            off = 0 if i % 2 == 0 else (7 if (i//2) % 2 == 0 else 12)
            bass.n(t+i*0.5, 0.45, r+off, 84)
    # A 短句来自 unifish2.mid: F F F F D F G F
    phA  = [(P('F5'),1),(P('F5'),1),(P('F5'),1),(P('F5'),1),(P('D5'),1),(P('F5'),1),(P('G5'),1),(P('F5'),1)]
    phA2 = [(P('F5'),0.5),(P('F5'),0.5),(P('F5'),1),(P('F5'),0.5),(P('F5'),0.5),(P('D5'),1),(P('F5'),0.5),(P('F5'),0.5),(P('G5'),0.5),(P('G5'),0.5),(P('F5'),1)]
    phB  = [(P('D5'),1),(P('F5'),1),(P('G5'),1),(P('F5'),1),(P('D5'),1.5),(P('A#4'),2.5)]
    # intro 2 bars
    bass.n(0, 2, F, 80); bass.n(2, 1.5, C, 80); bass.n(3.5, 0.5, C, 70)
    mb.mel(4, [(P('F5'),0.5),(P('G5'),0.5),(P('A5'),0.5),(P('A#5'),0.5)])
    dr.beat(0, 'soft', 2, fill=True)
    # A (bars 2-9)
    rootsA = [F,F,Bb,C,F,F,Bb,C]
    mels = [phA, phA, phA2, phA2]
    chF = [P('F3'),P('A3'),P('C4')]; chBb = [P('A#3'),P('D4'),P('F4')]; chC = [P('C4'),P('E4'),P('G4')]
    for i in range(4):
        mb.mel((2+i*2)*4, mels[i])
    for i in range(8):
        t = (2+i)*4
        bassroots(t, rootsA[i])
        if i % 2 == 0: vib.chord(t, 4, chF, 55)
        elif i % 4 == 1: vib.chord(t, 4, chBb, 55)
        else: vib.chord(t, 4, chC, 55)
    dr.beat(2, 'soft', 8, fill=True)
    # B (bars 10-13): 上行模进 Bb C Dm C7
    seqB = [[(P('D5'),0.5),(P('E5'),0.5),(P('F5'),0.5),(P('D5'),1),(None,0.5),(P('D5'),0.5)],
            [(P('E5'),0.5),(P('F5'),0.5),(P('G5'),0.5),(P('E5'),1),(None,0.5),(P('E5'),0.5)],
            [(P('F5'),0.5),(P('G5'),0.5),(P('A5'),0.5),(P('F5'),1),(None,0.5),(P('F5'),0.5)],
            [(P('G5'),0.5),(P('A5'),0.5),(P('B5'),0.5),(P('G5'),1),(None,0.5),(P('G5'),0.5)]]
    rootsB = [Bb, C, P('D2'), C]
    chB = [chBb, chC, [P('D4'),P('F4'),P('A4')], [P('C4'),P('E4'),P('G4')]]
    for i in range(4):
        t = (10+i)*4
        mb.mel(t, seqB[i]); bassroots(t, rootsB[i]); vib.chord(t, 4, chB[i], 58)
    dr.beat(10, 'soft', 4, fill=True)
    # A' (bars 14-21): 低八度颤音琴对位
    for i in range(4):
        t = (14+i*2)*4
        mb.mel(t, mels[i])
        vib.mel(t, [(p-12, d, 68) if j % 3 == 0 else (None, d) for j, (p, d) in enumerate(mels[i])])
    for i in range(8):
        t = (14+i)*4
        bassroots(t, rootsA[i])
    dr.beat(14, 'soft', 8, fill=True)
    # B' (22-25) + coda (26-27)
    for i in range(4):
        t = (22+i)*4
        mb.mel(t, seqB[i]); bassroots(t, rootsB[i]); vib.chord(t, 4, chB[i], 55)
    dr.beat(22, 'soft', 4, fill=True)
    mb.mel(26*4, phB)
    bass.n(26*4, 1.5, Bb, 80); bass.n(26*4+2, 2, F, 82)
    vib.chord(26*4, 2, chBb, 55); vib.chord(26*4+2, 2, chF, 58)
    dr.beat(26, 'soft', 1); dr.d(26*4+3.5, Drums.CRASH, 50)
    mb.mel(27*4, [(P('F5'),4,90)])
    return pc.save(os.path.join(OUT, '03_小银鱼快跑_基于unifish2_原创.mid'))

# ============================================================ 4. 未完成1
def piece_unfinished1():
    pc = Piece('Violet (after unfinished1.mid)', 78, 4, 4, 'F#')
    pm  = pc.add(Trk('Piano Melody', 0, 0, vol=100, pan=64))
    pa  = pc.add(Trk('Piano Arp', 0, 1, vol=70, pan=44))
    bass= pc.add(Trk('Bass', 32, 2, vol=85, pan=48))
    strs= pc.add(Trk('Strings', 48, 3, vol=55, pan=80))
    dr  = pc.add(Drums(vol=55))
    chA = [[P('F#3'),P('A#3'),P('C#4'),P('F4')],   # F#maj7
           [P('D#3'),P('F#3'),P('A#3'),P('D#4')],  # D#m7
           [P('D#3'),P('F#3'),P('B3'),P('D#4')],   # Bmaj7
           [P('F3'),P('G#3'),P('B3'),P('C#4')]]   # C#9(no root)
    rootsA = [P('F#2'),P('D#2'),P('B1'),P('C#2')]
    def arps(t, chords, dur=4):
        for i, ch in enumerate(chords):
            pat = [0,1,2,3,2,1,2,3]
            for j, k in enumerate(pat):
                pa.n(t+i*dur+j*0.5, 0.9, ch[k], 56)
    def wholer(t, chords, vel=44):
        for i, ch in enumerate(chords):
            strs.chord(t+i*4, 4, ch, vel)
    def bassr(t, roots, vel=82):
        for i, r in enumerate(roots):
            bass.n(t+i*4, 3.5, r, vel); bass.n(t+i*4+3.5, 0.5, r+7, vel-10)
    # Intro (4 bars)
    arps(0, chA)
    bassr(0, rootsA)
    dr.beat(0, 'soft', 4)
    # A1 (bars 4-11): 修复后的旋律(去掉开头的音簇与游离低音)
    melA1 = [[(P('F#5'),0.5),(P('A#5'),1),(P('A#5'),0.5),(P('A#5'),1),(P('A#5'),0.5)],
             [(P('G#5'),1.5),(P('F#5'),2.5)],
             [(P('F#5'),0.5),(P('A#5'),1),(P('A#5'),0.5),(P('A#5'),1),(P('A#5'),0.5)],
             [(P('G#5'),1.5),(P('F#5'),1),(P('D#5'),1.5)],
             [(P('C#6'),1),(P('A#5'),0.5),(P('A#5'),0.5),(P('F#5'),1),(P('G#5'),1)],
             [(P('A#5'),2),(P('F#5'),2)],
             [(P('G#5'),0.5),(P('A#5'),0.5),(P('B5'),1),(P('A#5'),2)],
             [(P('G#5'),1),(P('F5'),1),(P('F#5'),2)]]
    for i, m in enumerate(melA1):
        t = (4+i)*4
        pm.mel(t, m); arps(t, [chA[i % 4]]); bassr(t, [rootsA[i % 4]])
        wholer(t, [chA[i % 4][:3]], 40)
    dr.beat(4, 'soft', 8, fill=True)
    # B (bars 12-19)
    chB = [[P('D#3'),P('F#3'),P('B3'),P('D#4')],
           [P('F3'),P('G#3'),P('B3'),P('C#4')],
           [P('D#3'),P('F#3'),P('A#3'),P('D#4')],
           [P('B2'),P('D#3'),P('F#3'),P('B3')],
           [P('D#3'),P('F#3'),P('B3'),P('D#4')],
           [P('F3'),P('G#3'),P('B3'),P('C#4')],
           [P('D#3'),P('F#3'),P('A#3'),P('D#4')],
           [P('F3'),P('G#3'),P('B3'),P('C#4')]]
    rootsB = [P('B1'),P('C#2'),P('D#2'),P('G#2'),P('B1'),P('C#2'),P('D#2'),P('C#2')]
    melB = [[(P('D#6'),1),(P('C#6'),1),(P('B5'),1),(P('A#5'),1)],
            [(P('G#5'),1),(P('A#5'),1),(P('B5'),2)],
            [(P('F#5'),1),(P('G#5'),1),(P('A#5'),1),(P('B5'),1)],
            [(P('B5'),1),(P('A#5'),1),(P('G#5'),2)],
            [(P('D#6'),1),(P('C#6'),1),(P('B5'),1),(P('F#5'),1)],
            [(P('G#5'),2),(P('B5'),1),(P('C#6'),1)],
            [(P('A#5'),1.5),(P('B5'),0.5),(P('C#6'),2)],
            [(P('F5'),2),(P('F#5'),2)]]
    for i, m in enumerate(melB):
        t = (12+i)*4
        pm.mel(t, m); arps(t, [chB[i]]); bassr(t, [rootsB[i]])
        wholer(t, [chB[i][:3]], 46)
    dr.beat(12, 'soft', 8, fill=True)
    # A' (bars 20-27)
    for i, m in enumerate(melA1):
        t = (20+i)*4
        pm.mel(t, m); arps(t, [chA[i % 4]]); bassr(t, [rootsA[i % 4]])
        wholer(t, [chA[i % 4][:3]], 46)
    dr.beat(20, 'soft', 8, fill=True)
    # coda (28-31)
    pm.mel(28*4, [(P('C#6'),1),(P('B5'),0.5),(P('A#5'),0.5),(P('G#5'),1),(P('F#5'),4)])
    arps(28*4, [chA[3], chA[0], chA[0], chA[0]])
    bassr(28*4, [P('C#2'),P('F#2'),P('F#2'),P('F#2')])
    wholer(28*4, [chA[3][:3]] + [chA[0][:3]]*3, 50)
    pm.mel(31*4, [(P('F#5'),4,70)])
    dr.beat(28, 'soft', 3); dr.d(30*4+3.5, Drums.CRASH, 45)
    return pc.save(os.path.join(OUT, '04_紫罗兰_基于未完成1_原创.mid'))

if __name__ == '__main__':
    print(piece_new_song())
    print(piece_unknown1())
    print(piece_unifish2())
    print(piece_unfinished1())
