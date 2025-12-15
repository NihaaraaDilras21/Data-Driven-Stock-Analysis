import pandas as pd

# Load processed stock data
df = pd.read_csv("processed_data.csv")

# Load sector mapping
sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# Extract ticker from the 'Symbol' column
# Example: "ADANI ENTERPRISES: ADANIGREEN" → "ADANIGREEN"
sector_df["Ticker"] = sector_df["Symbol"].apply(lambda x: x.split(":")[-1].strip())

# Rename 'sector' column to 'Sector' for clarity
sector_df = sector_df.rename(columns={"sector": "Sector"})

# Merge stock data with sector info
df = df.merge(sector_df[["Ticker", "Sector"]], left_on="ticker", right_on="Ticker", how="left")

# Compute sector-wise average daily return
sector_returns = (
    df.groupby("Sector")["daily_return"]
      .mean()
      .reset_index()
      .sort_values("daily_return", ascending=False)
)

# Save result
sector_returns.to_csv("sector_wise_avg_daily_return.csv", index=False)

print("\nSector-wise Average Daily Returns:")
print(sector_returns)
print("\nSaved to sector_wise_avg_daily_return.csv")
