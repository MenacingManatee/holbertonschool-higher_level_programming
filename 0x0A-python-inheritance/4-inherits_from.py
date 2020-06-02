#!/usr/bin/python3
'''Finds f the object is an instance of a class that inherited 
(directly or indirectly) from the specified class
'''


def inherits_from(obj, a_class):
    '''Usage: inherits_from(obj, class)'''
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
