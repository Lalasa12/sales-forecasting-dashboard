import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px

# Page Settings
st.set_page_config(
    page_title="Sales Forecast Dashboard",
    layout="wide"
)

st.title("📈 Sales Forecasting Dashboard")

# Read Data
df = pd.read_csv("monthly_sales.csv")

# Rename columns for Prophet
df.columns = ["ds", "y"]

# Train Model
model = Prophet()

model.fit(df)

# Future Predictions
future = model.make_future_dataframe(
    periods=12,
    freq="ME"
)

forecast = model.predict(future)

# KPI Section
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"{df['y'].sum():,.0f}"
)

col2.metric(
    "Average Monthly Sales",
    f"{df['y'].mean():,.0f}"
)

col3.metric(
    "Predicted Next Month",
    f"{forecast['yhat'].iloc[-1]:,.0f}"
)

# Historical Sales
st.subheader("📊 Monthly Sales Trend")

fig1 = px.line(
    df,
    x="ds",
    y="y",
    title="Historical Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# Forecast Chart
st.subheader("🔮 Future Sales Forecast")

fig2 = px.line(
    forecast,
    x="ds",
    y="yhat",
    title="Predicted Sales"
)

st.plotly_chart(fig2, use_container_width=True)

# Forecast Table
st.subheader("📋 Forecast Data")

forecast_table = forecast[["ds", "yhat"]].tail(12)

st.dataframe(forecast_table)

# Download Forecast
csv = forecast_table.to_csv(index=False)

st.download_button(
    label="⬇ Download Forecast CSV",
    data=csv,
    file_name="sales_forecast.csv",
    mime="text/csv"
)