# FL Studio Projects — 原创歌曲工程

三首用 FL Studio 2025 制作（ZCode 辅助作曲）的原创歌曲工程文件。

| # | 歌曲 | 来源 | 调性/速度 | 时长 | 说明 |
|---|---|---|---|---|---|
| 01 | 启程的那天 (Song For The Graduate) | 全新创作 | C 大调 / 76 BPM | 2:59 | 毕业赠礼，钢琴叙事+弦乐，含歌词 |
| 02 | 五月之舞 (Dance in May) | 补全自 2026-5-28 的 22 音动机 | G 大调 / 130 BPM | 2:48 | 舞曲，原动机原样保留为主题 |
| 03 | MAD之夜 (MAD Night) | 补全自 MAD_TRY（语音采样工程） | A 小调 / 140 BPM | 2:50 | 高能量 backing track，预留语音采样乐句空间 |

## 目录结构

每个歌曲文件夹内：
- `*.flp` — FL Studio 2025 工程文件（打开即用；旋律声部已导入为 FLEX 通道）
- `*.mid` — 完整版 MIDI（Type-1，含 GM 鼓组轨；`graduation_song.mid` 为 01 的原始完整版）
- `gen_song*.py` — 作曲生成脚本（Python + mido，可重新生成 MIDI）
- `README.md` — 各曲结构与声部说明（02/03）

## 使用

用 FL Studio 2025（v24+ 应可兼容）直接打开 `.flp`。完整 MIDI（含鼓组）也可直接拖入任意 DAW。
01 的歌词见 `01_Song_For_The_Graduate/歌词_Lyrics.txt`。

---
由 ZCode 完成作曲补全与工程化 · 2026-09
