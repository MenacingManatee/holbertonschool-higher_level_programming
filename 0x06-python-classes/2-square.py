#!/usr/bin/python3

'''Square class'''


class Square:
    '''Initialize a square with a checked size'''
    __size = 0

    def __init__(self, size=0):
        '''Initialize the value of size with errors raised on bad values'''
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
