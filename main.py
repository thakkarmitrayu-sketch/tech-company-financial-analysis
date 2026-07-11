"""
Tech Company Financial Analysis
--------------------------------
Pulls recent annual financials for 5 major tech companies, computes
revenue growth and profit margin, and produces two comparison charts.

Run this in Google Colab (colab.research.google.com) for a zero-setup
option, or locally with: pip install yfinance pandas matplotlib
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]


def get_financials(ticker):
    """Pull annual revenue and net income for one ticker."""
    stock = yf.Ticker(ticker)
    financials = stock.financials.T.sort_index()  # oldest -> newest

    df = pd.DataFrame({
        "Revenue": financials.get("Total Revenue"),
        "Net Income": financials.get("Net Income"),
    })
    df["Profit Margin (%)"] = (df["Net Income"] / df["Revenue"]) * 100
    df["Ticker"] = ticker
    return df


def main():
    all_data = []
    for t in TICKERS:
        try:
            df = get_financials(t)
            all_data.append(df)
            print(f"Pulled data for {t}")
        except Exception as e:
            print(f"Failed for {t}: {e}")

    combined = pd.concat(all_data)
    combined.to_csv("financial_data.csv")
    print("\nSaved financial_data.csv\n")
    print(combined)

    # Chart 1: Revenue over time, all companies
    plt.figure(figsize=(10, 6))
    for t in TICKERS:
        subset = combined[combined["Ticker"] == t]
        plt.plot(subset.index, subset["Revenue"] / 1e9, marker="o", label=t)
    plt.title("Revenue Over Time (Billions USD)")
    plt.xlabel("Fiscal Year")
    plt.ylabel("Revenue ($B)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("revenue_over_time.png")
    plt.close()

    # Chart 2: Profit margin comparison, most recent year
    latest = combined.groupby("Ticker").last()
    plt.figure(figsize=(8, 5))
    plt.bar(latest.index, latest["Profit Margin (%)"])
    plt.title("Profit Margin by Company (Most Recent Fiscal Year)")
    plt.ylabel("Profit Margin (%)")
    plt.tight_layout()
    plt.savefig("profit_margin_comparison.png")
    plt.close()

    print("\nCharts saved: revenue_over_time.png, profit_margin_comparison.png")

    # Simple takeaway
    fastest_growth = combined.groupby("Ticker")["Revenue"].apply(
        lambda s: (s.iloc[-1] / s.iloc[0] - 1) * 100
    ).idxmax()
    most_profitable = latest["Profit Margin (%)"].idxmax()
    print(f"\nTakeaway: {fastest_growth} had the fastest revenue growth; "
          f"{most_profitable} had the highest profit margin last year.")


if __name__ == "__main__":
    main()
