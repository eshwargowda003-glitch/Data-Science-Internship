import pandas as pd

df = pd.read_csv("dataset/students.csv")

print("----- Dataset -----")
print(df)

print("\n----- First 5 Rows -----")
print(df.head())

print("\n----- Last 5 Rows -----")
print(df.tail())

print("\n----- Columns -----")
print(df.columns)

print("\n----- Dataset Information -----")
print(df.info())

print("\n----- Shape -----")
print(df.shape)