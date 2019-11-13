def baseN(num, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // base, base, numerals).lstrip(numerals[0]) + numerals[num % base])


for n in range(40):
    print(baseN(n, 36))
