import yaml
import pandas as pd
from pathlib import Path

# 1️⃣ Path to the data folder
data_folder = Path("data")

all_records = []  # we will store everything here

# 2️⃣ Loop through all month folders
for month_folder in data_folder.iterdir():
    if month_folder.is_dir():  # make sure it's a folder
        print(f"Reading folder: {month_folder}")

        # 3️⃣ Loop through all YAML files in that folder
        for yaml_file in month_folder.glob("*.yaml"):
            print(f"  Reading file: {yaml_file}")

            # 4️⃣ Load YAML content
            with open(yaml_file, "r") as f:
                content = yaml.safe_load(f)

            # 5️⃣ content is a list of dictionaries → extend to records
            if isinstance(content, list):
                all_records.extend(content)

# 6️⃣ Convert list of all records to DataFrame
df = pd.DataFrame(all_records)

# 7️⃣ Clean date column
df['date'] = pd.to_datetime(df['date'])

# 8️⃣ Save as CSV
df.to_csv("all_data.csv", index=False)

print("\nDONE! Combined CSV saved as all_data.csv")
print("Total rows:", len(df))
