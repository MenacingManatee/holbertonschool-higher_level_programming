#!/usr/bin/python3
def islower(a):
    a = ord(a)
    if a > 96:
        return(a - (ord("a") - ord("A")))
    else:
        return(a)


def uppercase(s1):
    s1 = list(s1)
    for i in range(len(s1)):
        check = islower(s1[i])
        s1[i] = chr(check)
    print("".join(s1))
