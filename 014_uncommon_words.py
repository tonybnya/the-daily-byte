"""
Uncommon Words

This question is asked by Amazon.
Given two strings representing sentences, return the words that are not common
to both strings (i.e. the words that only appear in one of the sentences).
You may assume that each sentence is a sequence of words (without punctuation)
correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

from typing import Callable, Dict, List

from printer import print_fail, print_pass


# Runtime: O(m+n)
# Memory Space: O(m+n)
def uncommon_words(sentence1: str, sentence2: str) -> List[str]:
    """Return a list of uncommon words."""
    hmap: Dict = {}  # SC: O(n)
    lst: List[str] = []  # assuming this is a dynamic array, so SC is O(m+n)

    for chars in sentence1.split():
        hmap[chars] = hmap.get(chars, 0) + 1

    for chars in sentence2.split():
        hmap[chars] = hmap.get(chars, 0) + 1

    keys: List[str] = list(hmap.keys())
    for i in range(len(keys)):
        key: str = keys[i]
        if hmap[key] == 1:
            lst.append(key)

    return lst


def tester(
    func: Callable[[str, str], List[str]],
    sentence1: str,
    sentence2: str,
    expected: List[str],
):
    """Print custom output for testing."""
    if func(sentence1, sentence2) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        s1, s2, expected_str = line.strip().split()

        sentence1 = " ".join(s1.split(","))
        sentence2 = " ".join(s2.split(","))
        expected = expected_str.split(",")

        print(f'Input: sentence1 = "{sentence1}", sentence2 = "{sentence2}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {uncommon_words(sentence1, sentence2)}")
        tester(uncommon_words, sentence1, sentence2, expected)
        print()
