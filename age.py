#!/usr/bin/python3.7
# UTF8
# Date: Fri 30 Aug 2019 13:50:22 CEST
# Author: Nicolas Flandrois

from datetime import datetime

bdlt_Y = int(input("Year of Birth (YYYY Format):\t"))
bdlt_m = int(input("Month of Birth (MM Format):\t"))
bdlt_D = int(input("Day of Birth (DD Format):\t"))

b_date = datetime.strptime(f'{bdlt_Y} {bdlt_m} {bdlt_D}', '%Y %m %d').timetuple()
d_now = datetime.now().timetuple()

dlt = {}

if d_now[7] < b_date[7]:
    dlt['years'] = d_now[0] - b_date[0] - 1
    dlt['months'] = d_now[1] - b_date[1] + 11
    dlt['days'] = b_date[7] - d_now[7]
    dlt['hours'] = 24 - d_now[3] - b_date[3]
    dlt['minutes']= 60 - d_now[4] - b_date[4]
    dlt['seconds']= 60 - d_now[5] - b_date[5]
else:
    dlt['years'] = d_now[0] - b_date[0]
    dlt['months'] = d_now[1] - b_date[1]
    dlt['days'] = d_now[2] - b_date[2]
    dlt['hours'] = d_now[3] - b_date[3]
    dlt['minutes']= d_now[4] - b_date[4]
    dlt['seconds']= d_now[5] - b_date[5]

print(f"You are {dlt['years']} Years, {dlt['months']} Months, {dlt['days']} Days, and {dlt['hours']}:{dlt['minutes']}:{dlt['seconds']} old.")
