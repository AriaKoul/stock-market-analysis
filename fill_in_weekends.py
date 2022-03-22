import datetime

format = '%Y-%m-%d'

def create_next_day(date):
    current_day_datetime = datetime.datetime.strptime(date, format)
    next_day_datetime = current_day_datetime + datetime.timedelta(days=1)
    next_day_str = str(next_day_datetime).split(' ')[0]
    return next_day_str

def fill_in_weekends(raw_dict):
    """
    This function takes a dictionary of dates and portfolio values as an input
    and adds missing days and their corresponding portfolio values to the dictionary.  
    """
    # Create the empty dictionary
    completed_dict = dict()

    # Check if the next day exists in the dictionary
    dates = list(raw_dict.keys())
    for i in range(len(dates)):
        missing_dates = []
        if i == len(dates) - 1:
            completed_dict[dates[i]] = raw_dict.get(dates[i])
            break
        completed_dict[dates[i]] = raw_dict.get(dates[i])
        # Check if the following key is the next day 
        # If the following key is the following day, do nothing and continue in the loop 
        if dates[i+1] == create_next_day(dates[i]):
            pass
        else:
        # If the following key is not the next day, generate a list of all the missing days in between 
            missing_dates = [create_next_day(dates[i])]
            while missing_dates[-1] != dates[i+1]:
                missing_dates.append(create_next_day(missing_dates[-1]))
            missing_dates.pop()
        if missing_dates:
            for missing_day in missing_dates:
                completed_dict[missing_day] = raw_dict.get(dates[i])

    return completed_dict