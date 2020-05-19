#!/usr/bin/python3

'''Square class'''


class Square:
    '''Defines a square with size, area, and the ability to print'''
    __size = 0

    def area(self):
        '''Returns area of a square'''
        return (self.__size ** 2)

    def __init__(self, size=0):
        '''Initializes size'''
        self.__size = size

    @property
    def size(self):
        '''Getter for size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Setter for size'''
        if (type(value) is int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        '''Prints a square visually to the terminal'''
        for i in range(self.__size):
            print("#" * self.__size)
        if (self.__size == 0):
            print("")
