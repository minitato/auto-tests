import unittest
from unittest.mock import mock_open, patch
import yaml

def parse_yaml_string(yaml_string):
    return yaml.safe_load(yaml_string)

def write_yaml_file(file_path, data):
    with open(file_path, 'w') as f:
        yaml.safe_dump(data, f)

class TestYamlUtils(unittest.TestCase):
    def test_parse_yaml_string_valid(self):
        valid_yaml = """\
            key1: value1
            key2: value2
        """
        expected_output = {'key1': 'value1', 'key2': 'value2'}
        parsed_data = parse_yaml_string(valid_yaml)
        self.assertEqual(parsed_data, expected_output)

    def test_parse_yaml_string_invalid(self):
        invalid_yaml = "invalid yaml"
        with self.assertRaises(yaml.YAMLError):
            parse_yaml_string(invalid_yaml)

    def test_write_yaml_file_valid(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        file_path = 'test.yml'
        with patch('builtins.open', mock_open()) as mock_file:
            write_yaml_file(file_path, data)
            mock_file.assert_called_once_with(file_path, 'w')
            mock_file().write.assert_called_once_with('key1: value1\nkey2: value2\n')

    def test_write_yaml_file_invalid_path(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        file_path = '/invalid/path/test.yml'
        with self.assertRaises(OSError):
            write_yaml_file(file_path, data)

if __name__ == '__main__':
    unittest.main()
