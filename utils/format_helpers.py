"""
Format Helpers - Utility functions for formatting text and numbers
"""

def format_currency(amount, currency_symbol='$', decimal_places=2):
    """
    Format a number as currency with proper decimal places.
    
    Args:
        amount: The numeric amount to format
        currency_symbol: The currency symbol to use (default: '$')
        decimal_places: Number of decimal places (default: 2)
    
    Returns:
        Formatted currency string
    
    Example:
        >>> format_currency(1234.56)
        '$1,234.56'
    """
    formatted_number = f"{amount:,.{decimal_places}f}"
    return f"{currency_symbol}{formatted_number}"


def format_percentage(value, decimal_places=1):
    """
    Format a decimal value as a percentage.
    
    Args:
        value: The decimal value (e.g., 0.75 for 75%)
        decimal_places: Number of decimal places (default: 1)
    
    Returns:
        Formatted percentage string
    
    Example:
        >>> format_percentage(0.7523)
        '75.2%'
    """
    percentage = value * 100
    return f"{percentage:.{decimal_places}f}%"


def truncate_text(text, max_length=50, suffix='...'):
    """
    Truncate text to a maximum length and add suffix if truncated.
    
    Args:
        text: The text to truncate
        max_length: Maximum length before truncation (default: 50)
        suffix: String to append if truncated (default: '...')
    
    Returns:
        Truncated text with suffix if applicable
    
    Example:
        >>> truncate_text("This is a very long text that needs truncation", 20)
        'This is a very lo...'
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
