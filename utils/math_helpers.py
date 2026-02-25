"""
Mathematical utility functions
"""
from typing import List, Union


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two numbers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numeric values
    
    Returns:
        The arithmetic mean as a float
    
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.
    
    Args:
        numbers: List of numeric values
    
    Returns:
        The median value as a float
    
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 0:
        # Even length: average of two middle values
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        # Odd length: return middle value
        return float(sorted_nums[n // 2])
