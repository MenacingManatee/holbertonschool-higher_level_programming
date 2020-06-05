#!/usr/bin/python3
'''Module used to test the rectangle class'''
import unittest
import models.rectangle as r
Rectangle = r.Rectangle


class test_rectangle_2(unittest.TestCase):
    '''Test cases for the rectangle requirements of task 2'''
    def test_moduleDoc(self):
        '''Test for module documentation'''
        self.assertTrue(r.__doc__ is not None)

    def test_classDoc(self):
        '''Test for class documentation'''
        self.assertTrue(r.Rectangle.__doc__ is not None)

    def test_funcDoc(self):
        '''Tests for function documentation'''
        self.assertTrue(r.Rectangle.__init__.__doc__ is not None and
                        r.Rectangle.width.__doc__ is not None and
                        r.Rectangle.height.__doc__ is not None and
                        r.Rectangle.x.__doc__ is not None and
                        r.Rectangle.y.__doc__ is not None)

    def test_id_auto(self):
        '''Tests automatic assignment of IDs
        Starts at 6 due to 1-5 being used in Base tests'''
        r1 = Rectangle(0, 0)
        r2 = Rectangle(0, 0)
        r3 = Rectangle(0, 0)
        self.assertTrue(r1.id == 6)
        self.assertTrue(r2.id == 7)
        self.assertTrue(r3.id == 8)

    def test_id_manual(self):
        '''Tests manual assignment of IDs'''
        r1 = Rectangle(0, 0, 0, 0, 0)
        r2 = Rectangle(0, 0, 0, 0, 100)
        self.assertTrue(r1.id == 0 and r2.id == 100)

    def test_attributes(self):
        '''Tests that attributes are set and returned correctly'''
        r1 = Rectangle(1, 3, 5, 7, 101)
        self.assertTrue(r1.width == 1 and r1.height == 3 and r1.x == 5 and
                        r1.y == 7)

    def test_change_attrs(self):
        '''Tests that attributes are changed correctly'''
        r1 = Rectangle(0, 0, 0, 0, 1)
        r1.width = 100
        self.assertTrue(r1.width == 100)
