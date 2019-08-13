#!/usr/bin/python3.7
# UTF8
# Date: Mon 12 Aug 2019 14:51:37 CEST
# Author: Nicolas Flandrois
# Description: Itertools, Sorting, f-String (Py 3.6 & Up)

import itertools
import operator  # Used in line 254~ish with accumulators
from operator import attrgetter  # Used in line 441

##########################
# Count Itertools Method #
##########################
print("Count Itertools Method")

counter = itertools.count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# If no arguments this function goes in while True loop, and is indefinite.
# But we can iterate with next function

counter2 = itertools.count(start=5, step=-2.5)
print(next(counter2))
print(next(counter2))
print(next(counter2))
print(next(counter2))

data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))

print(daily_data)
print("")

################
# Zip function #
################
print("Zip function")
# Zip merge 2 list together and pair each list's index value together
# into a Tuple.
# cf previous exemple

daily_data2 = list(itertools.zip_longest(range(10), data))
print(daily_data2)
# As the range iterable is longer, the zip_longest() function will pair to the
# Longest iteration, attributing Null/None values to compleate the shortest
# iterable.
print("")

##################
# Cycle Function #
##################
print("Cycle Function")
# Be careful this function, like itertools.count(), can go forever,
# if not properly used.

cycle = itertools.cycle([1, 2, 3])
print(next(cycle))  # Will print 1
print(next(cycle))  # Will print 2
print(next(cycle))  # Will print 3
print(next(cycle))  # Will print 1
print(next(cycle))  # Will print 2
print(next(cycle))  # Will print 3

# It just pass through our iterable, and repeat, in cycle, as long as asked to.

cycle2 = itertools.cycle(("On", "Off"))
print(next(cycle2))  # Will print On
print(next(cycle2))  # Will print Off
print(next(cycle2))  # Will print On
print(next(cycle2))  # Will print Off
print(next(cycle2))  # Will print On
print(next(cycle2))  # Will print Off
print(next(cycle2))  # Will print On
print(next(cycle2))  # Will print Off
print("")

###################
# Repeat Function #
###################
print("Repeat Function")
rep = itertools.repeat(2, times=3)
print(next(rep))  # Will print 2
print(next(rep))  # Will repeat once again, and print 2
print(next(rep))  # Will repeat one last time (as times=3), and print 2
# print(next(rep))  # Will repeat NOTHING, as we finished our repeat 'loop'.
# print(next(rep))  # As we are out of the repeat 'loop',
# an exception is raised.
# If we'd use a for loop, the StopIteration is taken care of within the for
# loop, therefore the loop would stop, and no exception message would show.

# Useful to pass (repeat) a stream of constant values to an iterating function value

# Concreate exemple
print("Repeat used in Square function")
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))
print("")

####################
# Starmap Function #
####################
print("Starmap used in list of cubes")
cubes = itertools.starmap(pow, [(0, 3), (1, 3), (2, 3), (3, 3)])

print(list(cubes))
print()

#######################################
# Combination v. Permutation Function #
#######################################
# Combinations pair a certain number of items, where the order does not matters
# Permutations pair a certain number of items, where the order does matters
print("Combination v. Permutation Function")
letters = ['a', 'b', 'c', 'd']

# In this first exemple, we are looking for the combinations of all pairs of
# 2 letters from this list.
result = itertools.combinations(letters, 2)

# Exemple when the order does NOT Matter: a poker hand,
# if you get a Ace and a King, or a King and a Ace, it's the same for the game.

print("Combinations of letters (Order Does NOT Matter): ")
for item in result:
    print(item)
print()

# If Order Does Matter, then Use Permutations.
res = itertools.permutations(letters, 2)
# Can be used to simulate all possible results in a race, as reallife exemple.
print("Permutations of letters (Order DOES Matter): ")
for item in res:
    print(item)
print()

# Combinations and Permutations doesn't allow to repeat.
# It doesn't offer a (a, a) for exemple.

print("Combinations and Permitation... But we can repeat an item... \
Use the product function")

# Exemple: We'd like to get all combinations for a pin, using the numbers list.
# Which should allow pins like (0, 0, 0, 0) or (1, 1, 1, 1)
# Can be used to brute force a password, for exemple

