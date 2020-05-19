#!/usr/bin/python3

'''Square class'''


class Square:
    '''Defines a square class with logical operators available based on area,
as well as size and area'''
    __size = 0

    def area(self):
        '''area getter'''
        return (self.__size ** 2)

    def __init__(self, size=0):
        '''Initializes size'''
        self.__size = size

    @property
    def size(self):
        '''size getter'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''size setter'''
        if (type(value) is int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def __eq__(self, other):
        '''Sets __eq__ to check area'''
        return (self.area() == other.area())

    def __lt__(self, other):
        '''Sets __lt__ to check area'''
        return (self.area() < other.area())

    def __gt__(self, other):
        '''Sets __gt__ to check area'''
        return (self.area() > other.area())

    def __ne__(self, other):
        '''Sets __ne__ to check area'''
        return (not (self.area() == other.area()))

    def __le__(self, other):
        '''Sets __le__ to check area'''
        return (self.area() <= other.area())

    def __ge__(self, other):
        '''Sets __ge__ to check area'''
        return (self.area() >= other.area())
