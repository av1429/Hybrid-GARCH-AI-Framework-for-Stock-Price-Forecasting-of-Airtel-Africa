#1776 days with holidays and weekends

import yfinance as yf
import pandas as pd

# Download Airtel Africa stock data (London Stock Exchange ticker: AAF.L)
data = yf.download("AAF.L", start="2019-06-28", end="2024-05-08")

# Create full daily date range
full_range = pd.date_range(start="2019-06-28", end="2024-05-08", freq="D")

# Reindex data to daily frequency (missing days will show NaN)
data = data.reindex(full_range)

print(data.head(10))
print(data.tail(10))

# Save to CSV
data.to_csv("airtel_africa_daily.csv")

#1226 days without holidays and weekends: only trading days

import yfinance as yf

# Download Airtel Africa stock data (London Stock Exchange ticker: AAF.L)
data = yf.download("AAF.L", start="2019-06-28", end="2024-05-08")

print(data.head())
print(data.tail())

# Save to CSV
data.to_csv("airtel_africa.csv")
