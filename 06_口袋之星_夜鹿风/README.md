# 03「口袋之星」 — ヨルシカ（n-buna）风格致敬 × 宝可梦

- **速度/调/拍**: 92 BPM · D 大调 · 4/4 · 约 3'03"
- **概念**: 清晨草丛、出发的旅行。钟琴 = 宝可梦的鸣叫与图鉴闪光（前奏动机全曲贯穿）；
  桥段借 bVI/B♭ 与 Gm = 夜晚露营的篝火（单簧管领奏）；最终副歌回到大调 + 高八度钟琴 = 进化与抵达。
  旋律为原创，仅取"旅程感"，不引用任一宝可梦游戏实际旋律。
- 生成脚本: `_compose\song3_pocket_star.py`

## 曲式（小节起点）

| 段落 | 小节 | 内容 |
|---|---|---|
| Intro | 0 | 木吉他指弹 + 钟琴动机（A5–B5–D6…） |
| V1 | 4 | 主歌（轻鼓+边击感），旋律围绕 A4–D5 |
| Pre | 12 | B4→E5 爬升，弦乐垫进入 |
| C1 | 16 | 副歌「B4–D5 / D5–B4–G4」，过载吉他墙 |
| ITL | 24 | 间奏：钟琴动机 + 手风琴低声部 |
| V2 / Pre | 28 / 36 | 再现（鼓稍满） |
| C2 | 40 | 副歌，末句抬到 E5 悬停 |
| Bridge | 48 | **Gm – B♭ – F – C**（借小调），单簧管主奏 |
| C3 | 56 | 终副歌：钟琴对旋律 + 过载加厚，末小节补 F#5 |
| Outro | 64 | 指弹渐弱，钟琴再现动机，E–F# 三连颤音 → D6 长音（"宝可梦的叫声"） |

## 核心和声

- 主歌: `D – A/C# – Bm7 – G`（I–V/3–vi–IV 下行贝斯）
- 副歌: `G – A – F#m7 – Bm7 – G – A – D`（IV–V–iii–vi 回到 I）
- 桥段: `Gm – B♭ – F – C – Gm – B♭ – Asus4 – A7`（bVI/bVII 借用，夜的部分）

## 风格要点（对照 n-buna 的写法）

1. 指弹木吉他 8 分贯穿，副歌叠: 指弹 + 高把位 clean 分解 + 过载长和弦三层"吉他墙"；
2. 主旋律长音起步、级进下行，句尾收在长音上（ヨルシカ 式"叹息"）；
3. 配器讲故事: 钟琴（铃声）→ 单簧管（夜）→ 全员（天亮）；
4. 鼓极简: 主歌只有底鼓+镲点，副歌才给完整 backbeat。

## FL Studio 里替换音色（GM → 建议）

| 轨道 | GM | 换成 |
|---|---|---|
| Acoustic Gt | 25 | FL Keys? 无木吉他 → FLEX Acoustic / DirectWave 指弹采样 |
| Clean Gt | 27 | FLEX Clean Electric |
| Overdrive Gt | 29 | FLEX Drive Guitar（副歌双轨 pan L/R 更接近原风格） |
| Bass | 33 | BooBass |
| Glockenspiel | 9 | FLEX Mallets / Sytrus 铃（这是"宝可梦"的灵魂，选清脆的） |
| Accordion | 21 | FLEX World / DirectWave 手风琴 |
| Clarinet | 71 | FLEX Orchestral |
| Lead Vocal | 81 | 柔和 saw + 慢 attack；有条件换歌声合成器 |
| Strings | 48 | FLEX Strings（副歌低音量垫底即可） |
| （鼓已剥离） | — | drum_synth.wav；换 FPC 建议软一点的 indie 套鼓 |

混音起手：长混响 + 八分延迟 send 给钟琴/单簧管；吉他墙左右各 -3dB 不抢主旋律。
