# -*- coding: utf-8 -*-
"""风格致敬三首 - MIDI 作曲框架 (mido, GM, format 1, 480tpb)
鼓轨仅使用 _tools/drum_synth.py 已实现的音色:
  36底鼓 38军鼓 39拍手 42闭镲 44踩镲 46开镲 49/55/57吊镲 41/43/45/47/48/50通鼓
"""
import os, re, random
from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo

NOTE_BASE = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
FLAT_NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
SHARP_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def npitch(name):
    """'Bb4' / 'F#5' / 'C4' -> MIDI 号"""
    m = re.match(r'^([A-G])([#b]?)(-?\d)$', name)
    if not m:
        raise ValueError(name)
    pc = NOTE_BASE[m.group(1)] + (1 if m.group(2) == '#' else -1 if m.group(2) == 'b' else 0)
    return (int(m.group(3)) + 1) * 12 + pc


CHORD_INTS = {
    '': (0, 4, 7), '6': (0, 4, 7, 9), '69': (0, 4, 7, 9, 14),
    'maj7': (0, 4, 7, 11), 'maj9': (0, 4, 7, 11, 14), 'maj7#11': (0, 4, 7, 11, 18),
    'add9': (0, 4, 7, 14),
    '7': (0, 4, 7, 10), '9': (0, 4, 7, 10, 14), '13': (0, 4, 7, 10, 14, 21),
    '7#9': (0, 4, 10, 15), '7b9': (0, 4, 10, 13), '7sus4': (0, 5, 7, 10),
    'sus4': (0, 5, 7), 'sus2': (0, 2, 7),
    'm': (0, 3, 7), 'm7': (0, 3, 7, 10), 'm9': (0, 3, 7, 10, 14),
    'm6': (0, 3, 7, 9), 'm11': (0, 3, 7, 10, 17), 'm7b5': (0, 3, 6, 10),
    'dim': (0, 3, 6), 'aug': (0, 4, 8), '5': (0, 7),
}


class Chord:
    __slots__ = ('root', 'kind', 'ints', 'bass')

    def __init__(self, spec):
        m = re.match(r'^([A-G])([#b]?)([^/]*)(?:/([A-G][#b]?))?$', spec)
        if not m:
            raise ValueError(spec)
        self.root = (NOTE_BASE[m.group(1)] + (1 if m.group(2) == '#' else -1 if m.group(2) == 'b' else 0)) % 12
        kind = m.group(3)
        if kind not in CHORD_INTS:
            raise ValueError(f'unknown chord kind: {spec}')
        self.kind = kind
        self.ints = CHORD_INTS[kind]
        if m.group(4):
            acc = '#' if '#' in m.group(4) else ('b' if 'b' in m.group(4) else '')
            self.bass = (NOTE_BASE[m.group(4)[0]] + (1 if acc == '#' else -1 if acc == 'b' else 0)) % 12
        else:
            self.bass = self.root

    def shifted(self, st, use_flat=False):
        if st == 0:
            return self
        c = Chord.__new__(Chord)
        c.root = (self.root + st) % 12
        c.kind = self.kind
        c.ints = self.ints
        c.bass = (self.bass + st) % 12
        return c

    def name(self, use_flat=True):
        n = (FLAT_NAMES if use_flat else SHARP_NAMES)[self.root] + self.kind
        if self.bass != self.root:
            n += '/' + (FLAT_NAMES if use_flat else SHARP_NAMES)[self.bass]
        return n

    def voice(self, low=58, high=80, n=4):
        """中音区排列 (省五音), 返回升序 MIDI 列表"""
        ints = self.ints if len(self.ints) <= n else (self.ints[0], self.ints[1]) + self.ints[3:n + 1]
        out, cur = [], low - 1
        for iv in ints:
            p = low + ((self.root + iv - low) % 12)
            while p <= cur:
                p += 12
            out.append(p)
            cur = p
        if out[-1] > high and out[0] - 12 >= low - 6:
            out = [p - 12 for p in out]
        return out

    def bass_midi(self, octave=2):
        return (octave + 1) * 12 + self.bass


