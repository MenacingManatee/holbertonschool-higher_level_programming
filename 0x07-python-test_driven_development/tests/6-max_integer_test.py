#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Unit test cases for max_integer'''
    def test_doctest1(self):
        '''Check for module docstring'''
        self.assertIsNotNone(__import__('6-max_integer').__doc__)

    def test_doctest2(self):
        '''Check for function docstring'''
        self.assertIsNotNone(max_integer.__doc__)

    def test_basic(self):
        '''A simple test to ensure basic functionality'''
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

    def test_empty(self):
        '''A test with no arguments sent'''
        self.assertEqual(max_integer([]), None)

    def test_massive(self):
        '''a test with a very large number'''
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                      13, 15, 16, 17, 18, 19, 20,
                                      9223372036854775807]),
                         9223372036854775807)

    def test_negative(self):
        '''A test with all negative numbers'''
        self.assertEqual(max_integer([-1, -99, -9223372036854775800,
                                      -9999999]), -1)

    def test_max_first(self):
        '''A test where the max integer is the first number'''
        self.assertEqual(max_integer([5, 4, -1, 2, 0]), 5)

    def test_copy(self):
        '''A test with multiple copies of the same int'''
        self.assertEqual(max_integer([1, 1, 1, 1, 1, 1, 1]), 1)

    def test_pos_and_neg(self):
        '''A test with a mix of positive and negative ints'''
        self.assertEqual(max_integer([1, -1, 9, -9, 99, -99, 1027, -2048]),
                         1027)

    def test_floats(self):
        '''A test using floats instead of ints'''
        self.assertEqual(max_integer([1.1, 3.3, 5.5, 9.6, 7.2]), 9.6)

    def test_ints_and_floats(self):
        '''A test with a mix of ints and floats'''
        self.assertEqual(max_integer([1, 2.2, 3, 4.4, 5, 6.6, 7, 8.8]), 8.8)

    def test_tiny_floats(self):
        '''A test using very small floats'''
        self.assertEqual(max_integer([0.1, 0.00001, 0.00000000001, 0.0000002]),
                         0.1)

if __name__ == '__main__':
    unittest.main()
