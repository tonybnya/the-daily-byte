"""
Spot the Difference

This question is asked by Google.
You are given two strings, s and t which only consist of lowercase letters.
t is generated by shuffling the letters in s as well as potentially adding
an additional random character.
Return the letter that was randomly added to t if it exists,
otherwise, return ’  ‘.
Note: You may assume that at most one additional character can be added to t.

Ex: Given the following strings...

s = "foobar", t = "barfoot", return 't'
s = "ide", t = "idea", return 'a'
s = "coding", t "ingcod", return ''
"""

from typing import Callable, Dict

from printer import print_fail, print_pass


# Runtime: O(n + m)
# Extra Memory Space: O(n + m)
def spot_the_diff(s: str, t: str) -> str:
    """Return the only different letter."""
    hmap: Dict = {}  # O(n + m) SC

    # O(n) TC
    for c in s:
        hmap[c] = hmap.get(c, 0) + 1

    # O(m) TC
    for c in t:
        hmap[c] = hmap.get(c, 0) + 1

    return c if hmap.get(c, "") == 1 else " "


def tester(func: Callable[[str, str], str], s: str, t: str, expected: str) -> None:
    """Print custom output for testing."""
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
        expected: str = ""

        expected = " " if expected_str.isdigit() else expected_str

        print(f'Input: s = "{s}", t = "{t}"')
        print(f'Expected Output: "{expected}"')
        print(f'My Answer: "{spot_the_diff(s, t)}"')
        tester(spot_the_diff, s, t, expected)
        print()
