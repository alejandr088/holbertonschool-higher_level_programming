#!/usr/bin/python3
"""author: alejandr088"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test rectangle class"""
    def test_area(self):
        """test area"""
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_str(self):
        """test string"""
        rectangle = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(str(rectangle), '[Rectangle] (1) 4/5 - 2/3')

    def test_update_args(self):
        """test updt args"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(6, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)

    def test_update_kwargs(self):
        """test updt kwargs"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(width=6, height=7, x=8, y=9, id=10)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 8)
        self.assertEqual(rectangle.y, 9)

    def test_to_dictionary(self):
        """test dict"""
        rectangle = Rectangle(2, 3, 4, 5, 1)
        expected_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
