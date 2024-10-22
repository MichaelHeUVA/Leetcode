# https://leetcode.com/problems/swap-nodes-in-pairs/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pointer = dummy
        while pointer and pointer.next and pointer.next.next:
            pointer_next = pointer.next
            pointer_next_next = pointer_next.next
            pointer.next = pointer_next_next
            temp = pointer_next_next.next
            pointer_next_next.next = pointer_next
            pointer_next.next = temp
            pointer = pointer_next

        return dummy.next
