#!/usr/bin/python3
'''Contains unit tests for the Base class module'''
import unittest
from models.base import Base


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
        self.assertTrue(b1.id == 4 and b2.id == 12 and b3.id == 89 and b4.id == 5)
