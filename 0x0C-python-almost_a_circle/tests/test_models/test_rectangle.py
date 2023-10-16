#!/usr/bin/python3
'''Rectangle test'''


from unittest import TestCase, mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_area_1(self):
        """ Test area """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 2 * 3)
        self.assertEqual(r2.area(), 2 * 10)
        self.assertEqual(r3.area(), 8 * 7)

    def test_area_2(self):
        """ Checking the return value of area method """
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)
        r1.width = 5
        self.assertEqual(r1.area(), 10)
        r1.height = 5
        self.assertEqual(r1.area(), 25)

    def test_area_no_args(self):
        """ Test area method with no arguments """
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_print(self):
        expected = "[Rectangle] (42) 1/3 - 2/4"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            print(Rectangle(2, 4, 1, 3, 42), end='')
            self.assertEqual(output.getvalue(), expected)

    def test_str_str_method(self):
        expected = "[Rectangle] (98) 3/1 - 4/2"
        self.assertEqual(Rectangle(4, 2, 3, 1, 98).__str__(), expected)

    def test_str_str(self):
        expected = "[Rectangle] (1) 0/0 - 4/4"
        self.assertEqual(str(Rectangle(4, 4)), expected)

    def test_str_str_method_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).__str__(42)

class Test_Rectangle_update_with_kwargs(TestCase):
    '''Test cases for Rectangle's update with **kwargs method.'''

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_kwargs_none_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(id=None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def test_update_kwargs_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def test_update_kwargs_id_width(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=40, width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def test_update_kwargs_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, width=10, id=10, x=10, height=10, betty="holberton")
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_mixed_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, width=10, betty="holberton", id=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_args_before(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(42, 42, 42, y=10, x=10)
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 42/42")

    def test_update_kwargs_not_all_mixed(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (42) 10/10 - 2/10")

    def test_update_kwargs_only_wrong_keys(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(betty="holberton", holberton="betty")
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")

    def test_to_dictionary_basic(self):
        r = Rectangle(2, 4, 1, 2, 42)
        expected = {'width': 2, 'height': 4, 'x': 1, 'y': 2, 'id': 42}
        self.assertDictEqual(r.to_dictionary(), expected)

    def test_to_dictionary_basic_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 1, 2, 42).to_dictionary(42)


if __name__ == "__main__":
    unittest.main()
