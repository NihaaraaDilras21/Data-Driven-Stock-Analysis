import pandas as pd

df = pd.read_csv("processed_data.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Extract month in YYYY-MM format
df["month"] = df["date"].dt.to_period("M")

# Group by month + ticker
monthly_change = (
    df.groupby(["month", "ticker"])
    .agg(first_close=("close", "first"), last_close=("close", "last"))
    .reset_index()
)

# Calculate monthly % change
monthly_change["pct_change"] = (
    (monthly_change["last_close"] - monthly_change["first_close"]) /
    monthly_change["first_close"]
)

# Save results month by month
all_results = []

for month in monthly_change["month"].unique():
    temp = monthly_change[monthly_change["month"] == month]

    top_5_gainers = temp.sort_values("pct_change", ascending=False).head(5)
    top_5_losers = temp.sort_values("pct_change").head(5)

    all_results.append({
        "month": str(month),
        "top_5_gainers": top_5_gainers[["ticker", "pct_change"]].to_dict(orient="records"),
        "top_5_losers": top_5_losers[["ticker", "pct_change"]].to_dict(orient="records"),
    })

# Convert results to DataFrame and save
result_df = pd.DataFrame(all_results)
result_df.to_csv("monthly_gainers_losers.csv", index=False)

print("\nMonthly Top 5 Gainers & Losers saved to monthly_gainers_losers.csv")
