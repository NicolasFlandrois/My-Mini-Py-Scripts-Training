 #Barchart Practice
import csv
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

plt.xkcd()

with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	language_counter = Counter()
	
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

plt.barh(languages, popularity)

plt.xlabel('Number of people who Use')
plt.title('Most Popular languages')

plt.tight_layout()

plt.savefig('matplot2-bar1.png')
