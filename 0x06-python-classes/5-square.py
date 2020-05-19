#!/usr/bin/python3
class Square:
    __size = 0
    def area(self):
        return (self.__size ** 2)

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) is int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)
        if (self.__size == 0):
            print("")
