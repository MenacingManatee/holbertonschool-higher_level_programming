#!/usr/bin/python3
import hidden_4
d = dir(hidden_4)
for i in range(len(d)):
    if d[i][0] != '_':
        print("{}".format(d[i]))
