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


def reverse_string(s: str) -> str:
    """Reverse a string."""
    n: int = len(s)
    rs: str = ""

    for i in range(n - 1, -1, -1):
        rs += [c for c in s][i]

    return rs
    # return s[::-1]


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
        print(f'My Answer: "{reverse_string(s)}"')
        tester(reverse_string, s, expected)
        print()
