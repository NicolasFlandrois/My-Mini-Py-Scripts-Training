 #MATPLOTLIB Pie Chart Practice

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0] # Explode == Detach and expose a zone from chart.
# Explode is the percentage out radius to explose it to/from


plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90,
	wedgeprops={'edgecolor':'black'})

plt.title('Programming language popularity')
plt.tight_layout()
plt.savefig('matplot3-piechart.png')

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
