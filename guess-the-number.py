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
time.sleep(3)
print("You have to guess an integer number, between 1 and 100, within 7 guess.")
time.sleep(5)

clean()

#While True: #how to make it work
x = random.randrange(1,101,2)
#print(x) #Only for testing
time.sleep(5)
clean()
	
for i in range(7):
#	print("remaining " i "guess.") #add a remaining guess counter here
	y = int(input("Guess? "))
	if y > x:
		print("You guessed too high!")
		time.sleep(5)
		clean()
	elif y < x:
		print("You guessed too low!")
		time.sleep(5)
		clean()
	else:
		print("You win!!!")
		break
#Still to do:
#Offer a choice to start a new game or quit
#verify if input is: Interger + a positive number + within range [1;100]
