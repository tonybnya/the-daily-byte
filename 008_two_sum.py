"""
Two Sum

This question is asked by Google. Given an array of integers,
return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""

from typing import Callable, Dict, List

from printer import print_fail, print_pass


def two_sum(nums: List[int], k: int) -> List[int]:
    """Return a list of the two numbers of nums sum to k, or [-1, -1]."""
    hmap: Dict = {}

    i: int = 0
    while i < len(nums):
        diff: int = k - nums[i]
        if diff in hmap:
            return [diff, hmap[diff]]
        hmap[nums[i]] = diff
        i += 1

    return [-1, -1]


def tester(
    func: Callable[[List[int], int], List[int]],
    nums: List[int],
    k: int,
    expected: List[int],
) -> None:
    """Print custom output for testing."""
    if func(nums, k) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        nums_str, k_str, expected_str = line.strip().split()

        nums = [int(num) for num in nums_str.split(",")]
        k = int(k_str)
        expected = [int(num) for num in expected_str.split(",")]

        print(f"Input: nums = {nums}, k = {k}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {two_sum(nums, k)}")
        tester(two_sum, nums, k, expected)
        print()
