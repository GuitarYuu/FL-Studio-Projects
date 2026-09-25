# -*- coding: utf-8 -*-
"""06「あおいとびら」v2 —— 慢节奏动漫风迭代（学习 Ayase 夜撫でるメノウ / Lefty 恋音と雨空）
参考曲分析结论（analyze_refs.py 实测）:
  1. 慢歌 = 低BPM(65-100) × 恒定16分细分（onset 全程 7-8/s 不掉）
  2. 动态比仅 1.6-1.8x：逐段叠层的"缓坡填充"，不是大落差；副歌加层不加响
  3. 中频 40%+ 主导、低频<20%、air 8-12%（清透来源）
  4. intro 留白要极端（Lefty 开头低频 3%）；结尾大抽层
v2 变化（v1 保留在 git）:
  - BPM 92→84
  - V1 第一遍抽掉 pizz+鼓（更白）；C1 起全层（钢琴16分+弦乐4声部+内声部+harp16+glock+鼓全开）
  - V2 加回 pizz+轻鼓；Bridge 前半白+卡农、后半 build
  - C3 = +1 半音 + glock 高八度 + 长笛双簧管齐奏（人声三层: 主唱/下三度/低八度）
  - Outro 逐层抽空
  - 新增 harm2 低八度人声轨 (C1/C2/C3 段主旋律 -12, 全'ら')
输出: *_v2_complete.mid / *_v2_vocal_harm.musicxml / *_v2_vocal_harm2.musicxml (main 不变复用 v1 渲染? 否——BPM 变了, main 也要重出 musicxml)
"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from midilib import *

rng = make_rng(20260928)
BPM = 84
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = HERE
os.makedirs(OUTDIR, exist_ok=True)

p = Piece('あおいとびら v2 (慢节奏动漫风)', BPM, key='D')
piano = p.add(Trk('Piano', 0, 0, vol=76, pan=58, reverb=34))
mb = p.add(Trk('Music Box', 8, 1, vol=54, pan=44, reverb=58))
fl = p.add(Trk('Flute', 73, 2, vol=56, pan=30, reverb=48))
ob = p.add(Trk('Oboe', 68, 3, vol=52, pan=84, reverb=48))
harp = p.add(Trk('Harp', 46, 4, vol=48, pan=38, reverb=52))
glock = p.add(Trk('Glockenspiel', 9, 5, vol=46, pan=70, reverb=62))
strings = p.add(Trk('Strings', 48, 6, vol=48, pan=64, reverb=60))
pizz = p.add(Trk('Pizz', 45, 7, vol=48, pan=78, reverb=38))
bass = p.add(Trk('Bass', 33, 8, vol=82, pan=64, reverb=16))
gt = p.add(Trk('Clean Guitar', 27, 10, vol=50, pan=80, reverb=46))  # Lefty 式琶音铺底
dr = p.add(Drums(vol=88))

INTRO = ['Dadd9', 'Dadd9', 'Gmaj7', 'A6']
V8 = ['Dadd9', 'F#m7', 'Gmaj7', 'Aadd9', 'Dadd9', 'F#m7', 'Gmaj7', 'A7sus4']
PRE = ['Gmaj7', 'Aadd9', 'F#m7', 'Bm7']
C = ['D', 'A/C#', 'Bm7', 'Gmaj7', 'D/F#', 'Em7', 'A7sus4', 'A', 'D']
ITL = ['Bm7', 'Gmaj7', 'Dadd9', 'Aadd9']
BRK = ['Bm7', 'Gmaj7', 'Dadd9', 'A/C#', 'Em7', 'Gmaj7', 'A7sus4', 'Bbadd9']  # 末小节=新调V, 导入C3的E♭
TAG = ['D', 'Gmaj7', 'D']
SECS = [
    ('Intro', INTRO, 0), ('V1', V8, 0), ('Pre', PRE, 0), ('C1', C, 0),
    ('ITL', ITL, 0), ('V2', V8, 0), ('Pre', PRE, 0), ('C2', C, 0),
    ('Bridge', BRK, 0),
    ('C3', C + TAG, 1),
    ('Outro', ['Dadd9', 'Gmaj7', 'Dadd9', 'Dadd9'], 0),
]

# ============ 人声主旋律（与 v1 一致, 词不变） ============
MEL_V_A = [
    (0, 0, 1, 'A4', 74, 'し'), (0, 1, 1, 'B4', 76, 'ろ'), (0, 2, 1, 'C#5', 78, 'い'),
    (0, 3, 1.5, 'C#5', 78, 'い'), (1, 0.5, 1, 'B4', 74, 'ぶ'), (1, 1.5, 0.5, 'A4', 72, 'き'),
    (1, 2, 0.5, 'G4', 72, 'の'), (1, 2.5, 0.5, 'F#4', 74, 'な'), (1, 3, 1, 'A4', 76, 'か'),
]
MEL_V_B = [
    (2, 0, 0.5, 'D5', 80, 'そ'), (2, 0.5, 0.5, 'C#5', 78, 'っ'), (2, 1, 1, 'B4', 78, 'と'),
    (2, 2, 0.5, 'B4', 76, 'と'), (2, 2.5, 0.5, 'A4', 76, 'び'), (2, 3, 0.5, 'G4', 74, 'ら'),
    (2, 3.5, 0.5, 'A4', 76, 'を'), (3, 0, 1, 'B4', 78, 'あ'), (3, 1, 1.5, 'A4', 76, 'け'),
]
MEL_V_C = [
    (4, 0, 1, 'A4', 76, 'き'), (4, 1, 1, 'B4', 78, 'み'), (4, 2, 1, 'C#5', 78, 'の'),
    (4, 3, 1, 'D5', 80, 'ゆ'), (5, 0, 0.5, 'C#5', 78, 'び'), (5, 0.5, 0.5, 'B4', 76, 'さ'),
    (5, 1, 1, 'A4', 76, 'き'), (5, 2, 0.5, 'G4', 74, 'ふ'), (5, 2.5, 0.5, 'A4', 76, 'る'),
    (5, 3, 1, 'B4', 78, 'え'),
]
MEL_V_D = [
    (6, 0.5, 0.5, 'C#5', 78, 'て'), (6, 1, 0.5, 'B4', 74, 'そ'), (6, 1.5, 0.5, 'A4', 74, 'れ'),
    (6, 2, 0.5, 'G4', 72, 'で'), (6, 2.5, 0.5, 'A4', 74, 'も'), (6, 3, 0.5, 'B4', 76, 'ひ'),
    (6, 3.5, 0.5, 'C#5', 78, 'か'), (7, 0, 0.5, 'B4', 76, 'り'), (7, 0.5, 0.5, 'A4', 74, 'を'),
    (7, 1, 0.5, 'G4', 74, 'ま'), (7, 1.5, 0.5, 'F#4', 74, 'っ'), (7, 2, 2, 'F#4', 76, 'てた'),
]
MEL_PRE_A = [
    (0, 0, 0.5, 'A4', 78, 'た'), (0, 0.5, 0.5, 'B4', 78, 'め'), (0, 1, 1, 'C#5', 80, 'ら'),
    (0, 2, 1, 'D5', 82, 'う'), (0, 3, 1, 'D5', 80, 'お'), (1, 0, 0.5, 'C#5', 78, 'と'),
    (1, 0.5, 0.5, 'B4', 76, 'が'), (1, 1, 0.5, 'A4', 76, 'き'), (1, 1.5, 0.5, 'B4', 78, 'こ'),
    (1, 2, 1.5, 'C#5', 80, 'え'), (1, 3.5, 0.5, 'D5', 80, 'る'),
]
MEL_PRE_B = [
    (2, 0, 0.5, 'C#5', 80, 'ず'), (2, 0.5, 0.5, 'B4', 78, 'っ'), (2, 1, 1, 'A4', 78, 'と'),
    (2, 2, 0.5, 'G4', 76, 'こ'), (2, 2.5, 0.5, 'A4', 76, 'こ'), (2, 3, 0.5, 'B4', 78, 'に'),
    (2, 3.5, 0.5, 'C#5', 80, 'い'), (3, 0, 1, 'B4', 78, 'た'), (3, 1, 2.5, 'A4', 80, 'の'),
]
MEL_C = [
    (0, 0, 0.75, 'E5', 84, 'あ'), (0, 0.75, 0.75, 'D5', 82, 'お'), (0, 1.5, 1, 'C#5', 84, 'い'),
    (0, 2.5, 0.5, 'B4', 80, 'と'), (0, 3, 0.5, 'D5', 82, 'り'), (0, 3.5, 0.5, 'C#5', 82, 'は'),
    (1, 0, 0.5, 'B4', 82, 'お'), (1, 0.5, 0.5, 'A4', 80, 'り'), (1, 1, 0.5, 'B4', 82, 'か'),
    (1, 1.5, 2, 'C#5', 84, 'ら'),
    (2, 0, 0.75, 'E5', 86, 'と'), (2, 0.75, 0.75, 'D5', 84, 'び'), (2, 1.5, 0.75, 'C#5', 84, 'た'),
    (2, 2.25, 0.75, 'B4', 82, 'つ'), (2, 3, 0.5, 'A4', 80, 'こ'), (2, 3.5, 0.5, 'B4', 82, 'と'),
    (3, 0, 0.5, 'C#5', 84, 'お'), (3, 0.5, 0.5, 'D5', 86, 'し'), (3, 1, 0.5, 'C#5', 84, 'え'),
    (3, 1.5, 0.5, 'B4', 82, 'て'), (3, 2, 2, 'A4', 84, 'ー'),
    (4, 0, 0.5, 'B4', 82, 'こ'), (4, 0.5, 0.5, 'C#5', 82, 'わ'), (4, 1, 0.5, 'D5', 84, 'く'),
    (4, 1.5, 0.5, 'C#5', 82, 'て'), (4, 2, 1, 'B4', 82, 'も'), (4, 3, 0.5, 'A4', 80, 'いっ'),
    (4, 3.5, 0.5, 'B4', 80, 'しょ'), (5, 0, 0.5, 'C#5', 82, 'な'), (5, 0.5, 0.5, 'B4', 80, 'ら'),
    (5, 1, 1, 'A4', 82, 'ー'),
    (6, 0, 0.5, 'F#4', 78, 'そ'), (6, 0.5, 0.5, 'A4', 80, 'ら'), (6, 1, 1, 'B4', 80, 'は'),
    (6, 2, 0.5, 'D5', 84, 'み'), (6, 2.5, 0.5, 'C#5', 82, 'え'), (6, 3, 0.5, 'B4', 82, 'て'),
    (6, 3.5, 0.5, 'A4', 80, 'く'), (7, 0, 0.5, 'G4', 78, 'る'), (7, 0.5, 2, 'A4', 82, 'よ'),
    (7, 2.5, 0.5, 'A4', 82, 'ふ'), (7, 3, 0.5, 'B4', 82, 'た'), (7, 3.5, 0.5, 'C#5', 84, 'り'),
    (8, 0, 1, 'D5', 84, 'の'), (8, 1, 0.5, 'D5', 82, 'あ'), (8, 1.5, 0.5, 'C#5', 82, 'お'),
    (8, 2, 0.5, 'B4', 80, 'と'), (8, 2.5, 0.5, 'A4', 80, 'し'), (8, 3, 1, 'B4', 82, 'ろ'),
]
MEL_BRK = [
    (0, 0, 1, 'B4', 72, 'こ'), (0, 1, 1, 'C#5', 72, 'と'), (0, 2, 1, 'D5', 74, 'ば'),
    (0, 3, 1, 'D5', 74, 'よ'), (1, 0, 1, 'C#5', 74, 'り'), (1, 1, 0.5, 'B4', 72, 'さ'),
    (1, 1.5, 0.5, 'A4', 70, 'き'), (1, 2, 2, 'G4', 72, 'に'),
    (2, 0, 1, 'D5', 74, 'こ'), (2, 1, 1, 'B4', 72, 'た'), (2, 2, 1, 'C#5', 74, 'え'),
    (2, 3, 1, 'A4', 72, 'が'), (3, 0, 1, 'G4', 72, 'あ'), (3, 1, 0.5, 'F#4', 70, 'っ'),
    (3, 1.5, 2.5, 'E4', 72, 'た'),
    (4, 0, 0.5, 'C#5', 76, 'に'), (4, 0.5, 0.5, 'D5', 78, 'ど'), (4, 1, 1, 'E5', 80, 'と'),
    (4, 2, 1, 'E5', 80, 'に'), (4, 3, 0.5, 'D5', 78, 'が'), (4, 3.5, 0.5, 'C#5', 76, 'さ'),
    (5, 0, 1, 'B4', 76, 'な'), (5, 1, 2, 'C#5', 78, 'い'),
]
MEL_TAG = [
    (0, 0, 1, 'F5', 88, 'い'), (0, 1, 1, 'F5', 86, 'っ'), (0, 2, 1, 'D#5', 86, 'しょ'),
    (0, 3, 1, 'D5', 84, 'に'), (1, 0, 0.5, 'D5', 84, 'い'), (1, 0.5, 0.5, 'C5', 82, 'こ'),
    (1, 1, 2, 'D5', 86, 'うよ'),
]

FL_Q = [(0, 0, 0.5, 'A4', 66), (0, 0.5, 0.5, 'B4', 68), (0, 1, 1, 'D5', 72),
        (0, 2, 1.5, 'E5', 76), (0, 3.5, 0.5, 'F#5', 74), (1, 0, 2, 'E5', 72)]
OB_A = [(0, 0, 1, 'B4', 62), (0, 1, 1, 'A4', 60), (0, 2, 2, 'G4', 62)]
FL_RUN = [(0, 0, 0.5, 'D5', 70), (0, 0.5, 0.5, 'E5', 70), (0, 1, 0.5, 'F#5', 72),
          (0, 1.5, 0.5, 'G5', 72), (0, 2, 0.5, 'A5', 74), (0, 2.5, 0.5, 'G5', 70),
          (0, 3, 0.5, 'F#5', 70), (0, 3.5, 0.5, 'E5', 68),
          (1, 0, 1, 'D5', 72), (1, 1, 0.5, 'C#5', 66), (1, 1.5, 0.5, 'B4', 66),
          (1, 2, 2, 'A4', 70)]


def tvoice(c, low, high, n=3):
    """三和弦织体音集: maj7/9 去掉 7th/9th, 消除织体 root 与弦乐长音 7th 相邻半音的冲突."""
    import copy
    c2 = copy.copy(c)
    c2.ints = c.ints[:3]
    return c2.voice(low=low, high=high, n=n)


def sing(trk, sec_start, evts, tr=0):
    out = []
    for e in evts:
        b, bt, d, pp, v = e[0], e[1], e[2], e[3], e[4]
        mora = e[5] if len(e) > 5 else None
        m = npitch(pp) + tr
        trk.n(sec_start + b * 4 + bt, d, m, v)
        out.append((sec_start + b * 4 + bt, d, m, mora))
    return out


def dn3(name):
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    m = npitch(name) - 3
    return names[m % 12] + str(m // 12 - 1)


def sh8(evs, nbars):
    return [(b + nbars, bt, d, pp, v) for (b, bt, d, pp, v) in evs]


# ---------------- 装配 ----------------
t0 = 0.0
for si, (name, chords, tr) in enumerate(SECS):
    cs = [Chord(c).shifted(tr) for c in chords]
    nbars = len(cs)
    start = t0
    for i, c in enumerate(cs):
        b = start + i * 4
        if name == 'Intro':
            tones = tvoice(c, low=62, high=86, n=3)
            if i < 2:
                for k in range(4):
                    mb.n(b + k, 1.6, tones[k % len(tones)], hum(rng, 50))
                piano.n(b, 2.9, tvoice(c, low=50, high=62, n=1)[0], hum(rng, 46))
            else:
                for k in range(8):
                    piano.n(b + k * 0.5, 0.45, tvoice(c, low=57, high=78, n=3)[k % 3], hum(rng, 52))
                strings.chord(b, 3.9, tvoice(c, low=50, high=66, n=3), hum(rng, 22))
                glock.n(b, 1.5, tvoice(c, low=74, high=88, n=1)[0], hum(rng, 42))
            if i == 2:
                sing(fl, b, FL_Q, tr=tr)
            if i == 3:
                sing(ob, b, OB_A, tr=tr)
        elif name in ('V1', 'V2'):
            first = (name == 'V1')
            # v2: 第一遍主歌更白(无pizz无鼓); 第二遍加回一层
            for k in range(8):
                piano.n(b + k * 0.5, 0.45, tvoice(c, low=60, high=79, n=3)[k % 3], hum(rng, 58))
            for k in range(4):
                harp.n(b + k, 0.85, tvoice(c, low=57, high=76, n=3)[k % 3], hum(rng, 32))
            if not first:
                pt = tvoice(c, low=55, high=71, n=2)
                for k in range(4):
                    for pp2 in pt:
                        pizz.n(b + 0.5 + k, 0.2, pp2, hum(rng, 42))
                dr.hits(b, [(0, 36, 50), (2, 36, 44)]
                        + [(k * 0.5, 42, 22 if k % 2 else 30) for k in range(8)])
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 70))
            bass.n(b + 2, 1.9, c.bass_midi(2) + (7 if c.kind not in ('m', 'm7') else 3), hum(rng, 64))
            if i == 1:
                sing(fl, b, [(0, 0, 0.75, 'F#5', 60), (0, 0.75, 0.75, 'E5', 58),
                             (0, 1.5, 1.5, 'D5', 60)], tr=tr)
            if i == 5:
                sing(fl, b, [(0, 0, 0.75, 'E5', 60), (0, 0.75, 0.75, 'D5', 58),
                             (0, 1.5, 1.5, 'B4', 58)], tr=tr)
            if i == nbars - 1:
                sing(ob, b, [(0, 0, 0.75, 'C#5', 56), (0, 0.75, 0.75, 'B4', 54),
                             (0, 1.5, 1.5, 'A4', 56)], tr=tr)
                if not first:
                    dr.hits(b, [(3.5, 42, 46), (3.75, 42, 54), (3.875, 42, 62)])
        elif name == 'Pre':
            # v2: Pre = 缓坡第一级: 弦乐 swell + 钢琴八分 + 竖琴, 轻鼓只在后半
            piano.chord(b, 1.9, tvoice(c, low=58, high=76, n=3), hum(rng, 58))
            piano.chord(b + 2, 1.9, tvoice(c, low=58, high=76, n=3), hum(rng, 54))
            sv = tvoice(c, low=55, high=74, n=3)
            strings.chord(b, 3.9, sv, hum(rng, 34 + i * 4))
            for k in range(4):
                harp.n(b + k, 0.9, sv[k % len(sv)], hum(rng, 38))
                harp.n(b + k + 0.5, 0.4, sv[(k + 1) % len(sv)], hum(rng, 30))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 74))
            bass.n(b + 2, 1.9, c.bass_midi(2), hum(rng, 70))
            dr.hits(b, ([(0, 36, 62), (2, 36, 58)]
                        + [(k * 0.25, 42, min(82, 38 + k * 3)) for k in range(16)]
                        if i >= 2 else
                        [(0, 36, 62), (2, 36, 58)] + [(k * 0.5, 42, 34) for k in range(8)]))
            if i == nbars - 1:
                pass  # 慢歌无通鼓 fill
            if i == 2:
                sing(ob, b, [(0, 0, 0.75, 'C#5', 58), (0, 0.75, 0.75, 'D5', 60),
                             (0, 1.5, 2, 'E5', 62)], tr=tr)
        elif name in ('C1', 'C2', 'C3'):
            # v2 副歌: 恒定16分全层 (参考 Ayase 副歌"加层不加响")
            for k in range(16):                                  # 钢琴 16 分织体
                piano.n(b + k * 0.25, 0.22, tvoice(c, low=60, high=83, n=3)[k % 3]
                        if k % 2 else tvoice(c, low=62, high=79, n=3)[(k // 4) % 3], hum(rng, 62))
            strings.chord(b, 3.85, tvoice(c, low=55, high=77, n=4), hum(rng, 46))
            sv2 = tvoice(c, low=62, high=79, n=2)
            for k in range(8):                                   # 内声部 8 分移动
                strings.n(b + k * 0.5, 0.45, sv2[k % 2], hum(rng, 34))
            for k in range(8):
                harp.n(b + k * 0.5, 0.4, tvoice(c, low=57, high=78, n=3)[k % 3], hum(rng, 42))
            gt16 = tvoice(c, low=59, high=76, n=4)
            gpat = [0, 1, 2, 3, 2, 3, 1, 2, 0, 1, 2, 3, 1, 2, 3, 2]
            k0 = 8 if (name == 'C3' and i == 0) else 0   # 转调首小节前半只留弦乐+人声
            for k in range(k0, 16):
                gt.n(b + k * 0.25, 0.22, gt16[gpat[k] % len(gt16)], hum(rng, 44))
            # 慢歌删钟琴光点 (小打), 白色感交给音乐盒
            bass.n(b, 0.9, c.bass_midi(2), hum(rng, 82))
            bass.n(b + 1.5, 0.4, c.bass_midi(2) + 7, hum(rng, 72))
            bass.n(b + 2, 0.9, c.bass_midi(2), hum(rng, 78))
            bass.n(b + 3.5, 0.4, c.bass_midi(2) + 5, hum(rng, 70))
            # 慢歌鼓型: kick 稀疏 + rim/snare 反拍 + hat 16 分恒定
            # 心跳式极简鼓: kick + rim + hat 8 分, 16 分碎感全删
            dr.hits(b, [(0, 36, 66), (1, 37, 42), (2, 36, 58), (3, 37, 44)]
                    + [(k * 0.5, 42, 24 if k % 2 else 32) for k in range(8)])
            if i == 0:
                crash(dr, b, vel=34)
        elif name == 'ITL':
            if i == 0:
                sing(fl, b, FL_RUN, tr=tr)
            if i == 1:
                sing(fl, b, sh8(FL_RUN[6:], 0), tr=tr)
            if i == 2:
                sing(ob, b, [(0, 0, 1, 'F#4', 62), (0, 1, 0.5, 'G4', 62),
                             (0, 1.5, 0.5, 'A4', 64), (0, 2, 1.5, 'B4', 64),
                             (0, 3.5, 0.5, 'C#5', 62)], tr=tr)
            if i == 3:
                sing(ob, b, [(0, 0, 1.5, 'D5', 64), (0, 1.5, 0.5, 'C#5', 60),
                             (0, 2, 2, 'D5', 64)], tr=tr)
            for k in range(8):
                mb.n(b + k * 0.5, 0.45, tvoice(c, low=50, high=72, n=3)[k % 3], hum(rng, 46))
            piano.n(b, 2.9, tvoice(c, low=50, high=62, n=1)[0], hum(rng, 44))
            strings.chord(b, 3.9, tvoice(c, low=50, high=68, n=3), hum(rng, 24))
            bass.n(b, 1.9, c.bass_midi(2), hum(rng, 64))
        elif name == 'Bridge':
            if i < 4:
                mb.n(b, 1.9, tvoice(c, low=72, high=86, n=1)[0], hum(rng, 44))
                piano.n(b, 2.9, tvoice(c, low=54, high=70, n=2)[0], hum(rng, 48))
                strings.chord(b, 3.9, tvoice(c, low=52, high=68, n=3), hum(rng, 26))
                bass.n(b, 3.8, c.bass_midi(2), hum(rng, 56))
                dr.hits(b, [(0, 36, 40)])
            else:
                for k in range(8):
                    piano.n(b + k * 0.5, 0.45, tvoice(c, low=57, high=76, n=3)[k % 3], hum(rng, 56))
                strings.chord(b, 3.9, tvoice(c, low=55, high=74, n=3), hum(rng, 32 + (i - 4) * 6))
                bass.n(b, 1.9, c.bass_midi(2), hum(rng, 72))
                dr.hits(b, ([(0, 36, 50), (2, 36, 46), (3.5, 37, 44)]
                            + [(k * 0.5, 42, min(60, 26 + (i - 4) * 4))
                               for k in range(8)] if i == 7 else
                            [(0, 36, 48), (2, 36, 44)]
                            + [(k * 0.5, 42, 26) for k in range(8)]))
            if i == 4:
                sing(fl, b, [(0, 0, 0.75, 'B4', 62), (0, 0.75, 0.75, 'C#5', 62),
                             (0, 1.5, 1, 'E5', 66), (0, 2.5, 0.75, 'D5', 64),
                             (0, 3.25, 0.75, 'C#5', 62), (1, 0, 1.5, 'B4', 62)], tr=tr)
                sing(ob, b, [(1, 0, 0.75, 'G4', 56), (1, 0.75, 0.75, 'A4', 56),
                             (1, 1.5, 1, 'C#5', 60), (1, 2.5, 0.75, 'B4', 58),
                             (1, 3.25, 0.75, 'A4', 56), (2, 0, 1.5, 'G4', 56)], tr=tr)
            if i == 7:
                # 转调 lift: 属音上行 B♭-C-D 引入新调主音 E♭
                for k, nn in enumerate(('Bb4', 'C5', 'D5')):
                    glock.n(b + 2.5 + k * 0.5, 0.4, npitch(nn) + tr, hum(rng, 44 + k * 4))
            if i == 6:
                sing(fl, b, [(0, 0, 1, 'D5', 64), (0, 1, 0.5, 'E5', 64),
                             (0, 1.5, 0.5, 'F#5', 66), (0, 2, 2, 'G5', 66)], tr=tr)
                sing(ob, b, [(0, 0, 1, 'B4', 58), (0, 1, 0.5, 'C#5', 58),
                             (0, 1.5, 0.5, 'D5', 60), (0, 2, 2, 'E5', 60)], tr=tr)
        elif name == 'Outro':
            if i < 3:
                mb.n(b, 3.8, tvoice(c, low=74, high=88, n=1)[0], hum(rng, 50 - i * 10))
                piano.chord(b, 3.8, tvoice(c, low=57, high=76, n=3), hum(rng, 54 - i * 9))
                strings.chord(b, 3.9, tvoice(c, low=57, high=73, n=3), hum(rng, 30 - i * 7))
                bass.n(b, 3.8, c.bass_midi(2), hum(rng, 54 - i * 8))
            if i == 3:
                sing(fl, b, [(0, 0, 3.5, 'D5', 52)], tr=tr)
                sing(ob, b, [(0, 0, 3.5, 'A4', 48)], tr=tr)
            if i == 0:
                sing(fl, b, [(0, 0, 0.5, 'A4', 56), (0, 0.5, 0.5, 'B4', 56),
                             (0, 1, 1.5, 'D5', 58), (0, 2.5, 1.5, 'F#5', 54)], tr=tr)
                sing(ob, b, [(0, 0, 0.5, 'E4', 50), (0, 0.5, 0.5, 'F#4', 50),
                             (0, 1, 1.5, 'A4', 52), (0, 2.5, 1.5, 'D5', 50)], tr=tr)
                pass  # outro 无 crash, 留长笛双簧管余韵

    if name == 'C3':
        # Tag 长笛+双簧管八度齐奏 (接受时刻)
        tag_start = start + 9 * 4
        for k in range(2):
            ev = [(bb, bt, d, pp, v) for (bb, bt, d, pp, v, *_m) in MEL_TAG if bb == k]
            if ev:
                sing(fl, tag_start, ev, tr=0)
                if k == 0:   # 双簧管只在 B♭ 和弦小节齐奏 (bar68 的 D9音低八度会撞弦乐 E♭)
                    sing(ob, tag_start, ev, tr=-12)
        sing(fl, tag_start, [(2, 0, 4, 'D#5', 62)], tr=0)
        sing(ob, tag_start, [(2, 0, 4, 'D#4', 56)], tr=0)
    t0 = start + nbars * 4

print(f'total bars: {int(t0 // 4)}  time: {t0 * 60 / BPM:.1f}s  BPM={BPM}')
for trk in p.tracks:
    print(f'  {trk.name:10s} ch{trk.channel} prog{trk.program:3d} notes={len(trk.events)}')

# ---------------- 人声 XML ----------------
xml_main, xml_harm, xml_harm2 = [], [], []
offs = {}
tt = 0.0
for name, chords, tr in SECS:
    offs[name] = tt
    tt += len(chords) * 4
vg = Trk('gather', 0, 15)
# 段起点独立硬编码 (offs 字典会被两个同名 Pre 覆盖!): V1=4 Pre1=12 C1=16 V2=29 Pre2=37 C2=41 Bridge=50 C3=58
for nm, stb, tr in [('V1', 4 * 4, 0), ('Pre', 12 * 4, 0), ('C1', 16 * 4, 0),
                    ('V2', 29 * 4, 0), ('Pre', 37 * 4, 0),
                    ('C2', 41 * 4, 0), ('Bridge', 50 * 4, 0),
                    ('C3', 58 * 4, 1)]:
    if nm in ('V1', 'V2'):
        xml_main += sing(vg, stb, MEL_V_A + MEL_V_B + MEL_V_C + MEL_V_D, tr=tr)
    elif nm == 'Pre':
        xml_main += sing(vg, stb, MEL_PRE_A + MEL_PRE_B, tr=tr)
    elif nm in ('C1', 'C2', 'C3'):
        # 和声 = 逐音下三度后吸附到当前和弦三音 (消除 A#4 类增音/小二度冲突)
        CChords = [Chord(c).shifted(tr) for c in (C + TAG if nm == 'C3' else C)]
        NM = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        def harm_of(mel, bar_offset=0, vtr=None):
            vtr = tr if vtr is None else vtr
            h3 = []
            for (b, bt, d, pp, v, *r) in mel:
                m = npitch(pp) + vtr - 3
                cc = CChords[min((b - bar_offset) // 4, len(CChords) - 1)]
                pcs = {(cc.root + iv) % 12 for iv in cc.ints[:3]}
                for off in (0, -1, 1, -2, 2):
                    if (m + off) % 12 in pcs:
                        m += off
                        break
                h3.append((b, bt, d, NM[m % 12] + str(m // 12 - 1), max(58, v - 16)))
            return h3

        xml_main += sing(vg, stb, MEL_C, tr=tr)
        xml_harm += sing(vg, stb, harm_of(MEL_C), tr=0)
        h8 = [(b, bt, d, pp, max(52, v - 26)) for (b, bt, d, pp, v, *_m) in MEL_C]
        xml_harm2 += sing(vg, stb, h8, tr=tr)
        if nm == 'C3':
            xml_main += sing(vg, stb + len(C) * 4, MEL_TAG, tr=0)  # MEL_TAG 已含 +1, 不再移调
            tg = [(b + len(C) * 4, bt, d, pp, v, *r)
                  for (b, bt, d, pp, v, *r) in MEL_TAG]
            xml_harm += sing(vg, stb, harm_of(tg, bar_offset=len(C) * 4, vtr=0), tr=0)
    elif nm == 'Bridge':
        xml_main += sing(vg, stb, MEL_BRK, tr=tr)

lo = min(m for _, _, m, _ in xml_main); hi = max(m for _, _, m, _ in xml_main)
names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
print(f'main {len(xml_main)} notes {names[lo%12]}{lo//12-1}~{names[hi%12]}{hi//12-1}; '
      f'harm {len(xml_harm)}; harm2(低八度) {len(xml_harm2)}')
assert all(mora for _, _, _, mora in xml_main), '空歌词!'

base = os.path.join(OUTDIR, '06_青色的门_利兹与青鸟')
p.save(base + '_v2_complete.mid')
print('saved:', base + '_v2_complete.mid')


def pitch_step(midi):
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


def write_musicxml(path, notes, bpm, total_bars, key_fifths=2):
    DIV = 4
    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" '
         '"http://www.musicxml.org/dtds/partwise.dtd">',
         '<score-partwise version="3.1">',
         '<part-list><score-part id="P1"><part-name>Vocal</part-name></score-part></part-list>',
         '<part id="P1">']
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
        for bt, d, m, mora in sorted(by_bar.get(bar, []), key=lambda x: x[0]):
            if bt > pos + 1e-6:
                L.append(rest_xml(bt - pos, DIV))
                pos = bt
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


TOTAL = int(t0 // 4)
write_musicxml(base + '_v2_vocal_main.musicxml', xml_main, BPM, TOTAL)
write_musicxml(base + '_v2_vocal_harm.musicxml',
               [(bt, d, m, 'ら') for bt, d, m, _ in xml_harm], BPM, TOTAL)
write_musicxml(base + '_v2_vocal_harm2.musicxml',
               [(bt, d, m, 'ら') for bt, d, m, _ in xml_harm2], BPM, TOTAL)
