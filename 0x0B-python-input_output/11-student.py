#!/usr/bin/python3
'''Defines a class Student that defines a student by:
first name, last name, age
Methods:
to_json that retrieves a dictionary representation of a Student instance'''


class Student:
    '''Definition for a student'''
    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.age = age
        self.last_name = last_name
        self.first_name = first_name


    def to_json(self):
        '''retrieves a dictionary representation of a Student instance '''
        import json
        d = json.dumps(self.__dict__)
        return json.loads(d)
