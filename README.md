# Tech Company Financial Analysis

A small Python project that pulls real financial data for 5 major tech
companies, computes key ratios, and visualizes how they compare.

## What it does
- Pulls the last 5 years of **revenue** and **net income** for Apple,
  Microsoft, Google, Amazon, and Meta using the `yfinance` library.
- Calculates **profit margin** for each company, each year.
- Generates two charts:
  - Revenue over time (all 5 companies)
  - Profit margin comparison (most recent fiscal year)
- Prints a one-line takeaway: which company grew revenue fastest, and
  which is most profitable.

## Why
This started as a resume project to show I can go from raw financial
data to a business-relevant insight — the kind of task a data analyst
or FP&A role actually involves, without needing deep IB/quant tooling.

## How to run
**Easiest (no install):** Open [Google Colab](https://colab.research.google.com),
paste in `main.py`, and run it.

**Locally:**
```bash
pip install yfinance pandas matplotlib
python main.py
```

## Output
- `financial_data.csv` — the raw pulled data
- `revenue_over_time.png` — revenue trend chart
- `profit_margin_comparison.png` — margin comparison chart

## Key takeaway
> Meta had the fastest revenue growth of the group, up ~72% from 2022 to
> 2025 ($117B → $201B). Microsoft had the highest profit margin in the
> most recent fiscal year (~36%), narrowly ahead of Google (~33%).
> Amazon posted a negative margin in 2022 but climbed to ~11% by 2025 —
> the clearest turnaround story in the data.

## Tools used
Python, pandas, matplotlib, yfinance
