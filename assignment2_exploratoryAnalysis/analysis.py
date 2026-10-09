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

print("Sales data summary:")
print(df.groupby)

highest_order_value = df["order_value_EUR"].max()
lowest_order_value = df["order_value_EUR"].min()

print("Highest order value:")
print(highest_order_value)

print("Lowest order value:")
print(lowest_order_value)

average_order = df["order_value_EUR"].mean()
if average_order > 1000:
    print("Average order value is above 1000 EUR.")
else:
    print("Average order value is 1000 EUR or below.")

print("Sales data summary:")
print("Total sales:")
print(df["order_value_EUR"].sum())
print("Average order value:")
print(df["order_value_EUR"].mean())
print("Total cost:")
print(df["cost"].sum())