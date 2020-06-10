#!/usr/bin/python3
'''Contains unit tests for the Base class module'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_Base_1(unittest.TestCase):
    '''Defines tests for the Base class in task 1'''
    def test_doc_base(self):
        '''Checks the Base class for documentation'''
        self.assertTrue(Base.__doc__ is not None)

    def test_doc_init(self):
        '''tests Base.__init__ for documentation'''
        self.assertTrue(Base.__init__.__doc__ is not None)

    def test_id(self):
        '''tests for consecutive auto id assignments'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertTrue(b1.id == 1 and b2.id == 2 and b3.id == 3)

    def test_manual_id(self):
        '''Tests for manual id assignment. 4 and 5 for auto due to continuation
        of __nb_objects after previous test'''
        b1 = Base()
        b2 = Base(12)
        b3 = Base(89)
        b4 = Base(None)
        self.assertTrue(b1.id == 4 and b2.id == 12 and b3.id == 89 and
                        b4.id == 5)


class test_Base_15(unittest.TestCase):
    '''Tests for the dictionary to json string method defined in
    task 15'''
    def test_json_rep(self):
        '''Tests the return of the method'''
        r1 = Rectangle(10, 7, 2, 8, 1)
        self.assertTrue(r1.to_json_string(r1.to_dictionary()),
                        "[{\"x\": 2, \"width\": 10, \"id\": 1, \
                        \"height\": 7, \"y\": 8}]")

    def test_json_return_type(self):
        '''Tests the return type of the method'''
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertTrue(type(r1.to_json_string(r1.to_dictionary())) ==
                        str)

    def test_json_return_None(self):
        '''Tests for sending None'''
        self.assertEqual(Rectangle.to_json_string(None), '[]')

    def test_json_sent_nothing(self):
        '''Tests for sending no variables'''
        try:
            Rectangle.to_json_string()
        except TypeError as e:
            self.assertTrue(e is not None)


class test_Base_16(unittest.TestCase):
    '''tests for the class method def save_to_file(cls, list_objs):
    that writes the JSON string representation of list_objs to a file'''
    def test_rect(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json") as f:
            json = f.read()
            self.assertEqual(Rectangle.from_json_string(json),
                             [{"y": 1, "x": 1, "height": 1, "width": 1,
                               "id": 1}])
