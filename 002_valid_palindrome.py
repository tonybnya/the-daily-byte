"""
Valid Palindrome

This question is asked by Facebook.
Given a string, return whether or not it forms a palindrome
ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same
forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""

from typing import Callable, List

from printer import print_fail, print_pass


# Runtime: O(n)
# Memory Space: O(n)
def cleanup(s: str) -> str:
    """Cleanup a string."""
    rng1: List = list(range(65, 91))
    rng2: List = list(range(97, 123))

    chars = ""  # should end up with an O(n) extra memory space
    for c in s.lower():
        if ord(c) in rng1 or ord(c) in rng2:
            chars += c

    return chars


# Runtime: O(n)
# Memory Space: O(n)
def valid_palindrome(s: str) -> bool:
    """Valid a palindrome."""
    s = cleanup(s)  # memory space: O(n)
    i: int = 0
    j: int = len(s) - 1

    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


# Runtime: O(n)
# Memory Space: O(1)
def optimal(s: str) -> bool:
    """Valid a palindrome."""
    n: int = len(s)
    i: int = 0
    j: int = n - 1

    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

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
        s, expected_str = line.strip().split("|")
        expected = bool(int(expected_str))

        print(f'Input: s = "{s}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {optimal(s)}")
        tester(optimal, s, expected)
        print()
