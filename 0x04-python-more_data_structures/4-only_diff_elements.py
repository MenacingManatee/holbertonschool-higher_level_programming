#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res_list = {}
    res_list = set_1 ^ set_2
    return (res_list)
