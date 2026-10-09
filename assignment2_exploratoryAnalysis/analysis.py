import pandas as pd
df = pd.read_csv("data/Sales-Export_2019-2020.csv", thousands=",")
df.columns = df.columns.str.strip()

df["date"] = pd.to_datetime(df["date"])

print(df.head())
print(df.info())
print(df.describe())

print("shape:")
print(df.shape)

print(df.dtypes)
print("Data types:")

print("First 5 rows:")
print(df.head())

print("missing values:")
print(df.isnull().sum())

print(df.columns.to_list())

print("Statistics for order value and cost:")
print(df[["order_value_EUR", "cost"]].describe())