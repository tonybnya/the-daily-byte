"""
Validate Characters

This question is asked by Google.
Given a string only containing the following characters (, ), {, }, [, and ]
return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""

from __future__ import annotations

from collections import deque
from typing import Callable

from printer import print_fail, print_pass


def val_chars(chars: str) -> bool:
    """Validate characters."""
    hmap: dict = {"}": "{", ")": "(", "]": "["}
    stack: deque = deque()

    for char in chars:
        if char not in hmap:
            stack.append(char)
        elif not stack or stack.pop() != hmap.get(char, ''):
            return False

    return len(stack) == 0


def tester(func: Callable[[str], bool], chars: str, expected: bool) -> None:
    """Print custom output for testing."""
    if func(chars) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as file:
        lines: list[str] = file.readlines()

    for line in lines:
        chars, expected_str = line.strip().split()

        expected: bool = bool(int(expected_str))
        ans: bool = val_chars(chars)

        print(f"Input: chars = {chars}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        tester(val_chars, chars, expected)
        print()
