"""Unit tests for string helper functions."""

import unittest
from utils.string_helpers import capitalize_words, reverse_string


class TestStringHelpers(unittest.TestCase):
    """Test cases for string utility functions."""
    
    def test_capitalize_words(self):
        """Test word capitalization."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
    
    def test_reverse_string(self):
        """Test string reversal."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("12345"), "54321")


if __name__ == '__main__':
    unittest.main()
