 #MATPLOTLIB Pie Chart Practice

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

plt.pie([1, 1, 1], labels=["Player 1", "Player 2", "Player 3"])

plt.title('Stack Plot Practice')
plt.tight_layout()
plt.savefig('matplot3-piechart.png')
