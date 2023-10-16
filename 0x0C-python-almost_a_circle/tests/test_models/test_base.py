#!/usr/bin/python3
''' base unittest'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_with_argument(self):
        # Test if the 'id' is correctly assigned when an argument is provided
        base_instance = Base(42)
        self.assertEqual(base_instance.id, 42)

    def test_id_without_argument(self):
        # Test if the 'id' is correctly assigned when no argument is provided
        base_instance_1 = Base()
        base_instance_2 = Base()
        self.assertEqual(base_instance_1.id, 1)
        self.assertEqual(base_instance_2.id, 2)


if __name__ == "__main__":
    unittest.main()
