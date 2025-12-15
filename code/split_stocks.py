import pandas as pd
from pathlib import Path

# 1️⃣ Load processed data
df = pd.read_csv("processed_data.csv")

# 2️⃣ Create output folder
output_folder = Path("stocks")
output_folder.mkdir(exist_ok=True)

# 3️⃣ Loop through each unique Ticker
for ticker in df["ticker"].unique():
    ticker_df = df[df["ticker"] == ticker]

    # 4️⃣ Save each stock's data as CSV
    file_path = output_folder / f"{ticker}.csv"
    ticker_df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")

print("\nALL STOCK FILES CREATED SUCCESSFULLY!")
