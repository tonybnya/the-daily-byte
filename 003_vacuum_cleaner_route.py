"""
Vacuum Cleaner Route

This question is asked by Amazon. Given a string representing the
sequence of moves a robot vacuum makes, return whether or not it will
return to its original position. The string will only contain L, R, U,
and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

from typing import Callable, Dict, List

from printer import print_fail, print_pass


def vacuum_cleaner_route(s: str) -> bool:
    """Check vacuum cleaner route."""
    hm: Dict = {}

    if not s or len(s) < 2:
        return False

    for c in s:
        hm[c] = hm.get(c, 0) + 1

    keys: List = list(hm.keys())
    if len(keys) < 2:
        return False

    values: List = list(hm.values())
    val: int = values[0]

    for v in values[1:]:
        if v != val:
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
        print(f"My Answer: {vacuum_cleaner_route(s)}")
        tester(vacuum_cleaner_route, s, expected)
        print()
