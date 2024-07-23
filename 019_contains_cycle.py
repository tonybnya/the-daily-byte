"""
Contains Cycle

This question is asked by Microsoft.

Given a linked list, containing unique numbers,
return whether or not it has a cycle.
Note: a cycle is a circular arrangement
(i.e. one node points back to a previous node)

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
"""

from __future__ import annotations

from singly_linked_list import ListNode


# Runtime: O(n)
# Extra Memory Space: O(1)
def has_cycle(head: ListNode | None) -> bool:
    """Return weither a Linked List has a cycle or not."""
    if head is None:
        return False

    slow: ListNode | None = head
    fast: ListNode | None = head

    while fast and fast.nextnode:
        slow = slow.nextnode
        fast = fast.nextnode.nextnode

        if slow == fast:
            return True

    return False
