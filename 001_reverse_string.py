"""
Reverse String

This question is asked by Google.
Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""

from typing import Callable

from printer import print_fail, print_pass


# Runtime: O(n^2)
# Memory Space: O(n^2)
def solution1(s: str) -> str:
    """Reverse a string."""
    n: int = len(s)
    rs: str = ""

    for i in range(n - 1, -1, -1):
        rs += s[i]

    return rs


# Runtime: O(n)
# Memory Space: O(n)
def solution2(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


# Runtime: O(n)
# Memory Space: O(n)
def optimal(s: str) -> str:
    """Reverse a string."""
    n: int = len(s)
    rs: str = [""] * n
    j: int = 0

    for i in range(n - 1, -1, -1):
        rs[j] = s[i]
        j += 1

    return "".join(rs)


def tester(func: Callable[[str], str], s: str, expected: str) -> None:
    """Print custom output for testing."""
    if func(s) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        s, expected = line.strip().split(",")
        print(f'Input: s = "{s}"')
        print(f'Expected Output = "{expected}"')
        print(f'My Answer: "{optimal(s)}"')
        tester(optimal, s, expected)
        print()
