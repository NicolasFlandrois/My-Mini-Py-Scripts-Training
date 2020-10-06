#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Fri 24 July 2020 11:23:44
# Last Modified time: Fri 31 July 2020 17:07:49 

# Description:

# coding = zip(
#     [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
#     ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
# )

# # print(coding)
# # for d, r in coding:
# #     print('d', d)
# #     print('r', r)


# def decToRoman(num: int):
#     if num <= 0 or num >= 4000:
#         raise ValueError('Input should be an integer between 1 and 3999')
#     result = []
#     for d, r in coding:
#         while num >= d:
#             result.append(r)
#             num -= d
#     return ''.join(result)


# # for i in range(1, 4000):
#     # print(i, decToRoman(i))
# # for i in range(1, 10):
# #     print(decToRoman(i))
# # print(decToRoman(0))
# print(decToRoman(1))
# print(decToRoman(2))
# print(decToRoman(3))
# print(decToRoman(4))
# print(decToRoman(5))
# print(decToRoman(6))
# print(decToRoman(7))
# print(decToRoman(8))
# print(decToRoman(9))
# print(decToRoman(10))
# print(decToRoman(11))
# print(decToRoman(12))
# print(decToRoman(13))
# # print(decToRoman('A'))
###
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                num += roman[s[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[s[i]]
                i += 1
        return num


ob1 = Solution()
print(ob1.romanToInt("III"))
print(ob1.romanToInt("CDXLIII"))
###
# from collections import OrderedDict

def write_roman(num):

    # roman = OrderedDict()
    roman = {}
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


for i in range(1, 10):
    print(write_roman(i))
