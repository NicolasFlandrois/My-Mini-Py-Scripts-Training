#! usr/bin/python3
#Convert Stardate into Earthdate.

#Description: This program intend to convert a given Stardate, 
#into an Earthdate, using customized reference points for calculation:
# stardate = c + [1000*(y-b)] + [(1000/(n*1440))*((iso_day_of_year - 1)+time_in_minutes)]
import datetime

stardate = float(input("Stardate : "))

b = 2019
c = 96601.20
n = 1

def leapyr(year):
	"""" 
	This function defines if the year is 
	a Leap year (366 days) 
	or a Normal year (365 days).
	Then it will to the variable n the value of 366 or 365, accordingly.
	"""
	global n
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		n = 366
		print("The year is a Leap year.")

	else:
		n = 365
		print("The year is a normal year.")

ed_year = int(((stardate//1000) - (c//1000)) + b)
print("Year : ", ed_year)
leapyr(ed_year)

ed_time = ((stardate%1000)*n)/1000
print(ed_time)