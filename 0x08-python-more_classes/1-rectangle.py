#!/usr/bin/python3
'''Module defines a rectangle class'''


class Rectangle:
    '''Defines a rectangle based on width and height'''
    def __init__(self, width=0, height=0):
        '''Initialization for class'''
        self.width = width
        self.height = height

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        if (not isinstance(value, int) or value != value or value ==
                float("inf")):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        if (not isinstance(value, int) or value != value or value ==
                float("inf")):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
