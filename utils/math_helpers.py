"""Mathematical utility functions."""
import math
from typing import List, Union, Optional
from functools import reduce
from operator import mul


def factorial(n: int) -> int:
    """Calculate factorial of n.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor using Euclidean algorithm.
    
    Args:
        a: First integer (can be negative)
        b: Second integer (can be negative)
        
    Returns:
        Greatest common divisor (always positive)
        
    Examples:
        >>> gcd(12, 8)
        4
        >>> gcd(-12, 8)
        4
        >>> gcd(0, 5)
        5
    """
    # Handle negative numbers by taking absolute values
    a, b = abs(a), abs(b)
    
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate least common multiple.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Least common multiple
    """
    return abs(a * b) // gcd(a, b) if a and b else 0


def is_prime(n: int) -> bool:
    """Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative indices")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def mean(numbers: List[Union[int, float]]) -> float:
    """Calculate arithmetic mean.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Mean value
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """Calculate median value.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Median value
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]
