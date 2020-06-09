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

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        from models.rectangle import Rectangle
        from models.square import Square
        if "size" in dictionary.keys():
            res = Square(1)
        elif "width" in dictionary.keys():
            res = Rectangle(1, 1)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        try:
            with open(str(cls.__name__) + '.json', "r") as f:
                import json
                tmp = json.loads(f.read())
                res = []
                for item in tmp:
                    res.append(cls.create(**item))
                return res
        except OSError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Serializes an object inherited from Base in CSV'''
        if cls.__name__ == "Rectangle":
            ordr = ["id", "width", "height", "x", "y"]
        else:
            ordr = ["id", "size", "x", "y"]
        with open(str(cls.__name__) + '.json', "w") as csvf:
            import csv
            w = csv.DictWriter(csvf, fieldnames=ordr)
            for item in list_objs:
                w.writerow(item.to_dictionary())
            csvf.close()

    @classmethod
    def load_from_file_csv(cls):
        '''Deserializes an objest inherited from Base in CSV'''
        if cls.__name__ == "Rectangle":
            ordr = ["id", "width", "height", "x", "y"]
        else:
            ordr = ["id", "size", "x", "y"]
        with open(str(cls.__name__) + '.json', "r") as csvf:
            import csv
            r = csv.DictReader(csvf, fieldnames=ordr)
            tmp = {}
            tmp2 = []
            for row in r:
                tmp.update(row)
                tmp2.append(tmp.copy())
                tmp.clear()
            tmp2 = [dict([key, int(value)] for key, value in dicts.items())
                    for dicts in tmp2]
            res = []
            for item in tmp2:
                res.append(cls.create(**item))
            csvf.close()
            return res
