import pandas as pd
import ast

# Load your monthly gainers/losers file
df = pd.read_csv("monthly_gainers_losers.csv")

# The goal:
# Convert this structure:
# month | top_5_gainers | top_5_losers
# Into:
# month | stock | type (gainer/loser)

records = []

for _, row in df.iterrows():
    month = row["month"]

    # Convert list-like strings into Python lists
    gainers = ast.literal_eval(row["top_5_gainers"])
    losers  = ast.literal_eval(row["top_5_losers"])

    # Add gainers
    for stock in gainers:
        records.append({
            "month": month,
            "stock": stock,
            "type": "Gainer"
        })

    # Add losers
    for stock in losers:
        records.append({
            "month": month,
            "stock": stock,
            "type": "Loser"
        })

# Convert into dataframe
out_df = pd.DataFrame(records)

# Save cleaned file
out_df.to_csv("monthly_trend_clean.csv", index=False)

print("monthly_trend_clean.csv has been successfully created!")
