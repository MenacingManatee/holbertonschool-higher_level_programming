#!/usr/bin/python3
'''defines the class Square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Defines a square as a special rectangle with width and height being equal
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes a square as a special rectangle'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string description of the square'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Defines a method that assigns attributes'''
        if len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.width = kwargs.get('size')
                self.height = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
            return
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        res = {}
        res.update({"id": self.id})
        res.update({"size": self.size})
        res.update({"x": self.x})
        res.update({"y": self.y})
        return res
