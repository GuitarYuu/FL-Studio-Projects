# 06「あおいとびら」(青色的门) — 《利兹与青鸟》青白蓝渐变 小清新原创曲

- **速度/调/拍**: 92 BPM · D 大调（末段升半音到 E♭）· 4/4 · 3'13"
- **概念**: 青白蓝渐变；羞涩试探与接受。长笛（希美）与双簧管（霙）的器乐对话承担戏剧——
  门推开一条缝是试探，走进天空是接受。
- 生成脚本: `_compose\song6_aoi_tobira.py` → `pipe_song6.py` → `make_song6_mix.py`

## 曲式

| 段落 | 小节 | 内容 |
|---|---|---|
| Intro | 0 | 白: 音乐盒滴落 + **长笛问句悬停** + 双簧管首答 |
| V1 | 4 | 青: 钢琴 8 分 + 竖琴流水 + pizz 反拍 + 长笛插话 |
| Pre | 12 | 弦乐渐入（蓝渐染）+ 双簧管回应 |
| C1 | 16 | 蓝: 全奏副歌 hook + 和声轨 |
| ITL | 25 | 长笛华彩对答（骤轻留白） |
| V2 / Pre / C2 | 29 / 37 / 41 | 再现 |
| Bridge | 50 | 白回归 + **长笛双簧管卡农追逐**（滞后 1 拍）+ build |
| C3+Tag | 58 | 升半音, **Tag 处长笛双簧管齐奏 = 接受** |
| Outro | 70 | 白蓝交融八度余韵消散 |

## 交付
| 文件 | 内容 |
|---|---|
| `*_complete.mp3` | **成品**（320k） |
| `*.flp` / `*_complete.mid` / `*_melody.mid/.wav` / `*_drums.wav` | FL 工程 + MIDI + 分轨 |
| `*_vocal_main.mid/.musicxml` / `*_vocal_harm.mid/.musicxml` | 人声分轨（全假名歌词） |
| `*_vocal_main_neu.wav` / `*_vocal_harm_neu.wav` | NEUTRINO 琴葉葵真声（48k，未进 git） |
| `lyrics.md` | 中日对照歌词 |

## 歌声合成
NEUTRINO Tau v3 + 琴葉葵（`D:\NEUTRINO_tool\`, GPU）。musicXMLtoLabel → neutrino_client(-m)。
主唱 297 音 E4–F#5, 和声 154 音（全副歌+tag 下三度）。

---

# v2（慢节奏动漫风迭代）—— 2026-09-25 学习两首参考曲后重制

参考曲：Ayase《夜撫でるメノウ》、Lefty Hand Cream《恋音と雨空》（客观分析见 `docs\NEUTRINO虚拟歌姬制作手册.md` §3.6）。

## 参考曲分析结论 → v2 对应改动
| 参考曲特征（实测） | v2 改动 |
|---|---|
| BPM 感知 65-100（Ayase 99 / Lefty 65） | 92 → **84** |
| 动态比仅 1.6-1.8x，逐段叠层缓坡 | v1 段间 2.9x 大落差 → v2 缓坡递进（实测 1.26x，ITL 刻意留白除外） |
| onset 恒定 7-8/s = 恒定 16 分细分 | 副歌钢琴 16 分织体 + **clean guitar 16 分琶音铺底**（Lefty 核心织体）+ hat 16 分 |
| 中频 40%+ 主导、低频 <20% 克制、air 8-12% | 混音维持清透链（8k air shelf） |
| intro 留白要极端（Lefty 开头低频 3%） | Intro 只剩音乐盒+长笛问句 |
| 副歌人声加厚（Ayase 式堆唱） | 人声三层：主唱 + 下三度和声 + **低八度层（新增）** |
| 结尾大抽层 | Outro 弦乐→钢琴→音乐盒逐层抽空 |

## 人声三轨
`*_v2_vocal_main_neu.wav` / `*_v2_vocal_harm_neu.wav`（下三度）/ `*_v2_vocal_harm2_neu.wav`（低八度，C 段）

## 修复记录
v1 存在已知瑕疵：段起点字典 `offs['Pre']` 被两个同名 Pre 段覆盖 → v1 的 Pre1 段无人声、C3 段中混入错位歌词。
**v2 已修复**（段起点独立硬编码 + 补 V2 分支）。v1 的 complete.mp3 保留在 git 历史（3925d56 之后的版本）供对比。
