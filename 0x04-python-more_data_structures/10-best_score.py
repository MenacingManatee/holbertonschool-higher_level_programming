#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary == None):
        return (None)
    keys = a_dictionary.keys()
    res = 0
    for key in keys:
        if (a_dictionary[key] > res):
            res = a_dictionary[key]
            keyRes = key
    return (keyRes)
