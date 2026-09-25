# -*- coding: utf-8 -*-
"""Tiny MIDI composition framework."""
from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo
import os

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def P(name):
    """'C4' -> 60 ; supports 'Bb3' 'F#5'"""
    n = name[:-1]; o = int(name[-1])
    n = n.replace('b','b')
    if n.endswith('b'):
        idx = NOTE_NAMES.index(n[0]+'b') if (n[0]+'b') in NOTE_NAMES else NOTE_NAMES.index(n[0])+11
    else:
        idx = NOTE_NAMES.index(n)
    return (o+1)*12 + idx

class Trk:
    def __init__(self, name, program, channel, vol=100, pan=64, reverb=40):
        self.name = name; self.program = program; self.channel = channel
        self.vol = vol; self.pan = pan; self.reverb = reverb
        self.events = []          # (start_beat, dur_beat, pitch, vel)
    def n(self, start, dur, pitch, vel=92):
        self.events.append((round(start,4), round(dur,4), int(pitch), int(vel)))
    def mel(self, start, items, vel=92):
        """items: (pitch|None, dur[, vel]) sequential; None = rest"""
        t = start
        for it in items:
            p, d = it[0], it[1]
            v = it[2] if len(it) > 2 else vel
            if p is not None:
                self.n(t, d, p, v)
            t += d
        return t
    def chord(self, start, dur, pitches, vel=78):
        for p in pitches:
            self.n(start, dur, p, vel)

class Drums(Trk):
    KICK=36; SNARE=38; RIM=37; HH=42; HHO=46; RIDE=51; CRASH=49; TOM=45; HTOM=47; LTOM=43
    def __init__(self, name='Drums', vol=90):
        super().__init__(name, 0, 9, vol)
    def d(self, start, pitch, vel=90, dur=0.25):
        self.n(start, dur, pitch, vel)
    def beat(self, bar, style='rock', reps=1, fill=False, bpb=4):
        """`bar` = bar index; each bar is bpb beats"""
        for i in range(reps):
            t = bar*bpb + i*bpb
            if style == 'rock':
                self.d(t, self.KICK, 100); self.d(t+0.5, self.HH, 60)
                self.d(t+1, self.HH, 70); self.d(t+1.5, self.HH, 60)
                self.d(t+2, self.SNARE, 95); self.d(t+2.5, self.HH, 60)
                self.d(t+3, self.HH, 70); self.d(t+3.5, self.HH, 60)
                self.d(t, self.HH, 70)
                self.d(t+2.75, self.KICK, 85)
            elif style == 'soft':
                self.d(t, self.KICK, 80); self.d(t+1, self.HH, 45)
                self.d(t+2, self.RIM, 70); self.d(t+3, self.HH, 45)
            elif style == 'waltz':
                self.d(t, self.KICK, 95); self.d(t+1, self.RIM, 60); self.d(t+2, self.RIM, 60)
            if fill and i == reps-1:
                self.d(t+3, self.HTOM, 90); self.d(t+3.5, self.TOM, 95)
    def swing(self, bar, reps=1, fill=False, bpb=4):
        for i in range(reps):
            t = bar*bpb + i*bpb
            self.d(t, self.RIDE, 78); self.d(t+1+2/3, self.RIDE, 60)
            self.d(t+1, self.RIDE, 68); self.d(t+2+2/3, self.RIDE, 60)
            self.d(t+2, self.RIDE, 78); self.d(t+3+2/3, self.RIDE, 60)
            self.d(t+3, self.RIDE, 68)
            self.d(t, self.HH, 55)
            self.d(t, self.KICK, 85); self.d(t+2.5, self.KICK, 80)
            self.d(t+2, self.SNARE, 80, 0.2)
            if fill and i == reps-1:
                self.d(t+3, self.SNARE, 85, 0.2); self.d(t+3+2/3, self.SNARE, 92, 0.2)

class Piece:
    def __init__(self, title, bpm, num=4, den=4, key='C'):
        self.title = title; self.bpm = bpm
        self.num = num; self.den = den; self.key = key
        self.tracks = []
    def add(self, trk):
        self.tracks.append(trk); return trk
    def save(self, path):
        mf = MidiFile(type=1, ticks_per_beat=480)
        # meta track
        meta = MidiTrack(); mf.tracks.append(meta)
        meta.append(MetaMessage('track_name', name=self.title, time=0))
        meta.append(MetaMessage('set_tempo', tempo=bpm2tempo(self.bpm), time=0))
        meta.append(MetaMessage('time_signature', numerator=self.num, denominator=self.den, time=0))
        meta.append(MetaMessage('key_signature', key=self.key, time=0))
        meta.append(MetaMessage('end_of_track', time=1))
        for trk in self.tracks:
            t = MidiTrack(); mf.tracks.append(t)
            t.append(MetaMessage('track_name', name=trk.name, time=0))
            t.append(Message('program_change', channel=trk.channel, program=trk.program, time=0))
            t.append(Message('control_change', channel=trk.channel, control=7, value=trk.vol, time=0))
            t.append(Message('control_change', channel=trk.channel, control=10, value=trk.pan, time=0))
            t.append(Message('control_change', channel=trk.channel, control=91, value=trk.reverb, time=0))
            evs = sorted(trk.events, key=lambda e: (e[0], 1 if e[1] > 0 and False else 0))
            # note_off before note_on at same tick: sort by (time, is_on)
            evs2 = []
            for s, d, p, v in trk.events:
                evs2.append((s, 1, s, d, p, v))
                evs2.append((s+d, 0, s, d, p, v))
            evs2.sort(key=lambda e: (round(e[0],4), e[1]))
            last = 0.0
            for tt, flag, _s, _d, p, v in evs2:
                delta = int(round((tt - last) * 480))
                mtype = 'note_on' if flag == 1 else 'note_off'
                t.append(Message(mtype, channel=trk.channel, note=p, velocity=(v if mtype=='note_on' else 0), time=delta))
                last = tt
            t.append(MetaMessage('end_of_track', time=240))
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        mf.save(path)
        return path

# ---- chord vocabulary helper: name -> pitches (root position + common voicings) ----
def tri(root_pc, quality, octave=3):
    r = octave*12 + root_pc
    if quality == 'maj': iv = [0,4,7]
    elif quality == 'min': iv = [0,3,7]
    elif quality == 'dim': iv = [0,3,6]
    elif quality == 'aug': iv = [0,4,8]
    elif quality == '7': iv = [0,4,7,10]
    elif quality == 'm7': iv = [0,3,7,10]
    elif quality == 'maj7': iv = [0,4,7,11]
    elif quality == '6': iv = [0,4,7,9]
    elif quality == 'm6': iv = [0,3,7,9]
    elif quality == 'sus4': iv = [0,5,7]
    elif quality == '9': iv = [0,4,7,10,14]
    return [r+i for i in iv]
