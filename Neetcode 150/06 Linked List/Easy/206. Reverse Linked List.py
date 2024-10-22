# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev
