#! ~/bin/python3

#Automaticaly run bash from Python script
#Author Nicolas Flandrois - Sun 09 Dec 2018 04:26:44 PM CET 

#Copy this script in your file system in which you wish to use as a repository. This script use Bash command, and assume your system uses Bash (e.g. Linux).
#Add or remove bash command lines you actally need, and sleep lap time
#Run this program preceeded by "bg" command line, in bash/Linux terminal. To show what job is in Background run "bg job". to stop background jobs "bg stop".

import os
import time

print ("hello world")

# NAME = input("GitHub user name : ")
# PWD = input("Passphrase : ")
#This is no use as long as I don't find a way to use it

os.system("clear")

while True:
	for i in range(4):
		os.system ("git commit -a -m 'Auto Commit'")
		time.sleep(3)
		#time express in seconds (20min = 1200sec)
		#For testing this time.sleep is set to 3sec

	print("Now your commits will be push to GitHub")
	os.system("git push origin master")
	time.sleep(10)
	print("Your files, and commits has been uploaded and saved to your GitHub")



#Command lines reminder:
# "git init" initiate a git index in the folder you choose
# "git add <Name of file>" adds the designated file to your index, within existing git repo
# "git add -A" adds all folders and files to your index, BUT even remove from index objects that has been removed
# "git add --no-all" adds all files and folders to your index, BUT ignore if any was removed (will not erase from index files removed"
# "git commit -a -m <message>" create a commit, add info from indexed files, and add a message to the commit.
# "git push origin master" push all git info to GitHub (or remote) repository
# "git log" show log history of this repo
