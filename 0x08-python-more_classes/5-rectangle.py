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

    def area(self):
        '''Function that finds the area of a rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Function that finds the perimeter of a rectangle'''
        if (self.__height is 0 or self.__width is 0):
            return 0
        return ((2 * self.__height) + (2 * self.__width))

    def str_rep(self):
        '''Creates a string representation to be printed by other functions'''
        res = []
        for i in range(self.__height):
            res.append('#' * self.__width)
            if i != self.__height - 1:
                res.append('\n')
        return ("".join(res))

    def __str__(self):
        '''Defines the return value if a string is requested'''
        return self.str_rep()

    def __repr__(self):
        '''Returns a string telling eval to make a new rectangle'''
        return ("Rectangle(" + str(self.__width) + ', ' + str(self.__height) +
            ')')

    def __del__(self):
        '''Alerts user when a rectangle is deleted'''
        print("Bye rectangle...")
