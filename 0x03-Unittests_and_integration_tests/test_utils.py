#!/usr/bin/env python3
"""Utils testcase"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestCase of a Nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, path, expected):
        """Test for the dictionary of the ouput with the expected output"""
        output = access_nested_map(name, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a", ), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, map, path, output):
        """Tests the KeyError """
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, path)
            self.assertEqual(output, err.exception)


class TestGetJson(unittest.TestCase):
    """A Unittest to check and test for the Json of a file"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test JSON"""
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            res = get_json(test_url)
            self.assertEqual(res, test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Testing of Memoization"""
    def test_memoize(self):
        """Method to test the memo"""
        class TestClass:
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as method:
            testClass = TestClass()
            testClass.a_property()
            testClass.a_property()
            method.assert_called_once()
