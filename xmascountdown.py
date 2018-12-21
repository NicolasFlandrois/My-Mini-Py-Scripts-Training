#! usr/bin/python3

# Thu 20 Dec 2018 03:04:22 PM CET 
# Author: Nicolas Flandrois
# Description: Christmas countdown, according to a choosen year.
# NB: This script is not UTC/Timezone aware. Time is set as naive, using your local (computer) timezone as default.

import time
import datetime
import os
import platform
import sys

def clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

try:
    Year = int(input("Xmas of which year? "))
except:
    print("Oops! ",sys.exc_info()[0],""" occured. That was no valid number.  Try again...
choose a year, in number, format YYYY.""")

xd = datetime.datetime(Year, 7, 25, 0, 0, 1)

clean()

while True:
    td = datetime.datetime.now()
    delta = xd - td
    cd_Y = int(delta.days / 365)
    cd_W = int(abs(delta.days - (cd_Y * 365)) / 7)
    cd_D = int(abs(delta.days - ((cd_Y * 365)+ (cd_W * 7))))
    cd_h = int(delta.seconds / 3600)
    cd_m = int(abs(delta.seconds - (cd_h * 3600))/60)
    cd_s = int(abs(delta.seconds - ( cd_h*3600 + cd_m*60 )))

    print("Countdown until christmas of: ", xd.strftime("%A, %d of %B %Y"))
    print("")
    print("Total days left: ", delta.days)
    print("")
    print("or more precisely, time left: ")
    print(cd_Y, "Years", cd_W, "Weeks", cd_D, "Days - ", "%02d" % cd_h, ":", "%02d" % cd_m, ":", "%02d" % cd_s, "; Local Time.")
    print("")

    time.sleep(1)
    clean()
