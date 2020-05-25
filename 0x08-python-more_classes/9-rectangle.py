#!/usr/bin/python3
'''Module defines a rectangle class'''


class Rectangle:
    '''Defines a rectangle based on width and height'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialization for class'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            res.append(str(self.print_symbol) * self.__width)
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
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if rect_1 is None or not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if rect_2 is None or not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
