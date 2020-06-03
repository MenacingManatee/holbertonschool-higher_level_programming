#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0
    with open(filename) as f:
        e = f.read()
        for i in e:
            if i == '\n':
                count += 1
    return count
