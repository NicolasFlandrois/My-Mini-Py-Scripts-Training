#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date: Fri 24 July 2020 11:23:44
# Last Modified : Wed 18 May 2022 22:38:08 CEST


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


def roman_translate(rom_num: str) -> int:
    '''
    Translating a Roman numeral into modern decimal (positive integer) number.
    The submitted roman numeral will be between 'I'(1) and 'MMMCMXCIX'(3999).

    It must follow the common rules of roman numeral system. Which includes no
    suite of same letters more than 3 times in a raw.

    For which [900, 400, 90, 40, 9, 4] would have special treatment,
    and be converted as [CM, CD, XC, XL, IX, IV]. That is also why we are
    limited to a max of 3999, because 4000 would be "MMMM" 4 M in a raw,
    and won't be legitimate.
    And notably, Zero doesn't exists.

    Argument
    -----------
    rom_num (str): Roman Numeral String Positive Integer from 1 to 3999.
                   Usually Roman Numerals are Upper Cases, but here we accept
                   Lower Cases as well, it will be converted into upper cases.

    Return
    --------
    int: If the process succeed, the translated integer will be returned,
         comprised in a range between 1, and 3999.
    str: In any errors a Message will be delivered.

    A good website reference, to explain how Roman Numerals works:
    https://all-about-roman-numerals.com/

    __Developper's Notes__:
        I am well aware this is not the most mathematical, nor the most
        optimized process to translate a Roman Numeral into modern numbers.
        Recreating the dictionary, and storing the entire 3999 numbers in
        memory, can have LOTS of disadvantages (For Massive Implementations).
        But considering we operate in a finite range of allowed numbers (rules
        are rules), and that this is the easiest way to implement it.
        This is still a work in process for more mathematical/optimized
        wizardry.
        However, with today's technology (CPU speed, and RAM capacities), and
        considering that statistically this function won't be use at massive
        scale or frequency... I believe it's still a valid algorithm.
    '''
    rom_dict = {roman_convert(n): n for n in range(1, 4000)}
    if type(rom_num) is not str or rom_num.upper() not in rom_dict:
        return f"Out of range [1, 3999], or this is not a Roman Numeral,\
or is not a string:\t{rom_num}\t{type(rom_num)}"
    else:
        return rom_dict[rom_num.upper()]


# Testing & Illustration (proof of concept)
# A few Exemples:
test_rom_num = ["TEST", 123, "123", "MMXXII", 'mmxxii', 'III', 'VIII', 'XII',
                "XXXVII", "LXXXII", "CCCLIII", "XVIII", "LXI", "DCXXXII",
                "MMVI", "MMMM", "MMMCMXCIX"]
for m in test_rom_num:
    print(m, ':\t', roman_translate(m))

# Expected output
# TEST :   out of range - this text is not a Roman Numeral
# 123 :    out of range - This is an INT, not a str
# 123 :    out of range - This STR is composed of digits, not RomanNumerals
# MMXXII :     2022
# mmxxii :     2022
# III :    3
# VIII :   8
# XII :    12
# XXXVII :     37
# LXXXII :     82
# CCCLIII :    353
# XVIII :  18
# LXI :    61
# DCXXXII :    632
# MMVI :   2006
# MMMM :   out of range -> 'MMMM' = 4 x 1000 = 4000 out of range 1 to 3999
# MMMCMXCIX :  3999

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
