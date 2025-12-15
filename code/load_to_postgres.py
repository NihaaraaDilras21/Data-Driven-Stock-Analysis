import pandas as pd
from sqlalchemy import create_engine

# 1️⃣ Load processed CSV
df = pd.read_csv("processed_data.csv")

# 2️⃣ Convert date column
df["date"] = pd.to_datetime(df["date"])

# 3️⃣ Create connection string
# Replace 'admin123' with YOUR PostgreSQL password
engine = create_engine("postgresql://postgres:nikkuy2k@localhost:5432/nifty50")

# 4️⃣ Load into SQL
df.to_sql("stock_data", engine, if_exists="replace", index=False)

print("SUCCESS! Data loaded into PostgreSQL table 'stock_data'.")
print("Total rows loaded:", len(df))
