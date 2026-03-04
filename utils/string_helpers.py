"""String manipulation utilities."""
import re
from typing import str as String


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word.
    
    Args:
        text: Input string
        
    Returns:
        String with each word capitalized
    """
    return ' '.join(word.capitalize() for word in text.split())


def snake_to_camel(snake_str: str) -> str:
    """Convert snake_case to camelCase.
    
    Args:
        snake_str: String in snake_case format
        
    Returns:
        String in camelCase format
        
    Example:
        >>> snake_to_camel('hello_world_example')
        'helloWorldExample'
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def kebab_to_snake(kebab_str: str) -> str:
    """Convert kebab-case to snake_case.
    
    Args:
        kebab_str: String in kebab-case format
        
    Returns:
        String in snake_case format
        
    Example:
        >>> kebab_to_snake('hello-world-example')
        'hello_world_example'
    """
    return kebab_str.replace('-', '_')


def truncate(text: str, max_length: int, suffix: str = '...') -> str:
    """Truncate string to maximum length with suffix.
    
    Args:
        text: Input string
        max_length: Maximum length including suffix
        suffix: String to append when truncated
        
    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def remove_extra_spaces(text: str) -> str:
    """Remove extra whitespace from string.
    
    Args:
        text: Input string
        
    Returns:
        String with normalized whitespace
    """
    return ' '.join(text.split())
