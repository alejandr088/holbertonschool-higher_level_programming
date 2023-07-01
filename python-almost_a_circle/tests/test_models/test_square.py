import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_size(self):
        square = Square(2)
        self.assertEqual(square.size, 2)

    def test_size_setter(self):
        square = Square(2)
        square.size = 3
        self.assertEqual(square.size, 3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)

    def test_str(self):
        square = Square(2, 3, 4, 1)
        self.assertEqual(str(square), '[Square] (1) 3/4 - 2')

    def test_update_args(self):
        square = Square(1, 2, 3, 4)
        square.update(5, 6, 7, 8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_kwargs(self):
        square = Square(1, 2, 3, 4)
        square.update(size=5, x=6, y=7, id=8)
        self.assertEqual(square.id, 8)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_to_dictionary(self):
        square = Square(2, 3, 4, 1)
        expected_dict = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
