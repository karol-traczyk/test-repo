"""
Bubble Sort Implementation

This module provides a stable implementation of the Bubble Sort algorithm
with early termination optimization.
"""

from typing import List, TypeVar

T = TypeVar("T")


def bubble_sort(arr: List[T]) -> List[T]:
    """
    Sort an array/list in ascending order using Bubble Sort algorithm.

    This is a stable sort implementation that includes the standard optimization
    to terminate early when a full pass performs no swaps.

    Time Complexity: O(n^2) in worst and average case, O(n) in best case
    Space Complexity: O(1) extra space (in-place sorting)

    Args:
        arr: List of comparable values to sort

    Returns:
        The sorted list (sorted in-place, same reference is returned)

    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]

        >>> bubble_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]

        >>> bubble_sort([])
        []

        >>> bubble_sort([-3, 5, -1, 0, 2])
        [-3, -1, 0, 2, 5]
    """
    n = len(arr)

    # Handle edge cases
    if n <= 1:
        return arr

    # Perform bubble sort with early termination optimization
    for i in range(n):
        # Flag to detect if any swap happened in this pass
        swapped = False

        # Last i elements are already in place
        for j in range(n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the array is already sorted
        if not swapped:
            break

    return arr
