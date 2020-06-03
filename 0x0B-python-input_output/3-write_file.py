#!/usr/bin/python3
'''Defines a function that writes a string to a text file (UTF8)
 and returns the number of characters written:'''


def write_file(filename="", text=""):
    '''Usage: write_file(filename="", text="")'''
    with open(filename, "w") as f:
        f.write(text)
    f.close()
    return len(text)
