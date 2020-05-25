#!/usr/bin/python3
'''Prints a square in a visual format using
the '#' symbol
Example: print_square(2)
##
##
'''


def print_square(size):
    '''Usage: print_square(size)'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise TypeError('size must be >= 0')
    elif size is 0:
        print("", end="")
    else:
        print("".join(['#' * size + '\n' for i in range(size)]), end="")
