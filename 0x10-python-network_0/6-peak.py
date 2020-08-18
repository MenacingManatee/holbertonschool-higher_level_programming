#!/usr/bin/python3
'''Finds a peak in an array'''


def find_peak(list_of_integers):
    '''Uses a binary search to find the peak'''
    arr = list_of_integers
    l = len(arr)
    num = int(l / 2)
    if l == 0:
        return None
    if l == 1:
        return arr[0]
    while True:
        tmp = arr[num]
        plus = num + 1
        minu = num - 1
        if plus > l:
            plus = 0
        if arr[minu] <= tmp:
            if arr[plus] <= tmp:
                return tmp
            else:
                num = int(num + ((l - num) / 2))
        else:
            num = int(num / 2)
