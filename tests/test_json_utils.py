import json
import os
import unittest
from unittest.mock import mock_open, patch

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

class TestJsonUtils(unittest.TestCase):
    def test_read_json_file_valid(self):
        valid_json = '{"key": "value"}'
        with patch('builtins.open', mock_open(read_data=valid_json)):
            data = read_json_file('test.json')
            self.assertEqual(data, {'key': 'value'})

    def test_read_json_file_invalid(self):
        invalid_json = 'invalid json'
        with patch('builtins.open', mock_open(read_data=invalid_json)):
            with self.assertRaises(ValueError):
                read_json_file('test.json')

    def test_read_json_file_nonexistent(self):
        nonexistent_file = 'nonexistent.json'
        with self.assertRaises(FileNotFoundError):
            read_json_file(nonexistent_file)

if __name__ == '__main__':
    unittest.main()
