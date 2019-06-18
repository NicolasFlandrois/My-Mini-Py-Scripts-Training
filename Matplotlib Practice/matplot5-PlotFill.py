 #MATPLOTLIB Filling area on line plots Practice

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
				 where=(py_salaries > dev_salaries),
				 interpolate=True, color='green', alpha=0.25)
				 # Fill When OVER the other plot in GREEN

plt.fill_between(ages, py_salaries, dev_salaries,
				 where=(py_salaries <= dev_salaries),
				 interpolate=True, color='red', alpha=0.25)
				 # Fill When Bellow the other plot in RED

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.savefig('matplot5-PlotFill.png')
