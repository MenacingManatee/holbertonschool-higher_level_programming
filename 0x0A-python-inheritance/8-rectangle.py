#!/usr/bin/python3
'''Defines a class, BaseGeometry, that serves as a parent to rectangle
and provides a validator and area function (unimplemented)
Defines a class, Rectangle, that inherits from BaseGeometry
and has a width and height validated by integer_validator'''


class BaseGeometry():
    '''Defines public method area() that is not yet implemented'''
    def area(self):
        '''Not yet implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates that value is a valid integer'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    '''Defines a rectangle with a width and height'''
    def __init__(self, width, height):
        '''Initializes a rectangle with width and height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
