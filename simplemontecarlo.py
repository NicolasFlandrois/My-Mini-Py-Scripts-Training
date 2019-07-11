#!/usr/bin/python3.7
# UTF8
# Date: Thu 11 Jul 2019 11:39:39 CEST
# Author: Nicolas Flandrois
# Description: Simple Montecarlo model for statistical analysis.

# Random Walk Context: Supose you are in a city arranged in a perfect grid.
# You go for a walk, and at each intersection you choose your next direction
# randomly to go North, South, East, or West. Backtracking is permited.
# Once you finish with your walk, you check how far away you are from where
# you began, home. If you are more than 4 blocks away, you'll pay for a
# transport. Otherwise you'll just walk. What is the longest random walk you
# can take so that on average you will en up 4 blocks or fewer from home?

import random


def random_walk(n):
    """return coordinates after 'n' block random walk"""
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx  # dx = "Difference in x"
        y += dy  # dy = "Difference in y"
    return x, y

number_of_walks = 20000

for walk_length in range(1, 31):
    no_transport = 0  # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print(f"walk size = {walk_length} \
| % of no transport = {100*no_transport_percentage}.")

# How to get the simmulation more efficient? Using a generator (Yield)!?
# Also, I can make a function that return a Tuple
# (walk_length, %_of_no_transport),
# so we can store the info, or export for further analysis,
# and statistical Data Science.
