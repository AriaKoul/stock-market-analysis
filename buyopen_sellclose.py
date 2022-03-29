import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt 
from fill_in_weekends import fill_in_weekends 

def buyopen_sellclose(ticker, start_date, end_date, starting_amount):
    """
    This function takes a ticker, a start date, an end date, a starting amount, and if the user
    wants to plot the output or not. The output of this function is a graph with the x-axis representing
    the period specified by the user and the y-axis representing how much the portfolio value changes 
    over the specified time period. Note that the dates and the portfolio values are stored in a dictionary."""

    df = yf.download(ticker, start=start_date, end=end_date)
    # Saving to a csv and reading from it to generate the data frame because of the "Date" column issue (resulted in a Key Error)
    df.to_csv("data/sample_data.csv")
    df = pd.read_csv("data/sample_data.csv")
    df['S1 Return'] = df['Close']/df['Open']

    portfolio_values = dict() 
    portfolio_value = starting_amount

    for index, row in df.iterrows():
        portfolio_value = portfolio_value * row['S1 Return']
        portfolio_value = round(portfolio_value, 2)
        portfolio_values[row['Date']] = portfolio_value

    names = list(portfolio_values.keys())
    values = list(portfolio_values.values())

    return fill_in_weekends(portfolio_values)