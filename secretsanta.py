#!/usr/bin/python3.7
# UTF8
# Date: Fri 30 Aug 2019 14:41:01 CEST
# Author: Nicolas Flandrois

# Description: cf 'The indisputable existance of Santa Claus' by Dr Hannah Fry,
# Chapter 4 'Secret Santa' (p.46 to 54; ISBN 9781784162740).
# This exercice tends to define a Random Hat Picking assignment of
# a Secret Santa, to another participant.

# In this short exercice, we just simply create a pool, according to the number
# of participants, a randomly paired number ID with some other number ID.
# Then a pair is Randomly pulled out of the Bag (Pool list),
# and printed to the screen.

# That way each Santa is randomly assigned to a participant.

# In a real life situation, we should print out the Secret Santa Pairing list,
# cut the different strips of pairs. People picks in a sorting hat.
# Then We just list Who they are (not who they offer to),
# either right after sorting their pairs,
# or right before opening presents (Adding a bit of mistery).

# Nota Benne: As it is all managed and randomised by a computer, we could
# create a script with names assignements. Same random pairing script, then
# email/sms each pairs to the concerned secret santa, leaving no traces.
# >>>>>>Done!

import random

participants = int(input('How many participants?\t'))

numlist = [i+1 for i in range(participants)]
random.shuffle(numlist)
pair = {}

for n in numlist:
    pair[n] = numlist[numlist.index(n)-1]

scrtsanta = [f'\tI am {i}. \tI offer a gift to {v}' for i, v in pair.items()]

# print()
# for i in range(len(scrtsanta)):
#     choice = random.choice(scrtsanta)
#     scrtsanta.remove(choice)
#     print(choice)

with open('secretsanta.txt', 'w') as secretsanta:
    text = ['List of participant (place your name with each ID)']

    for i in range(len(scrtsanta)):
        text.append(f'\n\n\t{i+1}.\t........................................')

    text.append('\n\n\n\nSecret Santa Pairing Tickets (Cut and Hat Pick):')

    for i in scrtsanta:
        text.append(f'\n\n...........................................\n\n{i}')

    textview = " ".join([str(i) for i in text])
    secretsanta.write(str(textview))

print('Finished Process')
