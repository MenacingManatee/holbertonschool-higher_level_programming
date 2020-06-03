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


    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance '''
        if type(attrs) == list:
            flag = 0
            for i in attrs:
                if type(i) != str:
                    flag = 1
            if flag == 0:
                res = {}
                for i in self.__dict__:
                    if i in attrs:
                        res.update({i: self.__dict__[i]})
                return res
        return self.__dict__
