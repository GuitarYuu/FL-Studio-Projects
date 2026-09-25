# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Piece, Trk, Drums, P

OUT = r"C:\Users\25448\Downloads\原创乐曲"

# ============================================================ 5. Track_02
def piece_track02():
    pc = Piece('Carousel Waltz (after Track_02.mid)', 120, 3, 4, 'Am')
    mel = pc.add(Trk('Accordion', 21, 0, vol=100, pan=64))
    pia = pc.add(Trk('Piano Comp', 0, 1, vol=72, pan=44))
    bass= pc.add(Trk('Acoustic Bass', 32, 2, vol=88, pan=52))
    dr  = pc.add(Drums(vol=62))
    Am=[P('A2'),P('E3'),P('A3'),P('C4')]; G=[P('G2'),P('D3'),P('G3'),P('B3')]
    Cc=[P('C3'),P('G3'),P('C4'),P('E4')]; F=[P('F2'),P('C3'),P('F3'),P('A3')]
    G7=[P('G2'),P('D3'),P('F3'),P('B3')]; Dm=[P('D3'),P('A3'),P('D4'),P('F4')]
    def comp(t, ch, dur=3):
        bass.n(t, 1.0, ch[0], 84)
        pia.chord(t+1, 1, ch[1:4], 62); pia.chord(t+2, 1, ch[1:4], 58)
    def waltz_drums(t, n):
        dr.beat(t, 'waltz', n, bpb=3)
    # 原旋律(A段动机)保留自 Track_02.mid, 去掉突兀的半音和弦链,改为规整小调进行
    melA1 = [[(P('E4'),1.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),0.5)],
             [(P('E4'),1),(None,0.5),(P('D4'),0.5),(P('B3'),0.5),(P('G3'),0.5)],
             [(P('C4'),1),(P('E4'),1),(P('G4'),1)],
             [(P('A4'),1.5),(P('G4'),0.5),(P('F4'),0.5),(P('D4'),0.5)],
             [(P('E4'),1.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),0.5)],
             [(P('C4'),1),(P('A3'),1),(P('F3'),1)],
             [(P('D4'),1),(P('C4'),1),(P('B3'),1)],
             [(P('E4'),1),(P('D4'),1),(P('C4'),1)]]
    progA = [Am,G,Cc,G,Am,F,G7,Am]
    # B 段(C大调区, 提升色彩)
    melB = [[(P('G4'),1),(P('A4'),0.5),(P('C5'),0.5),(P('E5'),1)],
            [(P('D5'),1.5),(P('C5'),0.5),(P('B4'),1)],
            [(P('A4'),1),(P('C5'),1),(P('F5'),1)],
            [(P('E5'),2),(None,1)],
            [(P('F5'),1),(P('E5'),1),(P('C5'),1)],
            [(P('D5'),1.5),(P('B4'),0.5),(P('G4'),1)],
            [(P('F4'),1),(P('E4'),1),(P('D4'),1)],
            [(P('C4'),1.5),(P('E4'),0.5),(P('E4'),1)]]
    AmFinal = [P('A2'),P('E3'),P('A3'),P('C4')]
    progB = [Cc,G,Dm,Cc,F,G7,Dm,AmFinal]
    # intro 4 bars
    for i, ch in enumerate([Am, G, Cc, G7]):
        comp(i*3, ch)
    mel.mel(2*3+2, [(P('E4'),0.5),(P('G4'),0.5)])
    waltz_drums(0, 4)
    # A (bars 4-11)
    for i, (m, ch) in enumerate(zip(melA1, progA)):
        t = (4+i)*3
        mel.mel(t, m); comp(t, ch)
    waltz_drums(4, 8)
    # A2 (bars 12-19): 第二遍,结尾变化(终止在E7属和弦)
    melA2 = [list(m) for m in melA1]
    melA2[6] = [(P('D4'),1),(P('C4'),1),(P('B3'),1)]
    melA2[7] = [(P('G#3'),1.5),(P('B3'),1.5)]
    for i, (m, ch) in enumerate(zip(melA2, progA)):
        t = (12+i)*3
        mel.mel(t, m); comp(t, ch)
    waltz_drums(12, 8)
    # B (bars 20-27)
    for i, m in enumerate(melB):
        t = (20+i)*3
        mel.mel(t, m); comp(t, progB[i])
    waltz_drums(20, 8)
    # A final (bars 28-35) 结尾大终止
    melA3 = [list(m) for m in melA1]
    melA3[7] = [(P('A4'),3)]
    for i, (m, ch) in enumerate(zip(melA3, progA)):
        t = (28+i)*3
        mel.mel(t, m); comp(t, ch)
    waltz_drums(28, 7)
    # coda (bars 36-37)
    mel.mel(36*3, [(P('E4'),0.5),(P('A4'),0.5),(P('C5'),0.5),(P('E5'),0.5),(P('A5'),1)])
    bass.n(36*3, 3, P('A2'), 84); pia.chord(36*3+1, 2, [P('E3'),P('A3'),P('C4')], 60)
    dr.d(36*3, Drums.CRASH, 55)
    return pc.save(os.path.join(OUT, '05_旋转木马圆舞曲_基于Track_02_原创.mid'))

