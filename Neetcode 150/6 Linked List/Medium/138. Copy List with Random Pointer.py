# https://leetcode.com/problems/copy-list-with-random-pointer/description/
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        node_map = {None: None}  # {old Node: new Node}

        pointer = head
        while pointer:
            node_map[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:
            copy = node_map[pointer]
            copy.next = node_map[pointer.next]
            copy.random = node_map[pointer.random]
            pointer = pointer.next

        return node_map[head]
