"""
First Unique Character

This question is asked by Microsoft.
Given a string, return the index of its first unique character.
If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""

from printer import print_fail, print_pass

from typing import Callable, Dict


def first_unique_character(s: str) -> int:
    """Return the index of the first unique character."""
    hmap: Dict = {}

    for c in s:
        hmap[c] = hmap.get(c, 0) + 1

    for i, c in enumerate(s):
        if hmap[c] == 1:
            return i

    return -1


def tester(func: Callable[[str], int], s: str, expected: int) -> None:
    """Print custom output for testing."""
    if func(s) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        s, expected_str = line.strip().split()
        expected = int(expected_str)

        print(f'Input: s = "{s}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {first_unique_character(s)}")
        tester(first_unique_character, s, expected)
        print()
