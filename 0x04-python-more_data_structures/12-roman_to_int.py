#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    res, i = 0, 0
    romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
              'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}

    while i < len(roman_string):
        if roman_string[i] not in romans:
            res = 0
            break
        elif i + 2 <= len(roman_string) and roman_string[i:i+2] in romans:
            res += romans[roman_string[i:i+2]]
            i += 1
        else:
            res += romans[roman_string[i]]
        i += 1

    return res
