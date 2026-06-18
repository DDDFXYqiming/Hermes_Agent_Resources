---
name: ericwarn-dingning-pr-methodology
description: "Apply ericwarn丁宁's 市赚率(PR) investment methodology: PE/PB/ROE valuation, PR three formulas, dividend-payout correction, 0.4/0.5/0.6PR buy zones, A/H tax differences, red-dividend ETF rotation, and Buffett case studies. Use when the user asks about 丁宁、市赚率、PR估值、巴菲特案例复盘、红利ETF、A/H价值股估值、银行/保险/资源股估值, or wants valuation-first rules rather than chart timing."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms:
  - windows
  - linux
  - macos
metadata:
  hermes:
    tags: [finance, valuation, value-investing, pr, roe, dividend, buffett, xueqiu]
    related_skills: [fox-finance-methodology]
---

# Ericwarn丁宁市赚率方法论

## Overview

This skill packages the investment rules distilled from 雪球用户 `ericwarn丁宁` 的市赚率(PR)体系与用户整理文档 `C:\Users\39795\Desktop\books\雪球\PR.md`。它用于**估值优先**的价值投资判断：先看企业/指数是否便宜，再决定是否需要用技术分析寻找执行节奏。

This is **not investment advice**. Use it to reproduce, audit, or explain 丁宁's methodology; always mark data freshness and source quality.

## When to Use

Use this skill when the user asks to:

- 用丁宁/市赚率/PR体系分析个股、ETF、银行、保险、资源股、红利基金。
- 计算或解释 `PR = PE / (ROE × 100)`、第二公式、第三公式、修正市赚率。
- 处理股利支付率、分红率、A/H股股息税差异对估值阈值的修正。
- 复盘巴菲特案例：喜诗糖果、可口可乐、中国石油、华盛顿邮报、苹果、伯克希尔13F。
- 判断 0.4PR、0.5PR、0.6PR、1PR、A/H股股息税差对应的买卖区间。
- 比较丁宁体系与 fox 技术分析体系，或需要“估值罗盘 + 交易执行”的组合输出。

Do **not** use it as a short-term chart-trading system. For K线、EMA、KDJ、MACD、BOLL、支撑压力 and execution timing, pair with `fox-finance-methodology`.

## Quick Workflow

1. **Identify asset type**: 稳定ROE个股 / 周期股 / 指数基金 / 银行保险国央企 / H股红筹 / 商品或债券基金。
2. **Choose PR formula**:
   - Formula 1: `PR = PE / (ROE × 100)` for stable ROE companies.
   - Formula 2: `PR = PB / (ROE × ROE × 100)` for cyclicals or when PB + normalized ROE are better.
   - Formula 3: `PR = PE × PE / (PB × 100)` for index funds when PE/PB are easier than ROE.
   - Corrected PR: `PR' = N × PE / (ROE × 100)`, where `N = benchmark payout / actual payout`.
3. **Normalize inputs**: Use TTM PE/PB, multi-year or cycle-normalized ROE, current dividend payout, A/H dividend tax, and recent filings. Mark every stale value.
4. **Apply valuation bands**:
   - `<0.4PR`: 4折极低估区。
   - `0.4-0.5PR`: 巴菲特式好球区。
   - `0.5-0.6PR`: 可分批/小仓试探区。
   - `0.7-0.8PR`: 指数/ETF偏定投或观察区。
   - `≈1PR`: A股合理到高估阈值；H股因20%股息税常按0.8PR折算。
5. **Run vetoes before action**: ROE失真、分红率过低、周期景气误判、财务质量差、政策/税制变化、估值数据未验证 → downgrade confidence.
6. **Use fox only after valuation**: 丁宁 determines “is it cheap enough”; fox determines “where to enter/exit technically”.
7. **Output a valuation card** using `templates/pr-valuation-card.md`.

## Rule References

- Core rulebook: `references/rulebook.md`
- Evidence map and source notes: `references/evidence-map.md`
- Data verification checklist: `references/data-verification.md`
- Output template: `templates/pr-valuation-card.md`

## Output Requirements

Always include:

| Field | Requirement |
|---|---|
| Formula | Which PR formula is used and why |
| Inputs | PE/PB/ROE/payout/tax, with source and date |
| PR result | Raw PR and corrected PR if applicable |
| Band | 4折/5折/6折/合理/高估 |
| Vetoes | Any data, cycle, dividend, or accounting risk |
| Action label | One of the allowed labels below |

Allowed labels:

- `数据不足/不计算`
- `高估/回避`
- `合理偏贵/等待`
- `观察区/小仓研究`
- `6折区/轻仓试探`
- `5折区/分批低吸`
- `4折区/重点跟踪`
- `卖出/换仓候选`

## Common Pitfalls

1. **Do not treat PR as universal.** 科技股、成长股、周期顶点、亏损股、ROE异常股可能不适用。
2. **Do not use one-year peak ROE for cyclicals.** Use normalized multi-year/cycle ROE.
3. **Dividend payout correction is time-sensitive.** Example: 茅台 2024-2026 payout rose to 75-79%, while 丁宁 earlier used 50% as historical benchmark.
4. **A/H tax matters.** A股长期股息税可为0%；H股/红筹税负 lowers fair PR threshold.
5. **Never fabricate current data.** Use AnySearch/finance sources and mark stale values.
6. **Separate valuation from timing.** Cheap can get cheaper; use fox methodology or explicit technical confirmation for execution.

## Verification Checklist

- [ ] Inputs have source/date and are not silently extrapolated.
- [ ] Formula choice matches asset type.
- [ ] Corrected PR is used when payout differs materially.
- [ ] A/H dividend tax adjustment is noted.
- [ ] Output is a conditional valuation card, not investment advice.
