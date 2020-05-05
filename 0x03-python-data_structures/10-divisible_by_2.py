#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list):
        res_list = []
        for i in range(len(my_list)):
            if (my_list[i] % 2 == 0):
                res_list.append(True)
            else:
                res_list.append(False)
        return (res_list)
