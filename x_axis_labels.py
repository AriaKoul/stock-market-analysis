import datetime

def generate_x_axis_labels(a_dict):
    """
    To get daily x-axis labels, use every key in the dictionary as a label.
    To get weekly x-axis labels, use datetime.weekday() to find each Monday and use each 
    Monday as the label.
    To get monthly x-axis labels, if the last two characters in the day are '01' then use it as a label.
    To get quarterly x-axis labels, use the first day and use datetime relativedata function to get the 
    next quarter using months = 3. 
    To get yearly x-axis labels, use the first day and use datetime relativedata function to get the next
    year using months = 12.
    """
    x_axis_labels = []
    format = '%Y-%m-%d'
    days = list(a_dict.keys())
    num_days = len(days)
    print(num_days)

    # This displays labels for every day
    if num_days < 10:
        for day in days:
            x_axis_labels.append(day)

    # This displays labels for every other day 
    if num_days > 9 and num_days < 15:
        counter = 0
        for day in days:
            if counter % 2 == 0:
                x_axis_labels.append(day)
            counter += 1

    # This displays labels for every three days
    if num_days > 14 and num_days < 29:
        counter = 0
        for day in days:
            if counter % 3 == 0:
                x_axis_labels.append(day)
            counter += 1

    # This displays labels for the Monday of every week
    if num_days > 28 and num_days < 61:
        for day in days:
            day_of_week = datetime.datetime.strptime(day, format).weekday()
            if day_of_week % 2 == 0:
                x_axis_labels.append(day)

    # This displays labels for the Monday of every other week 
    if num_days > 60 and num_days < 151:
        counter = 0
        for day in days:
            day_of_week = datetime.datetime.strptime(day, format).weekday()
            if day_of_week == 0:
                if counter % 2 == 0:
                    x_axis_labels.append(day)
                counter += 1

    # This displays labels for the first of every month
    if num_days > 150 and num_days < 251:
        for day in days:
            if day[-2:] == '01':
                x_axis_labels.append(day)
            
    # This displays labels for the first of every other month
    if num_days > 250 and num_days < 500:
        counter = 0
        for day in days:
            if day[-2:] == '01':
                if counter % 2 == 0:
                    x_axis_labels.append(day)
                counter += 1

    # This displays labels for the first of every third month
    if num_days > 499 and num_days < 900:
        counter = 0
        for day in days:
            if day[-2:] == '01':
                if counter % 3 == 0:
                    x_axis_labels.append(day)
                counter += 1

    # This displays labels for the first of every sixth month
    if num_days > 899 and num_days < 1800:
        counter = 0
        for day in days:
            if day[-2:] == '01':
                if counter % 6 == 0:
                    x_axis_labels.append(day)
                counter += 1
    
    # This displays labels for the first new month and every year after that
    if num_days > 1799 and num_days < 3700:
        counter = 0
        for day in days:
            if day[-2:] == '01':
                if counter % 12 == 0:
                    x_axis_labels.append(day)
                counter += 1
    
    # This displays labels for the first new month and every two years after that
    if num_days > 3699:
        counter = 0
        for day in days:
            if day[-2:] == '01':
                if counter % 24 == 0:
                    x_axis_labels.append(day)
                counter += 1

    return x_axis_labels

def generate_evenly_spaced_x_axis_labels(a_dict):
    """
    alternative method of generating x axis labels
    """
    # The below line is where I set the range of number of acceptable labels
    label_options = range(6,11)
    days = list(a_dict.keys())
    num_days = len(days)
    x_axis_labels = []
    
    label_dict = dict()
    for i in label_options:
        remainder = num_days % i
        label_dict[remainder] = i

    num_labels = label_dict.get(min(list(label_dict.keys())))
    counter = 0
    for i in range(num_days):
        counter += 1
        if counter % (num_days // num_labels) == 0:
            x_axis_labels.append(days[i])

    print(f'{num_days} entries in list')
    print(f'Intended number of labels is {num_labels}')
    print(f'Actual number of labels is {len(x_axis_labels)}')
    return x_axis_labels