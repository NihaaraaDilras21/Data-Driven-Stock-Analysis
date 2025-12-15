import pandas as pd

# 1️⃣ Read the combined CSV
df = pd.read_csv("all_data.csv")

# 2️⃣ Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# 3️⃣ Sort by Ticker + date
df = df.sort_values(["Ticker", "date"])

# 4️⃣ Remove duplicate rows (just in case)
df = df.drop_duplicates()

# 5️⃣ Fix column names (make lowercase)
df.columns = [c.lower() for c in df.columns]

# 6️⃣ Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("CLEANING COMPLETE!")
print("Final rows:", len(df))
print("Cleaned file saved as cleaned_data.csv")
