# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Piece, Trk, Drums, P

OUT = r"C:\Users\25448\Downloads\原创乐曲"

# ============================================================ 9. o.mid
def piece_o():
    pc = Piece('Letter by the Sea (after o.mid)', 96, 4, 4, 'Bb')
    pm  = pc.add(Trk('Piano Melody', 0, 0, vol=100, pan=64))
    pa  = pc.add(Trk('Piano Comp', 0, 1, vol=70, pan=44))
    bass= pc.add(Trk('Acoustic Bass', 32, 2, vol=82, pan=52))
    strs= pc.add(Trk('Strings', 48, 3, vol=52, pan=82))
    # 和声: Bb Eb Bb F | Bb Gm Eb F  (原素材为同音列的小调侧写, 取关系大调重释)
    Bb=[P('A#2'),P('D3'),P('F3')]; Eb=[P('D#2'),P('G2'),P('A#2')]
    F =[P('F2'),P('A2'),P('C3')];  Gm=[P('G2'),P('A#2'),P('D3')]
    Cm=[P('C3'),P('D#3'),P('G3')]; F7=[P('F2'),P('A2'),P('D#3')]
    def comp(t, ch, dur=4):
        pa.chord(t, 2, ch, 56); pa.chord(t+2, 1.5, ch, 50)
        bass.n(t, 1.5, ch[0], 76); bass.n(t+2, 1, ch[0]+7, 70); bass.n(t+3, 1, ch[2], 70)
    def pad(t, ch, vel=40):
        strs.chord(t, 4, [c+12 for c in ch], vel)
    # A1 动机来自 o.mid: D D C D F / D D C D G
    A1 = [[(P('D4'),0.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),0.5),(P('F4'),1),(None,1)],
          [(P('D4'),0.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),0.5),(P('G4'),1),(None,1)],
          [(P('D4'),0.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),0.5),(P('F4'),0.5),(P('G4'),0.5),(P('A4'),0.5),(P('G4'),0.5)],
          [(P('F4'),2.5),(None,1.5)],
          [(P('D5'),0.5),(P('D5'),0.5),(P('C5'),0.5),(P('D5'),0.5),(P('F5'),1),(None,1)],
          [(P('D5'),0.5),(P('C5'),0.5),(P('B4'),0.5),(P('C5'),0.5),(P('D5'),1),(None,1)],
          [(P('D#5'),1),(P('D5'),0.5),(P('C5'),0.5),(P('A#4'),1),(P('C5'),1)],
          [(P('A4'),1.5),(P('F4'),0.5),(P('D4'),2)]]
    progA = [Bb,Eb,Bb,F,Bb,Gm,Eb,F]
    # B 段
    B1 = [[(P('G4'),0.5),(P('A#4'),0.5),(P('D5'),1),(P('D#5'),1),(P('D5'),1)],
          [(P('D5'),0.5),(P('A#4'),0.5),(P('G4'),1),(P('A4'),1),(P('A#4'),1)],
          [(P('C5'),1),(P('D5'),1),(P('D#5'),1),(P('F5'),1)],
          [(P('F5'),1.5),(P('D#5'),0.5),(P('D5'),2)],
          [(P('G4'),0.5),(P('A#4'),0.5),(P('D5'),1),(P('D#5'),1),(P('G5'),1)],
          [(P('F5'),2),(P('D5'),1),(None,1)],
          [(P('D#5'),1),(P('D5'),1),(P('C5'),1),(P('A#4'),1)],
          [(P('A4'),2),(P('C5'),1),(None,1)]]
    progB = [Eb,Gm,Cm,F,Eb,Bb,Cm,F7]
    # intro 4 bars
    for i, ch in enumerate([Bb, Eb, Bb, F]):
        comp(i*4, ch); pad(i*4, ch)
    pm.mel(3*4, [(P('F4'),0.5),(P('G4'),0.5),(P('A4'),1)])
    # A (bars 4-11) x2
    for rep in range(2):
        ms = A1 if rep == 0 else [list(m) for m in A1]
        if rep == 1:
            ms[7] = [(P('C5'),1),(P('B4'),0.5),(P('A4'),0.5),(P('F4'),2)]
        for i, (m, ch) in enumerate(zip(ms, progA)):
            t = (4+rep*8+i)*4
            pm.mel(t, m); comp(t, ch); pad(t, ch)
    # B (bars 20-27)
    for i, (m, ch) in enumerate(zip(B1, progB)):
        t = (20+i)*4
        pm.mel(t, m); comp(t, ch); pad(t, ch, 44)
    # A' (bars 28-35) pp 复述
    for i, (m, ch) in enumerate(zip(A1, progA)):
        t = (28+i)*4
        pm.mel(t, [(p, d, min(86, 92)) for p, d in m]); comp(t, ch); pad(t, ch, 38)
    # coda (bars 36-39)
    pm.mel(36*4, [(P('D5'),1),(P('C5'),0.5),(P('B4'),0.5),(P('A4'),1),(P('A#4'),4)])
    for i, ch in enumerate([Eb, F7, Bb, Bb]):
        comp((36+i)*4, ch)
        strs.chord((36+i)*4, 4, [c+12 for c in ch], 44 if i < 3 else 30)
    pm.mel(39*4, [(P('B4'),4,66)])
    return pc.save(os.path.join(OUT, '09_海边的信_基于o_原创.mid'))

