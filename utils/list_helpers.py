"""
List utility functions for common operations
"""
from typing import List, Any, Callable


def chunk_list(lst: list, chunk_size: int) -> list:
    """Split a list into chunks of specified size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def flatten(nested_list: list) -> list:
    """Flatten a nested list structure."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def remove_duplicates(lst: list) -> list:
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def rotate_list(lst: List[Any], positions: int) -> List[Any]:
    """
    Rotate list elements by specified positions.
    Positive values rotate right, negative rotate left.
    
    Args:
        lst: List to rotate
        positions: Number of positions to rotate
    
    Returns:
        New rotated list
    
    Examples:
        >>> rotate_list([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate_list([1, 2, 3, 4, 5], -2)
        [3, 4, 5, 1, 2]
    """
    if not lst:
        return []
    
    n = len(lst)
    positions = positions % n  # Handle rotations larger than list length
    
    return lst[-positions:] + lst[:-positions] if positions else lst.copy()


def filter_by_condition(lst: List[Any], condition: Callable[[Any], bool]) -> List[Any]:
    """
    Filter list elements based on a condition function.
    
    Args:
        lst: List to filter
        condition: Function that returns True for elements to keep
    
    Returns:
        Filtered list
    
    Examples:
        >>> filter_by_condition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        [2, 4]
    """
    return [item for item in lst if condition(item)]


def group_by(lst: List[Any], key_func: Callable[[Any], Any]) -> dict:
    """
    Group list elements by a key function.
    
    Args:
        lst: List to group
        key_func: Function to extract grouping key from each element
    
    Returns:
        Dictionary with keys mapped to lists of grouped elements
    
    Examples:
        >>> group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4]}
    """
    groups = {}
    for item in lst:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups
