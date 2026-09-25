# きみと春めき（与你的春之初）— 原「终将成春」ずとまよ风格致敬 ×《终将成为你》

F♯ 小调（副歌 A 大调，末段 B 大调）· 142 BPM · 4/4 · 3'03"

## 版本演进（旧版均在 git 历史）
| 版本 | 内容 |
|---|---|
| v1（本文件夹 `*_complete.mid`/`*_melody.flp`） | 纯器乐版：16 分放克 + 关系大调副歌 + 末段升全音 + 急停 |
| v2 | Sinsy DNN 歌声（音色有年代感，已被替换） |
| v3 | NEUTRINO Tau v3 琴葉葵演唱，干净伴奏 |
| **v4（最新，`*_v4.*`）** | **层次升级**：弦乐组/钟琴音乐盒/回调合成器/16 分琶音四层 + NEUTRINO 双唱层 |

## 人声版（v2-v4）演唱: NEUTRINO Tau v3 + 琴葉葵（A.I.VOICE）
- 主旋律重写：音域收进 E4–F#5，副歌 hook = 同音三连 + 级进下落
- `*_vocal_main.musicxml` 主旋律谱（假名歌词随谱）/ `*_vocal_harm.musicxml` 和声谱
- 歌词中日对照见 `lyrics_v2.md`；乐谱册见仓库 `乐谱与歌词/01_*.html`

## 文件
- `02_..._v4.flp` / `_v4.mid` / `_v4_melody.mid` — v4 层次升级版工程与 MIDI
- `02_..._vocal_main.mid/.musicxml`、`_vocal_harm.mid/.musicxml` — 人声分轨
- `gen_song.py`（v1 器乐）、`gen_song_v2_vocal.py`（人声版旋律+歌词+MusicXML）、`gen_song_v4_layers.py`（v4 加层）+ `midilib.py`
- 成品 mp3 未入库（本地 `05_风格致敬三首/02_.../complete_v4.mp3`）
