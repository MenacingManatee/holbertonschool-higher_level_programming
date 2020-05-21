#!/usr/bin/python3
'''Prints a user-defined first and last name in the format:
My name is <first name> <last name>
Last name is not a required variable'''


def say_my_name(first_name, last_name=""):
    '''Usage: say_my_name(first_name, last_name="")'''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
