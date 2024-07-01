"""
This question is asked by Facebook.
Given a string and the ability to delete at most one character,
return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters
that reads the same forwards and backwards.

Ex: Given the following strings...

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"""

from typing import Callable

from printer import print_fail, print_pass


def isPalindrome(s: str) -> bool:
    """Valid a palindrome with removal."""

    def is_palindrome_range(i, j):
        return all(s[k] == s[j - k + i] for k in range(i, j))

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(
                left, right - 1
            )
        left, right = left + 1, right - 1

    return True


def tester(func: Callable[[str], bool], s: str, expected: bool) -> None:
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
        expected: bool = bool(int(expected_str))

        print(f'Input: s = "{s}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {isPalindrome(s)}")
        tester(isPalindrome, s, expected)
        print()
