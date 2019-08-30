#!/usr/bin/python3.7
# UTF8
# Date: Tue 27 Aug 2019 14:27:23 CEST
# Author: Nicolas Flandrois
# Description:
    # This tool will automatically check your python's pip list in your system,
    # and update all packages to their newest versions.
    # Then it will display a summary, with double checking points
    # (number of packages before update compared to after update;
    # and the number of packages that have been updated). Then it will display
    # the list of updated packages: New Versions vs. Old versions.

import os
import pkg_resources
import platform
from subprocess import call
import time


def clean():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def autoupdate():
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("pip install --upgrade " + ' '.join(packages), shell=True)


os.system("pip list > piplist_before.txt")

autoupdate()

print('\n\nUpdate Completed. Please Wait for checkpoint.\
\t(Estimated Waiting Time: 00:00:30)')
time.sleep(30)

os.system("pip list > piplist_after.txt")

with open('piplist_before.txt', 'r') as f:
    before = set(f.read().lower().replace(" ", "").split('\n'))

with open('piplist_after.txt', 'r') as f:
    after = set(f.read().lower().replace(" ", "").split('\n'))

delta1 = sorted(list(after.difference(before)))
delta2 = sorted(list(before.difference(after)))

clean()
print(f'lenght of pip list Before:\t{len(before)}')
print(f'lenght of pip list After:\t{len(after)}')
print(f'lenght of pip list delta(after/before):\t{len(delta1)}')
print(f'lenght of pip list delta(before/after):\t{len(delta2)}')
print('\n\nNew Versions\t||\tOld Versions\n')
for i in range(len(delta1)):
    print(f'{delta1[i]}\t ||\t {delta2[i]}')
