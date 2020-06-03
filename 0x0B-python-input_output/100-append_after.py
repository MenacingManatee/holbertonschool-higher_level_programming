#!/usr/bin/python3
'''Defines a function that inserts a line of text to a file,
 after each line containing a specific string'''


def append_after(filename="", search_string="", new_string=""):
    '''Usage: append_after(filename="", search_string="", new_string="")'''
    with open(filename, "r") as f:
        res = []
        s = f.readline()
        while (s != ""):
            res.append(s)
            if search_string in s:
                res.append(new_string)
            s = f.readline()
    f.close()
    with open(filename, "w") as f:
        f.write("".join(res))
    f.close()
