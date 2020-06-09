#!/usr/bin/python3
'''Defines a base class for all projects in this module'''


class Base:
    '''Defines the the id, based on the number of objects'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initializes self.id based on the id sent, or number of objects'''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        import json
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if list_objs is None or list_objs[0] is None:
            t = list_objs.__class__.__name__
            if list_objs is not None:
                t = list_objs[0].__class__.__name__
            l = []
        elif len(list_objs) > 0:
            t = list_objs[0].__class__.__name__
            l = []
            for item in list_objs:
                l.append(item.to_dictionary())
        res = "["
        count = 0
        with open(t + '.json', "w") as f:
            for item in l:
                if count != 0:
                    res = res + ', '
                count += 1
                res = res + Base.to_json_string(item)
            res = res + ']'
            f.write(res)
            f.close()

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
