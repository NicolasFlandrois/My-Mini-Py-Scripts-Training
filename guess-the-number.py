#! usr/bin/python3

#Wed 19 Dec 2018 04:22:18 PM CET 
#Author: Nicolas Flandrois
#Description: The playuer have to guess a randomly defined whole number, between [1 and 100], within 7 guesses.

import random
import os
import platform
import time
import sys

def clean():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")

print("Welcome to 'Guess the Number' game!")
time.sleep(1)
print("""You have to guess a randomly defined whole number, 
between 1 and 100, 
within 7 guesses.""")
time.sleep(5)

clean()

loop = 0
win = 0
def score():
    print('Your score is ' + str(win) + '/' + str(loop))

def dubai():
    print('remaining ' + str(trials) + ' trials.')
    time.sleep(3)
    clean()
#named it "dubai", because why not! came short of a code name for this function.

while True:
    trials=int(7)
    x = random.randrange(1,101,2)
    loop += 1
    r=range(1,101)

    for i in range(7):
        trials -= 1

        try:
            y = int(input("Guess the number? "))

#Verification if input number is valid
        except:
            print("Oops! ",sys.exc_info()[0]," occured. That was no valid number.  Try again...")
            time.sleep(1)
            dubai()
            continue

        if y not in r:
            print("""Oops!  That was no valid number. 
REMINDER: choose a number between 1 and 100. 
Try again...""")
            dubai()
#Test if player win or loose
        elif y > x:
            print("You guessed too high!")
            dubai()
        elif y < x:
            print("You guessed too low!")
            dubai()
        elif y == x:
            print("You won!!!")
            win += 1
            time.sleep(1)
            score()
            time.sleep(2)
            break

#If after 7 guesses player didn't guess correctly, let's inform him he lost! Or if he won and break the loop, let's continue.
    if y != x:
        print("You lost!")
        time.sleep(1)
        score()

#Start a new game (continue infinite While True loop) or Quit loop?
    time.sleep(1)
    answer = input("Do you want to play again? Y/N ").strip().lower()
    if answer in ("no","n","q","quit"):
        time.sleep(1)
        clean()
        print("Good bye! Thank you for playing.")
        break
    
    time.sleep(1)
    clean()
