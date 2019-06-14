 #Barchart Practice
import csv
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd

plt.xkcd()

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
	language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

# plt.ylabel('Programming languages')
plt.xlabel('Number of people who Use')
plt.title('Most Popular languages')

plt.tight_layout()

plt.savefig('matplot2-bar1.png')
