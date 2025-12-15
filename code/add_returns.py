import pandas as pd

# 1️⃣ Load the cleaned data
df = pd.read_csv("cleaned_data.csv")

# 2️⃣ Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# 3️⃣ Sort for correct calculations
df = df.sort_values(["ticker", "date"])

# 4️⃣ Previous day's close
df["prev_close"] = df.groupby("ticker")["close"].shift(1)

# 5️⃣ Daily return
df["daily_return"] = (df["close"] - df["prev_close"]) / df["prev_close"]
df["daily_return"] = df["daily_return"].fillna(0)

# 6️⃣ Cumulative return (FIXED using transform)
df["cumulative_return"] = df.groupby("ticker")["daily_return"].transform(
    lambda x: (1 + x).cumprod() - 1
)

# 7️⃣ Save the results
df.to_csv("processed_data.csv", index=False)

print("\nSUCCESS! Daily & cumulative returns added.")
print("Saved to: processed_data.csv")
print("Total rows:", len(df))
