#!/usr/bin/python3
'''Test for Base class'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''test base class'''

    def test_default_id_assignment(self):
        '''test to check if ID attribute is auto increamented correctly'''
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id_assignment(self):
        '''test id attribute with custom assignment'''
        obj3 = Base(100)
        self.assertEqual(obj3.id, 100)

    def test_mixed_id_assignment(self):
        '''Mixed ID Assignment Test'''
        obj5 = Base()
        obj6 = Base(200)
        obj7 = Base()
        self.assertEqual(obj5.id, 3)
        self.assertEqual(obj6.id, 200)
        self.assertEqual(obj7.id, 4)

    if __name__ == "__main__":
        unittest.main()
