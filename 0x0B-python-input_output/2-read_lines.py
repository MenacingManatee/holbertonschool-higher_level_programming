#!/usr/bin/python3
'''defines a function that reads n lines of a text file
(UTF8) and prints it to stdout'''


def read_lines(filename="", nb_lines=0):
    '''Usage: read_lines(filename="", nb_lines=0)'''
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                e = f.readline()
                if e == "":
                    break
                print(e, end="")
    f.close()
