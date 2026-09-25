# 04「电气花火」 — YOASOBI「BiriBiri」风格致敬 × 宝可梦（v4 洗脑钩子版）

- **速度/调/拍**: 160 BPM · A 大调（终段升半音） · 4/4 · 2'47"
- **版本**: v4（当前）。v3=tag dianqi-v3（音墙版）、v2=dianqi-v2、v1=dianqi-v1，本地 snapshots/。
  v4 = v3 的音墙编曲原样保留 + **旋律全面钩子化** + 弱段重做 + 虚拟歌姬歌唱工程。
- 生成脚本: `_compose\song4_v4.py`

## v4 旋律的"洗脑上头"设计

1. **pickup 音头**: 副歌每句以「E5-E5-E5」三连 16 分起头（"bi-ri-bi"），全曲重复 6 次以上；
2. **2 小节单元格**: 副歌 = 同一单元格 ×4（仅第 4 次变化收束），主歌 = 4 小节乐句 ×2
   （仅句尾不同），第一遍就能跟着哼 = 熟悉感；
3. **五声倾向**: 旋律骨架 A-B-C#-E-F#（A 大调五声），D 只作经过解决——日系熟悉感的来源；
4. **预副歌节奏阶梯**: 4 分 → 8 分 → 长音加速爬升，接半拍真空后 drop；
5. **Break 重做**: 稀疏长音里插入 pickup 单元格预告（"motto motto"），间奏也洗脑；
6. **收束 fanfare**: 段落头钟琴 A5-C#6-E6 上行三和弦（宝可梦捕获 fanfare 式手势，原创）。

## 虚拟歌姬歌唱版（新增，已含成品音频）

| 文件 | 用途 |
|---|---|
| **`04_…_有人声版.mp3`** | **成品可播放**：NEUTRINO 琴葉葵(AOI) 主唱 + 三度和声叠 v4 音墙伴奏 |
| `vocal_project.ust` | OpenUTAU / UTAU 直接打开，假名逐音填好（含休止），换声库重唱用 |
| `vocal_lead.mid` | 纯主旋律 MIDI（SynthV/VOCALOID 用户导入用） |
| `lyrics_v4.txt` | 全词假名 + 分段标注 |

- 歌手: 琴葉葵 (Kotonoha Aoi, NEUTRINO Tau v3 扩散模型, GPU 渲染 43s)，
  主唱链 HP85→存在感 EQ→轻混响，和声 HP140→Haas 展宽 -70%；
- 歌词主题: 电光火花×冒险出发（びりびり ひかって きみと いく…），假名一音一符；
- 换人声: 改 `_compose\song4_v4_vocal.py` 的 VOICE = 'MERROW'（中性少年音）等重跑即可；
- 时间轴与伴奏 0 偏移对齐（MusicXML 绝对拍=工程绝对拍）。

## 编曲层（沿用 v3 音墙）

双手 16 分钢琴墙（LH 八度泵+run / RH 脉冲）、锯齿和弦墙（终段脉冲化）、合唱 Aahs 三度
和声、Ooh 长音垫、Vocal Chop、恒 8 分驱动贝斯（sub+滑音）、段落头弦乐 impact、
副歌四踩+全反拍开镲+鬼音、终副歌钟琴对旋律（C#6-A5 线条）。

## FL 音色替换（GM → 建议）

同 v3：Lead Vocal→虚拟歌姬/人声源；Lead Harmony→FLEX Choir；Ooh Pad→Voice Oohs；
Piano LH/RH→FL Keys ×2；Saw Wall→Sytrus 超锯齿（-8dB）；Vocal Chop→方波 chop；
Slap Bass→BooBass+过载；Strings Hit→FLEX Strings；鼓→drum_synth.wav 或 FPC 电子套鼓。
