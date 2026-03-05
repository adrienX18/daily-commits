"""Validation utility functions for common input types."""

import re
from typing import Any


def is_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_url(url: str) -> bool:
    """Validate URL format."""
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(pattern, url))


def is_phone_number(phone: str) -> bool:
    """Validate phone number (US format)."""
    pattern = r'^\+?1?\d{10}$|^\+?1?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    cleaned = re.sub(r'[\s.-]', '', phone)
    return bool(re.match(pattern, cleaned))


def is_positive_integer(value: Any) -> bool:
    """Check if value is a positive integer."""
    try:
        num = int(value)
        return num > 0
    except (ValueError, TypeError):
        return False


def is_in_range(value: float, min_val: float, max_val: float) -> bool:
    """Check if value is within a specified range (inclusive)."""
    try:
        return min_val <= float(value) <= max_val
    except (ValueError, TypeError):
        return False
