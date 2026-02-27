"""
Unit tests for list_helpers module
"""
import unittest
from utils.list_helpers import (
    flatten, 
    remove_duplicates, 
    chunk_list, 
    find_common_elements
)


class TestListHelpers(unittest.TestCase):
    
    def test_flatten_nested_list(self):
        """Test flattening a nested list"""
        nested = [[1, 2], [3, 4], [5]]
        self.assertEqual(flatten(nested), [1, 2, 3, 4, 5])
    
    def test_flatten_empty_list(self):
        """Test flattening an empty list"""
        self.assertEqual(flatten([]), [])
    
    def test_remove_duplicates_preserves_order(self):
        """Test that remove_duplicates preserves first occurrence order"""
        items = [1, 2, 3, 2, 4, 1, 5]
        self.assertEqual(remove_duplicates(items), [1, 2, 3, 4, 5])
    
    def test_remove_duplicates_empty_list(self):
        """Test remove_duplicates on empty list"""
        self.assertEqual(remove_duplicates([]), [])
    
    def test_chunk_list_even_division(self):
        """Test chunking a list that divides evenly"""
        items = [1, 2, 3, 4, 5, 6]
        chunks = chunk_list(items, 2)
        self.assertEqual(chunks, [[1, 2], [3, 4], [5, 6]])
    
    def test_chunk_list_uneven_division(self):
        """Test chunking a list with remainder"""
        items = [1, 2, 3, 4, 5]
        chunks = chunk_list(items, 2)
        self.assertEqual(chunks, [[1, 2], [3, 4], [5]])
    
    def test_find_common_elements(self):
        """Test finding common elements between lists"""
        list1 = [1, 2, 3, 4, 5]
        list2 = [3, 4, 5, 6, 7]
        self.assertEqual(set(find_common_elements(list1, list2)), {3, 4, 5})
    
    def test_find_common_elements_no_overlap(self):
        """Test finding common elements with no overlap"""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(find_common_elements(list1, list2), [])


if __name__ == '__main__':
    unittest.main()
