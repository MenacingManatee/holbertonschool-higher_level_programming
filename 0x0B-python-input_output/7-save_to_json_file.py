#!/usr/bin/python3
'''Defines a function that writes an Object to a text file,
 using a JSON representation'''


def save_to_json_file(my_obj, filename):
    '''Usage: save_to_json_file(my_obj, filename)'''
    with open(filename, "w") as f:
        import json
        f.write(json.dumps(my_obj))
    f.close
