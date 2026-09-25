# -*- coding: utf-8 -*-
"""校验生成的原创 MIDI"""
import mido, os

DL = r"C:\Users\25448\Downloads\原创乐曲"
def nn(n): return ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][n%12] + str(n//12-1)

for fn in sorted(os.listdir(DL)):
    if not fn.lower().endswith('.mid'): continue
    path = os.path.join(DL, fn)
    try:
        mf = mido.MidiFile(path)
    except Exception as e:
        print(f"[FAIL] {fn}: {e}"); continue
    tpb = mf.ticks_per_beat
    issues = []
    total_notes = 0
    prog_info = []
    meta_ok = {'tempo': False, 'ts': False, 'ks': False}
    for ti, tr in enumerate(mf.tracks):
        t = 0; active = {}; count = 0
        for m in tr:
            t += m.time
            if m.type == 'set_tempo': meta_ok['tempo'] = True
            if m.type == 'time_signature': meta_ok['ts'] = True
            if m.type == 'key_signature': meta_ok['ks'] = True
            if m.type == 'program_change': prog_info.append((ti, m.channel, m.program))
            if m.type == 'note_on' and m.velocity > 0:
                if m.note in active: issues.append(f"tr{ti} overlapping same pitch {m.note} at {t}")
                active[m.note] = t; count += 1
            elif m.type == 'note_off' or (m.type == 'note_on' and m.velocity == 0):
                if m.note not in active:
                    issues.append(f"tr{ti} orphan note_off {m.note} at {t}")
                else:
                    del active[m.note]
        total_notes += count
        if active: issues.append(f"tr{ti} {len(active)} hanging notes")
    dur = mf.length
    flag = 'OK  ' if not issues else 'WARN'
    print(f"[{flag}] {fn}: {dur:.1f}s, {total_notes} notes, meta(ts/tempo/ks)={meta_ok['ts']}/{meta_ok['tempo']}/{meta_ok['ks']}")
    if issues:
        for i in issues[:6]: print("     -", i)
