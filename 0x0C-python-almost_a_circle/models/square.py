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
