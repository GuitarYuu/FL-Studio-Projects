# 04「电气花火」 — YOASOBI「BiriBiri」风格致敬 × 宝可梦

- **速度/调/拍**: 150 BPM · A 大调（终段升半音到 B♭） · 4/4 · 约 2'53"
- **概念**: 对标 YOASOBI×宝可梦的「BiriBiri」——电老鼠的噼里啪啦。两小节一循环的
  洗脑钩子（E5-E5-D5-C#5→B4），四踩底鼓 + 反拍贝斯的舞曲律动，钟琴高八度对钩子
  = 电火花的"啪嚓"感。**无人声成品**：Lead Vocal 轨就是"虚拟歌姬位"。
- 生成脚本: `_compose\song4_biribiri.py`；**另附 `vocal_lead.mid`**（428 音，仅主旋律，
  A 大调 150bpm，终段已含移调）——拖进 OpenUTAU / Synthesizer V / VOCALOID 填词即得人声。

## 层次感设计（逐段加层/减层）

| 段落 | 小节 | 层叠（→ 表示新增） |
|---|---|---|
| Intro | 0 | 垫 + 钩子预告（主唱+钟琴+12）→ 4 小节后 riff + 律动进 |
| A1 | 8 | 放克贝斯 + EP 钉 + 鼓 + 主唱（四层） |
| Pre | 24 | →16分琶音、反拍贝斯，末小节镲片/军鼓滚奏 build |
| B1 | 28 | **drop**：→钢琴 16 分驱动、副歌和弦钉、主唱加倍、四踩+拍手（七层全开） |
| Post | 36 | riff 回收 |
| A2 | 40 | →闷音吉他扫弦、琶音常驻、低垫 |
| B2 | 60 | →钟琴高八度对钩子（后 4 小节） |
| Riff | 68 | riff + 低八度方波 |
| Break | 72 | 减到 垫+贝斯+EP 三层，半拍长音；末 4 小节 build（贝斯抽空） |
| B3/B3' | 84/92 | **升半音**，钩子+高八度钟琴全开；B3' 末句爬到 A5 |
| Outro | 100 | 钩子淡出 + 两次全乐队 hit 收束 |

## 核心和声

- 主歌: `F♯m7 – Dmaj7 – A – E`（vi–IV–I–V 循环）
- 副歌: `A – E – F♯m7 – D`（I–V–vi–IV，洗脑循环）
- Break: `F♯m7 – E – Dmaj7 – C♯m7`（下行，长音）

## 洗脑钩子的写法（BiriBiri 式）

1. 动机只有 5 个音（E5 D5 C#5 B4 A4），2 小节 call + 2 小节 response，全曲循环 ≥6 次；
2. 节奏前紧后松（4×八分 + 长音），每遍入点都踩在四踩底鼓上；
3. 副歌和声只用 I–V–vi–IV，任何一遍都能跟着哼。

## 接虚拟歌姬 / 人声音源

1. **OpenUTAU / SynthV**: 导入 `vocal_lead.mid`，工程 A 大调 150bpm；按段落填词即可
   （副歌钩子建议「ら・ら・ら」或中文「电·气·花·火」开头的双字词）；
2. **FL Studio 内模拟**: Lead Vocal 通道换人声音源（FLEX Vocal 组 / DirectWave 加
   "oooh"采样 / Painful Singing 类音源），保留 Lead Double 作和声位；
3. 不想加人声：`complete.mp3` 本身就是纯伴奏（主唱位由合成器占位）。

## FL 音色替换（GM → 建议）

| 轨道 | GM | 换成 |
|---|---|---|
| Lead Vocal | 81 | 虚拟歌姬 / 人声音源（见上） |
| Lead Double | 80 | Sytrus 超锯齿（-6dB 垫主唱） |
| Glockenspiel | 9 | FLEX Mallets（电火花感选亮脆的） |
| Piano Drive | 0 | FL Keys Grand（副歌 16 分驱动） |
| E.Piano | 4 | FL Keys Rhodes |
| Arp Synth | 81 | Sytrus/3xOsc 亮方波琶音 |
| Riff Guitar | 29 | FLEX 过载（riff 处紧贴节拍） |
| Slap Bass | 33 | BooBass + 轻过载 |
| Warm Pad | 89 | FLEX Warm Pad |
| （鼓已剥离） | — | drum_synth.wav；换 FPC 选电子舞曲套鼓 |
