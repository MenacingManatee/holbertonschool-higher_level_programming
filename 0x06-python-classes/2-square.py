#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0):
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
