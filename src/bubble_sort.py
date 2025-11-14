"""Bubble Sort implementation with optional descending order support.

Usage example:
    >>> from src.bubble_sort import bubble_sort
    >>> bubble_sort([3, 1, 2])
    [1, 2, 3]
    >>> bubble_sort([3, 1, 2], descending=True)
    [3, 2, 1]

The algorithm is stable (duplicate values maintain their relative order).
Time complexity: O(n^2) comparisons/swaps in the worst and average case.
Space complexity: O(1) auxiliary (excluding the returned copy of the input).
"""

from __future__ import annotations

from typing import List, MutableSequence, Sequence, TypeVar

T = TypeVar("T")


def bubble_sort(values: Sequence[T], *, descending: bool = False) -> List[T]:
    """Return a stably sorted copy of *values* using the Bubble Sort algorithm.

    Args:
        values: A sequence of comparable items (typically numbers) to sort.
        descending: When True, sort from largest to smallest. Defaults to ascending.

    Returns:
        A new list with the sorted values.
    """

    if isinstance(values, list):
        working: MutableSequence[T] = values.copy()
    else:
        working = list(values)

    n = len(working)
    if n < 2:
        return list(working)

    def _compare(left: T, right: T) -> bool:
        return left < right if descending else left > right

    for pass_index in range(n - 1):
        swapped = False
        for idx in range(0, n - 1 - pass_index):
            if _compare(working[idx], working[idx + 1]):
                working[idx], working[idx + 1] = working[idx + 1], working[idx]
                swapped = True
        if not swapped:
            break

    return list(working)
