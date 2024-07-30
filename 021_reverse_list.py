"""
Reverse List

This question is asked by Facebook.
Given a linked list, containing unique values, reverse it, and return the result.

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3
which points to a list that looks like the following: 3->2->1->null

7->15->9->2->null, return a reference to the node that contains 2
which points to a list that looks like the following: 2->9->15->7->null

1->null, return a reference to the node that contains 1
which points to a list that looks like the following: 1->null
"""

from __future__ import annotations

from collections import deque

from singly_linked_list import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a Linked List."""
    previous = None
    current: ListNode = head

    while current:
        node: ListNode = current.next
        current.next = previous
        previous = current
        current = node

    return previous
