#!/usr/bin/python3.7
# UTF8
# Date: Mon 12 Aug 2019 14:51:37 CEST
# Author: Nicolas Flandrois

# Description: Practice exercise using Iterators, Class and Generators. This
# script will simulate (recreate) Python's range method.

# Using Class


class MyRange(object):
    """
    MyRange simulates the Python's range method, using Class, and only
    Integers
    """
    def __init__(self, start: int, end: int):
        """This __init__() defines arguments"""
        self.value = start
        self.end = end

    def __iter__(self):
        """This __iter__() defines self as an iterable"""
        return self

    def __next__(self):
        """This __next__() defines the possibility to iter to the next item"""
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# Exemple Using Class:

print("Exemple Using Class")

c_nums = MyRange(1, 10)

print("Using a For loop to print each iteration")

for num in c_nums:
    print(num)

# We need to create a new range, as previous MyRange has been exhausted from
# iteration in previous exemple

c2_nums = MyRange(2, 10)

print("Print each iterable using the next function")

print(next(c2_nums))
print(next(c2_nums))
print(next(c2_nums))
print(next(c2_nums))

# Using a Generator


def my_range(start: int, end: int):
    """
    my_range simulates the Python's range method, using a generator, and
    only Integers. One of the few avantages, the script here is shorter, as
    the iteration and next method already exist and inherit from the generator.
    """
    current = start
    while current < end:
        yield current
        current += 1


# Exemple using Generator

print("Exemple using Generator")

g_nums = my_range(3, 10)

print("Using a For loop to print each iteration")

for num in g_nums:
    print(num)

# We need to create a new range, as previous my_range has been exhausted from
# iteration in previous exemple

g2_nums = my_range(4, 10)

print("Print each iterable using the next function")

print(next(g2_nums))
print(next(g2_nums))
print(next(g2_nums))
print(next(g2_nums))
