"""
String validation utilities for common patterns.

This module provides helper functions for validating strings against common patterns
like palindromes, anagrams, balanced brackets, and more.
"""


def is_palindrome(text: str, case_sensitive: bool = False) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text: String to check
        case_sensitive: Whether to consider case in comparison
        
    Returns:
        True if string is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Hello")
        False
        >>> is_palindrome("Aba", case_sensitive=False)
        True
    """
    if not case_sensitive:
        text = text.lower()
    # Remove non-alphanumeric characters
    cleaned = ''.join(c for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def are_anagrams(str1: str, str2: str, case_sensitive: bool = False) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        str1: First string
        str2: Second string
        case_sensitive: Whether to consider case
        
    Returns:
        True if strings are anagrams, False otherwise
        
    Example:
        >>> are_anagrams("listen", "silent")
        True
        >>> are_anagrams("Hello", "World")
        False
    """
    if not case_sensitive:
        str1, str2 = str1.lower(), str2.lower()
    
    # Remove spaces and sort characters
    sorted1 = sorted(str1.replace(" ", ""))
    sorted2 = sorted(str2.replace(" ", ""))
    
    return sorted1 == sorted2


def has_balanced_brackets(text: str) -> bool:
    """
    Check if a string has balanced brackets/parentheses.
    
    Supports: (), [], {}
    
    Args:
        text: String to check
        
    Returns:
        True if brackets are balanced, False otherwise
        
    Example:
        >>> has_balanced_brackets("(hello [world])")
        True
        >>> has_balanced_brackets("(()")
        False
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in text:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0


def contains_only_digits(text: str) -> bool:
    """
    Check if string contains only digits.
    
    Args:
        text: String to check
        
    Returns:
        True if string contains only digits, False otherwise
        
    Example:
        >>> contains_only_digits("12345")
        True
        >>> contains_only_digits("123a45")
        False
    """
    return text.isdigit() and len(text) > 0


def is_valid_identifier(text: str) -> bool:
    """
    Check if string is a valid Python identifier.
    
    Args:
        text: String to check
        
    Returns:
        True if valid identifier, False otherwise
        
    Example:
        >>> is_valid_identifier("my_variable")
        True
        >>> is_valid_identifier("2invalid")
        False
        >>> is_valid_identifier("valid_name_123")
        True
    """
    return text.isidentifier()
