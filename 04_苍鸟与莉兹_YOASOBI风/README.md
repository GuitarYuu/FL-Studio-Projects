# 01「苍鸟与莉兹」 — YOASOBI 风格致敬 ×《莉兹与青鸟》

- **速度/调/拍**: 134 BPM · B♭ 大调 · 4/4 · 约 3'00"
- **概念**: 长笛 = 青鸟（双笠），双簧管 = 莉兹（铠冢）。全曲用两支管乐的对话织体写
  "想放手却又想留住"的关系；副歌即"飞翔"，桥段半拍落 = 告别的静止，末段升半音 = 真正的起飞。
- 生成脚本: `_compose\song1_ao_to_rizu.py`（改参数可重新生成）

## 曲式（小节起点）

| 段落 | 小节 | 内容 |
|---|---|---|
| Intro | 0 | 钢琴 16 分 riff（E♭maj9↔F9），长笛鸣叫点缀 |
| A1 / A2 | 8 / 16 | 主歌，钢琴 8 分分解；A2 加入副钢琴与更满的鼓 |
| Pre | 24 | ii–V 上行推进，16 分镲渐强 + 军鼓滚奏 |
| C1 | 28 | 副歌「F5–D5–C5」钩子，全乐队 |
| ITL | 36 | 间奏：长笛/双簧管二重对话 |
| A3 / A4 | 40 / 48 | 主歌再现（加电钢琴） |
| C2 | 60 | 副歌 + 合成器加倍 + 长笛答句 |
| Bridge | 68 | 半拍落，借 E♭m7 变暗，弦乐渐强 |
| C3 + tag | 80 | **整体升半音到 B 大调**，末 4 小节 tag 收束 |
| Outro | 92 | riff 渐弱，B(add9) 长音 + 长笛告别句 |

## 核心和声

- 主歌: `E♭maj7 – F – Gm7 – Cm7 – E♭maj7 – F – Gm7 – F7`（IV–V–iii–vi 循环 + 属七推动）
- 副歌: `B♭ – F/A – Gm7 – E♭maj7 – B♭/D – E♭/F – F – F7`（下行贝斯 B♭→A→G→F）
- 桥段: `E♭maj7 – E♭m7 – B♭/D – Cm7 – A♭maj7 – B♭ ...`（同名小调借用变暗）

## 风格要点（对照 YOASOBI 的写法）

1. 常动 16 分钢琴 riff 贯穿 intro/间奏/outro，副歌改为驱动型分解 + 左手根五；
2. 主歌音节密、副歌大跳长音（F5 起、D5 落）；
3. 末段半音升调（B♭→B）是 YOASOBI 式"最后的推背感"；
4. 打击乐: 底鼓 0–1.75–2.5，军鼓 2/4 拍，预副歌 16 分镲渐强。

## FL Studio 里替换音色（GM → 建议）

| 轨道 | GM | 换成 |
|---|---|---|
| Piano Main/Off | 0 | FL Keys – Grand Piano（副歌叠两层，一层 pan 左一层右） |
| E.Piano | 4 | FL Keys Rhodes / FLEX Electronic Piano |
| Lead Vocal | 81 | FLEX Lead / Sytrus 锯齿+慢Attack（当人声位） |
| Lead Synth | 80 | Sytrus / 3xOsc 超锯齿（音量 -6dB 垫在主音下） |
| Flute / Oboe | 73 / 68 | FLEX Orchestral（长笛高八度点缀即可） |
| Finger Bass | 33 | BooBass / FLEX Finger Bass |
| Strings | 48 | FLEX Strings Ensemble（挂总线混响 send） |
| （鼓已剥离） | — | 由 drum_synth.wav 提供；也可换 FPC 原声套鼓 |

混音起手：总线 Fruity Limiter；主歌干一点，副歌给并行压缩；长笛/双簧管对置左右。
