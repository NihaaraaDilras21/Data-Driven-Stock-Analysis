import pandas as pd

df = pd.read_csv("processed_data.csv")

# Pivot data: rows = date, columns = ticker, values = close price
pivot_df = df.pivot_table(index="date", columns="ticker", values="close")

# Calculate correlation matrix
correlation_matrix = pivot_df.corr()

# Save to CSV
correlation_matrix.to_csv("correlation_matrix.csv")

print("\nCorrelation matrix saved to correlation_matrix.csv")
