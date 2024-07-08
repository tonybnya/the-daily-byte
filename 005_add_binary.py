"""
Add binary

This question is asked by Apple. Given two binary strings (strings
containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string
itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""

from typing import Callable

from printer import print_fail, print_pass


# Runtime: O(logn) -> `bin()` is O(logn) TC, `int()` is O(1) TC
# Memory Space: O(1)
def add_binary(bin1: str, bin2: str) -> str:
    """Add two binary strings."""
    return bin(int(bin1, 2) + int(bin2, 2))[2:]


def tester(
    func: Callable[[str, str], str], bin1: str, bin2: str, expected: str
) -> None:
    """Print custom output for testing."""
    if func(bin1, bin2) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        bins, expected = line.strip().split()
        bin1, bin2 = bins.split(",")

        print(f'Input: bin1 = "{bin1}", bin2 = "{bin2}"')
        print(f'Expected Output: "{expected}"')
        print(f'My Answer: "{add_binary(bin1, bin2)}"')
        tester(add_binary, bin1, bin2, expected)
        print()
