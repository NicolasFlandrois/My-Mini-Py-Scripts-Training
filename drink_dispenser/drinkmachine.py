#! usr/bin/python3
# Start coding exercice: Thu 27 Dec 2018 10:39:02 AM CET 
# End date v1:
# Author: Nicolas Flandrois

# Description: 
# We consider a drink dispenser, prices are integer, and the machine keeps change only in coins of 2€, 5€, 10€, in a finit amount. 
# When the user (player) chooses a drink, the machine asks the player to pay the drink's price. The player can input any amount of money, >0€ & int().
# Then the machine will determine the change to return to the player, within its account of finit amount of coins of 2€, 5€, and 10€.
# It will first give change for biggest coin value, within available balance account for this coin value.
# If it cannot, then it will give change for Second biggest value, within available balance account for this coin value.
# If it cannot, then it will give change for third (last) biggest value, within available balance account for this coin value.
# If it couldn't give remaining change, then return NONE. The machine keep the remaining change.
# The machine can give change with any or all coin value, to give the closest change to real.
#
# In addition, the machine will keep track of all sales - Balance Account:
#   - Total Sales in value = sum of all prices sold.
#   - Total of sales = the number of sales in general, counting the number of loops the player have been playing.
#   - The detail of merchandise/drinks sold = individual count of each drinks sold
#   - The change coins balance, in details per coins value (Coin value, number of remaining coins, total € value for this coin value), and a global value amount (in €) of change coins
#   - The total Money in the machine (Total Sales + Global value amount€ of change coins)
# 
# Optional features:
#   - At begining of launching script, ask what drinks and prices has to be set. Inclued them in a dictionary.
#   - At begining of launching script, ask how many coins are in the machine, for each coin value... the initial "fond de caisse".
#   - Give the balace Account, when interupting any loop with [ except keyInterrupt: ] command.
