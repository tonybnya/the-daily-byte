"""
Return Start of Cycle

This question is asked by Apple.
Given a potentially cyclical linked list where each value is unique,
return the node at which the cycle starts.
If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""

from __future__ import annotations

from singly_linked_list import ListNode


def linked_list_cycle(head: ListNode | None) -> ListNode | None:
    """Return the node at which the cycle starts."""
    if head is None:
        return head

    slow: ListNode | None = head
    fast: ListNode | None = head

    while fast is not None and fast.nextnode is not None:
        slow = slow.nextnode
        fast = fast.nextnode.nextnode
        if slow == fast:
            break

    if fast is None or fast.nextnode is None:
        return None

    slow = head
    while slow != fast:
        slow = slow.nextnode
        fast = fast.nextnode

    return slow