# ============================================================ 6. unfinish
def piece_unfinish():
    pc = Piece('Echo and Answer (after unfinish.mid)', 100, 4, 4, 'Am')
    vio = pc.add(Trk('Violin', 40, 0, vol=98, pan=64))
    pia = pc.add(Trk('Piano', 0, 1, vol=76, pan=46))
    bass= pc.add(Trk('Bass', 32, 2, vol=86, pan=52))
    strs= pc.add(Trk('Strings', 48, 3, vol=50, pan=80))
    dr  = pc.add(Drums(vol=45))
    Am=[P('A2'),P('E3'),P('A3'),P('C4')]; F=[P('F2'),P('C3'),P('F3'),P('A3')]
    Cc=[P('C3'),P('G3'),P('C4'),P('E4')]; Dm=[P('D3'),P('A3'),P('D4'),P('F4')]
    E7=[P('E2'),P('B2'),P('D3'),P('G#3')]; G=[P('G2'),P('D3'),P('G3'),P('B3')]
    # 原旋律(修复: 低音C#2与旋律C4冲突->低音改为A; 音簇内声部->改为规整三和弦)
    melA = [[(P('E4'),1),(P('E4'),1),(P('E4'),1),(P('C4'),1)],
            [(P('E4'),1),(P('F4'),1),(P('E4'),2)],
            [(P('E4'),1),(P('E4'),1),(P('E4'),1),(P('C4'),1)],
            [(P('E4'),1),(P('F4'),1),(P('E4'),2)],
            [(P('G4'),1),(P('F4'),1),(P('F4'),1),(P('F4'),1)],
            [(P('E4'),1),(P('E4'),1),(P('E4'),1),(P('E4'),1)],
            [(P('D4'),1),(P('D4'),1),(P('A3'),1),(P('C4'),1)],
            [(P('D4'),1.5),(P('E4'),0.5),(P('D4'),2)]]
    progA = [Am,F,Am,F,Cc,Am,Dm,E7]
    melB = [[(P('E4'),1),(P('G4'),1),(P('C5'),1),(P('G4'),1)],
            [(P('A4'),1),(P('C5'),1),(P('B4'),1),(P('A4'),1)],
            [(P('F4'),1),(P('A4'),1),(P('C5'),1),(P('A4'),1)],
            [(P('G4'),1),(P('B4'),1),(P('D5'),2)],
            [(P('E4'),1),(P('G4'),1),(P('C5'),1),(P('G4'),1)],
            [(P('A4'),1),(P('C5'),1),(P('E5'),1),(P('C5'),1)],
            [(P('D5'),1),(P('C5'),1),(P('A4'),1),(P('F4'),1)],
            [(P('G#4'),1),(P('B4'),1),(P('D5'),1),(P('B4'),1)]]
    progB = [Cc,Am,F,G,Cc,Am,Dm,E7]
    def bar(t, ch):
        pia.chord(t, 2, ch[1:4], 58); pia.chord(t+2, 2, ch[1:4], 54)
        bass.n(t, 2, ch[0], 84); bass.n(t+2, 2, ch[0]+7, 78)
    # intro 2 bars
    bar(0, Am); bar(4, Am)
    vio.mel(4, [(P('E4'),1),(P('G4'),1),(P('A4'),2)])
    # A x2 (bars 2-17)
    for rep in range(2):
        for i, (m, ch) in enumerate(zip(melA, progA)):
            t = (2+rep*8+i)*4
            vio.mel(t, m); bar(t, ch); strs.chord(t, 4, ch[1:4], 38)
    dr.beat(2, 'soft', 16)
    # B (bars 18-25)
    for i, (m, ch) in enumerate(zip(melB, progB)):
        t = (18+i)*4
        vio.mel(t, m); bar(t, ch); strs.chord(t, 4, ch[1:4], 44)
    dr.beat(18, 'soft', 8, fill=True)
    # A' (bars 26-33): 末句上扬收束
    melA3 = [list(m) for m in melA]
    melA3[6] = [(P('D4'),1),(P('D4'),1),(P('G4'),1),(P('A4'),1)]
    melA3[7] = [(P('B4'),1.5),(P('C5'),0.5),(P('A4'),2)]
    for i, (m, ch) in enumerate(zip(melA3, progA)):
        t = (26+i)*4
        vio.mel(t, m); bar(t, ch); strs.chord(t, 4, ch[1:4], 46)
    dr.beat(26, 'soft', 8)
    # coda (bars 34-35)
    vio.mel(34*4, [(P('A4'),1),(P('G4'),1),(P('E4'),2)])
    bar(34*4, Am); strs.chord(34*4, 8, [P('A3'),P('C4'),P('E4')], 48)
    vio.mel(35*4, [(P('A4'),4,80)])
    dr.d(35*4, Drums.CRASH, 45)
    return pc.save(os.path.join(OUT, '06_回声与答案_基于unfinish_原创.mid'))

