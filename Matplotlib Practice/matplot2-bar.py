 #Barchart Practice
import csv
from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	row = next(csv_reader)
	print(row['LanguagesWorkedWith'].split(';'))

# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
# plt.title('Median Salary (USD) by Age')
# plt.tight_layout()

# plt.savefig('matplot2-bar1.png')
