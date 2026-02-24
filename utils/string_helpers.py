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
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    return ' '.join(text.split()[::-1])
