# Stock Market Analysis 
## Background
There are many articles in the financial press about how the stock market tends to rise overnight instead of during trading hours. Some of these articles are below:

[New York Times](https://www.nytimes.com/2018/02/02/your-money/stock-market-after-hours-trading.html)

[Financial Times](https://www.ft.com/content/1cc17824-3077-4e39-9a99-cbccc83a2251)

[Bloomberg](https://www.bloomberg.com/news/articles/2020-09-17/volatility-bout-puts-outsize-overnight-stock-moves-in-focus)

Below is a quote from the New York Times article:

>Separate the daytime and the after-hour returns and calculate them cumulatively, as Bespoke has done, and it turns out that **all of that price gain since 1993 has come outside regular trading hours**.
If you had bought the SPY at the last second of trading on each business day since 1993 and sold at the market open the next day — capturing all of the net after-hour gains — your cumulative price gain would be 571 percent.
On the other hand, if you had done the reverse, buying the E.T.F. at the first second of regular trading every morning at 9:30 a.m. and selling at the 4 p.m. close, you would be down 4.4 percent since 1993.

![This is an image from the New York Times article](https://i.imgur.com/5jIfi80.png)

This finding is counterintuitive, and I set out to validate this conclusion.

## How to Use
Clone this repository using the following code:

`$ git clone https://github.com/AriaKoul/stock-market-analysis`

Specify the ticker, start date, end date, and the portfolio starting amount in the file named `create_plot.py`

For example: 

`ticker = 'SPY'`

`start_date = '2021-01-01'`

`end_date = '2022-01-01'`

`starting_amount = 10000`

Run `python create_plot.py`. This will generate a plot using `matplotlib` and display it on the screen.

![Example Graph](https://i.imgur.com/cFlZNO2.png)


## Dependencies
To execute this code, you will need Python3, and the following Python modules: yfinance, matplotlib, datetime, pandas, and numpy. 

To install Python, visit [the Python website] (https://www.python.org/downloads/).

To install these modules, use the following commands:

`$ pip install yfinance matplotlib datetime pandas numpy`

## Description
`buyopen_sellclose.py`

`buyclose_sellopen.py`

`buy_and_hold.py`

`fill_in_weekends.py`

`x_axis_labels.py`

`plotter.py`

`create_plot.py`

## Conclusions
