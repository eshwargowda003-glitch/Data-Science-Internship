import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("dataset/students_cleaned.csv")

# Export the dataset to a new CSV file
df.to_csv("dataset/exported_students.csv", index=False)

print("Cleaned dataset exported successfully!")

print("\nExported Dataset:")
print(df)