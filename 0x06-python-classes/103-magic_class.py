#!/usr/bin/python3
'''Magic class'''
import math


class MagicClass:
    '''Defines a class with area, circumference, radius of circle'''
    def __init__(self, radius=0):
        '''initializes radius'''
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''Getter for area'''
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        '''getter for circumference'''
        return (2 * math.pi * self.__radius)
