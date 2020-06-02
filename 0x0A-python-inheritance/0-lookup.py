#!/usr/bin/python3
'''Defines a function lookup that finds and returns a list of
available attributes and methods for an object'''


def lookup(obj):
    '''Usage: lookup(obj)'''
    return(dir(obj))
