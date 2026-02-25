"""
Date and time utility functions
"""
from datetime import datetime, date
from typing import Union


def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    
    A leap year is divisible by 4, except for century years which must be
    divisible by 400.
    
    Args:
        year: The year to check
    
    Returns:
        True if the year is a leap year, False otherwise
    
    Examples:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_between(date1: Union[date, str], date2: Union[date, str]) -> int:
    """
    Calculate the number of days between two dates.
    
    Args:
        date1: First date (date object or ISO format string 'YYYY-MM-DD')
        date2: Second date (date object or ISO format string 'YYYY-MM-DD')
    
    Returns:
        Absolute number of days between the two dates
    
    Examples:
        >>> days_between('2026-01-01', '2026-01-10')
        9
        >>> days_between(date(2026, 1, 1), date(2026, 2, 1))
        31
    """
    if isinstance(date1, str):
        date1 = datetime.fromisoformat(date1).date()
    if isinstance(date2, str):
        date2 = datetime.fromisoformat(date2).date()
    
    return abs((date2 - date1).days)


def format_duration(seconds: int) -> str:
    """
    Format a duration in seconds into a human-readable string.
    
    Args:
        seconds: Duration in seconds
    
    Returns:
        Formatted string (e.g., "2h 30m 15s")
    
    Examples:
        >>> format_duration(3665)
        '1h 1m 5s'
        >>> format_duration(90)
        '1m 30s'
    """
    if seconds < 0:
        raise ValueError("Duration must be non-negative")
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")
    
    return ' '.join(parts)
