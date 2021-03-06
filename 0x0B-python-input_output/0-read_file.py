#!/usr/bin/python3
'''defines a function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''usage: read_file(filename="")'''
    with open(filename) as f:
        print(f.read(), end="")
    f.close()
