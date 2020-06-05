#!/usr/bin/python3
'''Defines the class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Defines a rectangle by width, height, position, and ID'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes id, and calls setters of width, height, and pos'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''Getter for position x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        '''Validates integers for private values'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError('{} must be > 0'.format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
