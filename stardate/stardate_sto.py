#! usr/bin/python3

#################################################################################
# MIT License
#
# Copyright (c) 2019 - Nicolas Flandrois
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

#Thu 10 Jan 2019 12:42:24 PM CET - Stradate 96627.31 (STO)
#Author: Nicolas Flandrois
#Description: This program intend to compute Stardate, 
#according to current time defined by the computer, 
#it is using customized reference points for calculation:
# stardate = c + [1000*(y-b)] + [(1000/(n*1440))*((iso_day_of_year - 1)+time_in_minutes)]
# Comment: This isn't the prettiest way to compute all that, nor python zen. But it works
#Version: v1 (the messy version)

import datetime

d = datetime.datetime.now()
earthdate = d.timetuple()

ed_display = d.strftime('%A, %Y %B %d. %H:%M:%S')
print('Earthdate : ', ed_display)

#The following reference points are from 
#the MMORPG Star Trek Online (STO). 
#This STO referncial was determined from their online converter:
# 2019/01/01 00:00 = 96601.20 stardate units
#https://www.stoacdemy.com/tools/stardate.php
#STO online converter uses differnt round parameters, 
#and I discovered they don't take leap year into account. 
#They apply n = 365, even during a leap year of 366 days.
b = 2019
c = 96601.20
#Referents point variables can be customized. 
#Please refer to the reference dates document.

n = 1

def leapyr(year):
	"""" 
	This function defines if the year is 
	a Leap year (366 days) 
	or a Normal year (365 days).
	Then it will apply to variable n the value of 366 or 365, accordingly.
	"""
	global n
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		n = 366
		print("The year is a Leap year.")

	else:
		n = 365
		print("The year is a normal year.")

leapyr(earthdate.tm_year)

#Here we convert the current Year into a Stardate.
sd_yeardelta = earthdate.tm_year-b
sd_yearunit = 1000*sd_yeardelta
sd_year = c+sd_yearunit

#Here we convert the current iso-day_of_year 
#and time (hh:mm), into Stardate
ed_min = ((earthdate.tm_yday-1.0)*1440.0)+(earthdate.tm_hour*60.0)+earthdate.tm_min
sd_timeunit = 1000/(n*1440.00)
sd_min = sd_timeunit*ed_min

#Here we add up the Year Stardate, and Time Stardate, 
#to get a full STARDATE
stardate = sd_year+sd_min
print("")
print("Stardate : ", format(stardate, '.2f'))
