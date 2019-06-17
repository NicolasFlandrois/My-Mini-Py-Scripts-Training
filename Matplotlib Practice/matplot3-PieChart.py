 #MATPLOTLIB Pie Chart Practice

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524,
18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java',
'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):',
'Ruby', 'Go', 'Assembly']

# Too many data, for a usable Pie Chart, that actually means something...
# Use Pie Charts with max 5 data items, for more visual effects.

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'})

plt.title('Programming language popularity')
plt.tight_layout()
plt.savefig('matplot3-piechart1.png')

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
