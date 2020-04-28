#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if j > i and j * i != 8 * 9:
            print("{}{}".format(i, j), end=", ")
        elif j * i == 8 * 9:
            print("{}{}".format(i, j))
