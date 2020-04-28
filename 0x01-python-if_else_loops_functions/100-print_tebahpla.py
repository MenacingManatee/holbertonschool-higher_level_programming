#!/usr/bin/python3
j = 0
for i in range(ord("z"), ord("a") - 1, -1):
    asc = i
    if j % 2 == 1:
        asc -= (ord("a") - ord("A"))
    j += 1
    print("{}".format(chr(asc)), end="")
