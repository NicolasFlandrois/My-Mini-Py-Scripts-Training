 #MATPLOTLIB Pie Chart Practice

from matplotlib import pyplot as plt


plt.xkcd()

slices = [60, 40]

plt.pie(slices)

plt.title('Awsome Pie Chart')
plt.tight_layout()
plt.savefig('matplot3-piechart1.png')

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# 