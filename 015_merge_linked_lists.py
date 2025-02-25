"""
Merge Linked Lists

This question is asked by Apple.
Given two sorted linked lists, merge them together in ascending order
and return a reference to the merged list.

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

1-2-3 4-5-6 1-2-3-4-5-6
1-3-5 2-4-6 1-2-3-4-5-6
4-4-7 1-5-6 1-4-4-5-6-7
"""

from __future__ import annotations

from singly_linked_list import SLL, ListNode


# Runtime: O(m+n)
# Extra Memory Space: O(1)
def merge_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """Merge two Linked Lists."""
    dummy: ListNode | None = ListNode()
    curr: ListNode | None = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.nextnode = l1
            l1 = l1.nextnode
        else:
            curr.nextnode = l2
            l2 = l2.nextnode

        curr = curr.nextnode

    curr.nextnode = l1 if l1 else l2

    return dummy.nextnode


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        list1_str, list2_str, merged_list_str = line.strip().split()

        list1: list[int] = [int(x) for x in list1_str.split("-")]
        list2: list[int] = [int(x) for x in list2_str.split("-")]
        expected_merged_list: list[int] = [int(x) for x in merged_list_str.split("-")]

        l1: SLL = SLL()
        l2: SLL = SLL()
        expected_ll: SLL = SLL()

        for x in list1:
            l1.insert_node(x)

        for x in list2:
            l2.insert_node(x)

        for x in expected_merged_list:
            expected_ll.insert_node(x)

        merged: SLL = merge_linked_lists(l1, l2)
        merged.print_sll()

        print()
