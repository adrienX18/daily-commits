"""String utility functions for daily coding practice."""

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())


def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]
