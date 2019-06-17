 #MATPLOTLIB Pie Chart Practice

from matplotlib import pyplot as plt


plt.xkcd()

slices = [120, 80, 30, 20]
labels = ['Not-sixty', 'Not-fourty', 'Extra1', 'Extra2']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, colors=colors, 
	wedgeprops={'edgecolor':'black'})

plt.title('Awsome Pie Chart')
plt.tight_layout()
plt.savefig('matplot3-piechart1.png')

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
