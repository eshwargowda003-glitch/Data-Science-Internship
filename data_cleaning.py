import pandas as pd

# Load dataset
df = pd.read_csv("dataset/students_dirty.csv")

print("----- Original Dataset -----")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Correct data types
df["Age"] = df["Age"].astype(int)

print("\n----- Cleaned Dataset -----")
print(df)

print("\nDataset Information:")
print(df.info())

# Save cleaned dataset
df.to_csv("dataset/students_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")