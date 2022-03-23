import matplotlib.pyplot as plt
import time
import numpy as np
import datetime

start_time = time.time()
# Import functions from the other files
from buyopen_sellclose import buyopen_sellclose
from buyclose_sellopen import buyclose_sellopen
from buy_and_hold import buy_and_hold
from x_axis_labels import generate_x_axis_labels

ticker = 'SPY'
start_date = '2021-03-03'
end_date = '2022-03-18'
starting_amount = 10000

# Set the imported functions equal to variables
s1 = buyopen_sellclose(ticker, start_date, end_date, starting_amount)
s2 = buyclose_sellopen(ticker, start_date, end_date, starting_amount)
s3 = buy_and_hold(ticker, start_date, end_date, starting_amount)

# Plot the data and adjusting the characteristics of the plot
fig, ax = plt.subplots()
plt.plot(s1.keys(), s1.values())
plt.plot(s2.keys(), s2.values())
plt.plot(s3.keys(), s3.values())
plt.legend(['Day', 'Night', 'Hold'])
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.xticks(rotation = 30, fontsize = 8)
plt.yticks(fontsize=8)
ax.set_xticks(generate_x_axis_labels(s1))
plt.show()

end_time = time.time()
print(f"Executed in {round(end_time - start_time, 2)} seconds")