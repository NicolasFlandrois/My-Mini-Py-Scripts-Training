#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Fri 31 July 2020 11:16:57
# Last Modified time: Fri 31 July 2020 16:39:14 

# Description:

# Solution:
# The almost impossible chessboard puzzle | Stand-Up Maths - https://youtu.be/as7Gkm7Y7h4
# DataGenetics | Impossible Escape? - http://datagenetics.com/blog/december12014/index.html
# How Might it be Impossible???:
# The impossible chessboard puzzle | 3Blue1Brown - https://youtu.be/wTJI_WuZSwE

# A warden gives an impossible puzzle to solve, to 2 inmates, in exchange of there freedom.
# On the a chessboard are displayed coins on each tiles, randomly facing Head or Tail.
# The first inmate comes in the room (without his other inmate),
# the warden show him under wich tile is the key hidden.
# This first inmate must communicate this key's tile to the second inmate,
# by flipping only 1 coin, then leaves the room.
# The Second inmate come in, the first time he has a look to the board and coin set.
# If the second inmate can find the correct tile with the key underneath, then they go free.
# Bothe inmates can cohers and strategies beforehand.

# For more difficulties, the warden knows your strategy in advance,
# and change the display of the head/tail, in a non random matter, to make it more difficult.

# How to do it?


# Random Head/Tail chessboard, Head = 0, Tail = 1
from random import choice

print('Initial Setup:\n\n')
chessboard = [[n, format(n, '06b'), choice([0, 1])] for n in range(64)]

print(
    f'Chessboard Coins (H = 0 / T = 1) display :\n{[n[2] for n in chessboard]}\n\n')
print(f'Full chessboard display:\n{chessboard}\n\n')
key_target = choice(range(64))
key_target_bin = format(key_target, '06b')
print(
    f'Key Target :\tTile nb:\t{key_target},\tCoordinates:\t{key_target_bin}\n\n')

# Encrypt


