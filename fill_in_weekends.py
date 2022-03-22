import datetime


format = '%Y-%m-%d'

# This is broken, the dates are not in order and for example, the date range from 
def fill_in_weekends(raw_dict):
    """
    This function takes a dictionary of dates and portfolio values as an input
    and adds missing days and their corresponding portfolio values up to three days 
    forward. This accounts for weekends, long weekends, and holidays in the US Market
    but not market closures longer than three days. 
    A better way to account for longer gaps is to see when a day is missing, check for the 
    next day that exists and create a list of all days in between and key-value pairs for 
    all the missing days. 
    """
    # Create the empty dictionary
    completed_dict = dict()
    # Get the last day of the already created dictionary
    last_day = list(raw_dict.keys())[-1]
    # Iterate over the raw dictionary and add the values for the days that aren't included 
    for day in raw_dict:
        # Break out of the for loop when reaching the last day in order to not extend beyond the time range
        if day == last_day:
            completed_dict[day] = raw_dict.get(day)
            break
        # Check if the next day exists in the dictionary
        day_datetime = datetime.datetime.strptime(day, format)
        d_plus_1_datetime = day_datetime + datetime.timedelta(days=1)
        d_plus_2_datetime = day_datetime + datetime.timedelta(days=2)
        d_plus_3_datetime = day_datetime + datetime.timedelta(days=3)
        d_plus_1 = str(d_plus_1_datetime).split(' ')[0]
        d_plus_2 = str(d_plus_2_datetime).split(' ')[0]
        d_plus_3 = str(d_plus_3_datetime).split(' ')[0]

        if raw_dict.get(day):
            completed_dict[day] = raw_dict.get(day)

        if raw_dict.get(d_plus_1) is None:
            completed_dict[d_plus_1] = raw_dict.get(day)
        if raw_dict.get(d_plus_2) is None:
            completed_dict[d_plus_2] = raw_dict.get(day)
        if raw_dict.get(d_plus_3) is None:
            completed_dict[d_plus_3] = raw_dict.get(day)
        
    return completed_dict

a_dict = {'2021-12-27':100, '2021-12-29':200, '2021-12-30':150, '2022-01-02':175}
b_dict = {'2022-03-03':100, '2022-03-18':200}
def test_fill_in_weekends():
    a_correct_dict = {'2021-12-27':100, '2021-12-28':100, '2021-12-29':200, '2021-12-30':150, '2021-12-31':150, '2022-01-01':150, '2022-01-02':175}
    assert isinstance(fill_in_weekends(a_dict), dict)
    assert fill_in_weekends(a_dict) == a_correct_dict

    b_correct_dict = {'2022-03-03':1}

print(fill_in_weekends(a_dict))