# ============================================================ 10. New Song2
def piece_newsong2():
    pc = Piece('Daybreak (after New Song2.mid)', 140, 4, 4, 'Gm')
    lead= pc.add(Trk('Lead Saw', 81, 0, vol=104, pan=66))
    harm= pc.add(Trk('Square Counter', 80, 1, vol=66, pan=40))
    bass= pc.add(Trk('Synth Bass', 38, 2, vol=94, pan=52))
    cho = pc.add(Trk('Overdrive Stabs', 29, 3, vol=70, pan=76))
    dr  = pc.add(Drums(vol=86))
    Gm=[P('G3'),P('A#3'),P('D4')]; Eb=[P('G#2'),P('C3'),P('D#3')]
    F =[P('F2'),P('A2'),P('C3')];  D7=[P('D3'),P('F#3'),P('A3'),P('C4')]
    Cm=[P('C3'),P('D#3'),P('G3')]; Bb=[P('A#2'),P('D3'),P('F3')]
    def b8(t, r, pat=None, vel=86):
        pat = pat or [0,12,0,12,0,12,0,12]
        for i, off in enumerate(pat):
            bass.n(t+i*0.5, 0.47, r+off, vel)
    # A 段 riff (来自 New Song2/o 的音高序): D D C D F ...
    riffA1 = [(P('D4'),0.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),0.5),(P('F4'),0.5),(P('D4'),0.5),(P('D4'),0.5),(P('C4'),0.5)]
    riffA2 = [(P('D4'),0.5),(P('G4'),0.5),(P('D4'),0.5),(P('D4'),0.5),(P('C4'),0.5),(P('D4'),1.5)]
    riffA3 = [(P('A4'),1),(P('A4'),1),(P('A4'),0.5),(P('G4'),0.5),(P('A4'),1)]
    riffA4 = [(P('G4'),1),(P('A4'),1),(P('D4'),2)]
    progA = [P('G2'),P('G2'),P('D#2'),P('F2'),P('G2'),P('G2'),P('D#2'),P('D2')]
    # C 段 (C5 区): C C Bb C F C / G G G F F G
    C1 = [[(P('C5'),0.5),(P('C5'),0.5),(P('A#4'),0.5),(P('C5'),0.5),(P('F5'),0.5),(P('C5'),0.5),(P('C5'),0.5),(P('C5'),0.5)],
          [(P('G5'),0.5),(P('G5'),0.5),(P('G5'),0.5),(P('F5'),0.5),(P('F5'),0.5),(P('G5'),1),(None,0.5)],
          [(P('C5'),0.5),(P('C5'),0.5),(P('A#4'),0.5),(P('C5'),0.5),(P('D#5'),0.5),(P('C5'),0.5),(P('C5'),0.5),(P('A4'),0.5)],
          [(P('D5'),1),(P('C5'),1),(P('A4'),2)]]
    progC = [P('C2'),P('G2'),P('C2'),P('D2')]
    # D 段 (D6 高潮): D6 D6 D6 Bb5 C6 C6 D6 / F5 D6...
    D1 = [[(P('D6'),0.5),(P('D6'),0.5),(P('D6'),0.5),(P('A#5'),0.5),(P('C6'),0.5),(P('C6'),0.5),(P('D6'),0.5),(P('F5'),0.5)],
          [(P('D6'),0.5),(P('D6'),0.5),(P('D6'),0.5),(P('A#5'),0.5),(P('C6'),0.5),(P('C6'),0.5),(P('D6'),0.5),(P('F6'),0.5)],
          [(P('A#5'),1),(P('D6'),1),(P('G5'),0.5),(P('F5'),0.5),(P('F5'),0.5),(P('G5'),0.5)],
          [(P('A5'),0.5),(P('A5'),0.5),(P('C6'),0.5),(P('C6'),0.5),(P('D6'),2)]]
    progD = [P('G2'),P('D#2'),P('G2'),P('F2')]
    # intro 4 bars
    b8(0, P('G2')); b8(4, P('G2'), pat=[0,0,12,0,0,12,0,0])
    b8(8, P('D#2')); b8(12, P('F2'), pat=[0,0,12,0,0,12,0,0])
    dr.beat(0, 'rock', 4, fill=True)
    # A (bars 4-11)
    for i in range(8):
        t = (4+i)*4
        b8(t, progA[i])
        if i < 4:
            lead.mel(t, riffA1 if i % 2 == 0 else riffA2)
        else:
            lead.mel(t, riffA3 if i % 2 == 0 else riffA4)
        ch = [Gm, Gm, Eb, F][i % 4]
        cho.chord(t+1.5, 0.5, ch, 66); cho.chord(t+3, 0.5, ch, 60)
    dr.beat(4, 'rock', 8, fill=True)
    # C (bars 12-19): C1 x2 + riffA 收尾
    for i in range(8):
        t = (12+i)*4
        b8(t, progC[i % 4])
        lead.mel(t, C1[i % 4])
        ch = [Cm, Gm, Cm, D7][i % 4]
        cho.chord(t+1.5, 0.5, ch, 66); cho.chord(t+3, 0.5, ch, 60)
        if i % 4 == 3:
            harm.mel(t, [(P('F4'),2),(P('A4'),2)], 60)
    dr.beat(12, 'rock', 8, fill=True)
    # D (bars 20-27): 高潮
    for i in range(8):
        t = (20+i)*4
        b8(t, progD[i % 4])
        lead.mel(t, D1[i % 4])
        ch = [Gm, Eb, Gm, F][i % 4]
        cho.chord(t+1.5, 0.5, ch, 70); cho.chord(t+3, 0.5, ch, 64)
    dr.beat(20, 'rock', 8, fill=True)
    # A' (bars 28-35): 高八度
    for i in range(8):
        t = (28+i)*4
        b8(t, progA[i], pat=[0,12,0,12,3,12,0,12] if i % 4 == 3 else None)
        src = riffA1 if i % 2 == 0 else (riffA2 if i < 6 else riffA4)
        lead.mel(t, [(p+12, d) for p, d in src])
        ch = [Gm, Gm, Eb, F][i % 4]
        cho.chord(t+1.5, 0.5, ch, 66); cho.chord(t+3, 0.5, ch, 60)
    dr.beat(28, 'rock', 8, fill=True)
    # coda (bars 36-39): D5 尾奏 riff 渐弱
    tail = [(P('D5'),0.5),(P('D5'),0.5),(P('C5'),0.5),(P('D5'),0.5),(P('A#4'),1),(None,1)]
    tail2 = [(P('C5'),0.5),(P('C5'),0.5),(P('A#4'),0.5),(P('C5'),0.5),(P('G4'),1),(None,1)]
    codach = [P('G2'),P('D#2'),P('F2'),P('G2')]
    for i in range(4):
        t = (36+i)*4
        b8(t, codach[i], vel=82-i*6)
        lead.mel(t, tail if i % 2 == 0 else tail2)
        ch = [Gm, Eb, F, Gm][i]
        cho.chord(t, 1, ch, 60-i*6)
    dr.beat(36, 'rock', 4); dr.d(39*4+3.5, Drums.CRASH, 45)
    lead.mel(39*4+3.5, [(P('D5'),0.5,70)])
    return pc.save(os.path.join(OUT, '10_破晓_基于New Song2_原创.mid'))

