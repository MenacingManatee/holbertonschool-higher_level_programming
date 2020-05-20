#!/usr/bin/python3

'''Square class'''


class Square:
    '''Initialize a square class with size and area
Size has a getter and setter function'''
    __size = 0

    def area(self):
        '''Returns the area of the square'''
        return (self.__size ** 2)

    def __init__(self, size=0):
        '''Initializes size'''
        self.__size = size

    @property
    def size(self):
        '''Returns size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Sets/resets size, with error raised on bad value'''
        if (type(value) is int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        '''Prints out a visual representation of square
        using string.join() method and list comprehension'''
        if self.__size is 0:
            print()
        print("".join(['#' * self.__size + '\n' for i in range(self.__size)]),
              end="")
