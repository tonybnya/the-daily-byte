"""
Intersection of Numbers

This question is asked by Google.
Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

from typing import Callable, Dict, List

from printer import print_fail, print_pass


# Runtime: O(m+n)
# Memory Space: O(m+n)
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """Return the intersection of the two lists."""
    hmap: Dict = {}
    inter: List[int] = []

    for num in nums1:
        hmap[num] = hmap.get(num, 0) + 1

    for num in nums2:
        if num in hmap:
            inter.append(num)

    return list(set(inter))


def tester(
    func: Callable[[List[int], List[int]], List[int]],
    nums1: List[int],
    nums2: List[int],
    expected: List[int],
) -> None:
    """Print custom output for testing."""
    if func(nums1, nums2) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        strs, expected_str = line.strip().split()

        nums1_str, nums2_str = strs.split("-")
        nums1 = [int(num) for num in nums1_str.split(",")]
        nums2 = [int(num) for num in nums2_str.split(",")]

        expected = (
            [int(num) for num in expected_str.split(",")]
            if not expected_str.isalpha()
            else []
        )

        print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {intersection(nums1, nums2)}")
        tester(intersection, nums1, nums2, expected)
        print()
