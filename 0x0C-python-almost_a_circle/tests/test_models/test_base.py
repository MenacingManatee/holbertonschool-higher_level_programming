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

    def test_pep8(self):
        '''Test for conformation to pep8'''
        import pep8
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py', 'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


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

    def test_doc_15(self):
        '''Tests documentation for to_json_string() method'''
        self.assertTrue(Rectangle.to_json_string.__doc__ is not None)


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

    def test_doc_16(self):
        '''Tests documentation for save_to_file() method'''
        self.assertTrue(Rectangle.save_to_file.__doc__ is not None)


class test_Base_17(unittest.TestCase):
    '''Test the from_json_string method added in task 17'''
    def test_17_method_doc(self):
        '''Tests the documentation for added method'''
        self.assertTrue(Base.from_json_string.__doc__ is not None)

    def test_basic_functionality_17(self):
        '''Basic test for the method'''
        inp = [{'id': 89, 'width': 10, 'height': 4}]
        json_inp = Rectangle.to_json_string(inp)
        list_out = Rectangle.from_json_string(json_inp)
        self.assertTrue(type(list_out) is list)
        self.assertTrue(type(list_out[0]) is dict)
        self.assertTrue(list_out == inp)


class test_Base_18(unittest.TestCase):
    '''Test the create method added in task 18'''
    def test_create_doc(self):
        '''Tests the documentation of create() method'''
        self.assertTrue(Base.create.__doc__ is not None)

    def test_create_simple(self):
        '''Simple functionality test'''
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)
        self.assertTrue(r1.__str__() == r2.__str__())


class test_Base_19(unittest.TestCase):
    '''tests the load_from_file() method added in task 19'''
    def test_19_method_doc(self):
        '''Tests the documentation of the method'''
        self.assertTrue(Base.load_from_file.__doc__ is not None)


class test_Base_20(unittest.TestCase):
    '''Tests the save_to_file() method added in task 20'''
    def test_20_method_doc(self):
        self.assertTrue(Base.save_to_file_csv.__doc__ is not None)
