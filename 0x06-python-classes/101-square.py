#!/usr/bin/python3

'''Square class'''


class Square:
    '''Defines a class square with area, size, position, and the ability
to visually print. Returns a string of the visual square'''
    __size = 0

    def area(self):
        '''Area getter'''
        return (self.__size ** 2)

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes size and position'''
        self.position = position
        self.__size = size

    @property
    def size(self):
        '''size getter'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''size setter'''
        if (type(value) is int):
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        '''position getter'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''position setter'''
        if (isinstance(value, tuple) and len(value) is 2 and
                len([i for i in value if type(value) is tuple and i >= 0]) is
                2):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        '''prints a square visually at position to terminal'''
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            if (self.position[0] > 0):
                print(' ' * self.position[0], end="")
            print("#" * self.__size)
        if (self.__size == 0):
            print("")

    def strsqr(self):
        '''Returns a string representation of the square'''
        res = []
        if (self.__size is 0):
            res.append('\n')
            return ("".join(res))
        for i in range(self.__position[1]):
            res.append('\n')
        for i in range(self.__size):
            if (self.__position[0] > 0):
                res.append(' ' * self.__position[0])
            res.append('#' * self.__size)
            if (i != self.__size - 1):
                res.append('\n')
        return ("".join(res))

    def __repr__(self):
        '''Defines return value of Square class to be strsqr'''
        return (self.strsqr())
