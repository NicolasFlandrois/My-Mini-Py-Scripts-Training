#!/usr/bin/python3.7
# UTF8
# Date: Thu 12 Sep 2019 12:48:10 CEST
# Author: Nicolas Flandrois
# Description: Experimenting with Progress Bar
# Other Progressbar process https://codingdose.info/2019/06/15/how-to-use-a-progress-bar-in-python/
import progressbar
import datetime
import os
import platform
import time


def clean():
    """Clear the terminal windox on Windows or Linux."""
    if platform.system() == "Windows":
        os.system("cls")
    else :
        # Linux and OSx
        os.system("clear")


def leapyr(year: int):
        """"
        This function defines if the year is
        a Leap year (366 days)
        or a Normal year (365 days).
        Then it will to the variable n the value of 366 or 365, accordingly.
        Returns a Tuple:
            - number of days tha year,
            - and a Boolean :
                            True == Leap Year
                            False == Normal Year
        """
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            n = 366
            leapyear = True

        else:
            n = 365
            leapyear = False

        return (n, leapyear)


# Loading Process Bar (Simulation)
pbar = progressbar.ProgressBar().start()
print('Loading Program :\t')
for i in range(100):
    time.sleep(0.02)
    # Or Do Something
    pbar.update(i+1)

pbar.finish()

clean()

now = datetime.datetime.now().timetuple()

print(f'Today\'s Year {now[0]} progression:\n(\'Ctrl+C\' to escape)\n')

yrpbar = progressbar.ProgressBar().start()
# for i in range(100):
#     time.sleep(0.02)
#     yrpbar.update(int((now[7]/leapyr(now[0])[0])*100))
# yrpbar.finished()
# yrpbar.widgets()

while True:
    time.sleep(0.05)
    yrpbar.update(int((now[7]/leapyr(now[0])[0])*100))

yrpbar.finished()
