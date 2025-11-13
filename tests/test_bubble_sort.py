"""
Comprehensive test suite for Bubble Sort implementation.

Tests cover edge cases, various input scenarios, and verify the algorithm's
stability and correctness.
"""

import pytest
from src.sorting.bubble_sort import bubble_sort


class TestBubbleSort:
    """Test cases for bubble_sort function."""

    def test_empty_array(self):
        """Test with empty input array."""
        arr = []
        result = bubble_sort(arr)
        assert result == []
        assert arr == []  # Verify original is modified (in-place)

    def test_single_element(self):
        """Test with single element array."""
        arr = [42]
        result = bubble_sort(arr)
        assert result == [42]
        assert arr == [42]

    def test_two_elements_sorted(self):
        """Test with two elements already sorted."""
        arr = [1, 2]
        result = bubble_sort(arr)
        assert result == [1, 2]

    def test_two_elements_unsorted(self):
        """Test with two elements in reverse order."""
        arr = [2, 1]
        result = bubble_sort(arr)
        assert result == [1, 2]

    def test_already_sorted(self):
        """Test with already sorted array (best case - O(n))."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_reverse_sorted(self):
        """Test with reverse sorted array (worst case - O(n^2))."""
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_with_duplicates(self):
        """Test with duplicate values to verify stability."""
        arr = [5, 2, 8, 2, 9, 1, 5, 5]
        result = bubble_sort(arr)
        assert result == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_all_duplicates(self):
        """Test with all elements being the same."""
        arr = [7, 7, 7, 7, 7]
        result = bubble_sort(arr)
        assert result == [7, 7, 7, 7, 7]

    def test_negative_numbers(self):
        """Test with negative numbers only."""
        arr = [-5, -1, -10, -3, -7]
        result = bubble_sort(arr)
        assert result == [-10, -7, -5, -3, -1]

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        arr = [3, -1, 4, -5, 2, -3, 0]
        result = bubble_sort(arr)
        assert result == [-5, -3, -1, 0, 2, 3, 4]

    def test_with_zero(self):
        """Test with zeros and other values."""
        arr = [0, 5, 0, -2, 3, 0, 1]
        result = bubble_sort(arr)
        assert result == [-2, 0, 0, 0, 1, 3, 5]

    def test_random_order(self):
        """Test with random order of elements."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = bubble_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]

    def test_large_numbers(self):
        """Test with large numbers."""
        arr = [1000000, 999999, 1000001, 5, 1000000]
        result = bubble_sort(arr)
        assert result == [5, 999999, 1000000, 1000000, 1000001]

    def test_floats(self):
        """Test with floating point numbers."""
        arr = [3.14, 2.71, 1.41, 2.71, 0.5]
        result = bubble_sort(arr)
        assert result == [0.5, 1.41, 2.71, 2.71, 3.14]

    def test_strings(self):
        """Test with strings (lexicographic sorting)."""
        arr = ["banana", "apple", "cherry", "apple", "date"]
        result = bubble_sort(arr)
        assert result == ["apple", "apple", "banana", "cherry", "date"]

    def test_stability_with_tuples(self):
        """Test stability of sort using tuples (sort by first element)."""
        arr = [(3, "a"), (1, "b"), (2, "c"), (1, "d"), (3, "e")]
        result = bubble_sort(arr)
        # Stable sort should maintain relative order of equal elements
        assert result == [(1, "b"), (1, "d"), (2, "c"), (3, "a"), (3, "e")]

    def test_in_place_modification(self):
        """Test that the sort is done in-place."""
        arr = [3, 1, 2]
        result = bubble_sort(arr)
        # Same object reference
        assert result is arr
        assert arr == [1, 2, 3]

    def test_early_termination(self):
        """Test that early termination works (nearly sorted array)."""
        # This array needs only one pass
        arr = [1, 2, 3, 5, 4]
        result = bubble_sort(arr)
        assert result == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
