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

    def __eq__(self, other):
        return (self.area() == other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ne__(self, other):
        return (not (self.area() == other.area()))

    def __le__(self, other):
        return (self.area() <= other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())
