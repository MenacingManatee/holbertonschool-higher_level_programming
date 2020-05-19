#!/usr/bin/python3

'''Square class'''


class Square:
    '''Initialize a square with a size and area'''
    __size = 0
    area = 0

    def area(self):
        '''Returns the area of the square'''
        self.area = self.__size ** 2
        return (self.area)

    def __init__(self, size=0):
        '''Sets size, with errors raised on bad values'''
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
