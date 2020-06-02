#!/usr/bin/python3
'''Defines an empty class, BaseGeometry'''


class BaseGeometry():
    '''Defines public method area() that is not yet implemented'''
    def area(self):
        '''Not yet implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
