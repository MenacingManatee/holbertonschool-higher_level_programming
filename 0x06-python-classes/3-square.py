#!/usr/bin/python3
class Square:
    __size = 0
    area = 0
    def area(self):
        self.area = self.__size ** 2
        return (self.area)
    def __init__(self, size=0):
        if (type(size) is int):
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
