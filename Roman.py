#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date: Fri 24 July 2020 11:23:44
# Last Modified : Wed 18 May 2022 16:57:49 CEST


def roman_convert(dec_num: int) -> str:
    '''
    Convert a decimal number (Positive Integer) between 1 and 3999
    to a Roman numeral equivalent.

    It must follow the common rules of roman numeral system. Which includes no
    suite of same letters more than 3 times in a raw.

    For which [900, 400, 90, 40, 9, 4] would have special treatment,
    and be converted as [CM, CD, XC, XL, IX, IV]. That is also why we are
    limited to a max of 3999, because 4000 would be "MMMM" 4 M in a raw,
    and won't be legitimate.
    And notably, Zero doesn't exists.

    Argument
    -----------
    dec_num (int): Positive Integer from 1 to 3999

    Return
    --------
    str: Either a Message error if out of range,
         or the Roman Converted numeral.

    A good website reference, to explain how Roman Numerals works:
    https://all-about-roman-numerals.com/
    '''
    if dec_num not in range(1, 4000):
        return "Out of range - Should be between 1 and 3999."
    else:
        romdict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                   'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
                   'IV': 4, 'I': 1}
        rom_tmp_lst = []
        for key, val in romdict.items():
            rom_tmp_lst.append((dec_num // val)*key)
            dec_num = dec_num % val
        return ''.join(rom_tmp_lst)


# A few Exemples:
for n in range(20):
    print(n, ':\t', roman_convert(n))

# This should look like:
# 0 :  Out of range - Should be between 1 and 3999.
# 1 :  I
# 2 :  II
# 3 :  III
# 4 :  IV
# 5 :  V
# 6 :  VI
# 7 :  VII
# 8 :  VIII
# 9 :  IX
# 10 :     X
# 11 :     XI
# 12 :     XII
# 13 :     XIII
# 14 :     XIV
# 15 :     XV
# 16 :     XVI
# 17 :     XVII
# 18 :     XVIII
# 19 :     XIX

test_list = [0, -1, 20, 40, 44, 50, 55, 77, 99, 100, 490, 500, 600, 649, 899,
             900, 999, 1000, 1754, 1998, 1999, 2022, 2999, 3000, 3549, 3999,
             4000, 5000]
for n in test_list:
    print(n, ':\t', roman_convert(n))

# This should look like this:
# 0 :  Out of range - Should be between 1 and 3999.
# -1 :     Out of range - Should be between 1 and 3999.
# 20 :     XX
# 40 :     XL
# 44 :     XLIV
# 50 :     L
# 55 :     LV
# 77 :     LXXVII
# 99 :     XCIX
# 100 :    C
# 490 :    CDXC
# 500 :    D
# 600 :    DC
# 649 :    DCXLIX
# 899 :    DCCCXCIX
# 900 :    CM
# 999 :    CMXCIX
# 1000 :   M
# 1754 :   MDCCLIV
# 1998 :   MCMXCVIII
# 1999 :   MCMXCIX
# 2022 :   MMXXII
# 2999 :   MMCMXCIX
# 3000 :   MMM
# 3549 :   MMMDXLIX
# 3999 :   MMMCMXCIX
# 4000 :   Out of range - Should be between 1 and 3999.
# 5000 :   Out of range - Should be between 1 and 3999.
