# Algorithm Implementations

This repository contains well-tested implementations of common algorithms with comprehensive documentation.

## Bubble Sort

A stable sorting algorithm implementation with early termination optimization.

### Usage

```python
from src.sorting.bubble_sort import bubble_sort

# Sort a list of numbers
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]

# Works with negative numbers
mixed = [3, -1, 4, -5, 2, -3, 0]
bubble_sort(mixed)
print(mixed)  # [-5, -3, -1, 0, 2, 3, 4]

# Handles duplicates (stable sort)
with_dupes = [5, 2, 8, 2, 9, 1, 5, 5]
bubble_sort(with_dupes)
print(with_dupes)  # [1, 2, 2, 5, 5, 5, 8, 9]
```

### Algorithm Details

**Bubble Sort** is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

#### Complexity

- **Time Complexity:**
  - Best Case: O(n) - when the array is already sorted (early termination optimization)
  - Average Case: O(n²)
  - Worst Case: O(n²) - when the array is reverse sorted
  
- **Space Complexity:** O(1) - sorts in-place with only constant extra space

#### Properties

- **Stable:** Yes - maintains relative order of equal elements
- **In-place:** Yes - requires only O(1) extra space
- **Adaptive:** Yes - performs better on nearly sorted data due to early termination
- **Online:** No - requires all data upfront

#### Optimization

This implementation includes the standard optimization: if no swaps occur during a complete pass through the array, the algorithm terminates early since the array is already sorted. This makes the best-case time complexity O(n).

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd test-repo

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

The implementation includes comprehensive unit tests covering:
- Empty arrays
- Single element arrays
- Arrays with duplicates
- Already sorted arrays
- Reverse sorted arrays
- Negative numbers
- Mixed positive and negative values
- Stability verification
- Early termination optimization

```bash
# Run all tests
pytest tests/test_bubble_sort.py -v

# Run with coverage
pytest tests/test_bubble_sort.py --cov=src.sorting.bubble_sort --cov-report=term-missing
```

### Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   └── sorting/
│       ├── __init__.py
│       └── bubble_sort.py
└── tests/
    ├── __init__.py
    └── test_bubble_sort.py
```

## Contributing

When adding new algorithms:
1. Follow the existing code structure
2. Include comprehensive documentation
3. Add unit tests with edge cases
4. Document time and space complexity
5. Ensure all tests pass before submitting

## License

MIT
