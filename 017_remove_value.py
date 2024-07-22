"""
Remove Value

This question is asked by Google.
Given a linked list and a value, remove all nodes containing the provided value,
and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
"""

from __future__ import annotations

from singly_linked_list import ListNode


def remove_value(head: ListNode | None, val: int) -> ListNode | None:
    """Remove all nodes containing the value `val`."""
    if head is None:
        return head

    dummy: ListNode | None = ListNode(0, head)
    slow: ListNode | None = dummy
    fast: ListNode | None = head

    while fast:
        if fast.val == val:
            fast = fast.nextnode
            slow.nextnode = fast
        else:
            slow = fast
            fast = fast.nextnode

    head = dummy.nextnode
    return head
