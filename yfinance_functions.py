import yfinance as yf
import pandas as pd

ticker = 'SPY'
security = yf.Ticker(ticker)
hist = security.history(period="10d")

# A method to create a dataframe with stock data given a data range
data = yf.download("SPY", start="2022-01-01", end="2022-01-08")


# Creates a new column in the data using the two existing columns Open and Close
data['S1 Return'] = data['Close']/data['Open']

print(data)