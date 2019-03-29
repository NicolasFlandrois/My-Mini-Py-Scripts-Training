#!#!usr/bin/python3

#################################################################################
# MIT License
#
# Copyright (c) 2019 - Nicolas Flandrois
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

#Thu 10 Jan 2019 12:42:24 PM CET - Stradate 96627.31 (STO)
#Author: Nicolas Flandrois
#Description: Generatin a list of random words, according to length chosen, from an import of words in a text.
#Version: v1.0

import random
liste = []
with open('text.txt') as f:
	liste = list(set(item.lower() for item in [
		word for line in f for word in line.split()]))
secure_random = random.SystemRandom()
pw =[]
n = int(input("n? "))
for i in range(n):
	pw.append(secure_random.choice(liste))

print("pw: ", pw)

#Still to do: Filter and remove none ASCII letters and numbers from source list imported from .txt... Or! Shall we keep it to create special caracters inclusion in passwords?
#Also can transfer the list back into a string for easier readings
