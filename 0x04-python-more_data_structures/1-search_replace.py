#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res_list = my_list.copy()
    while search in res_list:
        x = res_list.index(search)
        res_list.remove(search)
        res_list.insert(x, replace)
    return (res_list)
