#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list is None or len(my_list) == 0):
        return (0)
    total = 0
    scores = 0
    for tup in my_list:
        scores += tup[1]
    for tup in my_list:
        total += (tup[0] * (tup[1] / scores))
    return (total)
