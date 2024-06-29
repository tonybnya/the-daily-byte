"""
Longest Common Prefix

This question is asked by Microsoft. Given an array of
strings, return the longest common prefix that is shared
amongst all strings.
Note: you may assume all strings only contain lowercase
alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""

from typing import Callable, List

from printer import print_fail, print_pass


def longest_common_prefix(strs: List[str]) -> str:
    """Return the longest common prefix."""
    strs = sorted(strs)

    first_str: str = strs[0]
    last_str: str = strs[-1]

    m: int = len(first_str)
    n: int = len(last_str)

    lcp: str = ""

    for i in range(min(m, n)):
        if first_str[i] != last_str[i]:
            return lcp
        lcp += first_str[i]

    return lcp


def tester(func: Callable[[List[str]], str], strs: List[str], expected: str) -> None:
    """Print custom output for testing."""
    if func(strs) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        arr_str, expected = line.split()

        strs = arr_str.split(",")

        if expected == "0":
            expected = ""

        print(f"Input: strs = {strs}")
        print(f'Expected Output: "{expected}"')
        print(f'My Answer: "{longest_common_prefix(strs)}"')
        tester(longest_common_prefix, strs, expected)
        print()
