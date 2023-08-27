#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map
class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, expected, path):
        output = access_nested_map(name, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a", ), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, output):
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, path)
            self.assertEqual(output, err.exception)