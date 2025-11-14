import random
import sys
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from bubble_sort import bubble_sort


@dataclass(frozen=True)
class StableNumber:
    value: int
    tag: str

    def __lt__(self, other: "StableNumber") -> bool:
        return self.value < other.value

    def __gt__(self, other: "StableNumber") -> bool:
        return self.value > other.value


class BubbleSortTests(unittest.TestCase):
    def test_empty_sequence(self) -> None:
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([], descending=True), [])

    def test_single_element_is_unchanged(self) -> None:
        item = [42]
        self.assertEqual(bubble_sort(item), [42])
        self.assertEqual(item, [42], "input should not be mutated")

    def test_already_sorted_sequence(self) -> None:
        data = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(data), data)
        self.assertEqual(bubble_sort(data, descending=True), [5, 4, 3, 2, 1])

    def test_reverse_sorted_sequence(self) -> None:
        data = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(data), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort(data, descending=True), data)

    def test_duplicates_preserve_order(self) -> None:
        data: List[StableNumber] = [
            StableNumber(2, "a"),
            StableNumber(2, "b"),
            StableNumber(1, "c"),
            StableNumber(2, "d"),
        ]

        sorted_data = bubble_sort(data)
        self.assertEqual([item.value for item in sorted_data], [1, 2, 2, 2])
        self.assertEqual(
            [item.tag for item in sorted_data if item.value == 2], ["a", "b", "d"]
        )

    def test_negative_numbers(self) -> None:
        data = [-5, -1, -3, 0, 2]
        self.assertEqual(bubble_sort(data), [-5, -3, -1, 0, 2])
        self.assertEqual(bubble_sort(data, descending=True), [2, 0, -1, -3, -5])

    def test_random_input_matches_python_sorted(self) -> None:
        random.seed(1337)
        data = [random.randint(-100, 100) for _ in range(25)]
        self.assertEqual(bubble_sort(data), sorted(data))
        self.assertEqual(
            bubble_sort(data, descending=True), sorted(data, reverse=True)
        )


if __name__ == "__main__":
    unittest.main()
