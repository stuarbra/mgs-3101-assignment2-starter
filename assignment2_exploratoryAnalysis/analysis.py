import pandas as pd
df = pd.read_csv("data/Sales-Export_2019-2020.csv", thousands=",")
df.columns = df.columns.str.strip()

df["date"] = pd.to_datetime(df["date"])

print(df.head())
print(df.info())
print(df.describe())