class Trk:
    def __init__(self, name, program=0, channel=0, vol=100, pan=64, reverb=0, chorus=0):
        self.name, self.program, self.channel = name, program, channel
        self.vol, self.pan, self.reverb, self.chorus = vol, pan, reverb, chorus
        self.events = []   # (start_beat, dur_beat, pitch, vel)
        self.bends = []    # (start_beat, cents)

    def n(self, start, dur, pitch, vel=92):
        self.events.append((round(start, 4), round(dur, 4), int(pitch), max(1, min(127, int(vel)))))

    def chord(self, start, dur, pitches, vel=78, spread=0.0):
        for i, p in enumerate(pitches):
            self.n(start + (i * spread if spread > 0 else 0), dur, p, vel)

    def mel(self, start, items, vel=92):
        """items: (pitch|None, dur[, vel]) 顺序推进"""
        t = start
        for it in items:
            p, d = it[0], it[1]
            v = it[2] if len(it) > 2 else vel
            if p is not None:
                self.n(t, d, p, v)
            t += d
        return t

    def bend(self, start, cents):
        self.bends.append((round(start, 4), int(cents)))

    def phrase(self, sec_start, evts, tr=0, bpb=4):
        """evts: (bar, beat, dur, pitch_name_or_int, vel)"""
        for b, bt, d, p, v in evts:
            pitch = npitch(p) if isinstance(p, str) else p
            self.n(sec_start + b * bpb + bt, d, pitch + tr, v)


class Drums(Trk):
    K, S, CLAP, CH, PH, OH = 36, 38, 39, 42, 44, 46
    CR, CR2, T_LO, T_FL, T_M = 49, 57, 41, 43, 45

    def __init__(self, name='Drums', vol=100):
        super().__init__(name, 0, 9, vol)

    def d(self, start, pitch, vel=90):
        self.n(start, 0.25, pitch, vel)

    def hits(self, bar_start, spec):
        """spec: [(beat, note, vel), ...]"""
        for bt, note, vel in spec:
            self.d(bar_start + bt, note, vel)


class Piece:
    def __init__(self, title, bpm, num=4, den=4, key='C'):
        self.title, self.bpm, self.num, self.den, self.key = title, bpm, num, den, key
        self.tracks = []
        self.sections = []   # (name, start_beat, bars)

    def add(self, trk):
        self.tracks.append(trk)
        return trk

    def save(self, path):
        mf = MidiFile(type=1, ticks_per_beat=480, charset='utf-8')
        meta = MidiTrack()
        mf.tracks.append(meta)
        meta.append(MetaMessage('track_name', name=self.title, time=0))
        meta.append(MetaMessage('set_tempo', tempo=bpm2tempo(self.bpm), time=0))
        meta.append(MetaMessage('time_signature', numerator=self.num, denominator=self.den, time=0))
        meta.append(MetaMessage('key_signature', key=self.key, time=0))
        meta.append(MetaMessage('end_of_track', time=1))
        for trk in self.tracks:
            t = MidiTrack()
            mf.tracks.append(t)
            t.append(MetaMessage('track_name', name=trk.name, time=0))
            t.append(Message('program_change', channel=trk.channel, program=trk.program, time=0))
            t.append(Message('control_change', channel=trk.channel, control=7, value=trk.vol, time=0))
            t.append(Message('control_change', channel=trk.channel, control=10, value=trk.pan, time=0))
            t.append(Message('control_change', channel=trk.channel, control=91, value=trk.reverb, time=0))
            t.append(Message('control_change', channel=trk.channel, control=93, value=trk.chorus, time=0))
            # 统一事件流: note_off 优先级 0, note_on/bend 优先级 1, 全部按绝对拍排序后 delta 编码
            stream = []
            for s, d, p, v in trk.events:
                stream.append((round(s + d, 4), 0, ('off', p, 0)))
                stream.append((round(s, 4), 1, ('on', p, v)))
            for st, cents in trk.bends:
                stream.append((round(st, 4), 1, ('bend', 0, int(cents))))
            stream.sort(key=lambda e: (e[0], e[1]))
            last = 0.0
            for tt, _prio, (kind, p, val) in stream:
                delta = int(round((tt - last) * 480))
                if kind == 'on':
                    t.append(Message('note_on', channel=trk.channel, note=p, velocity=val, time=delta))
                elif kind == 'off':
                    t.append(Message('note_off', channel=trk.channel, note=p, velocity=0, time=delta))
                else:
                    bend = max(-8192, min(8191, int(val / 200 * 8192)))
                    t.append(Message('pitchwheel', channel=trk.channel, pitch=bend, time=delta))
                last = tt
            t.append(MetaMessage('end_of_track', time=240))
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        mf.save(path)
        return path


