# https://leetcode.com/problems/reorder-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        # Find middle using fast and slow pointers
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second part of the list
        current = slow
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Merge the lists
        list1 = head
        list2 = prev
        while list2.next:
            temp = list1.next
            list1.next = list2
            list1 = temp
            temp = list2.next
            list2.next = list1
            list2 = temp
