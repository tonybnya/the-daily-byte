"""
Remove Nth to Last Node

This question is asked by Facebook.
Given a linked list and a value n, remove the nth to last node
and return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
"""

from __future__ import annotations

from singly_linked_list import ListNode


# Runtime: O(n)
# Extra Memory Space: O(1)
def remove_nth_to_last_node(lst: ListNode, n: int) -> ListNode:
    """Remove nth to last node."""
    dummy: ListNode = ListNode()
    dummy.nextnode = lst

    left: ListNode = dummy
    right: ListNode = lst

    while n > 0 and right:
        right = right.nextnode
        n -= 1

    while right:
        left = left.nextnode
        right = right.nextnode

    left.nextnode = left.nextnode.nextnode

    return dummy.nextnode
