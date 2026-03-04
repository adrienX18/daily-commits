"""Unit tests for list helper functions."""
import pytest
from utils.list_helpers import (
    flatten, chunk, unique, group_by, binary_search
)


class TestFlatten:
    """Tests for flatten function."""
    
    def test_flatten_nested_list(self):
        """Test flattening a nested list."""
        nested = [[1, 2], [3, 4], [5]]
        assert flatten(nested) == [1, 2, 3, 4, 5]
    
    def test_flatten_empty_list(self):
        """Test flattening an empty list."""
        assert flatten([]) == []
    
    def test_flatten_single_element_lists(self):
        """Test flattening lists with single elements."""
        nested = [[1], [2], [3]]
        assert flatten(nested) == [1, 2, 3]


class TestChunk:
    """Tests for chunk function."""
    
    def test_chunk_even_division(self):
        """Test chunking with even division."""
        lst = [1, 2, 3, 4, 5, 6]
        assert chunk(lst, 2) == [[1, 2], [3, 4], [5, 6]]
    
    def test_chunk_uneven_division(self):
        """Test chunking with uneven division."""
        lst = [1, 2, 3, 4, 5]
        assert chunk(lst, 2) == [[1, 2], [3, 4], [5]]
    
    def test_chunk_size_larger_than_list(self):
        """Test chunk size larger than list."""
        lst = [1, 2, 3]
        assert chunk(lst, 5) == [[1, 2, 3]]


class TestUnique:
    """Tests for unique function."""
    
    def test_unique_removes_duplicates(self):
        """Test removing duplicates."""
        lst = [1, 2, 2, 3, 3, 3, 4]
        assert unique(lst) == [1, 2, 3, 4]
    
    def test_unique_preserves_order(self):
        """Test that order is preserved."""
        lst = [3, 1, 2, 1, 3]
        assert unique(lst) == [3, 1, 2]
    
    def test_unique_empty_list(self):
        """Test with empty list."""
        assert unique([]) == []


class TestBinarySearch:
    """Tests for binary_search function."""
    
    def test_binary_search_found(self):
        """Test finding an element."""
        lst = [1, 3, 5, 7, 9, 11]
        assert binary_search(lst, 7) == 3
    
    def test_binary_search_not_found(self):
        """Test element not in list."""
        lst = [1, 3, 5, 7, 9]
        assert binary_search(lst, 6) is None
    
    def test_binary_search_empty_list(self):
        """Test with empty list."""
        assert binary_search([], 5) is None
    
    def test_binary_search_first_element(self):
        """Test finding first element."""
        lst = [1, 2, 3, 4, 5]
        assert binary_search(lst, 1) == 0
    
    def test_binary_search_last_element(self):
        """Test finding last element."""
        lst = [1, 2, 3, 4, 5]
        assert binary_search(lst, 5) == 4
