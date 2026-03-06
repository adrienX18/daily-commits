"""
Performance Helpers - Utilities for timing and profiling code execution.

This module provides decorators and context managers for measuring execution time,
profiling functions, and tracking performance metrics in your applications.
"""

import time
import functools
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    Decorator to measure and print function execution time.
    
    Args:
        func: Function to be timed
        
    Returns:
        Wrapped function that prints execution time
        
    Example:
        >>> @timer
        ... def slow_function():
        ...     time.sleep(1)
        ...     return "done"
        >>> slow_function()
        Function 'slow_function' took 1.001 seconds
        'done'
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed:.3f} seconds")
        return result
    return wrapper


class Timer:
    """
    Context manager for timing code blocks.
    
    Example:
        >>> with Timer("Database query"):
        ...     # Simulated database operation
        ...     time.sleep(0.5)
        Database query: 0.501 seconds
    """
    
    def __init__(self, name: str = "Operation"):
        """
        Initialize timer with a descriptive name.
        
        Args:
            name: Description of the operation being timed
        """
        self.name = name
        self.start_time = None
        self.elapsed = None
    
    def __enter__(self):
        """Start timing when entering context."""
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        """Stop timing and print elapsed time when exiting context."""
        end_time = time.perf_counter()
        self.elapsed = end_time - self.start_time
        print(f"{self.name}: {self.elapsed:.3f} seconds")


def memoize(func: Callable) -> Callable:
    """
    Decorator to cache function results for repeated calls with same arguments.
    
    Useful for expensive computations with repeated inputs. Note: only works
    with hashable arguments.
    
    Args:
        func: Function to memoize
        
    Returns:
        Wrapped function with caching
        
    Example:
        >>> @memoize
        ... def fibonacci(n):
        ...     if n < 2:
        ...         return n
        ...     return fibonacci(n-1) + fibonacci(n-2)
        >>> fibonacci(100)  # Fast due to caching
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper


def count_calls(func: Callable) -> Callable:
    """
    Decorator to count how many times a function is called.
    
    Args:
        func: Function to track
        
    Returns:
        Wrapped function with call counting
        
    Example:
        >>> @count_calls
        ... def greet(name):
        ...     return f"Hello {name}"
        >>> greet("Alice")
        'Hello Alice'
        >>> greet("Bob")
        'Hello Bob'
        >>> print(f"Called {greet.call_count} times")
        Called 2 times
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay in seconds between retries
        
    Returns:
        Decorator function
        
    Example:
        >>> @retry(max_attempts=3, delay=0.5)
        ... def unstable_api_call():
        ...     # Simulated API call that might fail
        ...     if random.random() < 0.7:
        ...         raise ConnectionError("Network error")
        ...     return "Success"
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator
