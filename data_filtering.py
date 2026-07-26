import pandas as pd

# Load dataset
df = pd.read_csv("dataset/students.csv")

print("===== Original Dataset =====")
print(df)

# Filter rows where Age is greater than 20
print("\n===== Students with Age > 20 =====")
filtered_age = df[df["Age"] > 20]
print(filtered_age)

# Filter rows where CGPA is greater than or equal to 8.5
print("\n===== Students with CGPA >= 8.5 =====")
filtered_cgpa = df[df["CGPA"] >= 8.5]
print(filtered_cgpa)

# Select specific columns
print("\n===== Selected Columns =====")
selected_columns = df[["Name", "Department", "CGPA"]]
print(selected_columns)

# Sort dataset by CGPA (Highest First)
print("\n===== Sorted by CGPA =====")
sorted_data = df.sort_values(by="CGPA", ascending=False)
print(sorted_data)

# Save filtered dataset
sorted_data.to_csv("dataset/students_filtered.csv", index=False)

print("\nFiltered dataset saved successfully!")