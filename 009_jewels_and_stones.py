"""
Jewels and Stones

This question is asked by Amazon. Given a string representing your
stones and another string representing a list of jewels,
return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""

from typing import Callable, Dict

from printer import print_fail, print_pass


def jewels_and_stones(jewels: str, stones: str) -> int:
    """Return the number of stones that are also jewels."""
    hmap: Dict = {}
    k: int = 0

    for c in jewels:
        hmap[c] = hmap.get(c, 0) + 1

    for c in stones:
        if c in hmap:
            k += 1

    return k


def tester(
    func: Callable[[str, str], int], jewels: str, stones: str, expected: int
) -> None:
    """Print custom output for testing."""
    if func(jewels, stones) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        strs, expected_str = line.strip().split()

        jewels, stones = strs.split(",")
        expected = int(expected_str)

        print(f'Input: jewels = "{jewels}", stones = "{stones}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {jewels_and_stones(jewels, stones)}")
        tester(jewels_and_stones, jewels, stones, expected)
        print()
