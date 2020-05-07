#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) is not str):
        return (0)
    sum = 0
    for i in range(len(roman_string)):
        num = roman_string[i]
        if (num is 'M'):
            sum += 1000
        elif (num is 'D'):
            sum += 500
        elif (num is 'C'):
            sum += 100
        elif (num is 'L'):
            sum += 50
        elif (num is 'X'):
            sum += 10
        elif (num is 'V'):
            sum += 5
        else:
            sum += 1
    return (sum)