numbers = [0, 1, 2, 3]

prod = itertools.product(numbers, repeat=4)
for item in prod:
    print(item)

print("But there is a way to do it with combinations:")
c_rep = itertools.combinations_with_replacement(numbers, 3)
for item in c_rep:
    print(item)
print()

##################
# Chain Function #
##################
print('Chain Function')
# This function chain multiple iterables, so after exhausting an iterable,
# it pass through the next iterable, and so on, especially using
# Giant iterables, or generators, or iterables are of different types.
names = ['Martin', 'Frida']

combined = itertools.chain(letters, numbers, names)

for i in combined:
    print(i)
print()

###################
# islice Function #
###################
print('islice Function')
# provides a slice of an iterator, Specifying how many First/Last items
# of an iterator you'd like.
print('simple islice function, arg = Stoping point')
aslice = itertools.islice(range(10), 5)
for i in aslice:
    print(i)
print()
# Passing a starting point
print('islice function with starting point')
aslice2 = itertools.islice(range(10), 1, 5)
for i in aslice2:
    print(i)
print()
# We Can do Steps
print('islice function with steps')
aslice3 = itertools.islice(range(10), 1, 5, 2)
for i in aslice3:
    print(i)
print()

# Useful Exemple:
# We may have an iterable that is too large to store in memory. So we don't
# want to put it into a list, just to have a slice out of it
# (from list slicing function).
# Exemple a log file with Thousands of logs, but we just want the Top one.
# So Use ISLICE function.

#####################
# Compress Function #
#####################
print('Compress Function')
selectors = [True, True, False, True]

compress = itertools.compress(letters, selectors)

for i in compress:
    print(i)
print()
# return only items matching True value, from combined iterables
# Other way is to use standard build in filter function.
print('Using Filter')
# The Filter function, uses a function to compare if 2 iterators are
# True or False. Instead, the Compressor uses 2 iterators,
# T/F statement already exists. Depending on what solution we need to our task.


def lt_2(n):
    if n < 2:
        return True
    return False


fltr = filter(lt_2, numbers)
for i in fltr:
    print(i)
print()
# We can also filter False Value...
print('Using Filter False')
fltr_f = itertools.filterfalse(lt_2, numbers)
for i in fltr_f:
    print(i)
print()

#######################
# Drop while Function #
#######################
num2 = [0, 1, 2, 3, 2, 1, 0]
print("num2 = [0, 1, 2, 3, 2, 1, 0]")
print('Using Filter False like previously with num2, before Drop While Function')
fltr_f2 = itertools.filterfalse(lt_2, num2)
for i in fltr_f2:
    print(i)
print()
print('Using num2 with Drop While Function > return value if False')
fltr_f3 = itertools.dropwhile(lt_2, num2)
for i in fltr_f3:
    print(i)
# After hiting the first value verifying the condition, it iterates the rest of
# the iterables, regardless of its value, or the condition.
print()
print('Using num2 with Take While Function > return value if True')
fltr_t = itertools.takewhile(lt_2, num2)
for i in fltr_t:
    print(i)
# After hiting the first value verifying the condition, it discard the rest of
# the iterables, regardless of its value, or the condition.
print()

#######################
# Accumulate Function #
#######################
# Keeps a running total (Sum by default) of the iterables
print('Accumulates Function')
print('default == Sum')
acc_default = itertools.accumulate(num2)
for i in acc_default:
    print(i)
print()
print('Specific == multiply')
num3 = [1, 2, 3, 2, 1, 0]
print("using num3 = [1, 2, 3, 2, 1, 0]")
acc_mul = itertools.accumulate(num3, operator.mul)
for i in acc_mul:
    print(i)
# Works if the first iterable isn't 0,
# or everything in the iterable will be == 0
print()

#############
# Group Val #
#############
print('Group values (returning a group of Tuples)')
print()


def get_state(person):
    """Feed a person dict return the state only"""
    return person['state']

