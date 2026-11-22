[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Nmercy12/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Nmercy12/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

# news-image-20261121 (v4 "Fresh Pixel")

This is the v4 entry for the `news-image-20261121` bounty on [make.fun](https://make.fun). It is a complete, publication-grade newspaper front page summarizing world news for Saturday 21 November 2026 across 37 verified stories and 9 regions.

## Front Page Contents
- **Masthead & Sub-deck**: Saturday 21 November 2026 with headline summaries of major geopolitical and climate events.
- **UTC Timeline & KPI Strip**: Key timestamps and major metric callouts (tankers attacked, COP31 countries, Peru quake magnitude, autonomous weapons talks, French protests, Bitcoin low).
- **Region Bar**: 9 regional chips with story counts.
- **Three Lead Stories (Heroes)**: Illustrated panels covering the Bahrain/Hormuz conflict, COP31 climate deadlock in Antalya, and the M6.7 Peru earthquake.
- **Ten Secondary Stories**: Grid of 5+5 detailed secondary reports with custom mini-art scenes and verification badges.
- **Where It Happened Map & Also On List**: Stylized world map with numbered location pins (1–13) alongside a 24-item "Also On" news roundup (14–37).
- **Date Check & Verification Legend**: Contextual box separating preceding/future events and clear source credibility legends.

## Architecture & Determinism
The generator script (`gen_v4.py`) produces `entry.png` (1024x1024, RGB, PNG format, under 1 MiB) with absolute determinism (no random number generation, time dependencies, or network calls).

`main.py` is written entirely in Python standard library (`os`, `shutil`, `hashlib`) and copies `entry.png` to the output destination (`MAKEFUN_OUTPUT_DIR` or `out/entry.png`), validating file sizes before completing.

## Run
```bash
python3 main.py
```

Find out more at [make.fun](https://make.fun).
