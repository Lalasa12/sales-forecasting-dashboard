import pandas as pd

df = pd.read_csv(
    "Sample - Superstore.csv",
    encoding="latin1"
)

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

print(monthly_sales.head())

monthly_sales.to_csv(
    "monthly_sales.csv",
    index=False
)

print("Monthly sales file created!")