# ============================================================ 7. sunny day
def piece_sunnyday():
    pc = Piece('Sunny Day Stroll (after sunny day.mid)', 92, 4, 4, 'C')
    gm  = pc.add(Trk('Nylon Guitar Melody', 24, 0, vol=100, pan=64))
    ga  = pc.add(Trk('Nylon Guitar Arp', 24, 1, vol=76, pan=44))
    bass= pc.add(Trk('Acoustic Bass', 32, 2, vol=84, pan=52))
    dr  = pc.add(Drums(vol=48))
    C=[P('C3'),P('E3'),P('G3'),P('C4')]; G=[P('G2'),P('B2'),P('D3'),P('G3')]
    Am=[P('A2'),P('C3'),P('E3'),P('A3')]; F=[P('F2'),P('A2'),P('C3'),P('F3')]
    G7=[P('G2'),P('B2'),P('D3'),P('F3')]; Fm=[P('F2'),P('G#2'),P('C3'),P('F3')]
    def arp(t, ch, n=8, vel=62):
        seq = [0,1,2,3,2,1,2,3][:n]
        for i, k in enumerate(seq):
            ga.n(t+i*0.5, 0.85, ch[k], vel)
    def bb(t, ch, vel=80):
        bass.n(t, 1.5, ch[0], vel); bass.n(t+2, 1.5, ch[0]+7, vel-6)
    # Verse 旋律(取自 sunny day.mid 的音高素材,节奏重写)
    V1 = [[(P('C4'),1),(P('E4'),1),(P('D4'),1),(P('E4'),1)],
          [(P('D4'),1),(P('C4'),2),(None,1)],
          [(P('E4'),1),(P('D4'),1),(P('E4'),1),(P('D4'),1)],
          [(P('D4'),2),(None,1),(P('B3'),0.5),(P('C4'),0.5)],
          [(P('C4'),1),(P('E4'),1),(P('D4'),1),(P('E4'),1)],
          [(P('F4'),1),(P('E4'),1),(P('D4'),1),(P('C4'),1)],
          [(P('D4'),1),(P('E4'),1),(P('F4'),1),(P('D4'),1)],
          [(P('C4'),3),(None,1)]]
    progV = [C,G,G,C,Am,F,G7,C]
    # Chorus 旋律(取自高音素材 C5 C5 C5 A4 / G5 F5 E5 C5)
    CH = [[(P('C5'),1),(P('C5'),1),(P('C5'),1),(P('A4'),1)],
          [(P('C5'),2),(P('B4'),0.5),(P('C5'),0.5),(None,0.5),(P('G4'),0.5)],
          [(P('A4'),1),(P('C5'),1),(P('E5'),1),(P('C5'),1)],
          [(P('B4'),1.5),(P('G4'),1.5),(None,1)],
          [(P('C5'),1),(P('C5'),1),(P('C5'),1),(P('A4'),1)],
          [(P('B4'),1),(P('D5'),1),(P('B4'),1),(P('G4'),1)],
          [(P('C5'),1),(P('D5'),1),(P('E5'),1),(P('D5'),1)],
          [(P('C5'),3),(None,1)]]
    progC = [F,C,Am,G,F,G7,C,C]
    # intro 4 bars
    for i, ch in enumerate([C, G, Am, G7]):
        arp(i*4, ch); bb(i*4, ch)
    dr.beat(0, 'soft', 4, fill=True)
    gm.mel(3*4, [(P('E4'),0.5),(P('G4'),0.5)])
    # V1 (bars 4-11)
    for i, (m, ch) in enumerate(zip(V1, progV)):
        t = (4+i)*4; gm.mel(t, m); arp(t, ch); bb(t, ch)
    dr.beat(4, 'soft', 8)
    # V2 (bars 12-19) 加花
    V2 = [list(m) for m in V1]
    V2[1] = [(P('D4'),1),(P('C4'),1),(P('E4'),0.5),(P('D4'),0.5),(P('C4'),1)]
    V2[5] = [(P('F4'),0.5),(P('G4'),0.5),(P('A4'),1),(P('G4'),1),(P('F4'),1)]
    V2[7] = [(P('C4'),2),(None,0.5),(P('E4'),0.5),(P('G4'),0.5),(P('A4'),0.5)]
    for i, (m, ch) in enumerate(zip(V2, progV)):
        t = (12+i)*4; gm.mel(t, m); arp(t, ch); bb(t, ch)
    dr.beat(12, 'soft', 8, fill=True)
    # Chorus (bars 20-27)
    for i, (m, ch) in enumerate(zip(CH, progC)):
        t = (20+i)*4; gm.mel(t, m); arp(t, ch); bb(t, ch)
    dr.beat(20, 'soft', 8, fill=True)
    # V3 (bars 28-35) 弱处理
    for i, (m, ch) in enumerate(zip(V1, progV)):
        t = (28+i)*4
        gm.mel(t, [(p, d, 78) for p, d in m]); arp(t, ch, vel=54); bb(t, ch, vel=72)
    dr.beat(28, 'soft', 8)
    # Chorus2 (bars 36-43) 结尾变化
    CH2 = [list(m) for m in CH]
    CH2[7] = [(P('E5'),1),(P('D5'),1),(P('C5'),2)]
    for i, (m, ch) in enumerate(zip(CH2, progC)):
        t = (36+i)*4; gm.mel(t, m); arp(t, ch); bb(t, ch)
    dr.beat(36, 'soft', 8)
    # outro (44-47)
    gm.mel(44*4, [(P('E4'),0.5),(P('G4'),0.5),(P('C5'),0.5),(P('E5'),0.5),(P('G5'),2)])
    for i, ch in enumerate([F, G7, C]):
        arp((45+i)*4, ch); bb((45+i)*4, ch)
    gm.mel(45*4, [(P('E5'),1),(P('D5'),1),(P('C5'),2)])
    gm.mel(46*4, [(P('D5'),1),(P('B4'),1),(P('C5'),2)])
    gm.mel(47*4, [(P('C5'),4,76)])
    dr.d(47*4, Drums.CRASH, 45)
    return pc.save(os.path.join(OUT, '07_晴天散步_基于sunny day_原创.mid'))

