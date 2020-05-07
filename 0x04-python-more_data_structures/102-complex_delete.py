#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return (a_dictionary)
    for key in list(a_dictionary):
        if (a_dictionary.get(key) == value):
            a_dictionary.pop(key)
    return (a_dictionary)
