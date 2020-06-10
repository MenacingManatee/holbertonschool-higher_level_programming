#!/usr/bin/python3
'''Defines multiple tests and test cases for the square class'''
import models.square as s
import unittest
Square = s.Square


class test_square_10(unittest.TestCase):
    '''Defines multiple test cases for the square class added in task 10'''
    def test_square_modDoc(self):
        '''Tests for module documentation'''
        self.assertTrue(s.__doc__ is not None)

    def test_square_doc(self):
        '''Tests for documentation in the square class'''
        self.assertTrue(Square.__doc__ is not None)

    def test_square_funcDoc(self):
        '''Tests for documentation in init and str'''
        self.assertTrue(Square.__init__.__doc__ is not None and
                        Square.__str__.__doc__ is not None)


class test_square_11(unittest.TestCase):
    '''Tests for the size getter and setter'''
    def test_size_doc(self):
        '''Tests for documentation in the size getter and setter'''
        self.assertTrue(Square.size.__doc__ is not None)

    def test_size_good(self):
        '''Tests for a good size being sent to square'''
        s1 = Square(5)
        self.assertTrue(s1.size == 5)
        s1.size = 10
        self.assertTrue(s1.size == 10)

    def test_size_bad(self):
        '''Tests for a bad size being sent to square'''
        s1 = Square(5)
        with self.assertRaises(ValueError) as e:
            s1.size = -1
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_size_str(self):
        '''Tests for sending a non-integer size'''
        s1 = Square(5)
        with self.assertRaises(TypeError) as e:
            s1.size = "1"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_nan_inf(self):
        '''Tests for sending nan and inf as the size'''
        s1 = Square(5)
        with self.assertRaises(TypeError) as e:
            s1.size = (float("NaN"))
        with self.assertRaises(TypeError) as e:
            s1.size = (float("inf"))


class test_square_12(unittest.TestCase):
    '''Tests the update method added in task 12'''
    def test_update_doc(self):
        '''Tests the documentation of the update method'''
        self.assertTrue(Square.update.__doc__ is not None)

    def test_functionality_args(self):
        '''Tests the basic functionality using args'''
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_functionality_kwargs(self):
        '''Tests the basic functionality using kwargs'''
        s1 = Square(5)
        s1.update(id=1, size=2, x=3, y=4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_functionaluty_args_and_kwargs(self):
        '''Tests basic functionality when both args and kwargs are sent'''
        s1 = Square(5)
        s1.update(89, id=99)
        self.assertTrue(s1.id == 89)

    def test_none(self):
        '''Tests when nothing is sent'''
        s1 = Square(5)
        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (20) 0/0 - 5")


class test_square_14(unittest.TestCase):
    '''Tests the to_dictionary() method added in task 14'''
    def test_14_method_doc(self):
        '''Tests the documentation for the method added'''
        self.assertTrue(Square.to_dictionary.__doc__ is not None)

    def test_different_rect(self):
        '''Tests to make sure the dict has size, and not width or height'''
        s1 = Square(1, 1, 1, 1)
        d = s1.to_dictionary()
        self.assertTrue('height' not in d and 'weight' not in d and
                        'size' in d)
