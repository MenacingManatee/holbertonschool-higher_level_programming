#!/usr/bin/python3
'''Module describes a child of int that reverses '!=' and '==' '''


class MyInt(int):
    '''Class reverses the != and == operators of int'''

    def __eq__(self, other):
        '''defines the eq operator as !='''
        return int(self) != other

    def __ne__(self, other):
        '''defines the ne operator as =='''
        return int(self) == other
