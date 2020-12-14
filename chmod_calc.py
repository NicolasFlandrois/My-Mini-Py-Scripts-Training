#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Mon 14 December 2020 13:13:31 CET
# Author: Nicolas Flandrois
# Last updated by: Nicolas Flandrois
# Last updated date: Thu 17 September 2020 13:28:48 CEST

# Description:
# Linux system chmod converter, to ease the use of `chmod` command line.
# The program (developped in a short script),
# will prompt you which permissions should be allowed.
# Depending on your choice, it will display the command line you
# copy/paste in your terminal. Don't forget to replace the `filename`

def chmod_convert(filename):
    chmod = {'o':{'r':0, 'w':0, 'x':0},
             'g':{'r':0, 'w':0, 'x':0},
             'p':{'r':0, 'w':0, 'x':0},}

    print("What permissions would you like, for each sections:")
    chmod['o']['r'] = 4 if input('Owner Read? [Y/N]\t').lower() == 'y' else 0
    chmod['o']['w'] = 2 if input('Owner Write? [Y/N]\t').lower() == 'y' else 0
    chmod['o']['x'] = 1 if input('Owner Execute? [Y/N]\t').lower() == 'y' else 0
    chmod['g']['r'] = 4 if input('Group Read? [Y/N]\t').lower() == 'y' else 0
    chmod['g']['w'] = 2 if input('Group Write? [Y/N]\t').lower() == 'y' else 0
    chmod['g']['x'] = 1 if input('Group Execute? [Y/N]\t').lower() == 'y' else 0
    chmod['p']['r'] = 4 if input('Public Read? [Y/N]\t').lower() == 'y' else 0
    chmod['p']['w'] = 2 if input('Public Write? [Y/N]\t').lower() == 'y' else 0
    chmod['p']['x'] = 1 if input('Public Execute? [Y/N]\t').lower() == 'y' else 0

    print(f"\nYour command line should be: chmod \
{chmod['o']['r'] + chmod['o']['w'] + chmod['o']['x']}\
{chmod['g']['r'] + chmod['g']['w'] + chmod['g']['x']}\
{chmod['p']['r'] + chmod['p']['w'] + chmod['p']['x']} {filename}")
    print("\nWhen doing:\tls -l\nYour file should have the following permissions:")
    print(f"\n\t{'r' if chmod['o']['r'] == 4 else '-'}\
{'w' if chmod['o']['w'] == 2 else '-'}\
{'x' if chmod['o']['x'] == 1 else '-'}\
{'r' if chmod['g']['r'] == 4 else '-'}\
{'w' if chmod['g']['w'] == 2 else '-'}\
{'x' if chmod['g']['x'] == 1 else '-'}\
{'r' if chmod['p']['r'] == 4 else '-'}\
{'w' if chmod['p']['w'] == 2 else '-'}\
{'x' if chmod['p']['x'] == 1 else '-'} \
[number of links to the file] [Owner's name] [Group's name] \
[File's size in bytes] [Date & Time] [Filename]")

    print(f"\nFor exemple:\n\t{'r' if chmod['o']['r'] == 4 else '-'}\
{'w' if chmod['o']['w'] != 0 else '-'}\
{'x' if chmod['o']['x'] != 0 else '-'}\
{'r' if chmod['g']['r'] != 0 else '-'}\
{'w' if chmod['g']['w'] != 0 else '-'}\
{'x' if chmod['g']['x'] != 0 else '-'}\
{'r' if chmod['p']['r'] != 0 else '-'}\
{'w' if chmod['p']['w'] != 0 else '-'}\
{'x' if chmod['p']['x'] != 0 else '-'} \
1 bob_usr admin_grp 63276000 Oct 29 14:00 {filename}")

if __name__ == '__main__':
    chmod_convert('filename')
