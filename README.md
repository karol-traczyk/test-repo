# test-repo

## Bubble Sort Utility

This repository now exposes a stable Bubble Sort implementation via `src/bubble_sort.py`.
Import the `bubble_sort` function wherever you need a deterministic in-memory sort that
supports both ascending and descending orders and short-circuits when the input is already sorted.

### Usage

```python
from bubble_sort import bubble_sort

numbers = [3, 1, 2, 2]
ascending = bubble_sort(numbers)
# [1, 2, 2, 3]

descending = bubble_sort(numbers, descending=True)
# [3, 2, 2, 1]
```

### Complexity

- Time: O(n²) worst/average, O(n) best case when the list is already sorted (thanks to the early-exit optimization).
- Space: O(1) auxiliary work besides the returned copy of the input.

### Tests

Run the comprehensive unit suite (covering empty, single element, sorted, reverse-sorted,
duplicates, negatives, and randomized input) with:

```
python3 -m unittest discover -s tests
```
