#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    keys = a_dictionary.keys()
    for key in keys:
        new_dict.update({key: a_dictionary.get(key) * 2})
    return (new_dict)
