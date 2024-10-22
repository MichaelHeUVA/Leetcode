# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=float("inf"), next=head)
        prev = dummy
        while head:
            if prev.val == head.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
