#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        res = True
    except:
        res = False
    return (res)