people = [
    {
        'name':'Batman',
        'city':'Gotham',
        'state':'whocares'
    },
    {
        'name':'Superman',
        'city':'Metropolis',
        'state':'whocares'
    },
    {
        'name':'Flash',
        'city':'Central City',
        'state':'whocares'
    },
    {
        'name':'Spiderman',
        'city':'New York City',
        'state':'SomewhereNorthEast'
    },
    {
        'name':'Green Arrow',
        'city':'Starling City',
        'state':'SomewhereNorthEast'
    }
]

person_group = itertools.groupby(people, get_state)
# itertools.groupby(iterable, key)

for key, group in person_group:
    print(key)
    for person in group:
        print(person)
    print()
print()
# becareful, if keys are spread out, and not already sorted in the dict,
# this function doesn't sort it for you.
# If for instance, here Flash('state':'whocares') is position
# after Green Arrow('state':'SomewhereNortEast')
# The function will return 3 KeysGroups : whocares(with 2 items),
# SomewhereNortEast(with 2 items), whocares(with 1 item)
person_group = itertools.groupby(people, get_state)
for key, group in person_group:
    print(key, len(list(group)))
print()

####################################################
# How to replicate/duplicate an iterator/iterable? #
####################################################
print('Replicate/Duplicate an iterator')
person_group2 = itertools.groupby(people, get_state)
copy1, copy2 = itertools.tee(person_group2)
print('copy1')
for key, group in copy1:
    print(key)
    for person in group:
        print(person)
    print()
print()
print("copy2")
for key, group in copy2:
    print(key, len(list(group)))

##############################################################################
############ The following is out of Itertools perimeter #####################
##############################################################################

###########
# SORTING #
###########

######################################################
# Sorting iterables in ascending or descending order #
######################################################
print('\n Sorting iterables in ascending or descending order')
print('\n Sorting Lists')
li = [0, 7, 8, 4, 5, 6, 1, 9, 1]
print('Original variable (unsorted): \t', li)
s_li = sorted(li)  # This method sort and create a new variable
print('Sorted Variable: \t\t', s_li)
li.sort()  # This method sort the things in place, and return none
print('Original list sorted: \t\t', li)
rev_sort = sorted(li, reverse=True)
print('Reverse sorted Variable: \t', rev_sort)
li.sort(reverse=True)
print('Original reverse sorted: \t', li)

print('\n Sorting Tuples')
tup = (9, 7, 5, 3, 1, 2, 4, 6, 8, 0)
print('Original Tuple: \t', tup, ' Returning a Tuple')
# tup.sort() Would raise an error
s_tup = sorted(tup)
print('Sorted Tuple: \t\t', s_tup, ' Returning a List')

print('\n Sorting Dictionary')
dic = {'name':'Superman', 'job':'Super Hero', 'age':'Unknown',
       'secretid':'Clark Kent'}
print('Original Dictionary: \t', dic)
s_dic = sorted(dic)  # Sorting Keys into a list
print('Sorted Dictionary: \t', s_dic)

#########################################
# Sorting iterables from other criteria #
#########################################
print('\n\n Sorting iterables from other criterias')
li2 = [-5, -6, -4, 1, 2, 3, 0]
print('\nOriginal Variables: \t\t', li2)
s_li2 = sorted(li2)
print('Default sorted: \t\t', s_li2)
# Sort based on Absolute values
abs_li2 = sorted(li2, key=abs)
print('Sorted by Absolute values: \t', abs_li2)

print('\n\n Sorting by keys')


class Employee():
    """Employee Class"""
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, $ {self.salary})'

e1 = Employee('Carl', 37, 70_000)
e2 = Employee('Sarah', 29, 80_000)
e3 = Employee('John', 43, 90_000)

employees = [e1, e2, e3]


# def e_sort(emp):
#     """Key variables"""
#     return emp.name
#     # return emp.age
#     # return emp.salary

# s_employees = sorted(employees, key=e_sort, reverse=True)


# s_employees = sorted(employees, key=lambda e: e.name, reverse=True)
s_employees = sorted(employees, key=attrgetter('age'))

print('Sorted (reversed) Employees by key (name): \t', s_employees)

print('\n\n Sorting a list of dictionnaries, from a Key, \
then groupby with itertools')

