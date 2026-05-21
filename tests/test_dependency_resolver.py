
""" Module for unit test for DependencyResolver class."""

import unittest

from dependency_resolver.src import dependency_resolver

class TestDependencyResolver(unittest.TestCase):
    """ Unit tests for DependencyResolver class. This class tests the get_dependancy_chain
    method with different parameters.
    """

    def test_dependency_chain_with_d(self):
        """Test that the dependency chain for D is correct."""
        expected_result = ["G", "D"]
        actual_result = dependency_resolver.main("D")
        assert expected_result == actual_result, (
            f"actual_result != expected_result, expected={expected_result}, actual={actual_result}"
        )

    def test_dependency_chain_with_a(self):
        """Test that the dependency chain for A is correct."""
        expected_result = ["E", "G", "D", "F", "B", "A"]
        actual_result = dependency_resolver.main("A")
        assert expected_result == actual_result, (
            f"actual_result != expected_result, expected={expected_result}, actual={actual_result}"
        )

    def test_dependency_chain_with_empty_result(self):
        """Test that the dependency chain for F is correct empty."""
        expected_result = []
        actual_result = dependency_resolver.main("F")
        assert expected_result == actual_result, (
            f"actual_result != expected_result, expected={expected_result}, actual={actual_result}"
        )