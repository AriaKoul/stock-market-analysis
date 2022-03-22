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
    # Increment types: daily, weekly, monthly, quarterly, yearly
    # If date range is 10 days or less, give every day

    # If date range is 


    return x_axis_labels

