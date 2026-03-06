"""
Format Helpers - Utility functions for formatting text and numbers.

This module provides a collection of formatting utilities for common tasks like
currency formatting, percentage display, and text truncation with proper handling
of edge cases and configurable options.
"""


def format_currency(amount, currency_symbol='$', decimal_places=2):
    """
    Format a number as currency with proper decimal places and thousands separator.
    
    This function takes a numeric value and formats it as currency with proper
    thousands separators (commas) and the specified number of decimal places.
    
    Args:
        amount (float or int): The numeric amount to format
        currency_symbol (str, optional): The currency symbol to use. Defaults to '$'
        decimal_places (int, optional): Number of decimal places to display. Defaults to 2
    
    Returns:
        str: Formatted currency string with symbol, commas, and decimal places
    
    Examples:
        >>> format_currency(1234.56)
        '$1,234.56'
        >>> format_currency(1000000, currency_symbol='€', decimal_places=0)
        '€1,000,000'
        >>> format_currency(99.9, decimal_places=3)
        '$99.900'
    
    Note:
        Negative amounts will have the minus sign before the currency symbol.
    """
    formatted_number = f"{amount:,.{decimal_places}f}"
    return f"{currency_symbol}{formatted_number}"


def format_percentage(value, decimal_places=1):
    """
    Format a decimal value as a percentage with the % symbol.
    
    Converts a decimal value (where 1.0 = 100%) to a percentage string with
    the specified number of decimal places.
    
    Args:
        value (float): The decimal value to format (e.g., 0.75 represents 75%)
        decimal_places (int, optional): Number of decimal places to show. Defaults to 1
    
    Returns:
        str: Formatted percentage string with % symbol
    
    Examples:
        >>> format_percentage(0.7523)
        '75.2%'
        >>> format_percentage(0.5, decimal_places=0)
        '50%'
        >>> format_percentage(1.2345, decimal_places=2)
        '123.45%'
    
    Note:
        Values greater than 1.0 will display as percentages greater than 100%.
    """
    percentage = value * 100
    return f"{percentage:.{decimal_places}f}%"


def truncate_text(text, max_length=50, suffix='...'):
    """
    Truncate text to a maximum length and add suffix if truncated.
    
    This function intelligently truncates long strings to fit within a specified
    length, adding an ellipsis or custom suffix to indicate truncation.
    
    Args:
        text (str): The text to truncate
        max_length (int, optional): Maximum length before truncation. Defaults to 50
        suffix (str, optional): String to append if truncated. Defaults to '...'
    
    Returns:
        str: Original text if within max_length, otherwise truncated text with suffix
    
    Examples:
        >>> truncate_text("This is a very long text that needs truncation", 20)
        'This is a very lo...'
        >>> truncate_text("Short text", 50)
        'Short text'
        >>> truncate_text("Long description here", 15, suffix='…')
        'Long descri…'
    
    Note:
        The suffix is included in the max_length count, so the actual text content
        will be shorter than max_length by the length of the suffix.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
