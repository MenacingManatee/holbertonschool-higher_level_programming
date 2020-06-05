#!/usr/bin/python3
'''Defines a base class for all projects in this module'''


class Base:
    '''Defines the the id, based on the number of objects'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''initializes self.id based on the id sent, or number of objects'''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
