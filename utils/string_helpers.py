"""
String utility functions for common operations
"""
import re


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string."""
    if not text:
        return ''
    return ' '.join(word.capitalize() for word in text.split())


def remove_extra_spaces(text: str) -> str:
    """Remove extra whitespace from a string."""
    if not text:
        return ''
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
    if not text:
        return ''
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
    Email validation with improved regex pattern.
    
    Args:
        email: The email address to validate
    
    Returns:
        True if email format appears valid, False otherwise
    
    Examples:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid.email")
        False
        >>> is_valid_email("user+tag@example.co.uk")
        True
    """
    if not email:
        return False
    
    # More robust email validation pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def sanitize_filename(filename: str, replacement: str = '_') -> str:
    """
    Sanitize a string to make it safe for use as a filename.
    
    Removes or replaces characters that are invalid on most filesystems
    including Windows, macOS, and Linux.
    
    Args:
        filename: The string to sanitize
        replacement: Character to use for replacing invalid characters (default: '_')
    
    Returns:
        A sanitized filename string safe for use on common filesystems
    
    Examples:
        >>> sanitize_filename("report:2024.txt")
        'report_2024.txt'
        >>> sanitize_filename("my/file\\name.pdf")
        'my_file_name.pdf'
        >>> sanitize_filename("data<>file?.csv", replacement='-')
        'data--file-.csv'
    """
    if not filename:
        return ''
    
    # Invalid characters on Windows, macOS, and Linux filesystems
    # < > : " / \ | ? * and control characters (0-31)
    invalid_chars = r'[<>:"/\\|?*\x00-\x1f]'
    
    # Replace invalid characters with the replacement character
    sanitized = re.sub(invalid_chars, replacement, filename)
    
    # Remove leading/trailing dots and spaces (problematic on Windows)
    sanitized = sanitized.strip('. ')
    
    # If the result is empty or only contains replacement chars, use a default
    if not sanitized or sanitized.replace(replacement, '') == '':
        sanitized = 'unnamed_file'
    
    return sanitized