def make_rng(seed):
    return random.Random(seed)


def hum(rng, vel, amount=4):
    return max(8, min(127, vel + rng.randint(-amount, amount)))


def sh(evs, nbars):
    """乐句整体后移 nbars 小节 (拼接乐句用)"""
    return [(b + nbars, bt, d, p, v) for (b, bt, d, p, v) in evs]


# ---------- 作曲构件 ----------
def piano_riff16(trk, bar_start, chord, rng, vel=84, TONES5=True):
    """YOASOBI 式 16 分音符上下行 riff (5音列)"""
    tones = chord.voice(low=58, high=84, n=5 if TONES5 else 4)
    pat = [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1] if TONES5 else \
          [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 3, 1, 2, 3, 2]
    pat = [i % len(tones) for i in pat]
    for i, idx in enumerate(pat):
        v = vel if i % 8 == 0 else vel - 12
        trk.n(bar_start + i * 0.25, 0.24, tones[idx], hum(rng, v))


def piano_arp8(trk, bar_start, chord, rng, vel=64):
    """8 分分解和弦 (主歌)"""
    tones = chord.voice(low=60, high=81, n=4)
    pat = [i % len(tones) for i in (0, 2, 1, 3, 2, 1, 3, 2)]
    for i, idx in enumerate(pat):
        trk.n(bar_start + i * 0.5, 0.45, tones[idx], hum(rng, vel - (6 if i % 2 else 0)))


def piano_drive16(trk, bar_start, chord, rng, vel=88):
    """副歌驱动 16 分 + 左手根音五度"""
    tones = chord.voice(low=60, high=84, n=4)
    pat = [i % len(tones) for i in (0, 1, 2, 3, 2, 3, 1, 2)]
    for i, idx in enumerate(pat):
        trk.n(bar_start + i * 0.25, 0.22, tones[idx], hum(rng, vel - (10 if i % 4 else 0)))
    root = chord.bass_midi(3)
    trk.n(bar_start, 0.9, root, hum(rng, vel - 10))
    trk.n(bar_start + 1, 0.9, root + 7, hum(rng, vel - 22))
    trk.n(bar_start + 2, 0.9, root, hum(rng, vel - 12))
    trk.n(bar_start + 3, 0.9, root + 7, hum(rng, vel - 24))


def piano_blocks(trk, bar_start, chord, rng, hits=((0, 2.0, 72), (2, 1.0, 66), (3, 1.0, 68)), n=4, low=56, high=78):
    tones = chord.voice(low=low, high=high, n=n)
    for bt, d, v in hits:
        trk.chord(bar_start + bt, d * 0.95, tones, hum(rng, v))


def ep_stabs(trk, bar_start, chord, rng, beats=((0.5, 0.5, 62), (1.5, 0.5, 58), (2.5, 0.5, 62), (3.5, 0.5, 58)), n=4):
    tones = chord.voice(low=58, high=79, n=n)
    for bt, d, v in beats:
        trk.chord(bar_start + bt, d * 0.9, tones, hum(rng, v))


