import pandas as pd

df = pd.read_csv("Sample - Superstore.csv",encoding="latin1")

print(df.head())

print(df.info())

print(df.describe())