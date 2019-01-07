#! usr/bin/python3
# Mon 07 Jan 2019 09:07:44 AM CET 
# Author: Nicolas Flandrois
# Description: This program will calculate Stardate (Star trek style), according to current time and date in computer, or on a specific date.

# Choose between Generate (G) a stardate from current datetime of computer automatically, OR Convert (C) according to a date and time input.
# User/Player input G or C, standardise input to avoid error (c == C and g == G, or reverse). If any other input, inform not valid input, give choice between Exit Programm or try again.

# Date Converter data set up:
#   Input Year
#   Input Month
#   Input Day
#   Input Hour (24h system)
#   Input Minutes
#   Or directly input date and time according to standardized YYYY/MM/DD hh:mm
#   Convert in a Python Standard
#   Verify all input as integer 
#   Save variables for calculation

# Date Generator data set up:
#   datetime module needs to be imported
#   At open determine current Date and Time (using datetime module) on computer, at launch
#   Standardize the datetime to fit needs of calculation
#   Save variables as integer

# Stardate calculation:
#   What's the arytmetic formula to convert Earth Date into (Star trek) Stardate?
#   Can we use ISO day?
#   Have to determine if Year is a leap year!? As it changes calculations

# Have a Note/Foot note reminder of both officials reference date points for calculattion 2005 = 58000.00 and 2323 = 000000.00

# Display Stadate output print Stardate

# REMINDER Variables and Arythmetic formula

# 1 Earth Year = 1000 Stardate units

# IF Leap Year:
#   n = 366 days (in 1 hearth year number of days)
# ELSE (normal year):
#   n = 365 days (in 1 hearth year number of days)

# Choose a Base date (b):
#   b = 2005 | c = 58000.00
#OR
#   b = 2323 | c = 00000.00

# Calculate the "month number". 
#This number shall be called m. Here's a list: 
#   January = 0; 
#   February = 31. 
#       For all other months, add one if it is a leap year. 
#   March = 59; 
#   April = 90; 
#   May = 120; 
#   June = 151; 
#   July = 181; 
#   August = 212; 
#   September = 243; 
#   October = 273; 
#   November = 304; 
#   December = 334.
# Personal Note: Would that be easier, if using ISO days?

# Find the day and year. 
# The day in the month is called d, 
# and the year is called y. 
# So, using 2005 as the base date, 23 May 2008 
# has these values: 
#   n = 366; 
#   b = 2005; 
#   c = 58000.00; 
#   m = 121 (120, +1 for leap year); 
#   d = 23; 
#   y = 2008.

# Put these values into the formula. 
# The stardate formula is this: 
#   c + (1000*(y-b)) + ((1000/n)*(m + d -1)) = Stardate. 
# Using the above values, the stardate works out to be 61390.71. 
# Stardates are usually quoted to two decimal places.
# Personal Note: Display ABS value at 2 decimas places

# Personal Note: For this part of Arythm Formula: (m + d -1); m+d can be replaced by ISO day!? But why the (-1) then? If using ISO date should we still need this -1? I don't think so.?
# After veriification:
#   For the date: 23 May 2008
#       ISO Date: Year 2008 Day 144
#   From above calculations: m+d = 144
# SO We keep (-1) in calculations

# Personal note: How to include Time? hh:mm?
# 1 day = 24h = 1440 minutes = 86400s
# We can include time (hh:mm) in our Calculation
# Determine current time hh:mm in minutes in t variable (as integer)
# consider those modifications:
#   1000/(n*1440)
#   (m + d -1)+t

# What is this sites' https://www.stoacademy.com/tools/stardate.php calculation? and Reference year?
# On the same web site, after few trials.
# We could determin their reference point beeing:
#   May 2, 1922 @ 14:01 = Stardate 00000.00
# This date as reference point seems Totally arbitrary to me, at first look.
# Other ways to define reference point: 2019/01/01 00:00 = Stadate 96601.20
# Rest of calculations confirm 1000 Stardate units = 1 Year = 365 Days (Normal Year) = 8 760 h = 525 600 mn = 31 536 000 s
# LEAP YEAR: Calculation in a Leap year is false in this website, as 1 leap year = 1001.37 Stadate units != 1000 Stardate units as it suppose to.

# OTHER PROJECT: Convert back STARDATE into Earth Date
