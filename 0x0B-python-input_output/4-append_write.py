#!/usr/bin/python3
'''Defines a function that appends a string to a text file (UTF8)
 and returns the number of characters written:'''


def append_write(filename="", text=""):
    '''Usage: append_write(filename="", text="")'''
    with open(filename, "a") as f:
        f.write(text)
    f.close()
    return len(text)
