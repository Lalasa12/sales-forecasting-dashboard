import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv("monthly_sales.csv")

df.columns = ["ds", "y"]

model = Prophet()

model.fit(df)

future = model.make_future_dataframe(
    periods=12,
    freq="ME"
)

forecast = model.predict(future)

# Plot forecast
fig = model.plot(forecast)
forecast[["ds", "yhat"]].to_csv(
    "sales_forecast.csv",
    index=False
)

print("Forecast saved successfully!")

plt.show()