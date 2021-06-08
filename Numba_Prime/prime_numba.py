#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Tue 08 June 2021 11:25:41 CEST
# Author: Nicolas Flandrois
# Last updated by: Nicolas Flandrois
# Last updated date: Tue 08 June 2021 11:25:53 CEST
# Python 3.9
# Numba 0.53.1
# Description: How to boost computation with Numba?
# Here filtering if a number is a Prime Number.

from numba import jit, int32
import math
import time

target_num = 10000000  # 10 Million

# NO Numba Boost
def isPrime(n):
    if n == 2 or n == 5:
        return True
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False

    max = int(math.ceil(math.sqrt(n)))
    i = 5
    w = 2
    while i < max:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

start = time.time()
numprimes = target_num
oddnum = [n for n in range(1, numprimes) if n % 2 != 0]
oddnum.insert(0, 2)
countprimes = 0
my_primes = []

for i in oddnum:
    if isPrime(i):
        countprimes += 1
        my_primes.append(i)
end = time.time()
print(f"NFL\nNumba Boost = False: There are {'{:,}'.format(countprimes).replace(',', ' ')} primes in the first {'{:,}'.format(numprimes).replace(',', ' ')}, computed in {end - start} s")
# print(len(my_primes))

# With Numba Boost
@jit(int32(int32))
def is_prime(n):
    if n == 2 or n == 5:
        return True
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False

    max = int(math.ceil(math.sqrt(n)))
    i = 5
    w = 2
    while i < max:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

start = time.time()
numprimes = target_num
oddnum = [n for n in range(1, numprimes) if n % 2 != 0]
oddnum.insert(0, 2)
countprimes2 = 0
my_primes = []

for i in oddnum:
    if is_prime(i):
        countprimes2 += 1
        my_primes.append(i)
end = time.time()
print(f"Numba Boost = True: There are {'{:,}'.format(countprimes2).replace(',', ' ')} primes in the first {'{:,}'.format(numprimes).replace(',', ' ')}, computed in {end - start} s")
# print(len(my_primes))

# ##########################################################################
# LOANN Version
# No Numba Boost

time1 = time.time()
results = [2, 3, 5]

def loannPrime(n:int, primes:list):
    a = math.sqrt(n)
    for prime in primes:
        if n % prime == 0:
            return False
        if prime > a:
            return True

target = target_num
for n in range(7, target, 2):
    if loannPrime(n, results):
        results.append(n)

time2 = time.time()-time1
print(f"Loann Version,\nNumba Boost = False: There are {'{:,}'.format(len(results)).replace(',', ' ')} primes in the first {'{:,}'.format(target).replace(',', ' ')}, computed in {time2} s")
# # Numba Boost = True
# time1 = time.time()
# results = [2, 3, 5]

# @jit(int32(int32))
# def loannPrimeBoosted(n:int, primes:list):
#     a = math.sqrt(n)
#     for prime in primes:
#         if n % prime == 0:
#             return False
#         if prime > a:
#             return True

# target = target_num
# for n in range(7, target, 2):
#     if loannPrimeBoosted(n, results):
#         results.append(n)

# time2 = time.time()-time1
# print(f'Loann Version, Numba Boost = True, For Target {target}, found {len(results)} primes number, computed in {time2} s.')
