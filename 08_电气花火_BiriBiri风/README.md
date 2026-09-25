# 04「电气花火」 — YOASOBI「BiriBiri」风格致敬 × 宝可梦（v2 现代日系流行层次重构）

- **速度/调/拍**: 150 BPM · A 大调（终段升半音） · 4/4 · 2'54"
- **版本**: v2（当前）。v1 编曲见 git tag `dianqi-v1`（GitHub）与 `snapshots/v1/` 本地快照。
  v2 保留 v1 的钩子与曲式骨架，**编曲全部重做**，对标现代日系流行的制作手法。
- 生成脚本: `_compose\song4_v2.py`；`vocal_lead.mid`（428 音纯主旋律）供 OpenUTAU/SynthV 填词。

## v2 层次重构的六板斧（对照 v1）

1. **声部 register 分离**——贝斯占 40Hz 区、垫/EP 占中音区、钩子在 C5-A5、
   钟琴答句在 79-95（高音"火花"区），四层频段互不打架；
2. **侧链泵感**——垫与 EP 改为"重拍压低、反拍回弹"的 4 段包络（`pad_pump`），
   模拟现代舞曲的 sidechain 呼吸感；
3. **四小节微变化**——鼓组按小节轮换闭镲/踩镲/开镲轮廓、军鼓鬼音，副歌每第 3 小节
   加 ghost fill，终段 fill 递增到五件套；
4. **riser / 抽空**——预副歌末小节镲+军鼓双滚奏渐强且贝斯抽空，Break 末小节
   全队静默只留主唱爬音，drop 前留半拍真空；
5. **对钩子（counter-hook）**——钟琴在钩子长音的空拍上插下行 8 分答句
   （`glock_interlock`）；终副歌换成整条对旋律 `COUNTER`（C#6-A5 线条对钩子）；
6. **双钢琴位 + 气口**——副歌钢琴拆 L/R 两个声像位交错 16 分，每小节第 4 拍后半
   留缝给底鼓，律动更"跳"；低频加 sub 八度层 + 落头滑音。

## 曲式与层次表（v2）

| 段落 | 小节 | 层叠 |
|---|---|---|
| Intro | 0 | 侧链垫 + 心跳鼓 → 4 小节后 riff+律动，钩子预告（主唱+钟琴+12） |
| A1 | 8 | 放克贝斯 + EP 钉 + 鼓 + 主唱 |
| Pre | 24 | 加琶音（后 2 小节上移八度），末小节 riser 双滚奏+贝斯抽空 |
| B1 | 28 | drop：双钢琴驱动 + sub 低音 + 和弦钉 + 主唱加倍 + 四踩拍手 |
| A2 | 40 | 加闷音吉他、琶音常驻、低垫 |
| B2 | 60 | 加钟琴对钩子（后 4 小节） |
| Break | 72 | 减到垫+贝斯+EP → 琶音渐强 → 末小节全队抽空只留爬音 |
| B3/B3' | 84/92 | 升半音；B3' 换整条对旋律 + 钟琴全开，末句爬到 A5 |
| Outro | 100 | 钩子淡出 + 两次全乐队 hit |

## 接虚拟歌姬 / 人声音源

1. **OpenUTAU / SynthV**: 导入 `vocal_lead.mid`（A 大调 150bpm，含终段移调）填词即可；
2. **FL 内模拟**: Lead Vocal 通道换 FLEX Vocal / DirectWave 人声采样；
3. 不加人声：`complete.mp3` 即纯伴奏（合成器占位主唱位）。

## FL 音色替换（GM → 建议）

同 v1（见下表），另注意：Piano Drive 拆了 L/R 两轨，建议 pan 46/82 各挂一个
FL Keys，右轨 -3dB；Warm Pad 换音色后可挂真 sidechain（Fruity Limiter 侧链到鼓组）。

| 轨道 | GM | 换成 |
|---|---|---|
| Lead Vocal | 81 | 虚拟歌姬 / 人声音源 |
| Lead Double | 80 | Sytrus 超锯齿（-6dB） |
| Glockenspiel | 9 | FLEX Mallets（亮脆款） |
| Piano Drive L/R | 0 | FL Keys Grand ×2 |
| E.Piano | 4 | FL Keys Rhodes |
| Arp Synth | 81 | Sytrus/3xOsc 方波琶音 |
| Riff Guitar | 29 | FLEX 过载 |
| Slap Bass | 33 | BooBass + 轻过载 |
| Warm Pad | 89 | FLEX Warm Pad + 侧链 |
