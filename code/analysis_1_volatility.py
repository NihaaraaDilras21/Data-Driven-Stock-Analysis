import pandas as pd

df = pd.read_csv("processed_data.csv")

# Group by ticker and calculate volatility (std deviation of daily returns)
volatility = (
    df.groupby("ticker")["daily_return"]
    .std()
    .sort_values(ascending=False)
    .reset_index()
)

volatility.columns = ["Ticker", "Volatility"]

# Save output
volatility.to_csv("top_10_volatile_stocks.csv", index=False)

print("\nTop 10 Most Volatile Stocks:")
print(volatility.head(10))
print("\nSaved to top_10_volatile_stocks.csv")
