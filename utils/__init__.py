"""
Utility functions package
"""

from .string_helpers import capitalize_words, remove_extra_spaces, truncate
from .math_helpers import fibonacci, is_prime, gcd

__all__ = [
    'capitalize_words',
    'remove_extra_spaces',
    'truncate',
    'fibonacci',
    'is_prime',
    'gcd',
]

__version__ = '0.1.0'