def gt_skank16(trk, bar_start, chord, rng, vel_hi=66):
    """闷音 16 分放克扫弦, 反拍重音"""
    tones = chord.voice(low=55, high=72, n=2)
    for i in range(16):
        v = vel_hi if i % 2 else vel_hi - 24
        for p in tones:
            trk.n(bar_start + i * 0.25, 0.1, p, hum(rng, v))


def gt_doublestop8(trk, bar_start, chord, rng, vel=70):
    tones = chord.voice(low=61, high=76, n=2)
    for i in range(4):
        for p in tones:
            trk.n(bar_start + 0.5 + i, 0.2, p, hum(rng, vel))


def ac_pick8(trk, bar_start, chord, rng, vel=70):
    """民谣指弹 8 分 (低根音起)"""
    tones = chord.voice(low=52, high=69, n=4)
    pat = [i % len(tones) for i in (0, 1, 2, 3, 0, 1, 2, 1)]
    base = [vel, vel - 14, vel - 8, vel - 10, vel - 4, vel - 14, vel - 8, vel - 14]
    for i, idx in enumerate(pat):
        trk.n(bar_start + i * 0.5, 0.48, tones[idx], hum(rng, base[i]))


def bass_8(trk, bar_start, chord, next_chord, rng, vel=78, walking=True):
    r = chord.bass_midi(2)
    trk.n(bar_start, 0.9, r, hum(rng, vel))
    if walking:
        trk.n(bar_start + 1.5, 0.4, r + 7, hum(rng, vel - 14))
    trk.n(bar_start + 2, 0.9, r, hum(rng, vel - 4))
    if walking:
        nr = next_chord.bass_midi(2)
        appr = nr - 1 if nr > r else nr + 2
        trk.n(bar_start + 3.5, 0.4, appr, hum(rng, vel - 8))


def bass_funk16(trk, bar_start, chord, next_chord, rng, vel=90):
    r = chord.bass_midi(2)
    nr = next_chord.bass_midi(2)
    appr = nr - 1 if nr > r else nr + 2
    spec = [(0, r, 96, 0.45), (0.5, r, 42, 0.1), (0.75, r + 7, 80, 0.35),
            (1.5, r + 12, 84, 0.3), (1.75, r + 10, 74, 0.3), (2, r, 94, 0.2),
            (2.25, r, 40, 0.1), (2.5, r + 7, 82, 0.35), (3, r + 12, 80, 0.3),
            (3.25, r + 10, 70, 0.25), (3.5, appr, 86, 0.4)]
    for bt, p, v, d in spec:
        trk.n(bar_start + bt, d, p, hum(rng, v))


def bass_folk(trk, bar_start, chord, rng, vel=72):
    r = chord.bass_midi(2)
    trk.n(bar_start, 1.8, r, hum(rng, vel))
    trk.n(bar_start + 2, 1.8, r + 7 if chord.kind not in ('m', 'm7', 'm9') else r + 3, hum(rng, vel - 10))


def pad_strings(trk, bar_start, chord, rng, vel=42, n=4, low=50, high=72):
    tones = chord.voice(low=low, high=high, n=n)
    trk.chord(bar_start, 3.9, tones, hum(rng, vel, 2))


