#!/usr/bin/python3
'''Defines a function that creates an Object from a JSON file'''


def load_from_json_file(filename):
    '''Usage: load_from_json_file(filename)'''
    with open(filename) as f:
        import json
        r = f.read()
        return json.loads(r)
    f.close()
