# https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2024-09-08
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        count = 0
        pointer = head
        while pointer:
            count += 1
            pointer = pointer.next
        output = []
        pointer = head
        groups = count // k
        remainder = count % k
        for i in range(k):
            part_head = pointer
            size = groups
            if remainder:
                size += 1
                remainder -= 1
            for _ in range(size - 1):
                pointer = pointer.next
            if pointer:
                temp = pointer.next
                pointer.next = None
                pointer = temp
            output.append(part_head)
        return output
