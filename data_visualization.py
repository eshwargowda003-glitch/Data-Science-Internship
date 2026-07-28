import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/students.csv")

# -----------------------------
# Bar Chart - Student CGPA
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["CGPA"])
plt.title("Student CGPA")
plt.xlabel("Students")
plt.ylabel("CGPA")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# -----------------------------
# Line Chart - Age of Students
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Age"], marker="o")
plt.title("Student Age")
plt.xlabel("Students")
plt.ylabel("Age")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# -----------------------------
# Pie Chart - Department Count
# -----------------------------
department_count = df["Department"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Students by Department")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

print("Charts created successfully!")