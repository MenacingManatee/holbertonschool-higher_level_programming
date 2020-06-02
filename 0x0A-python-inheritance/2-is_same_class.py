#!/usr/bin/python3
'''Finds if the object is exactly an instance of the specified class'''


def is_same_class(obj, a_class):
    '''Usage: is_same_class(obj, class)'''
    return type(obj) is a_class
