# 05「きみいろグラデーション」(你的颜色渐变) — 《终将成为你》粉蓝白渐变甜美风原创曲

- **速度/调/拍**: 100 BPM · A 大调（末段升半音到 B♭）· 4/4 · 2'50"
- **概念**: 颜色即心情。白（音乐盒留白）→ 粉（钢琴/拨弦心动）→ 蓝（弦乐/合唱沉淀），
  三色渐变铺满全曲；hook「きみいろ」落在大七度音上 = 甜味。
- 生成脚本: `_compose\song5_kimi_iro.py` → `_compose\pipe_song5.py` → `_compose\make_song5_mix.py`

## 曲式

| 段落 | 小节 | 内容 |
|---|---|---|
| Intro | 0 | 音乐盒 hook 预告 + 分解和弦（白） |
| V1 | 4 | 钢琴 8 分 + 拨弦反拍 + 软鼓（粉） |
| Pre | 12 | 弦乐上行 swell + 竖琴 |
| C1 | 16 | 全奏副歌 hook（蓝），和声轨入 |
| ITL | 24 | 音乐盒 + 长笛回调 |
| V2 / Pre / C2 | 28 / 36 / 40 | 再现 |
| Bridge | 48 | 音乐盒独白 + 气声，后半 build |
| C3+tag | 56 | **升半音 B♭**，tag「やさしいいろ」 |
| Outro | 67 | 音乐盒回声消散 |

## 交付
| 文件 | 内容 |
|---|---|
| `*_complete.mp3` | **成品**（320k） |
| `*.flp` / `*_complete.mid` / `*_melody.mid` / `*_melody.wav` | FL 工程 + MIDI + 渲染伴奏 |
| `*_drums.wav` | 定制柔和鼓（numpy 合成） |
| `*_vocal_main.mid/.musicxml` / `*_vocal_harm.mid/.musicxml` | 人声分轨（带假名歌词） |
| `*_vocal_main_neu.wav` / `*_vocal_harm_neu.wav` | NEUTRINO 琴葉葵真声（48k，未进 git） |
| `lyrics.md` | 中日对照歌词 |

## 歌声合成
NEUTRINO Tau v3 + 琴葉葵 v3.2.2（部署于 `D:\NEUTRINO_tool\`），GPU 渲染。
`musicXMLtoLabel → neutrino_server + neutrino_client(-m)`，输出与乐谱 0 偏移。
注意: 歌词 mora 不能为空字符串（空歌词音符会让音素链断裂 → "Failed to load phrase data"）。


---

# v2（四色酸甜升级版）—— 2026-09-25 层次/密度/酸甜

v1 保留在 git 历史。`*_v2_*` 全套交付（complete_v2.mp3 / v2.flp / v2_complete.mid / v2_melody.wav / v2_vocal_harm_neu.wav；主唱复用 v1 渲染）。

## 升级点
| 项 | 内容 |
|---|---|
| 橙层（新） | E.Piano(prog4) 切分暖和声 + Vibraphone(prog11) 高音区 16 分玻璃闪光（479 音） |
| 酸甜和声 | Dm6（iv 借用）: Pre 末长音下 / Bridge 末 / **Outro 第2小节 酸→甜收束**; B7(V/V) 主歌拉力; 副歌 E9 |
| 密度 | 副歌 piano 16 分 drive + 弦乐内声部 8 分移动 + hat 16 分 + 军鼓鬼音; 主歌竖琴 8 分 + 贝斯经过音 + 16 分 hat ghost; 小节尾 16 分经过音 |
| 和声轨 | 50 音 → 155 音（扩到全副歌 + tag），重渲染 |

和声脚本: `_compose/song5_v2.py`（改和声/配器后重跑 → NEUTRINO 重渲染 harm → make_song5_v2_mix.py）
