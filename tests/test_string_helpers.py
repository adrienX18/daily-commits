"""
Unit tests for string helper functions
"""
import unittest
import sys
sys.path.insert(0, '..')

from utils.string_helpers import (
    capitalize_words,
    remove_extra_spaces,
    truncate,
    reverse_words,
    is_palindrome,
    is_valid_email
)


class TestStringHelpers(unittest.TestCase):
    
    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python is awesome"), "Python Is Awesome")
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()))
        self.assertFalse(is_palindrome("hello"))
    
    def test_is_valid_email(self):
        # Valid emails
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@company.co.uk"))
        self.assertTrue(is_valid_email("test123@test.org"))
        
        # Invalid emails
        self.assertFalse(is_valid_email("invalid.email"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("user@"))
        self.assertFalse(is_valid_email("user@domain"))
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email("no-at-sign.com"))


if __name__ == '__main__':
    unittest.main()
