#!/usr/bin/python3
#Date: Friday, April 3rd, 2019
#Python Exercice
#Source & credits: https://www.youtube.com/watch?v=ve2pmm5JqmI&list=WL&index=2
#Description:
#This exercice aim to automate parsing and renaming multiple files in a 
#specific directory. 
#Path to the directory needs to be changed/updated to your project.
#The video exemple (cf source) uses a directory of multiple video files
#with the original naming as "Earth - Our Solar System - #4.mp4"
#("f_title - f_course - f_num f_ext") This stripping needs to be 
#customed/changed to fit your project.

import os

#Define path (change or update said path according to project)
os.chdir('/home/User/Pictures')

#Renaming process
for f in os.listdir():
	#Reminder initial exemple's format: "f_title - f_course - f_num f_ext"
	#Formating to adapt according to project.
	f_name, f_ext = os.path.splitext(f) #Split name & ext from 2 Tuple into var
	f_title, f_course, f_num = f_name.split('-') #split parts while remove "-"
	f_title = f_title.strip() #striping any blank/white spaces unused
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zfill(2) 
	#strip blanks + not consider 1st character "#" + fill 0 to get 2 dec digits
	new_name = '{}-{}{}'.format(f_num, f_title, f_ext) #formating nem naming
	os.rename(f, new_name) #applying new name to each enumerated/listed file.