def drum_bar(dr, bar_start, style, rng, fill=False, vel_scale=1.0, bpb=4):
    """风格鼓型; vel_scale 用于渐弱/渐强"""
    def v(x):
        return int(x * vel_scale)

    if style == 'yo_intro':
        dr.hits(bar_start, [(0, 36, v(88)), (2, 36, v(80))] +
                [(i * 0.5, 42, v(58 if i % 2 else 72)) for i in range(8)])
    elif style == 'yo_verse':
        dr.hits(bar_start, [(0, 36, 96), (1.5, 36, 78), (2.5, 36, 88),
                            (1, 38, 96), (3, 38, 98)])
        dr.hits(bar_start, [(i * 0.5, 42, 70 if i % 2 == 0 else 52) for i in range(8)])
        if not fill:
            dr.hits(bar_start, [(3.5, 46, 66)])
    elif style == 'yo_pre':
        dr.hits(bar_start, [(i * 0.25, 42, min(118, 48 + i * 4)) for i in range(16)])
        dr.hits(bar_start, [(0, 36, 90), (2, 36, 88)])
    elif style == 'yo_pre_snare':
        dr.hits(bar_start, [(i * 0.25, 38, min(126, 62 + i * 5)) for i in range(16)])
    elif style == 'yo_chorus':
        dr.hits(bar_start, [(0, 36, 104), (1.75, 36, 86), (2.5, 36, 96),
                            (1, 38, 106), (3, 38, 108)])
        dr.hits(bar_start, [(i * 0.5, 42, 84 if i % 2 == 0 else 62) for i in range(8)])
        if fill:
            dr.hits(bar_start, [(3, 38, 100), (3.25, 38, 106), (3.5, 38, 112),
                                (3.75, 43, 116)])
    elif style == 'yo_bridge':
        dr.hits(bar_start, [(0, 36, 92), (2, 38, 96), (1, 42, 56), (3, 42, 56)])
    elif style == 'z_verse':
        dr.hits(bar_start, [(0, 36, 98), (1.75, 36, 82), (2.5, 36, 90),
                            (1, 38, 100), (3, 38, 102),
                            (0.75, 38, 30), (2.25, 38, 34), (3.625, 38, 28)])
        dr.hits(bar_start, [(i * 0.25, 42, (88 if i % 4 == 0 else 60) if i % 2 == 0 else 44)
                            for i in range(16)])
    elif style == 'z_chorus':
        dr.hits(bar_start, [(0, 36, 106), (1.5, 36, 88), (2.75, 36, 94),
                            (1, 38, 108), (3, 38, 110)])
        dr.hits(bar_start, [(i * 0.5, 46, 76) for i in range(4)])
        dr.hits(bar_start, [(0, 42, 92), (1, 42, 92), (2, 42, 92), (3, 42, 92)])
        if fill:
            dr.hits(bar_start, [(3, 38, 104), (3.25, 38, 108), (3.5, 45, 114), (3.75, 43, 118)])
    elif style == 'z_pre':
        dr.hits(bar_start, [(i * 0.25, 42, min(112, 52 + i * 3)) for i in range(16)])
        dr.hits(bar_start, [(0, 36, 92), (2.5, 36, 90)])
    elif style == 'z_break':
        dr.hits(bar_start, [(0, 36, 84), (2.5, 36, 72), (1, 42, 40), (3, 42, 40)])
    elif style == 'z_build':
        dr.hits(bar_start, [(i * 0.25, 38, min(124, 54 + i * 5)) for i in range(16)])
        dr.hits(bar_start, [(3, 45, 118), (3.5, 43, 122)])
    elif style == 'y_verse':
        dr.hits(bar_start, [(0, 36, 74)] + ([(2.5, 36, 62)] if not fill else []) +
                [(1, 42, 46), (3, 42, 46),
                 (0.5, 42, 26), (1.5, 42, 26), (2.5, 42, 26), (3.5, 42, 26)])
    elif style == 'y_pre':
        dr.hits(bar_start, [(0, 36, 82), (2.5, 36, 70), (1, 42, 56), (3, 42, 56)] +
                [(i * 0.5, 42, 40) for i in range(8)])
    elif style == 'y_chorus':
        dr.hits(bar_start, [(0, 36, 100), (2.5, 36, 88), (1, 38, 102), (3, 38, 104),
                            (3.5, 46, 66)] +
                [(i * 0.5, 42, 70 if i % 2 == 0 else 50) for i in range(8)])
        if fill:
            dr.hits(bar_start, [(3.25, 38, 104), (3.5, 45, 112), (3.75, 43, 116)])
    elif style == 'y_bridge':
        dr.hits(bar_start, [(0, 36, 66), (1, 42, 40), (3, 42, 40),
                            (0.5, 42, 22), (1.5, 42, 22), (2.5, 42, 22), (3.5, 42, 22)])


def crash(dr, beat, vel=92, note=49):
    dr.d(beat, note, vel)
