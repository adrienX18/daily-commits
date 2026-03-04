"""List utility functions for common operations."""
from typing import List, TypeVar, Optional, Any
from functools import reduce

T = TypeVar('T')


def flatten(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list into a single list.
    
    Args:
        nested_list: A list of lists to flatten
        
    Returns:
        A flattened list containing all elements
    """
    return [item for sublist in nested_list for item in sublist]


def chunk(lst: List[T], size: int) -> List[List[T]]:
    """Split a list into chunks of specified size.
    
    Args:
        lst: The list to chunk
        size: Size of each chunk
        
    Returns:
        A list of chunks
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def unique(lst: List[T]) -> List[T]:
    """Return unique elements while preserving order.
    
    Args:
        lst: The input list
        
    Returns:
        List with duplicates removed
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def group_by(lst: List[T], key_fn) -> dict:
    """Group list elements by a key function.
    
    Args:
        lst: The list to group
        key_fn: Function to extract grouping key
        
    Returns:
        Dictionary mapping keys to lists of elements
    """
    groups = {}
    for item in lst:
        key = key_fn(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


def binary_search(sorted_list: List[T], target: T) -> Optional[int]:
    """Perform binary search on a sorted list.
    
    Args:
        sorted_list: A sorted list to search in
        target: The value to search for
        
    Returns:
        Index of target if found, None otherwise
        
    Time Complexity: O(log n)
    """
    if not sorted_list:
        return None
        
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = sorted_list[mid]
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return None
