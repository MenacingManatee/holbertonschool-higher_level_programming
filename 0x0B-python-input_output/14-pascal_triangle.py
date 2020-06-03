#!/usr/bin/python3
'''Defines a function that returns a list of lists of integers
 representing the Pascals triangle of n'''


def pascal_triangle(n):
    '''Usage: pascal_triangle(n)'''
    if n <= 0:
        return []
    res = []
    res.append([1])
    tmp = []
    for i in range(1, n):
        for j in range(i + 1):
            if j - 1 < 0:
                num = 0
            else:
                num = res[i - 1][j - 1]
            if j > i - 1:
                num += 0
            else:
                num += res[i - 1][j]
            tmp.append(num)
        res.append(tmp.copy())
        tmp.clear()
    return res
