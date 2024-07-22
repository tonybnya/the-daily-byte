"""
Find Middle Element

This question is asked by Amazon.
Given a non-empty linked list, return the middle node of the list.
If the linked list contains an even number of elements,
return the node closer to the end.
Ex: Given the following linked lists...

1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
"""

from __future__ import annotations

from singly_linked_list import ListNode


def find_middle_node(head: ListNode | None) -> ListNode | None:
    """Find the middle node."""
    if head is None:
        return head

    fast: ListNode | None = head
    slow: ListNode | None = head

    while fast and fast.nextnode:
        slow = slow.nextnode
        fast = fast.nextnode.nextnode

    return slow