# ============================================================ 8. sunny day2
def piece_sunnyday2():
    pc = Piece('Midsummer (after sunny day2.mid)', 100, 4, 4, 'C')
    pia = pc.add(Trk('Piano Melody', 0, 0, vol=100, pan=64))
    pc2 = pc.add(Trk('Piano Comp', 0, 1, vol=70, pan=44))
    bass= pc.add(Trk('Finger Bass', 33, 2, vol=86, pan=52))
    strs= pc.add(Trk('Strings', 48, 3, vol=54, pan=84))
    dr  = pc.add(Drums(vol=64))
    C=[P('C3'),P('E3'),P('G3')]; G=[P('G2'),P('B2'),P('D3')]
    Am=[P('A2'),P('C3'),P('E3')]; F=[P('F2'),P('A2'),P('C3')]
    G7=[P('G2'),P('B2'),P('D3'),P('F3')]; Dm=[P('D3'),P('F3'),P('A3')]
    Em=[P('E2'),P('G2'),P('B2')]
    def comp8(t, ch):
        seq = [0,1,2,1,0,1,2,1]
        for i, k in enumerate(seq):
            pc2.n(t+i*0.5, 0.45, ch[k], 58)
    def bb(t, ch):
        bass.n(t, 0.75, ch[0], 86); bass.n(t+1, 0.75, ch[0], 80)
        bass.n(t+2, 0.75, ch[0]+7, 82); bass.n(t+3, 0.75, ch[0], 80)
    # A 段(sunny day2 素材: C E D E D C / A G / D E F D E C)
    A1 = [[(P('C4'),1),(P('E4'),1),(P('D4'),1),(P('E4'),1)],
          [(P('D4'),1),(P('C4'),1.5),(None,0.5),(P('G3'),1)],
          [(P('C4'),1),(P('E4'),1),(P('D4'),1),(P('E4'),1)],
          [(P('A4'),1.5),(P('G4'),1.5),(None,1)],
          [(P('G4'),1),(P('F4'),1),(P('E4'),1),(P('G4'),1)],
          [(P('A4'),1),(P('G4'),1),(P('E4'),1),(P('D4'),1)],
          [(P('E4'),0.5),(P('D4'),0.5),(P('E4'),0.5),(P('F4'),0.5),(P('D4'),1),(P('E4'),1)],
          [(P('C4'),3),(None,1)]]
    progA = [C,G,Am,C,F,G7,G7,C]
    # B 段(相对小调区, 素材 E D E D C)
    B1 = [[(P('E5'),2),(P('C5'),1),(P('A4'),1)],
          [(P('F4'),1),(P('A4'),1),(P('C5'),1),(P('E5'),1)],
          [(P('D5'),1.5),(P('C5'),0.5),(P('B4'),2)],
          [(P('G4'),1),(P('B4'),1),(P('D5'),1),(P('B4'),1)],
          [(P('E5'),2),(P('C5'),1),(P('A4'),1)],
          [(P('D5'),1),(P('C5'),1),(P('A4'),1),(P('F4'),1)],
          [(P('G4'),1),(P('A4'),1),(P('B4'),1),(P('C5'),1)],
          [(P('D5'),2),(None,2)]]
    progB = [Am,F,G7,G,Am,F,G7,G]
    # C 段(高音区素材 C5 C5 C5 A4 C5 / G5 F5 E5 C5 D5 C5 D5 E5)
    C1 = [[(P('C5'),1),(P('C5'),0.5),(P('C5'),0.5),(P('A4'),1),(P('C5'),1)],
          [(P('G5'),1),(P('F5'),1),(P('E5'),2)],
          [(P('C5'),1),(P('D5'),1),(P('C5'),1),(P('D5'),1)],
          [(P('E5'),2),(P('G4'),1),(None,1)],
          [(P('E5'),1),(P('F5'),1),(P('E5'),1),(P('D5'),1)],
          [(P('E5'),1),(P('F5'),1),(P('E5'),1),(P('C5'),1)],
          [(P('B4'),1),(P('G4'),1),(P('F4'),1),(P('E4'),1)],
          [(P('C4'),3),(None,1)]]
    progC = [F,C,Am,C,F,G7,C,C]
    # intro 4
    for i, ch in enumerate([C, G, Am, G7]):
        comp8(i*4, ch); bb(i*4, ch)
    pia.mel(3*4, [(P('E4'),0.5),(P('G4'),0.5),(P('C5'),1)])
    dr.beat(0, 'rock', 4, fill=True)
    # A x2 (bars 4-19)
    for rep in range(2):
        ms = A1 if rep == 0 else [list(m) for m in A1]
        if rep == 1:
            ms[1] = [(P('D4'),1),(P('C4'),1),(P('E4'),0.5),(P('D4'),0.5),(P('C4'),1)]
            ms[7] = [(P('C4'),2),(None,0.5),(P('E4'),0.5),(P('G4'),0.5),(P('A4'),0.5)]
        for i, (m, ch) in enumerate(zip(ms, progA)):
            t = (4+rep*8+i)*4
            pia.mel(t, m); comp8(t, ch); bb(t, ch); strs.chord(t, 4, ch[1:3], 36)
    dr.beat(4, 'rock', 16, fill=True)
    # B (bars 20-27)
    for i, (m, ch) in enumerate(zip(B1, progB)):
        t = (20+i)*4
        pia.mel(t, m); comp8(t, ch); bb(t, ch); strs.chord(t, 4, ch[1:3], 44)
    dr.beat(20, 'rock', 8, fill=True)
    # C (bars 28-35)
    for i, (m, ch) in enumerate(zip(C1, progC)):
        t = (28+i)*4
        pia.mel(t, m); comp8(t, ch); bb(t, ch); strs.chord(t, 4, ch[1:3], 46)
    dr.beat(28, 'rock', 8, fill=True)
    # A (36-43) 弱
    for i, (m, ch) in enumerate(zip(A1, progA)):
        t = (36+i)*4
        pia.mel(t, [(p, d, 82) for p, d in m]); comp8(t, ch); bb(t, ch); strs.chord(t, 4, ch[1:3], 38)
    dr.beat(36, 'soft', 8)
    # C2 (44-51) 终段
    C2 = [list(m) for m in C1]
    C2[7] = [(P('E5'),1),(P('D5'),1),(P('C5'),2)]
    for i, (m, ch) in enumerate(zip(C2, progC)):
        t = (44+i)*4
        pia.mel(t, m); comp8(t, ch); bb(t, ch); strs.chord(t, 4, ch[1:3], 48)
    dr.beat(44, 'rock', 8)
    # outro (52-55)
    pia.mel(52*4, [(P('E4'),0.5),(P('G4'),0.5),(P('C5'),0.5),(P('E5'),0.5),(P('G5'),2)])
    for i, ch in enumerate([F, G7, C]):
        comp8((53+i)*4, ch); bb((53+i)*4, ch)
    pia.mel(53*4, [(P('F5'),1),(P('E5'),1),(P('D5'),2)])
    pia.mel(54*4, [(P('D5'),1),(P('B4'),1),(P('C5'),2)])
    pia.mel(55*4, [(P('C5'),4,80)])
    strs.chord(52*4, 16, [P('C3'),P('E3'),P('G3'),P('C4')], 44)
    dr.d(55*4, Drums.CRASH, 50)
    return pc.save(os.path.join(OUT, '08_盛夏_基于sunny day2_原创.mid'))

if __name__ == '__main__':
    print(piece_track02())
    print(piece_unfinish())
    print(piece_sunnyday())
    print(piece_sunnyday2())
