#!/usr/bin/python3.7
# UTF8
# Author: Nicolas Flandrois
# Description: Ici je cherche à grouper par valeur, selon une clé,
# des données venant d'une liste de disctionaires, afin d'en effectuer un compte.

import itertools

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
######################################################
# Mentor's Suggestions:
# Suggestion 1: in One liner!
groups_count = [*map(lambda g: (g[0], len(list(g[1]))), itertools.groupby(sorted(heroes, key=get_univers), get_univers))]

print('\nRaw output from Mentor\'s Oneliner suggestion 1 : \t', groups_count)

# Suggestion 2
from collections import Counter
print('\nMentor Suggestion 2: \t', Counter(h['univers'] for h in heroes))

# Suggestion 3
import collections
suphero = dict(collections.Counter(h['univers'] for h in heroes))
print('\nMentor Suggestion 3: \t', suphero)

print('Or Suggestion 3 put it nicely:')
for n in suphero:
    print(n, ': ', suphero[n])
