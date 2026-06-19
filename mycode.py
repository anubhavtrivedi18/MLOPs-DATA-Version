import pandas as pd
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Sample dataset
data = {
    "id": [1, 2, 3],
    "name": ["Aman", "Ravi", "Neha"],
    "score": [85, 90, 88]
}

df = pd.DataFrame(data)

# Save CSV inside data folder
df.to_csv("data/data.csv", index=False)

print("CSV file created successfully in data/data.csv")