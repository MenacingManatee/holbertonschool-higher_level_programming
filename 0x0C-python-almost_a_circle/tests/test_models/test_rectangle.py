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

    def test_valid_doc(self):
        '''Tests for documentation in the integer validator'''
        self.assertTrue(Rectangle.integer_validator.__doc__ is not None)


class test_rectangle_4(unittest.TestCase):
    '''Tests the area() public method added in task 4'''
    def test_area_1(self):
        '''Tests the area of a small rectangle'''
        r1 = Rectangle(3, 6, 0, 0, 0)
        self.assertEqual(r1.area(), 18)
        r1.height = 10
        self.assertEqual(r1.area(), 30)

    def test_area_2(self):
        '''Tests the area of a large rectangle'''
        r1 = Rectangle(9223372036854775807, 9223372036854775807, 0, 0, 0)
        self.assertEqual(r1.area(), 9223372036854775807 ** 2)

    def test_area_doc(self):
        '''Tests documentation for area() method'''
        self.assertTrue(Rectangle.area.__doc__ is not None)


class test_rectangle_6(unittest.TestCase):
    '''Tests the __str__ dunder method overridden in task 6'''
    def test_str(self):
        '''Tests the __str__ method'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_2(self):
        '''Tests the __str__ method'''
        r1 = Rectangle(5, 5, 1, 0, 0)
        self.assertEqual(r1.__str__(), "[Rectangle] (0) 1/0 - 5/5")

    def test_str_doc(self):
        '''Tests the __str__ documentaion'''
        self.assertTrue(Rectangle.__str__.__doc__ is not None)


class test_rectangle_7(unittest.TestCase):
    '''Tests the display method added in task 7'''
    def test_display_doc(self):
        '''Tests the documentation of the display method'''
        self.assertTrue(Rectangle.display.__doc__ is not None)

    def test_display_simple(self):
        '''Tests the display() method with a 1x1 rectangle'''
        r1 = Rectangle(1, 1, 0, 0, 1)
        import sys
        from io import StringIO
        from unittest.mock import patch
        with patch('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue().strip(), "#")

    def test_display_larger(self):
        '''tests the display() method with a larger rectangle'''
        r1 = Rectangle(3, 2, 0, 0, 1)
        import sys
        from io import StringIO
        from unittest.mock import patch
        with patch('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue().strip(), '###\n###')

    def test_rectangle_position(self):
        '''Tests the position in the display() method'''
        r1 = Rectangle(2, 3, 2, 2, 1)
        import sys
        from io import StringIO
        from unittest.mock import patch
        with patch('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(),
                             '\n\n  ##\n  ##\n  ##\n')


class test_rectangle_8(unittest.TestCase):
    '''Tests the update() method, ensuring values are correctly updated and
    sent to the propper setter functions'''
    def test_update(self):
        '''Basic test for update method'''
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", r1.__str__())
        r1.update(1)
        self.assertTrue(r1.id == 1)
        r1.update(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", r1.__str__())

    def test_update_fail(self):
        '''Tests an update that should fail'''
        r1 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(ValueError) as e:
            r1.update(1, 0)

    def test_update_none(self):
        '''Tests the update method if no arguments are sent'''
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update()

    def test_update_doc(self):
        '''Tests the documentation for update() method'''
        self.assertTrue(Rectangle.update.__doc__ is not None)


class test_rectangle_9(unittest.TestCase):
    '''Tests for the kwargs added to update method in task 9'''
    def test_kwargs(self):
        '''Basic test to ensure kwargs functionality'''
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertTrue(r1.x == 10)
        r1.update(x=2)
        self.assertTrue(r1.x == 2)

    def test_all_kwargs(self):
        '''Tests all kwargs in update'''
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_args_kwargs(self):
        '''Tests kwargs in update when args also sent'''
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1, x=2)
        self.assertTrue(r1.id == 1)
        self.assertTrue(r1.x == 10)