heroes = [
    {
        'name':'Batman',
        'city':'Gotham',
        'univers':'DC'
    },
    {
        'name':'Superman',
        'city':'Metropolis',
        'univers':'DC'
    },
    {
        'name':'Flash',
        'city':'Central City',
        'univers':'DC'
    },
    {
        'name':'Spiderman',
        'city':'New York City',
        'univers':'Marvel'
    },
    {
        'name':'Green Arrow',
        'city':'Starling City',
        'univers':'DC'
    },
    {
        'name':'Aquaman',
        'city':'Antlantic City',
        'univers':'DC'
    },
    {
        'name':'Iron Man',
        'city':'New York City',
        'univers':'Marvel'
    },
    {
        'name':'Wonder Woman',
        'city':None,
        'univers':'DC'
    },
    {
        'name':'Spider Gwen',
        'city':'New York City',
        'univers':'Marvel'
    }
]

print('\nOriginal Data: \t\t', heroes, '\n')
# This is a mess to read!

#############################################

hero1, hero2 = itertools.tee(heroes)

#############################################


def get_univers(person):
    return person['univers']

unsorted_univgroup = itertools.groupby(hero1, get_univers)

print('\nUnsorted Group by Univers (from Original Data):')
for key, group in unsorted_univgroup:
    print('\t', key, len(list(group)))

# This doesn't really group, as presented unsorted data

##############################################

# This doesn't seem to be the easy way, but it works.
# If you can Optimise, you're very welcome!


class Hero():
    """This class defines the hero's attributes"""
    def __init__(self, name, city, univers):
        self.name = name
        self.city = city
        self.univers = univers

    def __repr__(self):
        return f'({self.name}, {self.city}, {self.univers})'


def e_heroes(pers):
    return pers.univers


hero_list = [Hero(h['name'], h['city'], h['univers']) for h in hero2]

s_heroes = sorted(hero_list, key=e_heroes)

print('\nSorted by Univers: \t', s_heroes, '\n')

univers_group = itertools.groupby(s_heroes, e_heroes)


print('\nSorted Group by Univers (from Sorted Data):')
for key, group in univers_group:
    print('\t', key, len(list(group)))

#########################
# Mentor's Suggestions: #
#########################

# Suggestion 1: in One liner!
groups_count = [*map(lambda g: (g[0], len(list(g[1]))),
                     itertools.groupby(sorted(heroes, key=get_univers),
                                       get_univers))]

print('\nRaw output from Mentor\'s Oneliner suggestion 1 : \t', groups_count)

# Suggestion 2
from collections import Counter
print('\nRaw output from Mentor\'s Suggestion 2: \t', Counter(h['univers'] for h in heroes))

# Suggestion 3
import collections
suphero = dict(collections.Counter(h['univers'] for h in heroes))
print('\nRaw output from Mentor\'s Suggestion 3: \t', suphero)

print('Or Suggestion 3 put it nicely:')
for n in suphero:
    print('\t', n, ': ', suphero[n])


##############################################################################
############# The following is out of previous perimeter #####################
##############################################################################

############
# F STRING #
############

print('\n\n\nF-String\n\n\n'.upper())

# The following works in Python 3.6 and up.
# Multiple exemples of formating:

hero = 'Superman'
first_name = 'clark'
last_name = 'kent'
print(f'{hero} is {first_name.title()} {last_name.upper()}\n')

batman = {'name':'Bruce Wayne', 'city':'Gotham'}
print(f"{batman['name']}  is in {batman['city'].upper()}\n")
# As the simple quote inside the dictionnary key, would disrupt the single
# quote in the f-string, therefor we use f-string with double quotes.

print(f'4 multiplied by 11 is equal to {4 * 11}.\n')
# We can Calculate inside a f-string

for n in range(1, 11):
    print(f'the value is {n:03}')
    # Formating the integer with 0 padding @ 3 digits

pi = 3.14159265
print(f'\nPi is equal to {pi:.4f}\n')
# displaying 4 digits after the floating point + Bonus, it's rounded up.

from datetime import datetime
birthday = datetime(1990, 1, 1)
print(f'Is {hero.lower()}\'s birthday on {birthday:%B %d, %Y}.')
