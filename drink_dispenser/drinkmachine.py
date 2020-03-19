#! usr/bin/python3
# Start coding exercice: Thu 27 Dec 2018 10:39:02 AM CET
# End date v1:
# Author: Nicolas Flandrois

# Description:
# We consider a drink dispenser, prices are integer, and the machine keeps change only in coins of 2€, 5€, 10€, in a finit amount.
# When the user (player) chooses a drink, the machine asks the player to pay the drink's price. The player can input any amount of money, >0€ & int() & >drink_price_€.
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
#   - Establish an email alert. Down to a certain level of change coins amount(nb), send an email to dispenser Owner.
#            - As soon as 1 coin ammount(nb) = 0 (or 1 coin)
#            - Send email:
#                    - To: owner
#                    - Object: "No more change, please refill me"
#                    - Gives Machine ID number
#                    - Which coin value raised the alert?
#                    - Gives a summary of Balance account
#    - Make a balance account for number of drinks, which at every sale, it substract 1. If = 0 then print message "Out of this drink. Victim of its success."

def change(cash):
    # Your code goes here
    try:
        if cash < 2:
            return None
        else:
            ten = cash // 10
            cash = cash % 10
            five = cash // 5
            cash = cash % 5
            two = cash // 2
            res = cash % 2
        return {
            'two': two,
            'five': five,
            'ten': ten
        }
    except:
        return None


print(change(1))  # None

res = change(42)
print(res['two'])  # 1
print(res['five'])  # 0
print(res['ten'])  # 4
