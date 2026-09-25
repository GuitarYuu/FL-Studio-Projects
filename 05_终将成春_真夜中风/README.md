# 02「终将成春」 — ずっと真夜中でいいのに。（ZUTOMAYO）风格致敬 ×《终将成为你》

- **速度/调/拍**: 142 BPM · F♯ 小调（副歌转关系大调 A） · 4/4 · 约 3'03"
- **概念**: 主歌 16 分切分 = 对不齐的心跳与踌躇；副歌转 A 大调 = "和你在一起时的春天"；
  末段整体升全音（→B 大调）= 两份心意重迭；结尾一记和弦急停 = 没说出口的那句话。
- 生成脚本: `_compose\song2_yagate_haru.py`

## 曲式（小节起点）

| 段落 | 小节 | 内容 |
|---|---|---|
| Intro | 0 | 贝斯+吉他+电钢琴 **同度 riff**（2 小节循环），第 3 小节鼓进 |
| V1 | 8 | 切分主唱（16 分弱起），闷音吉他 16 分、放克贝斯 |
| Pre | 24 | Bm7→C#7→D→E 逐级抬升，末小节军鼓滚奏 |
| C1 | 32 | A 大调副歌，钩子「C#5–A4 / F#5 落 D5」 |
| ITL | 40 | riff 间奏 |
| V2 / Pre / C2 | 44 / 60 / 68 | 再现；C2 末加 adlib（G#5–A5–B5） |
| Break | 76 | 半拍分解 + 电钢琴长和弦，末 2 小节 build |
| C3 + tag | 92 | **升全音到 B 大调**，末 4 小节 tag |
| Outro | 104 | riff 两遍后**全乐队急停** |

## 核心和声

- 主歌: `F#m7 – Dmaj7 – Bm7 – C#7sus4/C#7`（小调 iv–VII–V 功能圈）
- 预副歌: `Bm7 – C#7 – Dmaj7 – Eadd9`（全音上行链条）
- 副歌: `A – E/G# – F#m7 – Dmaj7 – A/C# – D – E – E7`（下行贝斯 A→G#→F#→E）
- Break: `F#m9 – Dmaj7 – Bm7 – C#7#9`（#9 是 ACA-ne 式的"辣味"）

## 风格要点（对照 ZUTOMAYO 的写法）

1. 16 分放克底: 闷音吉他反拍重音、贝斯八度+半音接近、鼓组军鼓鬼音（vel≈30）；
2. riff 三件套同度（bass 低八度 / 吉他高八度 / EP 打点），带滑音 pitch bend；
3. 主唱线大量 16 分弱起与跳进（C#5→F#5），副歌换关系大调提亮；
4. 末段升全音 + 急停收尾。

## FL Studio 里替换音色（GM → 建议）

| 轨道 | GM | 换成 |
|---|---|---|
| Riff Guitar | 29 | FLEX 电吉他过载 / FL Slap? 建议 Guitar Rig 类；riff 记得紧贴节拍器 |
| Slap Bass | 33 | BooBass + Fruity Blood Overdrive（或 FLEX Finger Bass） |
| E.Piano | 4 | FL Keys Rhodes（副歌加 tremolo 轻） |
| Mute Guitar | 27 | FLEX Muted/Funk Guitar |
| Lead Vocal | 80 | 音源里最"咬字"的 lead（Harmor 共振峰调亮） |
| Synth Stab | 81 | Sytrus 方波 stab（音量低） |
| Warm Pad | 89 | FLEX Warm Pad / Sytrus |
| （鼓已剥离） | — | drum_synth.wav；换 FPC 建议选干、紧的放克套鼓 |

混音起手：总线压缩要快 attack；贝斯与底鼓 sidechain；riff 三轨 pan 微散（吉他 35%/EP 45%）。
