import yaml

# 1️⃣ Path to ONE yaml file — change this path to ANY file inside data/2023-10/
file_path = "data/2023-10/2023-10-03_05-30-00.yaml"

# 2️⃣ Open the yaml file
with open(file_path, "r") as f:
    content = yaml.safe_load(f)

# 3️⃣ Print the contents nicely
print("YAML CONTENT:\n")
print(content)
