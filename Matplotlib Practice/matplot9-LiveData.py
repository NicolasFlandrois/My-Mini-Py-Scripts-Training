import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

plt.plot(x_vals, y_vals)


# index = count()

# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))


plt.tight_layout()
plt.show()


# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']
#######################
# Snippet:
# Another way to do it without clearing the Axis

# def animate(i):
#     data = pd.read_csv('data.csv')
#     x = data['x_value']
#     y1 = data['total_1']
#     y2 = data['total_2']

#     line1.set_data(x, y1)
#     line2.set_data(x, y2)

#     ax = plt.gca()
#     xlim_low, xlim_high = ax.get_xlim()
#     ylim_low, ylim_high = ax.get_ylim()

#     ax.set_xlim(xlim_low, (x.max() + 5))

#     y1max = y1.max()
#     y2max = y2.max()
#     current_ymax = y1max if (y1max > y2max) else y2max

#     y1min = y1.min()
#     y2min = y2.min()
#     current_ymin = y1min if (y1min < y2min) else y2min

#     ax.set_ylim((current_ymin - 5), (current_ymax + 5))
