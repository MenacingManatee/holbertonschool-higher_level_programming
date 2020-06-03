#!/usr/bin/python3
'''Defines a function that adds a new attribute to an object if possible'''


def add_attribute(obj, name, value):
    '''Usage: add_attribute(object, attribute_name, attribute_value)'''
    if ((hasattr(obj, '__slots__') and name in obj.__slots__) or
            hasattr(obj, '__dict__')):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
