#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) is not str):
        return (0)
    numerals = {'M': 1000, 'D': 500, 'C': 100,
                'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sm = 0
    for i in range(len(roman_string)):
        num = roman_string[i]
        if (num in numerals):
            if (i + 1 < len(roman_string) and
                numerals.get(roman_string[i + 1]) >
                    numerals.get(roman_string[i])):
                sm -= numerals.get(roman_string[i])
            else:
                sm += numerals.get(roman_string[i])
    return (sm)
