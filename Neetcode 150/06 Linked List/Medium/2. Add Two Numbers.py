# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            pointer.next = ListNode(val=((v1 + v2 + carry) % 10))
            carry = (v1 + v2 + carry) // 10
            pointer = pointer.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
