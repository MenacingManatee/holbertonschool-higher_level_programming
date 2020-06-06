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
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        r3 = Rectangle(1, 1)
        self.assertTrue(r1.id == 6)
        self.assertTrue(r2.id == 7)
        self.assertTrue(r3.id == 8)

    def test_id_manual(self):
        '''Tests manual assignment of IDs'''
        r1 = Rectangle(1, 1, 1, 1, 0)
        r2 = Rectangle(1, 1, 1, 1, 100)
        self.assertTrue(r1.id == 0 and r2.id == 100)

    def test_attributes(self):
        '''Tests that attributes are set and returned correctly'''
        r1 = Rectangle(1, 3, 5, 7, 101)
        self.assertTrue(r1.width == 1 and r1.height == 3 and r1.x == 5 and
                        r1.y == 7)

    def test_change_attrs(self):
        '''Tests that attributes are changed correctly'''
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.width = 100
        self.assertTrue(r1.width == 100)


class test_rectangle_3(unittest.TestCase):
    '''Defines test cases for the changes to rectangle made in task 3'''
    def test_exception_type(self):
        '''Tests to make sure typeerror is raised on various wrong types
        Also tests the error message when raised'''
        with self.assertRaises(TypeError) as e:
            Rectangle(1, '3')
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(float("inf"), 3)
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 3, float("NaN"), 0)
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 3, 0, 0.1)
        self.assertEqual('y must be an integer', str(e.exception))

    def test_exception_val(self):
        '''Tests for value error with message'''
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 0, 0, 0, 0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 1, -1, 0, 0)
        self.assertEqual('x must be >= 0', str(e.exception))
