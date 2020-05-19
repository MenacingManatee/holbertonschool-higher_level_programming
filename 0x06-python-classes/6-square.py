#!/usr/bin/python3

'''Square class'''


class Square:
    '''Defines a square class with the attributes size,
area, and position, with the ability to print the square visually'''
    __size = 0

    def area(self):
        '''Gets the area of the square'''
        return (self.__size ** 2)

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes values for size and position'''
        self.position = position
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

    @property
    def position(self):
        '''Getter for position'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''Setter for position'''
        if (isinstance(value, tuple) and len(value) is 2 and
                len([i for i in value if type(i) is int and i >= 0]) is 2):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        '''Prints a square visually at position provided'''
        if (self.__size is 0):
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            if (self.position[0] > 0):
                print(' ' * self.position[0], end="")
            print("#" * self.__size)
