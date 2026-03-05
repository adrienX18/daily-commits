"""Unit tests for string helper functions."""

import pytest
from utils.string_helpers import capitalize_words, reverse_string, count_vowels


def test_capitalize_words():
    """Test word capitalization."""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is great") == "Python Is Great"


def test_reverse_string():
    """Test string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"


def test_count_vowels():
    """Test vowel counting."""
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0
