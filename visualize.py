import pandas as pd
import matplotlib.pyplot as plt

# Read monthly sales data
df = pd.read_csv("monthly_sales.csv")

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create graph
plt.figure(figsize=(12,6))

plt.plot(
    df["Order Date"],
    df["Sales"]
)

plt.title("Monthly Sales Trend")

plt.xlabel("Date")

plt.ylabel("Sales")

plt.grid(True)

plt.show()