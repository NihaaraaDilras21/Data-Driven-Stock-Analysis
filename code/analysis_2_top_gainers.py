import pandas as pd

df = pd.read_csv("processed_data.csv")

# Get last record per ticker (final cumulative return)
last_returns = (
    df.sort_values("date")
      .groupby("ticker")["cumulative_return"]
      .last()
      .reset_index()
      .sort_values("cumulative_return", ascending=False)
)

# Save top 5
top_5 = last_returns.head(5)
top_5.to_csv("top_5_highest_gainers.csv", index=False)

print("\nTop 5 Highest Gainers (Cumulative Return):")
print(top_5)
print("\nSaved to top_5_highest_gainers.csv")
