#!/usr/bin/python3
def islower(a):
    a = ord(a)
    if a > 96:
        return(a - (ord("a") - ord("A")))
    else:
        return(a)


def uppercase(s1):
    s2 = list(s1)
    for i in range(len(s2)):
        check = islower(s2[i])
        s2[i] = chr(check)
        print("{:s}".format(s2[i]), end="")
    print("")
