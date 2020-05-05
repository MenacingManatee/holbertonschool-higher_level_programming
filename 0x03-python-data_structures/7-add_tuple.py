#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res_list = []
    for i in range(0, 2):
        if (len(tuple_a) <= i):
            num1 = 0
        else:
            num1 = tuple_a[i]
        if (len(tuple_b) <= i):
            num2 = 0
        else:
            num2 = tuple_b[i]
        res_list.append(num1 + num2)
    return (tuple(res_list))
