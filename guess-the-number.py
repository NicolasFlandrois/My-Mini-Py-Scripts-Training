#! usr/bin/python3

#Wed 19 Dec 2018 04:22:18 PM CET 
#Author: Nicolas Flandrois

import random
import os
import platform
import time

def clean():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

print("Welcome to 'Guess the Number' game!")
time.sleep(1)
print("You have to guess an integer number, between 1 and 100, within 7 guess.")
time.sleep(3)

clean()

loop = 0
win = 0
def score():
    print('Your score is ' + str(win) + '/' + str(loop))

def trial():
    print('remaining ' + str(trials) + ' trials.')

while True:
    trials=int(7)
    x = random.randrange(1,101,2)
    loop += 1
    r=range(1,101)

    for i in range(7):
        trials -= 1
        y = int(input("Guess the number? "))

#        if except ValueError:
#            return ("Oops!  That was no valid number.  Try again...")
#            pass
#        elif:  
#            y in r
#                if False
#                    return("Oops!  That was no valid number. Reminder choose a number between 1 and 100. Try again...")
#                else:
#                    continue
#        finally:
#            pass

        if y > x:
            print("You guessed too high!")
            trial()
            time.sleep(3)
            clean()
        elif y < x:
            print("You guessed too low!")
            trial()
            time.sleep(3)
            clean()
        elif y == x:
            print("You won!!!")
            win += 1
            time.sleep(1)
            score()
            time.sleep(5)
            clean()
            break

    if y != x:
        print("You lost!")
        time.sleep(1)
        score()
    else:
        continue
    
    time.sleep(5)
    clean()

#Still to do:
#Offer a choice to start a new game or quit
#verify if input is: Interger + a positive number + within range [1;100]
#use error value >> if ErrorValue: print("we said a number, WTF!") then continue or pass
