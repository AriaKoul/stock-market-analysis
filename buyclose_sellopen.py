import time
import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from fill_in_weekends import fill_in_weekends 

def buyclose_sellopen(ticker, start_date, end_date, starting_amount, plot=False):
    """
    This function takes a ticker, a start date, an end date, a starting amount, and if the user
    wants to plot the output or not. The output of this function is a graph with the x-axis representing
    the period specified by the user and the y-axis representing how much the portfolio value changes 
    over the specified time period. Note that the dates and the portfolio values are stored in a dictionary."""

    df = yf.download(ticker, start=start_date, end=end_date)
    # Saving to a csv and reading from it to generate the data frame because of the "Date" column issue (resulted in a Key Error)
    df.to_csv("data/sample_data.csv")
    df = pd.read_csv("data/sample_data.csv")

    # Creating the dictionary
    portfolio_values = dict()
    portfolio_value = starting_amount

    # Creating an empty column for S2 Return 
    df['S2 Return'] = ''
    
    # Iterating over the dataframe in order to fill out the 'S2 Return' column
    for index, row in df.iterrows(): 
        # if index == 0:
        if index > 0:
            df.iat[index, df.columns.get_loc('S2 Return')] = df.iloc[index]['Open'] / df.iloc[index-1]['Close'] 
            df = df.replace(r'^\s*$', 1, regex=True)
    
    # Converting the columns in the dataframe to a list 
    s2_return = df['S2 Return'].tolist()
    dates = df['Date'].tolist()

    # Iterating over the dates and generating the portfolio values for each date
    for i in range(len(dates)):
        portfolio_value = portfolio_value * s2_return[i]
        portfolio_value = round(portfolio_value, 2)
        portfolio_values[dates[i]] = portfolio_value

    names = list(portfolio_values.keys())
    values = list(portfolio_values.values())

    if plot:
        plt.plot(range(len(portfolio_values)), values) # plot does not include the dates but we need it to 
        plt.show()

    return fill_in_weekends(portfolio_values)
