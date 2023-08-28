#!/usr/bin/env python3
"""Test Case for the client"""

from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from fixtures import TEST_PAYLOAD
from parameterized import parameterized

@parameterized.expand([
    ('google', {'google': True}),
    ('abc', {'abc': True})
])
@patch('client.get_json')
class TestGithubOrgClient(unittest.TestCase):
    """Class for testing of the github client"""

    def test_org(self, org, expected):
        """Test for the matching of the org output with he expected result"""
        mock = Mock()
        mock.return_value = expected
        MainClient = GithubOrgClient(org)
        self.assertEqual(MainClient.org, expected)
        mock.assert_called_once()