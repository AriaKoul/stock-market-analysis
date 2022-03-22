import pytest 
from datetime import datetime

from buyopen_sellclose import buyopen_sellclose
from buyclose_sellopen import buyclose_sellopen
from buy_and_hold import buy_and_hold
from fill_in_weekends import fill_in_weekends

ticker = 'SPY'
start_date = '2020-01-01'
end_date = '2020-02-01'
starting_amount = 10000


def test_buy_and_hold():
    # Check that the output is a dictionary
    assert isinstance(buy_and_hold(ticker, start_date, end_date, starting_amount), dict)
    # Check that this is the correct value for the specified date
    assert buy_and_hold('SPY', '2020-01-01', '2020-02-01', 10000).get('2020-01-31') == 9903.34
    # Check that each date is within the date range
    for day in list(buy_and_hold(ticker, start_date, end_date, starting_amount).keys()):
        assert datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime(day, '%Y-%m-%d') <= datetime.strptime(end_date, '%Y-%m-%d')
    
def test_buyopen_sellclose():
    assert isinstance(buyopen_sellclose(ticker, start_date, end_date, starting_amount), dict)
    assert buyopen_sellclose('SPY', '2020-01-01', '2020-02-01', 10000).get('2020-01-31') == 10163.62
    for day in list(buyopen_sellclose(ticker, start_date, end_date, starting_amount).keys()):
        assert datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime(day, '%Y-%m-%d') <= datetime.strptime(end_date, '%Y-%m-%d')


def test_buyclose_sellopen():
    assert isinstance(buyclose_sellopen(ticker, start_date, end_date, starting_amount), dict)
    assert buyclose_sellopen('SPY', '2020-01-01', '2020-02-01', 10000).get('2020-01-31') == 9783.98
    for day in list(buyclose_sellopen(ticker, start_date, end_date, starting_amount).keys()):
        assert datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime(day, '%Y-%m-%d') <= datetime.strptime(end_date, '%Y-%m-%d')

# Test that fill_in_weekends returns a_dict with all the dates filled in 
a_dict = {'2021-12-27':100, '2021-12-29':200, '2021-12-30':150, '2022-01-02':175}
def test_fill_in_weekends():
    correct_dict = {'2021-12-27':100, '2021-12-28':100, '2021-12-29':200, '2021-12-30':150, '2021-12-31':150, '2022-01-01':150, '2022-01-02':175}
    assert isinstance(fill_in_weekends(a_dict), dict)
    assert fill_in_weekends(a_dict) == correct_dict

test_buy_and_hold()
test_buyopen_sellclose()
test_buyclose_sellopen()
test_fill_in_weekends()