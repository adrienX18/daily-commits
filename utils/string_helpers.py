"""
String utility functions for common operations
"""

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())


def remove_extra_spaces(text: str) -> str:
    """Remove extra whitespace from a string."""
    return ' '.join(text.split())


def truncate(text: str, max_length: int, suffix: str = '...') -> str:
    """Truncate a string to a maximum length with optional suffix."""
    if not text or max_length <= 0:
        return ''
    if len(text) <= max_length:
        return text
    if len(suffix) >= max_length:
        return text[:max_length]
    return text[:max_length - len(suffix)] + suffix


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    return ' '.join(text.split()[::-1])


def is_palindrome(text: str, case_sensitive: bool = False) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text: The string to check
        case_sensitive: Whether to consider case when checking (default: False)
    
    Returns:
        True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("RaceCar")
        True
        >>> is_palindrome("RaceCar", case_sensitive=True)
        False
    """
    if not text:
        return True
    
    check_text = text if case_sensitive else text.lower()
    return check_text == check_text[::-1]


def is_valid_email(email: str) -> bool:
    """
    Basic email validation checker.
    
    Args:
        email: The email address to validate
    
    Returns:
        True if email format appears valid, False otherwise
    
    Examples:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid.email")
        False
    """
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local, domain = parts
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True
