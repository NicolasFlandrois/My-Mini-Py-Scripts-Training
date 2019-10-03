#!/usr/bin/python3.7
# UTF8
# Date: Thu 03 Oct 2019 15:44:32 CEST
# Author: Nicolas Flandrois

# Description: Recursion practice exercise in Python, using Tower of Hanoï game.
# https://en.wikipedia.org/wiki/Tower_of_Hanoi
# The objective of the puzzle is to move the entire stack to another rod,
# obeying the following simple rules:
#   1/ Only one disk can be moved at a time.
#   2/ Each move consists of taking the upper disk from one of the stacks and
#      placing it on top of another stack or on an empty rod.
#   3/ No larger disk may be placed on top of a smaller disk.

# Legend:
# f = 'from' position
# t = 'to' position
# h = 'helper' position
# n = number of disks

from math import pow


def move(f, t):
    """
    The move function, describe a movement of an(/1) object,
    from a position 'f', to a position 't'.
        f = 'from' position
        t = 'to' position
    """
    print(f'Move {f} to {t} !')


def hanoi(n, f, h, t):
    """
    The Hanoi function manages through recursion moves of 'Tower of Hanoi'
    mathematical game, of 'n' numbers of disks, from an initial position 'f',
    to the target position 't', using the help of a third helper position 'h'.
    In it's quintessencial definition, the 'Tower of Hanoi' puzzle uses
    only 3 positions.
    """
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, t, h)
        move(f, t)
        hanoi(n - 1, h, f, t)


print("""
The Tower of Hanoi (also called the Tower of Brahma or Lucas' Tower and \
sometimes pluralized as Towers) is a mathematical game or puzzle.\
It consists of three rods and a number of disks of different sizes, \
which can slide onto any rod. The puzzle starts with the disks in a neat stack \
in ascending order of size on one rod, the smallest at the top, \
thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying \
the following simple rules:

        1/ Only one disk can be moved at a time.
        2/ Each move consists of taking the upper disk from one of the stacks
           and placing it on top of another stack or on an empty rod.
        3/ No larger disk may be placed on top of a smaller disk.

The minimal number of moves required to solve a Tower of Hanoi puzzle is \
2^n − 1, where n is the number of disks.

source: https://en.wikipedia.org/wiki/Tower_of_Hanoi
""")

n = int(input('How many (n) Disks ? '))
# n = 3  # Test

hanoi(n, 'A', 'B', 'C')

print(f'Minimum number of moves for this instance of n = {n} disks, \
is in {int(pow(2, n)-1)} moves.')

# How to count the number of steps used? Here we mathematically deduce it.
