#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Sat 12 December 2020 21:36:52 CET
# Author: Nicolas Flandrois
# Last updated by: Nicolas Flandrois
# Last updated date:Mon 14 December 2020 13:12:01 CET

# Description:
# Game development, game logic structure: SHIFUMI / Rock Paper Scissors.
# Player vs Computer
# Managing to each round, either Win, Tie, or Lose.
# Best out of 3 is the winner, get the score.
# simple menu to play again. Keeping score tracks, overall.

from random import choice

rps = ["rock", "paper", "scissors"]

global_score = {"player":0, "computer":0, "tie":0, "nb_game":0}

print("Rock - Paper - Scissors GAME")

while True:
    global_score["nb_game"] += 1
    best_out_of_3 = {"player":0, "computer":0}
    for _ in range(3):
        print()
        computer = choice(rps)
        player = input("Rock (R), Paper (P), Scissors (S) ?\n").lower()

        if player in ['r', 'rock', 'pierre']:
            player = "rock"
        elif player in ['p', 'paper', 'papier', 'pq']:
            player = "paper"
        elif player in ['s',
                        'scissors', 'scisors', 'scizors',
                        'scissor', 'scisor', 'scizor',
                        'sissors', 'sisors', 'sizors',
                        'sissor', 'sisor', 'sizor',
                        'ciseaux', 'ciseau', 'cisueax', 'cisuea',
                        'razor', 'rasor', 'razors', 'rasors', 'rasoir',
                        'rasoirs', 'knife', 'knifes', 'couteaux', 'couteau']:
            player = "scissors"
        else:
            pass

        if  player == computer:
            print("Nobody wins...")
        elif player =='rock' and computer == 'scissors':
            best_out_of_3["player"] += 1
            print("you Win !")
        elif player == 'scissors' and computer == 'paper':
            best_out_of_3["player"] += 1
            print("you Win !")
        elif player == 'paper' and computer == 'rock':
            best_out_of_3["player"] += 1
            print("You win !")
        else:
            best_out_of_3["computer"] += 1
            print("You Lost !")
        print("you chose:\t", player.capitalize(), "\nComputer Chose:\t", computer.capitalize())

    print()
    if best_out_of_3["player"] == best_out_of_3["computer"]:
        global_score["tie"] += 1
        print("This is a tie! Nobody wins.")
    elif best_out_of_3["player"] > best_out_of_3["computer"]:
        global_score["player"] += 1
        print("You win this round!")
    else:
        global_score["computer"] += 1
        print("computer wins this round.")

    print(f'''\nOverall Score, out of {global_score["nb_game"]} games:
        Player :\t{global_score["player"]}
        Computer:\t{global_score["computer"]}
        Tie (games with no winners):\t{global_score["tie"]}''')

    if input("Would you like to play again? (Y/N)\t").lower() == "n":
        break
