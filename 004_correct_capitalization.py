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


# Runtime: O(n)
# Memory Space: O(1)
def correct_capitalization(s: str) -> bool:
    """Check correct capitalization."""
    # should be all time the same - SC: O(1)
    range_lower: List = list(range(97, 123))
    # should be all time the same - SC: O(1)
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


# Runtime: O(n)
# Memory Space: O(1)
def optimal(s: str) -> bool:
    """Check correct capitalization."""
    n: int = len(s)
    counter: int = 0

    for c in s:
        if c.isupper():
            counter += 1

    return counter == 0 or counter == n or (counter == 1 and s[0].isupper())


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
        print(f"My Answer: {optimal(s)}")
        tester(optimal, s, expected)
        print()
