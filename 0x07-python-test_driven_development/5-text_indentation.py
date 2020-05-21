#!/usr/bin/python3
'''Prints a string, adding two newlines after each of the following:
'.', '?', and ':'
Text must be a string'''


def text_indentation(text):
    '''Usage: text_indentation(text)'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    flag = 0
    for char in text:
        if flag is 1 and char is ' ':
            continue
        print(char, end="")
        flag = 0
        if char in ['.', ':', '?']:
            print('\n')
            flag = 1
