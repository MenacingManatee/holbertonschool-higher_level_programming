#!/usr/bin/python3
import math
'''Magic class'''


class MagicClass:
    '''Defines a class that includes the radius, area, etc of a circle'''
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
