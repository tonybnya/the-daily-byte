"""
Definition of a Singly Linked List.
"""

from __future__ import annotations


class ListNode:
    """Define a node."""

    def __init__(self, val: int = 0, nextnode: ListNode | None = None) -> None:
        """Initialize the Singly Linked List."""
        self.val: int = val
        self.nextnode: ListNode | None = nextnode


class SLL:
    """Define a Singly Linked List."""

    def __init__(self):
        """Initialize the Singly Linked List."""
        self.head: ListNode | None = None
        self.length: int = 0

    def insert_node(self, val: int) -> None:
        """Insert a new node with the value `val`."""
        node: ListNode = ListNode(val)

        if self.head:
            temp: ListNode = self.head
            while temp.nextnode:
                temp = temp.nextnode

            temp.nextnode = node
        else:
            self.head = node

        self.length += 1

    def print_sll(self) -> None:
        """Print the Singly Linked List."""
        temp: ListNode | None = self.head

        while temp:
            if temp.nextnode is None:
                print(f"{temp.val} -> null")
            else:
                print(f"{temp.val} -> ", end="")

            temp = temp.nextnode
