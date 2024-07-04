"""
Valid Anagram

This question is asked by Facebook.
Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""

from typing import Callable

from printer import print_fail, print_pass


def valid_anagram(s: str, t: str) -> bool:
    """Validate anagram."""
    hmaps, hmapt = {}, {}

    for c in s:
        hmaps[c] = hmaps.get(c, 0) + 1

    for c in t:
        hmapt[c] = hmapt.get(c, 0) + 1

    return hmaps == hmapt
    # return set(s) == set(t)


def tester(func: Callable[[str, str], bool], s: str, t: str, expected: bool) -> None:
    """Print a custom output for testing."""
    if func(s, t) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        strs, expected_str = line.strip().split()

        s, t = strs.split(",")
        expected = bool(int(expected_str))

        print(f'Input: s = "{s}", t = "{t}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {valid_anagram(s, t)}")
        tester(valid_anagram, s, t, expected)
        print()
