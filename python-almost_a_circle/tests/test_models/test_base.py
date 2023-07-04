#!/usr/bin/python3
"""author: alejandr088"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test base class"""
    def test_to_json_string_empty_list(self):
        """test empty list"""
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_non_empty_list(self):
        """test not empty list"""
        dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expected_json = '[{"id": 1, "name": "John"}, \
{"id": 2, "name": "Jane"}]'
        self.assertEqual(Base.to_json_string(dictionaries), expected_json)

    def test_save_to_file_none(self):
        """test save to file none"""
        Base.save_to_file(None)
        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_empty_list(self):
        """test save empty list"""
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string_empty_string(self):
        """test empty string"""
        self.assertEqual(Base.from_json_string(''), [])

    def test_from_json_string_non_empty_string(self):
        """test not empty string"""
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expected_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)


if __name__ == '__main__':
    unittest.main()
