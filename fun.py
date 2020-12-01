from time import sleep
from itertools import count
from random import choice
from base64 import b64encode


def baseN(num, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // base, base,
                                                  numerals).lstrip(numerals[0])
                                            + numerals[num % base])


counter = count(start=1)

while True:
    # n_round = next(counter)
    # rand_choice = choice([
    #                      bin(n_round)[2:],
    #                      hex(n_round)[2:],
    #                      n_round,
    #                      str(b64encode(str(n_round).encode())).replace(
    #                          '=', '')[2:-1],
    #                      baseN(n_round, 36),
    #                      baseN(n_round, 3),
    #                      baseN(n_round, 32),
    #                      baseN(n_round, 20)
    #                      ])
    print(baseN(random.randrange(1, 101), random.randrange(1, 37)))

    # print(f'Hello World ! {n_round} = {rand_choice}')
    sleep(0.5)
