import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# Ref Colormap : https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
# Ref Marker Styles: 
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, edgecolor='black', linewidth=1, alpha=0.75)

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.savefig('matplot7-ScatterPlot.png')
