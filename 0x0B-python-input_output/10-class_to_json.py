#!/usr/bin/python3
'''Defines a function that returns the dictionary description with simple data
 structure (list, dictionary, string, integer and boolean)
 for JSON serialization of an object'''



def class_to_json(obj):
    '''Usage: class_to_json(obj)'''
    import json
    return json.dumps(obj.__dict__)
