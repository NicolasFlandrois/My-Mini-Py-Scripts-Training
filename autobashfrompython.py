#! ~/bin/python3

#Automaticaly run bash from Python script
#Author Nicolas Flandrois - Sun 09 Dec 2018 04:26:44 PM CET 

#Add or remove what you actally need, and sleep lap time

#Run this program preceeding by "bg" command line, in bash/Linux terminal. To show what job is in Background run "bg job". to stop background jobs "bg stop".

import os
import time

print ("hello world")

# i = 1
# for i in range(3):      
#This function runs the program a certain amond of time in loop

while True:
#infinit loop
	#os.system ("git init") #This line will initialize the Git Repo
	#os.system ("git add autobashfrompython.py") #This line add itself to the repo
	os.system ("git commit -a -m 'Auto Commit'") #This line create a commit of itself, automatically
	time.sleep(10) #time express in seconds

print ("EOF")

#To improve this programe:
#Auto commit every 20min (1200 sec)
#Every loop of X repetition (say X = 3), send git to remote on GitHub
