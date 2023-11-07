#!/usr/bin/env python3
"""Test Case for the client"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class

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

    def test_public_repos_url(self):
        """Tests the public repo"""
        expected = "http://test_url"
        outcome = {"repos_url": expected}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock:
            mock.return_value = {outcome}
            self.assertEqual(GithubOrgClient("google")._public_repos_url, expected)
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "other_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """Test the github license"""
        getlicense = GithubOrgClient.has_license(repo, key)
        self.assertEqual(getlicense, expected)
def requests_get(*args, **kwargs):
    """
    Function that mocks requests
    """
    class MockResponse:
        """
        Mock response
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up function for TestIntegrationGithubOrgClient class
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down resources set up for class
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos license
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Testing public repo
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos)