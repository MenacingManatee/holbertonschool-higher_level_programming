#!/usr/bin/python3
'''Defines a function that returns the number of lines of a text file'''


def number_of_lines(filename=""):
    '''Usage: number_of_lines(filename="")'''
    count = 0
    with open(filename) as f:
        e = f.read()
        for i in e:
            if i == '\n':
                count += 1
    f.close()
    return count
