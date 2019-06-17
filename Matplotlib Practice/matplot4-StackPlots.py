 #MATPLOTLIB Stack Plots Practice

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ["Player 1", "Player 2", "Player 3"]
colors = ["#6d904f", "#fc4f30", "#008fd5"]

plt.stackplot(minutes, player1, player2, player3, labels=labels,
	colors=colors)
# A stack plot will stack each value for each 'players', on top of each other
# as a compound display, over time.

plt.legend(loc="lower left")

plt.title('Stack Plot Practice')
plt.tight_layout()
plt.savefig('matplot4-Stackplot.png')