def chessboard_state(chessboard):
    bit_1 = (chessboard[1][2] + chessboard[3][2] + chessboard[5][2] + chessboard[7][2] +
             chessboard[9][2] + chessboard[11][2] + chessboard[13][2] + chessboard[15][2] +
             chessboard[17][2] + chessboard[19][2] + chessboard[21][2] + chessboard[23][2] +
             chessboard[25][2] + chessboard[27][2] + chessboard[29][2] + chessboard[31][2] +
             chessboard[33][2] + chessboard[35][2] + chessboard[37][2] + chessboard[39][2] +
             chessboard[41][2] + chessboard[43][2] + chessboard[45][2] + chessboard[47][2] +
             chessboard[49][2] + chessboard[51][2] + chessboard[53][2] + chessboard[55][2] +
             chessboard[57][2] + chessboard[59][2] + chessboard[61][2] + chessboard[63][2]) % 2

    bit_2 = (chessboard[2][2] + chessboard[3][2] + chessboard[6][2] + chessboard[7][2] +
             chessboard[10][2] + chessboard[11][2] + chessboard[14][2] + chessboard[15][2] +
             chessboard[18][2] + chessboard[19][2] + chessboard[22][2] + chessboard[23][2] +
             chessboard[26][2] + chessboard[27][2] + chessboard[30][2] + chessboard[31][2] +
             chessboard[34][2] + chessboard[35][2] + chessboard[38][2] + chessboard[39][2] +
             chessboard[42][2] + chessboard[43][2] + chessboard[46][2] + chessboard[47][2] +
             chessboard[50][2] + chessboard[51][2] + chessboard[54][2] + chessboard[55][2] +
             chessboard[58][2] + chessboard[59][2] + chessboard[62][2] + chessboard[63][2]) % 2

    bit_3 = (chessboard[4][2] + chessboard[5][2] + chessboard[6][2] + chessboard[7][2] +
             chessboard[12][2] + chessboard[13][2] + chessboard[14][2] + chessboard[15][2] +
             chessboard[20][2] + chessboard[21][2] + chessboard[22][2] + chessboard[23][2] +
             chessboard[28][2] + chessboard[29][2] + chessboard[30][2] + chessboard[31][2] +
             chessboard[36][2] + chessboard[37][2] + chessboard[38][2] + chessboard[39][2] +
             chessboard[44][2] + chessboard[45][2] + chessboard[46][2] + chessboard[47][2] +
             chessboard[52][2] + chessboard[53][2] + chessboard[54][2] + chessboard[55][2] +
             chessboard[60][2] + chessboard[61][2] + chessboard[62][2] + chessboard[63][2]) % 2

    bit_4 = (chessboard[8][2] + chessboard[9][2] + chessboard[10][2] + chessboard[11][2] + chessboard[12][2] + chessboard[13][2] + chessboard[14][2] + chessboard[15][2] +
             chessboard[24][2] + chessboard[25][2] + chessboard[26][2] + chessboard[27][2] + chessboard[28][2] + chessboard[29][2] + chessboard[30][2] + chessboard[31][2] +
             chessboard[40][2] + chessboard[41][2] + chessboard[42][2] + chessboard[43][2] + chessboard[44][2] + chessboard[45][2] + chessboard[46][2] + chessboard[47][2] +
             chessboard[56][2] + chessboard[57][2] + chessboard[58][2] + chessboard[59][2] + chessboard[60][2] + chessboard[61][2] + chessboard[62][2] + chessboard[63][2]) % 2

    bit_5 = (chessboard[16][2] + chessboard[17][2] + chessboard[18][2] + chessboard[19][2] + chessboard[20][2] + chessboard[21][2] + chessboard[22][2] + chessboard[23][2] +
             chessboard[24][2] + chessboard[25][2] + chessboard[26][2] + chessboard[27][2] + chessboard[28][2] + chessboard[29][2] + chessboard[30][2] + chessboard[31][2] +
             chessboard[48][2] + chessboard[49][2] + chessboard[50][2] + chessboard[51][2] + chessboard[52][2] + chessboard[53][2] + chessboard[54][2] + chessboard[55][2] +
             chessboard[56][2] + chessboard[57][2] + chessboard[58][2] + chessboard[59][2] + chessboard[60][2] + chessboard[61][2] + chessboard[62][2] + chessboard[63][2]) % 2

    bit_6 = (chessboard[32][2] + chessboard[33][2] + chessboard[34][2] + chessboard[35][2] + chessboard[36][2] + chessboard[37][2] + chessboard[38][2] + chessboard[39][2] +
             chessboard[40][2] + chessboard[41][2] + chessboard[42][2] + chessboard[43][2] + chessboard[44][2] + chessboard[45][2] + chessboard[46][2] + chessboard[47][2] +
             chessboard[48][2] + chessboard[49][2] + chessboard[50][2] + chessboard[51][2] + chessboard[52][2] + chessboard[53][2] + chessboard[54][2] + chessboard[55][2] +
             chessboard[56][2] + chessboard[57][2] + chessboard[58][2] + chessboard[59][2] + chessboard[60][2] + chessboard[61][2] + chessboard[62][2] + chessboard[63][2]) % 2

    return f'{bit_6}{bit_5}{bit_4}{bit_3}{bit_2}{bit_1}'


current_State = chessboard_state(chessboard)
print('Current State :\t', current_State)


def bin_sub(x, y):
    return abs(int(x) - int(y))


need_change = f'{bin_sub(key_target_bin[0], current_State[0])}\
{bin_sub(key_target_bin[1], current_State[1])}\
{bin_sub(key_target_bin[2], current_State[2])}\
{bin_sub(key_target_bin[3], current_State[3])}\
{bin_sub(key_target_bin[4], current_State[4])}\
{bin_sub(key_target_bin[5], current_State[5])} '

need_change_tile = int(need_change, base=2)

print(f'Need to flip/Change this coin:\t{need_change}\n\
Which is in Tile nb:\t{need_change_tile}\n\
Coin in tile nb {need_change_tile} was :\t{chessboard[need_change_tile][2]} (\
{"Tail" if chessboard[need_change_tile][2] == 1 else "Head"})\n\
Now this coin needs to be :\t{"0 (Head)" if chessboard[need_change_tile][2] == 1 else "1 (Tail)"}')

# Decrypt
print('\n\nLets Decrypt the puzzle then!?\n\n')
new_chessboard = chessboard

if new_chessboard[need_change_tile][2] == 1:
    new_chessboard[need_change_tile][2] = 0
else:
    new_chessboard[need_change_tile][2] = 1

print(
    f'\nNew Chessboard Coin (H = 0 / T = 1) Display:\n{[n[2] for n in new_chessboard]}\n\n')
print(f'\nFull chessboard display:\n{new_chessboard}\n\n')

new_state = chessboard_state(new_chessboard)

print('New Chessboard State:\t', new_state)

if new_state == key_target_bin:
    print(f'The new Chessboard State ({new_state}) \
matches the Target Key Tile ({key_target_bin}, tile nb:{key_target}).\
The key is underneath tile nb:\t{int(new_state, base=2)}')
else:
    print('An Error Occured.')
