import pandas as pd

# Load dataset
df = pd.read_csv("dataset/students.csv")

print("===== Dataset =====")
print(df)

print("\n===== Data Analysis =====")

# Total Students
print("Total Students:", df["ID"].count())

# Average Age
print("Average Age:", df["Age"].mean())

# Average CGPA
print("Average CGPA:", round(df["CGPA"].mean(), 2))

# Minimum CGPA
print("Minimum CGPA:", df["CGPA"].min())

# Maximum CGPA
print("Maximum CGPA:", df["CGPA"].max())

# Count Students in Each Department
print("\nStudents by Department:")
print(df["Department"].value_counts())