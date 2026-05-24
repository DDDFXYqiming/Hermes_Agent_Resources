---
name: fox-finance-methodology
description: "Use when applying or explaining the investment methodology from the 40-video Bilibili corpus: technical chart analysis, ETF timing, support/resistance, EMA tunnel, KDJ/MACD/Bollinger/Fibonacci rules, volume-amount validation, and risk vetoes. Produces quantified, judgeable trading-rule checklists with evidence references; not investment advice."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms:
  - windows
  - linux
  - macos
metadata:
  hermes:
    tags: [finance, technical-analysis, trading-rules, bilibili, etf, risk-control]
    related_skills: [video-notes-generator]
---

# Investment Methodology

## Overview

This skill captures the repeatable methodology extracted from 40 visual-enhanced notes of a Bilibili investment-analysis video corpus. It turns the corpus into a rule checklist that is as quantifiable and falsifiable as possible: trend structure first, risk veto before buy signals, then EMA/KDJ/MACD/Bollinger/Fibonacci/volume confirmation.

This is **not investment advice** and should not be presented as a prediction. Use it to reproduce and audit the UP's analysis style, explain why a signal is valid/invalid under that style, or convert chart observations into a structured decision card.

## When to Use

Use this skill when the user asks to:

- 按该视频体系的方法分析黄金、美股、港股/A股ETF、周期股、比特币、铜、白银等。
- 提取、复盘、执行或检查该视频体系的交易规则、方法论、买卖点。
- 把某张K线图/行情截图/视频笔记转成可判断的交易信号。
- 比较支撑压力、趋势线、EMA隧道、KDJ、MACD、布林带、斐波那契、成交量/成交额是否共振。
- 生成「触发条件 → 量化判定 → 行动 → 失效条件 → 证据」格式的规则卡。

Do **not** use it for fundamental valuation,财报建模, or guaranteed price forecasts. If price/indicator data is missing, state which checks are unverified instead of inventing them.

## Quick Workflow

1. **Normalize the asset and timeframe**: 国内资产 / 国际资产 / 加密 / ETF / 个股；优先周线→日线→4H，大周期先定方向，小周期只找节奏。
2. **Apply risk vetoes first**: 双趋势线下方、长期趋势线多次受压、抛物线末端、鱼尾行情、历史大顶/M2背离、趋势未反转前重仓，任一命中先降级为「回避/轻仓」。
3. **Map structure**: 箱体上下沿、平行通道上下轨、趋势线、关键斐波那契位、1号/2号EMA隧道、前高/前低。
4. **Confirm trend and timing**: EMA8/13/21/55/83，隧道EMA144/169与288/338，KDJ金叉/死叉，MACD零轴与能量柱，布林带中/上下轨。
5. **Validate with volume/amount**: 成交量与成交额共振才增强信号；量额背离的阳线/阴线要当作「假性K线」处理。
6. **Output a signal card** using `templates/signal-card.md`; every conclusion must have a trigger, numeric/visual判定, action, invalidation, and evidence/confidence.

## Rule Hierarchy

1. **Risk veto overrides entry**: 高位、双趋势线下方、跌破关键结构位、熊旗/鱼尾/M2顶背离时，即使小周期金叉也不能直接升级为买入。
2. **Structure overrides indicator**: 支撑/压力/趋势线/箱体/通道/斐波那契先于KDJ、MACD。
3. **Big timeframe overrides small timeframe**: 周线支撑/压力强于日线，日线强于4H/小时线。
4. **Confirmation beats anticipation**: 优先「突破→站稳→回踩不破→再起」右侧确认；左侧只能轻仓/分批。
5. **No single-indicator trades**: KDJ/MACD/Bollinger are confirmation tools;至少要和结构或均线系统共振。

## Core Quantitative Rules

See `references/rulebook.md` for the full rulebook. Minimum checks:

- **EMA/tunnel**: EMA8/13 are short-term buy zones in an uptrend; EMA13/21 cross + MACD cross + price above EMA144/169 tunnel is the strongest simple buy confirmation. EMA144/169 = 1号隧道; EMA288/338 = 2号隧道.
- **KDJ**: K>80/J>100 overbought, K<20/J<0 oversold. In震荡/整理区间: KDJ<30金叉买, KDJ>70死叉卖. Strong trends can钝化, so require structure confirmation.
- **Fibonacci**: 国际资产用0.618定义趋势底线/反转线; 国内资产牛市结构更重视0.382是否守住. Draw from wick high to wick low.
- **MACD**: 零上金叉强势涨, 零上死叉看回调, 零下金叉只当反弹, 零下死叉弱势低, 零轴本身是支撑/压力.
- **Volume/amount**: 成交量与成交额同向为真信号; 量平/放量但成交额缩量 = 阳线/阴线有水分, 不追高或重新判断.
- **Positioning**: 买在足够低（结构支撑/箱底/隧道/周线支撑）或足够强（突破站稳、压力变支撑、均线多头支撑）。周期股/ETF必须分批，禁止一把梭。

## Output Requirements

When using this skill, produce a concise table:

| Check | Status | Evidence | Action | Invalidation |
|---|---|---|---|---|

Then give one of these final labels only:

- `回避/风险优先`
- `观察等待确认`
- `轻仓试探/底仓`
- `分批低吸`
- `右侧确认买入`
- `持有/加仓`
- `减仓/卖出`

Never output a vague conclusion like「看起来不错」without a rule row.

## Evidence and Source Files

- Main rules: `references/rulebook.md`
- Evidence map: `references/evidence-map.md`
- Timestamped evidence: `references/timestamped-evidence.md`
- Source video index: `references/source-videos.md`
- Output template: `templates/signal-card.md`
- Optional validator: `scripts/validate_skill.py`

Source corpus default root: `<SOURCE_VIDEO_NOTES_ROOT>`. If moved, set `METHODOLOGY_VIDEO_NOTES_ROOT` to the new root.

## Common Pitfalls

1. **Turning rules into predictions.** Keep outputs conditional: if support holds → X; if support breaks → Y.
2. **Ignoring risk vetoes.** A KDJ金叉 inside a broken structure is not a valid buy signal.
3. **Using 0.618 everywhere.** 国际资产重0.618; 国内板块牛市结构多用0.382.
4. **Forgetting wicks in Fibonacci.** High/low shadows count.
5. **Treating high open as a buy.** In this corpus, 高开靠近均线/压力 often means do not chase; may be a sell/reduce point unless it breaks and stands firm.
6. **Skipping volume/amount.** A candle without amount confirmation may be fake even when price shape looks good.

## Verification Checklist

- [ ] Frontmatter is valid YAML and description is under 1024 characters.
- [ ] Rulebook includes trigger, quant判定, action, invalidation, and evidence style.
- [ ] Evidence map cites BV IDs/titles from the 40-video corpus.
- [ ] Template produces rule rows and a final label from the allowed set.
- [ ] No rule is phrased as guaranteed investment advice.
