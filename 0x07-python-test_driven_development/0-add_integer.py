#!/usr/bin/python3
'''Adds two integers
   If floats are sent, casts to int before adding'''


def add_integer(a, b=98):
    '''Usage: add_integer(a, b=98)'''
    if (a == float("inf") or (not isinstance(a, int) and not
                              isinstance(a, float)) or a != a):
        raise TypeError('a must be an integer')
    elif (b == float("inf") or (not isinstance(b, int) and not
                                isinstance(b, float)) or b != b or
            b is float("inf")):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
