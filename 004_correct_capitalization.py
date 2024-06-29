"""
Correct Capitalization

This question is asked by Google. Given a string, return whether or
not it uses capitalization correctly. A string correctly uses
capitalization if all letters are capitalized, no letters are
capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

from typing import Callable, List

from printer import print_fail, print_pass


def correct_capitalization(s: str) -> bool:
    """Check correct capitalization."""
    range_lower: List = list(range(97, 123))
    range_upper: List = list(range(65, 91))

    first_letter: str = s[0]

    if ord(first_letter) in range_lower:
        for c in s[1:]:
            if ord(c) in range_upper:
                return False

    if ord(first_letter) in range_upper:
        c2: str = s[1]
        if ord(c2) in range_lower:
            for c in s[2:]:
                if ord(c) in range_upper:
                    return False

        if ord(c2) in range_upper:
            for c in s[2:]:
                if ord(c) in range_lower:
                    return False

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
        s, expected_str = line.strip().split(",")
        expected = bool(int(expected_str))

        print(f'Input: s = "{s}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {correct_capitalization(s)}")
        tester(correct_capitalization, s, expected)
        print()