# ============================================================ 11. 前辈(1).mp3.mid
def piece_senpai():
    pc = Piece('Senpai Blues (after qianbei.mp3.mid)', 120, 4, 4, 'F')
    pm  = pc.add(Trk('Piano Lead', 0, 0, vol=100, pan=60))
    pc2 = pc.add(Trk('Piano Comp', 0, 1, vol=66, pan=44))
    bass= pc.add(Trk('Walking Bass', 32, 2, vol=88, pan=52))
    dr  = pc.add(Drums(vol=74))
    # 和弦: 根音, 三音, 五音, 七音 (用于 comp 与 walking bass)
    F7 =(P('F2'),4,7,10); Bb7=(P('A#1'),4,7,10); D7=(P('D2'),4,7,10)
    Gm7=(P('G2'),3,7,10); C7 =(P('C2'),4,7,10); E7=(P('E2'),4,7,10)
    Eb7=(P('D#2'),4,7,10); Db7=(P('C#2'),4,7,10)
    def walk(t, ch, nxt_root=None):
        r, third, fifth, sev = ch[0], ch[0]+ch[1], ch[0]+ch[2], ch[0]+ch[3]
        notes = [r, third, fifth, sev]
        if nxt_root is not None:
            d = nxt_root - r
            if d > 6: d -= 12
            if d < -6: d += 12
            notes[3] = r + d
        for i, n in enumerate(notes):
            bass.n(t+i, 0.95, n, 84)
    def stab(t, ch, dur=0.5, vel=60):
        r = ch[0]
        pc2.chord(t, dur, [r+12+ch[1], r+12+ch[3], r+24+ch[2]], vel)  # rootless-ish voicing
    def s(a):  # swing pair
        return 0.66, 0.34
    def BLUES12(t0, variant=0):
        """12小节 F 布鲁斯, 旋律用 F 布鲁斯音阶(F Ab Bb B C Eb), 素材来自源文件的 F7 琶音"""
        ch_prog = [F7, Bb7, F7, F7, Bb7, Bb7, F7, D7, Gm7, C7, F7, Gm7]
        chord2  = [None, None, None, None, None, None, None, None, None, None, D7, C7]
        roots   = [c[0] for c in ch_prog]
        m = [[] for _ in range(12)]
        # b1 F7
        m[0] = [(P('F4'),0.66),(P('G#4'),0.34),(P('C5'),0.66),(P('G#4'),0.34),(P('F4'),1),(P('C4'),1)]
        # b2 Bb7
        m[1] = [(P('D5'),0.66),(P('C5'),0.34),(P('A#4'),0.66),(P('G#4'),0.34),(P('F4'),2)]
        # b3 F7
        m[2] = [(P('F4'),0.66),(P('G4'),0.34),(P('A4'),0.66),(P('C5'),0.34),(P('A4'),2)]
        # b4 F7
        m[3] = [(P('C5'),0.66),(P('D5'),0.34),(P('D#5'),0.66),(P('D5'),0.34),(P('C5'),1),(P('A4'),1)]
        # b5 Bb7
        m[4] = [(P('A#4'),0.66),(P('C5'),0.34),(P('D5'),0.66),(P('D#5'),0.34),(P('D5'),1),(P('C5'),1)]
        # b6 Bb7
        m[5] = [(P('A#4'),0.66),(P('G#4'),0.34),(P('F4'),1),(P('D4'),2)]
        # b7 F7
        m[6] = [(P('F4'),0.66),(P('A4'),0.34),(P('C5'),0.66),(P('D#5'),0.34),(P('A4'),1),(P('F4'),1)]
        # b8 D7
        m[7] = [(P('D5'),0.66),(P('A4'),0.34),(P('F#4'),0.66),(P('A4'),0.34),(P('D4'),1),(P('F#4'),1)]
        # b9 Gm7
        m[8] = [(P('G4'),0.66),(P('A#4'),0.34),(P('D5'),1),(P('A#4'),1),(P('G4'),1)]
        # b10 C7
        m[9] = [(P('C5'),0.66),(P('E5'),0.34),(P('A#4'),1),(P('G4'),1),(P('E4'),1)]
        # b11 F7->D7
        m[10] = [(P('A4'),0.66),(P('C5'),0.34),(P('A4'),0.66),(P('F4'),0.34),(P('D5'),2)] if variant == 0 else \
                [(P('D5'),0.66),(P('C5'),0.34),(P('A4'),0.66),(P('F4'),0.34),(P('D5'),2)]
        # b12 Gm7->C7
        m[11] = [(P('G4'),0.66),(P('A#4'),0.34),(P('D5'),1),(P('A#4'),1)] if variant == 0 else \
                [(P('G4'),0.66),(P('A4'),0.34),(P('A#4'),0.66),(P('C5'),0.34),(P('E5'),1)]
        if variant == 2:
            m[11] = [(P('A4'),1),(P('C5'),1),(P('F5'),2)]
        for i in range(12):
            t = t0 + i*4
            pm.mel(t, m[i])
            nxt = roots[i+1] if i < 11 else P('F2')
            walk(t, ch_prog[i], nxt)
            stabs = [1.5, 3.0] if i % 2 == 0 else [0.5, 2.5]
            for st in stabs:
                stab(t+st, ch_prog[i])
            if chord2[i] is not None:
                stab(t+3, chord2[i], 0.5, 56)
        dr.swing(t0 // 4, 12, fill=True)
        return t0 + 48
    def BRIDGE(t0):
        chs = [F7, E7, Eb7, D7, Gm7, C7, F7, Bb7]
        mels = [[(P('A4'),0.66),(P('C5'),0.34),(P('D#5'),0.66),(P('C5'),0.34),(P('A4'),1),(P('F4'),1)],
                [(P('G#4'),0.66),(P('B4'),0.34),(P('D5'),0.66),(P('B4'),0.34),(P('G#4'),1),(P('E4'),1)],
                [(P('G4'),0.66),(P('A#4'),0.34),(P('C#5'),0.66),(P('A#4'),0.34),(P('G4'),1),(P('D#4'),1)],
                [(P('F#4'),0.66),(P('A4'),0.34),(P('C5'),0.66),(P('A4'),0.34),(P('F#4'),1),(P('D4'),1)],
                [(P('G4'),1),(P('A#4'),1),(P('D5'),2)],
                [(P('E5'),0.66),(P('D5'),0.34),(P('C5'),0.66),(P('A#4'),0.34),(P('G4'),1),(P('E4'),1)],
                [(P('F4'),0.66),(P('G4'),0.34),(P('A4'),0.66),(P('C5'),0.34),(P('A4'),1),(P('F4'),1)],
                [(P('D5'),1),(P('C5'),1),(P('A#4'),2)]]
        roots = [c[0] for c in chs]
        for i in range(8):
            t = t0 + i*4
            pm.mel(t, mels[i])
            nxt = roots[i+1] if i < 7 else P('F2')
            walk(t, chs[i], nxt)
            for st in ([1.5, 3.0] if i % 2 == 0 else [0.5, 2.5]):
                stab(t+st, chs[i])
        dr.swing(t0 // 4, 8, fill=True)
        return t0 + 32
    # intro 4 bars: 鼓 + 贝斯铺垫 + 钢琴钩子
    for i, ch in enumerate([F7, F7, Bb7, C7]):
        walk(i*4, ch, [F7,F7,Bb7,C7][i][0]+0)
        stab(i*4+1.5, ch, 0.5, 58); stab(i*4+3, ch, 0.5, 54)
    dr.swing(0, 4, fill=True)
    pm.mel(12, [(P('C5'),0.66),(P('D#5'),0.34),(P('C5'),0.66),(P('A4'),0.34),(P('F4'),1)])
    # Blues 1 (bars 4-15)
    t = 16; t = BLUES12(t, 0)
    # Blues 2 (bars 16-27)
    t = BLUES12(t, 1)
    # Bridge (bars 28-35): F7 E7 Eb7 D7 下行属和弦链 (源自原文件的和声骨架)
    t = BRIDGE(t)
    # Blues 3 (bars 36-47) 终段
    t = BLUES12(t, 2)
    # outro 4 bars: F7 E7 D7 Db7 -> F 停留
    outs = [F7, E7, D7, Db7]
    for i, ch in enumerate(outs):
        t2 = t + i*4
        walk(t2, ch, outs[i+1][0] if i < 3 else P('F2'))
        pm.mel(t2, [(P('A4'),0.66),(P('C5'),0.34),(P('D#5'),0.66),(P('C5'),0.34),(P('A4'),1),(P('F4'),1)] if i == 0 else
                  [(ch[0]+12+ch[1]+12,2)] )  # 各和弦三音: A4->G#4->F#4->F4 下行
        for st in [1.5, 3.0]:
            stab(t2+st, ch, 0.5, 56)
    dr.swing(t // 4, 4, fill=True)
    # final F7 chord
    pm.chord(t+16, 4, [P('F3'),P('A3'),P('C4'),P('D#4'),P('F4')], 80)
    bass.n(t+16, 4, P('F2'), 88)
    pc2.chord(t+16, 3, [P('A3'),P('C4'),P('D#4')], 60)
    dr.d(t+16, Drums.CRASH, 70)
    dr.d(t+16, Drums.KICK, 90)
    return pc.save(os.path.join(OUT, '11_前辈蓝调_基于前辈mp3_原创.mid'))

if __name__ == '__main__':
    print(piece_o())
    print(piece_newsong2())
    print(piece_senpai())
