#! usr/bin/python3
# Start coding exercice: Thu 27 Dec 2018 10:39:02 AM CET
# Author: Nicolas Flandrois
# Last modified: Fri 15 January 2021 23:34:51 CET
# Last modified by: Nicolas Flandrois
# Version: v2

# Description:
# We consider a drink dispenser, prices are integer, and the machine keeps
# change only in coins of 2€, 5€, 10€, in a finit amount.
# When the user (player) chooses a drink, the machine asks the player to pay
# the drink's price. The player can input any amount of money,
# >0€ & int() & >drink_price_€.
# Then the machine will determine the change to return to the player, within
# its account of finit amount of coins of 2€, 5€, and 10€.
# It will first give change for biggest coin value, within available balance
# account for this coin value.
# If it cannot, then it will give change for Second biggest value, within
# available balance account for this coin value.
# If it cannot, then it will give change for third (last) biggest value,
# within available balance account for this coin value.
# If it couldn't give remaining change, then return NONE. The machine keep the
# remaining change.
# The machine can give change with any or all coin value, to give the closest
# change to real.
#
# In addition, the machine will keep track of all sales - Balance Account:
#   - Total Sales in value = sum of all prices sold.
#   - Total of sales = the number of sales in general, counting the number of
# loops the player have been playing.
#   - The detail of merchandise/drinks sold = individual count of each drinks
# sold
#   - The change coins balance, in details per coins value (Coin value, number
# of remaining coins, total € value for this coin value), and a global value
# amount (in €) of change coins
#   - The total Money in the machine (Total Sales + Global value amount€ of
# change coins)
#
# Optional features:
#   - At begining of launching script, ask what drinks and prices has to be
# set. Inclued them in a dictionary.
#   - At begining of launching script, ask how many coins are in the machine,
# for each coin value... the initial "fond de caisse".
#   - Give the balace Account, when interupting any loop with
# [ except keyInterrupt: ] command.
#   - Establish an email alert. Down to a certain level of change coins
# amount(nb), send an email to dispenser Owner.
#            - As soon as 1 coin ammount(nb) = 0 (or 1 coin)
#            - Send email:
#                    - To: owner
#                    - Object: "No more change, please refill me"
#                    - Gives Machine ID number
#                    - Which coin value raised the alert?
#                    - Gives a summary of Balance account
#    - Make a balance account for number of drinks, which at every sale,
# it substract 1. If = 0 then print message
# "Out of this drink. Victim of its success."

# ===========================================================================
# Infinite amount in Dispenser's balance at disposal


def change(cash):
    '''Give back change with infinite money at disposal'''
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
    except Exception as e:
        return None, e


print(change(1))  # None

res = change(42)
print(res['two'])  # 1
print(res['five'])  # 0
print(res['ten'])  # 4


# ===========================================================================
# Finite amount in Dispenser's balance at disposal


def check_change(val: int, return_money: int, balance: int):
    """
    This function will check in the balance sheet (Balance),
    how many coins is available, for a specific coin value,
    to correspond to the money return.
    """
    if return_money >= val:
        money = return_money // val
        if money < balance:
            return_money = return_money % val
            balance -= money
        else:
            money = balance
            return_money -= money * val
            balance -= money
    else:
        money = 0

    return money, return_money, balance


def drink_disp(amount: int, price: int,
               balance_2: int, balance_5: int, balance_10: int):
    """
    Dispenser computing :
        - cash input, price, finite balance of money at disposal.
        - It will return the details of money returned,
        and a balance of remaining cash
    """
    balance = {'two': balance_2, 'five': balance_5, 'ten': balance_10}
    return_money = amount - price

    if amount < price or return_money < 2:
        return None, balance

    else:
        tmp_ten = check_change(10, return_money, balance['ten'])
        tens = tmp_ten[0]
        return_money = tmp_ten[1]
        balance["ten"] = tmp_ten[2]

        tmp_five = check_change(5, return_money, balance['five'])
        fives = tmp_five[0]
        return_money = tmp_five[1]
        balance["five"] = tmp_five[2]

        tmp_two = check_change(2, return_money, balance['two'])
        twos = tmp_two[0]
        return_money = tmp_two[1]
        balance["two"] = tmp_two[2]

        return f'Dispenser will return :\n{tens} x 10€\n{fives} x 5€\n{twos} \
x 2€', balance


print("Test 1")
disp = {'two': 10, 'five': 10, 'ten': 10}
player = 80
price = 5

result = drink_disp(player, price, disp['two'], disp['five'], disp['ten'])

print(result[0])
print(result[1])

print('Test 2')

result = drink_disp(87, 1, 20, 0, 0)

print(result[0])
print(result[1])

print('Test 3')

result = drink_disp(87, 1, 10, 10, 10)

print(result[0])
print(result[1])
