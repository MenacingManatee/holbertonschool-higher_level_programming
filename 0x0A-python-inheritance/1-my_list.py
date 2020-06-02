#!/usr/bin/python3
'''Defines a class MyList that inherits from list'''


class MyList(list):
    ''' Defines a class that add a sorted print to list'''

    def print_sorted(self):
        '''Prints a sorted list'''
        tmp = self.copy()
        tmp.sort()
        print(tmp)
