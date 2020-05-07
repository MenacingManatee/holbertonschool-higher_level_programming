#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    sum = 0
    for i in range(len(my_list)):
        if (my_list[i] not in uniq_list):
            sum += my_list[i]
            uniq_list.append(my_list[i])
    return (sum)
